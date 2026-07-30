# GLP-1 Adverse Event Analysis

Python analysis of publicly available GLP-1 adverse event reports, focusing on weight-related reporting patterns across seven GLP-1 receptor agonists.

## Project Overview

This project analyzes the adverse event reporting data from the publicly available GLP-1 Weight Loss Drugs Master Dataset (2017–2026) to compare weight-related reporting patterns among GLP-1 receptor agonists. The analysis focuses on reporting share, female representation, and average reported age using Python and Pandas.
## Dataset

- **Source:** [GLP-1 Weight Loss Drugs Master Dataset (2017–2026)](https://www.kaggle.com/datasets/devtayyabsajjad/glp-1-weight-loss-drugs-master-dataset-2017-2026)
- **License:** CC0 Public Domain
- **Records:** 11,093 aggregated adverse event records
- **Drugs analyzed:** Semaglutide, Tirzepatide, Liraglutide, Dulaglutide, Exenatide, Lixisenatide, Albiglutide
- **Note:** The original dataset is not included in this repository due to file size. The processed analysis results (`glp1_weight_analysis.csv`) are provided.
  
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

- README.md — Project overview
- analysis.py — Data cleaning, aggregation, and reporting analysis
- glp1_weight_analysis.csv — Final analysis results

## Disclaimer

This project is intended for data analysis practice and portfolio purposes only. The results describe reporting patterns within the dataset and should not be interpreted as evidence of drug safety or effectiveness.
