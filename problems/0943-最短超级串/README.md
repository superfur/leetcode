# 943. 最短超级串

## 题目描述

<p>给定一个字符串数组 <code>words</code>，找到以 <code>words</code> 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中 <strong>任意一个</strong> 即可。</p>

<p>我们可以假设 <code>words</code> 中没有字符串是 <code>words</code> 中另一个字符串的子字符串。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = ["alex","loves","leetcode"]
<strong>输出：</strong>"alexlovesleetcode"
<strong>解释：</strong>"alex"，"loves"，"leetcode" 的所有排列都会被接受。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = ["catg","ctaagt","gcta","ttca","atgcatc"]
<strong>输出：</strong>"gctaagttcatgcatc"</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= words.length <= 12</code></li>
	<li><code>1 <= words[i].length <= 20</code></li>
	<li><code>words[i]</code> 由小写英文字母组成</li>
	<li><code>words</code> 中的所有字符串 <strong>互不相同</strong></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 字符串
- 动态规划
- 状态压缩

## 示例

```
["alex","loves","leetcode"]
["catg","ctaagt","gcta","ttca","atgcatc"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string shortestSuperstring(vector<string>& words) {
        
    }
};
```

### Java

```java
class Solution {
    public String shortestSuperstring(String[] words) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestSuperstring(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        
```

### C

```c
char* shortestSuperstring(char** words, int wordsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string ShortestSuperstring(string[] words) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {string}
 */
var shortestSuperstring = function(words) {
    
};
```

### TypeScript

```typescript
function shortestSuperstring(words: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return String
     */
    function shortestSuperstring($words) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestSuperstring(_ words: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestSuperstring(words: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String shortestSuperstring(List<String> words) {
    
  }
}
```

### Go

```golang
func shortestSuperstring(words []string) string {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @return {String}
def shortest_superstring(words)
    
end
```

### Scala

```scala
object Solution {
    def shortestSuperstring(words: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_superstring(words: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-superstring words)
  (-> (listof string?) string?)
  )
```

### Erlang

```erlang
-spec shortest_superstring(Words :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
shortest_superstring(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_superstring(words :: [String.t]) :: String.t
  def shortest_superstring(words) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestSuperstring(words: Array<String>): String {

    }
}
```

