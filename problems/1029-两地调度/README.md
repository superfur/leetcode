# 1029. 两地调度

## 题目描述

<p>公司计划面试 <code>2n</code> 人。给你一个数组 <code>costs</code> ，其中 <code>costs[i] = [aCost<sub>i</sub>, bCost<sub>i</sub>]</code> 。第 <code>i</code> 人飞往 <code>a</code> 市的费用为 <code>aCost<sub>i</sub></code> ，飞往 <code>b</code> 市的费用为 <code>bCost<sub>i</sub></code> 。</p>

<p>返回将每个人都飞到 <code>a</code> 、<code>b</code> 中某座城市的最低费用，要求每个城市都有 <code>n</code> 人抵达<strong>。</strong></p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>costs = [[10,20],[30,200],[400,50],[30,20]]
<strong>输出：</strong>110
<strong>解释：</strong>
第一个人去 a 市，费用为 10。
第二个人去 a 市，费用为 30。
第三个人去 b 市，费用为 50。
第四个人去 b 市，费用为 20。

最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
<strong>输出：</strong>1859
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
<strong>输出：</strong>3086
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 * n == costs.length</code></li>
	<li><code>2 <= costs.length <= 100</code></li>
	<li><code>costs.length</code> 为偶数</li>
	<li><code>1 <= aCost<sub>i</sub>, bCost<sub>i</sub> <= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 示例

```
[[10,20],[30,200],[400,50],[30,20]]
[[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
[[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        
    }
};
```

### Java

```java
class Solution {
    public int twoCitySchedCost(int[][] costs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
```

### C

```c
int twoCitySchedCost(int** costs, int costsSize, int* costsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int TwoCitySchedCost(int[][] costs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} costs
 * @return {number}
 */
var twoCitySchedCost = function(costs) {
    
};
```

### TypeScript

```typescript
function twoCitySchedCost(costs: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $costs
     * @return Integer
     */
    function twoCitySchedCost($costs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func twoCitySchedCost(_ costs: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun twoCitySchedCost(costs: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int twoCitySchedCost(List<List<int>> costs) {
    
  }
}
```

### Go

```golang
func twoCitySchedCost(costs [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} costs
# @return {Integer}
def two_city_sched_cost(costs)
    
end
```

### Scala

```scala
object Solution {
    def twoCitySchedCost(costs: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn two_city_sched_cost(costs: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (two-city-sched-cost costs)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec two_city_sched_cost(Costs :: [[integer()]]) -> integer().
two_city_sched_cost(Costs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec two_city_sched_cost(costs :: [[integer]]) :: integer
  def two_city_sched_cost(costs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func twoCitySchedCost(costs: Array<Array<Int64>>): Int64 {

    }
}
```

