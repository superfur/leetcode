# 1397. 找到所有好字符串

## 题目描述

<p>给你两个长度为 <code>n</code>&nbsp;的字符串&nbsp;<code>s1</code> 和&nbsp;<code>s2</code>&nbsp;，以及一个字符串&nbsp;<code>evil</code>&nbsp;。请你返回 <strong>好字符串&nbsp;</strong>的数目。</p>

<p><strong>好字符串</strong>&nbsp;的定义为：它的长度为&nbsp;<code>n</code>&nbsp;，字典序大于等于&nbsp;<code>s1</code>&nbsp;，字典序小于等于&nbsp;<code>s2</code>&nbsp;，且不包含&nbsp;<code>evil</code>&nbsp;为子字符串。</p>

<p>由于答案可能很大，请你返回答案对 10^9 + 7 取余的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 2, s1 = &quot;aa&quot;, s2 = &quot;da&quot;, evil = &quot;b&quot;
<strong>输出：</strong>51 
<strong>解释：</strong>总共有 25 个以 &#39;a&#39; 开头的好字符串：&quot;aa&quot;，&quot;ac&quot;，&quot;ad&quot;，...，&quot;az&quot;。还有 25 个以 &#39;c&#39; 开头的好字符串：&quot;ca&quot;，&quot;cc&quot;，&quot;cd&quot;，...，&quot;cz&quot;。最后，还有一个以 &#39;d&#39; 开头的好字符串：&quot;da&quot;。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 8, s1 = &quot;leetcode&quot;, s2 = &quot;leetgoes&quot;, evil = &quot;leet&quot;
<strong>输出：</strong>0 
<strong>解释：</strong>所有字典序大于等于 s1 且小于等于 s2 的字符串都以 evil 字符串 &quot;leet&quot; 开头。所以没有好字符串。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 2, s1 = &quot;gx&quot;, s2 = &quot;gz&quot;, evil = &quot;x&quot;
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>s1.length == n</code></li>
	<li><code>s2.length == n</code></li>
	<li><code>s1 &lt;= s2</code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>1 &lt;= evil.length &lt;= 50</code></li>
	<li>所有字符串都只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划
- 字符串匹配

## 提示

1. Use DP with 4 states (pos: Int, posEvil: Int, equalToS1: Bool, equalToS2: Bool) which compute the number of valid strings of size "pos" where the maximum common suffix with string "evil" has size "posEvil". When "equalToS1" is "true", the current valid string is equal to "S1" otherwise it is greater. In a similar way when equalToS2 is "true" the current valid string is equal to "S2" otherwise it is smaller.
2. To update the maximum common suffix with string "evil" use KMP preprocessing.

## 示例

```
2
"aa"
"da"
"b"
8
"leetcode"
"leetgoes"
"leet"
2
"gx"
"gz"
"x"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findGoodStrings(int n, string s1, string s2, string evil) {
        
    }
};
```

### Java

```java
class Solution {
    public int findGoodStrings(int n, String s1, String s2, String evil) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findGoodStrings(self, n, s1, s2, evil):
        """
        :type n: int
        :type s1: str
        :type s2: str
        :type evil: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        
```

### C

```c
int findGoodStrings(int n, char* s1, char* s2, char* evil) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindGoodStrings(int n, string s1, string s2, string evil) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {string} s1
 * @param {string} s2
 * @param {string} evil
 * @return {number}
 */
var findGoodStrings = function(n, s1, s2, evil) {
    
};
```

### TypeScript

```typescript
function findGoodStrings(n: number, s1: string, s2: string, evil: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param String $s1
     * @param String $s2
     * @param String $evil
     * @return Integer
     */
    function findGoodStrings($n, $s1, $s2, $evil) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findGoodStrings(_ n: Int, _ s1: String, _ s2: String, _ evil: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findGoodStrings(n: Int, s1: String, s2: String, evil: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findGoodStrings(int n, String s1, String s2, String evil) {
    
  }
}
```

### Go

```golang
func findGoodStrings(n int, s1 string, s2 string, evil string) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {String} s1
# @param {String} s2
# @param {String} evil
# @return {Integer}
def find_good_strings(n, s1, s2, evil)
    
end
```

### Scala

```scala
object Solution {
    def findGoodStrings(n: Int, s1: String, s2: String, evil: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_good_strings(n: i32, s1: String, s2: String, evil: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-good-strings n s1 s2 evil)
  (-> exact-integer? string? string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_good_strings(N :: integer(), S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary(), Evil :: unicode:unicode_binary()) -> integer().
find_good_strings(N, S1, S2, Evil) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_good_strings(n :: integer, s1 :: String.t, s2 :: String.t, evil :: String.t) :: integer
  def find_good_strings(n, s1, s2, evil) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findGoodStrings(n: Int64, s1: String, s2: String, evil: String): Int64 {

    }
}
```

