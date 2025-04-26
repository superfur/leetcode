# 2842. 统计一个字符串的 k 子序列美丽值最大的数目

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p><strong>k 子序列</strong>指的是 <code>s</code>&nbsp;的一个长度为 <code>k</code>&nbsp;的 <strong>子序列</strong>&nbsp;，且所有字符都是 <strong>唯一</strong>&nbsp;的，也就是说每个字符在子序列里只出现过一次。</p>

<p>定义&nbsp;<code>f(c)</code>&nbsp;为字符 <code>c</code>&nbsp;在 <code>s</code>&nbsp;中出现的次数。</p>

<p>k 子序列的 <strong>美丽值</strong>&nbsp;定义为这个子序列中每一个字符 <code>c</code>&nbsp;的&nbsp;<code>f(c)</code>&nbsp;之 <strong>和</strong>&nbsp;。</p>

<p>比方说，<code>s = "abbbdd"</code>&nbsp;和&nbsp;<code>k = 2</code>&nbsp;，我们有：</p>

<ul>
	<li><code>f('a') = 1</code>, <code>f('b') = 3</code>, <code>f('d') = 2</code></li>
	<li><code>s</code>&nbsp;的部分 k 子序列为：
	<ul>
		<li><code>"<em><strong>ab</strong></em>bbdd"</code> -&gt; <code>"ab"</code>&nbsp;，美丽值为&nbsp;<code>f('a') + f('b') = 4</code></li>
		<li><code>"<em><strong>a</strong></em>bbb<em><strong>d</strong></em>d"</code> -&gt; <code>"ad"</code>&nbsp;，美丽值为&nbsp;<code>f('a') + f('d') = 3</code></li>
		<li><code>"a<em><strong>b</strong></em>bb<em><strong>d</strong></em>d"</code> -&gt; <code>"bd"</code>&nbsp;，美丽值为&nbsp;<code>f('b') + f('d') = 5</code></li>
	</ul>
	</li>
</ul>

<p>请你返回一个整数，表示所有 <strong>k 子序列&nbsp;</strong>里面 <strong>美丽值 </strong>是&nbsp;<strong>最大值</strong>&nbsp;的子序列数目。由于答案可能很大，将结果对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;取余后返回。</p>

<p>一个字符串的子序列指的是从原字符串里面删除一些字符（也可能一个字符也不删除），不改变剩下字符顺序连接得到的新字符串。</p>

<p><strong>注意：</strong></p>

<ul>
	<li><code>f(c)</code> 指的是字符&nbsp;<code>c</code>&nbsp;在字符串&nbsp;<code>s</code>&nbsp;的出现次数，不是在 k 子序列里的出现次数。</li>
	<li>两个 k 子序列如果有任何一个字符在原字符串中的下标不同，则它们是两个不同的子序列。所以两个不同的 k 子序列可能产生相同的字符串。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>s = "bcca", k = 2
<b>输出：</b>4
<b>解释：</b><span style="white-space: normal">s 中我们有 f('a') = 1 ，f('b') = 1 和 f('c') = 2 。</span>
s 的 k 子序列为：
<em><strong>bc</strong></em>ca ，美丽值为 f('b') + f('c') = 3
<em><strong>b</strong></em>c<em><strong>c</strong></em>a ，美丽值为 f('b') + f('c') = 3
<em><strong>b</strong></em>cc<em><strong>a</strong></em> ，美丽值为 f('b') + f('a') = 2
b<em><strong>c</strong></em>c<em><strong>a</strong></em><strong> </strong>，美丽值为 f('c') + f('a') = 3
bc<em><strong>ca</strong></em> ，美丽值为 f('c') + f('a') = 3
总共有 4 个 k 子序列美丽值为最大值 3 。
所以答案为 4 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>s = "abbcd", k = 4
<b>输出：</b>2
<b>解释：</b><span style="white-space: normal">s 中我们有 f('a') = 1 ，f('b') = 2&nbsp;，f('c') = 1&nbsp;和</span> f('d') = 1 。
s 的 k 子序列为：
<em><strong>ab</strong></em>b<em><strong>cd</strong></em> ，美丽值为 f('a') + f('b') + f('c') + f('d') = 5
<span style="white-space: normal;"><b><i>a</i></b></span>b<em><strong>bcd</strong></em> ，美丽值为 f('a') + f('b') + f('c') + f('d') = 5 
总共有 2 个 k 子序列美丽值为最大值 5 。
所以答案为 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 哈希表
- 数学
- 字符串
- 组合数学

## 提示

1. Since every character appears once in a k-subsequence, we can solve the following problem first: Find the total number of ways to select <code>k</code> characters such that the sum of their frequencies is maximum.
2. An obvious case to eliminate is if <code>k</code> is greater than the number of distinct characters in <code>s</code>, then the answer is <code>0</code>.
3. We are now interested in the top frequencies among the characters. Using a map data structure, let <code>cnt[x]</code> denote the number of characters that have a frequency of <code>x</code>.
4. Starting from the maximum value <code>x</code> in <code>cnt</code>. Let <code>i = min(k, cnt[x])</code> we add to our result <code> <sup>cnt[x]</sup>C<sub>i</sub> * x<sup>i</sup></code> representing the number of ways to select <code>i</code> characters from all characters with frequency <code>x</code>, multiplied by the number of ways to choose each individual character. Subtract <code>i</code> from <code>k</code> and continue downwards to the next maximum value.
5. Powers, combinations, and additions should be done modulo <code>10<sup>9</sup> + 7</code>.

## 示例

```
"bcca"
2
"abbcd"
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countKSubsequencesWithMaxBeauty(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int countKSubsequencesWithMaxBeauty(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countKSubsequencesWithMaxBeauty(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        
```

### C

```c
int countKSubsequencesWithMaxBeauty(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountKSubsequencesWithMaxBeauty(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var countKSubsequencesWithMaxBeauty = function(s, k) {
    
};
```

### TypeScript

```typescript
function countKSubsequencesWithMaxBeauty(s: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function countKSubsequencesWithMaxBeauty($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countKSubsequencesWithMaxBeauty(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countKSubsequencesWithMaxBeauty(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countKSubsequencesWithMaxBeauty(String s, int k) {
    
  }
}
```

### Go

```golang
func countKSubsequencesWithMaxBeauty(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def count_k_subsequences_with_max_beauty(s, k)
    
end
```

### Scala

```scala
object Solution {
    def countKSubsequencesWithMaxBeauty(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_k_subsequences_with_max_beauty(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-k-subsequences-with-max-beauty s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_k_subsequences_with_max_beauty(S :: unicode:unicode_binary(), K :: integer()) -> integer().
count_k_subsequences_with_max_beauty(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_k_subsequences_with_max_beauty(s :: String.t, k :: integer) :: integer
  def count_k_subsequences_with_max_beauty(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countKSubsequencesWithMaxBeauty(s: String, k: Int64): Int64 {

    }
}
```

