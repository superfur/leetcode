# 2129. 将标题首字母大写

## 题目描述

<p>给你一个字符串&nbsp;<code>title</code>&nbsp;，它由单个空格连接一个或多个单词组成，每个单词都只包含英文字母。请你按以下规则将每个单词的首字母 <strong>大写</strong>&nbsp;：</p>

<ul>
	<li>如果单词的长度为&nbsp;<code>1</code>&nbsp;或者&nbsp;<code>2</code>&nbsp;，所有字母变成小写。</li>
	<li>否则，将单词首字母大写，剩余字母变成小写。</li>
</ul>

<p>请你返回 <strong>大写后</strong>&nbsp;的<em>&nbsp;</em><code>title</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<pre><b>输入：</b>title = "capiTalIze tHe titLe"
<b>输出：</b>"Capitalize The Title"
<strong>解释：</strong>
由于所有单词的长度都至少为 3 ，将每个单词首字母大写，剩余字母变为小写。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>title = "First leTTeR of EACH Word"
<b>输出：</b>"First Letter of Each Word"
<strong>解释：</strong>
单词 "of" 长度为 2 ，所以它保持完全小写。
其他单词长度都至少为 3 ，所以其他单词首字母大写，剩余字母小写。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>title = "i lOve leetcode"
<b>输出：</b>"i Love Leetcode"
<strong>解释：</strong>
单词 "i" 长度为 1 ，所以它保留小写。
其他单词长度都至少为 3 ，所以其他单词首字母大写，剩余字母小写。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= title.length &lt;= 100</code></li>
	<li><code>title</code>&nbsp;由单个空格隔开的单词组成，且不含有任何前导或后缀空格。</li>
	<li>每个单词由大写和小写英文字母组成，且都是 <strong>非空</strong>&nbsp;的。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Firstly, try to find all the words present in the string.
2. On the basis of each word's lengths, simulate the process explained in Problem.

## 示例

```
"capiTalIze tHe titLe"
"First leTTeR of EACH Word"
"i lOve leetcode"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string capitalizeTitle(string title) {
        
    }
};
```

### Java

```java
class Solution {
    public String capitalizeTitle(String title) {
        
    }
}
```

### Python

```python
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
```

### C

```c
char* capitalizeTitle(char* title) {
    
}
```

### C#

```csharp
public class Solution {
    public string CapitalizeTitle(string title) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} title
 * @return {string}
 */
var capitalizeTitle = function(title) {
    
};
```

### TypeScript

```typescript
function capitalizeTitle(title: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $title
     * @return String
     */
    function capitalizeTitle($title) {
        
    }
}
```

### Swift

```swift
class Solution {
    func capitalizeTitle(_ title: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun capitalizeTitle(title: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String capitalizeTitle(String title) {
    
  }
}
```

### Go

```golang
func capitalizeTitle(title string) string {
    
}
```

### Ruby

```ruby
# @param {String} title
# @return {String}
def capitalize_title(title)
    
end
```

### Scala

```scala
object Solution {
    def capitalizeTitle(title: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn capitalize_title(title: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (capitalize-title title)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec capitalize_title(Title :: unicode:unicode_binary()) -> unicode:unicode_binary().
capitalize_title(Title) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec capitalize_title(title :: String.t) :: String.t
  def capitalize_title(title) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func capitalizeTitle(title: String): String {

    }
}
```

