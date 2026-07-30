# GLP-1 Adverse Event Analysis

Python analysis of publicly available GLP-1 adverse event reports, focusing on weight-related reporting patterns across seven GLP-1 receptor agonists.

## Project Overview

This project analyzes a publicly available adverse event dataset to compare weight-related reporting patterns among GLP-1 receptor agonists. The analysis focuses on reporting share, female representation, and average reported age using Python and Pandas.

## Dataset

- **Source:** Publicly available Kaggle dataset
- **Records:** 11,093 aggregated adverse event records
- **Drugs analyzed:** Semaglutide, Tirzepatide, Liraglutide, Dulaglutide, Exenatide, Lixisenatide, Albiglutide

## Objectives

- Identify weight-related adverse event reports.
- Calculate weight-related reporting share for each drug.
- Compare female representation using report-count weighted estimates.
- Compare report-count weighted average age across drugs.

## Tools

- Python
- Pandas
- NumPy
- Matplotlib

## Key Findings

- Exenatide showed the highest weight-related reporting share (3.32%) in the analyzed dataset.
- Female representation ranged from approximately 56% to 64% across most drugs.
- Average reported age ranged from approximately 56 to 63 years.

## Repository Structure

- README.md — Project overview and methodology
- analysis.py — Python script for data cleaning and analysis
- adverse_events_summary.csv — Original dataset
- glp1_weight_analysis.csv — Processed analysis results

## Disclaimer

This project is intended for data analysis practice and portfolio purposes only. The results describe reporting patterns within the dataset and should not be interpreted as evidence of drug safety or effectiveness.
