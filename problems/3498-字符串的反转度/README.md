# 3498. 字符串的反转度

## 题目描述

<p>给你一个字符串 <code>s</code>，计算其 <strong>反转度</strong>。</p>

<p><strong>反转度</strong>的计算方法如下：</p>

<ol>
	<li>对于每个字符，将其在 <strong>反转</strong> 字母表中的位置（<code>'a'</code> = 26, <code>'b'</code> = 25, ..., <code>'z'</code> = 1）与其在字符串中的位置（下标从<strong>1 </strong>开始）相乘。</li>
	<li>将这些乘积加起来，得到字符串中所有字符的和。</li>
</ol>

<p>返回 <strong>反转度</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "abc"</span></p>

<p><strong>输出：</strong> <span class="example-io">148</span></p>

<p><strong>解释：</strong></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">字母</th>
			<th style="border: 1px solid black;">反转字母表中的位置</th>
			<th style="border: 1px solid black;">字符串中的位置</th>
			<th style="border: 1px solid black;">乘积</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>'a'</code></td>
			<td style="border: 1px solid black;">26</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">26</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>'b'</code></td>
			<td style="border: 1px solid black;">25</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">50</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>'c'</code></td>
			<td style="border: 1px solid black;">24</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">72</td>
		</tr>
	</tbody>
</table>

<p>反转度是 <code>26 + 50 + 72 = 148</code> 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "zaza"</span></p>

<p><strong>输出：</strong> <span class="example-io">160</span></p>

<p><strong>解释：</strong></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">字母</th>
			<th style="border: 1px solid black;">反转字母表中的位置</th>
			<th style="border: 1px solid black;">字符串中的位置</th>
			<th style="border: 1px solid black;">乘积</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>'z'</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>'a'</code></td>
			<td style="border: 1px solid black;">26</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">52</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>'z'</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>'a'</code></td>
			<td style="border: 1px solid black;">26</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">104</td>
		</tr>
	</tbody>
</table>
</div>

<p>反转度是 <code>1 + 52 + 3 + 104 = 160</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> 仅包含小写字母。</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 模拟

## 提示

1. Simulate the operations as described.

## 示例

```
"abc"
"zaza"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int reverseDegree(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int reverseDegree(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def reverseDegree(self, s: str) -> int:
        
```

### C

```c
int reverseDegree(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int ReverseDegree(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var reverseDegree = function(s) {
    
};
```

### TypeScript

```typescript
function reverseDegree(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function reverseDegree($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reverseDegree(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reverseDegree(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int reverseDegree(String s) {
    
  }
}
```

### Go

```golang
func reverseDegree(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def reverse_degree(s)
    
end
```

### Scala

```scala
object Solution {
    def reverseDegree(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reverse_degree(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (reverse-degree s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec reverse_degree(S :: unicode:unicode_binary()) -> integer().
reverse_degree(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reverse_degree(s :: String.t) :: integer
  def reverse_degree(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reverseDegree(s: String): Int64 {

    }
}
```

