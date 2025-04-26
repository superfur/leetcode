# 2900. 最长相邻不相等子序列 I

## 题目描述

<p>给你一个下标从&nbsp;<strong>0</strong>&nbsp;开始的字符串数组&nbsp;<code>words</code>&nbsp;，和一个下标从 <strong>0</strong>&nbsp;开始的 <strong>二进制</strong>&nbsp;数组&nbsp;<code>groups</code>&nbsp;，两个数组长度都是&nbsp;<code>n</code>&nbsp;。</p>

<p>你需要从&nbsp;<code>words</code>&nbsp;中选出&nbsp;<strong>最长<span data-keyword="subsequence-array">子序列</span></strong>。如果对于序列中的任何两个连续串，二进制数组&nbsp;<code>groups</code>&nbsp;中它们的对应元素不同，则&nbsp;<code>words</code> 的子序列是不同的。</p>

<p>正式来说，你需要从下标&nbsp;<code>[0, 1, ..., n - 1]</code>&nbsp;中选出一个&nbsp;<strong>最长子序列</strong>&nbsp;，将这个子序列记作长度为 <code>k</code> 的&nbsp;<code>[i<sub>0</sub>, i<sub>1</sub>, ..., i<sub>k - 1</sub>]</code>&nbsp;，对于所有满足&nbsp;<code>0 &lt;= j&nbsp;&lt; k - 1</code>&nbsp;的&nbsp;<code>j</code>&nbsp;都有&nbsp;<code>groups[i<sub>j</sub>] != groups[i<sub>j + 1</sub>]</code>&nbsp;。</p>

<p>请你返回一个字符串数组，它是下标子序列&nbsp;<strong>依次</strong>&nbsp;对应&nbsp;<code>words</code>&nbsp;数组中的字符串连接形成的字符串数组。如果有多个答案，返回 <strong>任意</strong> 一个。</p>

<p><b>注意：</b><code>words</code>&nbsp;中的元素是不同的&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>words = ["e","a","b"], groups = [0,0,1]
<b>输出：</b>["e","b"]
<strong>解释：</strong>一个可行的子序列是 [0,2] ，因为 groups[0] != groups[2] 。
所以一个可行的答案是 [words[0],words[2]] = ["e","b"] 。
另一个可行的子序列是 [1,2] ，因为 groups[1] != groups[2] 。
得到答案为 [words[1],words[2]] = ["a","b"] 。
这也是一个可行的答案。
符合题意的最长子序列的长度为 2 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>words = ["a","b","c","d"], groups = [1,0,1,1]
<b>输出：</b>["a","b","c"]
<b>解释：</b>一个可行的子序列为 [0,1,2] 因为 groups[0] != groups[1] 且 groups[1] != groups[2] 。
所以一个可行的答案是 [words[0],words[1],words[2]] = ["a","b","c"] 。
另一个可行的子序列为 [0,1,3] 因为 groups[0] != groups[1] 且 groups[1] != groups[3] 。
得到答案为 [words[0],words[1],words[3]] = ["a","b","d"] 。
这也是一个可行的答案。
符合题意的最长子序列的长度为 3 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == words.length == groups.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>groups[i]</code>&nbsp;是&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code>。</li>
	<li><code>words</code>&nbsp;中的字符串 <strong>互不相同</strong>&nbsp;。</li>
	<li><code>words[i]</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 字符串
- 动态规划

## 提示

1. This problem can be solved greedily.
2. Begin by constructing the answer starting with the first number in <code>groups</code>.
3. For each index <code>i</code> in the range <code>[1, n - 1]</code>, add <code>i</code> to the answer if <code>groups[i] != groups[i - 1]</code>.

## 示例

```
["c"]
[0]
["d"]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> getLongestSubsequence(vector<string>& words, vector<int>& groups) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> getLongestSubsequence(String[] words, int[] groups) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** getLongestSubsequence(char** words, int wordsSize, int* groups, int groupsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> GetLongestSubsequence(string[] words, int[] groups) {
        
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
var getLongestSubsequence = function(words, groups) {
    
};
```

### TypeScript

```typescript
function getLongestSubsequence(words: string[], groups: number[]): string[] {
    
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
    function getLongestSubsequence($words, $groups) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getLongestSubsequence(_ words: [String], _ groups: [Int]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getLongestSubsequence(words: Array<String>, groups: IntArray): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> getLongestSubsequence(List<String> words, List<int> groups) {
    
  }
}
```

### Go

```golang
func getLongestSubsequence(words []string, groups []int) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {Integer[]} groups
# @return {String[]}
def get_longest_subsequence(words, groups)
    
end
```

### Scala

```scala
object Solution {
    def getLongestSubsequence(words: Array[String], groups: Array[Int]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (get-longest-subsequence words groups)
  (-> (listof string?) (listof exact-integer?) (listof string?))
  )
```

### Erlang

```erlang
-spec get_longest_subsequence(Words :: [unicode:unicode_binary()], Groups :: [integer()]) -> [unicode:unicode_binary()].
get_longest_subsequence(Words, Groups) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_longest_subsequence(words :: [String.t], groups :: [integer]) :: [String.t]
  def get_longest_subsequence(words, groups) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getLongestSubsequence(words: Array<String>, groups: Array<Int64>): ArrayList<String> {

    }
}
```

