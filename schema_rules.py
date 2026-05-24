VALID_ASSAYS = {
    "rna_seq": "RNA-seq",
    "rnaseq": "RNA-seq",
    "rna-seq": "RNA-seq",
    "atacseq": "ATAC-seq",
    "atac-seq": "ATAC-seq",
    "chipseq": "ChIP-seq",
    "chip-seq": "ChIP-seq"
}

VALID_GENOMES = {
    "hg19": "GRCh37",
    "grch37": "GRCh37",
    "hg38": "GRCh38",
    "grch38": "GRCh38"
}

REQUIRED_FIELDS = [
    "sample_id",
    "patient_id",
    "assay",
    "genome",
    "fastq_1"
]
