# 405. 数字转换为十六进制数

## 题目描述

<p>给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用&nbsp;<a href="https://baike.baidu.com/item/%E8%A1%A5%E7%A0%81/6854613?fr=aladdin">补码运算</a>&nbsp;方法。</p>

<p>答案字符串中的所有字母都应该是小写字符，并且除了 0 本身之外，答案中不应该有任何前置零。</p>

<p><strong>注意: </strong>不允许使用任何由库提供的将数字直接转换或格式化为十六进制的方法来解决这个问题。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>num = 26
<b>输出：</b>"1a"
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>num = -1
<b>输出：</b>"ffffffff"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数学

## 示例

```
26
-1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string toHex(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public String toHex(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def toHex(self, num: int) -> str:
        
```

### C

```c
char* toHex(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public string ToHex(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {string}
 */
var toHex = function(num) {
    
};
```

### TypeScript

```typescript
function toHex(num: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return String
     */
    function toHex($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func toHex(_ num: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun toHex(num: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String toHex(int num) {
    
  }
}
```

### Go

```golang
func toHex(num int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {String}
def to_hex(num)
    
end
```

### Scala

```scala
object Solution {
    def toHex(num: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn to_hex(num: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (to-hex num)
  (-> exact-integer? string?)
  )
```

### Erlang

```erlang
-spec to_hex(Num :: integer()) -> unicode:unicode_binary().
to_hex(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec to_hex(num :: integer) :: String.t
  def to_hex(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func toHex(num: Int64): String {

    }
}
```

