import json
import csv


INPUT_FILE = "data/cleaned_samples.json"
OUTPUT_FILE = "data/validated_manifest.csv"


def generate_manifest():

    with open(INPUT_FILE, "r") as f:
        samples = json.load(f)

    validated_samples = [
        s for s in samples
        if s.get("status") == "validated"
    ]

    with open(OUTPUT_FILE, "w", newline="") as csvfile:

        fieldnames = [
            "sample_id",
            "patient_id",
            "assay",
            "genome",
            "fastq_1",
            "fastq_2",
            "tissue",
            "quality_score"
        ]

        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for sample in validated_samples:

            writer.writerow({
                "sample_id": sample.get("sample_id"),
                "patient_id": sample.get("patient_id"),
                "assay": sample.get("assay"),
                "genome": sample.get("genome"),
                "fastq_1": sample.get("fastq_1"),
                "fastq_2": sample.get("fastq_2"),
                "tissue": sample.get("tissue"),
                "quality_score": sample.get("quality_score")
            })

    print(
        f"Manifest generated with "
        f"{len(validated_samples)} validated samples"
    )


if __name__ == "__main__":
    generate_manifest()
