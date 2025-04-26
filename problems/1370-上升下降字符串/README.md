# 1370. 上升下降字符串

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，请你根据下面的算法重新构造字符串：</p>

<ol>
	<li>从 <code>s</code>&nbsp;中选出 <strong>最小</strong>&nbsp;的字符，将它 <strong>接在</strong>&nbsp;结果字符串的后面。</li>
	<li>从 <code>s</code> 剩余字符中选出比上一个添加字符更大的 <strong>最小</strong> 字符，将它 <strong>接在</strong>&nbsp;结果字符串后面。</li>
	<li>重复步骤 2 ，直到你没法从 <code>s</code>&nbsp;中选择字符。</li>
	<li>从 <code>s</code>&nbsp;中选出 <strong>最大</strong>&nbsp;的字符，将它 <strong>接在</strong>&nbsp;结果字符串的后面。</li>
	<li>从 <code>s</code> 剩余字符中选出比上一个添加字符更小的 <strong>最大</strong>&nbsp;字符，将它 <strong>接在</strong>&nbsp;结果字符串后面。</li>
	<li>重复步骤 5&nbsp;，直到你没法从 <code>s</code>&nbsp;中选择字符。</li>
	<li>重复步骤 1 到 6 ，直到 <code>s</code>&nbsp;中所有字符都已经被选过。</li>
</ol>

<p>在任何一步中，如果最小或者最大字符不止一个&nbsp;，你可以选择其中任意一个，并将其添加到结果字符串。</p>

<p>请你返回将&nbsp;<code>s</code>&nbsp;中字符重新排序后的 <strong>结果字符串</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aaaabbbbcccc"
<strong>输出：</strong>"abccbaabccba"
<strong>解释：</strong>第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "rat"
<strong>输出：</strong>"art"
<strong>解释：</strong>单词 "rat" 在上述算法重排序以后变成 "art"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Count the frequency of each character.
2. Loop over all character from 'a' to 'z' and append the character if it exists and decrease frequency by 1. Do the same from 'z' to 'a'.
3. Keep repeating until the frequency of all characters is zero.

## 示例

```
"aaaabbbbcccc"
"rat"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string sortString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String sortString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def sortString(self, s: str) -> str:
        
```

### C

```c
char* sortString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string SortString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var sortString = function(s) {
    
};
```

### TypeScript

```typescript
function sortString(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function sortString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sortString(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sortString(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String sortString(String s) {
    
  }
}
```

### Go

```golang
func sortString(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def sort_string(s)
    
end
```

### Scala

```scala
object Solution {
    def sortString(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sort_string(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (sort-string s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec sort_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
sort_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sort_string(s :: String.t) :: String.t
  def sort_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sortString(s: String): String {

    }
}
```

