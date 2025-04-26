# 1560. 圆形赛道上经过次数最多的扇区

## 题目描述

<p>给你一个整数 <code>n</code> 和一个整数数组 <code>rounds</code> 。有一条圆形赛道由 <code>n</code> 个扇区组成，扇区编号从 <code>1</code> 到 <code>n</code> 。现将在这条赛道上举办一场马拉松比赛，该马拉松全程由 <code>m</code> 个阶段组成。其中，第 <code>i</code> 个阶段将会从扇区 <code>rounds[i - 1]</code> 开始，到扇区 <code>rounds[i]</code> 结束。举例来说，第 <code>1</code> 阶段从&nbsp;<code>rounds[0]</code>&nbsp;开始，到&nbsp;<code>rounds[1]</code>&nbsp;结束。</p>

<p>请你以数组形式返回经过次数最多的那几个扇区，按扇区编号 <strong>升序</strong> 排列。</p>

<p>注意，赛道按扇区编号升序逆时针形成一个圆（请参见第一个示例）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/3rd45e.jpg" style="height: 341px; width: 433px;"></p>

<pre><strong>输入：</strong>n = 4, rounds = [1,3,1,2]
<strong>输出：</strong>[1,2]
<strong>解释：</strong>本场马拉松比赛从扇区 1 开始。经过各个扇区的次序如下所示：
1 --&gt; 2 --&gt; 3（阶段 1 结束）--&gt; 4 --&gt; 1（阶段 2 结束）--&gt; 2（阶段 3 结束，即本场马拉松结束）
其中，扇区 1 和 2 都经过了两次，它们是经过次数最多的两个扇区。扇区 3 和 4 都只经过了一次。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 2, rounds = [2,1,2,1,2,1,2,1,2]
<strong>输出：</strong>[2]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 7, rounds = [1,3,5,7]
<strong>输出：</strong>[1,2,3,4,5,6,7]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= m &lt;= 100</code></li>
	<li><code>rounds.length == m + 1</code></li>
	<li><code>1 &lt;= rounds[i] &lt;= n</code></li>
	<li><code>rounds[i] != rounds[i + 1]</code> ，其中 <code>0 &lt;= i &lt; m</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 模拟

## 提示

1. For each round increment the visits of the sectors visited during the marathon with 1.
2. Determine the max number of visits, and return any sector visited the max number of visits.

## 示例

```
4
[1,3,1,2]
2
[2,1,2,1,2,1,2,1,2]
7
[1,3,5,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> mostVisited(int n, vector<int>& rounds) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> mostVisited(int n, int[] rounds) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* mostVisited(int n, int* rounds, int roundsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> MostVisited(int n, int[] rounds) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} rounds
 * @return {number[]}
 */
var mostVisited = function(n, rounds) {
    
};
```

### TypeScript

```typescript
function mostVisited(n: number, rounds: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $rounds
     * @return Integer[]
     */
    function mostVisited($n, $rounds) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mostVisited(_ n: Int, _ rounds: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mostVisited(n: Int, rounds: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> mostVisited(int n, List<int> rounds) {
    
  }
}
```

### Go

```golang
func mostVisited(n int, rounds []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} rounds
# @return {Integer[]}
def most_visited(n, rounds)
    
end
```

### Scala

```scala
object Solution {
    def mostVisited(n: Int, rounds: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn most_visited(n: i32, rounds: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (most-visited n rounds)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec most_visited(N :: integer(), Rounds :: [integer()]) -> [integer()].
most_visited(N, Rounds) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec most_visited(n :: integer, rounds :: [integer]) :: [integer]
  def most_visited(n, rounds) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mostVisited(n: Int64, rounds: Array<Int64>): ArrayList<Int64> {

    }
}
```

