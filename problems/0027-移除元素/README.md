# 27. 移除元素

## 题目描述

<p>给你一个数组 <code>nums</code><em>&nbsp;</em>和一个值 <code>val</code>，你需要 <strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a></strong> 移除所有数值等于&nbsp;<code>val</code><em>&nbsp;</em>的元素。元素的顺序可能发生改变。然后返回&nbsp;<code>nums</code>&nbsp;中与&nbsp;<code>val</code>&nbsp;不同的元素的数量。</p>

<p>假设 <code>nums</code> 中不等于 <code>val</code> 的元素数量为 <code>k</code>，要通过此题，您需要执行以下操作：</p>

<ul>
	<li>更改 <code>nums</code> 数组，使 <code>nums</code> 的前 <code>k</code> 个元素包含不等于 <code>val</code> 的元素。<code>nums</code> 的其余元素和 <code>nums</code> 的大小并不重要。</li>
	<li>返回 <code>k</code>。</li>
</ul>

<p><strong>用户评测：</strong></p>

<p>评测机将使用以下代码测试您的解决方案：</p>

<pre>
int[] nums = [...]; // 输入数组
int val = ...; // 要移除的值
int[] expectedNums = [...]; // 长度正确的预期答案。
                            // 它以不等于 val 的值排序。

int k = removeElement(nums, val); // 调用你的实现

assert k == expectedNums.length;
sort(nums, 0, k); // 排序 nums 的前 k 个元素
for (int i = 0; i &lt; actualLength; i++) {
    assert nums[i] == expectedNums[i];
}</pre>

<p>如果所有的断言都通过，你的解决方案将会 <strong>通过</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,2,3], val = 3
<strong>输出：</strong>2, nums = [2,2,_,_]
<strong>解释：</strong>你的函数函数应该返回 k = 2, 并且 nums<em> </em>中的前两个元素均为 2。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,2,2,3,0,4,2], val = 2
<strong>输出：</strong>5, nums = [0,1,4,0,3,_,_,_]
<strong>解释：</strong>你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
注意这五个元素可以任意顺序返回。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>0 &lt;= val &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 双指针

## 提示

1. The problem statement clearly asks us to modify the array in-place and it also says that the element beyond the new length of the array can be anything. Given an element, we need to remove all the occurrences of it from the array. We don't technically need to <b>remove</b> that element per-say, right?
2. We can move all the occurrences of this element to the end of the array. Use two pointers!
<br><img src="https://assets.leetcode.com/uploads/2019/10/20/hint_remove_element.png" width="500"/>
3. Yet another direction of thought is to consider the elements to be removed as non-existent. In a single pass, if we keep copying the visible elements in-place, that should also solve this problem for us.

## 示例

```
[3,2,2,3]
3
[0,1,2,2,3,0,4,2]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
    }
};
```

### Java

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
```

### C

```c
int removeElement(int* nums, int numsSize, int val) {
    
}
```

### C#

```csharp
public class Solution {
    public int RemoveElement(int[] nums, int val) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    
};
```

### TypeScript

```typescript
function removeElement(nums: number[], val: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $val
     * @return Integer
     */
    function removeElement(&$nums, $val) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeElement(nums: IntArray, `val`: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int removeElement(List<int> nums, int val) {
    
  }
}
```

### Go

```golang
func removeElement(nums []int, val int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} val
# @return {Integer}
def remove_element(nums, val)
    
end
```

### Scala

```scala
object Solution {
    def removeElement(nums: Array[Int], `val`: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        
    }
}
```

### Cangjie

```cangjie
class Solution {
    func removeElement(nums: Array<Int64>, val: Int64): Int64 {

    }
}
```

