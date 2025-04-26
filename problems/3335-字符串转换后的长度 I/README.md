# 3335. 字符串转换后的长度 I

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个整数 <code>t</code>，表示要执行的<strong> 转换 </strong>次数。每次 <strong>转换 </strong>需要根据以下规则替换字符串 <code>s</code> 中的每个字符：</p>

<ul>
	<li>如果字符是 <code>'z'</code>，则将其替换为字符串 <code>"ab"</code>。</li>
	<li>否则，将其替换为字母表中的<strong>下一个</strong>字符。例如，<code>'a'</code> 替换为 <code>'b'</code>，<code>'b'</code> 替换为 <code>'c'</code>，依此类推。</li>
</ul>

<p>返回<strong> 恰好 </strong>执行 <code>t</code> 次转换后得到的字符串的 <strong>长度</strong>。</p>

<p>由于答案可能非常大，返回其对 <code>10<sup>9</sup> + 7</code> 取余的结果。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "abcyy", t = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">7</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><strong>第一次转换 (t = 1)</strong>

	<ul>
		<li><code>'a'</code> 变为 <code>'b'</code></li>
		<li><code>'b'</code> 变为 <code>'c'</code></li>
		<li><code>'c'</code> 变为 <code>'d'</code></li>
		<li><code>'y'</code> 变为 <code>'z'</code></li>
		<li><code>'y'</code> 变为 <code>'z'</code></li>
		<li>第一次转换后的字符串为：<code>"bcdzz"</code></li>
	</ul>
	</li>
	<li><strong>第二次转换 (t = 2)</strong>
	<ul>
		<li><code>'b'</code> 变为 <code>'c'</code></li>
		<li><code>'c'</code> 变为 <code>'d'</code></li>
		<li><code>'d'</code> 变为 <code>'e'</code></li>
		<li><code>'z'</code> 变为 <code>"ab"</code></li>
		<li><code>'z'</code> 变为 <code>"ab"</code></li>
		<li>第二次转换后的字符串为：<code>"cdeabab"</code></li>
	</ul>
	</li>
	<li><strong>最终字符串长度</strong>：字符串为 <code>"cdeabab"</code>，长度为 7 个字符。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "azbk", t = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><strong>第一次转换 (t = 1)</strong>

	<ul>
		<li><code>'a'</code> 变为 <code>'b'</code></li>
		<li><code>'z'</code> 变为 <code>"ab"</code></li>
		<li><code>'b'</code> 变为 <code>'c'</code></li>
		<li><code>'k'</code> 变为 <code>'l'</code></li>
		<li>第一次转换后的字符串为：<code>"babcl"</code></li>
	</ul>
	</li>
	<li><strong>最终字符串长度</strong>：字符串为 <code>"babcl"</code>，长度为 5 个字符。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
	<li><code>1 &lt;= t &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 数学
- 字符串
- 动态规划
- 计数

## 提示

1. Maintain the frequency of each character.

## 示例

```
"abcyy"
2
"azbk"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int lengthAfterTransformations(string s, int t) {
        
    }
};
```

### Java

```java
class Solution {
    public int lengthAfterTransformations(String s, int t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
```

### C

```c
int lengthAfterTransformations(char* s, int t) {
    
}
```

### C#

```csharp
public class Solution {
    public int LengthAfterTransformations(string s, int t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} t
 * @return {number}
 */
var lengthAfterTransformations = function(s, t) {
    
};
```

### TypeScript

```typescript
function lengthAfterTransformations(s: string, t: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $t
     * @return Integer
     */
    function lengthAfterTransformations($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lengthAfterTransformations(_ s: String, _ t: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lengthAfterTransformations(s: String, t: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int lengthAfterTransformations(String s, int t) {
    
  }
}
```

### Go

```golang
func lengthAfterTransformations(s string, t int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} t
# @return {Integer}
def length_after_transformations(s, t)
    
end
```

### Scala

```scala
object Solution {
    def lengthAfterTransformations(s: String, t: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn length_after_transformations(s: String, t: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (length-after-transformations s t)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec length_after_transformations(S :: unicode:unicode_binary(), T :: integer()) -> integer().
length_after_transformations(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec length_after_transformations(s :: String.t, t :: integer) :: integer
  def length_after_transformations(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lengthAfterTransformations(s: String, t: Int64): Int64 {

    }
}
```

