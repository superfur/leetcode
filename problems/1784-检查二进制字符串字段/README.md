# 1784. 检查二进制字符串字段

## 题目描述

<p>给你一个二进制字符串 <code>s</code> ，该字符串 <strong>不含前导零</strong> 。</p>

<p>如果 <code>s</code> 包含 <strong>零个或一个由连续的 <code>'1'</code> 组成的字段</strong> ，返回 <code>true</code>​​​ 。否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "1001"
<strong>输出：</strong>false
<strong>解释：</strong>由连续若干个&nbsp;<code>'1'</code> 组成的字段数量为 2，返回 false
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "110"
<strong>输出：</strong>true</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code>​​​​ 为 <code>'0'</code> 或 <code>'1'</code></li>
	<li><code>s[0]</code> 为 <code>'1'</code></li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. It's guaranteed to have at least one segment
2. The string size is small so you can count all segments of ones with no that have no adjacent ones.

## 示例

```
"1001"
"110"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkOnesSegment(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkOnesSegment(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
```

### C

```c
bool checkOnesSegment(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckOnesSegment(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var checkOnesSegment = function(s) {
    
};
```

### TypeScript

```typescript
function checkOnesSegment(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function checkOnesSegment($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkOnesSegment(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkOnesSegment(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkOnesSegment(String s) {
    
  }
}
```

### Go

```golang
func checkOnesSegment(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def check_ones_segment(s)
    
end
```

### Scala

```scala
object Solution {
    def checkOnesSegment(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_ones_segment(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-ones-segment s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec check_ones_segment(S :: unicode:unicode_binary()) -> boolean().
check_ones_segment(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_ones_segment(s :: String.t) :: boolean
  def check_ones_segment(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkOnesSegment(s: String): Bool {

    }
}
```

