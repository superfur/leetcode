# 12. 整数转罗马数字

## 题目描述

<p>七个不同的符号代表罗马数字，其值如下：</p>

<table>
	<thead>
		<tr>
			<th>符号</th>
			<th>值</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>I</td>
			<td>1</td>
		</tr>
		<tr>
			<td>V</td>
			<td>5</td>
		</tr>
		<tr>
			<td>X</td>
			<td>10</td>
		</tr>
		<tr>
			<td>L</td>
			<td>50</td>
		</tr>
		<tr>
			<td>C</td>
			<td>100</td>
		</tr>
		<tr>
			<td>D</td>
			<td>500</td>
		</tr>
		<tr>
			<td>M</td>
			<td>1000</td>
		</tr>
	</tbody>
</table>

<p>罗马数字是通过添加从最高到最低的小数位值的转换而形成的。将小数位值转换为罗马数字有以下规则：</p>

<ul>
	<li>如果该值不是以 4 或 9 开头，请选择可以从输入中减去的最大值的符号，将该符号附加到结果，减去其值，然后将其余部分转换为罗马数字。</li>
	<li>如果该值以 4 或 9 开头，使用 <strong>减法形式</strong>，表示从以下符号中减去一个符号，例如&nbsp;4 是 5 (<code>V</code>) 减 1 (<code>I</code>): <code>IV</code>&nbsp;，9 是 10 (<code>X</code>) 减&nbsp;1 (<code>I</code>)：<code>IX</code>。仅使用以下减法形式：4 (<code>IV</code>)，9 (<code>IX</code>)，40 (<code>XL</code>)，90 (<code>XC</code>)，400 (<code>CD</code>) 和&nbsp;900 (<code>CM</code>)。</li>
	<li>只有 10 的次方（<code>I</code>, <code>X</code>, <code>C</code>, <code>M</code>）最多可以连续附加 3 次以代表 10 的倍数。你不能多次附加&nbsp;5&nbsp;(<code>V</code>)，50 (<code>L</code>) 或 500 (<code>D</code>)。如果需要将符号附加4次，请使用 <strong>减法形式</strong>。</li>
</ul>

<p>给定一个整数，将其转换为罗马数字。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">num = 3749</span></p>

<p><strong>输出：</strong>&nbsp;<span class="example-io">"MMMDCCXLIX"</span></p>

<p><strong>解释：</strong></p>

<pre>
3000 = MMM 由于 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC 由于 500 (D) + 100 (C) + 100 (C)
  40 = XL 由于 50 (L) 减 10 (X)
   9 = IX 由于 10 (X) 减 1 (I)
注意：49 不是 50 (L) 减 1 (I) 因为转换是基于小数位
</pre>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">num = 58</span></p>

<p><strong>输出：</strong><span class="example-io">"LVIII"</span></p>

<p><strong>解释：</strong></p>

<pre>
50 = L
 8 = VIII
</pre>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">num = 1994</span></p>

<p><strong>输出：</strong><span class="example-io">"MCMXCIV"</span></p>

<p><strong>解释：</strong></p>

<pre>
1000 = M
 900 = CM
  90 = XC
   4 = IV
</pre>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 3999</code></li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 数学
- 字符串

## 示例

```
3749
58
1994
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string intToRoman(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public String intToRoman(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def intToRoman(self, num: int) -> str:
        
```

### C

```c
char* intToRoman(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public string IntToRoman(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    
};
```

### TypeScript

```typescript
function intToRoman(num: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return String
     */
    function intToRoman($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func intToRoman(_ num: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun intToRoman(num: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String intToRoman(int num) {
    
  }
}
```

### Go

```golang
func intToRoman(num int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {String}
def int_to_roman(num)
    
end
```

### Scala

```scala
object Solution {
    def intToRoman(num: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (int-to-roman num)
  (-> exact-integer? string?)
  )
```

### Erlang

```erlang
-spec int_to_roman(Num :: integer()) -> unicode:unicode_binary().
int_to_roman(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec int_to_roman(num :: integer) :: String.t
  def int_to_roman(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func intToRoman(num: Int64): String {

    }
}
```

