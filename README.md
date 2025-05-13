
# 🧠 Mental Health in Tech: A Multi-Year Analysis

## 📌 Introduction

Mental well-being has grown to be a more significant issue in today's workplace, particularly in the high-speed and demanding atmosphere of the tech sector. Workers frequently endure extended hours, solitude, exhaustion, and restricted availability of mental health services, all of which can greatly affect their wellness. This initiative examines mental health patterns in tech workers through survey data from Open Sourcing Mental Illness (OSMI) gathered from 2017 to 2021. The aim is to reveal trends in awareness, support, diagnosis, and risk factors over time, while also pinpointing the demographics most impacted by mental health issues.

The project encompasses an entire data science pipeline—from data preprocessing and exploratory analysis to unsupervised clustering, risk classification, and supervised machine learning models. Moreover, a semantic chatbot was created to enable users to interactively ask for key insights from the data. This research seeks to inform employers, researchers, and policymakers about mental health in the tech industry by integrating statistical analysis with machine learning and NLP methods, offering practical recommendations for building healthier and more supportive work environments.

## 📊 Datasets

- OSMI Mental Health in Tech Survey (2017–2021)

## 🛠 System Design

1. **Data Preprocessing**
2. **Exploratory Data Analysis (EDA)**
3. **Feature Selection**
4. **Predictive Modeling**
5. **Risk Indicator Modeling (Clustering)**
6. **Trend Analysis – Pre vs. Post COVID**
7. **Chatbot - Mental health Recommendation and Risk Indication**

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

### Chatbot - Mental Health Recommendations and Risk Indication

This chatbot aims to respond to user inquiries by consulting findings from a mental health EDA (Exploratory Data Analysis) summary document. It starts by reading the content of eda_summary.txt and dividing it into clear, significant lines. Each line is subsequently transformed into a numerical vector with the help of a pre-trained HuggingFace sentence transformer model (all-MiniLM-L6-v2). These vectors are organized utilizing FAISS, a quick and effective similarity search tool, enabling the chatbot to comprehend semantically and look for related content.

When a user asks a question, the chatbot conducts a similarity search in the FAISS index to locate the top 5 most pertinent text snippets from the EDA summary. It eliminates duplicate or excessively similar responses by employing fuzzy string matching (SequenceMatcher) and chooses a maximum of two varied and pertinent replies. If no significant matches are discovered, the chatbot provides a warm fallback response that suggests general mental health assistance. This design enables the chatbot to deliver succinct, human-like responses grounded in actual data insights, rendering it a useful partner for examining mental health trends and discoveries obtained from EDA

## 📌 Conclusion

This initiative successfully integrates data science methods with actual mental health data to offer analytical insights and useful tools. By meticulously cleaning data, performing feature engineering, and applying encoding, a solid groundwork was established for in-depth analysis of trends and patterns in employee mental health over a span of five years. Clustering alongside a tailored risk scoring system provided clear insights into risk levels across various demographic categories, whereas predictive modeling delivered precise diagnosis forecasts through machine learning. The chatbot feature introduced an interactive dimension, enabling users to engage with results in a conversational manner through semantic search. Overall, the project emphasizes mental health issues within the tech sector while also offering a scalable, data-oriented strategy to enhance awareness, facilitate early detection, and promote better decision-making.

## 📌Summary

We started by exploring mental health survey data collected between 2017 and 2021 to understand key patterns—like how family history, remote work, and lack of support at work impact mental well-being. After analyzing the data, we summarized the most important insights in simple, easy-to-read text.

Instead of letting that information sit in a report, we turned it into something interactive—a chatbot. Using HuggingFace models, we converted the summary into vector embeddings and stored them with FAISS so the chatbot could search and respond to questions in a smart, relevant way.

We wrote logic to handle user questions, pick the most meaningful answers, and even offer general mental health tips if no direct match was found. Then, we built a clean, user-friendly web app using Streamlit so anyone could talk to the chatbot in real time.

In the end, we turned complex data analysis into a helpful, human-like tool that makes mental health insights more accessible and supportive.

Contributors:
Sai Varun Nimmagadda,
Shaheen Chirakula,
Vishnu Vikas Nallamalli.
---
