# 2983. 回文串重新排列查询

## 题目描述

<p>给你一个长度为 <strong>偶数</strong>&nbsp;<code>n</code>&nbsp;，下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>s</code>&nbsp;。</p>

<p>同时给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>queries</code>&nbsp;，其中&nbsp;<code>queries[i] = [a<sub>i</sub>, b<sub>i</sub>, c<sub>i</sub>, d<sub>i</sub>]</code>&nbsp;。</p>

<p>对于每个查询&nbsp;<code>i</code>&nbsp;，你需要执行以下操作：</p>

<ul>
	<li>将下标在范围&nbsp;<code>0 &lt;= a<sub>i</sub> &lt;= b<sub>i</sub> &lt; n / 2</code>&nbsp;内的&nbsp;<strong>子字符串</strong>&nbsp;<code>s[a<sub>i</sub>:b<sub>i</sub>]</code>&nbsp;中的字符重新排列。</li>
	<li>将下标在范围 <code>n / 2 &lt;= c<sub>i</sub> &lt;= d<sub>i</sub> &lt; n</code>&nbsp;内的 <strong>子字符串</strong>&nbsp;<code>s[c<sub>i</sub>:d<sub>i</sub>]</code>&nbsp;中的字符重新排列。</li>
</ul>

<p>对于每个查询，你的任务是判断执行操作后能否让 <code>s</code>&nbsp;变成一个 <strong>回文串</strong> 。</p>

<p>每个查询与其他查询都是 <strong>独立的</strong>&nbsp;。</p>

<p>请你返回一个下标从 <strong>0</strong>&nbsp;开始的数组<em>&nbsp;</em><code>answer</code>&nbsp;，如果第&nbsp;<code>i</code>&nbsp;个查询执行操作后，可以将&nbsp;<code>s</code>&nbsp;变为一个回文串，那么<em>&nbsp;</em><code>answer[i] =&nbsp;true</code>，否则为<em>&nbsp;</em><code>false</code>&nbsp;。</p>

<ul>
	<li><strong>子字符串</strong>&nbsp;指的是一个字符串中一段连续的字符序列。</li>
	<li><code>s[x:y]</code>&nbsp;表示 <code>s</code>&nbsp;中从下标 <code>x</code>&nbsp;到 <code>y</code>&nbsp;且两个端点 <strong>都包含</strong>&nbsp;的子字符串。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>s = "abcabc", queries = [[1,1,3,5],[0,2,5,5]]
<b>输出：</b>[true,true]
<b>解释：</b>这个例子中，有 2 个查询：
第一个查询：
- a<sub>0</sub> = 1, b<sub>0</sub> = 1, c<sub>0</sub> = 3, d<sub>0</sub> = 5
- 你可以重新排列 s[1:1] =&gt; a<em><strong>b</strong></em>cabc 和 s[3:5] =&gt; abc<em><strong>abc</strong></em>&nbsp;。
- 为了让 s 变为回文串，s[3:5] 可以重新排列得到 =&gt; abc<strong><em>cba </em></strong>。
- 现在 s 是一个回文串。所以 answer[0] = true 。
第二个查询：
- a<sub>1</sub> = 0, b<sub>1</sub> = 2, c<sub>1</sub> = 5, d<sub>1</sub> = 5.
- 你可以重新排列 s[0:2] =&gt; <em><strong>abc</strong></em>abc 和 s[5:5] =&gt; abcab<strong><em>c</em></strong>&nbsp;。
- 为了让 s 变为回文串，s[0:2] 可以重新排列得到 =&gt; <em><strong>cba</strong></em>abc 。
- 现在 s 是一个回文串，所以 answer[1] = true 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>s = "abbcdecbba", queries = [[0,2,7,9]]
<b>输出：</b>[false]
<b>解释：</b>这个示例中，只有一个查询。
a<sub>0</sub> = 0, b<sub>0</sub> = 2, c<sub>0</sub> = 7, d<sub>0</sub> = 9.
你可以重新排列 s[0:2] =&gt; <em><strong>abb</strong></em>cdecbba 和 s[7:9] =&gt; abbcdec<em><strong>bba</strong></em>&nbsp;。
无法通过重新排列这些子字符串使 s 变为一个回文串，因为 s[3:6] 不是一个回文串。
所以 answer[0] = false 。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>s = "acbcab", queries = [[1,2,4,5]]
<b>输出：</b>[true]
<strong>解释：</strong>这个示例中，只有一个查询。
a<sub>0</sub> = 1, b<sub>0</sub> = 2, c<sub>0</sub> = 4, d<sub>0</sub> = 5.
你可以重新排列 s[1:2] =&gt; a<em><strong>cb</strong></em>cab 和 s[4:5] =&gt; acbc<strong><em>ab</em></strong>&nbsp;。
为了让 s 变为回文串，s[1:2] 可以重新排列得到 =&gt; a<em><strong>bc</strong></em>cab<code>&nbsp;</code>。
然后 s[4:5] 重新排列得到 abcc<em><strong>ba</strong></em>&nbsp;。
现在 s 是一个回文串，所以 answer[0] = true 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n == s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length == 4</code></li>
	<li><code>a<sub>i</sub> == queries[i][0], b<sub>i</sub> == queries[i][1]</code></li>
	<li><code>c<sub>i</sub> == queries[i][2], d<sub>i</sub> == queries[i][3]</code></li>
	<li><code>0 &lt;= a<sub>i</sub> &lt;= b<sub>i</sub> &lt; n / 2</code></li>
	<li><code>n / 2 &lt;= c<sub>i</sub> &lt;= d<sub>i</sub> &lt; n </code></li>
	<li><code>n</code>&nbsp;是一个偶数。</li>
	<li><code>s</code> 只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 哈希表
