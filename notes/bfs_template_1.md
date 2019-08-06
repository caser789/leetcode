---
tags: [BFS, queue, template]
title: BFS Template One
created: '2019-08-05T05:47:52.602Z'
modified: '2019-08-05T05:48:35.699Z'
---

# BFS Template One



```java
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    int step = 0;       // number of steps neeeded from root to current node
    // initialize
    add root to queue;
    // BFS
    while (queue is not empty) {
        step = step + 1;
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                add next to queue;
            }
            remove the first node from queue;
        }
    }
    return -1;          // there is no path from root to target
}
```

```python
def bfs(root, target):
    q = Queue()
    step = 0
    q.enqueue(root)
    while q:
        step += 1
        for i in range(len(q)):
            n = q.dequeue()
            if n == target:
                return step
            for neighbor in n.neighbours:
                q.enqueue(neighbor)
    return -1
```
