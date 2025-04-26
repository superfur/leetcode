# 1547. 切棍子的最小成本

## 题目描述

<p>有一根长度为 <code>n</code> 个单位的木棍，棍上从 <code>0</code> 到 <code>n</code> 标记了若干位置。例如，长度为 <strong>6</strong> 的棍子可以标记如下：</p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/09/statement.jpg" style="height: 111px; width: 521px;" /></p>

<p>给你一个整数数组 <code>cuts</code> ，其中 <code>cuts[i]</code> 表示你需要将棍子切开的位置。</p>

<p>你可以按顺序完成切割，也可以根据需要更改切割的顺序。</p>

<p>每次切割的成本都是当前要切割的棍子的长度，切棍子的总成本是历次切割成本的总和。对棍子进行切割将会把一根木棍分成两根较小的木棍（这两根木棍的长度和就是切割前木棍的长度）。请参阅第一个示例以获得更直观的解释。</p>

<p>返回切棍子的 <strong>最小总成本</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/09/e1.jpg" style="height: 284px; width: 350px;" /></p>

<pre>
<strong>输入：</strong>n = 7, cuts = [1,3,4,5]
<strong>输出：</strong>16
<strong>解释：</strong>按 [1, 3, 4, 5] 的顺序切割的情况如下所示：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/09/e11.jpg" style="height: 284px; width: 350px;" />
第一次切割长度为 7 的棍子，成本为 7 。第二次切割长度为 6 的棍子（即第一次切割得到的第二根棍子），第三次切割为长度 4 的棍子，最后切割长度为 3 的棍子。总成本为 7 + 6 + 4 + 3 = 20 。
而将切割顺序重新排列为 [3, 5, 1, 4] 后，总成本 = 16（如示例图中 7 + 4 + 3 + 2 = 16）。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 9, cuts = [5,6,1,4,2]
<strong>输出：</strong>22
<strong>解释：</strong>如果按给定的顺序切割，则总成本为 25 。总成本 <= 25 的切割顺序很多，例如，[4, 6, 5, 2, 1] 的总成本 = 22，是所有可能方案中成本最小的。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= n <= 10^6</code></li>
	<li><code>1 <= cuts.length <= min(n - 1, 100)</code></li>
	<li><code>1 <= cuts[i] <= n - 1</code></li>
	<li><code>cuts</code> 数组中的所有整数都 <strong>互不相同</strong></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 排序

## 提示

1. Build a dp array where dp[i][j] is the minimum cost to achieve all the cuts between i and j.
2. When you try to get the minimum cost between i and j, try all possible cuts k between them, dp[i][j] = min(dp[i][k] + dp[k][j]) + (j - i) for all possible cuts k between them.

## 示例

```
7
[1,3,4,5]
9
[5,6,1,4,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCost(int n, vector<int>& cuts) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCost(int n, int[] cuts) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
```

### C

```c
int minCost(int n, int* cuts, int cutsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCost(int n, int[] cuts) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} cuts
 * @return {number}
 */
var minCost = function(n, cuts) {
    
};
```

### TypeScript

```typescript
function minCost(n: number, cuts: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $cuts
     * @return Integer
     */
    function minCost($n, $cuts) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCost(_ n: Int, _ cuts: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCost(n: Int, cuts: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCost(int n, List<int> cuts) {
    
  }
}
```

### Go

```golang
func minCost(n int, cuts []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} cuts
# @return {Integer}
def min_cost(n, cuts)
    
end
```

### Scala

```scala
object Solution {
    def minCost(n: Int, cuts: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost(n: i32, cuts: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost n cuts)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost(N :: integer(), Cuts :: [integer()]) -> integer().
min_cost(N, Cuts) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost(n :: integer, cuts :: [integer]) :: integer
  def min_cost(n, cuts) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCost(n: Int64, cuts: Array<Int64>): Int64 {

    }
}
```

