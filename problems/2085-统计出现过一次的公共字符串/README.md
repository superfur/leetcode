# 2085. 统计出现过一次的公共字符串

## 题目描述

<p>给你两个字符串数组&nbsp;<code>words1</code>&nbsp;和&nbsp;<code>words2</code>&nbsp;，请你返回在两个字符串数组中 <strong>都恰好出现一次</strong>&nbsp;的字符串的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
<b>输出：</b>2
<strong>解释：</strong>
- "leetcode" 在两个数组中都恰好出现一次，计入答案。
- "amazing" 在两个数组中都恰好出现一次，计入答案。
- "is" 在两个数组中都出现过，但在 words1 中出现了 2 次，不计入答案。
- "as" 在 words1 中出现了一次，但是在 words2 中没有出现过，不计入答案。
所以，有 2 个字符串在两个数组中都恰好出现了一次。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
<b>输出：</b>0
<b>解释：</b>没有字符串在两个数组中都恰好出现一次。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>words1 = ["a","ab"], words2 = ["a","a","a","ab"]
<b>输出：</b>1
<b>解释：</b>唯一在两个数组中都出现一次的字符串是 "ab" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words1.length, words2.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words1[i].length, words2[j].length &lt;= 30</code></li>
	<li><code>words1[i]</code> 和&nbsp;<code>words2[j]</code>&nbsp;都只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串
- 计数

## 提示

1. Could you try every word?
2. Could you use a hash map to achieve a good complexity?

## 示例

```
["leetcode","is","amazing","as","is"]
["amazing","leetcode","is"]
["b","bb","bbb"]
["a","aa","aaa"]
["a","ab"]
["a","a","a","ab"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        
    }
};
```

### Java

```java
class Solution {
    public int countWords(String[] words1, String[] words2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
```

### C

```c
int countWords(char** words1, int words1Size, char** words2, int words2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountWords(string[] words1, string[] words2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words1
 * @param {string[]} words2
 * @return {number}
 */
var countWords = function(words1, words2) {
    
};
```

### TypeScript

```typescript
function countWords(words1: string[], words2: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words1
     * @param String[] $words2
     * @return Integer
     */
    function countWords($words1, $words2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countWords(_ words1: [String], _ words2: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countWords(words1: Array<String>, words2: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countWords(List<String> words1, List<String> words2) {
    
  }
}
```

### Go

```golang
func countWords(words1 []string, words2 []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words1
# @param {String[]} words2
# @return {Integer}
def count_words(words1, words2)
    
end
```

### Scala

```scala
object Solution {
    def countWords(words1: Array[String], words2: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_words(words1: Vec<String>, words2: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-words words1 words2)
  (-> (listof string?) (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_words(Words1 :: [unicode:unicode_binary()], Words2 :: [unicode:unicode_binary()]) -> integer().
count_words(Words1, Words2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_words(words1 :: [String.t], words2 :: [String.t]) :: integer
  def count_words(words1, words2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countWords(words1: Array<String>, words2: Array<String>): Int64 {

    }
}
```

