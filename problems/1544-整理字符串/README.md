# 1544. 整理字符串

## 题目描述

<p>给你一个由大小写英文字母组成的字符串 <code>s</code> 。</p>

<p>一个整理好的字符串中，两个相邻字符 <code>s[i]</code> 和 <code>s[i+1]</code>，其中 <code>0<= i <= s.length-2</code> ，要满足如下条件:</p>

<ul>
	<li>若 <code>s[i]</code> 是小写字符，则 <code>s[i+1]</code> 不可以是相同的大写字符。</li>
	<li>若 <code>s[i]</code> 是大写字符，则 <code>s[i+1]</code> 不可以是相同的小写字符。</li>
</ul>

<p>请你将字符串整理好，每次你都可以从字符串中选出满足上述条件的 <strong>两个相邻</strong> 字符并删除，直到字符串整理好为止。</p>

<p>请返回整理好的 <strong>字符串</strong> 。题目保证在给出的约束条件下，测试样例对应的答案是唯一的。</p>

<p><strong>注意：</strong>空字符串也属于整理好的字符串，尽管其中没有任何字符。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "leEeetcode"
<strong>输出：</strong>"leetcode"
<strong>解释：</strong>无论你第一次选的是 i = 1 还是 i = 2，都会使 "leEeetcode" 缩减为 "leetcode" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abBAcC"
<strong>输出：</strong>""
<strong>解释：</strong>存在多种不同情况，但所有的情况都会导致相同的结果。例如：
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "s"
<strong>输出：</strong>"s"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 100</code></li>
	<li><code>s</code> 只包含小写和大写英文字母</li>
</ul>


## 难度

Easy

## 标签

- 栈
- 字符串

## 提示

1. The order you choose 2 characters to remove doesn't matter.
2. Keep applying the mentioned step to s till the length of the string is not changed.

## 示例

```
"leEeetcode"
"abBAcC"
"s"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string makeGood(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String makeGood(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def makeGood(self, s: str) -> str:
        
```

### C

```c
char* makeGood(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string MakeGood(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var makeGood = function(s) {
    
};
```

### TypeScript

```typescript
function makeGood(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function makeGood($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeGood(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeGood(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String makeGood(String s) {
    
  }
}
```

### Go

```golang
func makeGood(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def make_good(s)
    
end
```

### Scala

```scala
object Solution {
    def makeGood(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_good(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (make-good s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec make_good(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
make_good(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_good(s :: String.t) :: String.t
  def make_good(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeGood(s: String): String {

    }
}
```

