# 3110. 字符串的分数

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;。一个字符串的&nbsp;<strong>分数</strong>&nbsp;定义为相邻字符 <strong>ASCII</strong>&nbsp;码差值绝对值的和。</p>

<p>请你返回 <code>s</code>&nbsp;的 <strong>分数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "hello"</span></p>

<p><span class="example-io"><b>输出：</b>13</span></p>

<p><strong>解释：</strong></p>

<p><code>s</code>&nbsp;中字符的 <strong>ASCII </strong>码分别为：<code>'h' = 104</code>&nbsp;，<code>'e' = 101</code>&nbsp;，<code>'l' = 108</code>&nbsp;，<code>'o' = 111</code>&nbsp;。所以&nbsp;<code>s</code>&nbsp;的分数为&nbsp;<code>|104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "zaz"</span></p>

<p><span class="example-io"><b>输出：</b>50</span></p>

<p><strong>解释：</strong></p>

<p><code>s</code>&nbsp;中字符的 <strong>ASCII&nbsp;</strong>码分别为：<code>'z' = 122</code>&nbsp;，<code>'a' = 97</code>&nbsp;。所以&nbsp;<code>s</code>&nbsp;的分数为&nbsp;<code>|122 - 97| + |97 - 122| = 25 + 25 = 50</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Sum the difference between all the adjacent characters by just taking the absolute difference of their ASCII values.

## 示例

```
"hello"
"zaz"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int scoreOfString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int scoreOfString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def scoreOfString(self, s: str) -> int:
        
```

### C

```c
int scoreOfString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int ScoreOfString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    
};
```

### TypeScript

```typescript
function scoreOfString(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function scoreOfString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func scoreOfString(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun scoreOfString(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int scoreOfString(String s) {
    
  }
}
```

### Go

```golang
func scoreOfString(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def score_of_string(s)
    
end
```

### Scala

```scala
object Solution {
    def scoreOfString(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (score-of-string s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec score_of_string(S :: unicode:unicode_binary()) -> integer().
score_of_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec score_of_string(s :: String.t) :: integer
  def score_of_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func scoreOfString(s: String): Int64 {

    }
}
```

