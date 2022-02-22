from math import pow,sqrt
import matplotlib.pyplot as plt

class linair:
    def __init__(self,x,y):
        if len(x)!=len(y): 
            raise ValueError("hello")
        else:
            self.x=x
            self.y=y
            
    def moy(self,var):
        som=0
        for i in var:
            som+=i
        return (1/len(var))*som
        
    
    def variance(self,var):
        sum_moy=0
        for i in var:
            sum_moy+=(pow(i,2)-pow(self.moy(var),2))
        return (1/len(var))*sum_moy
    
    def ecart_type(self,var):
        return sqrt(self.variance(var))
    
    def cov(self):
        multi=0
        for i in range(len(self.x)):
            multi+=(self.x[i]*self.y[i])- ( (self.moy(self.x))*(self.moy(self.y)) )
        return (1/len(self.x))*multi
    
    def fct_lineaire_regression(self,u):
        deta1=self.cov()/self.variance(self.x)
        deta0=self.moy(self.y)-deta1*self.moy(self.x)
        print("1:",deta1,"0:",deta0)
        y_preddict=[]
        if isinstance(u,list):
            for i in u:
                y_preddict.append((deta1*i)+deta0)
            return y_preddict
        else:
            return (deta1*u)+deta0
    
    def show_graphe_lineaire(self):
        plt.figure(figsize=(10,4))
        plt.title("graphe of lineaire regression")
        plt.scatter(self.x,self.y,label="data initial")
        plt.plot(self.x,self.fct_lineaire_regression(self.x) ,label="predict data",c="red")
        plt.legend()
        plt.show()
        # plt.savefig("graphe_linaire.png")
        
# x=[2,4,14,8,12]
# y=[10,8,2,6,4]
# l=linair(x,y)
# print("les moyenne: x:",l.moy(x),"\ty:",l.moy(y),"\nvariance: ",l.variance(x),"\t",l.variance(y),"\ncov: ",l.cov(),"\npredict",l.fct_lineaire_regression(90))
# l.show_graphe_lineaire()