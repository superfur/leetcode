# 2264. 字符串中最大的 3 位相同数字

## 题目描述

<p>给你一个字符串 <code>num</code> ，表示一个大整数。如果一个整数满足下述所有条件，则认为该整数是一个 <strong>优质整数</strong> ：</p>

<ul>
	<li>该整数是 <code>num</code> 的一个长度为 <code>3</code> 的 <strong>子字符串</strong> 。</li>
	<li>该整数由唯一一个数字重复 <code>3</code> 次组成。</li>
</ul>

<p>以字符串形式返回 <strong>最大的优质整数</strong> 。如果不存在满足要求的整数，则返回一个空字符串 <code>""</code> 。</p>

<p><strong>注意：</strong></p>

<ul>
	<li><strong>子字符串</strong> 是字符串中的一个连续字符序列。</li>
	<li><code>num</code> 或优质整数中可能存在 <strong>前导零</strong> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = "6<em><strong>777</strong></em>133339"
<strong>输出：</strong>"777"
<strong>解释：</strong>num 中存在两个优质整数："777" 和 "333" 。
"777" 是最大的那个，所以返回 "777" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = "23<em><strong>000</strong></em>19"
<strong>输出：</strong>"000"
<strong>解释：</strong>"000" 是唯一一个优质整数。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>num = "42352338"
<strong>输出：</strong>""
<strong>解释：</strong>不存在长度为 3 且仅由一个唯一数字组成的整数。因此，不存在优质整数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= num.length &lt;= 1000</code></li>
	<li><code>num</code> 仅由数字（<code>0</code> - <code>9</code>）组成</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. We can sequentially check if “999”, “888”, “777”, … , “000” exists in num in that order. The first to be found is the maximum good integer.
2. If we cannot find any of the above integers, we return an empty string “”.

## 示例

```
"6777133339"
"2300019"
"42352338"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string largestGoodInteger(string num) {
        
    }
};
```

### Java

```java
class Solution {
    public String largestGoodInteger(String num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
```

### C

```c
char* largestGoodInteger(char* num) {
    
}
```

### C#

```csharp
public class Solution {
    public string LargestGoodInteger(string num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function(num) {
    
};
```

### TypeScript

```typescript
function largestGoodInteger(num: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @return String
     */
    function largestGoodInteger($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestGoodInteger(_ num: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestGoodInteger(num: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String largestGoodInteger(String num) {
    
  }
}
```

### Go

```golang
func largestGoodInteger(num string) string {
    
}
```

### Ruby

```ruby
# @param {String} num
# @return {String}
def largest_good_integer(num)
    
end
```

### Scala

```scala
object Solution {
    def largestGoodInteger(num: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_good_integer(num: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (largest-good-integer num)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec largest_good_integer(Num :: unicode:unicode_binary()) -> unicode:unicode_binary().
largest_good_integer(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_good_integer(num :: String.t) :: String.t
  def largest_good_integer(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestGoodInteger(num: String): String {

    }
}
```

