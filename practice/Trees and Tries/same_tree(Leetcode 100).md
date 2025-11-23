# 🌳 Same Tree — LeetCode 100  
🔗 **Problem Link:** https://leetcode.com/problems/same-tree/

This problem checks whether two binary trees are identical in both **structure** and **node values**.

Two trees are considered the same if:

1. They have the same shape.  
2. Corresponding nodes contain equal values.

---

## 🧠 Intuition

The idea is straightforward:

- If both nodes are `None` → they match.
- If only one is `None` → structure differs → trees differ.
- If values differ → trees differ.
- Otherwise, check both left and right children.

This makes it ideal for:

- **Recursive DFS** (most elegant)
- **Iterative DFS** (more control, avoids recursion depth issues)

---

## ✅ Recursive DFS Solution

```
class Solution(object):
    def isSameTree(self, p, q):
        # Both nodes None → identical
        if not p and not q:
            return True
        
        # One None → not identical
        if not p or not q:
            return False
        
        # Node values differ → not identical
        if p.val != q.val:
            return False
        
        # Recursively check children
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))```python         
```
# Recursion Algorithm

Check if both nodes are None:

If yes → this part of the tree matches → return True.

Check if only one of the nodes is None:

If one exists and the other doesn’t → structure is different → return False.

Compare the node values:

If p.val != q.val → values differ → return False.

If values match:

Recursively check:

Are the left subtrees the same? → self.isSameTree(p.left, q.left)

Are the right subtrees the same? → self.isSameTree(p.right, q.right)

Return True only if BOTH sides return True


If at any point:

Structure doesn't match

Or values don’t match
→ the function returns False immediately.
## Iterative Approach
```
class Solution(object):
    def isSameTree(self, p, q):
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            # Both None → continue
            if not node1 and not node2:
                continue
            
            # One None or values differ → not identical
            if not node1 or not node2 or node1.val != node2.val:
                return False

            # Push children to stack
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True
```
# Algorithm Summary

Compare the roots of both trees.

If both are None, continue.

If only one is None, return False.

If values differ, return False.

Compare left children.

Compare right children.

Continue until all node pairs are processed.

If no mismatch → return True.

Time & Space Complexity
Approach	Time Complexity	Space Complexity	Notes
Recursive DFS	O(n)	O(h) (h = height of tree)	Cleanest approach
Iterative DFS	O(n)	O(n) worst-case	Avoids recursion limits

Where n = number of nodes.
