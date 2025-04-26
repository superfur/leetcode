# 2585. 获得分数的方法数

## 题目描述

<p>考试中有 <code>n</code> 种类型的题目。给你一个整数 <code>target</code> 和一个下标从 <strong>0</strong> 开始的二维整数数组 <code>types</code> ，其中 <code>types[i] = [count<sub>i</sub>, marks<sub>i</sub>] </code>表示第 <code>i</code> 种类型的题目有 <code>count<sub>i</sub></code> 道，每道题目对应 <code>marks<sub>i</sub></code> 分。</p>

<p>返回你在考试中恰好得到 <code>target</code> 分的方法数。由于答案可能很大，结果需要对 <code>10<sup>9</sup> +7</code> 取余。</p>

<p><strong>注意</strong>，同类型题目无法区分。</p>

<ul>
	<li>比如说，如果有 <code>3</code> 道同类型题目，那么解答第 <code>1</code> 和第 <code>2</code> 道题目与解答第 <code>1</code> 和第 <code>3</code> 道题目或者第 <code>2</code> 和第 <code>3</code> 道题目是相同的。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>target = 6, types = [[6,1],[3,2],[2,3]]
<strong>输出：</strong>7
<strong>解释：</strong>要获得 6 分，你可以选择以下七种方法之一：
- 解决 6 道第 0 种类型的题目：1 + 1 + 1 + 1 + 1 + 1 = 6
- 解决 4 道第 0 种类型的题目和 1 道第 1 种类型的题目：1 + 1 + 1 + 1 + 2 = 6
- 解决 2 道第 0 种类型的题目和 2 道第 1 种类型的题目：1 + 1 + 2 + 2 = 6
- 解决 3 道第 0 种类型的题目和 1 道第 2 种类型的题目：1 + 1 + 1 + 3 = 6
- 解决 1 道第 0 种类型的题目、1 道第 1 种类型的题目和 1 道第 2 种类型的题目：1 + 2 + 3 = 6
- 解决 3 道第 1 种类型的题目：2 + 2 + 2 = 6
- 解决 2 道第 2 种类型的题目：3 + 3 = 6
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>target = 5, types = [[50,1],[50,2],[50,5]]
<strong>输出：</strong>4
<strong>解释：</strong>要获得 5 分，你可以选择以下四种方法之一：
- 解决 5 道第 0 种类型的题目：1 + 1 + 1 + 1 + 1 = 5
- 解决 3 道第 0 种类型的题目和 1 道第 1 种类型的题目：1 + 1 + 1 + 2 = 5
- 解决 1 道第 0 种类型的题目和 2 道第 1 种类型的题目：1 + 2 + 2 = 5
- 解决 1 道第 2 种类型的题目：5
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>target = 18, types = [[6,1],[3,2],[2,3]]
<strong>输出：</strong>1
<strong>解释：</strong>只有回答所有题目才能获得 18 分。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
	<li><code>n == types.length</code></li>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>types[i].length == 2</code></li>
	<li><code>1 &lt;= count<sub>i</sub>, marks<sub>i</sub> &lt;= 50</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. Use Dynamic Programming
2. Let ways[i][points] be the number of ways to score a given number of points after solving some questions of the first i types.
3. ways[i][points] is equal to the sum of ways[i-1][points - solved * marks[i] over 0 <= solved <= count_i

## 示例

```
6
[[6,1],[3,2],[2,3]]
5
[[50,1],[50,2],[50,5]]
18
[[6,1],[3,2],[2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int waysToReachTarget(int target, vector<vector<int>>& types) {
        
    }
};
```

### Java

```java
class Solution {
    public int waysToReachTarget(int target, int[][] types) {
        
    }
}
```

### Python

```python
class Solution(object):
    def waysToReachTarget(self, target, types):
        """
        :type target: int
        :type types: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        
```

### C

```c
int waysToReachTarget(int target, int** types, int typesSize, int* typesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int WaysToReachTarget(int target, int[][] types) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} target
 * @param {number[][]} types
 * @return {number}
 */
var waysToReachTarget = function(target, types) {
    
};
```

### TypeScript

```typescript
function waysToReachTarget(target: number, types: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $target
     * @param Integer[][] $types
     * @return Integer
     */
    function waysToReachTarget($target, $types) {
        
    }
}
```

### Swift

```swift
class Solution {
    func waysToReachTarget(_ target: Int, _ types: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun waysToReachTarget(target: Int, types: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int waysToReachTarget(int target, List<List<int>> types) {
    
  }
}
```

### Go

```golang
func waysToReachTarget(target int, types [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} target
# @param {Integer[][]} types
# @return {Integer}
def ways_to_reach_target(target, types)
    
end
```

### Scala

```scala
object Solution {
    def waysToReachTarget(target: Int, types: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ways_to_reach_target(target: i32, types: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (ways-to-reach-target target types)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec ways_to_reach_target(Target :: integer(), Types :: [[integer()]]) -> integer().
ways_to_reach_target(Target, Types) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ways_to_reach_target(target :: integer, types :: [[integer]]) :: integer
  def ways_to_reach_target(target, types) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func waysToReachTarget(target: Int64, types: Array<Array<Int64>>): Int64 {

    }
}
```

