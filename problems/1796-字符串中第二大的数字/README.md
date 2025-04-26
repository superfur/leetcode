# 1796. 字符串中第二大的数字

## 题目描述

<p>给你一个混合字符串 <code>s</code> ，请你返回 <code>s</code> 中 <strong>第二大 </strong>的数字，如果不存在第二大的数字，请你返回 <code>-1</code> 。</p>

<p><strong>混合字符串 </strong>由小写英文字母和数字组成。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "dfa12321afd"
<b>输出：</b>2
<b>解释：</b>出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "abc1111"
<b>输出：</b>-1
<b>解释：</b>出现在 s 中的数字只包含 [1] 。没有第二大的数字。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 500</code></li>
	<li><code>s</code> 只包含小写英文字母和（或）数字。</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. First of all, get the distinct characters since we are only interested in those
2. Let's note that there might not be any digits.

## 示例

```
"dfa12321afd"
"abc1111"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int secondHighest(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int secondHighest(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def secondHighest(self, s: str) -> int:
        
```

### C

```c
int secondHighest(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int SecondHighest(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var secondHighest = function(s) {
    
};
```

### TypeScript

```typescript
function secondHighest(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function secondHighest($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func secondHighest(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun secondHighest(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int secondHighest(String s) {
    
  }
}
```

### Go

```golang
func secondHighest(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def second_highest(s)
    
end
```

### Scala

```scala
object Solution {
    def secondHighest(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn second_highest(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (second-highest s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec second_highest(S :: unicode:unicode_binary()) -> integer().
second_highest(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec second_highest(s :: String.t) :: integer
  def second_highest(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func secondHighest(s: String): Int64 {

    }
}
```

