# 336. 回文对

## 题目描述

<p>给定一个由唯一字符串构成的 <strong>0 索引&nbsp;</strong>数组 <code>words</code>&nbsp;。</p>

<p><strong>回文对</strong> 是一对整数 <code>(i, j)</code> ，满足以下条件：</p>

<ul>
	<li><code>0 &lt;= i, j &lt; words.length</code>，</li>
	<li><code>i != j</code> ，并且</li>
	<li><code>words[i] + words[j]</code>（两个字符串的连接）是一个<span data-keyword="palindrome-string">回文串</span>。</li>
</ul>

<p>返回一个数组，它包含&nbsp;<code>words</code> 中所有满足 <strong>回文对</strong> 条件的字符串。</p>

<p>你必须设计一个时间复杂度为 <code>O(sum of words[i].length)</code> 的算法。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["abcd","dcba","lls","s","sssll"]
<strong>输出：</strong>[[0,1],[1,0],[3,2],[2,4]] 
<strong>解释：</strong>可拼接成的回文串为 <code>["dcbaabcd","abcddcba","slls","llssssll"]</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["bat","tab","cat"]
<strong>输出：</strong>[[0,1],[1,0]] 
<strong>解释：</strong>可拼接成的回文串为 <code>["battab","tabbat"]</code></pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = ["a",""]
<strong>输出：</strong>[[0,1],[1,0]]
</pre>
&nbsp;

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 5000</code></li>
	<li><code>0 &lt;= words[i].length &lt;= 300</code></li>
	<li><code>words[i]</code> 由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 字典树
- 数组
- 哈希表
- 字符串

## 提示

1. Checking every two pairs will exceed the time limit. It will be O(n^2 * k). We need a faster way.
2. If we hash every string in the array, how can we check if two pairs form a palindrome after the concatenation?
3. We can check every string in words and consider it as words[j] (i.e., the suffix of the target palindrome). We can check if there is a hash of string that can be the prefix to make it a palindrome.

## 示例

```
["abcd","dcba","lls","s","sssll"]
["bat","tab","cat"]
["a",""]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> palindromePairs(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** palindromePairs(char** words, int wordsSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> PalindromePairs(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number[][]}
 */
var palindromePairs = function(words) {
    
};
```

### TypeScript

```typescript
function palindromePairs(words: string[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer[][]
     */
    function palindromePairs($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func palindromePairs(_ words: [String]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun palindromePairs(words: Array<String>): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> palindromePairs(List<String> words) {
    
  }
}
```

### Go

```golang
func palindromePairs(words []string) [][]int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer[][]}
def palindrome_pairs(words)
    
end
```

### Scala

```scala
object Solution {
    def palindromePairs(words: Array[String]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn palindrome_pairs(words: Vec<String>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (palindrome-pairs words)
  (-> (listof string?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec palindrome_pairs(Words :: [unicode:unicode_binary()]) -> [[integer()]].
palindrome_pairs(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec palindrome_pairs(words :: [String.t]) :: [[integer]]
  def palindrome_pairs(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func palindromePairs(words: Array<String>): ArrayList<ArrayList<Int64>> {

    }
}
```

