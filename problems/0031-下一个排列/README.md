# 31. 下一个排列

## 题目描述

<p>整数数组的一个 <strong>排列</strong>&nbsp; 就是将其所有成员以序列或线性顺序排列。</p>

<ul>
	<li>例如，<code>arr = [1,2,3]</code> ，以下这些都可以视作 <code>arr</code> 的排列：<code>[1,2,3]</code>、<code>[1,3,2]</code>、<code>[3,1,2]</code>、<code>[2,3,1]</code> 。</li>
</ul>

<p>整数数组的 <strong>下一个排列</strong> 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 <strong>下一个排列</strong> 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。</p>

<ul>
	<li>例如，<code>arr = [1,2,3]</code> 的下一个排列是 <code>[1,3,2]</code> 。</li>
	<li>类似地，<code>arr = [2,3,1]</code> 的下一个排列是 <code>[3,1,2]</code> 。</li>
	<li>而 <code>arr = [3,2,1]</code> 的下一个排列是 <code>[1,2,3]</code> ，因为 <code>[3,2,1]</code> 不存在一个字典序更大的排列。</li>
</ul>

<p>给你一个整数数组 <code>nums</code> ，找出 <code>nums</code> 的下一个排列。</p>

<p>必须<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank"> 原地 </a></strong>修改，只允许使用额外常数空间。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[1,3,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,1]
<strong>输出：</strong>[1,2,3]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,5]
<strong>输出：</strong>[1,5,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针

## 示例

```
[1,2,3]
[3,2,1]
[1,1,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public void nextPermutation(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
```

### Python3

```python3
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
```

### C

```c
void nextPermutation(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public void NextPermutation(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    
};
```

### TypeScript

```typescript
/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums: number[]): void {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    function nextPermutation(&$nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func nextPermutation(_ nums: inout [Int]) {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun nextPermutation(nums: IntArray): Unit {
        
    }
}
```

### Dart

```dart
class Solution {
  void nextPermutation(List<int> nums) {
    
  }
}
```

### Go

```golang
func nextPermutation(nums []int)  {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def next_permutation(nums)
    
end
```

### Scala

```scala
object Solution {
    def nextPermutation(nums: Array[Int]): Unit = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn next_permutation(nums: &mut Vec<i32>) {
        
    }
}
```

### Cangjie

```cangjie
class Solution {
    func nextPermutation(nums: Array<Int64>): Unit {

    }
}
```

