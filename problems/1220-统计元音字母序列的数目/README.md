# 1220. 统计元音字母序列的数目

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>，请你帮忙统计一下我们可以按下述规则形成多少个长度为&nbsp;<code>n</code>&nbsp;的字符串：</p>

<ul>
	<li>字符串中的每个字符都应当是小写元音字母（<code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, <code>&#39;u&#39;</code>）</li>
	<li>每个元音&nbsp;<code>&#39;a&#39;</code>&nbsp;后面都只能跟着&nbsp;<code>&#39;e&#39;</code></li>
	<li>每个元音&nbsp;<code>&#39;e&#39;</code>&nbsp;后面只能跟着&nbsp;<code>&#39;a&#39;</code>&nbsp;或者是&nbsp;<code>&#39;i&#39;</code></li>
	<li>每个元音&nbsp;<code>&#39;i&#39;</code>&nbsp;后面&nbsp;<strong>不能</strong> 再跟着另一个&nbsp;<code>&#39;i&#39;</code></li>
	<li>每个元音&nbsp;<code>&#39;o&#39;</code>&nbsp;后面只能跟着&nbsp;<code>&#39;i&#39;</code>&nbsp;或者是&nbsp;<code>&#39;u&#39;</code></li>
	<li>每个元音&nbsp;<code>&#39;u&#39;</code>&nbsp;后面只能跟着&nbsp;<code>&#39;a&#39;</code></li>
</ul>

<p>由于答案可能会很大，所以请你返回 模&nbsp;<code>10^9 + 7</code>&nbsp;之后的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 1
<strong>输出：</strong>5
<strong>解释：</strong>所有可能的字符串分别是：&quot;a&quot;, &quot;e&quot;, &quot;i&quot; , &quot;o&quot; 和 &quot;u&quot;。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>10
<strong>解释：</strong>所有可能的字符串分别是：&quot;ae&quot;, &quot;ea&quot;, &quot;ei&quot;, &quot;ia&quot;, &quot;ie&quot;, &quot;io&quot;, &quot;iu&quot;, &quot;oi&quot;, &quot;ou&quot; 和 &quot;ua&quot;。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 5
<strong>输出：</strong>68</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2 * 10^4</code></li>
</ul>


## 难度

Hard

## 标签

- 动态规划

## 提示

1. Use dynamic programming.
2. Let dp[i][j] be the number of strings of length i that ends with the j-th vowel.
3. Deduce the recurrence from the given relations between vowels.

## 示例

```
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countVowelPermutation(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int countVowelPermutation(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
```

### C

```c
int countVowelPermutation(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountVowelPermutation(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countVowelPermutation = function(n) {
    
};
```

### TypeScript

```typescript
function countVowelPermutation(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countVowelPermutation($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countVowelPermutation(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countVowelPermutation(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countVowelPermutation(int n) {
    
  }
}
```

### Go

```golang
func countVowelPermutation(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def count_vowel_permutation(n)
    
end
```

### Scala

```scala
object Solution {
    def countVowelPermutation(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_vowel_permutation(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-vowel-permutation n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_vowel_permutation(N :: integer()) -> integer().
count_vowel_permutation(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_vowel_permutation(n :: integer) :: integer
  def count_vowel_permutation(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countVowelPermutation(n: Int64): Int64 {

    }
}
```

