# 2243. 计算字符串的数字和

## 题目描述

<p>给你一个由若干数字（<code>0</code> - <code>9</code>）组成的字符串 <code>s</code> ，和一个整数。</p>

<p>如果 <code>s</code> 的长度大于 <code>k</code> ，则可以执行一轮操作。在一轮操作中，需要完成以下工作：</p>

<ol>
	<li>将 <code>s</code> <strong>拆分 </strong>成长度为 <code>k</code> 的若干 <strong>连续数字组</strong> ，使得前 <code>k</code> 个字符都分在第一组，接下来的 <code>k</code> 个字符都分在第二组，依此类推。<strong>注意</strong>，最后一个数字组的长度可以小于 <code>k</code> 。</li>
	<li>用表示每个数字组中所有数字之和的字符串来 <strong>替换</strong> 对应的数字组。例如，<code>"346"</code> 会替换为 <code>"13"</code> ，因为 <code>3 + 4 + 6 = 13</code> 。</li>
	<li><strong>合并</strong> 所有组以形成一个新字符串。如果新字符串的长度大于 <code>k</code> 则重复第一步。</li>
</ol>

<p>返回在完成所有轮操作后的 <code>s</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "11111222223", k = 3
<strong>输出：</strong>"135"
<strong>解释：</strong>
- 第一轮，将 s 分成："111"、"112"、"222" 和 "23" 。
  接着，计算每一组的数字和：1 + 1 + 1 = 3、1 + 1 + 2 = 4、2 + 2 + 2 = 6 和 2 + 3 = 5 。 
&nbsp; 这样，s 在第一轮之后变成 "3" + "4" + "6" + "5" = "3465" 。
- 第二轮，将 s 分成："346" 和 "5" 。
&nbsp; 接着，计算每一组的数字和：3 + 4 + 6 = 13 、5 = 5 。
&nbsp; 这样，s 在第二轮之后变成 "13" + "5" = "135" 。 
现在，s.length &lt;= k ，所以返回 "135" 作为答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "00000000", k = 3
<strong>输出：</strong>"000"
<strong>解释：</strong>
将 "000", "000", and "00".
接着，计算每一组的数字和：0 + 0 + 0 = 0 、0 + 0 + 0 = 0 和 0 + 0 = 0 。 
s 变为 "0" + "0" + "0" = "000" ，其长度等于 k ，所以返回 "000" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>2 &lt;= k &lt;= 100</code></li>
	<li><code>s</code> 仅由数字（<code>0</code> - <code>9</code>）组成。</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 模拟

## 提示

1. Try simulating the entire process to find the final answer.

## 示例

```
"11111222223"
3
"00000000"
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string digitSum(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String digitSum(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
```

### C

```c
char* digitSum(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string DigitSum(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var digitSum = function(s, k) {
    
};
```

### TypeScript

```typescript
function digitSum(s: string, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function digitSum($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func digitSum(_ s: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun digitSum(s: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String digitSum(String s, int k) {
    
  }
}
```

### Go

```golang
func digitSum(s string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def digit_sum(s, k)
    
end
```

### Scala

```scala
object Solution {
    def digitSum(s: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn digit_sum(s: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (digit-sum s k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec digit_sum(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
digit_sum(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec digit_sum(s :: String.t, k :: integer) :: String.t
  def digit_sum(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func digitSum(s: String, k: Int64): String {

    }
}
```

