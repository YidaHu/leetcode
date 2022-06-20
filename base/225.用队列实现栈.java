import java.util.LinkedList;
import java.util.Queue;

/*
 * @lc app=leetcode.cn id=225 lang=java
 *
 * [225] 用队列实现栈
 */

// @lc code=start
class MyStack {

    private Queue<Integer> q;
    private int top_element;

    public MyStack() {
        q = new LinkedList<>();
        top_element = 0;
    }

    public void push(int x) {
        q.offer(x);
        top_element = x;
    }

    public int pop() {
        int size = q.size();
        // 留下队尾两个元素
        while (size > 2) {
            q.offer(q.poll());
            size--;
        }
        // 记录队尾元素
        top_element = q.peek();
        q.offer(q.poll());
        // 删除最后一个元素
        return q.poll();
    }

    public int top() {
        return top_element;
    }

    public boolean empty() {
        return q.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
// @lc code=end
