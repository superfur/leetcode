# 2506. 统计相似字符串对的数目

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串数组 <code>words</code> 。</p>

<p>如果两个字符串由相同的字符组成，则认为这两个字符串 <strong>相似</strong> 。</p>

<ul>
	<li>例如，<code>"abca"</code> 和 <code>"cba"</code> 相似，因为它们都由字符 <code>'a'</code>、<code>'b'</code>、<code>'c'</code> 组成。</li>
	<li>然而，<code>"abacba"</code> 和 <code>"bcfd"</code> 不相似，因为它们不是相同字符组成的。</li>
</ul>

<p>请你找出满足字符串&nbsp;<code>words[i]</code><em> </em>和<em> </em><code>words[j]</code> 相似的下标对<em> </em><code>(i, j)</code><em> </em>，并返回下标对的数目，其中 <code>0 &lt;= i &lt; j &lt;= words.length - 1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["aba","aabb","abcd","bac","aabc"]
<strong>输出：</strong>2
<strong>解释：</strong>共有 2 对满足条件：
- i = 0 且 j = 1 ：words[0] 和 words[1] 只由字符 'a' 和 'b' 组成。 
- i = 3 且 j = 4 ：words[3] 和 words[4] 只由字符 'a'、'b' 和 'c' 。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["aabb","ab","ba"]
<strong>输出：</strong>3
<strong>解释：</strong>共有 3 对满足条件：
- i = 0 且 j = 1 ：words[0] 和 words[1] 只由字符 'a' 和 'b' 组成。 
- i = 0 且 j = 2 ：words[0] 和 words[2] 只由字符 'a' 和 'b' 组成。 
- i = 1 且 j = 2 ：words[1] 和 words[2] 只由字符 'a' 和 'b' 组成。 
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = ["nba","cba","dba"]
<strong>输出：</strong>0
<strong>解释：</strong>不存在满足条件的下标对，返回 0 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组
- 哈希表
- 字符串
- 计数

## 提示

1. How can you check if two strings are similar?
2. Use a hashSet to store the character of each string.

## 示例

```
["aba","aabb","abcd","bac","aabc"]
["aabb","ab","ba"]
["nba","cba","dba"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int similarPairs(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int similarPairs(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
```

### C

```c
int similarPairs(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SimilarPairs(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var similarPairs = function(words) {
    
};
```

### TypeScript

```typescript
function similarPairs(words: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function similarPairs($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func similarPairs(_ words: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun similarPairs(words: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int similarPairs(List<String> words) {
    
  }
}
```

### Go

```golang
func similarPairs(words []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def similar_pairs(words)
    
end
```

### Scala

```scala
object Solution {
    def similarPairs(words: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn similar_pairs(words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (similar-pairs words)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec similar_pairs(Words :: [unicode:unicode_binary()]) -> integer().
similar_pairs(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec similar_pairs(words :: [String.t]) :: integer
  def similar_pairs(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func similarPairs(words: Array<String>): Int64 {

    }
}
```

