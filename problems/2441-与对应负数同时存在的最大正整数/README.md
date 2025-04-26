# 2441. 与对应负数同时存在的最大正整数

## 题目描述

<p>给你一个 <strong>不包含</strong> 任何零的整数数组 <code>nums</code> ，找出自身与对应的负数都在数组中存在的最大正整数 <code>k</code> 。</p>

<p>返回正整数<em> </em><code>k</code> ，如果不存在这样的整数，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,2,-3,3]
<strong>输出：</strong>3
<strong>解释：</strong>3 是数组中唯一一个满足题目要求的 k 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,10,6,7,-7,1]
<strong>输出：</strong>7
<strong>解释：</strong>数组中存在 1 和 7 对应的负数，7 的值更大。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [-10,8,6,7,-2,-3]
<strong>输出：</strong>-1
<strong>解释：</strong>不存在满足题目要求的 k ，返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>nums[i] != 0</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 双指针
- 排序

## 提示

1. What data structure can help you to determine if an element exists?
2. Would a hash table help?

## 示例

```
[-1,2,-3,3]
[-1,10,6,7,-7,1]
[-10,8,6,7,-2,-3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMaxK(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMaxK(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
```

### C

```c
int findMaxK(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMaxK(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxK = function(nums) {
    
};
```

### TypeScript

```typescript
function findMaxK(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaxK($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMaxK(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaxK(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMaxK(List<int> nums) {
    
  }
}
```

### Go

```golang
func findMaxK(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_max_k(nums)
    
end
```

### Scala

```scala
object Solution {
    def findMaxK(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_max_k(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-max-k nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_max_k(Nums :: [integer()]) -> integer().
find_max_k(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_max_k(nums :: [integer]) :: integer
  def find_max_k(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMaxK(nums: Array<Int64>): Int64 {

    }
}
```

