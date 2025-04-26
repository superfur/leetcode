# 2751. 机器人碰撞

## 题目描述

<p>现有 <code>n</code> 个机器人，编号从 <strong>1</strong> 开始，每个机器人包含在路线上的位置、健康度和移动方向。</p>

<p>给你下标从 <strong>0</strong> 开始的两个整数数组 <code>positions</code>、<code>healths</code> 和一个字符串 <code>directions</code>（<code>directions[i]</code> 为 <strong>'L'</strong> 表示 <strong>向左</strong> 或 <strong>'R'</strong> 表示 <strong>向右</strong>）。 <code>positions</code> 中的所有整数 <strong>互不相同</strong> 。</p>

<p>所有机器人以 <strong>相同速度</strong> <strong>同时</strong> 沿给定方向在路线上移动。如果两个机器人移动到相同位置，则会发生 <strong>碰撞</strong> 。</p>

<p>如果两个机器人发生碰撞，则将 <strong>健康度较低</strong> 的机器人从路线中 <strong>移除</strong> ，并且另一个机器人的健康度 <strong>减少 1</strong> 。幸存下来的机器人将会继续沿着与之前 <strong>相同</strong> 的方向前进。如果两个机器人的健康度相同，则将二者都从路线中移除。</p>

<p>请你确定全部碰撞后幸存下的所有机器人的 <strong>健康度</strong> ，并按照原来机器人编号的顺序排列。即机器人 1 （如果幸存）的最终健康度，机器人 2 （如果幸存）的最终健康度等。 如果不存在幸存的机器人，则返回空数组。</p>

<p>在不再发生任何碰撞后，请你以数组形式，返回所有剩余机器人的健康度（按机器人输入中的编号顺序）。</p>

<p><strong>注意：</strong>位置&nbsp; <code>positions</code> 可能是乱序的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img height="169" src="https://assets.leetcode.com/uploads/2023/05/15/image-20230516011718-12.png" width="808" /></p>

<pre>
<strong>输入：</strong>positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"
<strong>输出：</strong>[2,17,9,15,10]
<strong>解释：</strong>在本例中不存在碰撞，因为所有机器人向同一方向移动。所以，从第一个机器人开始依序返回健康度，[2, 17, 9, 15, 10] 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img height="176" src="https://assets.leetcode.com/uploads/2023/05/15/image-20230516004433-7.png" width="717" /></p>

<pre>
<strong>输入：</strong>positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"
<strong>输出：</strong>[14]
<strong>解释：</strong>本例中发生 2 次碰撞。首先，机器人 1 和机器人 2 将会碰撞，因为二者健康度相同，二者都将被从路线中移除。接下来，机器人 3 和机器人 4 将会发生碰撞，由于机器人 4 的健康度更小，则它会被移除，而机器人 3 的健康度变为 15 - 1 = 14 。仅剩机器人 3 ，所以返回 [14] 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img height="172" src="https://assets.leetcode.com/uploads/2023/05/15/image-20230516005114-9.png" width="732" /></p>

<pre>
<strong>输入：</strong>positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"
<strong>输出：</strong>[]
<strong>解释：</strong>机器人 1 和机器人 2 将会碰撞，因为二者健康度相同，二者都将被从路线中移除。机器人 3 和机器人 4 将会碰撞，因为二者健康度相同，二者都将被从路线中移除。所以返回空数组 [] 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= positions.length == healths.length == directions.length == n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= positions[i], healths[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>directions[i] == 'L'</code> 或 <code>directions[i] == 'R'</code></li>
	<li><code>positions</code> 中的所有值互不相同</li>
</ul>


## 难度

Hard

## 标签

- 栈
- 数组
- 排序
- 模拟

## 提示

1. Process the robots in the order of their positions to ensure that we process the collisions correctly.
2. To optimize the solution, use a stack to keep track of the surviving robots as we iterate through the positions.
3. Instead of simulating each collision, check the current robot against the top of the stack (if it exists) to determine if a collision occurs.

## 示例

```
[5,4,3,2,1]
[2,17,9,15,10]
"RRRRR"
[3,5,2,6]
[10,10,15,12]
"RLRL"
[1,2,5,6]
[10,10,11,11]
"RLRL"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        
    }
}
```

### Python

```python
class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* survivedRobotsHealths(int* positions, int positionsSize, int* healths, int healthsSize, char* directions, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> SurvivedRobotsHealths(int[] positions, int[] healths, string directions) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} positions
 * @param {number[]} healths
 * @param {string} directions
 * @return {number[]}
 */
var survivedRobotsHealths = function(positions, healths, directions) {
    
};
```

### TypeScript

```typescript
function survivedRobotsHealths(positions: number[], healths: number[], directions: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $positions
     * @param Integer[] $healths
     * @param String $directions
     * @return Integer[]
     */
    function survivedRobotsHealths($positions, $healths, $directions) {
        
    }
}
```

### Swift

```swift
class Solution {
    func survivedRobotsHealths(_ positions: [Int], _ healths: [Int], _ directions: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun survivedRobotsHealths(positions: IntArray, healths: IntArray, directions: String): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> survivedRobotsHealths(List<int> positions, List<int> healths, String directions) {
    
  }
}
```

### Go

```golang
func survivedRobotsHealths(positions []int, healths []int, directions string) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} positions
# @param {Integer[]} healths
# @param {String} directions
# @return {Integer[]}
def survived_robots_healths(positions, healths, directions)
    
end
```

### Scala

```scala
object Solution {
    def survivedRobotsHealths(positions: Array[Int], healths: Array[Int], directions: String): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn survived_robots_healths(positions: Vec<i32>, healths: Vec<i32>, directions: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (survived-robots-healths positions healths directions)
  (-> (listof exact-integer?) (listof exact-integer?) string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec survived_robots_healths(Positions :: [integer()], Healths :: [integer()], Directions :: unicode:unicode_binary()) -> [integer()].
survived_robots_healths(Positions, Healths, Directions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec survived_robots_healths(positions :: [integer], healths :: [integer], directions :: String.t) :: [integer]
  def survived_robots_healths(positions, healths, directions) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func survivedRobotsHealths(positions: Array<Int64>, healths: Array<Int64>, directions: String): ArrayList<Int64> {

    }
}
```

