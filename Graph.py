# -*- coding: utf-8 -*-

import sys

class GraphInformation:
  # 顶点信息 初始
# =============================================================================
#     pro_graph_vertex = [{'id': 3, 'name': 'LiZhan', 'age': '23', 'verType': 'Persion'},
#                         {'id': 5, 'name': 'YunJie', 'age': '20', 'verType': 'Persion'},
#                         {'id': 2, 'name': 'TingJin', 'age': '30', 'verType': 'Persion'},
#                         {'id': 7, 'name': 'ZhiDaoChuangYu', 'verType': 'Company'}]
# =============================================================================
  pro_graph_vertex = []
  with open('vertex.txt','r') as fread:
    rline = fread.readline()
    while rline:
      result = rline.rstrip().split(' ')
      if len(result) == 4:
        pro_graph_vertex.append({'id': result[0], 'name': result[1], 'age': result[2], 'verType': result[3]})
      elif len(result) == 3:
        pro_graph_vertex.append({'id': result[0], 'name': result[1], 'verType': result[2]})
      rline = fread.readline()
      
  # 边权信息 初始
# =============================================================================
# pro_graph_edge = [{'srcid': '3', 'dstid': '7', 'property': 'Belong', 'weight': 5}, # 3-->7
#                   {'srcid': '5', 'dstid': '3','property': 'Friend', 'weight': 4}, # 5-->3
#                   {'srcid': '2', 'dstid': '5','property': 'Friend', 'weight': 10}, # 2-->5
#                   {'srcid': '3', 'dstid': '7','property': 'Belong', 'weight': 8}] # 5-->7
# =============================================================================
  pro_graph_edge = []
  with open('edge.txt', 'r') as fread:
    rline = fread.readline()
    while rline:
      result = rline.rstrip().split(' ')
      pro_graph_edge.append({'srcid': result[0], 'dstid': result[1], 'property': result[2], 'weight': int(result[3])})
      rline = fread.readline()


class GraphOperator(GraphInformation):
  
  MAX = 99999 #表示无限大
    
  # 过滤 getVertexs(self, vkey, vvalue) 中 vkey是需要筛选出的类型， vvalue是需要筛选出的内容
  def getVertexs(self, vkey, vvalue):
    for vertex in self.pro_graph_vertex:
        try:
         if vertex[vkey] == vvalue:
             print(vertex)
        except:
            continue
      
# 插入顶点
  def insertVertex(self, *par):
    v = [] #获取传入的参数
    if len(par) == 4:
      for p in par:
          v.append(p)
      self.pro_graph_vertex.append({'id': v[0], 'name': v[1], 'age':v[2], 'verType': v[3]})
    elif len(par) == 3:
      for p in par:
          v.append(p)
      self.pro_graph_vertex.append({'id': v[0], 'name': v[1], 'verType': v[2]})
    with open('vertex.txt','w') as fwrite: #按格式写入文件
      for vertex in self.pro_graph_vertex:
        if len(vertex) == 4:
          fwrite.write(" ".join([vertex['id'],vertex['name'],vertex['age'],vertex['verType']]))
          fwrite.write("\n")
        elif len(vertex) == 3:
          fwrite.write(" ".join([vertex['id'],vertex['name'],vertex['verType']]))
          fwrite.write("\n")

# 插入边
  def insertEdge(self, sid, dsid, pro, wei):
    self.pro_graph_edge.append({'srcid': sid, 'dstid': dsid, 'property': pro, 'weight': wei})
    with open('edge.txt', 'w') as fwrite:
      for edge in self.pro_graph_edge:
        fwrite.write(" ".join([edge['srcid'],edge['dstid'],edge['property'],str(edge['weight'])]))
        fwrite.write("\n")
    
          
#给出两点，获取权值
  def getWeight(self,srcid, dstid):
    for w in self.pro_graph_edge:
      if w['srcid'] == srcid and w['dstid'] == dstid:
        number = w['weight']
        return number
      else:
        number = self.MAX
    return number
      
      
# 传入一个列表，返回权值最小的入度
  def minWeightInEdge(self, count, alist=[]):
    i = 0
    minWeight = alist[i]
    while alist[i]:
      if minWeight['weight'] > alist[i]['weight']:
        minWeight = alist[i]
      i += 1
      if i == count:break
    if minWeight['weight'] != self.MAX:
      return minWeight['to']
    else:
      print('%s do not attach %s'%(minWeight['from'], minWeight['to']))
      print('\n\n\n\n')
      sys.exit(0)
        
    
# 计算最短路径之和
  def sumWeight(self, count, alist=[]):
    i = 0
    shortestWeight = 0
    while alist[i+1]:
      shortestWeight += self.getWeight(alist[i],alist[i+1])
      i += 1
      if i == count-1:break
    return shortestWeight
      

    
# 修改版dijkstra算法
  def dijkstraModify(self, begin, end):
    vertexs = [] # 顶点id
    path_vertex = [] # 储存顶点数组
    path_sum = [] # 储存路径以及权值
    
    path_vertex.append(begin)
    
    for v in self.pro_graph_vertex:
      vertexs.append(v['id'])
    
    for p_v in path_vertex:
      if path_vertex[-1] != end:
        path_sum.clear()
        for v in vertexs:
          path_sum.append({ 'from': p_v, 'to': v, 'weight':self.getWeight(p_v, v)})
        path_vertex.append(self.minWeightInEdge(len(path_sum), path_sum))
      else:
        for rpv in path_vertex:
          print('%s --> '%(rpv), end='')
        print('最短路径长度为：%d'%(self.sumWeight(len(path_vertex), path_vertex)))
        break
    

