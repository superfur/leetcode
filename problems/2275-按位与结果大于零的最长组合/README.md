# 2275. 按位与结果大于零的最长组合

## 题目描述

<p>对数组&nbsp;<code>nums</code> 执行 <strong>按位与</strong> 相当于对数组&nbsp;<code>nums</code> 中的所有整数执行 <strong>按位与</strong> 。</p>

<ul>
	<li>例如，对 <code>nums = [1, 5, 3]</code> 来说，按位与等于 <code>1 &amp; 5 &amp; 3 = 1</code> 。</li>
	<li>同样，对 <code>nums = [7]</code> 而言，按位与等于 <code>7</code> 。</li>
</ul>

<p>给你一个正整数数组 <code>candidates</code> 。计算 <code>candidates</code> 中的数字每种组合下 <strong>按位与</strong> 的结果。</p>

<p>返回按位与结果大于 <code>0</code> 的 <strong>最长</strong> 组合的长度<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>candidates = [16,17,71,62,12,24,14]
<strong>输出：</strong>4
<strong>解释：</strong>组合 [16,17,62,24] 的按位与结果是 16 &amp; 17 &amp; 62 &amp; 24 = 16 &gt; 0 。
组合长度是 4 。
可以证明不存在按位与结果大于 0 且长度大于 4 的组合。
注意，符合长度最大的组合可能不止一种。
例如，组合 [62,12,24,14] 的按位与结果是 62 &amp; 12 &amp; 24 &amp; 14 = 8 &gt; 0 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>candidates = [8,8]
<strong>输出：</strong>2
<strong>解释：</strong>最长组合是 [8,8] ，按位与结果 8 &amp; 8 = 8 &gt; 0 。
组合长度是 2 ，所以返回 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= candidates.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= candidates[i] &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 哈希表
- 计数

## 提示

1. For the bitwise AND to be greater than zero, at least one bit should be 1 for every number in the combination.
2. The candidates are 24 bits long, so for every bit position, we can calculate the size of the largest combination such that the bitwise AND will have a 1 at that bit position.

## 示例

```
[16,17,71,62,12,24,14]
[8,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestCombination(int[] candidates) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
```

### C

```c
int largestCombination(int* candidates, int candidatesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestCombination(int[] candidates) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} candidates
 * @return {number}
 */
var largestCombination = function(candidates) {
    
};
```

### TypeScript

```typescript
function largestCombination(candidates: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $candidates
     * @return Integer
     */
    function largestCombination($candidates) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestCombination(_ candidates: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestCombination(candidates: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestCombination(List<int> candidates) {
    
  }
}
```

### Go

```golang
func largestCombination(candidates []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} candidates
# @return {Integer}
def largest_combination(candidates)
    
end
```

### Scala

```scala
object Solution {
    def largestCombination(candidates: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_combination(candidates: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-combination candidates)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_combination(Candidates :: [integer()]) -> integer().
largest_combination(Candidates) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_combination(candidates :: [integer]) :: integer
  def largest_combination(candidates) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestCombination(candidates: Array<Int64>): Int64 {

    }
}
```

