# 848. 字母移位

## 题目描述

<p>有一个由小写字母组成的字符串 <code>s</code>，和一个长度相同的整数数组 <code>shifts</code>。</p>

<p>我们将字母表中的下一个字母称为原字母的 <em>移位</em>&nbsp;<code>shift()</code>&nbsp;（由于字母表是环绕的， <code>'z'</code>&nbsp;将会变成&nbsp;<code>'a'</code>）。</p>

<ul>
	<li>例如，<code>shift('a') = 'b'<font color="#333333"><font face="Helvetica Neue, Helvetica, Arial, sans-serif"><span style="font-size:14px"><span style="background-color:#ffffff">,&nbsp;</span></span></font></font></code><code>shift('t') = 'u'</code>,&nbsp;以及&nbsp;<code>shift('z') = 'a'</code>。</li>
</ul>

<p>对于每个&nbsp;<code>shifts[i] = x</code>&nbsp;， 我们会将 <code>s</code>&nbsp;中的前&nbsp;<code>i + 1</code>&nbsp;个字母移位&nbsp;<code>x</code>&nbsp;次。</p>

<p>返回 <em>将所有这些移位都应用到 <code>s</code> 后最终得到的字符串</em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abc", shifts = [3,5,9]
<strong>输出：</strong>"rpl"
<strong>解释： </strong>
我们以 "abc" 开始。
将 S 中的第 1 个字母移位 3 次后，我们得到 "dbc"。
再将 S 中的前 2 个字母移位 5 次后，我们得到 "igc"。
最后将 S 中的这 3 个字母移位 9 次后，我们得到答案 "rpl"。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> s = "aaa", shifts = [1,2,3]
<strong>输出:</strong> "gfd"
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;由小写英文字母组成</li>
	<li><code>shifts.length == s.length</code></li>
	<li><code>0 &lt;= shifts[i] &lt;= 10<sup>9</sup></code></li>
</ul>
<span style="display:block"><span style="height:0px"><span style="position:absolute">​​​​​​</span></span></span>

## 难度

Medium

## 标签

- 数组
- 字符串
- 前缀和

## 示例

```
"abc"
[3,5,9]
"aaa"
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string shiftingLetters(string s, vector<int>& shifts) {
        
    }
};
```

### Java

```java
class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
```

### C

```c
char* shiftingLetters(char* s, int* shifts, int shiftsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string ShiftingLetters(string s, int[] shifts) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number[]} shifts
 * @return {string}
 */
var shiftingLetters = function(s, shifts) {
    
};
```

### TypeScript

```typescript
function shiftingLetters(s: string, shifts: number[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[] $shifts
     * @return String
     */
    function shiftingLetters($s, $shifts) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shiftingLetters(_ s: String, _ shifts: [Int]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shiftingLetters(s: String, shifts: IntArray): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String shiftingLetters(String s, List<int> shifts) {
    
  }
}
```

### Go

```golang
func shiftingLetters(s string, shifts []int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer[]} shifts
# @return {String}
def shifting_letters(s, shifts)
    
end
```

### Scala

```scala
object Solution {
    def shiftingLetters(s: String, shifts: Array[Int]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shifting_letters(s: String, shifts: Vec<i32>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (shifting-letters s shifts)
  (-> string? (listof exact-integer?) string?)
  )
```

### Erlang

```erlang
-spec shifting_letters(S :: unicode:unicode_binary(), Shifts :: [integer()]) -> unicode:unicode_binary().
shifting_letters(S, Shifts) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shifting_letters(s :: String.t, shifts :: [integer]) :: String.t
  def shifting_letters(s, shifts) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shiftingLetters(s: String, shifts: Array<Int64>): String {

    }
}
```

