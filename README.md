# Student Sleeping Patterns 💤

Analyze and visualize student sleeping behaviors to uncover patterns that affect focus, grades, and well-being. This repository includes cleaned data, notebooks, and reproducible analysis for exploring relationships between bedtime, wake time, study load, caffeine, and academic performance.

## 🔍 Key Questions
- What are the typical sleep durations and chronotypes among students?
- How do bedtime/wake time correlate with GPA or self-reported focus?
- Which factors (caffeine, screen time, workload) are most associated with poor sleep?

## 🗂️ Repository Structure
.
├─ data/
│ ├─ raw/ # original data (KEEP OUT of git if large/private)
│ ├─ processed/ # cleaned datasets
│ └─ sample.csv # small sample for demo/repro
├─ notebooks/
│ ├─ 01_explore.ipynb # EDA: distributions, missingness, outliers
│ ├─ 02_clean.ipynb # cleaning, feature engineering
│ └─ 03_model.ipynb # simple models / correlations
├─ src/
│ ├─ data_prep.py # functions for cleaning/validation
│ ├─ features.py # feature engineering helpers
│ └─ viz.py # plotting utilities
├─ reports/
│ └─ figures/ # exported charts
├─ requirements.txt
├─ .gitignore
└─ LICENSE
