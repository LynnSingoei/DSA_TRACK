## 🌳 Maximum Depth of Binary Tree — LeetCode 104  
🔗 **Problem Link:** https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its **maximum depth**.  
The maximum depth is defined as the number of nodes along the longest path from the root down to the farthest leaf node.

---

## 🧠 Intuition

- Maximum depth is basically “how deep can we go” in the tree.  
- Naturally, **recursion** works perfectly:  
  - Depth of a tree = 1 (current node) + max depth of left and right subtrees.  
- Iterative solutions are also possible using **BFS (queue)** or **DFS (stack)**.

---

## ✅ Recursive Solution

```python
class Solution(object):
    def maxDepth(self, root):
        # Base case: empty tree has depth 0
        if root is None:
            return 0
        
        # Recursively find left and right subtree depths
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        # Depth of current node = max of left and right + 1
        return max(left, right) + 1

```
# Iterative solution
## Using queue
```
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        queue=collections.deque([root])
        count=0
        while queue:
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count+=1
        return count
```
# Comparison Table(Time and space complexities)
Approach	Time Complexity	Space Complexity	Notes
Recursive DFS	O(n)	O(h) worst-case, O(log n) best-case	Elegant, but can hit recursion depth limit
Iterative BFS (Queue)	O(n)	O(n) worst-case, O(1) best-case	Level-by-level processing; safe for deep trees
