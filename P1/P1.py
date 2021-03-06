
import sympy as sp  #calculo simbolico
from sympy.utilities.lambdify import lambdify
from sympy.interactive import printing
from sympy.plotting import plot_parametric
import numpy as np
import math
from scipy.spatial.distance import cdist
printing.init_printing(use_latex=True)


t = sp.symbols('t')

if __name__ == "__main__":
    #curvas: 
    #  Gamma=c(t)=(x(t), y(t))
    
    #a
    #x0, y0 = t-1,t
    #x1, y1 = 2*t-5,3-t
    #intervalo0 = [0, 1]
    #intervalo1 = [-1, 0]
    
    #b
    #x0, y0 = 2*sp.cos(t), 3*sp.sin(t)
    #x1, y1 = 3*sp.cos(t), 2*sp.sin(t)
    #intervalo0 = [0, 2*math.pi]
    #intervalo1 = [0, 2*math.pi]
    
    #c
    #x0, y0 = t,1/(2*t)
    #x1, y1 = sp.cosh(t),sp.sinh(t)
    #intervalo0 = [1/10,10]
    #intervalo1 = [0,1]
    
    #d
    x0, y0 = t,t**2
    x1 = -(0.5)*sp.sqrt(3.0)*(sp.log(t)**2)+(0.5)*sp.log(t)+1
    y1 = (0.5)*(sp.log(t)**2)+(0.5)*sp.sqrt(3.0)*sp.log(t)-1
    intervalo0 = [-2,2]
    intervalo1 = [0.1,10]
    
    # Porcentaje para calcular el numero de 0's
    porcentaje = 0.10
    # Numero de puntos a tomar en el intervalo
    puntos_intervalo = 100
    # eps: Error al comparar los puntos
    eps = 0.001
    
# calcula la signatura de c(t)=(x(t), y(t)) en funcion de t
# Devuelve el par ( K(s), dK/ds )
def sig(x, y, t):
    #primeras derivadas
    dx = sp.diff(x,t)
    dy = sp.diff(y,t)

    #segundas derivadas
    d2x = sp.diff(dx, t).simplify()
    d2y = sp.diff(dy, t).simplify()

    determinante = (dx * d2y) - (dy * d2x)
    norma = sp.sqrt(dx**2 + dy**2)

    K = determinante / norma**3
    K = K.simplify()
    dKdt = sp.diff(K, t)
    dKds = (1 / norma) * dKdt
    dKds = dKds.simplify()

    return (K, dKds)

#obtenemos las signaturas y las convertimos a numpy
sig0 = sig(x0, y0, t)
sig1 = sig(x1, y1, t)
print "sig0(t) =",sig0
print "sig1(t) =",sig1
#plot_parametric(sig0, (t,intervalo0[0],intervalo0[1]))
#plot_parametric(sig1, (t,intervalo1[0],intervalo1[1]))

num_sig0 = lambdify(t, sig0, [{'ImmutableMatrix': np.array}, 'numpy'])
num_sig1 = lambdify(t, sig1, [{'ImmutableMatrix': np.array}, 'numpy'])


#puntos a evaluar
paso0 = math.fabs((intervalo0[1] - intervalo0[0]) )/ puntos_intervalo
paso1 = math.fabs((intervalo1[1] - intervalo1[0]) )/ puntos_intervalo

puntos0 = np.arange(intervalo0[0], intervalo0[1]+paso0, paso0)

puntos1 = np.arange(intervalo1[0], intervalo1[1]+paso1, paso1)

evaluacion0=[]; evaluacion1=[];
#evaluacion de la signatura
for i in range(puntos_intervalo):
    evaluacion0.append(num_sig0(puntos0[i]))
    evaluacion1.append(num_sig1(puntos1[i]))

distancias = cdist(evaluacion0, evaluacion1, 'euclidean')
num_ceros = (distancias < eps).sum()
for i in range(puntos_intervalo):
    for j in range(i,puntos_intervalo):
        if distancias[j][i] < eps:
            num_ceros = num_ceros +1
print "h"
print distancias[0][0]
print distancias[4][2],distancias[2][4]
print distancias.size
acierto = num_ceros*1.0/puntos_intervalo*100
print num_ceros
print acierto     
if acierto > 100:
    acierto = 100

if num_ceros >= puntos_intervalo*porcentaje*1.0:
    print "Las dos curvas son equivalentes un",acierto,"%"
else:
    print "Las dos curvas NO son equivalentes"
