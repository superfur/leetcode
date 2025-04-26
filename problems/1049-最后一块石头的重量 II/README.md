# 1049. 最后一块石头的重量 II

## 题目描述

<p>有一堆石头，用整数数组&nbsp;<code>stones</code> 表示。其中&nbsp;<code>stones[i]</code> 表示第 <code>i</code> 块石头的重量。</p>

<p>每一回合，从中选出<strong>任意两块石头</strong>，然后将它们一起粉碎。假设石头的重量分别为&nbsp;<code>x</code> 和&nbsp;<code>y</code>，且&nbsp;<code>x &lt;= y</code>。那么粉碎的可能结果如下：</p>

<ul>
	<li>如果&nbsp;<code>x == y</code>，那么两块石头都会被完全粉碎；</li>
	<li>如果&nbsp;<code>x != y</code>，那么重量为&nbsp;<code>x</code>&nbsp;的石头将会完全粉碎，而重量为&nbsp;<code>y</code>&nbsp;的石头新重量为&nbsp;<code>y-x</code>。</li>
</ul>

<p>最后，<strong>最多只会剩下一块 </strong>石头。返回此石头 <strong>最小的可能重量 </strong>。如果没有石头剩下，就返回 <code>0</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>stones = [2,7,4,1,8,1]
<strong>输出：</strong>1
<strong>解释：</strong>
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>stones = [31,26,33,21,40]
<strong>输出：</strong>5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= stones.length &lt;= 30</code></li>
	<li><code>1 &lt;= stones[i] &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Think of the final answer as a sum of weights with + or - sign symbols infront of each weight.  Actually, all sums with 1 of each sign symbol are possible.
2. Use dynamic programming: for every possible sum with N stones, those sums +x or -x is possible with N+1 stones, where x is the value of the newest stone.  (This overcounts sums that are all positive or all negative, but those don't matter.)

## 示例

```
[2,7,4,1,8,1]
[31,26,33,21,40]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        
    }
};
```

### Java

```java
class Solution {
    public int lastStoneWeightII(int[] stones) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
```

### C

```c
int lastStoneWeightII(int* stones, int stonesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LastStoneWeightII(int[] stones) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeightII = function(stones) {
    
};
```

### TypeScript

```typescript
function lastStoneWeightII(stones: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function lastStoneWeightII($stones) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lastStoneWeightII(_ stones: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lastStoneWeightII(stones: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int lastStoneWeightII(List<int> stones) {
    
  }
}
```

### Go

```golang
func lastStoneWeightII(stones []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} stones
# @return {Integer}
def last_stone_weight_ii(stones)
    
end
```

### Scala

```scala
object Solution {
    def lastStoneWeightII(stones: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn last_stone_weight_ii(stones: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (last-stone-weight-ii stones)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec last_stone_weight_ii(Stones :: [integer()]) -> integer().
last_stone_weight_ii(Stones) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec last_stone_weight_ii(stones :: [integer]) :: integer
  def last_stone_weight_ii(stones) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lastStoneWeightII(stones: Array<Int64>): Int64 {

    }
}
```

