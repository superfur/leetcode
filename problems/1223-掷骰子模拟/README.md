# 1223. 掷骰子模拟

## 题目描述

<p>有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。</p>

<p>不过我们在使用它时有个约束，就是使得投掷骰子时，<strong>连续</strong> 掷出数字&nbsp;<code>i</code>&nbsp;的次数不能超过&nbsp;<code>rollMax[i]</code>（<code>i</code>&nbsp;从 1 开始编号）。</p>

<p>现在，给你一个整数数组&nbsp;<code>rollMax</code>&nbsp;和一个整数&nbsp;<code>n</code>，请你来计算掷&nbsp;<code>n</code>&nbsp;次骰子可得到的不同点数序列的数量。</p>

<p>假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 <strong>模&nbsp;<code>10^9 + 7</code></strong>&nbsp;之后的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 2, rollMax = [1,1,2,2,2,3]
<strong>输出：</strong>34
<strong>解释：</strong>我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2 最多连续出现一次，所以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 2, rollMax = [1,1,1,1,1,1]
<strong>输出：</strong>30
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 3, rollMax = [1,1,1,2,2,3]
<strong>输出：</strong>181
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>rollMax.length == 6</code></li>
	<li><code>1 &lt;= rollMax[i] &lt;= 15</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. Think on Dynamic Programming.
2. DP(pos, last) which means we are at the position pos having as last the last character seen.

## 示例

```
2
[1,1,2,2,2,3]
2
[1,1,1,1,1,1]
3
[1,1,1,2,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int dieSimulator(int n, vector<int>& rollMax) {
        
    }
};
```

### Java

```java
class Solution {
    public int dieSimulator(int n, int[] rollMax) {
        
    }
}
```

### Python

```python
class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
```

### C

```c
int dieSimulator(int n, int* rollMax, int rollMaxSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int DieSimulator(int n, int[] rollMax) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} rollMax
 * @return {number}
 */
var dieSimulator = function(n, rollMax) {
    
};
```

### TypeScript

```typescript
function dieSimulator(n: number, rollMax: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $rollMax
     * @return Integer
     */
    function dieSimulator($n, $rollMax) {
        
    }
}
```

### Swift

```swift
class Solution {
    func dieSimulator(_ n: Int, _ rollMax: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun dieSimulator(n: Int, rollMax: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int dieSimulator(int n, List<int> rollMax) {
    
  }
}
```

### Go

```golang
func dieSimulator(n int, rollMax []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} roll_max
# @return {Integer}
def die_simulator(n, roll_max)
    
end
```

### Scala

```scala
object Solution {
    def dieSimulator(n: Int, rollMax: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn die_simulator(n: i32, roll_max: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (die-simulator n rollMax)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec die_simulator(N :: integer(), RollMax :: [integer()]) -> integer().
die_simulator(N, RollMax) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec die_simulator(n :: integer, roll_max :: [integer]) :: integer
  def die_simulator(n, roll_max) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func dieSimulator(n: Int64, rollMax: Array<Int64>): Int64 {

    }
}
```

