# 1093. 大样本统计

## 题目描述

<p>我们对&nbsp;<code>0</code>&nbsp;到&nbsp;<code>255</code>&nbsp;之间的整数进行采样，并将结果存储在数组&nbsp;<code>count</code>&nbsp;中：<code>count[k]</code>&nbsp;就是整数&nbsp;<code>k</code> 在样本中出现的次数。</p>

<p>计算以下统计数据:</p>

<ul>
	<li><code>minimum</code>&nbsp;：样本中的最小元素。</li>
	<li><code>maximum</code>&nbsp;：样品中的最大元素。</li>
	<li><code>mean</code>&nbsp;：样本的平均值，计算为所有元素的总和除以元素总数。</li>
	<li><code>median</code>&nbsp;：
	<ul>
		<li>如果样本的元素个数是奇数，那么一旦样本排序后，中位数 <code>median</code> 就是中间的元素。</li>
		<li>如果样本中有偶数个元素，那么中位数<code>median</code> 就是样本排序后中间两个元素的平均值。</li>
	</ul>
	</li>
	<li><code>mode</code>&nbsp;：样本中出现次数最多的数字。保众数是 <strong>唯一</strong> 的。</li>
</ul>

<p>以浮点数数组的形式返回样本的统计信息<em>&nbsp;</em><code>[minimum, maximum, mean, median, mode]</code>&nbsp;。与真实答案误差在<em>&nbsp;</em><code>10<sup>-5</sup></code><em>&nbsp;</em>内的答案都可以通过。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
<strong>输出：</strong>[1.00000,3.00000,2.37500,2.50000,3.00000]
<strong>解释：</strong>用count表示的样本为[1,2,2,2,3,3,3,3]。
最小值和最大值分别为1和3。
均值是(1+2+2+2+3+3+3+3) / 8 = 19 / 8 = 2.375。
因为样本的大小是偶数，所以中位数是中间两个元素2和3的平均值，也就是2.5。
众数为3，因为它在样本中出现的次数最多。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
<strong>输出：</strong>[1.00000,4.00000,2.18182,2.00000,1.00000]
<strong>解释：</strong>用count表示的样本为[1,1,1,1,2,2,3,3,3,4,4]。
最小值为1，最大值为4。
平均数是(1+1+1+1+2+2+2+3+3+4+4)/ 11 = 24 / 11 = 2.18181818…(为了显示，输出显示了整数2.18182)。
因为样本的大小是奇数，所以中值是中间元素2。
众数为1，因为它在样本中出现的次数最多。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>count.length == 256</code></li>
	<li><code>0 &lt;= count[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= sum(count) &lt;= 10<sup>9</sup></code></li>
	<li>&nbsp;<code>count</code>&nbsp;的众数是 <strong>唯一</strong> 的</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 概率与统计

## 提示

1. The hard part is the median.  Write a helper function which finds the k-th element from the sample.

## 示例

```
[0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<double> sampleStats(vector<int>& count) {
        
    }
};
```

### Java

```java
class Solution {
    public double[] sampleStats(int[] count) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        
```

### Python3

```python3
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* sampleStats(int* count, int countSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double[] SampleStats(int[] count) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} count
 * @return {number[]}
 */
var sampleStats = function(count) {
    
};
```

### TypeScript

```typescript
function sampleStats(count: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $count
     * @return Float[]
     */
    function sampleStats($count) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sampleStats(_ count: [Int]) -> [Double] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sampleStats(count: IntArray): DoubleArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<double> sampleStats(List<int> count) {
    
  }
}
```

### Go

```golang
func sampleStats(count []int) []float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} count
# @return {Float[]}
def sample_stats(count)
    
end
```

### Scala

```scala
object Solution {
    def sampleStats(count: Array[Int]): Array[Double] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sample_stats(count: Vec<i32>) -> Vec<f64> {
        
    }
}
```

### Racket

```racket
(define/contract (sample-stats count)
  (-> (listof exact-integer?) (listof flonum?))
  )
```

### Erlang

```erlang
-spec sample_stats(Count :: [integer()]) -> [float()].
sample_stats(Count) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sample_stats(count :: [integer]) :: [float]
  def sample_stats(count) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sampleStats(count: Array<Int64>): Array<Float64> {

    }
}
```

