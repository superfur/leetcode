# 2516. 每种字符至少取 K 个

## 题目描述

<p>给你一个由字符 <code>'a'</code>、<code>'b'</code>、<code>'c'</code> 组成的字符串 <code>s</code> 和一个非负整数 <code>k</code> 。每分钟，你可以选择取走 <code>s</code> <strong>最左侧</strong> 还是 <strong>最右侧</strong> 的那个字符。</p>

<p>你必须取走每种字符 <strong>至少</strong> <code>k</code> 个，返回需要的 <strong>最少</strong> 分钟数；如果无法取到，则返回<em> </em><code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aabaaaacaabc", k = 2
<strong>输出：</strong>8
<strong>解释：</strong>
从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
共需要 3 + 5 = 8 分钟。
可以证明需要的最少分钟数是 8 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "a", k = 1
<strong>输出：</strong>-1
<strong>解释：</strong>无法取到一个字符 'b' 或者 'c'，所以返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由字母 <code>'a'</code>、<code>'b'</code>、<code>'c'</code> 组成</li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 提示

1. Start by counting the frequency of each character and checking if it is possible.
2. If you take x characters from the left side, what is the minimum number of characters you need to take from the right side? Find this for all values of x in the range 0 ≤ x ≤ s.length.
3. Use a two-pointers approach to avoid computing the same information multiple times.

## 示例

```
"aabaaaacaabc"
2
"a"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int takeCharacters(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int takeCharacters(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
```

### C

```c
int takeCharacters(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int TakeCharacters(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var takeCharacters = function(s, k) {
    
};
```

### TypeScript

```typescript
function takeCharacters(s: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function takeCharacters($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func takeCharacters(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun takeCharacters(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int takeCharacters(String s, int k) {
    
  }
}
```

### Go

```golang
func takeCharacters(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def take_characters(s, k)
    
end
```

### Scala

```scala
object Solution {
    def takeCharacters(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn take_characters(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (take-characters s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec take_characters(S :: unicode:unicode_binary(), K :: integer()) -> integer().
take_characters(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec take_characters(s :: String.t, k :: integer) :: integer
  def take_characters(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func takeCharacters(s: String, k: Int64): Int64 {

    }
}
```

