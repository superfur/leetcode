# 2901. 最长相邻不相等子序列 II

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;和一个下标从&nbsp;<strong>0</strong>&nbsp;开始的字符串数组&nbsp;<code>words</code>&nbsp;，和一个下标从&nbsp;<strong>0</strong>&nbsp;开始的数组&nbsp;<code>groups</code>&nbsp;，两个数组长度都是&nbsp;<code>n</code>&nbsp;。</p>

<p>两个长度相等字符串的 <strong>汉明距离</strong>&nbsp;定义为对应位置字符&nbsp;<strong>不同</strong>&nbsp;的数目。</p>

<p>你需要从下标&nbsp;<code>[0, 1, ..., n - 1]</code>&nbsp;中选出一个&nbsp;<strong>最长<span data-keyword="subsequence-array">子序列</span></strong>&nbsp;，将这个子序列记作长度为 <code>k</code> 的&nbsp;<code>[i<sub>0</sub>, i<sub>1</sub>, ..., i<sub>k - 1</sub>]</code>&nbsp;，它需要满足以下条件：</p>

<ul>
	<li><strong>相邻</strong> 下标对应的 <code>groups</code> 值 <strong>不同</strong>。即，对于所有满足&nbsp;<code>0 &lt; j + 1 &lt; k</code>&nbsp;的&nbsp;<code>j</code>&nbsp;都有&nbsp;<code>groups[i<sub>j</sub>] != groups[i<sub>j + 1</sub>]</code>&nbsp;。</li>
	<li>对于所有&nbsp;<code>0 &lt; j + 1 &lt; k</code>&nbsp;的下标&nbsp;<code>j</code>&nbsp;，都满足&nbsp;<code>words[i<sub>j</sub>]</code> 和&nbsp;<code>words[i<sub>j + 1</sub>]</code>&nbsp;的长度 <strong>相等</strong>&nbsp;，且两个字符串之间的 <strong>汉明距离</strong>&nbsp;为 <code>1</code>&nbsp;。</li>
</ul>

<p>请你返回一个字符串数组，它是下标子序列&nbsp;<strong>依次</strong>&nbsp;对应&nbsp;<code>words</code>&nbsp;数组中的字符串连接形成的字符串数组。如果有多个答案，返回任意一个。</p>

<p><strong>子序列</strong>&nbsp;指的是从原数组中删掉一些（也可能一个也不删掉）元素，剩余元素不改变相对位置得到的新的数组。</p>

<p><b>注意：</b><code>words</code>&nbsp;中的字符串长度可能&nbsp;<strong>不相等</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>n = 3, words = ["bab","dab","cab"], groups = [1,2,2]
<b>输出：</b>["bab","cab"]
<b>解释：</b>一个可行的子序列是 [0,2] 。
- groups[0] != groups[2]
- words[0].length == words[2].length 且它们之间的汉明距离为 1 。
所以一个可行的答案是 [words[0],words[2]] = ["bab","cab"] 。
另一个可行的子序列是 [0,1] 。
- groups[0] != groups[1]
- words[0].length = words[1].length 且它们之间的汉明距离为 1 。
所以另一个可行的答案是 [words[0],words[1]] = ["bab","dab"] 。
符合题意的最长子序列的长度为 2 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>n = 4, words = ["a","b","c","d"], groups = [1,2,3,4]
<b>输出：</b>["a","b","c","d"]
<b>解释：</b>我们选择子序列 [0,1,2,3] 。
它同时满足两个条件。
所以答案为 [words[0],words[1],words[2],words[3]] = ["a","b","c","d"] 。
它是所有下标子序列里最长且满足所有条件的。
所以它是唯一的答案。
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= n == words.length == groups.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= groups[i] &lt;= n</code></li>
	<li><code>words</code>&nbsp;中的字符串&nbsp;<strong>互不相同</strong>&nbsp;。</li>
	<li><code>words[i]</code> 只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 字符串
- 动态规划

## 提示

1. Let <code>dp[i]</code> represent the length of the longest subsequence ending with <code>words[i]</code> that satisfies the conditions.
2. <code>dp[i] =</code> (maximum value of <code>dp[j]</code>) <code>+ 1</code> for indices <code>j < i</code>, where <code>groups[i] != groups[j]</code>, <code>words[i]</code> and <code>words[j]</code> are equal in length, and the hamming distance between <code>words[i]</code> and <code>words[j]</code> is exactly <code>1</code>.
3. Keep track of the <code>j</code> values used to achieve the maximum <code>dp[i]</code> for each index <code>i</code>.
4. The expected array's length is <code>max(dp[0:n])</code>, and starting from the index having the maximum value in <code>dp</code>, we can trace backward to get the words.

## 示例

```
["bab","dab","cab"]
[1,2,2]
["a","b","c","d"]
[1,2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> getWordsInLongestSubsequence(vector<string>& words, vector<int>& groups) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> getWordsInLongestSubsequence(String[] words, int[] groups) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** getWordsInLongestSubsequence(char** words, int wordsSize, int* groups, int groupsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> GetWordsInLongestSubsequence(string[] words, int[] groups) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {number[]} groups
 * @return {string[]}
 */
var getWordsInLongestSubsequence = function(words, groups) {
    
};
```

### TypeScript

```typescript
function getWordsInLongestSubsequence(words: string[], groups: number[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param Integer[] $groups
     * @return String[]
     */
    function getWordsInLongestSubsequence($words, $groups) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getWordsInLongestSubsequence(_ words: [String], _ groups: [Int]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getWordsInLongestSubsequence(words: Array<String>, groups: IntArray): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> getWordsInLongestSubsequence(List<String> words, List<int> groups) {
    
  }
}
```

### Go

```golang
func getWordsInLongestSubsequence(words []string, groups []int) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {Integer[]} groups
# @return {String[]}
def get_words_in_longest_subsequence(words, groups)
    
end
```

### Scala

```scala
object Solution {
    def getWordsInLongestSubsequence(words: Array[String], groups: Array[Int]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_words_in_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (get-words-in-longest-subsequence words groups)
  (-> (listof string?) (listof exact-integer?) (listof string?))
  )
```

### Erlang

```erlang
-spec get_words_in_longest_subsequence(Words :: [unicode:unicode_binary()], Groups :: [integer()]) -> [unicode:unicode_binary()].
get_words_in_longest_subsequence(Words, Groups) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_words_in_longest_subsequence(words :: [String.t], groups :: [integer]) :: [String.t]
  def get_words_in_longest_subsequence(words, groups) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getWordsInLongestSubsequence(words: Array<String>, groups: Array<Int64>): ArrayList<String> {

    }
}
```

