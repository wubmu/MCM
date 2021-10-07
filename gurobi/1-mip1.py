'''
maximize
        x + y + 2z
subject to
        x + 2y + 3z <=4
        x + y  >=1
x,y,z binary
'''

from gurobipy import *

try:
    # 建立模型
    model = Model('mip1')

    # 创建变量
    x = model.addVar(vtype=GRB.BINARY, name='x')
    y = model.addVar(vtype=GRB.BINARY, name="y")
    z = model.addVar(vtype=GRB.BINARY, name='z')

    # 设置目标函数
    model.setObjective(x + y + 2 *z, GRB.MAXIMIZE)

    # 添加约束
    model.addConstr(x + 2 * y + 3 * z <= 4, 'c0')
    model.addConstr(x + y >= 1,'c1')

    model.optimize()

    for v in model.getVars():
        print('%s %g' % (v.VarName, v.x))

    print('Obj: %g' % model.objVal)
except GurobiError as e:
    print('Error reported'+ str(e.errno) + ": " +str(e))