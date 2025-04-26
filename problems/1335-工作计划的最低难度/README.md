# 1335. 工作计划的最低难度

## 题目描述

<p>你需要制定一份&nbsp;<code>d</code>&nbsp;天的工作计划表。工作之间存在依赖，要想执行第&nbsp;<code>i</code>&nbsp;项工作，你必须完成全部&nbsp;<code>j</code>&nbsp;项工作（&nbsp;<code>0 &lt;= j &lt; i</code>）。</p>

<p>你每天 <strong>至少</strong>&nbsp;需要完成一项任务。工作计划的总难度是这&nbsp;<code>d</code>&nbsp;天每一天的难度之和，而一天的工作难度是当天应该完成工作的最大难度。</p>

<p>给你一个整数数组&nbsp;<code>jobDifficulty</code>&nbsp;和一个整数&nbsp;<code>d</code>，分别代表工作难度和需要计划的天数。第&nbsp;<code>i</code>&nbsp;项工作的难度是&nbsp;<code>jobDifficulty[i]</code>。</p>

<p>返回整个工作计划的 <strong>最小难度</strong> 。如果无法制定工作计划，则返回&nbsp;<strong>-1&nbsp;</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/26/untitled.png" style="height: 304px; width: 365px;"></p>

<pre><strong>输入：</strong>jobDifficulty = [6,5,4,3,2,1], d = 2
<strong>输出：</strong>7
<strong>解释：</strong>第一天，您可以完成前 5 项工作，总难度 = 6.
第二天，您可以完成最后一项工作，总难度 = 1.
计划表的难度 = 6 + 1 = 7 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>jobDifficulty = [9,9,9], d = 4
<strong>输出：</strong>-1
<strong>解释：</strong>就算你每天完成一项工作，仍然有一天是空闲的，你无法制定一份能够满足既定工作时间的计划表。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>jobDifficulty = [1,1,1], d = 3
<strong>输出：</strong>3
<strong>解释：</strong>工作计划为每天一项工作，总难度为 3 。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>jobDifficulty = [7,1,7,1,7,1], d = 3
<strong>输出：</strong>15
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
<strong>输出：</strong>843
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= jobDifficulty.length &lt;= 300</code></li>
	<li><code>0 &lt;=&nbsp;jobDifficulty[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= d &lt;= 10</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. Use DP. Try to cut the array into d non-empty sub-arrays. Try all possible cuts for the array.
2. Use dp[i][j] where DP states are i the index of the last cut and j the number of remaining cuts. Complexity is O(n * n * d).

## 示例

```
[6,5,4,3,2,1]
2
[9,9,9]
4
[1,1,1]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minDifficulty(vector<int>& jobDifficulty, int d) {
        
    }
};
```

### Java

```java
class Solution {
    public int minDifficulty(int[] jobDifficulty, int d) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
```

### C

```c
int minDifficulty(int* jobDifficulty, int jobDifficultySize, int d) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinDifficulty(int[] jobDifficulty, int d) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} jobDifficulty
 * @param {number} d
 * @return {number}
 */
var minDifficulty = function(jobDifficulty, d) {
    
};
```

### TypeScript

```typescript
function minDifficulty(jobDifficulty: number[], d: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $jobDifficulty
     * @param Integer $d
     * @return Integer
     */
    function minDifficulty($jobDifficulty, $d) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minDifficulty(_ jobDifficulty: [Int], _ d: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minDifficulty(jobDifficulty: IntArray, d: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minDifficulty(List<int> jobDifficulty, int d) {
    
  }
}
```

### Go

```golang
func minDifficulty(jobDifficulty []int, d int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} job_difficulty
# @param {Integer} d
# @return {Integer}
def min_difficulty(job_difficulty, d)
    
end
```

### Scala

```scala
object Solution {
    def minDifficulty(jobDifficulty: Array[Int], d: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_difficulty(job_difficulty: Vec<i32>, d: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-difficulty jobDifficulty d)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_difficulty(JobDifficulty :: [integer()], D :: integer()) -> integer().
min_difficulty(JobDifficulty, D) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_difficulty(job_difficulty :: [integer], d :: integer) :: integer
  def min_difficulty(job_difficulty, d) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minDifficulty(jobDifficulty: Array<Int64>, d: Int64): Int64 {

    }
}
```

