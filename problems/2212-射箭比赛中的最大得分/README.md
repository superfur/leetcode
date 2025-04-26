# 2212. 射箭比赛中的最大得分

## 题目描述

<p>Alice 和 Bob 是一场射箭比赛中的对手。比赛规则如下：</p>

<ol>
	<li>Alice 先射 <code>numArrows</code> 支箭，然后 Bob 也射 <code>numArrows</code> 支箭。</li>
	<li>分数按下述规则计算：
	<ol>
		<li>箭靶有若干整数计分区域，范围从 <code>0</code> 到 <code>11</code> （含 <code>0</code> 和 <code>11</code>）。</li>
		<li>箭靶上每个区域都对应一个得分 <code>k</code>（范围是 <code>0</code> 到 <code>11</code>），Alice 和 Bob 分别在得分 <code>k</code>&nbsp;区域射中&nbsp;<code>a<sub>k</sub></code> 和 <code>b<sub>k</sub></code> 支箭。如果 <code>a<sub>k</sub> &gt;= b<sub>k</sub></code> ，那么 Alice 得 <code>k</code> 分。如果 <code>a<sub>k</sub> &lt; b<sub>k</sub></code> ，则 Bob 得 <code>k</code> 分</li>
		<li>如果 <code>a<sub>k</sub> == b<sub>k</sub> == 0</code> ，那么无人得到 <code>k</code> 分。</li>
	</ol>
	</li>
</ol>

<ul>
	<li>
	<p>例如，Alice 和 Bob 都向计分为 <code>11</code> 的区域射 <code>2</code> 支箭，那么 Alice 得 <code>11</code> 分。如果 Alice 向计分为 <code>11</code> 的区域射 <code>0</code> 支箭，但 Bob 向同一个区域射 <code>2</code> 支箭，那么 Bob 得&nbsp;<code>11</code> 分。</p>
	</li>
</ul>

<p>给你整数 <code>numArrows</code> 和一个长度为 <code>12</code> 的整数数组 <code>aliceArrows</code> ，该数组表示 Alice 射中&nbsp;<code>0</code> 到 <code>11</code> 每个计分区域的箭数量。现在，Bob 想要尽可能 <strong>最大化</strong> 他所能获得的总分。</p>

<p>返回数组 <code>bobArrows</code><em> </em>，该数组表示 Bob 射中&nbsp;<code>0</code> 到 <code>11</code> <strong>每个</strong> 计分区域的箭数量。且 <code>bobArrows</code> 的总和应当等于 <code>numArrows</code> 。</p>

<p>如果存在多种方法都可以使 Bob 获得最大总分，返回其中 <strong>任意一种</strong> 即可。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://pic.leetcode-cn.com/1647744752-kQKrXw-image.png" style="width: 600px; height: 120px;" /></p>

<pre>
<strong>输入：</strong>numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
<strong>输出：</strong>[0,0,0,0,1,1,0,0,1,2,3,1]
<strong>解释：</strong>上表显示了比赛得分情况。
Bob 获得总分 4 + 5 + 8 + 9 + 10 + 11 = 47 。
可以证明 Bob 无法获得比 47 更高的分数。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://pic.leetcode-cn.com/1647744785-cMHzaC-image.png" style="width: 600px; height: 117px;" /></p>

<pre>
<strong>输入：</strong>numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]
<strong>输出：</strong>[0,0,0,0,0,0,0,0,1,1,1,0]
<strong>解释：</strong>上表显示了比赛得分情况。
Bob 获得总分 8 + 9 + 10 = 27 。
可以证明 Bob 无法获得比 27 更高的分数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= numArrows &lt;= 10<sup>5</sup></code></li>
	<li><code>aliceArrows.length == bobArrows.length == 12</code></li>
	<li><code>0 &lt;= aliceArrows[i], bobArrows[i] &lt;= numArrows</code></li>
	<li><code>sum(aliceArrows[i]) == numArrows</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 回溯
- 枚举

## 提示

1. To obtain points for some certain section x, what is the minimum number of arrows Bob must shoot?
2. Given the small number of sections, can we brute force which sections Bob wants to win?
3. For every set of sections Bob wants to win, check if we have the required amount of arrows. If we do, it is a valid selection.

## 示例

```
9
[1,1,0,1,0,0,2,1,0,1,2,0]
3
[0,0,1,0,0,0,0,0,0,0,0,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> maximumBobPoints(int numArrows, vector<int>& aliceArrows) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] maximumBobPoints(int numArrows, int[] aliceArrows) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        """
        :type numArrows: int
        :type aliceArrows: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maximumBobPoints(int numArrows, int* aliceArrows, int aliceArrowsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MaximumBobPoints(int numArrows, int[] aliceArrows) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} numArrows
 * @param {number[]} aliceArrows
 * @return {number[]}
 */
var maximumBobPoints = function(numArrows, aliceArrows) {
    
};
```

### TypeScript

```typescript
function maximumBobPoints(numArrows: number, aliceArrows: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $numArrows
     * @param Integer[] $aliceArrows
     * @return Integer[]
     */
    function maximumBobPoints($numArrows, $aliceArrows) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumBobPoints(_ numArrows: Int, _ aliceArrows: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumBobPoints(numArrows: Int, aliceArrows: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> maximumBobPoints(int numArrows, List<int> aliceArrows) {
    
  }
}
```

### Go

```golang
func maximumBobPoints(numArrows int, aliceArrows []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} num_arrows
# @param {Integer[]} alice_arrows
# @return {Integer[]}
def maximum_bob_points(num_arrows, alice_arrows)
    
end
```

### Scala

```scala
object Solution {
    def maximumBobPoints(numArrows: Int, aliceArrows: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_bob_points(num_arrows: i32, alice_arrows: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-bob-points numArrows aliceArrows)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec maximum_bob_points(NumArrows :: integer(), AliceArrows :: [integer()]) -> [integer()].
maximum_bob_points(NumArrows, AliceArrows) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_bob_points(num_arrows :: integer, alice_arrows :: [integer]) :: [integer]
  def maximum_bob_points(num_arrows, alice_arrows) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumBobPoints(numArrows: Int64, aliceArrows: Array<Int64>): Array<Int64> {

    }
}
```

