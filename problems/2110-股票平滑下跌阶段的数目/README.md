# 2110. 股票平滑下跌阶段的数目

## 题目描述

<p>给你一个整数数组&nbsp;<code>prices</code>&nbsp;，表示一支股票的历史每日股价，其中&nbsp;<code>prices[i]</code>&nbsp;是这支股票第&nbsp;<code>i</code>&nbsp;天的价格。</p>

<p>一个 <strong>平滑下降的阶段</strong>&nbsp;定义为：对于&nbsp;<strong>连续一天或者多天</strong>&nbsp;，每日股价都比 <strong>前一日股价恰好少 </strong><code>1</code>&nbsp;，这个阶段第一天的股价没有限制。</p>

<p>请你返回 <strong>平滑下降阶段</strong>&nbsp;的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>prices = [3,2,1,4]
<b>输出：</b>7
<b>解释：</b>总共有 7 个平滑下降阶段：
[3], [2], [1], [4], [3,2], [2,1] 和 [3,2,1]
注意，仅一天按照定义也是平滑下降阶段。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>prices = [8,6,7,7]
<b>输出：</b>4
<b>解释：</b>总共有 4 个连续平滑下降阶段：[8], [6], [7] 和 [7]
由于 8 - 6 ≠ 1 ，所以 [8,6] 不是平滑下降阶段。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>prices = [1]
<b>输出：</b>1
<b>解释：</b>总共有 1 个平滑下降阶段：[1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= prices[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 动态规划

## 提示

1. Any array is a series of adjacent longest possible smooth descent periods. For example, [5,3,2,1,7,6] is [5] + [3,2,1] + [7,6].
2. Think of a 2-pointer approach to traverse the array and find each longest possible period.
3. Suppose you found the longest possible period with a length of k. How many periods are within that period? How can you count them quickly? Think of the formula to calculate the sum of 1, 2, 3, ..., k.

## 示例

```
[3,2,1,4]
[8,6,7,7]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        
    }
};
```

### Java

```java
class Solution {
    public long getDescentPeriods(int[] prices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
```

### C

```c
long long getDescentPeriods(int* prices, int pricesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long GetDescentPeriods(int[] prices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} prices
 * @return {number}
 */
var getDescentPeriods = function(prices) {
    
};
```

### TypeScript

```typescript
function getDescentPeriods(prices: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function getDescentPeriods($prices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getDescentPeriods(_ prices: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getDescentPeriods(prices: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int getDescentPeriods(List<int> prices) {
    
  }
}
```

### Go

```golang
func getDescentPeriods(prices []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} prices
# @return {Integer}
def get_descent_periods(prices)
    
end
```

### Scala

```scala
object Solution {
    def getDescentPeriods(prices: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_descent_periods(prices: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (get-descent-periods prices)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec get_descent_periods(Prices :: [integer()]) -> integer().
get_descent_periods(Prices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_descent_periods(prices :: [integer]) :: integer
  def get_descent_periods(prices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getDescentPeriods(prices: Array<Int64>): Int64 {

    }
}
```

