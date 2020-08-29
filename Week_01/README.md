## 算法学习笔记-Week01

### Array-数组
是有限个相同类型的变量所组成的有序集合
* 内存地址连续
* 随机访问快O(1) prepend/append/lookup
* insert O(n)、delete O(n)
* Python中没有数组，通过列表List和元组tuple实现

### Link List-链表
物理上非连续、非顺序的数据结构，由若干节点node组成
* insert O(1)、delete O(1)
* look up O(n)
* 单向链表、双向链表、循环链表

### Skip List-跳表
元素有序且添加了索引的链表，
* 插入/删除/搜索 O(log n)
* 原理简单
* 容易实现
* 方便扩展
* 只用于**元素有序**的情况

### Stack-栈
* 先入后出
* 添加删除O(1)

### Queue-队列
* 先入先出FIFO
* 添加删除O(1)

### Double-End Queue-双向队列
* 两端可进出的Queue
* 添加删除O(1)

### Priority Queue-优先队列
* 插入操作O(1)
* 取出操作O(log n) 
* 底层具体实现数据结构多样复杂：heap...

### 解题方法--五毒神掌
1. 读题、审题（与面试官交流、确认）
    * 5-10分钟没有思路立刻看题解，**不要死磕**
2. 马上自己写
    * 多种解法比较、体会，分析复杂度，优化执行时间
3. 一天后重新做题
    * 查看国际站 most voting
    * 不同解法的熟练程度+专项联系
4. 一周后反复练练习
5. 面试前一周恢复性训练

### 切题四件套
* Clarification
* Possible solutions
    * compare（time/space）
    * optimal
* Coding
* Test cases

### 一维数据如何加速（降低时间复杂度）
* 升维 （跳表）
* 空间换时间
