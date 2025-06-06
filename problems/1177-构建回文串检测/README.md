# 1177. 构建回文串检测

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>，请你对&nbsp;<code>s</code>&nbsp;的子串进行检测。</p>

<p>每次检测，待检子串都可以表示为&nbsp;<code>queries[i] = [left, right, k]</code>。我们可以 <strong>重新排列</strong> 子串&nbsp;<code>s[left], ..., s[right]</code>，并从中选择 <strong>最多</strong> <code>k</code>&nbsp;项替换成任何小写英文字母。&nbsp;</p>

<p>如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为&nbsp;<code>true</code>，否则结果为&nbsp;<code>false</code>。</p>

<p>返回答案数组&nbsp;<code>answer[]</code>，其中&nbsp;<code>answer[i]</code>&nbsp;是第&nbsp;<code>i</code>&nbsp;个待检子串&nbsp;<code>queries[i]</code>&nbsp;的检测结果。</p>

<p>注意：在替换时，子串中的每个字母都必须作为 <strong>独立的</strong> 项进行计数，也就是说，如果&nbsp;<code>s[left..right] = &quot;aaa&quot;</code>&nbsp;且&nbsp;<code>k = 2</code>，我们只能替换其中的两个字母。（另外，任何检测都不会修改原始字符串 <code>s</code>，可以认为每次检测都是独立的）</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>s = &quot;abcda&quot;, queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
<strong>输出：</strong>[true,false,false,true,true]
<strong>解释：</strong>
queries[0] : 子串 = &quot;d&quot;，回文。
queries[1] :&nbsp;子串 = &quot;bc&quot;，不是回文。
queries[2] :&nbsp;子串 = &quot;abcd&quot;，只替换 1 个字符是变不成回文串的。
queries[3] :&nbsp;子串 = &quot;abcd&quot;，可以变成回文的 &quot;abba&quot;。 也可以变成 &quot;baab&quot;，先重新排序变成 &quot;bacd&quot;，然后把 &quot;cd&quot; 替换为 &quot;ab&quot;。
queries[4] :&nbsp;子串 = &quot;abcda&quot;，可以变成回文的 &quot;abcba&quot;。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length,&nbsp;queries.length&nbsp;&lt;= 10^5</code></li>
	<li><code>0 &lt;= queries[i][0] &lt;= queries[i][1] &lt;&nbsp;s.length</code></li>
	<li><code>0 &lt;= queries[i][2] &lt;= s.length</code></li>
	<li><code>s</code> 中只有小写英文字母</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 哈希表
- 字符串
- 前缀和

## 提示

1. Since we can rearrange the substring, all we care about is the frequency of each character in that substring.
2. How to find the character frequencies efficiently ?
3. As a preprocess, calculate the accumulate frequency of all characters for all prefixes of the string.
4. How to check if a substring can be changed to a palindrome given its characters frequency ?
5. Count the number of odd frequencies, there can be at most one odd frequency in a palindrome.

## 示例

```
"abcda"
[[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
"lyb"
[[0,1,0],[2,2,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<bool> canMakePaliQueries(string s, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Boolean> canMakePaliQueries(String s, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
```

### Python3

```python3
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* canMakePaliQueries(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<bool> CanMakePaliQueries(string s, int[][] queries) {
        
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
var canMakePaliQueries = function(s, queries) {
    
};
```

### TypeScript

```typescript
function canMakePaliQueries(s: string, queries: number[][]): boolean[] {
    
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
    function canMakePaliQueries($s, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canMakePaliQueries(_ s: String, _ queries: [[Int]]) -> [Bool] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canMakePaliQueries(s: String, queries: Array<IntArray>): List<Boolean> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<bool> canMakePaliQueries(String s, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func canMakePaliQueries(s string, queries [][]int) []bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer[][]} queries
# @return {Boolean[]}
def can_make_pali_queries(s, queries)
    
end
```

### Scala

```scala
object Solution {
    def canMakePaliQueries(s: String, queries: Array[Array[Int]]): List[Boolean] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_make_pali_queries(s: String, queries: Vec<Vec<i32>>) -> Vec<bool> {
        
    }
}
```

### Racket

```racket
(define/contract (can-make-pali-queries s queries)
  (-> string? (listof (listof exact-integer?)) (listof boolean?))
  )
```

### Erlang

```erlang
-spec can_make_pali_queries(S :: unicode:unicode_binary(), Queries :: [[integer()]]) -> [boolean()].
can_make_pali_queries(S, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_make_pali_queries(s :: String.t, queries :: [[integer]]) :: [boolean]
  def can_make_pali_queries(s, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canMakePaliQueries(s: String, queries: Array<Array<Int64>>): ArrayList<Bool> {

    }
}
```

