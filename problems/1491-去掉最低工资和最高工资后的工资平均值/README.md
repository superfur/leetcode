# 1491. 去掉最低工资和最高工资后的工资平均值

## 题目描述

<p>给你一个整数数组&nbsp;<code>salary</code>&nbsp;，数组里每个数都是 <strong>唯一</strong>&nbsp;的，其中&nbsp;<code>salary[i]</code> 是第&nbsp;<code>i</code>&nbsp;个员工的工资。</p>

<p>请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>salary = [4000,3000,1000,2000]
<strong>输出：</strong>2500.00000
<strong>解释：</strong>最低工资和最高工资分别是 1000 和 4000 。
去掉最低工资和最高工资以后的平均工资是 (2000+3000)/2= 2500
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>salary = [1000,2000,3000]
<strong>输出：</strong>2000.00000
<strong>解释：</strong>最低工资和最高工资分别是 1000 和 3000 。
去掉最低工资和最高工资以后的平均工资是 (2000)/1= 2000
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>salary = [6000,5000,4000,3000,2000,1000]
<strong>输出：</strong>3500.00000
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>salary = [8000,9000,2000,3000,6000,1000]
<strong>输出：</strong>4750.00000
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= salary.length &lt;= 100</code></li>
	<li><code>10^3&nbsp;&lt;= salary[i] &lt;= 10^6</code></li>
	<li><code>salary[i]</code>&nbsp;是唯一的。</li>
	<li>与真实值误差在&nbsp;<code>10^-5</code> 以内的结果都将视为正确答案。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 排序

## 提示

1. Get the total sum and subtract the minimum and maximum value in the array.  Finally divide the result by n - 2.

## 示例

```
[4000,3000,1000,2000]
[1000,2000,3000]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double average(vector<int>& salary) {
        
    }
};
```

### Java

```java
class Solution {
    public double average(int[] salary) {
        
    }
}
```

### Python

```python
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def average(self, salary: List[int]) -> float:
        
```

### C

```c
double average(int* salary, int salarySize) {
    
}
```

### C#

```csharp
public class Solution {
    public double Average(int[] salary) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
    
};
```

### TypeScript

```typescript
function average(salary: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $salary
     * @return Float
     */
    function average($salary) {
        
    }
}
```

### Swift

```swift
class Solution {
    func average(_ salary: [Int]) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun average(salary: IntArray): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double average(List<int> salary) {
    
  }
}
```

### Go

```golang
func average(salary []int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} salary
# @return {Float}
def average(salary)
    
end
```

### Scala

```scala
object Solution {
    def average(salary: Array[Int]): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn average(salary: Vec<i32>) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (average salary)
  (-> (listof exact-integer?) flonum?)
  )
```

### Erlang

```erlang
-spec average(Salary :: [integer()]) -> float().
average(Salary) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec average(salary :: [integer]) :: float
  def average(salary) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func average(salary: Array<Int64>): Float64 {

    }
}
```

