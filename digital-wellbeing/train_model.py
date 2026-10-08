from sklearn.ensemble import RandomForestClassifier
import pickle

X = [
    [8, 5, 4, 120],
    [3, 1, 7, 30],
    [6, 4, 5, 80]
]

y = [2, 0, 1]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))

print("Model trained and saved!")