# LCR 192. 把字符串转换成整数 (atoi)

## 题目描述

<p>请你来实现一个&nbsp;<code>myAtoi(string s)</code>&nbsp;函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 <code>atoi</code> 函数）。</p>

<p>函数&nbsp;<code>myAtoi(string s)</code> 的算法如下：</p>

<ol>
	<li>读入字符串并丢弃无用的前导空格</li>
	<li>检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。</li>
	<li>读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。</li>
	<li>将前面步骤读入的这些数字转换为整数（即，"123" -&gt; 123， "0032" -&gt; 32）。如果没有读入数字，则整数为 <code>0</code> 。必要时更改符号（从步骤 2 开始）。</li>
	<li>如果整数数超过 32 位有符号整数范围 <code>[−2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>− 1]</code> ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 <code>−2<sup>31</sup></code> 的整数应该被固定为 <code>−2<sup>31</sup></code> ，大于 <code>2<sup>31&nbsp;</sup>− 1</code> 的整数应该被固定为 <code>2<sup>31&nbsp;</sup>− 1</code> 。</li>
	<li>返回整数作为最终结果。</li>
</ol>

<p><strong>注意：</strong></p>

<ul>
	<li>本题中的空白字符只包括空格字符 <code>' '</code> 。</li>
	<li>除前导空格或数字后的其余字符串外，<strong>请勿忽略</strong> 任何其他字符。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "42"
<strong>输出：</strong>42
<strong>解释：</strong>加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
第 1 步："42"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："<u>42</u>"（读入 "42"）
           ^
解析得到整数 42 。
由于 "42" 在范围 [-2<sup>31</sup>, 2<sup>31</sup> - 1] 内，最终结果为 42 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "   -42"
<strong>输出：</strong>-42
<strong>解释：</strong>
第 1 步："<u><strong>   </strong></u>-42"（读入前导空格，但忽视掉）
            ^
第 2 步："   <u><strong>-</strong></u>42"（读入 '-' 字符，所以结果应该是负数）
             ^
第 3 步："   <u><strong>-42</strong></u>"（读入 "42"）
               ^
解析得到整数 -42 。
由于 "-42" 在范围 [-2<sup>31</sup>, 2<sup>31</sup> - 1] 内，最终结果为 -42 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "4193 with words"
<strong>输出：</strong>4193
<strong>解释：</strong>
第 1 步："4193 with words"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："4193 with words"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："<u>4193</u> with words"（读入 "4193"；由于下一个字符不是一个数字，所以读入停止）
             ^
解析得到整数 4193 。
由于 "4193" 在范围 [-2<sup>31</sup>, 2<sup>31</sup> - 1] 内，最终结果为 4193 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 200</code></li>
	<li><code>s</code> 由英文字母（大写和小写）、数字（<code>0-9</code>）、<code>' '</code>、<code>'+'</code>、<code>'-'</code> 和 <code>'.'</code> 组成</li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 8 题相同：<a href="https://leetcode-cn.com/problems/string-to-integer-atoi/">https://leetcode-cn.com/problems/string-to-integer-atoi/</a></p>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 字符串

## 示例

```
"42"
"   -42"
"4193 with words"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int myAtoi(string str) {
        
    }
};
```

### Java

```java
class Solution {
    public int myAtoi(String str) {
        
    }
}
```

### Python

```python
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def myAtoi(self, str: str) -> int:
        
```

### C

```c
int myAtoi(char* str) {
    
}
```

### C#

```csharp
public class Solution {
    public int MyAtoi(string str) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    
};
```

### TypeScript

```typescript
function myAtoi(str: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $str
     * @return Integer
     */
    function myAtoi($str) {
        
    }
}
```

### Swift

```swift
class Solution {
    func myAtoi(_ str: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun myAtoi(str: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int myAtoi(String str) {
    
  }
}
```

### Go

```golang
func myAtoi(str string) int {
    
}
```

### Ruby

```ruby
# @param {String} str
# @return {Integer}
def my_atoi(str)
    
end
```

### Scala

```scala
object Solution {
    def myAtoi(str: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn my_atoi(str: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (my-atoi str)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec my_atoi(Str :: unicode:unicode_binary()) -> integer().
my_atoi(Str) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec my_atoi(str :: String.t) :: integer
  def my_atoi(str) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func myAtoi(str: String): Int64 {

    }
}
```

