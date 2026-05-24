import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# load dataset
data = pd.read_csv("data\student_data.csv")

# features (inputs)
X = data[["study_hours", "attendance", "sleep_hours", "assignments"]]

#Labels (output)
y= data["result"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = DecisionTreeClassifier()

#Train model
model.fit(X_train,y_train)

#Make predictions
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test,predictions)

print("predictions:")
print(predictions)

print("\nActual results:")
print(y_test.values)

print("\nAccuracy score:")
print(accuracy)

#Visualize decision tree
plt.figure(figsize=(12,8))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True
)

plt.show()