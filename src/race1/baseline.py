import time
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import numpy as np

tennis_data = pd.read_csv("tennis.csv", header=None)
car_data = pd.read_csv("car_eval.csv", header=None)

tennis_columns = ["Outlook", "Temperature", "Humidity", "Wind", "Play"]
tennis_data.columns = tennis_columns

car_columns = ["Buying", "Maint", "Doors", "Persons", "Lug_boot", "Safety", "Class"]
car_data.columns = car_columns

def evaluate_dataset(X, y, dataset_name, runs=1000):
    for col in X.columns:
        X[col] = LabelEncoder().fit_transform(X[col])
    y = LabelEncoder().fit_transform(y)

    train_times = []
    infer_times = []
    accuracies = []

    for _ in range(runs):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)

        clf = DecisionTreeClassifier(criterion="entropy")

        start_train = time.perf_counter_ns()
        clf.fit(X_train, y_train)
        end_train = time.perf_counter_ns()
        train_times.append((end_train - start_train) / 1_000)

        start_infer = time.perf_counter_ns()
        y_pred = clf.predict(X_test)
        end_infer = time.perf_counter_ns()
        infer_times.append((end_infer - start_infer) / 1_000)

        accuracies.append(accuracy_score(y_test, y_pred))

    print(f"\n{dataset_name} Dataset:")
    print(f"Average Training Time: {np.mean(train_times):.2f} µs")
    print(f"Median Training Time: {np.median(train_times):.2f} µs")
    print(f"Average Inference Time: {np.mean(infer_times):.2f} µs")
    print(f"Median Inference Time: {np.median(infer_times):.2f} µs")
    print(f"Average Accuracy: {np.mean(accuracies):.4f}")

X_tennis = tennis_data.drop(columns=["Play"])
y_tennis = tennis_data["Play"]
evaluate_dataset(X_tennis, y_tennis, "Tennis")

X_car = car_data.drop(columns=["Class"])
y_car = car_data["Class"]  
evaluate_dataset(X_car, y_car, "Car Evaluation")
