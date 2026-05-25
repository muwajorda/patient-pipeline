process GENERATE_COUNTS {

    tag "$sample_id"

    publishDir "results/counts", mode: 'copy'

    input:
    tuple val(sample_id), path(bam)

    output:
    tuple val(sample_id), path("${sample_id}_counts.txt")

    script:
    """
    echo "Generating counts for ${sample_id}" > ${sample_id}_counts.txt
    echo "geneA 10" >> ${sample_id}_counts.txt
    echo "geneB 5" >> ${sample_id}_counts.txt
    """
}
