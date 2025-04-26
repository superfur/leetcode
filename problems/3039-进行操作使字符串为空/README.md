# 3039. 进行操作使字符串为空

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;。</p>

<p>请你进行以下操作直到 <code>s</code>&nbsp;为 <strong>空</strong>&nbsp;：</p>

<ul>
	<li>每次操作 <strong>依次</strong> 遍历 <code>'a'</code> 到 <code>'z'</code>，如果当前字符出现在 <code>s</code> 中，那么删除出现位置&nbsp;<strong>最早</strong>&nbsp;的该字符（如果存在的话）。</li>
</ul>

<p>例如，最初 <code>s = "aabcbbca"</code>。我们执行下述操作：</p>

<ul>
	<li>移除下划线的字符&nbsp; <code>s = "<u><strong>a</strong></u>a<u><strong>bc</strong></u>bbca"</code>。结果字符串为 <code>s = "abbca"</code>。</li>
	<li>移除下划线的字符&nbsp; <code>s = "<u><strong>ab</strong></u>b<u><strong>c</strong></u>a"</code>。结果字符串为 <code>s = "ba"</code>。</li>
	<li>移除下划线的字符&nbsp; <code>s = "<u><strong>ba</strong></u>"</code>。结果字符串为 <code>s = ""</code>。</li>
</ul>

<p>请你返回进行 <strong>最后</strong>&nbsp;一次操作 <strong>之前</strong>&nbsp;的字符串<em>&nbsp;</em><code>s</code><em>&nbsp;</em>。在上面的例子中，答案是&nbsp;<code>"ba"</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>s = "aabcbbca"
<b>输出：</b>"ba"
<b>解释：</b>已经在题目描述中解释。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>s = "abcd"
<b>输出：</b>"abcd"
<b>解释：</b>我们进行以下操作：
- 删除 s = "<em><strong>abcd</strong></em>" 中加粗加斜字符，得到字符串 s = "" 。
进行最后一次操作之前的字符串为 "abcd" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 计数
- 排序

## 提示

1. Before the last operation, only the most frequent characters in the original string will remain.
2. Keep only the last occurence of each of the most frequent characters.

## 示例

```
"aabcbbca"
"abcd"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string lastNonEmptyString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String lastNonEmptyString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lastNonEmptyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        
```

### C

```c
char* lastNonEmptyString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string LastNonEmptyString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var lastNonEmptyString = function(s) {
    
};
```

### TypeScript

```typescript
function lastNonEmptyString(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function lastNonEmptyString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lastNonEmptyString(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lastNonEmptyString(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String lastNonEmptyString(String s) {
    
  }
}
```

### Go

```golang
func lastNonEmptyString(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def last_non_empty_string(s)
    
end
```

### Scala

```scala
object Solution {
    def lastNonEmptyString(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn last_non_empty_string(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (last-non-empty-string s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec last_non_empty_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
last_non_empty_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec last_non_empty_string(s :: String.t) :: String.t
  def last_non_empty_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lastNonEmptyString(s: String): String {

    }
}
```

