
# 🧠 Mental Health in Tech: A Multi-Year Analysis

## 📌 Introduction

The tech industry has long been associated with fast-paced environments, high workloads, and burnout risks. This study explores the mental health landscape of tech professionals using survey data from the Open Sourcing Mental Illness (OSMI) organization, covering the years 2017 to 2021. The goal is not just to predict the likelihood of mental health diagnoses among employees, but also to identify key workplace and personal factors that influence well-being.

This project combines predictive modeling and clustering techniques to build a diagnostic model and a risk indicator. Additionally, a multi-year trend analysis is performed to examine shifts in mental health perceptions and support — particularly in response to COVID-19, which significantly altered work culture and stress factors globally.

## 📊 Datasets

- OSMI Mental Health in Tech Survey (2017–2021)

## 🛠 System Design

1. **Data Preprocessing**
2. **Exploratory Data Analysis (EDA)**
3. **Feature Selection**
4. **Predictive Modeling**
5. **Risk Indicator Modeling (Clustering)**
6. **Trend Analysis – Pre vs. Post COVID**

## 🔧 Preprocessing

- Dropped columns with >50% missing values
- Imputed remaining missing data
- Handled categorical inconsistencies
- Treated numerical outliers
- Encoded data for modeling

## 🔍 Predicting Mental Health Diagnosis

This binary classification task predicts whether an employee has been diagnosed with a mental health condition.

**Models Evaluated:**

1. K-Nearest Neighbors (Best performer: 86.34% Accuracy)
2. Logistic Regression
3. Decision Tree
4. Random Forest
5. AdaBoost
6. Gradient Boosting
7. XGBoost

**Evaluation:**

- Train/Test Split: 70/30
- Metrics: Accuracy, F1 Score, Precision, Recall, ROC AUC
- K-Fold Cross Validation applied

## 📈 Risk Indicator (Clustering)

Clustering methods were used to group employees by mental health risk levels (Low, Medium, High).

**Clustering Models:**

- K-Means, K-Means++
- PAM (Partition Around Medoids)
- Agglomerative Clustering
- Spectral Clustering
- Gaussian Mixture Models
- BIRCH

**Evaluation Metrics:**

- Silhouette Score
- Calinski-Harabasz Index
- SSE

## 💡 Key Inferences

### Influential Factors:
- Willingness to discuss mental health at work
- Employer support and resources
- Personal history of mental illness
- Age, gender, and tech industry status

### Pre/Post COVID Trends:
- More formal discussions and support post-COVID
- Increased mental health awareness
- Greater work-from-home related stress factors

## 📌 Conclusion

This project not only predicts mental health diagnoses but also uncovers workplace patterns that contribute to mental health challenges. The insights can help tech organizations implement proactive mental health strategies.

---
