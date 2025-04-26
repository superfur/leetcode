# 2105. 给植物浇水 II

## 题目描述

<p>Alice 和 Bob 打算给花园里的 <code>n</code> 株植物浇水。植物排成一行，从左到右进行标记，编号从 <code>0</code> 到 <code>n - 1</code> 。其中，第 <code>i</code> 株植物的位置是 <code>x = i</code> 。</p>

<p>每一株植物都需要浇特定量的水。Alice 和 Bob 每人有一个水罐，<strong>最初是满的 </strong>。他们按下面描述的方式完成浇水：</p>

<ul>
	<li>&nbsp;Alice 按 <strong>从左到右</strong> 的顺序给植物浇水，从植物 <code>0</code> 开始。Bob 按 <strong>从右到左</strong> 的顺序给植物浇水，从植物 <code>n - 1</code> 开始。他们 <strong>同时</strong> 给植物浇水。</li>
	<li>无论需要多少水，为每株植物浇水所需的时间都是相同的。</li>
	<li>如果 Alice/Bob 水罐中的水足以 <strong>完全</strong> 灌溉植物，他们 <strong>必须</strong> 给植物浇水。否则，他们 <strong>首先</strong>（立即）重新装满罐子，然后给植物浇水。</li>
	<li>如果 Alice 和 Bob 到达同一株植物，那么当前水罐中水 <strong>更多</strong> 的人会给这株植物浇水。如果他俩水量相同，那么 Alice 会给这株植物浇水。</li>
</ul>

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>plants</code> ，数组由 <code>n</code> 个整数组成。其中，<code>plants[i]</code> 为第 <code>i</code> 株植物需要的水量。另有两个整数 <code>capacityA</code> 和&nbsp;<code>capacityB</code> 分别表示 Alice 和 Bob 水罐的容量。返回两人浇灌所有植物过程中重新灌满水罐的 <strong>次数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>plants = [2,2,3,3], capacityA = 5, capacityB = 5
<strong>输出：</strong>1
<strong>解释：</strong>
- 最初，Alice 和 Bob 的水罐中各有 5 单元水。
- Alice 给植物 0 浇水，Bob 给植物 3 浇水。
- Alice 和 Bob 现在分别剩下 3 单元和 2 单元水。
- Alice 有足够的水给植物 1 ，所以她直接浇水。Bob 的水不够给植物 2 ，所以他先重新装满水，再浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 + 0 + 1 + 0 = 1 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>plants = [2,2,3,3], capacityA = 3, capacityB = 4
<strong>输出：</strong>2
<strong>解释：</strong>
- 最初，Alice 的水罐中有 3 单元水，Bob 的水罐中有 4 单元水。
- Alice 给植物 0 浇水，Bob 给植物 3 浇水。
- Alice 和 Bob 现在都只有 1 单元水，并分别需要给植物 1 和植物 2 浇水。
- 由于他们的水量均不足以浇水，所以他们重新灌满水罐再进行浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 + 1 + 1 + 0 = 2 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>plants = [5], capacityA = 10, capacityB = 8
<strong>输出：</strong>0
<strong>解释：</strong>
- 只有一株植物
- Alice 的水罐有 10 单元水，Bob 的水罐有 8 单元水。因此 Alice 的水罐中水更多，她会给这株植物浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == plants.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= plants[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>max(plants[i]) &lt;= capacityA, capacityB &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 模拟

## 提示

1. Try "simulating" the process.
2. Since watering each plant takes the same amount of time, where will Alice and Bob meet if they start watering the plants simultaneously? How can you use this to optimize your solution?
3. What will you do when both Alice and Bob have to water the same plant?

## 示例

```
[2,2,3,3]
5
5
[2,2,3,3]
3
4
[5]
10
8
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumRefill(vector<int>& plants, int capacityA, int capacityB) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumRefill(int[] plants, int capacityA, int capacityB) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
```

### C

```c
int minimumRefill(int* plants, int plantsSize, int capacityA, int capacityB) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumRefill(int[] plants, int capacityA, int capacityB) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} plants
 * @param {number} capacityA
 * @param {number} capacityB
 * @return {number}
 */
var minimumRefill = function(plants, capacityA, capacityB) {
    
};
```

### TypeScript

```typescript
function minimumRefill(plants: number[], capacityA: number, capacityB: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $plants
     * @param Integer $capacityA
     * @param Integer $capacityB
     * @return Integer
     */
    function minimumRefill($plants, $capacityA, $capacityB) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumRefill(_ plants: [Int], _ capacityA: Int, _ capacityB: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumRefill(plants: IntArray, capacityA: Int, capacityB: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumRefill(List<int> plants, int capacityA, int capacityB) {
    
  }
}
```

### Go

```golang
func minimumRefill(plants []int, capacityA int, capacityB int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} plants
# @param {Integer} capacity_a
# @param {Integer} capacity_b
# @return {Integer}
def minimum_refill(plants, capacity_a, capacity_b)
    
end
```

### Scala

```scala
object Solution {
    def minimumRefill(plants: Array[Int], capacityA: Int, capacityB: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_refill(plants: Vec<i32>, capacity_a: i32, capacity_b: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-refill plants capacityA capacityB)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_refill(Plants :: [integer()], CapacityA :: integer(), CapacityB :: integer()) -> integer().
minimum_refill(Plants, CapacityA, CapacityB) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_refill(plants :: [integer], capacity_a :: integer, capacity_b :: integer) :: integer
  def minimum_refill(plants, capacity_a, capacity_b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumRefill(plants: Array<Int64>, capacityA: Int64, capacityB: Int64): Int64 {

    }
}
```

