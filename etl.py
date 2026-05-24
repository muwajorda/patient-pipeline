import json

from schema_rules import (
    VALID_ASSAYS,
    VALID_GENOMES,
    REQUIRED_FIELDS
)

from utils import setup_logger

logger = setup_logger()


def calculate_quality_score(sample, errors):

    score = 100

    score -= 15 * sum(
        1 for f in REQUIRED_FIELDS if not sample.get(f)
    )

    if sample.get("assay", "").lower() not in VALID_ASSAYS:
        score -= 20

    if sample.get("genome", "").lower() not in VALID_GENOMES:
        score -= 20

    if not sample.get("fastq_1"):
        score -= 25

    return max(score, 0)


def validate_sample(sample):

    errors = []

    sample_id = sample.get("sample_id", "UNKNOWN")

    logger.info(f"Processing {sample_id}")

    # Required field validation
    for field in REQUIRED_FIELDS:
        if not sample.get(field):
            errors.append(f"Missing required field: {field}")

    # Assay normalization
    assay_raw = (sample.get("assay") or "").lower()

    if assay_raw in VALID_ASSAYS:
        sample["assay"] = VALID_ASSAYS[assay_raw]
    else:
        errors.append(
            f"Invalid assay type: {sample.get('assay')}"
        )

    # Genome normalization
    genome_raw = (sample.get("genome") or "").lower()

    if genome_raw in VALID_GENOMES:
        sample["genome"] = VALID_GENOMES[genome_raw]
    else:
        errors.append(
            f"Unknown genome build: {sample.get('genome')}"
        )

    # Tissue cleanup
    if not sample.get("tissue"):
        sample["tissue"] = "unknown"

    # Score
    quality_score = calculate_quality_score(sample, errors)

    sample["quality_score"] = quality_score

    # Status
    if errors:
        sample["status"] = "needs_review"
        logger.warning(f"{sample_id} failed validation")
    else:
        sample["status"] = "validated"
        logger.info(f"{sample_id} validated")

    return sample, errors


def run_etl():

    with open("data/raw_samples.json", "r") as f:
        raw_data = json.load(f)

    cleaned_samples = []
    rejected_samples = []

    for sample in raw_data:

        validated_sample, errors = validate_sample(sample)

        validated_sample["errors"] = errors

        cleaned_samples.append(validated_sample)

        if errors:
            rejected_samples.append(validated_sample)

    with open("data/cleaned_samples.json", "w") as f:
        json.dump(cleaned_samples, f, indent=2)

    with open("data/rejected_samples.json", "w") as f:
        json.dump(rejected_samples, f, indent=2)

    logger.info("ETL complete")


if __name__ == "__main__":
    run_etl()
