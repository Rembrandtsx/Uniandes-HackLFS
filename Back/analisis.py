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
            a = X[i]
            # if type(a[0]) == bool:
            #     X[:,i] = array(list(map(int,a)))
            # else:
            for j in range(a.shape[1]):
                o = array(a[:,j])
                b.append((o-o.mean())/std(o))
        b = array(b).T 
        return X


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
            todos.append(reduc_dimen(i))
        xs=[todos[0][0],todos[1][:,0],todos[2][:,0]]
        xss = []
        for i in xs:
            xss.extend(i)
        ys=[todos[0][1],todos[1][:,1],todos[2][:,1]]
        yss = []
        for i in ys:
            yss.extend(i)
        
        return 0

    def porcentajeTotal(self): #retorna el porcentaje float de la entrada nueva total (guardar esto con la fecha)
        return {'E':0,'A':0}

