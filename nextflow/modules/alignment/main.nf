process ALIGN_READS {

    tag "$sample_id"

    input:
    tuple val(sample_id), path(reads)

    output:
    tuple val(sample_id), path("${sample_id}.bam")

    script:
    def is_paired = reads.size() > 1

    """
    echo "Aligning sample ${sample_id}" > align.log
    echo "READS: ${reads}" >> align.log

    if [ ${reads.size()} -eq 2 ]; then
        echo "PAIRED-END MODE"
    else
        echo "SINGLE-END MODE"
    fi

    touch ${sample_id}.bam
    """
}
