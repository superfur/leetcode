# 3081. 替换字符串中的问号使分数最小

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;。<code>s[i]</code>&nbsp;要么是小写英文字母，要么是问号&nbsp;<code>'?'</code>&nbsp;。</p>

<p>对于长度为 <code>m</code>&nbsp;且 <strong>只</strong>&nbsp;含有小写英文字母的字符串 <code>t</code>&nbsp;，我们定义函数&nbsp;<code>cost(i)</code>&nbsp;为下标 <code>i</code>&nbsp;之前（也就是范围 <code>[0, i - 1]</code>&nbsp;中）出现过与&nbsp;<code>t[i]</code>&nbsp;<strong>相同</strong>&nbsp;字符出现的次数。</p>

<p>字符串 <code>t</code>&nbsp;的&nbsp;<strong>分数</strong>&nbsp;为所有下标&nbsp;<code>i</code>&nbsp;的&nbsp;<code>cost(i)</code>&nbsp;之 <strong>和</strong>&nbsp;。</p>

<p>比方说，字符串&nbsp;<code>t = "aab"</code>&nbsp;：</p>

<ul>
	<li><code>cost(0) = 0</code></li>
	<li><code>cost(1) = 1</code></li>
	<li><code>cost(2) = 0</code></li>
	<li>所以，字符串&nbsp;<code>"aab"</code>&nbsp;的分数为&nbsp;<code>0 + 1 + 0 = 1</code>&nbsp;。</li>
</ul>

<p>你的任务是用小写英文字母&nbsp;<strong>替换</strong> <code>s</code>&nbsp;中 <strong>所有</strong> 问号，使 <code>s</code>&nbsp;的 <strong>分数</strong><strong>最小&nbsp;</strong>。</p>

<p>请你返回替换所有问号<em>&nbsp;</em><code>'?'</code>&nbsp;之后且分数最小的字符串。如果有多个字符串的&nbsp;<strong>分数最小</strong>&nbsp;，那么返回字典序最小的一个。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = "???" </span></p>

<p><strong>输出：</strong>&nbsp;<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">"abc" </span></p>

<p><strong>解释：</strong>这个例子中，我们将 <code>s</code>&nbsp;中的问号&nbsp;<code>'?'</code>&nbsp;替换得到&nbsp;<code>"abc"</code>&nbsp;。</p>

<p>对于字符串&nbsp;<code>"abc"</code>&nbsp;，<code>cost(0) = 0</code>&nbsp;，<code>cost(1) = 0</code>&nbsp;和&nbsp;<code>cost(2) = 0</code>&nbsp;。</p>

<p><code>"abc"</code>&nbsp;的分数为&nbsp;<code>0</code>&nbsp;。</p>

<p>其他修改 <code>s</code>&nbsp;得到分数 <code>0</code>&nbsp;的字符串为&nbsp;<code>"cba"</code>&nbsp;，<code>"abz"</code>&nbsp;和&nbsp;<code>"hey"</code>&nbsp;。</p>

<p>这些字符串中，我们返回字典序最小的。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = "a?a?"</span></p>

<p><strong>输出：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">"abac"</span></p>

<p><strong>解释：</strong>这个例子中，我们将&nbsp;<code>s</code>&nbsp;中的问号&nbsp;<code>'?'</code>&nbsp;替换得到&nbsp;<code>"abac"</code>&nbsp;。</p>

<p>对于字符串&nbsp;<code>"abac"</code>&nbsp;，<code>cost(0) = 0</code>&nbsp;，<code>cost(1) = 0</code>&nbsp;，<code>cost(2) = 1</code>&nbsp;和&nbsp;<code>cost(3) = 0</code>&nbsp;。</p>

<p><code>"abac"</code>&nbsp;的分数为&nbsp;<code>1</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code>&nbsp;要么是小写英文字母，要么是&nbsp;<code>'?'</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 哈希表
- 字符串
- 计数
- 排序
- 堆（优先队列）

## 提示

1. <p>The cost does not depend on the order of characters. If a character <code>c</code> appears <code>x</code> times, the cost is exactly <code>0 + 1 + 2 + … + (x − 1) = x * (x − 1) / 2</code>.</p>
2. <p>We know the total number of question marks; for each one, we should select the letter with the minimum frequency to replace it.</p>
3. <p>The letter selection can be achieved by a min-heap (or even by brute-forcing the <code>26</code> possibilities).</p>
4. <p>So, we know the extra letters we need to replace finally. However, we must put those letters in order from left to right so that the resulting string is the lexicographically smallest one.</p>

## 示例

```
"???"
"a?a?"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string minimizeStringValue(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String minimizeStringValue(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimizeStringValue(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        
```

### C

```c
char* minimizeStringValue(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string MinimizeStringValue(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var minimizeStringValue = function(s) {
    
};
```

### TypeScript

```typescript
function minimizeStringValue(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function minimizeStringValue($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimizeStringValue(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimizeStringValue(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String minimizeStringValue(String s) {
    
  }
}
```

### Go

```golang
func minimizeStringValue(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def minimize_string_value(s)
    
end
```

### Scala

```scala
object Solution {
    def minimizeStringValue(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimize_string_value(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (minimize-string-value s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec minimize_string_value(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
minimize_string_value(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimize_string_value(s :: String.t) :: String.t
  def minimize_string_value(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimizeStringValue(s: String): String {

    }
}
```

