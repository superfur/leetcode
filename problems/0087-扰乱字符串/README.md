# 87. 扰乱字符串

## 题目描述

使用下面描述的算法可以扰乱字符串 <code>s</code> 得到字符串 <code>t</code> ：
<ol>
	<li>如果字符串的长度为 1 ，算法停止</li>
	<li>如果字符串的长度 > 1 ，执行下述步骤：
	<ul>
		<li>在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 <code>s</code> ，则可以将其分成两个子字符串 <code>x</code> 和 <code>y</code> ，且满足 <code>s = x + y</code> 。</li>
		<li><strong>随机</strong> 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，<code>s</code> 可能是 <code>s = x + y</code> 或者 <code>s = y + x</code> 。</li>
		<li>在 <code>x</code> 和 <code>y</code> 这两个子字符串上继续从步骤 1 开始递归执行此算法。</li>
	</ul>
	</li>
</ol>

<p>给你两个 <strong>长度相等</strong> 的字符串 <code>s1</code><em> </em>和 <code>s2</code>，判断 <code>s2</code><em> </em>是否是 <code>s1</code><em> </em>的扰乱字符串。如果是，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s1 = "great", s2 = "rgeat"
<strong>输出：</strong>true
<strong>解释：</strong>s1 上可能发生的一种情形是：
"great" --> "gr/eat" // 在一个随机下标处分割得到两个子字符串
"gr/eat" --> "gr/eat" // 随机决定：「保持这两个子字符串的顺序不变」
"gr/eat" --> "g/r / e/at" // 在子字符串上递归执行此算法。两个子字符串分别在随机下标处进行一轮分割
"g/r / e/at" --> "r/g / e/at" // 随机决定：第一组「交换两个子字符串」，第二组「保持这两个子字符串的顺序不变」
"r/g / e/at" --> "r/g / e/ a/t" // 继续递归执行此算法，将 "at" 分割得到 "a/t"
"r/g / e/ a/t" --> "r/g / e/ a/t" // 随机决定：「保持这两个子字符串的顺序不变」
算法终止，结果字符串和 s2 相同，都是 "rgeat"
这是一种能够扰乱 s1 得到 s2 的情形，可以认为 s2 是 s1 的扰乱字符串，返回 true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s1 = "abcde", s2 = "caebd"
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s1 = "a", s2 = "a"
<strong>输出：</strong>true
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>s1.length == s2.length</code></li>
	<li><code>1 <= s1.length <= 30</code></li>
	<li><code>s1</code> 和 <code>s2</code> 由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 示例

```
"great"
"rgeat"
"abcde"
"caebd"
"a"
"a"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isScramble(string s1, string s2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isScramble(String s1, String s2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
```

### C

```c
bool isScramble(char* s1, char* s2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsScramble(string s1, string s2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var isScramble = function(s1, s2) {
    
};
```

### TypeScript

```typescript
function isScramble(s1: string, s2: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function isScramble($s1, $s2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isScramble(_ s1: String, _ s2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isScramble(s1: String, s2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isScramble(String s1, String s2) {
    
  }
}
```

### Go

```golang
func isScramble(s1 string, s2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @return {Boolean}
def is_scramble(s1, s2)
    
end
```

### Scala

```scala
object Solution {
    def isScramble(s1: String, s2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_scramble(s1: String, s2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-scramble s1 s2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec is_scramble(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
is_scramble(S1, S2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_scramble(s1 :: String.t, s2 :: String.t) :: boolean
  def is_scramble(s1, s2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isScramble(s1: String, s2: String): Bool {

    }
}
```

