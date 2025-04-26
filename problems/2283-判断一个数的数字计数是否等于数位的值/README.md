# 2283. 判断一个数的数字计数是否等于数位的值

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>n</code>&nbsp;的字符串&nbsp;<code>num</code>&nbsp;，它只包含数字。</p>

<p>如果对于 <strong>每个</strong><em>&nbsp;</em><code>0 &lt;= i &lt; n</code>&nbsp;的下标&nbsp;<code>i</code>&nbsp;，都满足数位<em>&nbsp;</em><code>i</code>&nbsp;在 <code>num</code>&nbsp;中出现了&nbsp;<code>num[i]</code>次，那么请你返回&nbsp;<code>true</code>&nbsp;，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>num = "1210"
<b>输出：</b>true
<strong>解释：</strong>
num[0] = '1' 。数字 0 在 num 中出现了一次。
num[1] = '2' 。数字 1 在 num 中出现了两次。
num[2] = '1' 。数字 2 在 num 中出现了一次。
num[3] = '0' 。数字 3 在 num 中出现了零次。
"1210" 满足题目要求条件，所以返回 true 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>num = "030"
<b>输出：</b>false
<strong>解释：</strong>
num[0] = '0' 。数字 0 应该出现 0 次，但是在 num 中出现了两次。
num[1] = '3' 。数字 1 应该出现 3 次，但是在 num 中出现了零次。
num[2] = '0' 。数字 2 在 num 中出现了 0 次。
下标 0 和 1 都违反了题目要求，所以返回 false 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == num.length</code></li>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>num</code>&nbsp;只包含数字。</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Count the frequency of each digit in num.

## 示例

```
"1210"
"030"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool digitCount(string num) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean digitCount(String num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def digitCount(self, num: str) -> bool:
        
```

### C

```c
bool digitCount(char* num) {
    
}
```

### C#

```csharp
public class Solution {
    public bool DigitCount(string num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @return {boolean}
 */
var digitCount = function(num) {
    
};
```

### TypeScript

```typescript
function digitCount(num: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @return Boolean
     */
    function digitCount($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func digitCount(_ num: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun digitCount(num: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool digitCount(String num) {
    
  }
}
```

### Go

```golang
func digitCount(num string) bool {
    
}
```

### Ruby

```ruby
# @param {String} num
# @return {Boolean}
def digit_count(num)
    
end
```

### Scala

```scala
object Solution {
    def digitCount(num: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn digit_count(num: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (digit-count num)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec digit_count(Num :: unicode:unicode_binary()) -> boolean().
digit_count(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec digit_count(num :: String.t) :: boolean
  def digit_count(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func digitCount(num: String): Bool {

    }
}
```

