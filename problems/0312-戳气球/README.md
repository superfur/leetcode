# 312. 戳气球

## 题目描述

<p>有 <code>n</code> 个气球，编号为<code>0</code> 到 <code>n - 1</code>，每个气球上都标有一个数字，这些数字存在数组&nbsp;<code>nums</code>&nbsp;中。</p>

<p>现在要求你戳破所有的气球。戳破第 <code>i</code> 个气球，你可以获得&nbsp;<code>nums[i - 1] * nums[i] * nums[i + 1]</code> 枚硬币。&nbsp;这里的 <code>i - 1</code> 和 <code>i + 1</code> 代表和&nbsp;<code>i</code>&nbsp;相邻的两个气球的序号。如果 <code>i - 1</code>或 <code>i + 1</code> 超出了数组的边界，那么就当它是一个数字为 <code>1</code> 的气球。</p>

<p>求所能获得硬币的最大数量。</p>

<p>&nbsp;</p>
<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [3,1,5,8]
<strong>输出：</strong>167
<strong>解释：</strong>
nums = [3,1,5,8] --&gt; [3,5,8] --&gt; [3,8] --&gt; [8] --&gt; []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5]
<strong>输出：</strong>10
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 示例

```
[3,1,5,8]
[1,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxCoins(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
```

### C

```c
int maxCoins(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxCoins(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxCoins = function(nums) {
    
};
```

### TypeScript

```typescript
function maxCoins(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxCoins($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxCoins(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxCoins(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxCoins(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxCoins(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_coins(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxCoins(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_coins(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-coins nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_coins(Nums :: [integer()]) -> integer().
max_coins(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_coins(nums :: [integer]) :: integer
  def max_coins(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxCoins(nums: Array<Int64>): Int64 {

    }
}
```

