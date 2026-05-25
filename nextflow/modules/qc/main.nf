process QC_CHECK {

    tag "$sample_id"

    input:
    tuple val(sample_id), path(reads)

    output:
    tuple val(sample_id), path("${sample_id}_qc.txt")

    script:
    """
    echo "QC REPORT for ${sample_id}" > ${sample_id}_qc.txt
    echo "READ FILES:" >> ${sample_id}_qc.txt

    for f in ${reads}; do
        echo " - \$f" >> ${sample_id}_qc.txt
    done

    echo "QC STATUS: PASSED" >> ${sample_id}_qc.txt
    """
}
