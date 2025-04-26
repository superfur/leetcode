# 318. 最大单词长度乘积

## 题目描述

<p>给你一个字符串数组&nbsp;<code>words</code> ，找出并返回 <code>length(words[i]) * length(words[j])</code>&nbsp;的最大值，并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 <code>0</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>words = <code>["abcw","baz","foo","bar","xtfn","abcdef"]</code>
<strong>输出：</strong><code>16 
<strong>解释</strong></code><strong>：</strong><code>这两个单词为<strong> </strong>"abcw", "xtfn"</code>。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = <code>["a","ab","abc","d","cd","bcd","abcd"]</code>
<strong>输出：</strong><code>4 
<strong>解释</strong></code><strong>：</strong>这两个单词为 <code>"ab", "cd"</code>。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = <code>["a","aa","aaa","aaaa"]</code>
<strong>输出：</strong><code>0 
<strong>解释</strong></code><strong>：</strong><code>不存在这样的两个单词。</code>
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 1000</code></li>
	<li><code>words[i]</code>&nbsp;仅包含小写字母</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 字符串

## 示例

```
["abcw","baz","foo","bar","xtfn","abcdef"]
["a","ab","abc","d","cd","bcd","abcd"]
["a","aa","aaa","aaaa"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxProduct(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxProduct(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
```

### C

```c
int maxProduct(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxProduct(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var maxProduct = function(words) {
    
};
```

### TypeScript

```typescript
function maxProduct(words: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function maxProduct($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxProduct(_ words: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxProduct(words: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxProduct(List<String> words) {
    
  }
}
```

### Go

```golang
func maxProduct(words []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def max_product(words)
    
end
```

### Scala

```scala
object Solution {
    def maxProduct(words: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_product(words: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-product words)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_product(Words :: [unicode:unicode_binary()]) -> integer().
max_product(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_product(words :: [String.t]) :: integer
  def max_product(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxProduct(words: Array<String>): Int64 {

    }
}
```

