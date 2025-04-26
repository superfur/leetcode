# 75. 颜色分类

## 题目描述

<p>给定一个包含红色、白色和蓝色、共&nbsp;<code>n</code><em> </em>个元素的数组<meta charset="UTF-8" />&nbsp;<code>nums</code>&nbsp;，<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a>&nbsp;</strong>对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。</p>

<p>我们使用整数 <code>0</code>、&nbsp;<code>1</code> 和 <code>2</code> 分别表示红色、白色和蓝色。</p>

<ul>
</ul>

<p>必须在不使用库内置的 sort 函数的情况下解决这个问题。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,0,2,1,1,0]
<strong>输出：</strong>[0,0,1,1,2,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,0,1]
<strong>输出：</strong>[0,1,2]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>nums[i]</code> 为 <code>0</code>、<code>1</code> 或 <code>2</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你能想出一个仅使用常数空间的一趟扫描算法吗？</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 排序

## 提示

1. A rather straight forward solution is a two-pass algorithm using counting sort.
2. Iterate the array counting number of 0's, 1's, and 2's.
3. Overwrite array with the total number of 0's, then 1's and followed by 2's.

## 示例

```
[2,0,2,1,1,0]
[2,0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public void sortColors(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
```

### Python3

```python3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
```

### C

```c
void sortColors(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public void SortColors(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    
};
```

### TypeScript

```typescript
/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    function sortColors(&$nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sortColors(_ nums: inout [Int]) {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sortColors(nums: IntArray): Unit {
        
    }
}
```

### Dart

```dart
class Solution {
  void sortColors(List<int> nums) {
    
  }
}
```

### Go

```golang
func sortColors(nums []int)  {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def sort_colors(nums)
    
end
```

### Scala

```scala
object Solution {
    def sortColors(nums: Array[Int]): Unit = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        
    }
}
```

### Cangjie

```cangjie
class Solution {
    func sortColors(nums: Array<Int64>): Unit {

    }
}
```

