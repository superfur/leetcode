# 1221. 分割平衡字符串

## 题目描述

<p><strong>平衡字符串</strong> 中，<code>'L'</code> 和 <code>'R'</code> 字符的数量是相同的。</p>

<p>给你一个平衡字符串&nbsp;<code>s</code>，请你将它分割成尽可能多的子字符串，并满足：</p>

<ul>
	<li>每个子字符串都是平衡字符串。</li>
</ul>

<p>返回可以通过分割得到的平衡字符串的 <strong>最大数量</strong> <strong>。</strong></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "RLRRLLRLRL"
<strong>输出：</strong>4
<strong>解释：</strong>s 可以分割为 "RL"、"RRLL"、"RL"、"RL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "RLRRRLLRLL"
<strong>输出：</strong>2
<strong>解释：</strong>s 可以分割为 "RL"、"RRRLLRLL"，每个子字符串中都包含相同数量的 'L' 和 'R' 。
注意，s 无法分割为 "RL"、"RR"、"RL"、"LR"、"LL" 因为第 2 个和第 5 个子字符串不是平衡字符串。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "LLLLRRRR"
<strong>输出：</strong>1
<strong>解释：</strong>s 只能保持原样 "LLLLRRRR" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i] = 'L' 或 'R'</code></li>
	<li><code>s</code> 是一个 <strong>平衡</strong> 字符串</li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 字符串
- 计数

## 提示

1. Loop from left to right maintaining a balance variable when it gets an L increase it by one otherwise decrease it by one.
2. Whenever the balance variable reaches zero then we increase the answer by one.

## 示例

```
"RLRRLLRLRL"
"RLRRRLLRLL"
"LLLLRRRR"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int balancedStringSplit(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int balancedStringSplit(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
```

### C

```c
int balancedStringSplit(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int BalancedStringSplit(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    
};
```

### TypeScript

```typescript
function balancedStringSplit(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function balancedStringSplit($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func balancedStringSplit(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun balancedStringSplit(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int balancedStringSplit(String s) {
    
  }
}
```

### Go

```golang
func balancedStringSplit(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def balanced_string_split(s)
    
end
```

### Scala

```scala
object Solution {
    def balancedStringSplit(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn balanced_string_split(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (balanced-string-split s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec balanced_string_split(S :: unicode:unicode_binary()) -> integer().
balanced_string_split(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec balanced_string_split(s :: String.t) :: integer
  def balanced_string_split(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func balancedStringSplit(s: String): Int64 {

    }
}
```

