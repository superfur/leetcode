# 2564. 子字符串异或查询

## 题目描述

<p>给你一个 <strong>二进制字符串</strong>&nbsp;<code>s</code>&nbsp;和一个整数数组&nbsp;<code>queries</code>&nbsp;，其中&nbsp;<code>queries[i] = [first<sub>i</sub>, second<sub>i</sub>]</code>&nbsp;。</p>

<p>对于第&nbsp;<code>i</code>&nbsp;个查询，找到 <code>s</code>&nbsp;的 <strong>最短子字符串</strong>&nbsp;，它对应的 <strong>十进制</strong>值&nbsp;<code>val</code>&nbsp;与&nbsp;<code>first<sub>i</sub></code>&nbsp;<b>按位异或</b>&nbsp;得到&nbsp;<code>second<sub>i</sub></code>&nbsp;，换言之，<code>val ^ first<sub>i</sub> == second<sub>i</sub></code>&nbsp;。</p>

<p>第&nbsp;<code>i</code>&nbsp;个查询的答案是子字符串&nbsp;<code>[left<sub>i</sub>, right<sub>i</sub>]</code> 的两个端点（下标从&nbsp;<strong>0</strong>&nbsp;开始），如果不存在这样的子字符串，则答案为&nbsp;<code>[-1, -1]</code>&nbsp;。如果有多个答案，请你选择&nbsp;<code>left<sub>i</sub></code>&nbsp;最小的一个。</p>

<p>请你返回一个数组&nbsp;<code>ans</code>&nbsp;，其中&nbsp;<code>ans[i] = [left<sub>i</sub>, right<sub>i</sub>]</code>&nbsp;是第&nbsp;<code>i</code>&nbsp;个查询的答案。</p>

<p><strong>子字符串</strong>&nbsp;是一个字符串中一段连续非空的字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "101101", queries = [[0,5],[1,2]]
<b>输出：</b>[[0,2],[2,3]]
<b>解释：</b>第一个查询，端点为 <code>[0,2]</code> 的子字符串为 <strong>"101"</strong> ，对应十进制数字 <strong><code>5 ，且</code></strong> <strong><code>5 ^ 0 = 5</code></strong>&nbsp;，所以第一个查询的答案为 <code>[0,2]。第二个查询中，</code>端点为 <code>[2,3] 的子字符串为 </code><strong>"11" ，对应十进制数字</strong> <strong>3</strong>&nbsp;，且 <strong>3<code> ^ 1 = 2</code></strong><code>&nbsp;。所以第二个查询的答案为</code> <code>[2,3]</code> 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "0101", queries = [[12,8]]
<b>输出：</b>[[-1,-1]]
<b>解释：</b>这个例子中，没有符合查询的答案，所以返回 <code>[-1,-1] 。</code>
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>s = "1", queries = [[4,5]]
<b>输出：</b>[[0,0]]
<b>解释：</b>这个例子中，端点为 <code>[0,0]</code> 的子字符串对应的十进制值为 <strong><code>1</code></strong><code>&nbsp;，且</code> <strong><code>1 ^ 4 = 5</code></strong><code>&nbsp;。所以答案为</code> <code>[0,0] 。</code>
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s[i]</code>&nbsp;要么是&nbsp;<code>'0'</code>&nbsp;，要么是&nbsp;<code>'1'</code>&nbsp;。</li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= first<sub>i</sub>, second<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 位运算
- 数组
- 哈希表
- 字符串

## 提示

1. You do not need to consider substrings having lengths greater than 30.
2. Pre-process all substrings with lengths not greater than 30, and add the best endpoints to a dictionary.

## 示例

```
"101101"
[[0,5],[1,2]]
"0101"
[[12,8]]
"1"
[[4,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> substringXorQueries(string s, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] substringXorQueries(String s, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def substringXorQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** substringXorQueries(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] SubstringXorQueries(string s, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {number[][]}
 */
var substringXorQueries = function(s, queries) {
    
};
```

### TypeScript

```typescript
function substringXorQueries(s: string, queries: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Integer[][]
     */
    function substringXorQueries($s, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func substringXorQueries(_ s: String, _ queries: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun substringXorQueries(s: String, queries: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> substringXorQueries(String s, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func substringXorQueries(s string, queries [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[][]}
def substring_xor_queries(s, queries)
    
end
```

### Scala

```scala
object Solution {
    def substringXorQueries(s: String, queries: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn substring_xor_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (substring-xor-queries s queries)
  (-> string? (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec substring_xor_queries(S :: unicode:unicode_binary(), Queries :: [[integer()]]) -> [[integer()]].
substring_xor_queries(S, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec substring_xor_queries(s :: String.t, queries :: [[integer]]) :: [[integer]]
  def substring_xor_queries(s, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func substringXorQueries(s: String, queries: Array<Array<Int64>>): Array<Array<Int64>> {

    }
}
```

