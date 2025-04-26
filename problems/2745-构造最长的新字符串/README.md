# 2745. 构造最长的新字符串

## 题目描述

<p>给你三个整数&nbsp;<code>x</code>&nbsp;，<code>y</code>&nbsp;和&nbsp;<code>z</code>&nbsp;。</p>

<p>这三个整数表示你有&nbsp;<code>x</code>&nbsp;个&nbsp;<code>"AA"</code>&nbsp;字符串，<code>y</code>&nbsp;个&nbsp;<code>"BB"</code>&nbsp;字符串，和&nbsp;<code>z</code>&nbsp;个&nbsp;<code>"AB"</code>&nbsp;字符串。你需要选择这些字符串中的部分字符串（可以全部选择也可以一个都不选择），将它们按顺序连接得到一个新的字符串。新字符串不能包含子字符串&nbsp;<code>"AAA"</code>&nbsp;或者&nbsp;<code>"BBB"</code>&nbsp;。</p>

<p>请你返回 <em>新字符串的最大可能长度。</em></p>

<p><strong>子字符串</strong>&nbsp;是一个字符串中一段连续 <strong>非空</strong>&nbsp;的字符序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>x = 2, y = 5, z = 1
<b>输出：</b>12
<strong>解释： </strong>我们可以按顺序连接 "BB" ，"AA" ，"BB" ，"AA" ，"BB" 和 "AB" ，得到新字符串 "BBAABBAABBAB" 。
字符串长度为 12 ，无法得到一个更长的符合题目要求的字符串。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>x = 3, y = 2, z = 2
<b>输出：</b>14
<b>解释：</b>我们可以按顺序连接 "AB" ，"AB" ，"AA" ，"BB" ，"AA" ，"BB" 和 "AA" ，得到新字符串 "ABABAABBAABBAA" 。
字符串长度为 14 ，无法得到一个更长的符合题目要求的字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= x, y, z &lt;= 50</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 脑筋急转弯
- 数学
- 动态规划

## 提示

1. It can be proved that ALL “AB”s can be used in the optimal solution.
(1) If the final string starts with 'A', we can put all unused “AB”s at the very beginning.
(2) If the final string starts with 'B' (meaning) it starts with “BB”, we can put all unused “AB”s after the 2nd 'B'.
2. Using “AB” doesn’t increase the number of “AA”s or “BB”s we can use.
If we put an “AB” after “BB”, then we still need to append “AA” as before, so it doesn’t change the state.
3. We only need to consider strings “AA” and “BB”; we can either use the pattern “AABBAABB…” or the pattern “BBAABBAA…”, depending on which one of x and y is larger.

## 示例

```
2
5
1
3
2
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestString(int x, int y, int z) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestString(int x, int y, int z) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestString(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        
```

### C

```c
int longestString(int x, int y, int z) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestString(int x, int y, int z) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {number}
 */
var longestString = function(x, y, z) {
    
};
```

### TypeScript

```typescript
function longestString(x: number, y: number, z: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer $z
     * @return Integer
     */
    function longestString($x, $y, $z) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestString(_ x: Int, _ y: Int, _ z: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestString(x: Int, y: Int, z: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestString(int x, int y, int z) {
    
  }
}
```

### Go

```golang
func longestString(x int, y int, z int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} x
# @param {Integer} y
# @param {Integer} z
# @return {Integer}
def longest_string(x, y, z)
    
end
```

### Scala

```scala
object Solution {
    def longestString(x: Int, y: Int, z: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_string(x: i32, y: i32, z: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-string x y z)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_string(X :: integer(), Y :: integer(), Z :: integer()) -> integer().
longest_string(X, Y, Z) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_string(x :: integer, y :: integer, z :: integer) :: integer
  def longest_string(x, y, z) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestString(x: Int64, y: Int64, z: Int64): Int64 {

    }
}
```

