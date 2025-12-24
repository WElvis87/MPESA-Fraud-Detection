from load_data import load_data
from clean_data import clean_data
from data_split import split_data
from train_model import create_model, train_model, evaluate_model, create_evaluation_report, save_model

def run_pipeline():
    print("=== Starting MPESA Fraud Detection Pipeline ===")

    df = load_data()
    print("Data loaded:", df.shape)

    df = clean_data(df)
    print("Data cleaned:", df.shape)

    X_train, X_test, y_train, y_test = split_data(df)
    print(f"Data split: Train={len(X_train)}, Test={len(X_test)}")

    model = create_model()
    print("Model created.")

    model = train_model(model, X_train, y_train)
    print("Model trained.")

    cm, accuracy, ps, rs, f1, roc_auc, pr_auc, report, fraud_rate = evaluate_model(model, X_test, y_test)

    create_evaluation_report(cm, accuracy, ps, rs, f1, roc_auc, pr_auc, report, fraud_rate)

    save_model(model)

    print("=== Pipeline completed Successfully ===")

    return model

if __name__ == "__main__":
    run_pipeline()
