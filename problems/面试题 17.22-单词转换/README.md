# 面试题 17.22. 单词转换

## 题目描述

<p>给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。</p>

<p>编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

<strong>输出：</strong>
["hit","hot","dot","lot","log","cog"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

<strong>输出：</strong>[]

<strong>解释：</strong><em>endWord</em> "cog" 不在字典中，所以不存在符合要求的转换序列。</pre>


## 难度

Medium

## 标签

- 广度优先搜索
- 哈希表
- 字符串
- 回溯

## 提示

1. 从一个蛮力的递归解法开始。只需要创建所有一次编辑的单词，检查它们是否在字典中，然后尝试该编辑路径。
2. 一旦你有了一个蛮力解法，就可以尝试找到一个更快的方法以得到所有一次编辑的有效单词。当绝大多数字符串都不是有效的字典单词时，你不会想创建所有一次编辑的字符串。
3. 为了快速得到编辑距离为1的有效单词，试着将字典中的单词以一种有效的方式进行分组。注意，b_ll形式的所有单词（如bill、ball、bell和bull）的编辑距离为1。然而，这些并不是仅有的编辑距离为1的单词。
4. 创建从通配符形式（如b_ll）到该通配符所匹配的所有单词的映射。然后，当你想要查找与bill相隔编辑距离为1的所有单词时，可以在映射中查找_ill、b_ll、bi_l和bil_。
5. 你之前的算法可能类似于深度优先搜索。你能使它更快吗?
6. 广度优先的搜索通常比深度优先的搜索要快。在最坏的情况下未必如此，但在很多情况下都是这样。为什么？你能找到更快的方法吗？
7. 如果同时从起始单词和目标单词开始进行广度优先搜索，结果会怎样？

## 示例

```
"hit"
"cog"
["hot","dot","dog","lot","log","cog"]
"hit"
"cog"
["hot","dot","dog","lot","log"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> findLadders(String beginWord, String endWord, List<String> wordList) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findLadders(char* beginWord, char* endWord, char** wordList, int wordListSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> FindLadders(string beginWord, string endWord, IList<string> wordList) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {string[]}
 */
var findLadders = function(beginWord, endWord, wordList) {
    
};
```

### TypeScript

```typescript
function findLadders(beginWord: string, endWord: string, wordList: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $beginWord
     * @param String $endWord
     * @param String[] $wordList
     * @return String[]
     */
    function findLadders($beginWord, $endWord, $wordList) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLadders(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLadders(beginWord: String, endWord: String, wordList: List<String>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> findLadders(String beginWord, String endWord, List<String> wordList) {
    
  }
}
```

### Go

```golang
func findLadders(beginWord string, endWord string, wordList []string) []string {
    
}
```

### Ruby

```ruby
# @param {String} begin_word
# @param {String} end_word
# @param {String[]} word_list
# @return {String[]}
def find_ladders(begin_word, end_word, word_list)
    
end
```

### Scala

```scala
object Solution {
    def findLadders(beginWord: String, endWord: String, wordList: List[String]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_ladders(begin_word: String, end_word: String, word_list: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (find-ladders beginWord endWord wordList)
  (-> string? string? (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec find_ladders(BeginWord :: unicode:unicode_binary(), EndWord :: unicode:unicode_binary(), WordList :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
find_ladders(BeginWord, EndWord, WordList) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_ladders(begin_word :: String.t, end_word :: String.t, word_list :: [String.t]) :: [String.t]
  def find_ladders(begin_word, end_word, word_list) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLadders(beginWord: String, endWord: String, wordList: ArrayList<String>): ArrayList<String> {

    }
}
```

