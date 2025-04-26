# 2559. 统计范围内的元音字符串数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串数组 <code>words</code> 以及一个二维整数数组 <code>queries</code> 。</p>

<p>每个查询 <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code> 会要求我们统计在 <code>words</code> 中下标在 <code>l<sub>i</sub></code> 到 <code>r<sub>i</sub></code> 范围内（<strong>包含</strong> 这两个值）并且以元音开头和结尾的字符串的数目。</p>

<p>返回一个整数数组，其中数组的第 <code>i</code> 个元素对应第 <code>i</code> 个查询的答案。</p>

<p><strong>注意：</strong>元音字母是 <code>'a'</code>、<code>'e'</code>、<code>'i'</code>、<code>'o'</code> 和 <code>'u'</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
<strong>输出：</strong>[2,3,0]
<strong>解释：</strong>以元音开头和结尾的字符串是 "aba"、"ece"、"aa" 和 "e" 。
查询 [0,2] 结果为 2（字符串 "aba" 和 "ece"）。
查询 [1,4] 结果为 3（字符串 "ece"、"aa"、"e"）。
查询 [1,1] 结果为 0 。
返回结果 [2,3,0] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
<strong>输出：</strong>[3,2,1]
<strong>解释：</strong>每个字符串都满足这一条件，所以返回 [3,2,1] 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 40</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成</li>
	<li><code>sum(words[i].length) &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= queries[j][0] &lt;= queries[j][1] &lt;&nbsp;words.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 字符串
- 前缀和

## 提示

1. Precompute the prefix sum of strings that start and end with vowels.
2. Use unordered_set to store vowels.
3. Check if the first and last characters of the string are present in the vowels set.
4. Subtract prefix sum for range [l-1, r] to find the number of strings starting and ending with vowels.

## 示例

```
["aba","bcb","ece","aa","e"]
[[0,2],[1,4],[1,1]]
["a","e","i"]
[[0,2],[0,1],[2,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* vowelStrings(char** words, int wordsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] VowelStrings(string[] words, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {number[][]} queries
 * @return {number[]}
 */
var vowelStrings = function(words, queries) {
    
};
```

### TypeScript

```typescript
function vowelStrings(words: string[], queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function vowelStrings($words, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func vowelStrings(_ words: [String], _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun vowelStrings(words: Array<String>, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> vowelStrings(List<String> words, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func vowelStrings(words []string, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {Integer[][]} queries
# @return {Integer[]}
def vowel_strings(words, queries)
    
end
```

### Scala

```scala
object Solution {
    def vowelStrings(words: Array[String], queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn vowel_strings(words: Vec<String>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (vowel-strings words queries)
  (-> (listof string?) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec vowel_strings(Words :: [unicode:unicode_binary()], Queries :: [[integer()]]) -> [integer()].
vowel_strings(Words, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec vowel_strings(words :: [String.t], queries :: [[integer]]) :: [integer]
  def vowel_strings(words, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func vowelStrings(words: Array<String>, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

