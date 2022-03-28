前缀和：
原始数组不被修改的情况下，频繁查询某个区间的累加和

查分数组：
频繁对原始数组某个区间的元素进行增减

滑动窗口：
子串问题

二分搜索：
普通二分搜索，左侧搜索，右侧搜索

快慢指针：
数组原地修改，O(n)

单调栈：
解决 Next Great Number 的问题

```
for (int i = n - 1; i >= 0; i--) {
    // 如果栈不为空，栈顶数据小于当前数据，推出
    while (!stack.isEmpty() && temperatures[stack.peek()] <= temperatures[i]) {
        stack.pop();
    }
    // 栈为空时，没有下一个更大元素。否则，栈顶索引到当前索引的距离为值
    res[i] = stack.isEmpty() ? 0 : (stack.peek() - i);
    // 保存当前索引
    stack.push(i);
}
```

单调队列：
解决滑动窗口相关问题

中位数相关：
可以用两个有序队列。大小堆通常可以一起用来维护中位数。

快速排序就是二叉树的前序遍历，
归并排序就是二叉树的后序遍历

递归：
不去管函数的内部细节是如何处理的，我们只看其函数作用以及输入与输出。

将二叉树转化为列表，对于二叉树的题目，无非就以下几种解题思路：

先序遍历（深度优先搜索）
中序遍历（深度优先搜索）（尤其二叉搜索树）
后序遍历（深度优先搜索）
层序遍历（广度优先搜索）（尤其按照层来解决问题的时候）
序列化与反序列化（结构唯一性问题）

BFS:
常用于求无权图的最短路径问题

BST:

```java
void BST(TreeNode root, int target) {
    if (root.val == target) {
        // todo 找到目标，做点什么
    }
    if (root.val < target)
        BST(root.right, target);
    if (root.val > target)
        BST(root.left, target);
}
```

图：
图的存储方式主要有邻接表和邻接矩阵
