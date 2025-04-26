# 面试题 17.11. 单词距离

## 题目描述

<p>有个内含单词的超大文本文件，给定任意两个<code>不同的</code>单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
<strong>输出：</strong>1</pre>

<p>提示：</p>

<ul>
	<li><code>words.length &lt;= 100000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 字符串

## 提示

1. 如果只运行一次算法，请首先考虑寻找最近距离的算法。你应该能够在 O(N) 时间内完成这项工作，其中 N 是文档中的字数。
2. 调整你的算法，使它成为可以重复调用的算法的一次执行。它哪里慢?你能优化它吗?
3. 你可以构建一个查找表，把每个单词映射到它出现位置的列表。然后怎样找到最近的两个位置呢?
4. 如果你有一个每个单词出现次数的列表，那么你实际上需要在两个数组中寻找一对值(每个数组中选一个值)，使它们之间的差异最小。这应该是一个与初始算法很相似的算法。
5. 能用两个指针遍历两个数组吗?你应该能在 O(A+B)时间内完成，其中 A 和 B 是两个数组的大小。

## 示例

```
["I","am","a","student","from","a","university","in","a","city"]
"a"
"student"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findClosest(vector<string>& words, string word1, string word2) {
        
    }
};
```

### Java

```java
class Solution {
    public int findClosest(String[] words, String word1, String word2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findClosest(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        
```

### C

```c
int findClosest(char** words, int wordsSize, char* word1, char* word2) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindClosest(string[] words, string word1, string word2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var findClosest = function(words, word1, word2) {
    
};
```

### TypeScript

```typescript
function findClosest(words: string[], word1: string, word2: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $word1
     * @param String $word2
     * @return Integer
     */
    function findClosest($words, $word1, $word2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findClosest(_ words: [String], _ word1: String, _ word2: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findClosest(words: Array<String>, word1: String, word2: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findClosest(List<String> words, String word1, String word2) {
    
  }
}
```

### Go

```golang
func findClosest(words []string, word1 string, word2 string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {String} word1
# @param {String} word2
# @return {Integer}
def find_closest(words, word1, word2)
    
end
```

### Scala

```scala
object Solution {
    def findClosest(words: Array[String], word1: String, word2: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_closest(words: Vec<String>, word1: String, word2: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-closest words word1 word2)
  (-> (listof string?) string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_closest(Words :: [unicode:unicode_binary()], Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> integer().
find_closest(Words, Word1, Word2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_closest(words :: [String.t], word1 :: String.t, word2 :: String.t) :: integer
  def find_closest(words, word1, word2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findClosest(words: Array<String>, word1: String, word2: String): Int64 {

    }
}
```

