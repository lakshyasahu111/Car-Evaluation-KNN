---

# 🚗 Car Evaluation Predictor (KNN)

A machine learning project that uses the **K-Nearest Neighbors (KNN)** algorithm to classify the acceptability of cars based on several technical and price-related attributes.

## 📊 Dataset Overview

The **Car Evaluation Dataset** is a classic multi-attribute decision-making dataset from the UCI Machine Learning Repository.

* **Source:** [UCI Machine Learning Repository - Car Evaluation](https://archive.ics.uci.edu/dataset/19/car+evaluation)
* **Instances:** 1,728
* **Attributes:** 6 categorical features
* **Target:** `class` (unacc, acc, good, vgood)

### Features Description:

| Feature | Description | Values |
| --- | --- | --- |
| `buying` | Buying price | vhigh, high, med, low |
| `maint` | Price of maintenance | vhigh, high, med, low |
| `doors` | Number of doors | 2, 3, 4, 5-more |
| `persons` | Capacity (persons) | 2, 4, more |
| `lug_boot` | Size of luggage boot | small, med, big |
| `safety` | Estimated safety | low, med, high |

---

## 🧠 Model Explanation: K-Nearest Neighbors

This project implements **KNN**, a non-parametric classification algorithm.

**How it works:**
The model classifies a car by looking at the  most similar cars in the training data (its "neighbors"). It calculates the "distance" between car attributes to determine similarity.

We use **Euclidean Distance** to find the closest points:


---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed. You will need the following libraries:

```bash
pip install numpy pandas scikit-learn

```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

```


2. Run the script:
```bash
python KNN.py

```



---

## 🛠 Project Structure

```text
.
├── KNN.py                 # Main Python script for training and evaluation
├── car+evaluation/
│   └── car.data           # The raw dataset file
└── README.md              # Project documentation

```

## 📈 Results

The model's performance is measured using **Accuracy Score**.

* **Current Accuracy:** ~80-90% (Depending on K-value and feature selection)
* **Preprocessing:** Used `LabelEncoder` to convert categorical text data into numerical values for mathematical processing.

---


---

**Next Step:** Since your code currently only uses 3 features (`buying`, `main`, `safety`), would you like me to help you update the script to use **all 6 features**? This usually jumps the accuracy from ~80% to over 95%!
