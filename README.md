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
