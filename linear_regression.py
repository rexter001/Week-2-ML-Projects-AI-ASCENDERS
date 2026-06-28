# Dataset Creation
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5])
y = np.array([3 , 5, 7, 9, 11])
print ("Input (x): ", x)
print ("Output (y): ", y)


#Calculating Slope
n = len(x)
m  = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x * x) - (np.sum(x)) ** 2)
print ("Slope (m): ", m)

#Calculating Intercept
intercept = (np.sum(y) - m * np.sum(x)) / n
print ("Intercept (b): ", intercept)

#prediction
y_pred = m * x + intercept
print ("Predicted Values: ", y_pred)

#Mean Squared Error
mse = np.mean((y - y_pred) ** 2)
print ("Mean Squared Error: ", mse)

#Visualization
plt.scatter(x, y, color="blue", label = "Actual Data")
plt.plot(x, y_pred, color="red", label = "Regression Line")
plt.title("Linear Regression fromScratch")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
