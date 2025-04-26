# 2860. 让所有学生保持开心的分组方法数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数数组 <code>nums</code> ，其中 <code>n</code> 是班级中学生的总数。班主任希望能够在让所有学生保持开心的情况下选出一组学生：</p>

<p>如果能够满足下述两个条件之一，则认为第 <code>i</code> 位学生将会保持开心：</p>

<ul>
	<li>这位学生被选中，并且被选中的学生人数 <strong>严格大于</strong> <code>nums[i]</code> 。</li>
	<li>这位学生没有被选中，并且被选中的学生人数 <strong>严格小于</strong> <code>nums[i]</code> 。</li>
</ul>

<p>返回能够满足让所有学生保持开心的分组方法的数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1]
<strong>输出：</strong>2
<strong>解释：</strong>
有两种可行的方法：
班主任没有选中学生。
班主任选中所有学生形成一组。 
如果班主任仅选中一个学生来完成分组，那么两个学生都无法保持开心。因此，仅存在两种可行的方法。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [6,0,3,3,6,7,2,7]
<strong>输出：</strong>3
<strong>解释：</strong>
存在三种可行的方法：
班主任选中下标为 1 的学生形成一组。
班主任选中下标为 1、2、3、6 的学生形成一组。
班主任选中所有学生形成一组。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt; nums.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 枚举
- 排序

## 提示

1. If a student with <code>nums[i] = x</code> is selected, all the students with <code>nums[j] <= x</code> must be selected.
2. If a student with <code>nums[i] = x</code> is not selected, all the students with <code>nums[j] >= x</code> must not be selected.
3. Sort values in <code>nums</code> and try all possible values for <code>x</code> from <code>0</code> to <code>n</code> separately.

## 示例

```
[1,1]
[6,0,3,3,6,7,2,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countWays(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countWays(List<Integer> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countWays(self, nums: List[int]) -> int:
        
```

### C

```c
int countWays(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountWays(IList<int> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countWays = function(nums) {
    
};
```

### TypeScript

```typescript
function countWays(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countWays($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countWays(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countWays(nums: List<Int>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countWays(List<int> nums) {
    
  }
}
```

### Go

```golang
func countWays(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_ways(nums)
    
end
```

### Scala

```scala
object Solution {
    def countWays(nums: List[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_ways(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-ways nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_ways(Nums :: [integer()]) -> integer().
count_ways(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_ways(nums :: [integer]) :: integer
  def count_ways(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countWays(nums: ArrayList<Int64>): Int64 {

    }
}
```

