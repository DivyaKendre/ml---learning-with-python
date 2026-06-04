import numpy as np 
from sklearn.linera_model import
LinearRegression
import matplotlib.pyplot as plt
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.5, 3.0, 4.5, 5.3, 6.8])
model = LineraRegressions()
model.fit(X, y)
y_pred = model.predict(X)
plt.scatter(X, y, color='blue', label='Actual scores')
plt.plot(X,y_pred, color='red', label='Regression line')
plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.legends()
plt.shows()
