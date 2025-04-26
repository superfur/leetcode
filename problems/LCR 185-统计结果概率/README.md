# LCR 185. 统计结果概率

## 题目描述

<p>你选择掷出 <code>num</code> 个色子，请返回所有点数总和的概率。</p>

<p>你需要用一个浮点数数组返回答案，其中第 <code>i</code> 个元素代表这 <code>num</code> 个骰子所能掷出的点数集合中第 <code>i</code> 小的那个的概率。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = 3
<strong>输出：</strong>[0.00463,0.01389,0.02778,0.04630,0.06944,0.09722,0.11574,0.12500,0.12500,0.11574,0.09722,0.06944,0.04630,0.02778,0.01389,0.00463]
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>num = 5
<strong>输出:</strong>[0.00013,0.00064,0.00193,0.00450,0.00900,0.01620,0.02636,0.03922,0.05401,0.06944,0.08372,0.09452,0.10031,0.10031,0.09452,0.08372,0.06944,0.05401,0.03922,0.02636,0.01620,0.00900,0.00450,0.00193,0.00064,0.00013]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 11</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 数学
- 动态规划
- 概率与统计

## 示例

```
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<double> statisticsProbability(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public double[] statisticsProbability(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def statisticsProbability(self, num):
        """
        :type num: int
        :rtype: List[float]
        """
        
```

### Python3

```python3
class Solution:
    def statisticsProbability(self, num: int) -> List[float]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* statisticsProbability(int num, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double[] StatisticsProbability(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number[]}
 */
var statisticsProbability = function(num) {
    
};
```

### TypeScript

```typescript
function statisticsProbability(num: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Float[]
     */
    function statisticsProbability($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func statisticsProbability(_ num: Int) -> [Double] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun statisticsProbability(num: Int): DoubleArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<double> statisticsProbability(int num) {
    
  }
}
```

### Go

```golang
func statisticsProbability(num int) []float64 {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Float[]}
def statistics_probability(num)
    
end
```

### Scala

```scala
object Solution {
    def statisticsProbability(num: Int): Array[Double] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn statistics_probability(num: i32) -> Vec<f64> {
        
    }
}
```

### Racket

```racket
(define/contract (statistics-probability num)
  (-> exact-integer? (listof flonum?))
  )
```

### Erlang

```erlang
-spec statistics_probability(Num :: integer()) -> [float()].
statistics_probability(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec statistics_probability(num :: integer) :: [float]
  def statistics_probability(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func statisticsProbability(num: Int64): Array<Float64> {

    }
}
```

