# Statistical Classification and Logistic Regression

## CSCN8010 - Machine Learning Fundamentals

---

## 👥 Group 2 - Project Team

| Name | Role |
| :--- | :--- |
| **Ali Cihan Ozdemir** | Lead Developer & Presenter |
| **Lohith Reddy Danda** | Co-Developer & Presenter |
| **Roshan Bartaul** | Co-Developer & Presenter |

**Instructor:** Professor David

---

## 📽️ About This Project

This is the **Group 2 Presentation Project** for the CSCN8010 Machine Learning Fundamentals course. The project focuses on **Logistic Regression** - a fundamental statistical classification algorithm in machine learning.

### What This Project Does

This presentation covers the complete journey of understanding and implementing Logistic Regression:

1. **Introduction to Statistical Classification** - Understanding classification problems
2. **The Problem with Linear Regression** - Why we can't use linear regression for classification
3. **The Sigmoid Function** - The mathematical solution for probability estimation
4. **Building a Logistic Regression Model** - Hands-on implementation with scikit-learn
5. **Log-Loss (Cross-Entropy)** - Understanding model loss and confidence
6. **Evaluation Metrics** - Accuracy, Precision, Recall, F1-Score, Confusion Matrix

---

## 🎯 Project Purpose

### General Purpose
To educate and demonstrate the fundamentals of Logistic Regression as a binary classification technique, showing why it's essential for machine learning and how it differs from linear regression.

### Detailed Purpose
- **Explain** the mathematical foundations of logistic regression
- **Demonstrate** practical implementation using Python and scikit-learn
- **Visualize** key concepts like sigmoid curves, decision boundaries, and loss functions
- **Evaluate** model performance using industry-standard metrics

---

## 📁 Project Files

| File | Description |
|:-----|:------------|
| **Group2_LogisticRegression_Presentation.ipynb** | Main presentation notebook (use this for Teams meeting) |
| Group2_LogisticRegression_Assignment.ipynb | Assignment notebook with tasks |
| requirements.txt | Python dependencies |
| README.md | This file |

---

## 🚀 How to Run the Presentation

### Step 1: Clone the Repository
```bash
git clone https://github.com/alicih4n/LogisticRegressionClassifier_Workshop.git
cd LogisticRegressionClassifier_Workshop
```

### Step 2: Install Dependencies
```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate on Mac/Linux
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Step 3: Run the Presentation Notebook
```bash
# Start Jupyter Notebook
jupyter notebook Group2_LogisticRegression_Presentation.ipynb
```

### Step 4: Present in Teams
1. Open `Group2_LogisticRegression_Presentation.ipynb`
2. Share your screen in Microsoft Teams
3. Run each cell with Shift+Enter as you explain
4. Use the live code demos to show predictions

---

## 📊 Presentation Agenda (40 Minutes)

| Section | Content | Duration |
|:--------|:--------|:---------|
| 1 | Introduction to Classification | ~3 min |
| 2 | Linear vs Logistic Regression | ~5 min |
| 3 | The Sigmoid Function | ~5 min |
| 4 | Building the Model (Code Demo) | ~7 min |
| 5 | Log-Loss Explanation | ~5 min |
| 6 | Evaluation Metrics | ~5 min |
| 7 | Live Prediction Demo | ~5 min |
| 8 | Q&A | ~5 min |

---

## ✅ Learning Objectives

By following this presentation, you will understand:

- ✅ Why logistic regression is needed for classification problems (not linear regression)
- ✅ How the sigmoid function transforms predictions into probabilities (0-1)
- ✅ How to build and train a logistic regression model
- ✅ What log-loss is and why it penalizes confident wrong predictions
- ✅ How to evaluate classification models using various metrics

---

## 🔑 Key Formulas

### Sigmoid Function
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

### Log-Loss (Cross-Entropy)
$$\text{LogLoss} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \cdot \log(p_i) + (1 - y_i) \cdot \log(1 - p_i) \right]$$

### Classification Rule
- If probability ≥ 0.5 → **Class 1** (Pass/Positive)
- If probability < 0.5 → **Class 0** (Fail/Negative)

---

## 📦 Requirements

```
numpy
matplotlib
scikit-learn
seaborn
pandas
jupyter
```

---

## 🙏 Acknowledgments

- **Professor David** - For the excellent course and guidance
- **Reference Repository** - For foundational materials
- **Group 5** - For peer review

---

## 📬 Contact

For questions about this project:
- Ali Cihan Ozdemir
- Lohith Reddy Danda  
- Roshan Bartaul

---

*This project was created for CSCN8010 - Machine Learning Fundamentals*
*Presented by Group 2*
*Instructor: Professor David*
