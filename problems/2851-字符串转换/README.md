# 2851. 字符串转换

## 题目描述

<p>给你两个长度都为 <code>n</code>&nbsp;的字符串&nbsp;<code>s</code> 和&nbsp;<code>t</code>&nbsp;。你可以对字符串 <code>s</code>&nbsp;执行以下操作：</p>

<ul>
	<li>将 <code>s</code>&nbsp;长度为 <code>l</code>&nbsp;（<code>0 &lt; l &lt; n</code>）的 <strong>后缀字符串</strong>&nbsp;删除，并将它添加在 <code>s</code>&nbsp;的开头。<br />
	比方说，<code>s = 'abcd'</code>&nbsp;，那么一次操作中，你可以删除后缀&nbsp;<code>'cd'</code>&nbsp;，并将它添加到&nbsp;<code>s</code>&nbsp;的开头，得到&nbsp;<code>s = 'cdab'</code>&nbsp;。</li>
</ul>

<p>给你一个整数&nbsp;<code>k</code>&nbsp;，请你返回&nbsp;<strong>恰好</strong> <code>k</code>&nbsp;次操作将<em>&nbsp;</em><code>s</code> 变为<em>&nbsp;</em><code>t</code>&nbsp;的方案数。</p>

<p>由于答案可能很大，返回答案对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后的结果。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>s = "abcd", t = "cdab", k = 2
<b>输出：</b>2
<b>解释：</b>
第一种方案：
第一次操作，选择 index = 3 开始的后缀，得到 s = "dabc" 。
第二次操作，选择 index = 3 开始的后缀，得到 s = "cdab" 。

第二种方案：
第一次操作，选择 index = 1 开始的后缀，得到 s = "bcda" 。
第二次操作，选择 index = 1 开始的后缀，得到 s = "cdab" 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>s = "ababab", t = "ababab", k = 1
<b>输出：</b>2
<b>解释：</b>
第一种方案：
选择 index = 2 开始的后缀，得到 s = "ababab" 。

第二种方案：
选择 index = 4 开始的后缀，得到 s = "ababab" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>15</sup></code></li>
	<li><code>s.length == t.length</code></li>
	<li><code>s</code> 和&nbsp;<code>t</code>&nbsp;都只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 数学
- 字符串
- 动态规划
- 字符串匹配

## 提示

1. String <code>t</code> can be only constructed if it is a rotated version of string <code>s</code>.
2. Use KMP algorithm or Z algorithm to find the number of indices from where <code>s</code> is equal to <code>t</code>.
3. Use Dynamic Programming to count the number of ways.

## 示例

```
"abcd"
"cdab"
2
"ababab"
"ababab"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfWays(string s, string t, long long k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfWays(String s, String t, long k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfWays(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        
```

### C

```c
int numberOfWays(char* s, char* t, long long k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfWays(string s, string t, long k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @param {number} k
 * @return {number}
 */
var numberOfWays = function(s, t, k) {
    
};
```

### TypeScript

```typescript
function numberOfWays(s: string, t: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @param Integer $k
     * @return Integer
     */
    function numberOfWays($s, $t, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfWays(_ s: String, _ t: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfWays(s: String, t: String, k: Long): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfWays(String s, String t, int k) {
    
  }
}
```

### Go

```golang
func numberOfWays(s string, t string, k int64) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @param {Integer} k
# @return {Integer}
def number_of_ways(s, t, k)
    
end
```

### Scala

```scala
object Solution {
    def numberOfWays(s: String, t: String, k: Long): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_ways(s: String, t: String, k: i64) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-ways s t k)
  (-> string? string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_ways(S :: unicode:unicode_binary(), T :: unicode:unicode_binary(), K :: integer()) -> integer().
number_of_ways(S, T, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_ways(s :: String.t, t :: String.t, k :: integer) :: integer
  def number_of_ways(s, t, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfWays(s: String, t: String, k: Int64): Int64 {

    }
}
```

