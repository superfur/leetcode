# 3170. 删除星号以后字典序最小的字符串

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;。它可能包含任意数量的&nbsp;<code>'*'</code>&nbsp;字符。你的任务是删除所有的&nbsp;<code>'*'</code>&nbsp;字符。</p>

<p>当字符串还存在至少一个&nbsp;<code>'*'</code>&nbsp;字符时，你可以执行以下操作：</p>

<ul>
	<li>删除最左边的&nbsp;<code>'*'</code>&nbsp;字符，同时删除该星号字符左边一个字典序 <strong>最小</strong>&nbsp;的字符。如果有多个字典序最小的字符，你可以删除它们中的任意一个。</li>
</ul>

<p>请你返回删除所有&nbsp;<code>'*'</code>&nbsp;字符以后，剩余字符连接而成的 <span data-keyword="lexicographically-smaller-string">字典序最小</span> 的字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "aaba*"</span></p>

<p><span class="example-io"><b>输出：</b>"aab"</span></p>

<p><strong>解释：</strong></p>

<p>删除 <code>'*'</code>&nbsp;号和它左边的其中一个&nbsp;<code>'a'</code>&nbsp;字符。如果我们选择删除&nbsp;<code>s[3]</code>&nbsp;，<code>s</code>&nbsp;字典序最小。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "abc"</span></p>

<p><span class="example-io"><b>输出：</b>"abc"</span></p>

<p><strong>解释：</strong></p>

<p>字符串中没有&nbsp;<code>'*'</code>&nbsp;字符。<!-- notionvc: ff07e34f-b1d6-41fb-9f83-5d0ba3c1ecde --></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;只含有小写英文字母和&nbsp;<code>'*'</code>&nbsp;字符。</li>
	<li>输入保证操作可以删除所有的&nbsp;<code>'*'</code>&nbsp;字符。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 哈希表
- 字符串
- 堆（优先队列）

## 示例

```
"aaba*"
"abc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string clearStars(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String clearStars(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def clearStars(self, s: str) -> str:
        
```

### C

```c
char* clearStars(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string ClearStars(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var clearStars = function(s) {
    
};
```

### TypeScript

```typescript
function clearStars(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function clearStars($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func clearStars(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun clearStars(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String clearStars(String s) {
    
  }
}
```

### Go

```golang
func clearStars(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def clear_stars(s)
    
end
```

### Scala

```scala
object Solution {
    def clearStars(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn clear_stars(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (clear-stars s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec clear_stars(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
clear_stars(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec clear_stars(s :: String.t) :: String.t
  def clear_stars(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func clearStars(s: String): String {

    }
}
```

