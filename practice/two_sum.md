#  Two Sum

**LeetCode Question:** [Two Sum](https://leetcode.com/problems/two-sum/)

---

##  Problem Statement
Given an array of integers `nums` and an integer `target`, return **indices of the two numbers** such that they add up to `target`.  

**Constraints:**
- Each input has **exactly one solution**.  
- You **cannot use the same element twice**.

---

## Intuition
- **Brute Force Idea:** Check all possible pairs → O(n²) time.  
- **Optimized Idea:** Use a **hash map** to remember numbers we’ve seen.  
  - For each number, check if `target - num` exists in the map.  
  - If yes → return indices.  
  - If no → store `num` in the map and continue.

**Step-by-step Example:**

nums = [2, 7, 11, 15], target = 9
seen = {}

Step 1: num = 2 → complement = 7 → 7 not in seen → add 2:0 → seen = {2:0}
Step 2: num = 7 → complement = 2 → 2 is in seen → pair found → return [0,1]


---

##  Approach 1: Brute Force

**Step-by-step:**

nums = [2, 7, 11, 15], target = 9

i = 0, j = 1 → nums[0]+nums[1] = 2+7 = 9 → match → return [0,1]


**Code:**
```python
  def two_sum_bruteforce(nums, target):
      n = len(nums)
      for i in range(n):
          for j in range(i+1, n):
              if nums[i] + nums[j] == target:
                  return [i, j]
      return []
```
# Example 
print(two_sum_bruteforce([2,7,11,15], 9))  # Output: [0,1]

Complexity:

   ⏱ Time: O(n²)

  🗂 Space: O(1)

Approach 2: Optimized (Hash Map)

Step-by-step:

nums = [2, 7, 11, 15], target = 9
seen = {}

Step 1: num = 2 → complement = 7 → 7 not in seen → add 2:0 → seen = {2:0}
Step 2: num = 7 → complement = 2 → 2 is in seen → pair found → return [0,1]
Step 3: num = 11 → not reached
Step 4: num = 15 → not reached

Code:
```python 
    def two_sum_optimized(nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
```
# Example
print(two_sum_optimized([2,7,11,15], 9))  # Output: [0,1]

Complexity:

  ⏱ Time: O(n)

  🗂 Space: O(n)

🧩 Pattern

  Type: Arrays + Hashing

  Template: Walk through array → check complement in hash map → add current number to hash map

  When to use: Anytime you need to find pairs efficiently in an array
