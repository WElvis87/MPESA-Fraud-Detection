# 🛡️ M-PESA Fraud Detection System

## 🎯 Problem Definition:

M-PESA is the primary digital payment platform in Kenya, processing millions of peer-to-peer, merchant, and bill payment transactions daily. Its widespread adoption has also made it a target for fraudulent activities, including social engineering scams, account takeovers, SIM-swap fraud, and abnormal transaction behavior.

## 📌 Project Overview

M-PESA Fraud Detection is a machine learning initiative designed to identify suspicious transaction patterns. By analyzing transaction metadata, user behavior, and historical fraud markers, the system distinguishes between legitimate financial activity and potential fraudulent attempts.

This project demonstrates:
- Synthetic and real-world financial data preprocessing
- Detection of anomalous transaction patterns
- Robust model evaluation for imbalanced datasets

The goal is to provide a Decision Support Tool for fintech security teams. By flagging high-risk transactions before they are finalized, stakeholders can mitigate financial loss and enhance user security.


## 📊 Motivation

Current fraud detection approaches often rely on rule-based systems and manual reviews, which struggle to adapt to evolving fraud patterns, generate a high number of false positives, and fail to scale with transaction volume. As a result, fraudulent transactions may go undetected, while legitimate users experience unnecessary transaction blocks and delays.

The core problem is the lack of a data-driven, adaptive system that can identify potentially fraudulent M-PESA transactions in near real time, while maintaining a low false-positive rate and providing interpretable risk signals for investigation teams.

## 🧠 What This Project Does.

The system treats fraud detection as a binary classification problem (Fraud vs. Legitimate).

Specifically, it:
 1.Analyzes Transaction Flow: Tracks amount, timing, and frequency of transfers.
 2.Flags Behavioral Anomalies: Detects sudden spikes in activity or unusual transfer destinations.
 3.Optimizes for Precision: Ensures that legitimate users are not unnecessarily blocked while catching the majority of fraud cases.

### 🗂️ Project Structure
```
C:.
│   .gitignore
│   requirements.txt
│   __init__.py
│
├───config
│       config.yaml
│
├───data
│       mpesa_transactions.csv
│
├───models
│       model.pk1
│
├───notebooks
│       mpesa.ipynb
│
├───reports
│       evaluation_report.md
│
├───src
│   │   clean_data.py
│   │   config.py
│   │   data_split.py
│   │   load_data.py
│   │   pipeline.py
│   │   train_model.py
│   │   __init__.py
│   │
│   ├───mpesa_fraud.egg-info
│   │       dependency_links.txt
│   │       PKG-INFO
│   │       SOURCES.txt
│   │       top_level.txt
│   │
│   └───__pycache__
│           clean_data.cpython-313.pyc
│           clean_data.cpython-314.pyc
│           config.cpython-313.pyc
│           data_split.cpython-313.pyc
│           load_data.cpython-313.pyc
│           train_model.cpython-313.pyc
│           __init__.cpython-313.pyc
│           __init__.cpython-314.pyc
│
└───tests
        conftest.py
        test_config.py
        test_data_clean.py
        test_data_load.py
        test_data_split.py
        test_model_testing.py
```

---


## 🧰 Dataset

### 📥 Source
Due to the unavailability of publicly accessible M-PESA transaction data, this project uses a publicly available financial transaction dataset as a proxy to simulate M-PESA-like transaction behavior.

✅ PaySim Dataset
This is the gold standard for mobile money fraud research.

It contains:
1. A synthetic dataset generated from real mobile money transaction patterns
2. Widely cited in academic research
3. Explicitly designed to simulate M-PESA-like systems

This approach ensures:
1. Ethical data usage
2. Reproducibility
3. Realistic

🔍 Data Inputs: What the Model Uses

Each row in the dataset represents a single transaction, including:
Transaction type (TRANSFER, CASH_OUT, PAYMENT or DEBIT)
Transaction amount
Sender and receiver balances before and after transaction
Sender and receiver IDs
Balance differences between transactions
Fraud label (for supervised learning)


## 🧪 Modeling Approach: Why Machine Learning
Baseline problem
Problem Characteristics
1. Fraud cases are extremely rare (high class imbalance)
2. Fraud patterns evolve over time
3. Simple rules are insufficient
   
The ML Solution This project uses XGBoost because it:
1. Handle imbalanced data effectively (using scale_pos_weight).
2. Detect complex interactions (e.g., a specific transaction type + a specific hour + a high amount).
3. The model is trained to prioritize Recall—it is better to flag a suspicious transaction for review than to let a fraudster drain an account.

The model is trained on:
Pay Sim data with the column of "isFraud" being used as the target column.

## 📏 Evaluation: How We Know the Model Works

Predictions are evaluated using classification metrics because the model is predicting binary values on wherether a transaction is fraudulent(1) or not (0).

### Primary metrics:

1. Recall (Sensitivity): What percentage of all actual frauds did we catch?
2. Precision: When we flag a transaction as fraud, how often are we right?
3. F1-Score: The balance between Precision and Recall.
4. Confusion Matrix: To visualize False Positives vs. False Negatives.

📈 As a result:

This project enables proactive security measures:
1. Automated Flagging: Instant alerts for transactions with high fraud probability.
2. Threshold Setting: Custom "risk scores" that allow banks to decide when to require an extra OTP or call the user.
3. Mule Account Discovery: Identifying accounts that act as clearing houses for stolen funds.


## ⚠️ Limitations

This project explicitly acknowledges limitations:

1. Synthetic proxy data, not real M-PESA logs
2. No social or SIM-swap context
3. Fraud labels are simulated

Despite this, the modeling approach and pipeline are directly transferable to real mobile money systems.

## 🚀 Installation

### 🔧 Requirements  
Make sure Python (3.8+) is installed.

```bash
# Clone repository
git clone https://github.com/WElvis87/MPESA-Fraud-Detection.git
cd MPESA-Fraud-Detection

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux & macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run Pipeline
cd src
python pipeline.py
