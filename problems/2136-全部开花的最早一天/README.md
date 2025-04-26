# 2136. 全部开花的最早一天

## 题目描述

<p>你有 <code>n</code> 枚花的种子。每枚种子必须先种下，才能开始生长、开花。播种需要时间，种子的生长也是如此。给你两个下标从 <strong>0</strong> 开始的整数数组 <code>plantTime</code> 和 <code>growTime</code> ，每个数组的长度都是 <code>n</code> ：</p>

<ul>
	<li><code>plantTime[i]</code> 是 <strong>播种</strong> 第 <code>i</code> 枚种子所需的 <strong>完整天数</strong> 。每天，你只能为播种某一枚种子而劳作。<strong>无须</strong> 连续几天都在种同一枚种子，但是种子播种必须在你工作的天数达到 <code>plantTime[i]</code> 之后才算完成。</li>
	<li><code>growTime[i]</code> 是第 <code>i</code> 枚种子完全种下后生长所需的 <strong>完整天数 </strong>。在它生长的最后一天 <strong>之后</strong> ，将会开花并且永远 <strong>绽放</strong> 。</li>
</ul>

<p>从第 <code>0</code> 开始，你可以按 <strong>任意</strong> 顺序播种种子。</p>

<p>返回所有种子都开花的 <strong>最早</strong> 一天是第几天。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/21/1.png" style="width: 453px; height: 149px;">
<pre><strong>输入：</strong>plantTime = [1,4,3], growTime = [2,3,1]
<strong>输出：</strong>9
<strong>解释：</strong>灰色的花盆表示播种的日子，彩色的花盆表示生长的日子，花朵表示开花的日子。
一种最优方案是：
第 0 天，播种第 0 枚种子，种子生长 2 整天。并在第 3 天开花。
第 1、2、3、4 天，播种第 1 枚种子。种子生长 3 整天，并在第 8 天开花。
第 5、6、7 天，播种第 2 枚种子。种子生长 1 整天，并在第 9 天开花。
因此，在第 9 天，所有种子都开花。 
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/21/2.png" style="width: 454px; height: 184px;">
<pre><strong>输入：</strong>plantTime = [1,2,3,2], growTime = [2,1,2,1]
<strong>输出：</strong>9
<strong>解释：</strong>灰色的花盆表示播种的日子，彩色的花盆表示生长的日子，花朵表示开花的日子。 
一种最优方案是：
第 1 天，播种第 0 枚种子，种子生长 2 整天。并在第 4 天开花。
第 0、3 天，播种第 1 枚种子。种子生长 1 整天，并在第 5 天开花。
第 2、4、5 天，播种第 2 枚种子。种子生长 2 整天，并在第 8 天开花。
第 6、7 天，播种第 3 枚种子。种子生长 1 整天，并在第 9 天开花。
因此，在第 9 天，所有种子都开花。 
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>plantTime = [1], growTime = [1]
<strong>输出：</strong>2
<strong>解释：</strong>第 0 天，播种第 0 枚种子。种子需要生长 1 整天，然后在第 2 天开花。
因此，在第 2 天，所有种子都开花。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == plantTime.length == growTime.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= plantTime[i], growTime[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 排序

## 提示

1. List the planting like the diagram above shows, where a row represents the timeline of a seed. A row i is above another row j if the last day planting seed i is ahead of the last day for seed j. Does it have any advantage to spend some days to plant seed j before completely planting seed i?
2. No. It does not help seed j but could potentially delay the completion of seed i, resulting in a worse final answer. Remaining focused is a part of the optimal solution.
3. Sort the seeds by their growTime in descending order. Can you prove why this strategy is the other part of the optimal solution? Note the bloom time of a seed is the sum of plantTime of all seeds preceding this seed plus the growTime of this seed.
4. There is no way to improve this strategy. The seed to bloom last dominates the final answer. Exchanging the planting of this seed with another seed with either a larger or smaller growTime will result in a potentially worse answer.

## 示例

```
[1,4,3]
[2,3,1]
[1,2,3,2]
[2,1,2,1]
[1]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {
        
    }
};
```

### Java

```java
class Solution {
    public int earliestFullBloom(int[] plantTime, int[] growTime) {
        
    }
}
```

### Python

```python
class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
```

### C

```c
int earliestFullBloom(int* plantTime, int plantTimeSize, int* growTime, int growTimeSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int EarliestFullBloom(int[] plantTime, int[] growTime) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} plantTime
 * @param {number[]} growTime
 * @return {number}
 */
var earliestFullBloom = function(plantTime, growTime) {
    
};
```

### TypeScript

```typescript
function earliestFullBloom(plantTime: number[], growTime: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $plantTime
     * @param Integer[] $growTime
     * @return Integer
     */
    function earliestFullBloom($plantTime, $growTime) {
        
    }
}
```

### Swift

```swift
class Solution {
    func earliestFullBloom(_ plantTime: [Int], _ growTime: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun earliestFullBloom(plantTime: IntArray, growTime: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int earliestFullBloom(List<int> plantTime, List<int> growTime) {
    
  }
}
```

### Go

```golang
func earliestFullBloom(plantTime []int, growTime []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} plant_time
# @param {Integer[]} grow_time
# @return {Integer}
def earliest_full_bloom(plant_time, grow_time)
    
end
```

### Scala

```scala
object Solution {
    def earliestFullBloom(plantTime: Array[Int], growTime: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn earliest_full_bloom(plant_time: Vec<i32>, grow_time: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (earliest-full-bloom plantTime growTime)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec earliest_full_bloom(PlantTime :: [integer()], GrowTime :: [integer()]) -> integer().
earliest_full_bloom(PlantTime, GrowTime) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec earliest_full_bloom(plant_time :: [integer], grow_time :: [integer]) :: integer
  def earliest_full_bloom(plant_time, grow_time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func earliestFullBloom(plantTime: Array<Int64>, growTime: Array<Int64>): Int64 {

    }
}
```

