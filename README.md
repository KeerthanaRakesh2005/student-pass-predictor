# Student Pass/Fail Prediction using Decision Tree

## Project Overview
This machine learning project predicts whether a student will pass or fail based on:

- Study Hours
- Attendance
- Sleep Hours
- Assignments Completed

The project uses a Decision Tree Classifier from scikit-learn.

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

---

## Machine Learning Concepts Used

- Supervised Learning
- Classification
- Decision Tree
- Gini Index
- Train-Test Split
- Accuracy Score

---

## Project Structure

```text
student-pass-predictor/
│
├── data/
│   └── student_data.csv
│
├── src/
│   └── train_model.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run

### 1. Clone Repository

```bash
git clone <your-github-link>
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

#### Windows
```bash
venv\Scripts\activate
```

#### Mac/Linux
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Project

```bash
python src/train_model.py
```

---

## Model Accuracy

Current Accuracy:
```text
1.0
```

---

## Future Improvements

- Add larger dataset
- Prevent overfitting
- Add Streamlit web app
- Compare with other ML algorithms
- Deploy model online