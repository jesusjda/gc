import numpy as np
import matplotlib.pyplot as plt
'''
def coef(x, y, n): 
    x.astype(float) 
    y.astype(float) 
    n = len(x) 
    a = [] 
    for i in range(n): 
        a.append(y[i])
        for j in range(1, n):
            for i in range(n-1, j-1, -1):
                a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])

    return np.array(a) # return an array of coefficient

def Eval(a, x, r):
    x.astype(float)
    n = len( a ) - 1
    temp = a[n]
    for i in range( n - 1, -1, -1 ):
        temp = temp * ( r - x[i] ) + a[i]
    return temp # return the y_value interpolation
        
'''
def newton_polynomial(x, tau, num_points=100, libraries=False):
#your code here
    if libraries == False:
        #your code here    
    
        return polynomial #np.array of size num_points
    else:
        #your code here
        return another_polynomial #np.array of size num_points
    
if __name__ == '__main__':
    n = 10  
    tau = np.arange(n)
    x = np.random.randint(-10, 10, size=n)
    num_points = 100

    print 'tau', tau
    print 'x', x

    poly_0 = newton_polynomial(x, tau, num_points, libraries=False)
    poly_1 = newton_polynomial(x, tau, num_points, libraries=True)
    print np.linalg.norm(poly_0 - poly_1)
    
    t = np.linspace(tau[0], tau[-1], num_points)    
    plt.plot(t, poly_0)
    plt.plot(tau, x, 'o')
    plt.show()
    
    
    import timeit
    
    print(timeit.repeat("x = np.random.randint(-10, 10, size=n); newton_polynomial(x, tau, libraries=False)",
                        setup="from __main__ import newton_polynomial, n,  tau, np",
                        number=10000))
    print(timeit.repeat("x = np.random.randint(-10, 10, size=n); newton_polynomial(x, tau, libraries=True)",
                        setup="from __main__ import newton_polynomial, n,  tau, np",
                        number=10000))

    # URLs con info

    # https://gist.github.com/vene/921554
    # http://stackoverflow.com/questions/14823891/newton-s-interpolating-polynomial-python
