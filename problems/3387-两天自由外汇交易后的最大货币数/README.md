# 3387. 两天自由外汇交易后的最大货币数

## 题目描述

<p>给你一个字符串 <code>initialCurrency</code>，表示初始货币类型，并且你一开始拥有 <code>1.0</code> 单位的 <code>initialCurrency</code>。</p>

<p>另给你四个数组，分别表示货币对（字符串）和汇率（实数）：</p>

<ul>
	<li><code>pairs1[i] = [startCurrency<sub>i</sub>, targetCurrency<sub>i</sub>]</code> 表示在&nbsp;<strong>第 1 天</strong>，可以按照汇率 <code>rates1[i]</code> 将 <code>startCurrency<sub>i</sub></code> 转换为 <code>targetCurrency<sub>i</sub></code>。</li>
	<li><code>pairs2[i] = [startCurrency<sub>i</sub>, targetCurrency<sub>i</sub>]</code> 表示在&nbsp;<strong>第 2 天</strong>，可以按照汇率 <code>rates2[i]</code> 将 <code>startCurrency<sub>i</sub></code> 转换为 <code>targetCurrency<sub>i</sub></code>。</li>
	<li>此外，每种 <code>targetCurrency</code> 都可以以汇率 <code>1 / rate</code> 转换回对应的 <code>startCurrency</code>。</li>
</ul>

<p>你可以在&nbsp;<strong>第 1 天&nbsp;</strong>使用 <code>rates1</code> 进行任意次数的兑换（包括 0 次），然后在&nbsp;<strong>第 2 天&nbsp;</strong>使用 <code>rates2</code> 再进行任意次数的兑换（包括 0 次）。</p>

<p>返回在两天兑换后，最大可能拥有的 <code>initialCurrency</code> 的数量。</p>

<p><strong>注意：</strong>汇率是有效的，并且第 1 天和第 2 天的汇率之间相互独立，不会产生矛盾。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0]</span></p>

<p><strong>输出：</strong> <span class="example-io">720.00000</span></p>

<p><strong>解释：</strong></p>

<p>根据题目要求，需要最大化最终的 <strong>EUR</strong> 数量，从 1.0 <strong>EUR</strong> 开始：</p>

<ul>
	<li><strong>第 1 天：</strong>

	<ul>
		<li>将 <strong>EUR</strong> 换成 <strong>USD</strong>，得到 2.0&nbsp;<strong>USD</strong>。</li>
		<li>将 <strong>USD</strong> 换成 <strong>JPY</strong>，得到 6.0 <strong>JPY</strong>。</li>
	</ul>
	</li>
	<li><strong>第 2 天：</strong>
	<ul>
		<li>将 <strong>JPY</strong> 换成 <strong>USD</strong>，得到 24.0 <strong>USD</strong>。</li>
		<li>将 <strong>USD</strong> 换成 <strong>CHF</strong>，得到 120.0 <strong>CHF</strong>。</li>
		<li>最后将 <strong>CHF</strong> 换回 <strong>EUR</strong>，得到 720.0 <strong>EUR</strong>。</li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">initialCurrency = "NGN", pairs1 = [["NGN","EUR"]], rates1 = [9.0], pairs2 = [["NGN","EUR"]], rates2 = [6.0]</span></p>

<p><strong>输出：</strong> <span class="example-io">1.50000</span></p>

<p><strong>解释：</strong></p>

<p>在第 1 天将 <strong>NGN</strong> 换成 <strong>EUR</strong>，并在第 2 天用反向汇率将 <strong>EUR</strong> 换回 <strong>NGN</strong>，可以最大化最终的 <strong>NGN</strong> 数量。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0]</span></p>

<p><strong>输出：</strong> <span class="example-io">1.00000</span></p>

<p><strong>解释：</strong></p>

<p>在这个例子中，不需要在任何一天进行任何兑换。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= initialCurrency.length &lt;= 3</code></li>
	<li><code>initialCurrency</code> 仅由大写英文字母组成。</li>
	<li><code>1 &lt;= n == pairs1.length &lt;= 10</code></li>
	<li><code>1 &lt;= m == pairs2.length &lt;= 10</code></li>
	<li><code>pairs1[i] == [startCurrency<sub>i</sub>, targetCurrency<sub>i</sub>]</code></li>
	<li><code>pairs2[i] == [startCurrency<sub>i</sub>, targetCurrency<sub>i</sub>]</code></li>
	<li><code>1 &lt;= startCurrency<sub>i</sub>.length, targetCurrency<sub>i</sub>.length &lt;= 3</code></li>
	<li><code>startCurrency<sub>i</sub></code> 和 <code>targetCurrency<sub>i</sub></code> 仅由大写英文字母组成。</li>
	<li><code>rates1.length == n</code></li>
	<li><code>rates2.length == m</code></li>
	<li><code>1.0 &lt;= rates1[i], rates2[i] &lt;= 10.0</code></li>
	<li>输入保证两个转换图在各自的天数中没有矛盾或循环。</li>
	<li>输入保证输出&nbsp;<strong>最大</strong>&nbsp;为&nbsp;<code>5 * 10<sup>10</sup></code>。</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 数组
