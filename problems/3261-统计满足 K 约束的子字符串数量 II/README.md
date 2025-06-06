# 3261. 统计满足 K 约束的子字符串数量 II

## 题目描述

<p>给你一个 <strong>二进制</strong> 字符串 <code>s</code> 和一个整数 <code>k</code>。</p>

<p>另给你一个二维整数数组 <code>queries</code> ，其中 <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code> 。</p>

<p>如果一个 <strong>二进制字符串</strong> 满足以下任一条件，则认为该字符串满足 <strong>k 约束</strong>：</p>

<ul>
	<li>字符串中 <code>0</code> 的数量最多为 <code>k</code>。</li>
	<li>字符串中 <code>1</code> 的数量最多为 <code>k</code>。</li>
</ul>

<p>返回一个整数数组 <code>answer</code> ，其中 <code>answer[i]</code> 表示 <code>s[l<sub>i</sub>..r<sub>i</sub>]</code> 中满足 <strong>k 约束</strong> 的 <span data-keyword="substring-nonempty">子字符串</span> 的数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "0001111", k = 2, queries = [[0,6]]</span></p>

<p><strong>输出：</strong><span class="example-io">[26]</span></p>

<p><strong>解释：</strong></p>

<p>对于查询 <code>[0, 6]</code>， <code>s[0..6] = "0001111"</code> 的所有子字符串中，除 <code>s[0..5] = "000111"</code> 和 <code>s[0..6] = "0001111"</code> 外，其余子字符串都满足 k 约束。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]</span></p>

<p><strong>输出：</strong><span class="example-io">[15,9,3]</span></p>

<p><strong>解释：</strong></p>

<p><code>s</code> 的所有子字符串中，长度大于 3 的子字符串都不满足 k 约束。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 是 <code>'0'</code> 或 <code>'1'</code></li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i] == [l<sub>i</sub>, r<sub>i</sub>]</code></li>
	<li><code>0 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt; s.length</code></li>
	<li>所有查询互不相同</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 字符串
- 二分查找
- 前缀和
- 滑动窗口

## 提示

1. Answering online queries is tough. Try to answer them offline since the queries are known beforehand.
2. For each index, how do you calculate the left boundary so that the given condition is satisfied?
3. Using the precomputed left boundaries and a range data structure, you can now answer the queries optimally.

## 示例

```
"0001111"
2
[[0,6]]
"010101"
1
[[0,5],[1,4],[2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> countKConstraintSubstrings(string s, int k, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public long[] countKConstraintSubstrings(String s, int k, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countKConstraintSubstrings(self, s, k, queries):
        """
        :type s: str
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* countKConstraintSubstrings(char* s, int k, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long[] CountKConstraintSubstrings(string s, int k, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @param {number[][]} queries
 * @return {number[]}
 */
var countKConstraintSubstrings = function(s, k, queries) {
    
};
```

### TypeScript

```typescript
function countKConstraintSubstrings(s: string, k: number, queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function countKConstraintSubstrings($s, $k, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countKConstraintSubstrings(_ s: String, _ k: Int, _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countKConstraintSubstrings(s: String, k: Int, queries: Array<IntArray>): LongArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countKConstraintSubstrings(String s, int k, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func countKConstraintSubstrings(s string, k int, queries [][]int) []int64 {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @param {Integer[][]} queries
# @return {Integer[]}
def count_k_constraint_substrings(s, k, queries)
    
end
```

### Scala

```scala
object Solution {
    def countKConstraintSubstrings(s: String, k: Int, queries: Array[Array[Int]]): Array[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_k_constraint_substrings(s: String, k: i32, queries: Vec<Vec<i32>>) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (count-k-constraint-substrings s k queries)
  (-> string? exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_k_constraint_substrings(S :: unicode:unicode_binary(), K :: integer(), Queries :: [[integer()]]) -> [integer()].
count_k_constraint_substrings(S, K, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_k_constraint_substrings(s :: String.t, k :: integer, queries :: [[integer]]) :: [integer]
  def count_k_constraint_substrings(s, k, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countKConstraintSubstrings(s: String, k: Int64, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

