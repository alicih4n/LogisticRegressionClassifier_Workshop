# Logistic Regression Classifier Workshop

## Team Section (Group 2)

### Lead Developer
- **Ali Cihan Ozdemir** (Student Number: 9091405)

### Contributor
- **Danda, Lohith Reddy** (Student Number: 9054470)

### Note
**Roshan Bartaula** did not attend any classes and provided zero contribution to this project.

---

## Project Overview

This project implements a Logistic Regression classifier to predict Pass/Fail outcomes based on study hours. It serves as a foundational workshop for understanding statistical classification, binary classification metrics, and real-time data streaming.

## Features

- **Logistic Regression Model**: Using scikit-learn's LogisticRegression
- **Modular Pipeline**: load_data(), preprocess_data(), train_model(), evaluate_model()
- **SQLite Database**: Persistent storage for historical study records
- **Real-time Streaming**: Reads one record every 2 seconds
- **Dynamic Dashboard**: IPyWidgets-based real-time visualization
- **Complete Metrics**: Accuracy, Log-Loss, Confusion Matrix

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd LogisticRegressionClassifier_Workshop
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Enable Jupyter widgets:
```bash
jupyter nbextension enable --py widgetsnbextension
```

## Usage

Open and run the Jupyter notebook:
```bash
jupyter notebook LogisticRegressionClassifier_Workshop.ipynb
```

## Project Structure

```
LogisticRegressionClassifier_Workshop/
├── LogisticRegressionClassifier_Workshop.ipynb  # Main notebook
├── requirements.txt                              # Dependencies
└── README.md                                     # This file
```

## Technical Details

- **Database**: SQLite (study_records table)
- **Model**: scikit-learn LogisticRegression
- **Visualization**: matplotlib + IPyWidgets
- **Streaming**: 2-second interval data processing

## License

This project is for educational purposes as part of CSCN8010 coursework.
