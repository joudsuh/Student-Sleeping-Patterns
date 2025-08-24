# Student Sleeping Patterns

Analyze how students' sleep habits relate to study time, activity, and other factors. 
This repo includes a clean, reproducible pipeline and example models (Random Forest and Logistic Regression).

## Project Structure
```text
student-sleeping-patterns/
├─ src/
│  └─ main.py                # training & evaluation script
├─ data/
│  └─ student_sleep_patterns.csv
├─ reports/
│  ├─ confusion_matrix_rf.png
│  └─ confusion_matrix_lr.png
├─ requirements.txt
├─ .gitignore
└─ README.md
```

## Quickstart
1) (Optional) Create a virtual env
```bash
# Windows
python -m venv venv && venv\Scripts\activate
# macOS/Linux
python3 -m venv venv && source venv/bin/activate
```

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) Run
```bash
python src/main.py
```

The script will print accuracy and a classification report for two models and save confusion matrices in `reports/`.

## Notes
- The script automatically drops `Student_ID` if present (identifier, not a predictive feature).
- Categorical features are one-hot encoded; numeric features are standardized.
- Train/test split is stratified by `Sleep_Quality`.