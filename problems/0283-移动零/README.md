# 283. 移动零

## 题目描述

<p>给定一个数组 <code>nums</code>，编写一个函数将所有 <code>0</code> 移动到数组的末尾，同时保持非零元素的相对顺序。</p>

<p><strong>请注意</strong>&nbsp;，必须在不复制数组的情况下原地对数组进行操作。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = <code>[0,1,0,3,12]</code>
<strong>输出:</strong> <code>[1,3,12,0,0]</code>
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = <code>[0]</code>
<strong>输出:</strong> <code>[0]</code></pre>

<p>&nbsp;</p>

<p><strong>提示</strong>:</p>
<meta charset="UTF-8" />

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= nums[i] &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p>&nbsp;</p>

<p><b>进阶：</b>你能尽量减少完成的操作次数吗？</p>


## 难度

Easy

## 标签

- 数组
- 双指针

## 提示

1. <b>In-place</b> means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.
2. A <b>two-pointer</b> approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.

## 示例

```
[0,1,0,3,12]
[0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public void moveZeroes(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
```

### Python3

```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
```

### C

```c
void moveZeroes(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public void MoveZeroes(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    
};
```

### TypeScript

```typescript
/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    function moveZeroes(&$nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func moveZeroes(_ nums: inout [Int]) {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun moveZeroes(nums: IntArray): Unit {
        
    }
}
```

### Dart

```dart
class Solution {
  void moveZeroes(List<int> nums) {
    
  }
}
```

### Go

```golang
func moveZeroes(nums []int)  {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
    
end
```

### Scala

```scala
object Solution {
    def moveZeroes(nums: Array[Int]): Unit = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        
    }
}
```

### Cangjie

```cangjie
class Solution {
    func moveZeroes(nums: Array<Int64>): Unit {

    }
}
```

