# LCR 082. 组合总和 II

## 题目描述

<p>给定一个可能有重复数字的整数数组&nbsp;<code>candidates</code>&nbsp;和一个目标数&nbsp;<code>target</code>&nbsp;，找出&nbsp;<code>candidates</code>&nbsp;中所有可以使数字和为&nbsp;<code>target</code>&nbsp;的组合。</p>

<p><code>candidates</code>&nbsp;中的每个数字在每个组合中只能使用一次，解集不能包含重复的组合。&nbsp;</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>candidates = [10,1,2,7,6,1,5], target = 8
<strong>输出：</strong>
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>candidates = [2,5,2,1,2], target = 5
<strong>输出：</strong>
[
[1,2,2],
[5]
]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;candidates.length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;candidates[i] &lt;= 50</code></li>
	<li><code>1 &lt;= target &lt;= 30</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 40&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/combination-sum-ii/">https://leetcode-cn.com/problems/combination-sum-ii/</a></p>


## 难度

Medium

## 标签

- 数组
- 回溯

## 示例

```
[10,1,2,7,6,1,5]
8
[2,5,2,1,2]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {

    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {

    }
}
```

### Python

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
```

### Python3

```python3
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
```

### C

```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** combinationSum2(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes){

}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> CombinationSum2(int[] candidates, int target) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {

};
```

### TypeScript

```typescript
function combinationSum2(candidates: number[], target: number): number[][] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $candidates
     * @param Integer $target
     * @return Integer[][]
     */
    function combinationSum2($candidates, $target) {

    }
}
```

### Swift

```swift
class Solution {
    func combinationSum2(_ candidates: [Int], _ target: Int) -> [[Int]] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun combinationSum2(candidates: IntArray, target: Int): List<List<Int>> {

    }
}
```

### Go

```golang
func combinationSum2(candidates []int, target int) [][]int {

}
```

### Ruby

```ruby
# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum2(candidates, target)

end
```

### Scala

```scala
object Solution {
    def combinationSum2(candidates: Array[Int], target: Int): List[List[Int]] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn combination_sum2(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {

    }
}
```

### Racket

```racket
(define/contract (combination-sum2 candidates target)
  (-> (listof exact-integer?) exact-integer? (listof (listof exact-integer?)))

  )
```

### Erlang

```erlang
-spec combination_sum2(Candidates :: [integer()], Target :: integer()) -> [[integer()]].
combination_sum2(Candidates, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec combination_sum2(candidates :: [integer], target :: integer) :: [[integer]]
  def combination_sum2(candidates, target) do

  end
end
```

