nextflow.enable.dsl=2

include { QC_CHECK } from './modules/qc/main.nf'
include { ALIGN_READS } from './modules/alignment/main.nf'
include { GENERATE_COUNTS } from './modules/counts/main.nf'

params.test = false

workflow {

    def manifest = params.test ?
        "test_data/test_manifest.csv" :
        "data/validated_manifest.csv"

    samples_ch = Channel
        .fromPath(manifest)
        .splitCsv(header: true)
        .map { row ->

            def fq1 = file(row.fastq_1)

            // ✅ NO NULLS — use list instead
            def reads = row.fastq_2?.trim() ?
                [fq1, file(row.fastq_2)] :
                [fq1]

            tuple(row.sample_id, reads)
        }

    // QC branch
    qc_results = QC_CHECK(samples_ch)

    // Alignment branch (reuse same channel safely)
    bam_results = ALIGN_READS(samples_ch)

    // Counts
    counts_results = GENERATE_COUNTS(bam_results)
}
