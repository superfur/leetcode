# 287. 寻找重复数

## 题目描述

<p>给定一个包含&nbsp;<code>n + 1</code> 个整数的数组&nbsp;<code>nums</code> ，其数字都在&nbsp;<code>[1, n]</code>&nbsp;范围内（包括 <code>1</code> 和 <code>n</code>），可知至少存在一个重复的整数。</p>

<p>假设 <code>nums</code> 只有 <strong>一个重复的整数</strong> ，返回&nbsp;<strong>这个重复的数</strong> 。</p>

<p>你设计的解决方案必须 <strong>不修改</strong> 数组 <code>nums</code> 且只用常量级 <code>O(1)</code> 的额外空间。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,4,2,2]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,1,3,4,2]
<strong>输出：</strong>3
</pre>

<p><strong>示例 3 :</strong></p>

<pre>
<strong>输入：</strong>nums = [3,3,3,3,3]
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>nums.length == n + 1</code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
	<li><code>nums</code> 中 <strong>只有一个整数</strong> 出现 <strong>两次或多次</strong> ，其余整数均只出现 <strong>一次</strong></li>
</ul>

<p>&nbsp;</p>

<p><b>进阶：</b></p>

<ul>
	<li>如何证明 <code>nums</code> 中至少存在一个重复的数字?</li>
	<li>你可以设计一个线性级时间复杂度 <code>O(n)</code> 的解决方案吗？</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 双指针
- 二分查找

## 示例

```
[1,3,4,2,2]
[3,1,3,4,2]
[3,3,3,3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findDuplicate(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
```

### C

```c
int findDuplicate(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindDuplicate(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    
};
```

### TypeScript

```typescript
function findDuplicate(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findDuplicate($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findDuplicate(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findDuplicate(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findDuplicate(List<int> nums) {
    
  }
}
```

### Go

```golang
func findDuplicate(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_duplicate(nums)
    
end
```

### Scala

```scala
object Solution {
    def findDuplicate(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_duplicate(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-duplicate nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_duplicate(Nums :: [integer()]) -> integer().
find_duplicate(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_duplicate(nums :: [integer]) :: integer
  def find_duplicate(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findDuplicate(nums: Array<Int64>): Int64 {

    }
}
```

