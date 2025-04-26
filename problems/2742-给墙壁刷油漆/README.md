# 2742. 给墙壁刷油漆

## 题目描述

<p>给你两个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>cost</code> 和&nbsp;<code>time</code>&nbsp;，分别表示给&nbsp;<code>n</code>&nbsp;堵不同的墙刷油漆需要的开销和时间。你有两名油漆匠：</p>

<ul>
	<li>一位需要 <strong>付费</strong>&nbsp;的油漆匠，刷第&nbsp;<code>i</code>&nbsp;堵墙需要花费&nbsp;<code>time[i]</code>&nbsp;单位的时间，开销为&nbsp;<code>cost[i]</code>&nbsp;单位的钱。</li>
	<li>一位 <strong>免费</strong>&nbsp;的油漆匠，刷 <strong>任意</strong>&nbsp;一堵墙的时间为&nbsp;<code>1</code>&nbsp;单位，开销为&nbsp;<code>0</code>&nbsp;。但是必须在付费油漆匠&nbsp;<strong>工作</strong>&nbsp;时，免费油漆匠才会工作。</li>
</ul>

<p>请你返回刷完 <code>n</code>&nbsp;堵墙最少开销为多少。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>cost = [1,2,3,2], time = [1,2,3,2]
<b>输出：</b>3
<strong>解释：</strong>下标为 0 和 1 的墙由付费油漆匠来刷，需要 3 单位时间。同时，免费油漆匠刷下标为 2 和 3 的墙，需要 2 单位时间，开销为 0 。总开销为 1 + 2 = 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>cost = [2,3,4,2], time = [1,1,1,1]
<b>输出：</b>4
<b>解释：</b>下标为 0 和 3 的墙由付费油漆匠来刷，需要 2 单位时间。同时，免费油漆匠刷下标为 1 和 2 的墙，需要 2 单位时间，开销为 0 。总开销为 2 + 2 = 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= cost.length &lt;= 500</code></li>
	<li><code>cost.length == time.length</code></li>
	<li><code>1 &lt;= cost[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= time[i] &lt;= 500</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. Can we break the problem down into smaller subproblems and use DP?
2. Paid painters will be used for a maximum of N/2 units of time. There is no need to use paid painter for a time greater than this.

## 示例

```
[1,2,3,2]
[1,2,3,2]
[2,3,4,2]
[1,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int paintWalls(vector<int>& cost, vector<int>& time) {
        
    }
};
```

### Java

```java
class Solution {
    public int paintWalls(int[] cost, int[] time) {
        
    }
}
```

### Python

```python
class Solution(object):
    def paintWalls(self, cost, time):
        """
        :type cost: List[int]
        :type time: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
```

### C

```c
int paintWalls(int* cost, int costSize, int* time, int timeSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int PaintWalls(int[] cost, int[] time) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} cost
 * @param {number[]} time
 * @return {number}
 */
var paintWalls = function(cost, time) {
    
};
```

### TypeScript

```typescript
function paintWalls(cost: number[], time: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $cost
     * @param Integer[] $time
     * @return Integer
     */
    function paintWalls($cost, $time) {
        
    }
}
```

### Swift

```swift
class Solution {
    func paintWalls(_ cost: [Int], _ time: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun paintWalls(cost: IntArray, time: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int paintWalls(List<int> cost, List<int> time) {
    
  }
}
```

### Go

```golang
func paintWalls(cost []int, time []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} cost
# @param {Integer[]} time
# @return {Integer}
def paint_walls(cost, time)
    
end
```

### Scala

```scala
object Solution {
    def paintWalls(cost: Array[Int], time: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn paint_walls(cost: Vec<i32>, time: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (paint-walls cost time)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec paint_walls(Cost :: [integer()], Time :: [integer()]) -> integer().
paint_walls(Cost, Time) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec paint_walls(cost :: [integer], time :: [integer]) :: integer
  def paint_walls(cost, time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func paintWalls(cost: Array<Int64>, time: Array<Int64>): Int64 {

    }
}
```

