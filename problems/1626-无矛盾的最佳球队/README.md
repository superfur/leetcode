# 1626. 无矛盾的最佳球队

## 题目描述

<p>假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 <strong>总和</strong> 。</p>

<p>然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 <strong>没有矛盾</strong> 的球队。如果一名年龄较小球员的分数 <strong>严格大于</strong> 一名年龄较大的球员，则存在矛盾。同龄球员之间不会发生矛盾。</p>

<p>给你两个列表 <code>scores</code> 和 <code>ages</code>，其中每组 <code>scores[i]</code> 和 <code>ages[i]</code> 表示第 <code>i</code> 名球员的分数和年龄。请你返回 <strong>所有可能的无矛盾球队中得分最高那支的分数</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>scores = [1,3,5,10,15], ages = [1,2,3,4,5]
<strong>输出：</strong>34
<strong>解释：</strong>你可以选中所有球员。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>scores = [4,5,6,5], ages = [2,1,2,1]
<strong>输出：</strong>16
<strong>解释：</strong>最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>scores = [1,2,3,5], ages = [8,9,10,1]
<strong>输出：</strong>6
<strong>解释：</strong>最佳的选择是前 3 名球员。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= scores.length, ages.length &lt;= 1000</code></li>
	<li><code>scores.length == ages.length</code></li>
	<li><code>1 &lt;= scores[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= ages[i] &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 排序

## 提示

1. First, sort players by age and break ties by their score. You can now consider the players from left to right.
2. If you choose to include a player, you must only choose players with at least that score later on.

## 示例

```
[1,3,5,10,15]
[1,2,3,4,5]
[4,5,6,5]
[2,1,2,1]
[1,2,3,5]
[8,9,10,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        
    }
};
```

### Java

```java
class Solution {
    public int bestTeamScore(int[] scores, int[] ages) {
        
    }
}
```

### Python

```python
class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
```

### C

```c
int bestTeamScore(int* scores, int scoresSize, int* ages, int agesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int BestTeamScore(int[] scores, int[] ages) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} scores
 * @param {number[]} ages
 * @return {number}
 */
var bestTeamScore = function(scores, ages) {
    
};
```

### TypeScript

```typescript
function bestTeamScore(scores: number[], ages: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $scores
     * @param Integer[] $ages
     * @return Integer
     */
    function bestTeamScore($scores, $ages) {
        
    }
}
```

### Swift

```swift
class Solution {
    func bestTeamScore(_ scores: [Int], _ ages: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun bestTeamScore(scores: IntArray, ages: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int bestTeamScore(List<int> scores, List<int> ages) {
    
  }
}
```

### Go

```golang
func bestTeamScore(scores []int, ages []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} scores
# @param {Integer[]} ages
# @return {Integer}
def best_team_score(scores, ages)
    
end
```

### Scala

```scala
object Solution {
    def bestTeamScore(scores: Array[Int], ages: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn best_team_score(scores: Vec<i32>, ages: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (best-team-score scores ages)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec best_team_score(Scores :: [integer()], Ages :: [integer()]) -> integer().
best_team_score(Scores, Ages) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec best_team_score(scores :: [integer], ages :: [integer]) :: integer
  def best_team_score(scores, ages) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func bestTeamScore(scores: Array<Int64>, ages: Array<Int64>): Int64 {

    }
}
```

