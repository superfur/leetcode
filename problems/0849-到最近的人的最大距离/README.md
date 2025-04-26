# 849. 到最近的人的最大距离

## 题目描述

<p>给你一个数组 <code>seats</code> 表示一排座位，其中 <code>seats[i] = 1</code> 代表有人坐在第 <code>i</code> 个座位上，<code>seats[i] = 0</code> 代表座位 <code>i</code> 上是空的（<strong>下标从 0 开始</strong>）。</p>

<p>至少有一个空座位，且至少有一人已经坐在座位上。</p>

<p>亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。</p>

<p>返回他到离他最近的人的最大距离。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/10/distance.jpg" style="width: 650px; height: 257px;" />
<pre>
<strong>输入：</strong>seats = [1,0,0,0,1,0,1]
<strong>输出：</strong>2
<strong>解释：
</strong>如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>seats = [1,0,0,0]
<strong>输出：</strong>3
<strong>解释：</strong>
如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
这是可能的最大距离，所以答案是 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>seats = [0,1]
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= seats.length <= 2 * 10<sup>4</sup></code></li>
	<li><code>seats[i]</code> 为 <code>0</code> 或 <code>1</code></li>
	<li>至少有一个 <strong>空座位</strong></li>
	<li>至少有一个 <strong>座位上有人</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组

## 示例

```
[1,0,0,0,1,0,1]
[1,0,0,0]
[0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxDistToClosest(int[] seats) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
```

### C

```c
int maxDistToClosest(int* seats, int seatsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxDistToClosest(int[] seats) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} seats
 * @return {number}
 */
var maxDistToClosest = function(seats) {
    
};
```

### TypeScript

```typescript
function maxDistToClosest(seats: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $seats
     * @return Integer
     */
    function maxDistToClosest($seats) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxDistToClosest(_ seats: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxDistToClosest(seats: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxDistToClosest(List<int> seats) {
    
  }
}
```

### Go

```golang
func maxDistToClosest(seats []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} seats
# @return {Integer}
def max_dist_to_closest(seats)
    
end
```

### Scala

```scala
object Solution {
    def maxDistToClosest(seats: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_dist_to_closest(seats: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-dist-to-closest seats)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_dist_to_closest(Seats :: [integer()]) -> integer().
max_dist_to_closest(Seats) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_dist_to_closest(seats :: [integer]) :: integer
  def max_dist_to_closest(seats) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxDistToClosest(seats: Array<Int64>): Int64 {

    }
}
```

