# Student Sleeping Patterns 💤

Analyze and visualize student sleeping behaviors to uncover patterns that affect focus, grades, and well-being.

## Repository Structure
.
├─ data/
│ ├─ raw/ # original data (not committed)
│ ├─ processed/ # cleaned data (not committed)
│ └─ sample.csv # tiny sample included for demo
├─ notebooks/ # analysis notebooks (add as needed)
├─ src/ # reusable Python modules
│ ├─ data_prep.py
│ ├─ features.py
│ └─ viz.py
├─ reports/
│ └─ figures/
├─ requirements.txt
├─ README.md
├─ .gitignore
└─ LICENSE
## Quickstart

```bash
pip install -r requirements.txt

from src.data_prep import load_sample, clean
df = load_sample("data/sample.csv")
df = clean(df)
print(df.head())