- 字符串

## 提示

1. Choose an intermediate currency. Convert from <code>initialCurrency</code> to this currency on day 1, and from that currency back to <code>initialCurrency</code> on day 2.
2. Use a DFS/BFS to calculate the direct conversion rate between any two currencies.

## 示例

```
"EUR"
[["EUR","USD"],["USD","JPY"]]
[2.0,3.0]
[["JPY","USD"],["USD","CHF"],["CHF","EUR"]]
[4.0,5.0,6.0]
"NGN"
[["NGN","EUR"]]
[9.0]
[["NGN","EUR"]]
[6.0]
"USD"
[["USD","EUR"]]
[1.0]
[["EUR","JPY"]]
[10.0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1, vector<vector<string>>& pairs2, vector<double>& rates2) {
        
    }
};
```

### Java

```java
class Solution {
    public double maxAmount(String initialCurrency, List<List<String>> pairs1, double[] rates1, List<List<String>> pairs2, double[] rates2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2):
        """
        :type initialCurrency: str
        :type pairs1: List[List[str]]
        :type rates1: List[float]
        :type pairs2: List[List[str]]
        :type rates2: List[float]
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        
```

### C

```c
double maxAmount(char* initialCurrency, char*** pairs1, int pairs1Size, int* pairs1ColSize, double* rates1, int rates1Size, char*** pairs2, int pairs2Size, int* pairs2ColSize, double* rates2, int rates2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public double MaxAmount(string initialCurrency, IList<IList<string>> pairs1, double[] rates1, IList<IList<string>> pairs2, double[] rates2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} initialCurrency
 * @param {string[][]} pairs1
 * @param {number[]} rates1
 * @param {string[][]} pairs2
 * @param {number[]} rates2
 * @return {number}
 */
var maxAmount = function(initialCurrency, pairs1, rates1, pairs2, rates2) {
    
};
```

### TypeScript

```typescript
function maxAmount(initialCurrency: string, pairs1: string[][], rates1: number[], pairs2: string[][], rates2: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $initialCurrency
     * @param String[][] $pairs1
     * @param Float[] $rates1
     * @param String[][] $pairs2
     * @param Float[] $rates2
     * @return Float
     */
    function maxAmount($initialCurrency, $pairs1, $rates1, $pairs2, $rates2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxAmount(_ initialCurrency: String, _ pairs1: [[String]], _ rates1: [Double], _ pairs2: [[String]], _ rates2: [Double]) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxAmount(initialCurrency: String, pairs1: List<List<String>>, rates1: DoubleArray, pairs2: List<List<String>>, rates2: DoubleArray): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double maxAmount(String initialCurrency, List<List<String>> pairs1, List<double> rates1, List<List<String>> pairs2, List<double> rates2) {
    
  }
}
```

### Go

```golang
func maxAmount(initialCurrency string, pairs1 [][]string, rates1 []float64, pairs2 [][]string, rates2 []float64) float64 {
    
}
```

### Ruby

```ruby
# @param {String} initial_currency
# @param {String[][]} pairs1
# @param {Float[]} rates1
# @param {String[][]} pairs2
# @param {Float[]} rates2
# @return {Float}
def max_amount(initial_currency, pairs1, rates1, pairs2, rates2)
    
end
```

### Scala

```scala
object Solution {
    def maxAmount(initialCurrency: String, pairs1: List[List[String]], rates1: Array[Double], pairs2: List[List[String]], rates2: Array[Double]): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_amount(initial_currency: String, pairs1: Vec<Vec<String>>, rates1: Vec<f64>, pairs2: Vec<Vec<String>>, rates2: Vec<f64>) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-amount initialCurrency pairs1 rates1 pairs2 rates2)
  (-> string? (listof (listof string?)) (listof flonum?) (listof (listof string?)) (listof flonum?) flonum?)
  )
```

### Erlang

```erlang
-spec max_amount(InitialCurrency :: unicode:unicode_binary(), Pairs1 :: [[unicode:unicode_binary()]], Rates1 :: [float()], Pairs2 :: [[unicode:unicode_binary()]], Rates2 :: [float()]) -> float().
max_amount(InitialCurrency, Pairs1, Rates1, Pairs2, Rates2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_amount(initial_currency :: String.t, pairs1 :: [[String.t]], rates1 :: [float], pairs2 :: [[String.t]], rates2 :: [float]) :: float
  def max_amount(initial_currency, pairs1, rates1, pairs2, rates2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxAmount(initialCurrency: String, pairs1: ArrayList<ArrayList<String>>, rates1: Array<Float64>, pairs2: ArrayList<ArrayList<String>>, rates2: Array<Float64>): Float64 {

    }
}
```

