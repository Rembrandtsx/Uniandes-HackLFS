from numpy import *
from numpy.linalg import *
import os
import datos
import json

class Persona():

    def __init__(self,lista):
        self.lista = lista
        self.amount = self.lista.shape[0]
        self.X = self.darMatrizDeFeatures(self.lista)
        
    ## ACÁ VA A FALTAR TRATAR LOS DATOS

    def darMatrizDeFeatures(self,X): #loadea, arregla y normaliza
        X = array([[i['juego'],i['atributo2'],i['atributo3']] for i in X])
        b = [X[:,i]]
        X= array([X[X[:,0]==i+1][:,1:] for i in range(max(X[:,0]))])
        for i in range(len(X)):
            a = array(X[i])
            # if type(a[0]) == bool:
            #     X[:,i] = array(list(map(int,a)))
            # else:
            for j in range(a.shape[1]):
                o = array(a[:,j]).reshape(a.shape[0],1)
                b.append((o-o.mean())/std(o))
        b = array(b).T 
        return b


    def k_vals(self, s, percent=0.99): #esto no importa
        k = 0
        vari = 0
        while vari<percent:
            k+=1
            vari = sum(s[:k])/sum(s)
        return k

    def reduc_dimen(self,X): #este toca llamarlo para acer reduccion de dimensiones
        covar = (1/(self.amount -1))* X.T.dot(X)
        u,s,v = svd(covar)
        k = self.k_vals(s)
        ured = u[:,:k]
        z = X.dot(ured)
        return z

    
    def GD(self,X): #este hace las lineas de tendencia por gradient descent
        todos = []
        for i in X:
            todos.append(self.reduc_dimen(i))
        xs=[todos[0],todos[2],todos[4]]
        xss = []
        for i in xs:
            xss.extend(i)
        ys=[todos[1],todos[3],todos[5]]
        yss = []
        for i in ys:
            yss.extend(i)
        xss = array(xss)
        yss = array(yss)
        N=200
        theta = 0
        alpha = 0.4
        for i in range(N):
            theta = theta - (alpha/len(xss))*np.matmul(xss.T,(xss.dot(theta)-yss))

        return lambda m: theta[0]+theta[1]*m

    def porcentajeTotal(self): #retorna el porcentaje float de la entrada nueva total (guardar esto con la fecha)

        return {'E':30,'A':70}

