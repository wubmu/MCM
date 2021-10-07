# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:55:43 2020

@author: AtticusYuan

使用Gurobi求解一个简单的约束规划（Constraint Programming），输出约束规划所有的可行解
"""

from gurobipy import *
from gurobipy import GRB
import time


def cp_model():
    # 创建模型
    model = Model("cp_model")

    # 创建变量
    x1 = model.addVar(vtype=GRB.INTEGER, name='x1')
    x2 = model.addVar(vtype=GRB.INTEGER, name='x2')

    # 创建约束
    model.addConstr(x1 >= 1, name='c1')
    model.addConstr(x1 <= 30, name='c2')
    model.addConstr(x2 >= 1, name='c3')
    model.addConstr(x2 <= 30, name='c4')

    # 最小化一个常数，则输出所有可行解
    model.setObjective(0, GRB.MINIMIZE)

    model.__data = x1, x2

    return model


try:

    start = time.time()

    # 创建模型
    model = cp_model()

    # 求解约束规划需要结合Solution Pool的几个参数
    model.setParam(GRB.Param.PoolSolutions, 1000)  # 需要输出可行解的数量，如果不设置，默认为10个；如果设置的数量大于可行解的数量，则输出所有可行解
    model.setParam(GRB.Param.PoolSearchMode, 2)  # 搜索模式
    model.setParam(GRB.Param.PoolGap, 10)  # 找到的可行解与最优解的Gap值

    # 优化模型
    model.optimize()

    # 输出结果
    nSolutions = model.SolCount  # 查询解的数量SolCount（不可更改），如果PoolSolutions的值≤所有可行解的数量，那么SolCount等于PoolSolutions，否则等于所有可行解的数量
    x1, x2 = model.__data
    for i in range(nSolutions):
        model.setParam(GRB.Param.SolutionNumber, i)
        print("===solution for %s:" % i)
        print("x1:", x1.xn)
        print("x2:", x2.xn)
    print('找到可行解的数量为: ', nSolutions)

    # 计算程序运行时间
    end = time.time()
    print('程序运行时间：', end - start, '秒')


except GurobiError as exception:
    print('Error code ' + str(exception.errno) + ": " + str(exception))

except AttributeError:
    print('Encountered an attribute error')