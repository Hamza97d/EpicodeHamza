import array
import pandas as pd

bezdekIris= pd.read_csv("bezdekIris.data", header=0)
iris=pd.read_csv("iris.data",  names=["sepal_length","sepal width","petal_length", "petal_width", "class"])
indice=pd.read_csv("index")

#.head(), .tail()


dt_frame_iris= pd.DataFrame(iris)

print(dt_frame_iris.head())
print(dt_frame_iris.tail(10))

print(dt_frame_iris.describe())