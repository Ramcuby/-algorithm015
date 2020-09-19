## 算法学习笔记-Week04

### 深度优先DFS和广度优先BFS
* 树的定义
```Python
Class TreeNode():
    def __init__(self,val):
        self.val = val
        self.left,self.right = None,None
```
* DFS代码模板
```Python
#与原递归一样的格式
def dfs(node):
    if node in visited: # terminator
    # already visited 
    return 
	visited.add(node) 
	# process current node here. 
	... #logic here
    dfs(node.left)
    dfs(node.right)
```
```Python
#Python
visited = set() 
def dfs(node, visited):
    if node in visited: # terminator
    # already visited 
    return 
	visited.add(node) 
	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```
```Python
#非递归写法--手动维护一个stack
def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
```
* BFS代码模板
水波纹、地震、人脑思维

```Python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...

```


### 贪心 - 
* 


### 二分查找
* 前提
    1. 目标函数单调性（单调递增或递减）
    2. 存在上下界（bounded）
    3. 能够通过索引访问（index acceddible）
* 代码模板
```Python
left, right = 0, len(array) - 1 
while left <= right: 
    mid = (left + right) / 2 
    if array[mid] == target: 
        # find the target!! 
        break or return result 
    elif array[mid] < target: 
        left = mid + 1 
    else: 
        right = mid - 1
```
* 