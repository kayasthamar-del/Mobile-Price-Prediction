import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Step 1: Read data
data = pd.read_csv("mobile_data.csv")

# Step 2: Separate input and output
X = data.drop("price_range", axis=1)
y = data["price_range"]

# Step 3: Create model
model = DecisionTreeClassifier()

# Step 4: Train model
model.fit(X, y)

# Step 5: Save trained model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully")
