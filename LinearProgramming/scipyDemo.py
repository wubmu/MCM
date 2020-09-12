from scipy import optimize
import numpy as np
# max z = 2x(1)+3x(2)-5x(3)


#确定c A b Aeq beq
c = np.array([2,3,-5])
A = np.array([[-2,5,-1],[1,3,1]])
b = np.array([-10,12])
Aeq = np.array([[1,1,1]])
beq = np.array([7])
#求解
res = optimize.linprog(-c,A,b,Aeq,beq)
print(res)

## fun目标函数的最小化  x为最优解