# 2059. 转化数字的最小运算数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，该数组由 <strong>互不相同</strong> 的数字组成。另给你两个整数 <code>start</code> 和 <code>goal</code> 。</p>

<p>整数 <code>x</code> 的值最开始设为 <code>start</code> ，你打算执行一些运算使 <code>x</code> 转化为 <code>goal</code> 。你可以对数字 <code>x</code> 重复执行下述运算：</p>

<p>如果 <code>0 &lt;= x &lt;= 1000</code> ，那么，对于数组中的任一下标 <code>i</code>（<code>0 &lt;= i &lt; nums.length</code>），可以将 <code>x</code> 设为下述任一值：</p>

<ul>
	<li><code>x + nums[i]</code></li>
	<li><code>x - nums[i]</code></li>
	<li><code>x ^ nums[i]</code>（按位异或 XOR）</li>
</ul>

<p>注意，你可以按任意顺序使用每个 <code>nums[i]</code> 任意次。使 <code>x</code> 越过 <code>0 &lt;= x &lt;= 1000</code> 范围的运算同样可以生效，但该该运算执行后将不能执行其他运算。</p>

<p>返回将 <code>x = start</code><em> </em>转化为<em> </em><code>goal</code><em> </em>的最小操作数；如果无法完成转化，则返回<em> </em><code>-1</code><em> </em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4,12], start = 2, goal = 12
<strong>输出：</strong>2
<strong>解释：</strong>
可以按 2 → 14 → 12 的转化路径进行，只需执行下述 2 次运算：
- 2 + 12 = 14
- 14 - 2 = 12
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,5,7], start = 0, goal = -4
<strong>输出：</strong>2
<strong>解释：</strong>
可以按 0 → 3 → -4 的转化路径进行，只需执行下述 2 次运算：
- 0 + 3 = 3
- 3 - 7 = -4
注意，最后一步运算使 x 超过范围 0 &lt;= x &lt;= 1000 ，但该运算仍然可以生效。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,8,16], start = 0, goal = 1
<strong>输出：</strong>-1
<strong>解释：</strong>
无法将 0 转化为 1</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i], goal &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= start &lt;= 1000</code></li>
	<li><code>start != goal</code></li>
	<li><code>nums</code> 中的所有整数互不相同</li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 数组

## 提示

1. Once x drops below 0 or goes above 1000, is it possible to continue performing operations on x?
2. How can you use BFS to find the minimum operations?

## 示例

```
[2,4,12]
2
12
[3,5,7]
0
-4
[2,8,16]
0
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums, int start, int goal) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumOperations(int[] nums, int start, int goal) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumOperations(self, nums, start, goal):
        """
        :type nums: List[int]
        :type start: int
        :type goal: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        
```

### C

```c
int minimumOperations(int* nums, int numsSize, int start, int goal) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumOperations(int[] nums, int start, int goal) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} start
 * @param {number} goal
 * @return {number}
 */
var minimumOperations = function(nums, start, goal) {
    
};
```

### TypeScript

```typescript
function minimumOperations(nums: number[], start: number, goal: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $start
     * @param Integer $goal
     * @return Integer
     */
    function minimumOperations($nums, $start, $goal) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumOperations(_ nums: [Int], _ start: Int, _ goal: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumOperations(nums: IntArray, start: Int, goal: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumOperations(List<int> nums, int start, int goal) {
    
  }
}
```

### Go

```golang
func minimumOperations(nums []int, start int, goal int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} start
# @param {Integer} goal
# @return {Integer}
def minimum_operations(nums, start, goal)
    
end
```

### Scala

```scala
object Solution {
    def minimumOperations(nums: Array[Int], start: Int, goal: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>, start: i32, goal: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-operations nums start goal)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_operations(Nums :: [integer()], Start :: integer(), Goal :: integer()) -> integer().
minimum_operations(Nums, Start, Goal) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(nums :: [integer], start :: integer, goal :: integer) :: integer
  def minimum_operations(nums, start, goal) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumOperations(nums: Array<Int64>, start: Int64, goal: Int64): Int64 {

    }
}
```

