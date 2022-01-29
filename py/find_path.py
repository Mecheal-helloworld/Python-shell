import os
import random
import copy

graph = [] #结点代价表，本身代价为0 无连接代价为-1 其余代价为对应值
graph_type = [True,False,False]


def create_graph(number,direction=True,thinning=False,cost=5):
  assert number<100,"结点数请不要超过100"
  global graph
  graph = []
  for i in range(number):
    node_cost_i = []
    for j in range(number):
      if i==j:
        node_cost_i.append(0)
      else:
        random_cost = random.randint(0,cost)
        if thinning:
          random_rate = random.randint(0,cost)
          if random_rate:
             random_cost = 0
        if(random_cost):
          node_cost_i.append(random_cost)
        else:
          node_cost_i.append(-1)
    assert len(node_cost_i)==number,"node create error!" 
    graph.append(node_cost_i)
  if not direction:
    for i in range(number):
      for j in range(i+1,number):
        graph[j][i] = graph[i][j]


def find_path_dfs(nodeA,nodeB):
  assert nodeA != nodeB,"到结点自身的路径不需要寻找!"
  path_cost = []
  open_list = [[[nodeA],0]]
  close_list = []
  while True:
    if len(open_list)==0:
      path_cost = [[],-1]
      break
    now = open_list[0]
    open_list.pop(0)
    close_list.append(now[0][-1])
    if(now[0][-1]==nodeB):
      path_cost = now
      break
    add_open_list = []
    for index,node in enumerate(graph[now[0][-1]]):
      try:
        close_list.index(index)
      except:
        if node > 0:
          serch_path = now[0]+[index]
          add_open_list.append([serch_path,node+now[1]])
    add_open_list.sort(key=lambda x:x[1])
    open_list = add_open_list + open_list
  return path_cost


def find_path_bfs(nodeA,nodeB):
  assert nodeA != nodeB,"到结点自身的路径不需要寻找!"
  path_cost = []
  open_list = [[[nodeA],0]]
  close_list = []
  while True:
    if len(open_list)==0:
      path_cost = [[],-1]
      break
    now = open_list[0]
    open_list.pop(0)
    close_list.append(now[0][-1])
    if(now[0][-1]==nodeB):
      path_cost = now
      break
    for index,node in enumerate(graph[now[0][-1]]):
      try:
        close_list.index(index)
      except:
        if node > 0:
          serch_path = now[0]+[index]
          open_list.append([serch_path,node+now[1]])
    open_list.sort(key=lambda x:x[1])
  return path_cost


def find_path_and_print(startNode,endNode):
  dfs_path_cost = find_path_dfs(startNode,endNode)
  bfs_path_cost = find_path_bfs(startNode,endNode)
  dfs_path = dfs_path_cost[0]
  bfs_path = bfs_path_cost[0]
  dfs_cost = dfs_path_cost[1]
  bfs_cost = bfs_path_cost[1]

  print("\n从{:>2}到{:>2}构造的路径如下：\n".format(startNode,endNode))
  print("有代价的深度优先算法寻找到的路径为：",end="")
  print('{:<2}'.format(dfs_path[0]),end="")
  for node in dfs_path[1:]:
    print(" ->",end=" ")
    print('{:<2}'.format(node),end="")
  print("\n有代价的深度优先算法寻找到的路径代价为：{}".format(dfs_cost))
  print("有代价的广度优先算法寻找到的路径为：",end="")
  print('{:<2}'.format(bfs_path[0]),end="")
  for node in bfs_path[1:]:
    print(" ->",end=" ")
    print('{:<2}'.format(node),end="")
  print("\n有代价的广度优先算法寻找到的路径代价为：{}".format(bfs_cost))


number = input("请输入结点数（默认结点数为50）:")
if number=="":
  number = 50
elif len(number)==3:
  print("结点数请不要超过100,已自动更正为50")
  number = 50
else:
  try:
    number = int(number)
  except:
    print("'"+number+"'为不正确的输入,已自动更正为50")
    number = 50
graph_cost = 5
graph_types = input("请输入图的类型（稀疏S 有向D 带权W）:")
if graph_types=="":
  print("您未输入类型，默认类型为稠密无向带权图，权值为5")
else:
  types = graph_types.split(' ')
  if types[0]=='S':
    graph_type[2] = True
  if types[1]=='D':
    graph_type[0] = False
  if len(types)>=3 and types[2]=='W':
    graph_type[1] = True
    graph_cost_input = input("请输入权值:")
    try:
      graph_cost = int(graph_cost_input)
    except:
      print("'"+graph_cost_input+"'为不正确的输入,已自动更正权值为5")
create_graph(number,graph_type[0],graph_type[2],graph_cost)

graph_name = "稀疏" if graph_type[2] else "稠密"
graph_name += "有向" if graph_type[0] else "无向"
graph_name += "带权图" if graph_type[1] else "图"
print("\n生成的" + graph_name + "路径权值表如下：\n")
print("   ",end="")
for i in range(number):
  prt = '{:>3}'.format(i)
  print(prt,end="")
print("\n",end="")
for i in range(number):
  print('{:<3}'.format(i),end="")
  for j in range(number):
    print('{:>3}'.format(graph[i][j]),end="")
  print("\n",end="")



while True:
  input_path = input("\n请输入需要寻找路径的结点{A}->{B}：")
  if input_path == "":
    print("检测到您未输入任何值，程序退出！")
    break
  elif "->" not in input_path:
    print("您输入的格式不正确，请重新输入！")
    continue
  input_nodes = input_path.split("->")
  try:
    startNode = int(input_nodes[0])
    endNode = int(input_nodes[1])
  except:
    print("您输入的格式不正确，请重新输入！")
    continue
  find_path_and_print(startNode,endNode)