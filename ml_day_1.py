""" import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('BostonHousing.csv')


x = np.array(df['rm'])
y = np.array(df['medv'])

Theta_1 = 0.0
Theta_0 = 0.0
learning_rate = 0.0001
iterations = 1000

def compute_cost(x, y, Theta_1, Theta_0):
  m = len(y)
  prediction = Theta_1*x + Theta_0
  cost = (1/(2*m))* np.sum((prediction - y)*2)
  return cost


def gradient_descent(x, y, Theta_1, Theta_0, learning_rate):
    m = len(y)
    prediction = (Theta_1 * x) + Theta_0
    d_1 = (1/m) * np.sum((prediction - y) * x)
    d_0 = (1/m) * np.sum(prediction - y)
    Theta_1 -= learning_rate * d_1
    Theta_0 -= learning_rate * d_0
    return Theta_1, Theta_0


for i in range(iterations):
  Theta_1, Theta_0 = gradient_descent(x, y, Theta_1, Theta_0, learning_rate)
  if i% 100==0:
     cost = compute_cost(x, y, Theta_1, Theta_0)
     print(f"Iteration {i}, cost: {cost:.4f}, Theta_1: {Theta_1:.4f}, Theta_0: {Theta_0:.4f}")


print(f"\nFinal parameters: Theta_1: {Theta_1:.4f}, Theta_O: {Theta_0:.4f}")

y_pred = Theta_1 * x + Theta_0


plt.scatter(x, y, color='blue', label='Actual data')
plt.plot(x, y_pred, color='red', label='Fitted line')
plt.xlabel('Average Rooms (RM)')
plt.ylabel('House Price (MEDV)')
plt.legend()
plt.show()
plt.title("aryan_gupta_590027018_lab04") """

""" import pandas as pd,matplotlib.pyplot as plt,numpy as np,kagglehub
from sklearn.preprocessing import OneHotEncoder


df = pd.DataFrame({
    'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small']
})
coo = df.copy()
label = OneHotEncoder()
df["ll"] = label.fit_transform(df["Size"])
print(df) """  
import pandas as pd,matplotlib.pyplot as plt,numpy as np
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
df = pd.DataFrame(
  {"name" : ['a','b','c','d','e'],'gender':['m','f','m','f','m'],'passed':['y','n','y','y','n']}
)
""" df_label = df.copy()
le = LabelEncoder()
oh = OneHotEncoder() """
df_dummies = pd.get_dummies(df,columns=['gender','passed'])
""" df_label['label_encoded'] = le.fit_transform(df_label['gender'])
df_label['one hot encoded'] = oh.fit_transform(df)
print(df_label[['name','gender','label_encoded']]) """
""" print(df_dummies) """
import pandas as pd
from sklearn.preprocessing import StandardScaler

""" df = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40],
    "Salary": [20000, 40000, 60000, 80000, 100000]
})

scaler = StandardScaler()

df_scaled = scaler.fit_transform(df)

print(df_scaled)

 """
 
