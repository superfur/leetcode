# 2469. 温度转换

## 题目描述

<p>给你一个四舍五入到两位小数的非负浮点数 <code>celsius</code> 来表示温度，以 <strong>摄氏度</strong>（<strong>Celsius</strong>）为单位。</p>

<p>你需要将摄氏度转换为 <strong>开氏度</strong>（<strong>Kelvin</strong>）和 <strong>华氏度</strong>（<strong>Fahrenheit</strong>），并以数组 <code>ans = [kelvin, fahrenheit]</code> 的形式返回结果。</p>

<p>返回数组<em> <code>ans</code></em> 。与实际答案误差不超过 <code>10<sup>-5</sup></code> 的会视为正确答案<strong>。</strong></p>

<p><strong>注意：</strong></p>

<ul>
	<li><code>开氏度 = 摄氏度 + 273.15</code></li>
	<li><code>华氏度 = 摄氏度 * 1.80 + 32.00</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1 ：</strong></p>

<pre><strong>输入：</strong>celsius = 36.50
<strong>输出：</strong>[309.65000,97.70000]
<strong>解释：</strong>36.50 摄氏度：转换为开氏度是 309.65 ，转换为华氏度是 97.70 。</pre>

<p><strong>示例 2 ：</strong></p>

<pre><strong>输入：</strong>celsius = 122.11
<strong>输出：</strong>[395.26000,251.79800]
<strong>解释：</strong>122.11 摄氏度：转换为开氏度是 395.26 ，转换为华氏度是 251.798 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= celsius &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. Implement formulas that are given in the statement.

## 示例

```
36.50
122.11
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        
    }
};
```

### Java

```java
class Solution {
    public double[] convertTemperature(double celsius) {
        
    }
}
```

### Python

```python
class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        
```

### Python3

```python3
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double[] ConvertTemperature(double celsius) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} celsius
 * @return {number[]}
 */
var convertTemperature = function(celsius) {
    
};
```

### TypeScript

```typescript
function convertTemperature(celsius: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Float $celsius
     * @return Float[]
     */
    function convertTemperature($celsius) {
        
    }
}
```

### Swift

```swift
class Solution {
    func convertTemperature(_ celsius: Double) -> [Double] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun convertTemperature(celsius: Double): DoubleArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<double> convertTemperature(double celsius) {
    
  }
}
```

### Go

```golang
func convertTemperature(celsius float64) []float64 {
    
}
```

### Ruby

```ruby
# @param {Float} celsius
# @return {Float[]}
def convert_temperature(celsius)
    
end
```

### Scala

```scala
object Solution {
    def convertTemperature(celsius: Double): Array[Double] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn convert_temperature(celsius: f64) -> Vec<f64> {
        
    }
}
```

### Racket

```racket
(define/contract (convert-temperature celsius)
  (-> flonum? (listof flonum?))
  )
```

### Erlang

```erlang
-spec convert_temperature(Celsius :: float()) -> [float()].
convert_temperature(Celsius) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec convert_temperature(celsius :: float) :: [float]
  def convert_temperature(celsius) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func convertTemperature(celsius: Float64): Array<Float64> {

    }
}
```

