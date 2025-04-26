# 1625. 执行操作后字典序最小的字符串

## 题目描述

<p>给你一个字符串 <code>s</code> 以及两个整数 <code>a</code> 和 <code>b</code> 。其中，字符串 <code>s</code> 的长度为偶数，且仅由数字 <code>0</code> 到 <code>9</code> 组成。</p>

<p>你可以在 <code>s</code> 上按任意顺序多次执行下面两个操作之一：</p>

<ul>
	<li>累加：将&nbsp; <code>a</code> 加到 <code>s</code> 中所有下标为奇数的元素上（<strong>下标从 0 开始</strong>）。数字一旦超过 <code>9</code> 就会变成 <code>0</code>，如此循环往复。例如，<code>s = "3456"</code> 且 <code>a = 5</code>，则执行此操作后 <code>s</code> 变成 <code>"3951"</code>。</li>
	<li>轮转：将 <code>s</code> 向右轮转 <code>b</code> 位。例如，<code>s = "3456"</code> 且 <code>b = 1</code>，则执行此操作后 <code>s</code> 变成 <code>"6345"</code>。</li>
</ul>

<p>请你返回在 <code>s</code> 上执行上述操作任意次后可以得到的 <strong>字典序最小</strong> 的字符串。</p>

<p>如果两个字符串长度相同，那么字符串 <code>a</code> 字典序比字符串 <code>b</code> 小可以这样定义：在 <code>a</code> 和 <code>b</code> 出现不同的第一个位置上，字符串 <code>a</code> 中的字符出现在字母表中的时间早于 <code>b</code> 中的对应字符。例如，<code>"0158”</code> 字典序比 <code>"0190"</code> 小，因为不同的第一个位置是在第三个字符，显然 <code>'5'</code> 出现在 <code>'9'</code> 之前。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "5525", a = 9, b = 2
<strong>输出：</strong>"2050"
<strong>解释：</strong>执行操作如下：
初态："5525"
轮转："2555"
累加："2454"
累加："2353"
轮转："5323"
累加："5222"
累加："5121"
轮转："2151"
累加："2050"​​​​​
无法获得字典序小于 "2050" 的字符串。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "74", a = 5, b = 1
<strong>输出：</strong>"24"
<strong>解释：</strong>执行操作如下：
初态："74"
轮转："47"
累加："42"
轮转："24"​​​​​
无法获得字典序小于 "24" 的字符串。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "0011", a = 4, b = 2
<strong>输出：</strong>"0011"
<strong>解释：</strong>无法获得字典序小于 "0011" 的字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s.length</code> 是偶数</li>
	<li><code>s</code> 仅由数字 <code>0</code> 到 <code>9</code> 组成</li>
	<li><code>1 &lt;= a &lt;= 9</code></li>
	<li><code>1 &lt;= b &lt;= s.length - 1</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 字符串
- 枚举

## 提示

1. Since the length of s is even, the total number of possible sequences is at most 10 * 10 * s.length.
2. You can generate all possible sequences and take their minimum.
3. Keep track of already generated sequences so they are not processed again.

## 示例

```
"5525"
9
2
"74"
5
1
"0011"
4
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string findLexSmallestString(string s, int a, int b) {
        
    }
};
```

### Java

```java
class Solution {
    public String findLexSmallestString(String s, int a, int b) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
```

### C

```c
char* findLexSmallestString(char* s, int a, int b) {
    
}
```

### C#

```csharp
public class Solution {
    public string FindLexSmallestString(string s, int a, int b) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} a
 * @param {number} b
 * @return {string}
 */
var findLexSmallestString = function(s, a, b) {
    
};
```

### TypeScript

```typescript
function findLexSmallestString(s: string, a: number, b: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $a
     * @param Integer $b
     * @return String
     */
    function findLexSmallestString($s, $a, $b) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLexSmallestString(_ s: String, _ a: Int, _ b: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLexSmallestString(s: String, a: Int, b: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String findLexSmallestString(String s, int a, int b) {
    
  }
}
```

### Go

```golang
func findLexSmallestString(s string, a int, b int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} a
# @param {Integer} b
# @return {String}
def find_lex_smallest_string(s, a, b)
    
end
```

### Scala

```scala
object Solution {
    def findLexSmallestString(s: String, a: Int, b: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_lex_smallest_string(s: String, a: i32, b: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (find-lex-smallest-string s a b)
  (-> string? exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec find_lex_smallest_string(S :: unicode:unicode_binary(), A :: integer(), B :: integer()) -> unicode:unicode_binary().
find_lex_smallest_string(S, A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_lex_smallest_string(s :: String.t, a :: integer, b :: integer) :: String.t
  def find_lex_smallest_string(s, a, b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLexSmallestString(s: String, a: Int64, b: Int64): String {

    }
}
```