- 字符串
- 前缀和

## 提示

1. Consider two indices, <code>x</code> on the left side and its symmetrical index <code>y</code> on the right side.
2. Store the frequencies of all of the letters in both intervals <code>[a<sub>i</sub>, b<sub>i</sub>]</code> and <code>[c<sub>i</sub>, d<sub>i</sub>]</code> in a query.
3. If <code>x</code> is not in <code>[a<sub>i</sub>, b<sub>i</sub>]</code> and <code>y</code> is not in <code>[c<sub>i</sub>, d<sub>i</sub>]</code>, they must be the same.
4. If <code>x</code> is in <code>[a<sub>i</sub>, b<sub>i</sub>]</code> and <code>y</code> is not in <code>[c<sub>i</sub>, d<sub>i</sub>]</code>, remove one occurrence of the character at index <code>y</code> from the frequency array on the left side.
5. Similarly, if <code>x</code> is not in <code>[a<sub>i</sub>, b<sub>i</sub>]</code> and <code>y</code> is in <code>[c<sub>i</sub>, d<sub>i</sub>]</code>, remove one occurrence of the character at index <code>x</code> from the frequency array on the right side.
6. Finally, check whether the two frequency arrays are the same, and the indices that don't fall into any of the intervals are the same as well.
7. Use prefix-sum + hashing to improve the time complexity.

## 示例

```
"abcabc"
[[1,1,3,5],[0,2,5,5]]
"abbcdecbba"
[[0,2,7,9]]
"acbcab"
[[1,2,4,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<bool> canMakePalindromeQueries(string s, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean[] canMakePalindromeQueries(String s, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canMakePalindromeQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
```

### Python3

```python3
class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* canMakePalindromeQueries(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool[] CanMakePalindromeQueries(string s, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var canMakePalindromeQueries = function(s, queries) {
    
};
```

### TypeScript

```typescript
function canMakePalindromeQueries(s: string, queries: number[][]): boolean[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function canMakePalindromeQueries($s, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canMakePalindromeQueries(_ s: String, _ queries: [[Int]]) -> [Bool] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canMakePalindromeQueries(s: String, queries: Array<IntArray>): BooleanArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<bool> canMakePalindromeQueries(String s, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func canMakePalindromeQueries(s string, queries [][]int) []bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer[][]} queries
# @return {Boolean[]}
def can_make_palindrome_queries(s, queries)
    
end
```

### Scala

```scala
object Solution {
    def canMakePalindromeQueries(s: String, queries: Array[Array[Int]]): Array[Boolean] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_make_palindrome_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<bool> {
        
    }
}
```

### Racket

```racket
(define/contract (can-make-palindrome-queries s queries)
  (-> string? (listof (listof exact-integer?)) (listof boolean?))
  )
```

### Erlang

```erlang
-spec can_make_palindrome_queries(S :: unicode:unicode_binary(), Queries :: [[integer()]]) -> [boolean()].
can_make_palindrome_queries(S, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_make_palindrome_queries(s :: String.t, queries :: [[integer]]) :: [boolean]
  def can_make_palindrome_queries(s, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canMakePalindromeQueries(s: String, queries: Array<Array<Int64>>): Array<Bool> {

    }
}
```

