---
tags: [data structure/queue, method/traversal/level, template]
title: BFS template Two
created: '2019-08-05T05:49:20.347Z'
modified: '2019-12-02T15:09:11.612Z'
---

# BFS template Two

```java
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    Set<Node> visited;  // store all the nodes that we've visited
    int step = 0;       // number of steps neeeded from root to current node
    // initialize
    add root to queue;
    add root to visited;
    // BFS
    while (queue is not empty) {
        step = step + 1;
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                if (next is not in used) {
                    add next to queue;
                    add next to visited;
                }
                remove the first node from queue;
            }
        }
    }
    return -1;          // there is no path from root to target
}
```

```python
def bfs(root, target):
    q = Queue()
    visited = set()
    step = 0
    q.enqueue(root)
    visited.add(root)
    while q:
        step += 1
        for i in range(len(q)):
            e = q.dequeue()
            if e == target:
                return step
            for n in e.neighbours:
                if n not in visted:
                    q.enqueue(n)
    return -1
```
