# 1178. 猜字谜

## 题目描述

<p>外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。</p>

<p>字谜的迷面 <code>puzzle</code> 按字符串形式给出，如果一个单词 <code>word</code> 符合下面两个条件，那么它就可以算作谜底：</p>

<ul>
	<li>单词 <code>word</code> 中包含谜面 <code>puzzle</code> 的第一个字母。</li>
	<li>单词 <code>word</code> 中的每一个字母都可以在谜面 <code>puzzle</code> 中找到。<br />
	例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）都不能作为谜底。</li>
</ul>

<p>返回一个答案数组 <code>answer</code>，数组中的每个元素 <code>answer[i]</code> 是在给出的单词列表 <code>words</code> 中可以作为字谜迷面 <code>puzzles[i]</code> 所对应的谜底的单词数目。</p>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
<strong>输出：</strong>[1,1,3,2,4,0]
<strong>解释：</strong>
1 个单词可以作为 "aboveyz" 的谜底 : "aaaa" 
1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= words.length <= 10^5</code></li>
	<li><code>4 <= words[i].length <= 50</code></li>
	<li><code>1 <= puzzles.length <= 10^4</code></li>
	<li><code>puzzles[i].length == 7</code></li>
	<li><code>words[i][j]</code>, <code>puzzles[i][j]</code> 都是小写英文字母。</li>
	<li>每个 <code>puzzles[i]</code> 所包含的字符都不重复。</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 字典树
- 数组
- 哈希表
- 字符串

## 提示

1. Exploit the fact that the length of the puzzle is only 7.
2. Use bit-masks to represent the word and puzzle strings.
3. For each puzzle, count the number of words whose bit-mask is a sub-mask of the puzzle's bit-mask.

## 示例

```
["aaaa","asas","able","ability","actt","actor","access"]
["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
["apple","pleas","please"]
["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> findNumOfValidWords(String[] words, String[] puzzles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findNumOfValidWords(char** words, int wordsSize, char** puzzles, int puzzlesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> FindNumOfValidWords(string[] words, string[] puzzles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {string[]} puzzles
 * @return {number[]}
 */
var findNumOfValidWords = function(words, puzzles) {
    
};
```

### TypeScript

```typescript
function findNumOfValidWords(words: string[], puzzles: string[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String[] $puzzles
     * @return Integer[]
     */
    function findNumOfValidWords($words, $puzzles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findNumOfValidWords(_ words: [String], _ puzzles: [String]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findNumOfValidWords(words: Array<String>, puzzles: Array<String>): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findNumOfValidWords(List<String> words, List<String> puzzles) {
    
  }
}
```

### Go

```golang
func findNumOfValidWords(words []string, puzzles []string) []int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {String[]} puzzles
# @return {Integer[]}
def find_num_of_valid_words(words, puzzles)
    
end
```

### Scala

```scala
object Solution {
    def findNumOfValidWords(words: Array[String], puzzles: Array[String]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_num_of_valid_words(words: Vec<String>, puzzles: Vec<String>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-num-of-valid-words words puzzles)
  (-> (listof string?) (listof string?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_num_of_valid_words(Words :: [unicode:unicode_binary()], Puzzles :: [unicode:unicode_binary()]) -> [integer()].
find_num_of_valid_words(Words, Puzzles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_num_of_valid_words(words :: [String.t], puzzles :: [String.t]) :: [integer]
  def find_num_of_valid_words(words, puzzles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findNumOfValidWords(words: Array<String>, puzzles: Array<String>): ArrayList<Int64> {

    }
}
```

