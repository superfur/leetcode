# 1405. 最长快乐字符串

## 题目描述

<p>如果字符串中不含有任何 <code>&#39;aaa&#39;</code>，<code>&#39;bbb&#39;</code> 或 <code>&#39;ccc&#39;</code> 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。</p>

<p>给你三个整数 <code>a</code>，<code>b</code> ，<code>c</code>，请你返回 <strong>任意一个</strong> 满足下列全部条件的字符串 <code>s</code>：</p>

<ul>
	<li><code>s</code> 是一个尽可能长的快乐字符串。</li>
	<li><code>s</code> 中 <strong>最多</strong> 有<code>a</code> 个字母 <code>&#39;a&#39;</code>、<code>b</code>&nbsp;个字母 <code>&#39;b&#39;</code>、<code>c</code> 个字母 <code>&#39;c&#39;</code> 。</li>
	<li><code>s </code>中只含有 <code>&#39;a&#39;</code>、<code>&#39;b&#39;</code> 、<code>&#39;c&#39;</code> 三种字母。</li>
</ul>

<p>如果不存在这样的字符串 <code>s</code> ，请返回一个空字符串 <code>&quot;&quot;</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>a = 1, b = 1, c = 7
<strong>输出：</strong>&quot;ccaccbcc&quot;
<strong>解释：</strong>&quot;ccbccacc&quot; 也是一种正确答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>a = 2, b = 2, c = 1
<strong>输出：</strong>&quot;aabbc&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>a = 7, b = 1, c = 0
<strong>输出：</strong>&quot;aabaa&quot;
<strong>解释：</strong>这是该测试用例的唯一正确答案。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= a, b, c &lt;= 100</code></li>
	<li><code>a + b + c &gt; 0</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串
- 堆（优先队列）

## 提示

1. Use a greedy approach.
2. Use the letter with the maximum current limit that can be added without breaking the condition.

## 示例

```
1
1
7
7
1
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        
    }
};
```

### Java

```java
class Solution {
    public String longestDiverseString(int a, int b, int c) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
```

### C

```c
char* longestDiverseString(int a, int b, int c) {
    
}
```

### C#

```csharp
public class Solution {
    public string LongestDiverseString(int a, int b, int c) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {string}
 */
var longestDiverseString = function(a, b, c) {
    
};
```

### TypeScript

```typescript
function longestDiverseString(a: number, b: number, c: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return String
     */
    function longestDiverseString($a, $b, $c) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestDiverseString(_ a: Int, _ b: Int, _ c: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestDiverseString(a: Int, b: Int, c: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String longestDiverseString(int a, int b, int c) {
    
  }
}
```

### Go

```golang
func longestDiverseString(a int, b int, c int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {String}
def longest_diverse_string(a, b, c)
    
end
```

### Scala

```scala
object Solution {
    def longestDiverseString(a: Int, b: Int, c: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_diverse_string(a: i32, b: i32, c: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (longest-diverse-string a b c)
  (-> exact-integer? exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec longest_diverse_string(A :: integer(), B :: integer(), C :: integer()) -> unicode:unicode_binary().
longest_diverse_string(A, B, C) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_diverse_string(a :: integer, b :: integer, c :: integer) :: String.t
  def longest_diverse_string(a, b, c) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestDiverseString(a: Int64, b: Int64, c: Int64): String {

    }
}
```

