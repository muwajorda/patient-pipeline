# Patient Pipeline (Nextflow + Docker + CI/CD)

## Overview
A reproducible bioinformatics-style pipeline simulating NGS data processing from ETL to QC, alignment, and counts using Nextflow.

## Features
- Modular pipeline design (QC, Alignment, Counts)
- Containerized execution using Docker
- CI/CD via GitHub Actions
- ETL-based manifest validation
- nf-core inspired structure

## Architecture

ETL Manifest → QC → Alignment → Counts → Results

## Tech Stack
- Nextflow
- Docker
- GitHub Actions
- Python (ETL preprocessing)

## How to Run

```bash
nextflow run nextflow/main.nf -with-docker patient-pipeline:latest
