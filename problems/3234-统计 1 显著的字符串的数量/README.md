# 3234. 统计 1 显著的字符串的数量

## 题目描述

<p>给你一个二进制字符串 <code>s</code>。</p>

<p>请你统计并返回其中 <strong>1 显著 </strong> 的 <span data-keyword="substring-nonempty">子字符串</span> 的数量。</p>

<p>如果字符串中 1 的数量 <strong>大于或等于</strong> 0 的数量的 <strong>平方</strong>，则认为该字符串是一个 <strong>1 显著</strong> 的字符串 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "00011"</span></p>

<p><strong>输出：</strong><span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p>1 显著的子字符串如下表所示。</p>
</div>

<table>
	<thead>
		<tr>
			<th>i</th>
			<th>j</th>
			<th>s[i..j]</th>
			<th>0 的数量</th>
			<th>1 的数量</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>3</td>
			<td>3</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>4</td>
			<td>4</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>3</td>
			<td>01</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>4</td>
			<td>11</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>4</td>
			<td>011</td>
			<td>1</td>
			<td>2</td>
		</tr>
	</tbody>
</table>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "101101"</span></p>

<p><strong>输出：</strong><span class="example-io">16</span></p>

<p><strong>解释：</strong></p>

<p>1 不显著的子字符串如下表所示。</p>

<p>总共有 21 个子字符串，其中 5 个是 1 不显著字符串，因此有 16 个 1 显著子字符串。</p>
</div>

<table>
	<thead>
		<tr>
			<th>i</th>
			<th>j</th>
			<th>s[i..j]</th>
			<th>0 的数量</th>
			<th>1 的数量</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>4</td>
			<td>4</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>1</td>
			<td>4</td>
			<td>0110</td>
			<td>2</td>
			<td>2</td>
		</tr>
		<tr>
			<td>0</td>
			<td>4</td>
			<td>10110</td>
			<td>2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>1</td>
			<td>5</td>
			<td>01101</td>
			<td>2</td>
			<td>3</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>s</code> 仅包含字符 <code>'0'</code> 和 <code>'1'</code>。</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 枚举
- 滑动窗口

## 提示

1. Let us fix the starting index <code>l</code> of the substring and count the number of indices <code>r</code> such that <code>l <= r</code> and the substring <code>s[l..r]</code> has dominant ones.
2. A substring with dominant ones has at most <code>sqrt(n)</code> zeros.
3. We cannot iterate over every <code>r</code> and check if the  <code>s[l..r]</code> has dominant ones. Instead, we iterate over the next <code>sqrt(n)</code> zeros to the left of <code>l</code> and count the number of substrings with dominant ones where the current zero is the rightmost zero of the substring.

## 示例

```
"00011"
"101101"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfSubstrings(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfSubstrings(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
```

### C

```c
int numberOfSubstrings(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfSubstrings(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    
};
```

### TypeScript

```typescript
function numberOfSubstrings(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numberOfSubstrings($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfSubstrings(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfSubstrings(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfSubstrings(String s) {
    
  }
}
```

### Go

```golang
func numberOfSubstrings(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def number_of_substrings(s)
    
end
```

### Scala

```scala
object Solution {
    def numberOfSubstrings(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-substrings s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_substrings(S :: unicode:unicode_binary()) -> integer().
number_of_substrings(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_substrings(s :: String.t) :: integer
  def number_of_substrings(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfSubstrings(s: String): Int64 {

    }
}
```

