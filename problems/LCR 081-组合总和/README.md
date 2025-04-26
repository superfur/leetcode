# LCR 081. 组合总和

## 题目描述

<p>给定一个<strong>无重复元素</strong>的正整数数组&nbsp;<code>candidates</code>&nbsp;和一个正整数&nbsp;<code>target</code>&nbsp;，找出&nbsp;<code>candidates</code>&nbsp;中所有可以使数字和为目标数&nbsp;<code>target</code>&nbsp;的唯一组合。</p>

<p><code>candidates</code>&nbsp;中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是不同的。&nbsp;</p>

<p>对于给定的输入，保证和为&nbsp;<code>target</code> 的唯一组合数少于 <code>150</code> 个。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>candidates = [2,3,6,7], target = 7&lt;
<strong>输出: </strong>[[7],[2,2,3]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: </strong>candidates = [2,3,5], target = 8
<strong>输出: </strong>[[2,2,2,2],[2,3,3],[3,5]]</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入: </strong>candidates = [2], target = 1
<strong>输出: </strong>[]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入: </strong>candidates = [1], target = 1
<strong>输出: </strong>[[1]]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入: </strong>candidates = [1], target = 2
<strong>输出: </strong>[[1,1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>
	<li><code>1 &lt;= candidates[i] &lt;= 200</code></li>
	<li><code>candidate</code> 中的每个元素都是独一无二的。</li>
	<li><code>1 &lt;= target &lt;= 500</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 39&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/combination-sum/">https://leetcode-cn.com/problems/combination-sum/</a></p>


## 难度

Medium

## 标签

- 数组
- 回溯

## 示例

```
[2,3,6,7]
7
[2,3,5]
8
[2]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {

    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {

    }
}
```

### Python

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
```

### Python3

```python3
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
```

### C

```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** combinationSum(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes){

}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> CombinationSum(int[] candidates, int target) {

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
var combinationSum = function(candidates, target) {

};
```

### TypeScript

```typescript
function combinationSum(candidates: number[], target: number): number[][] {

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
    function combinationSum($candidates, $target) {

    }
}
```

### Swift

```swift
class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun combinationSum(candidates: IntArray, target: Int): List<List<Int>> {

    }
}
```

### Go

```golang
func combinationSum(candidates []int, target int) [][]int {

}
```

### Ruby

```ruby
# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum(candidates, target)

end
```

### Scala

```scala
object Solution {
    def combinationSum(candidates: Array[Int], target: Int): List[List[Int]] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {

    }
}
```

### Racket

```racket
(define/contract (combination-sum candidates target)
  (-> (listof exact-integer?) exact-integer? (listof (listof exact-integer?)))

  )
```

### Erlang

```erlang
-spec combination_sum(Candidates :: [integer()], Target :: integer()) -> [[integer()]].
combination_sum(Candidates, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec combination_sum(candidates :: [integer], target :: integer) :: [[integer]]
  def combination_sum(candidates, target) do

  end
end
```

