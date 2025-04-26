# 985. 查询后的偶数和

## 题目描述

<p>给出一个整数数组&nbsp;<code>A</code>&nbsp;和一个查询数组&nbsp;<code>queries</code>。</p>

<p>对于第&nbsp;<code>i</code>&nbsp;次查询，有&nbsp;<code>val =&nbsp;queries[i][0], index&nbsp;= queries[i][1]</code>，我们会把&nbsp;<code>val</code>&nbsp;加到&nbsp;<code>A[index]</code>&nbsp;上。然后，第&nbsp;<code>i</code>&nbsp;次查询的答案是 <code>A</code> 中偶数值的和。</p>

<p><em>（此处给定的&nbsp;<code>index = queries[i][1]</code>&nbsp;是从 0 开始的索引，每次查询都会永久修改数组&nbsp;<code>A</code>。）</em></p>

<p>返回所有查询的答案。你的答案应当以数组&nbsp;<code>answer</code>&nbsp;给出，<code>answer[i]</code>&nbsp;为第&nbsp;<code>i</code>&nbsp;次查询的答案。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
<strong>输出：</strong>[8,6,2,4]
<strong>解释：</strong>
开始时，数组为 [1,2,3,4]。
将 1 加到 A[0] 上之后，数组为 [2,2,3,4]，偶数值之和为 2 + 2 + 4 = 8。
将 -3 加到 A[1] 上之后，数组为 [2,-1,3,4]，偶数值之和为 2 + 4 = 6。
将 -4 加到 A[0] 上之后，数组为 [-2,-1,3,4]，偶数值之和为 -2 + 4 = 2。
将 2 加到 A[3] 上之后，数组为 [-2,-1,3,6]，偶数值之和为 -2 + 6 = 4。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>-10000 &lt;= A[i] &lt;= 10000</code></li>
	<li><code>1 &lt;= queries.length &lt;= 10000</code></li>
	<li><code>-10000 &lt;= queries[i][0] &lt;= 10000</code></li>
	<li><code>0 &lt;= queries[i][1] &lt; A.length</code></li>
</ol>


## 难度

Medium

## 标签

- 数组
- 模拟

## 示例

```
[1,2,3,4]
[[1,0],[-3,1],[-4,0],[2,3]]
[1]
[[4,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumEvenAfterQueries(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SumEvenAfterQueries(int[] nums, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var sumEvenAfterQueries = function(nums, queries) {
    
};
```

### TypeScript

```typescript
function sumEvenAfterQueries(nums: number[], queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function sumEvenAfterQueries($nums, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumEvenAfterQueries(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumEvenAfterQueries(nums: IntArray, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> sumEvenAfterQueries(List<int> nums, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func sumEvenAfterQueries(nums []int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def sum_even_after_queries(nums, queries)
    
end
```

### Scala

```scala
object Solution {
    def sumEvenAfterQueries(nums: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_even_after_queries(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (sum-even-after-queries nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec sum_even_after_queries(Nums :: [integer()], Queries :: [[integer()]]) -> [integer()].
sum_even_after_queries(Nums, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_even_after_queries(nums :: [integer], queries :: [[integer]]) :: [integer]
  def sum_even_after_queries(nums, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumEvenAfterQueries(nums: Array<Int64>, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

