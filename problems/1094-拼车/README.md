# 1094. 拼车

## 题目描述

<p>车上最初有&nbsp;<code>capacity</code>&nbsp;个空座位。车&nbsp;<strong>只能&nbsp;</strong>向一个方向行驶（也就是说，<strong>不允许掉头或改变方向</strong>）</p>

<p>给定整数&nbsp;<code>capacity</code>&nbsp;和一个数组 <code>trips</code> , &nbsp;<code>trip[i] = [numPassengers<sub>i</sub>, from<sub>i</sub>, to<sub>i</sub>]</code>&nbsp;表示第 <code>i</code> 次旅行有&nbsp;<code>numPassengers<sub>i</sub></code>&nbsp;乘客，接他们和放他们的位置分别是&nbsp;<code>from<sub>i</sub></code>&nbsp;和&nbsp;<code>to<sub>i</sub></code>&nbsp;。这些位置是从汽车的初始位置向东的公里数。</p>

<p>当且仅当你可以在所有给定的行程中接送所有乘客时，返回&nbsp;<code>true</code>，否则请返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>trips = [[2,1,5],[3,3,7]], capacity = 4
<strong>输出：</strong>false
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>trips = [[2,1,5],[3,3,7]], capacity = 5
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= trips.length &lt;= 1000</code></li>
	<li><code>trips[i].length == 3</code></li>
	<li><code>1 &lt;= numPassengers<sub>i</sub>&nbsp;&lt;= 100</code></li>
	<li><code>0 &lt;= from<sub>i</sub>&nbsp;&lt; to<sub>i</sub>&nbsp;&lt;= 1000</code></li>
	<li><code>1 &lt;= capacity &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 前缀和
- 排序
- 模拟
- 堆（优先队列）

## 提示

1. Sort the pickup and dropoff events by location, then process them in order.

## 示例

```
[[2,1,5],[3,3,7]]
4
[[2,1,5],[3,3,7]]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        
    }
}
```

### Python

```python
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
```

### C

```c
bool carPooling(int** trips, int tripsSize, int* tripsColSize, int capacity) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CarPooling(int[][] trips, int capacity) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */
var carPooling = function(trips, capacity) {
    
};
```

### TypeScript

```typescript
function carPooling(trips: number[][], capacity: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $trips
     * @param Integer $capacity
     * @return Boolean
     */
    function carPooling($trips, $capacity) {
        
    }
}
```

### Swift

```swift
class Solution {
    func carPooling(_ trips: [[Int]], _ capacity: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun carPooling(trips: Array<IntArray>, capacity: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool carPooling(List<List<int>> trips, int capacity) {
    
  }
}
```

### Go

```golang
func carPooling(trips [][]int, capacity int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} trips
# @param {Integer} capacity
# @return {Boolean}
def car_pooling(trips, capacity)
    
end
```

### Scala

```scala
object Solution {
    def carPooling(trips: Array[Array[Int]], capacity: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn car_pooling(trips: Vec<Vec<i32>>, capacity: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (car-pooling trips capacity)
  (-> (listof (listof exact-integer?)) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec car_pooling(Trips :: [[integer()]], Capacity :: integer()) -> boolean().
car_pooling(Trips, Capacity) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec car_pooling(trips :: [[integer]], capacity :: integer) :: boolean
  def car_pooling(trips, capacity) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func carPooling(trips: Array<Array<Int64>>, capacity: Int64): Bool {

    }
}
```

