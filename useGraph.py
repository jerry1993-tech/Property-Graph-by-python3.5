# -*- coding: utf-8 -*-
"""
Created on Beijing  Aug 17 01:26:52 2018

@author: xuyingjie
"""

from Graph import *

y = GraphInformation()
x = GraphOperator()

# 插入顶点（Persion 类型）
x.insertVertex('1','xiaoming','20', 'Persion')
for vertex in y.pro_graph_vertex:
 print(vertex)
print('\n')

# 插入顶点（Company 类型）
x.insertVertex('8','chagnhong','Company')
for vertex in y.pro_graph_vertex:
 print(vertex)
print('\n')

# 插入边权信息 例： 3 --> 2 , property:Belong , weight:9
x.insertEdge('3', '2', 'Belong', 9)
for edge in y.pro_graph_edge:
 print(edge)
print('\n')

# 获取类型为 Persion 的所有顶点信息
x.getVertexs('verType', 'Persion')
print('\n')

# 获取年龄为 20 的所有顶点信息
x.getVertexs('age', '20')
print('\n')

# 获取类型为 Persion 的所有顶点信息
x.getVertexs('verType','Company')

# 实现任意两个Vertex间的最短路径的计算
x.dijkstraModify('2', '7')
