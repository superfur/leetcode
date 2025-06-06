# 1619. 删除某些元素后的数组均值

## 题目描述

<p>给你一个整数数组 <code>arr</code> ，请你删除最小 <code>5%</code> 的数字和最大 <code>5%</code> 的数字后，剩余数字的平均值。</p>

<p>与 <strong>标准答案</strong> 误差在 <code>10<sup>-5</sup></code> 的结果都被视为正确结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
<b>输出：</b>2.00000
<b>解释：</b>删除数组中最大和最小的元素后，所有元素都等于 2，所以平均值为 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
<b>输出：</b>4.00000
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
<b>输出：</b>4.77778
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>arr = [9,7,8,7,7,8,4,4,6,8,8,7,6,8,8,9,2,6,0,0,1,10,8,6,3,3,5,1,10,9,0,7,10,0,10,4,1,10,6,9,3,6,0,0,2,7,0,6,7,2,9,7,7,3,0,1,6,1,10,3]
<b>输出：</b>5.27778
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<b>输入：</b>arr = [4,8,4,10,0,7,1,3,7,8,8,3,4,1,6,2,1,1,8,0,9,8,0,3,9,10,3,10,1,10,7,3,2,1,4,9,10,7,6,4,0,8,5,1,2,1,6,2,5,0,7,10,9,10,3,7,10,5,8,5,7,6,7,6,10,9,5,10,5,5,7,2,10,7,7,8,2,0,1,1]
<b>输出：</b>5.29167
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>20 <= arr.length <= 1000</code></li>
	<li><code>arr.length</code><b> </b>是 <code>20</code> 的<strong> 倍数</strong> </li>
	<li><code>0 <= arr[i] <= 10<sup>5</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 排序

## 提示

1. Sort the given array.
2. Remove the first and last 5% of the sorted array.

## 示例

```
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
[6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
[6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double trimMean(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public double trimMean(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
```

### C

```c
double trimMean(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double TrimMean(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var trimMean = function(arr) {
    
};
```

### TypeScript

```typescript
function trimMean(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Float
     */
    function trimMean($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func trimMean(_ arr: [Int]) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun trimMean(arr: IntArray): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double trimMean(List<int> arr) {
    
  }
}
```

### Go

```golang
func trimMean(arr []int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Float}
def trim_mean(arr)
    
end
```

### Scala

```scala
object Solution {
    def trimMean(arr: Array[Int]): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn trim_mean(arr: Vec<i32>) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (trim-mean arr)
  (-> (listof exact-integer?) flonum?)
  )
```

### Erlang

```erlang
-spec trim_mean(Arr :: [integer()]) -> float().
trim_mean(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec trim_mean(arr :: [integer]) :: float
  def trim_mean(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func trimMean(arr: Array<Int64>): Float64 {

    }
}
```

