# 面试题 10.11. 峰与谷

## 题目描述

<p>在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。例如，在数组{5, 8, 4, 2, 3, 4, 6}中，{8, 6}是峰， {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>[5, 3, 1, 2, 3]
<strong>输出：</strong>[5, 1, 3, 2, 3]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums.length &lt;= 10000</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. 假设数组按升序排序。有什么办法可以把它调整为交替的高峰和低谷？
2. 尝试遍历排序的数组。你可以交换元素直到将数组调整好吗？
3. 请注意，如果确保山峰位置正确，那么山谷也会在正确位置。因此，对数组x的迭代可以跳过每一个其他元素。
4. 你是否一定要对数组进行排序？你可以用一个未排序的数组来做到这一点吗？
5. 假设你有{0, 1, 2}三个元素的序列，以任意顺序排列。写出这些元素所有可能的排列，以及如何把它们变成1是波峰的形式。
6. 重新访问你刚才写出的{0, 1, 2}序列。想象一下有元素在最左边的元素之前。你能确保交换元素的方式不会使数组的前一部分失效吗？
7. 你应该可以设计一个O(n) 的算法。

## 示例

```
[3,5,2,1,6,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public void wiggleSort(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
```

### Python3

```python3
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
```

### C

```c
void wiggleSort(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public void WiggleSort(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var wiggleSort = function(nums) {
    
};
```

### TypeScript

```typescript
/**
 Do not return anything, modify nums in-place instead.
 */
function wiggleSort(nums: number[]): void {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    function wiggleSort(&$nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func wiggleSort(_ nums: inout [Int]) {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun wiggleSort(nums: IntArray): Unit {
        
    }
}
```

### Dart

```dart
class Solution {
  void wiggleSort(List<int> nums) {
    
  }
}
```

### Go

```golang
func wiggleSort(nums []int)  {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def wiggle_sort(nums)
    
end
```

### Scala

```scala
object Solution {
    def wiggleSort(nums: Array[Int]): Unit = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn wiggle_sort(nums: &mut Vec<i32>) {
        
    }
}
```

### Cangjie

```cangjie
class Solution {
    func wiggleSort(nums: Array<Int64>): Unit {

    }
}
```

