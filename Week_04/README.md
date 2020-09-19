## 算法学习笔记-Week04

### 递归 - 循环
函数调用自身，通过函数体来进行的循环
* 计算阶乘
* 汉诺塔
* 递归模板
```python
def recursion(level,param1,param2,...)
    #recursion terminator 递归终结条件
    if level > MAX_LEVEL:
        process_result
        return
    
    #process logic in current lvevl 处理当前层逻辑
    process(levle,data...)
    
    #drill down 下探到下一层
    self.recursion(level+1,p1,...)

    #reverse the current level status if needed 清理当前层

```

* 思维要点
    1. 不要人肉递归（最大误区）
    2. 找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
    3. 数学归纳法思维

### 分治 
是一种特殊的递归，Divide & Conquer & Merge
* 分解成多个子问题
* 找重复性
* 比递归模板增加一步:组合子结果
```python
    result = process_result(subresult1, subresult2, subresult3, ...)
```

### 回溯 - Backtracking
是一种特殊的递归
* 不断在每一层试错
* 八皇后问题

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