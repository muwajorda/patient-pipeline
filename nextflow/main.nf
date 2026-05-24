nextflow.enable.dsl=2

params.outdir = "/Users/jordanamuwanguzi/Desktop/patient_Pipeline/results"


params.manifest = "/Users/jordanamuwanguzi/Desktop/patient_Pipeline/data/validated_manifest.csv"


process QC_CHECK {

    publishDir "${params.outdir}/qc", mode: 'copy'

    input:
    val row

    output:
    tuple val(row), path("${row.sample_id}_qc.txt")

    script:
    """
    echo "QC PASSED" > ${row.sample_id}_qc.txt
    echo "Sample: ${row.sample_id}" >> ${row.sample_id}_qc.txt
    echo "Assay: ${row.assay}" >> ${row.sample_id}_qc.txt
    """
}


process ALIGN_READS {

    publishDir "${params.outdir}/alignment", mode: 'copy'

    input:
    tuple val(row), path(qc_file)

    output:
    tuple val(row), path("${row.sample_id}.bam")

    script:
    """
    echo "Simulated BAM file" > ${row.sample_id}.bam
    echo "Aligned to ${row.genome}" >> ${row.sample_id}.bam
    """
}


process GENERATE_COUNTS {

    publishDir "${params.outdir}/counts", mode: 'copy'

    input:
    tuple val(row), path(bam)

    output:
    path("${row.sample_id}_counts.txt")

    script:
    """
    echo "GeneA 120" > ${row.sample_id}_counts.txt
    echo "GeneB 88" >> ${row.sample_id}_counts.txt
    echo "GeneC 201" >> ${row.sample_id}_counts.txt
    """
}


workflow {

    samples_ch = Channel
        .fromPath(params.manifest)
        .splitCsv(header: true)

    qc_results = QC_CHECK(samples_ch)

    aligned = ALIGN_READS(qc_results)

    GENERATE_COUNTS(aligned)
}
