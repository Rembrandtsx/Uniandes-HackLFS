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
        for i in range(1,X.shape[1]):
            a = X[:,i]
            if type(a[0]) == bool:
                X[:,i] = array(list(map(int,a)))
            else:
                o = array(X[:,i])
                X[:,i] = (o-o.mean())/std(o)
        b = array(b).T 
        X = [b[b[:,0]==i+1][:,1:] for i in range(max(X[:,0]))]
        return X


    def k_vals(self, s, percent=0.9): #esto no importa
        k = 0
        vari = 0
        while vari<percent:
            k+=1
            vari = sum(s[:k])/sum(s)
        return k

    def reduc_dimen(self,X): #este toca llamarlo para acer reduccion de dimensiones
        covar = (1/(self.amount -1))* X.T.dot(X)
        u,s,v = svd(covar)
        k = self.k_vals(self,s)
        ured = u[:,:k]
        z = X.dot(ured)
        return z, u 

    
    def GD(self,u): #este hace las lineas de tendencia por gradient descent
        return 0

    def porcentajeTotal(self): #retorna el porcentaje float de la entrada nueva total (guardar esto con la fecha)
        return 0

    def porcentajeJuego(self): #retorna el porcentaje float de la nueva entrada para todos los juegos. 
        return [0,0,0]






    



