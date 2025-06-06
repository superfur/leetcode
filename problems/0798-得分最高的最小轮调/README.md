# 798. 得分最高的最小轮调

## 题目描述

<p>给你一个数组&nbsp;<code>nums</code>，我们可以将它按一个非负整数 <code>k</code> 进行轮调，这样可以使数组变为&nbsp;<code>[nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]]</code>&nbsp;的形式。此后，任何值小于或等于其索引的项都可以记作一分。</p>

<ul>
	<li>例如，数组为&nbsp;<code>nums = [2,4,1,3,0]</code>，我们按&nbsp;<code>k = 2</code>&nbsp;进行轮调后，它将变成&nbsp;<code>[1,3,0,2,4]</code>。这将记为 <code>3</code> 分，因为 <code>1 &gt; 0</code> [不计分]、<code>3 &gt; 1</code> [不计分]、<code>0 &lt;= 2</code> [计 1 分]、<code>2 &lt;= 3</code> [计 1 分]，<code>4 &lt;= 4</code> [计 1 分]。</li>
</ul>

<p>在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调下标 <code>k</code> 。如果有多个答案，返回满足条件的最小的下标 <code>k</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,1,4,0]
<strong>输出：</strong>3
<strong>解释：</strong>
下面列出了每个 k 的得分：
k = 0,  nums = [2,3,1,4,0],    score 2
k = 1,  nums = [3,1,4,0,2],    score 3
k = 2,  nums = [1,4,0,2,3],    score 3
k = 3,  nums = [4,0,2,3,1],    score 4
k = 4,  nums = [0,2,3,1,4],    score 3
所以我们应当选择&nbsp;k = 3，得分最高。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,0,2,4]
<strong>输出：</strong>0
<strong>解释：</strong>
nums 无论怎么变化总是有 3 分。
所以我们将选择最小的 k，即 0。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt; nums.length</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 前缀和

## 示例

```
[2,3,1,4,0]
[1,3,0,2,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int bestRotation(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int bestRotation(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def bestRotation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        
```

### C

```c
int bestRotation(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int BestRotation(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var bestRotation = function(nums) {
    
};
```

### TypeScript

```typescript
function bestRotation(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function bestRotation($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func bestRotation(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun bestRotation(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int bestRotation(List<int> nums) {
    
  }
}
```

### Go

```golang
func bestRotation(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def best_rotation(nums)
    
end
```

### Scala

```scala
object Solution {
    def bestRotation(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn best_rotation(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (best-rotation nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec best_rotation(Nums :: [integer()]) -> integer().
best_rotation(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec best_rotation(nums :: [integer]) :: integer
  def best_rotation(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func bestRotation(nums: Array<Int64>): Int64 {

    }
}
```

