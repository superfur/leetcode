# 1092. 最短公共超序列

## 题目描述

<p>给你两个字符串&nbsp;<code>str1</code> 和&nbsp;<code>str2</code>，返回同时以&nbsp;<code>str1</code>&nbsp;和&nbsp;<code>str2</code>&nbsp;作为 <strong>子序列</strong> 的最短字符串。如果答案不止一个，则可以返回满足条件的 <strong>任意一个</strong> 答案。</p>

<p>如果从字符串 <code>t</code> 中删除一些字符（也可能不删除），可以得到字符串 <code>s</code> ，那么 <code>s</code> 就是 t 的一个子序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>str1 = "abac", str2 = "cab"
<strong>输出：</strong>"cabac"
<strong>解释：</strong>
str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。 
str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
最终我们给出的答案是满足上述属性的最短字符串。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>str1 = "aaaaaaaa", str2 = "aaaaaaaa"
<strong>输出：</strong>"aaaaaaaa"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= str1.length, str2.length &lt;= 1000</code></li>
	<li><code>str1</code> 和&nbsp;<code>str2</code>&nbsp;都由小写英文字母组成。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. We can find the length of the longest common subsequence between str1[i:] and str2[j:] (for all (i, j)) by using dynamic programming.
2. We can use this information to recover the shortest common supersequence.

## 示例

```
"abac"
"cab"
"aaaaaaaa"
"aaaaaaaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string shortestCommonSupersequence(string str1, string str2) {
        
    }
};
```

### Java

```java
class Solution {
    public String shortestCommonSupersequence(String str1, String str2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
```

### C

```c
char* shortestCommonSupersequence(char* str1, char* str2) {
    
}
```

### C#

```csharp
public class Solution {
    public string ShortestCommonSupersequence(string str1, string str2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var shortestCommonSupersequence = function(str1, str2) {
    
};
```

### TypeScript

```typescript
function shortestCommonSupersequence(str1: string, str2: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $str1
     * @param String $str2
     * @return String
     */
    function shortestCommonSupersequence($str1, $str2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestCommonSupersequence(_ str1: String, _ str2: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestCommonSupersequence(str1: String, str2: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String shortestCommonSupersequence(String str1, String str2) {
    
  }
}
```

### Go

```golang
func shortestCommonSupersequence(str1 string, str2 string) string {
    
}
```

### Ruby

```ruby
# @param {String} str1
# @param {String} str2
# @return {String}
def shortest_common_supersequence(str1, str2)
    
end
```

### Scala

```scala
object Solution {
    def shortestCommonSupersequence(str1: String, str2: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_common_supersequence(str1: String, str2: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-common-supersequence str1 str2)
  (-> string? string? string?)
  )
```

### Erlang

```erlang
-spec shortest_common_supersequence(Str1 :: unicode:unicode_binary(), Str2 :: unicode:unicode_binary()) -> unicode:unicode_binary().
shortest_common_supersequence(Str1, Str2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_common_supersequence(str1 :: String.t, str2 :: String.t) :: String.t
  def shortest_common_supersequence(str1, str2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestCommonSupersequence(str1: String, str2: String): String {

    }
}
```

