# 1531. 压缩字符串 II

## 题目描述

<p><a href="https://baike.baidu.com/item/%E8%A1%8C%E7%A8%8B%E9%95%BF%E5%BA%A6%E7%BC%96%E7%A0%81/2931940?fr=aladdin" target="_blank">行程长度编码</a> 是一种常用的字符串压缩方法，它将连续的相同字符（重复 2 次或更多次）替换为字符和表示字符计数的数字（行程长度）。例如，用此方法压缩字符串 <code>&quot;aabccc&quot;</code> ，将 <code>&quot;aa&quot;</code> 替换为 <code>&quot;a2&quot;</code> ，<code>&quot;ccc&quot;</code> 替换为` <code>&quot;c3&quot;</code> 。因此压缩后的字符串变为 <code>&quot;a2bc3&quot;</code> 。</p>

<p>注意，本问题中，压缩时没有在单个字符后附加计数 <code>&#39;1&#39;</code> 。</p>

<p>给你一个字符串 <code>s</code> 和一个整数 <code>k</code> 。你需要从字符串 <code>s</code> 中删除最多 <code>k</code> 个字符，以使 <code>s</code> 的行程长度编码长度最小。</p>

<p>请你返回删除最多 <code>k</code> 个字符后，<code>s</code> <strong>行程长度编码的最小长度</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;aaabcccd&quot;, k = 2
<strong>输出：</strong>4
<strong>解释：</strong>在不删除任何内容的情况下，压缩后的字符串是 &quot;a3bc3d&quot; ，长度为 6 。最优的方案是删除 &#39;b&#39; 和 &#39;d&#39;，这样一来，压缩后的字符串为 &quot;a3c3&quot; ，长度是 4 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;aabbaa&quot;, k = 2
<strong>输出：</strong>2
<strong>解释：</strong>如果删去两个 &#39;b&#39; 字符，那么压缩后的字符串是长度为 2 的 &quot;a4&quot; 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;aaaaaaaaaaa&quot;, k = 0
<strong>输出：</strong>3
<strong>解释：</strong>由于 k 等于 0 ，不能删去任何字符。压缩后的字符串是 &quot;a11&quot; ，长度为 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
	<li><code>s</code> 仅包含小写英文字母</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. Use dynamic programming.
2. The state of the DP can be the current index and the remaining characters to delete.
3. Having a prefix sum for each character can help you determine for a certain character c in some specific range, how many characters you need to delete to merge all occurrences of c in that range.

## 示例

```
"aaabcccd"
2
"aabbaa"
2
"aaaaaaaaaaa"
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getLengthOfOptimalCompression(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int getLengthOfOptimalCompression(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
```

### C

```c
int getLengthOfOptimalCompression(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetLengthOfOptimalCompression(string s, int k) {
        
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
var getLengthOfOptimalCompression = function(s, k) {
    
};
```

### TypeScript

```typescript
function getLengthOfOptimalCompression(s: string, k: number): number {
    
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
    function getLengthOfOptimalCompression($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getLengthOfOptimalCompression(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getLengthOfOptimalCompression(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getLengthOfOptimalCompression(String s, int k) {
    
  }
}
```

### Go

```golang
func getLengthOfOptimalCompression(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def get_length_of_optimal_compression(s, k)
    
end
```

### Scala

```scala
object Solution {
    def getLengthOfOptimalCompression(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_length_of_optimal_compression(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-length-of-optimal-compression s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec get_length_of_optimal_compression(S :: unicode:unicode_binary(), K :: integer()) -> integer().
get_length_of_optimal_compression(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_length_of_optimal_compression(s :: String.t, k :: integer) :: integer
  def get_length_of_optimal_compression(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getLengthOfOptimalCompression(s: String, k: Int64): Int64 {

    }
}
```

