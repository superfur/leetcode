# 1717. 删除子字符串的最大得分

## 题目描述

<p>给你一个字符串 <code>s</code> 和两个整数 <code>x</code> 和 <code>y</code> 。你可以执行下面两种操作任意次。</p>

<ul>
	<li>删除子字符串 <code>"ab"</code> 并得到 <code>x</code> 分。

	<ul>
		<li>比方说，从 <code>"c<strong>ab</strong>xbae"</code> 删除 <code>ab</code> ，得到 <code>"cxbae"</code> 。</li>
	</ul>
	</li>
	<li>删除子字符串<code>"ba"</code> 并得到 <code>y</code> 分。
	<ul>
		<li>比方说，从 <code>"cabx<strong>ba</strong>e"</code> 删除 <code>ba</code> ，得到 <code>"cabxe"</code> 。</li>
	</ul>
	</li>
</ul>

<p>请返回对 <code>s</code> 字符串执行上面操作若干次能得到的最大得分。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "cdbcbbaaabab", x = 4, y = 5
<b>输出：</b>19
<strong>解释：</strong>
- 删除 "cdbcbbaaa<strong>ba</strong>b" 中加粗的 "ba" ，得到 s = "cdbcbbaaab" ，加 5 分。
- 删除 "cdbcbbaa<strong>ab</strong>" 中加粗的 "ab" ，得到 s = "cdbcbbaa" ，加 4 分。
- 删除 "cdbcb<strong>ba</strong>a" 中加粗的 "ba" ，得到 s = "cdbcba" ，加 5 分。
- 删除 "cdbc<strong>ba</strong>" 中加粗的 "ba" ，得到 s = "cdbc" ，加 5 分。
总得分为 5 + 4 + 5 + 5 = 19 。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "aabbaaxybbaabb", x = 5, y = 4
<b>输出：</b>20
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= x, y &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> 只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 字符串

## 提示

1. Note that it is always more optimal to take one type of substring before another
2. You can use a stack to handle erasures

## 示例

```
"cdbcbbaaabab"
4
5
"aabbaaxybbaabb"
5
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumGain(string s, int x, int y) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumGain(String s, int x, int y) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
```

### C

```c
int maximumGain(char* s, int x, int y) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumGain(string s, int x, int y) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var maximumGain = function(s, x, y) {
    
};
```

### TypeScript

```typescript
function maximumGain(s: string, x: number, y: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $x
     * @param Integer $y
     * @return Integer
     */
    function maximumGain($s, $x, $y) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumGain(_ s: String, _ x: Int, _ y: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumGain(s: String, x: Int, y: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumGain(String s, int x, int y) {
    
  }
}
```

### Go

```golang
func maximumGain(s string, x int, y int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def maximum_gain(s, x, y)
    
end
```

### Scala

```scala
object Solution {
    def maximumGain(s: String, x: Int, y: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_gain(s: String, x: i32, y: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-gain s x y)
  (-> string? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_gain(S :: unicode:unicode_binary(), X :: integer(), Y :: integer()) -> integer().
maximum_gain(S, X, Y) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_gain(s :: String.t, x :: integer, y :: integer) :: integer
  def maximum_gain(s, x, y) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumGain(s: String, x: Int64, y: Int64): Int64 {

    }
}
```

