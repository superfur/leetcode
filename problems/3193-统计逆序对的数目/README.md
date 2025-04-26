# 3193. 统计逆序对的数目

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;和一个二维数组&nbsp;<code>requirements</code>&nbsp;，其中&nbsp;<code>requirements[i] = [end<sub>i</sub>, cnt<sub>i</sub>]</code> <span class="text-only" data-eleid="10" style="white-space: pre;">表示这个要求中的末尾下标和 <strong>逆序对</strong> 的数目。</span></p>

<p>整数数组 <code>nums</code>&nbsp;中一个下标对&nbsp;<code>(i, j)</code>&nbsp;如果满足以下条件，那么它们被称为一个 <strong>逆序对</strong>&nbsp;：</p>

<ul>
	<li><code>i &lt; j</code>&nbsp;且&nbsp;<code>nums[i] &gt; nums[j]</code></li>
</ul>

<p>请你返回&nbsp;<code>[0, 1, 2, ..., n - 1]</code>&nbsp;的&nbsp;<span data-keyword="permutation">排列</span> <code>perm</code>&nbsp;的数目，满足对 <strong>所有</strong>&nbsp;的&nbsp;<code>requirements[i]</code>&nbsp;都满足&nbsp;<code>perm[0..end<sub>i</sub>]</code>&nbsp;中恰好有&nbsp;<code>cnt<sub>i</sub></code>&nbsp;个逆序对。</p>

<p>由于答案可能会很大，将它对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 3, requirements = [[2,2],[0,0]]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>两个排列为：</p>

<ul>
	<li><code>[2, 0, 1]</code>

	<ul>
		<li>前缀&nbsp;<code>[2, 0, 1]</code>&nbsp;的逆序对为&nbsp;<code>(0, 1)</code> 和&nbsp;<code>(0, 2)</code>&nbsp;。</li>
		<li>前缀&nbsp;<code>[2]</code>&nbsp;的逆序对数目为 0 个。</li>
	</ul>
	</li>
	<li><code>[1, 2, 0]</code>
	<ul>
		<li>前缀&nbsp;<code>[1, 2, 0]</code>&nbsp;的逆序对为&nbsp;<code>(0, 2)</code> 和&nbsp;<code>(1, 2)</code>&nbsp;。</li>
		<li>前缀&nbsp;<code>[1]</code>&nbsp;的逆序对数目为 0 个。</li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 3, requirements = [[2,2],[1,1],[0,0]]</span></p>

<p><b>输出：</b>1</p>

<p><strong>解释：</strong></p>

<p>唯一满足要求的排列是&nbsp;<code>[2, 0, 1]</code>&nbsp;：</p>

<ul>
	<li>前缀&nbsp;<code>[2, 0, 1]</code>&nbsp;的逆序对为&nbsp;<code>(0, 1)</code> 和&nbsp;<code>(0, 2)</code>&nbsp;。</li>
	<li>前缀&nbsp;<code>[2, 0]</code>&nbsp;的逆序对为&nbsp;<code>(0, 1)</code>&nbsp;。</li>
	<li>前缀&nbsp;<code>[2]</code>&nbsp;的逆序对数目为 0 。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 2, requirements = [[0,0],[1,0]]</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><b>解释：</b></p>

<p>唯一满足要求的排列为&nbsp;<code>[0, 1]</code>&nbsp;：</p>

<ul>
	<li>前缀&nbsp;<code>[0]</code>&nbsp;的逆序对数目为 0 。</li>
	<li>前缀&nbsp;<code>[0, 1]</code>&nbsp;的逆序对为&nbsp;<code>(0, 1)</code>&nbsp;。</li>
</ul>
</div>

<div id="gtx-trans" style="position: absolute; left: 198px; top: 756px;">
<div class="gtx-trans-icon">&nbsp;</div>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 300</code></li>
	<li><code>1 &lt;= requirements.length &lt;= n</code></li>
	<li><code>requirements[i] = [end<sub>i</sub>, cnt<sub>i</sub>]</code></li>
	<li><code>0 &lt;= end<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>0 &lt;= cnt<sub>i</sub> &lt;= 400</code></li>
	<li>输入保证至少有一个&nbsp;<code>i</code>&nbsp;满足&nbsp;<code>end<sub>i</sub> == n - 1</code>&nbsp;。</li>
	<li>输入保证所有的&nbsp;<code>end<sub>i</sub></code>&nbsp;互不相同。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. Let <code>dp[i][j]</code> denote the number of arrays of length <code>i</code> with <code>j</code> inversions.
2. <code>dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] + … + dp[i - 1][0]</code>.
3. <code>dp[i][j] = 0</code> if for some <code>x</code>, <code>requirements[x][0] == i</code> and <code>requirements[x][1] != j</code>.

## 示例

```
3
[[2,2],[0,0]]
3
[[2,2],[1,1],[0,0]]
2
[[0,0],[1,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfPermutations(int n, vector<vector<int>>& requirements) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfPermutations(int n, int[][] requirements) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        
```

### C

```c
int numberOfPermutations(int n, int** requirements, int requirementsSize, int* requirementsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfPermutations(int n, int[][] requirements) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} requirements
 * @return {number}
 */
var numberOfPermutations = function(n, requirements) {
    
};
```

### TypeScript

```typescript
function numberOfPermutations(n: number, requirements: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $requirements
     * @return Integer
     */
    function numberOfPermutations($n, $requirements) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfPermutations(_ n: Int, _ requirements: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfPermutations(n: Int, requirements: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfPermutations(int n, List<List<int>> requirements) {
    
  }
}
```

### Go

```golang
func numberOfPermutations(n int, requirements [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} requirements
# @return {Integer}
def number_of_permutations(n, requirements)
    
end
```

### Scala

```scala
object Solution {
    def numberOfPermutations(n: Int, requirements: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_permutations(n: i32, requirements: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-permutations n requirements)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_permutations(N :: integer(), Requirements :: [[integer()]]) -> integer().
number_of_permutations(N, Requirements) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_permutations(n :: integer, requirements :: [[integer]]) :: integer
  def number_of_permutations(n, requirements) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfPermutations(n: Int64, requirements: Array<Array<Int64>>): Int64 {

    }
}
```

