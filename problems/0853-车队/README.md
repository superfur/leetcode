# 853. 车队

## 题目描述

<p>在一条单行道上，有 <code>n</code> 辆车开往同一目的地。目的地是几英里以外的&nbsp;<code>target</code>&nbsp;。</p>

<p>给定两个整数数组&nbsp;<code>position</code>&nbsp;和&nbsp;<code>speed</code>&nbsp;，长度都是 <code>n</code> ，其中&nbsp;<code>position[i]</code>&nbsp;是第 <code>i</code> 辆车的位置，&nbsp;<code>speed[i]</code>&nbsp;是第 <code>i</code> 辆车的速度(单位是英里/小时)。</p>

<p>一辆车永远不会超过前面的另一辆车，但它可以追上去，并以较慢车的速度在另一辆车旁边行驶。</p>

<p><strong>车队 </strong>是指并排行驶的一辆或几辆汽车。车队的速度是车队中 <strong>最慢</strong> 的车的速度。</p>

<p>即便一辆车在&nbsp;<code>target</code> 才赶上了一个车队，它们仍然会被视作是同一个车队。</p>

<p>返回到达目的地的车队数量 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>从 10（速度为 2）和 8（速度为 4）开始的车会组成一个车队，它们在 12 相遇。车队在&nbsp;<code>target</code>&nbsp;形成。</li>
	<li>从 0（速度为 1）开始的车不会追上其它任何车，所以它自己是一个车队。</li>
	<li>从 5（速度为 1） 和 3（速度为 3）开始的车组成一个车队，在 6 相遇。车队以速度 1 移动直到它到达&nbsp;<code>target</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">target = 10, position = [3], speed = [3]</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">1</span></p>

<p><strong>解释：</strong></p>
只有一辆车，因此只有一个车队。</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span><span class="example-io">target = 100, position = [0,2,4], speed = [4,2,1]</span></p>

<p><span class="example-io"><b>输出：</b></span><span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>从 0（速度为 4） 和 2（速度为 2）开始的车组成一个车队，在 4&nbsp;相遇。从 4 开始的车（速度为 1）移动到了 5。</li>
	<li>然后，在 4（速度为 2）的车队和在 5（速度为 1）的车成为一个车队，在 6 相遇。车队以速度 1 移动直到它到达&nbsp;<code>target</code>。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == position.length == speed.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt; target &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= position[i] &lt; target</code></li>
	<li><code>position</code>&nbsp;中每个值都 <strong>不同</strong></li>
	<li><code>0 &lt; speed[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 排序
- 单调栈

## 示例

```
12
[10,8,0,5,3]
[2,4,1,1,3]
10
[3]
[3]
100
[0,2,4]
[4,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        
    }
};
```

### Java

```java
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        
    }
}
```

### Python

```python
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
```

### C

```c
int carFleet(int target, int* position, int positionSize, int* speed, int speedSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function(target, position, speed) {
    
};
```

### TypeScript

```typescript
function carFleet(target: number, position: number[], speed: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $target
     * @param Integer[] $position
     * @param Integer[] $speed
     * @return Integer
     */
    function carFleet($target, $position, $speed) {
        
    }
}
```

### Swift

```swift
class Solution {
    func carFleet(_ target: Int, _ position: [Int], _ speed: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun carFleet(target: Int, position: IntArray, speed: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int carFleet(int target, List<int> position, List<int> speed) {
    
  }
}
```

### Go

```golang
func carFleet(target int, position []int, speed []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} target
# @param {Integer[]} position
# @param {Integer[]} speed
# @return {Integer}
def car_fleet(target, position, speed)
    
end
```

### Scala

```scala
object Solution {
    def carFleet(target: Int, position: Array[Int], speed: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (car-fleet target position speed)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec car_fleet(Target :: integer(), Position :: [integer()], Speed :: [integer()]) -> integer().
car_fleet(Target, Position, Speed) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec car_fleet(target :: integer, position :: [integer], speed :: [integer]) :: integer
  def car_fleet(target, position, speed) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func carFleet(target: Int64, position: Array<Int64>, speed: Array<Int64>): Int64 {

    }
}
```

