# Model Performance Evaluation Report

## Confusion Matrix
| | Predicted Normal | Predicted Fraud |
|---|---|---|
| Actual Normal | 99952 | 1 |
| Actual Fraud | 31 | 16 |

## Classification Metrics
- Precision: 0.941
- Recall: 0.340
- F1-score: 0.500

- Accuracy: 1.000
## Threshold-independent Metrics
- ROC-AUC: 0.670
- PR-AUC: 0.321 (Baseline ≈ 0.000)

## Detailed Metrics from sklearn
{'0': {'precision': 0.9996899472910394, 'recall': 0.99998999529779, 'f1-score': 0.9998399487836107, 'support': 99953.0}, '1': {'precision': 0.9411764705882353, 'recall': 0.3404255319148936, 'f1-score': 0.5, 'support': 47.0}, 'accuracy': 0.99968, 'macro avg': {'precision': 0.9704332089396374, 'recall': 0.6702077636063418, 'f1-score': 0.7499199743918054, 'support': 100000.0}, 'weighted avg': {'precision': 0.999662445956989, 'recall': 0.99968, 'f1-score': 0.9996050240076824, 'support': 100000.0}}

## Interpretation
The model demonstrates strong ranking ability (ROC-AUC=0.670) and a trade-off between recall (0.340) and precision (0.941). Missed fraud cases (FN=31) may result in revenue loss, while false positives (FP=1) increase inspection costs.
