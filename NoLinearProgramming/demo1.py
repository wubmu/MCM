##计算  1/x+x的最小值

from scipy.optimize import minimize
import numpy as np

def fun(args):
    a = args
    v = lambda x:a/x[0]+x[0]
    return v
if __name__ == '__main__':
    args = (1)
    x0 = np.asarray((2)) #起始值猜测
    res = minimize(fun(args) , x0 , method='SLSQP')
    print(res.fun)
    print(res.success)
    print(res.x)