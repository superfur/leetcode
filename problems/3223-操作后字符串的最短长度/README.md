# 3223. 操作后字符串的最短长度

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;。</p>

<p>你需要对 <code>s</code>&nbsp;执行以下操作 <strong>任意</strong>&nbsp;次：</p>

<ul>
	<li>选择一个下标 <code>i</code>&nbsp;，满足 <code>s[i]</code>&nbsp;左边和右边都&nbsp;<strong>至少</strong>&nbsp;有一个字符与它相同。</li>
	<li>删除 <code>i</code>&nbsp;<strong>左边</strong>&nbsp;离它 <strong>最近</strong>&nbsp;的&nbsp;<code>s[i]</code> 字符。</li>
	<li>删除 <code>i</code>&nbsp;<strong>右边</strong>&nbsp;离它 <strong>最近</strong>&nbsp;的&nbsp;<code>s[i]</code> 字符。</li>
</ul>

<p>请你返回执行完所有操作后， <code>s</code>&nbsp;的 <strong>最短</strong>&nbsp;长度。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "abaacbcbb"</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><strong>解释：</strong><br />
我们执行以下操作：</p>

<ul>
	<li>选择下标 2 ，然后删除下标 0 和 3 处的字符，得到&nbsp;<code>s = "bacbcbb"</code>&nbsp;。</li>
	<li>选择下标 3 ，然后删除下标 0 和 5 处的字符，得到&nbsp;<code>s = "acbcb"</code>&nbsp;。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "aa"</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong><br />
无法对字符串进行任何操作，所以返回初始字符串的长度。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Only the frequency of each character matters in finding the final answer.
2. If a character occurs less than 3 times, we cannot perform any process with it.
3. Suppose there is a character that occurs at least 3 times in the string, we can repeatedly delete two of these characters until there are at most 2 occurrences left of it.

## 示例

```
"abaacbcbb"
"aa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumLength(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumLength(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumLength(self, s: str) -> int:
        
```

### C

```c
int minimumLength(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumLength(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumLength = function(s) {
    
};
```

### TypeScript

```typescript
function minimumLength(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumLength($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumLength(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumLength(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumLength(String s) {
    
  }
}
```

### Go

```golang
func minimumLength(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def minimum_length(s)
    
end
```

### Scala

```scala
object Solution {
    def minimumLength(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-length s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_length(S :: unicode:unicode_binary()) -> integer().
minimum_length(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_length(s :: String.t) :: integer
  def minimum_length(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumLength(s: String): Int64 {

    }
}
```

