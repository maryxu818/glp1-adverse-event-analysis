#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GLP-1 Adverse Event Reporting Analysis

This project analyzes publicly available GLP-1 adverse event reports to compare
weight-related reporting share, female representation, and average reported age
across seven GLP-1 receptor agonists.

@author: Lanxin Xu
"""

import pandas as pd

# Load data
df = pd.read_csv("adverse_events_summary.csv")
# Select weight-related reactions
weight_df = df[df["reaction"].isin([
    "Weight decreased",
    "Abnormal loss of weight"
])].copy()

# Calculate weight-related reporting share
weight_summary = (
    weight_df.groupby("generic_name", as_index=False)["report_count"]
    .sum()
    .rename(columns={"report_count": "weight_related_reports"})
)

total_reports = (
    df.groupby("generic_name", as_index=False)["report_count"]
    .sum()
    .rename(columns={"report_count": "total_reports"})
)

result = weight_summary.merge(total_reports, on="generic_name")

result["weight_related_rate_pct"] = (
    result["weight_related_reports"]
    / result["total_reports"]
    * 100
).round(2)

# Calculate weighted female percentage
weight_df["female_reports"] = (
    weight_df["report_count"] * weight_df["pct_female"]
)

female_summary = (
    weight_df.groupby("generic_name", as_index=False)
    .agg(
        total_weight_reports=("report_count", "sum"),
        female_reports=("female_reports", "sum")
    )
)

female_summary["female_pct"] = (
    female_summary["female_reports"]
    / female_summary["total_weight_reports"]
    * 100
).round(2)

# Calculate weighted average age
age_df = weight_df.dropna(subset=["median_age"]).copy()

age_df["weighted_age"] = (
    age_df["median_age"] * age_df["report_count"]
)

age_summary = (
    age_df.groupby("generic_name", as_index=False)
    .agg(
        reports_with_age=("report_count", "sum"),
        weighted_age=("weighted_age", "sum")
    )
)

age_summary["avg_age"] = (
    age_summary["weighted_age"]
    / age_summary["reports_with_age"]
).round(1)

# Combine results
final_df = (
    result
    .merge(
        female_summary[["generic_name", "female_pct"]],
        on="generic_name",
        how="left"
    )
    .merge(
        age_summary[["generic_name", "avg_age"]],
        on="generic_name",
        how="left"
    )
    .sort_values("weight_related_rate_pct", ascending=False)
)

print(final_df)

# Save results
final_df.to_csv("glp1_weight_analysis.csv", index=False)