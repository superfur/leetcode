# 2561. 重排水果

## 题目描述

<p>你有两个果篮，每个果篮中有 <code>n</code> 个水果。给你两个下标从 <strong>0</strong> 开始的整数数组 <code>basket1</code> 和 <code>basket2</code> ，用以表示两个果篮中每个水果的交换成本。你想要让两个果篮相等。为此，可以根据需要多次执行下述操作：</p>

<ul>
	<li>选中两个下标 <code>i</code> 和 <code>j</code> ，并交换 <code>basket1</code> 中的第 <code>i</code> 个水果和 <code>basket2</code> 中的第 <code>j</code> 个水果。</li>
	<li>交换的成本是 <code>min(basket1<sub>i</sub>,basket2<sub>j</sub>)</code> 。</li>
</ul>

<p>根据果篮中水果的成本进行排序，如果排序后结果完全相同，则认为两个果篮相等。</p>

<p>返回使两个果篮相等的最小交换成本，如果无法使两个果篮相等，则返回<em> </em><code>-1</code><em> </em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>basket1 = [4,2,2,2], basket2 = [1,4,1,2]
<strong>输出：</strong>1
<strong>解释：</strong>交换 basket1 中下标为 1 的水果和 basket2 中下标为 0 的水果，交换的成本为 1 。此时，basket1 = [4,1,2,2] 且 basket2 = [2,4,1,2] 。重排两个数组，发现二者相等。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>basket1 = [2,3,4,1], basket2 = [3,2,5,1]
<strong>输出：</strong>-1
<strong>解释：</strong>可以证明无法使两个果篮相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>basket1.length == bakste2.length</code></li>
	<li><code>1 &lt;= basket1.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= basket1<sub>i</sub>,basket2<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 哈希表

## 提示

1. Create two frequency maps for both arrays, and find the minimum element among all elements of both arrays.
2. Check if the sum of frequencies of an element in both arrays is odd, if so return -1
3. Store the elements that need to be swapped in a vector, and sort it.
4. Can we reduce swapping cost with the help of minimum element?
5. Calculate the minimum cost of swapping.

## 示例

```
[4,2,2,2]
[1,4,1,2]
[2,3,4,1]
[3,2,5,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minCost(vector<int>& basket1, vector<int>& basket2) {
        
    }
};
```

### Java

```java
class Solution {
    public long minCost(int[] basket1, int[] basket2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        
```

### C

```c
long long minCost(int* basket1, int basket1Size, int* basket2, int basket2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinCost(int[] basket1, int[] basket2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} basket1
 * @param {number[]} basket2
 * @return {number}
 */
var minCost = function(basket1, basket2) {
    
};
```

### TypeScript

```typescript
function minCost(basket1: number[], basket2: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $basket1
     * @param Integer[] $basket2
     * @return Integer
     */
    function minCost($basket1, $basket2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCost(_ basket1: [Int], _ basket2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCost(basket1: IntArray, basket2: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCost(List<int> basket1, List<int> basket2) {
    
  }
}
```

### Go

```golang
func minCost(basket1 []int, basket2 []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} basket1
# @param {Integer[]} basket2
# @return {Integer}
def min_cost(basket1, basket2)
    
end
```

### Scala

```scala
object Solution {
    def minCost(basket1: Array[Int], basket2: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost(basket1: Vec<i32>, basket2: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost basket1 basket2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost(Basket1 :: [integer()], Basket2 :: [integer()]) -> integer().
min_cost(Basket1, Basket2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost(basket1 :: [integer], basket2 :: [integer]) :: integer
  def min_cost(basket1, basket2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCost(basket1: Array<Int64>, basket2: Array<Int64>): Int64 {

    }
}
```

