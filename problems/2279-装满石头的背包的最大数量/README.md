# 2279. 装满石头的背包的最大数量

## 题目描述

<p>现有编号从&nbsp;<code>0</code> 到 <code>n - 1</code> 的 <code>n</code> 个背包。给你两个下标从 <strong>0</strong> 开始的整数数组 <code>capacity</code> 和 <code>rocks</code> 。第 <code>i</code> 个背包最大可以装 <code>capacity[i]</code> 块石头，当前已经装了 <code>rocks[i]</code> 块石头。另给你一个整数 <code>additionalRocks</code> ，表示<span class="text-only" data-eleid="10" style="white-space: pre;">你可以放置的额外石头数量，石头可以往 </span><strong><span class="text-only" data-eleid="11" style="white-space: pre;">任意</span></strong><span class="text-only" data-eleid="12" style="white-space: pre;"> 背包中放置。</span></p>

<p>请你将额外的石头放入一些背包中，并返回放置后装满石头的背包的 <strong>最大 </strong>数量<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
<strong>输出：</strong>3
<strong>解释：</strong>
1 块石头放入背包 0 ，1 块石头放入背包 1 。
每个背包中的石头总数是 [2,3,4,4] 。
背包 0 、背包 1 和 背包 2 都装满石头。
总计 3 个背包装满石头，所以返回 3 。
可以证明不存在超过 3 个背包装满石头的情况。
注意，可能存在其他放置石头的方案同样能够得到 3 这个结果。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100
<strong>输出：</strong>3
<strong>解释：</strong>
8 块石头放入背包 0 ，2 块石头放入背包 2 。
每个背包中的石头总数是 [10,2,2] 。
背包 0 、背包 1 和背包 2 都装满石头。
总计 3 个背包装满石头，所以返回 3 。
可以证明不存在超过 3 个背包装满石头的情况。
注意，不必用完所有的额外石头。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == capacity.length == rocks.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= capacity[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= rocks[i] &lt;= capacity[i]</code></li>
	<li><code>1 &lt;= additionalRocks &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Which bag should you fill completely first?
2. Can you think of a greedy solution?

## 示例

```
[2,3,4,5]
[1,2,4,4]
2
[10,2,2]
[2,2,0]
100
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumBags(vector<int>& capacity, vector<int>& rocks, int additionalRocks) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
```

### C

```c
int maximumBags(int* capacity, int capacitySize, int* rocks, int rocksSize, int additionalRocks) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} capacity
 * @param {number[]} rocks
 * @param {number} additionalRocks
 * @return {number}
 */
var maximumBags = function(capacity, rocks, additionalRocks) {
    
};
```

### TypeScript

```typescript
function maximumBags(capacity: number[], rocks: number[], additionalRocks: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $capacity
     * @param Integer[] $rocks
     * @param Integer $additionalRocks
     * @return Integer
     */
    function maximumBags($capacity, $rocks, $additionalRocks) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumBags(_ capacity: [Int], _ rocks: [Int], _ additionalRocks: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumBags(capacity: IntArray, rocks: IntArray, additionalRocks: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumBags(List<int> capacity, List<int> rocks, int additionalRocks) {
    
  }
}
```

### Go

```golang
func maximumBags(capacity []int, rocks []int, additionalRocks int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} capacity
# @param {Integer[]} rocks
# @param {Integer} additional_rocks
# @return {Integer}
def maximum_bags(capacity, rocks, additional_rocks)
    
end
```

### Scala

```scala
object Solution {
    def maximumBags(capacity: Array[Int], rocks: Array[Int], additionalRocks: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_bags(capacity: Vec<i32>, rocks: Vec<i32>, additional_rocks: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-bags capacity rocks additionalRocks)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_bags(Capacity :: [integer()], Rocks :: [integer()], AdditionalRocks :: integer()) -> integer().
maximum_bags(Capacity, Rocks, AdditionalRocks) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_bags(capacity :: [integer], rocks :: [integer], additional_rocks :: integer) :: integer
  def maximum_bags(capacity, rocks, additional_rocks) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumBags(capacity: Array<Int64>, rocks: Array<Int64>, additionalRocks: Int64): Int64 {

    }
}
```

