# 8. 字符串转换整数 (atoi)

## 题目描述

<p>请你来实现一个&nbsp;<code>myAtoi(string s)</code>&nbsp;函数，使其能将字符串转换成一个 32 位有符号整数。</p>

<p>函数&nbsp;<code>myAtoi(string s)</code> 的算法如下：</p>

<ol>
	<li><strong>空格：</strong>读入字符串并丢弃无用的前导空格（<code>" "</code>）</li>
	<li><strong>符号：</strong>检查下一个字符（假设还未到字符末尾）为&nbsp;<code>'-'</code> 还是 <code>'+'</code>。如果两者都不存在，则假定结果为正。</li>
	<li><strong>转换：</strong>通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾。如果没有读取数字，则结果为0。</li>
	<li><b>舍入：</b>如果整数数超过 32 位有符号整数范围 <code>[−2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>− 1]</code> ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 <code>−2<sup>31</sup></code> 的整数应该被舍入为 <code>−2<sup>31</sup></code> ，大于 <code>2<sup>31&nbsp;</sup>− 1</code> 的整数应该被舍入为 <code>2<sup>31&nbsp;</sup>− 1</code> 。</li>
</ol>

<p>返回整数作为最终结果。</p>

<p>&nbsp;</p>

<p><strong class="example">示例&nbsp;1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "42"</span></p>

<p><strong>输出：</strong><span class="example-io">42</span></p>

<p><strong>解释：</strong>加粗的字符串为已经读入的字符，插入符号是当前读取的字符。</p>

<pre>
带下划线线的字符是所读的内容，插入符号是当前读入位置。
第 1 步："42"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："<u>42</u>"（读入 "42"）
           ^
</pre>
</div>

<p><strong class="example">示例&nbsp;2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = " -042"</span></p>

<p><strong>输出：</strong><span class="example-io">-42</span></p>

<p><strong>解释：</strong></p>

<pre>
第 1 步："<u><strong>   </strong></u>-042"（读入前导空格，但忽视掉）
            ^
第 2 步："   <u>-</u>042"（读入 '-' 字符，所以结果应该是负数）
             ^
第 3 步："   <u>-042</u>"（读入 "042"，在结果中忽略前导零）
               ^
</pre>
</div>

<p><strong class="example">示例&nbsp;3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "</span>1337c0d3<span class="example-io">"</span></p>

<p><strong>输出：</strong><span class="example-io">1337</span></p>

<p><strong>解释：</strong></p>

<pre>
第 1 步："1337c0d3"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："1337c0d3"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："1337c0d3"（读入 "1337"；由于下一个字符不是一个数字，所以读入停止）
             ^
</pre>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "0-1"</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<pre>
第 1 步："0-1" (当前没有读入字符，因为没有前导空格)
         ^
第 2 步："0-1" (当前没有读入字符，因为这里不存在 '-' 或者 '+')
         ^
第 3 步："<u>0</u>-1" (读入 "0"；由于下一个字符不是一个数字，所以读入停止)
          ^
</pre>
</div>

<p><strong class="example">示例 5：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "words and 987"</span></p>

<p><strong>输出：</strong><span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>读取在第一个非数字字符“w”处停止。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 200</code></li>
	<li><code>s</code> 由英文字母（大写和小写）、数字（<code>0-9</code>）、<code>' '</code>、<code>'+'</code>、<code>'-'</code> 和 <code>'.'</code> 组成</li>
</ul>


## 难度

Medium

## 标签

- 字符串

## 示例

```
"42"
"   -042"
"1337c0d3"
"0-1"
"words and 987"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int myAtoi(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int myAtoi(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def myAtoi(self, s: str) -> int:
        
```

### C

```c
int myAtoi(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MyAtoi(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    
};
```

### TypeScript

```typescript
function myAtoi(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function myAtoi($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func myAtoi(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun myAtoi(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int myAtoi(String s) {
    
  }
}
```

### Go

```golang
func myAtoi(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def my_atoi(s)
    
end
```

### Scala

```scala
object Solution {
    def myAtoi(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (my-atoi s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec my_atoi(S :: unicode:unicode_binary()) -> integer().
my_atoi(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec my_atoi(s :: String.t) :: integer
  def my_atoi(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func myAtoi(s: String): Int64 {

    }
}
```

