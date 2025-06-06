# 2412. 完成所有交易的初始最少钱数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code><font face="monospace">transactions</font></code>，其中<code>transactions[i] = [cost<sub>i</sub>, cashback<sub>i</sub>]</code>&nbsp;。</p>

<p>数组描述了若干笔交易。其中每笔交易必须以 <strong>某种顺序</strong> 恰好完成一次。在任意一个时刻，你有一定数目的钱&nbsp;<code>money</code>&nbsp;，为了完成交易&nbsp;<code>i</code>&nbsp;，<code>money &gt;= cost<sub>i</sub></code>&nbsp;这个条件必须为真。执行交易后，你的钱数&nbsp;<code>money</code> 变成&nbsp;<code>money - cost<sub>i</sub> + cashback<sub>i</sub></code><sub>&nbsp;</sub>。</p>

<p>请你返回 <strong>任意一种</strong> 交易顺序下，你都能完成所有交易的最少钱数<em>&nbsp;</em><code>money</code>&nbsp;是多少。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>transactions = [[2,1],[5,0],[4,2]]
<b>输出：</b>10
<strong>解释：
</strong>刚开始 money = 10 ，交易可以以任意顺序进行。
可以证明如果 money &lt; 10 ，那么某些交易无法进行。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>transactions = [[3,0],[0,3]]
<b>输出：</b>3
<strong>解释：</strong>
- 如果交易执行的顺序是 [[3,0],[0,3]] ，完成所有交易需要的最少钱数是 3 。
- 如果交易执行的顺序是 [[0,3],[3,0]] ，完成所有交易需要的最少钱数是 0 。
所以，刚开始钱数为 3 ，任意顺序下交易都可以全部完成。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= transactions.length &lt;= 10<sup>5</sup></code></li>
	<li><code>transactions[i].length == 2</code></li>
	<li><code>0 &lt;= cost<sub>i</sub>, cashback<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Split transactions that have cashback greater or equal to cost apart from transactions that have cashback less than cost. You will always <strong>earn</strong> money in the first scenario.
2. For transactions that have cashback greater or equal to cost, sort them by cost in descending order.
3. For transactions that have cashback less than cost, sort them by cashback in ascending order.

## 示例

```
[[2,1],[5,0],[4,2]]
[[3,0],[0,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumMoney(vector<vector<int>>& transactions) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumMoney(int[][] transactions) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumMoney(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        
```

### C

```c
long long minimumMoney(int** transactions, int transactionsSize, int* transactionsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumMoney(int[][] transactions) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} transactions
 * @return {number}
 */
var minimumMoney = function(transactions) {
    
};
```

### TypeScript

```typescript
function minimumMoney(transactions: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $transactions
     * @return Integer
     */
    function minimumMoney($transactions) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumMoney(_ transactions: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumMoney(transactions: Array<IntArray>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumMoney(List<List<int>> transactions) {
    
  }
}
```

### Go

```golang
func minimumMoney(transactions [][]int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} transactions
# @return {Integer}
def minimum_money(transactions)
    
end
```

### Scala

```scala
object Solution {
    def minimumMoney(transactions: Array[Array[Int]]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_money(transactions: Vec<Vec<i32>>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-money transactions)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_money(Transactions :: [[integer()]]) -> integer().
minimum_money(Transactions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_money(transactions :: [[integer]]) :: integer
  def minimum_money(transactions) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumMoney(transactions: Array<Array<Int64>>): Int64 {

    }
}
```

