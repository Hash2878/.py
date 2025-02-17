from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import datasets

iris = datasets.load_iris()
x = iris.data
y = iris.target

print('Feature names:', iris.feature_names)
print('Classes: 0-Iris-Setosa, 1-Iris-Versicolour, 2-Iris-Virgi~nica')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

print('Classification Report:')
print(classification_report(y_test, y_pred))
