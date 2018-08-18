 ==============================================================================
 GraphInformation类里包含顶点以及边权信息
   # 从文件中读取图的信息
     # 顶点信息
     pro_graph_vertex
     # 边权信息
     pro_graph_graph
 ==============================================================================
 ==============================================================================
 GraphOperator继承GraphInformation，包含了对属性图的操作的方法
 	# 按类型过滤
 	getVertexs(String key, String value)
 	# 按类型插入顶点并保存到文件中
 	insertVertex(String id, String name, String age, String verType)或者 insertVertex(String id, String name, String verType)
 	# 按类型插入边权信息并保存到文件中
 	insertEdge(String srcid, String dstid, String property, Int weight)
 	# 根据贪心改编的最短路径算法
 	dijkstraModify(String begin, String end)
 ==============================================================================
