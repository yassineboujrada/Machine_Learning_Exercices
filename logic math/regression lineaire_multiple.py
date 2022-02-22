import numpy as np
import matplotlib.pyplot as plt
import math as ma
import random

class linair_multiple:
    
    def __init__(self,x,y):
        self.x=np.array([x])
        self.y=np.array([y])
        self.deta=np.random.randint((self.x).shape)
        
        
    def predict_function(self,list_predict):
        self.X=self.X_matrix(list_predict)
        return self.X.dot(self.tetha())
        
        
    def X_matrix(self,x):
        l=x.tolist()
        for i in range(len(x)):
            l[i].insert(x.shape[1]-1,1)
        return np.array(l)   
    
    def tetha(self):
        self.new_deta_value=self.deta
        for _ in range(1000):
            self.new_deta_value=self.descendent(0.01,self.new_deta_value)
        return self.new_deta_value 
    
    def descendent(self,d,alpha=0.1):
        return d-(np.dot(self.grade_function(),alpha))
    
    # grade_function=lambda x,o,y: np.dot(np.transpose(x),lineaire_prediction(x,o)-y)*(1 / len(x))
    def grade_function(self):
        return np.dot(np.transpose(self.X),self.predict_function(self.X)-self.y)*(1 / len(self.X))
    
    def cost_function(self):
        return (sum(self.X.dot(self.tetha())-self.y)**2)*(1/(2*len(self.X)))
    
x=np.array([[1,2,1],[3,4,1],[4,3,1],[2,2,1]])
from sklearn.datasets import make_regression
np.random.seed(0)
x_data,y_data = make_regression(n_samples=100, n_features=1,noise=10)

l=linair_multiple(x_data,y_data)
# deta=np.random.rand(x.shape[1],1)
# X=np.array([x.tolist()[i].insert(x.shape[1]-1,1) for i in range(len(x))])
n_y=l.predict_function(x_data)
print(n_y)