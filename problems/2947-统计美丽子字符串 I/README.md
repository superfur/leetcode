# 2947. 统计美丽子字符串 I

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个正整数 <code>k</code> 。</p>

<p>用 <code>vowels</code> 和 <code>consonants</code> 分别表示字符串中元音字母和辅音字母的数量。</p>

<p>如果某个字符串满足以下条件，则称其为 <strong>美丽字符串</strong> ：</p>

<ul>
	<li><code>vowels == consonants</code>，即元音字母和辅音字母的数量相等。</li>
	<li><code>(vowels * consonants) % k == 0</code>，即元音字母和辅音字母的数量的乘积能被 <code>k</code> 整除。</li>
</ul>

<p>返回字符串 <code>s</code> 中 <strong>非空美丽子字符串</strong> 的数量。</p>

<p>子字符串是字符串中的一个连续字符序列。</p>

<p>英语中的<strong> 元音字母 </strong>为 <code>'a'</code>、<code>'e'</code>、<code>'i'</code>、<code>'o'</code> 和 <code>'u'</code> 。</p>

<p>英语中的<strong> 辅音字母 </strong>为除了元音字母之外的所有字母。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "baeyh", k = 2
<strong>输出：</strong>2
<strong>解释：</strong>字符串 s 中有 2 个美丽子字符串。
- 子字符串 "b<em><strong>aeyh</strong></em>"，vowels = 2（["a","e"]），consonants = 2（["y","h"]）。
可以看出字符串 "aeyh" 是美丽字符串，因为 vowels == consonants 且 vowels * consonants % k == 0 。
- 子字符串 "<em><strong>baey</strong></em>h"，vowels = 2（["a","e"]），consonants = 2（["b","y"]）。
可以看出字符串 "baey" 是美丽字符串，因为 vowels == consonants 且 vowels * consonants % k == 0 。
可以证明字符串 s 中只有 2 个美丽子字符串。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abba", k = 1
<strong>输出：</strong>3
<strong>解释：</strong>字符串 s 中有 3 个美丽子字符串。
- 子字符串 "<strong><em>ab</em></strong>ba"，vowels = 1（["a"]），consonants = 1（["b"]）。
- 子字符串 "ab<strong><em>ba</em></strong>"，vowels = 1（["a"]），consonants = 1（["b"]）。
- 子字符串 "<em><strong>abba</strong></em>"，vowels = 2（["a","a"]），consonants = 2（["b","b"]）。
可以证明字符串 s 中只有 3 个美丽子字符串。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "bcdf", k = 1
<strong>输出：</strong>0
<strong>解释：</strong>字符串 s 中没有美丽子字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 数学
- 字符串
- 枚举
- 数论
- 前缀和

## 提示

1. Iterate over all substrings and maintain the frequencies of vowels and consonants.

## 示例

```
"baeyh"
2
"abba"
1
"bcdf"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int beautifulSubstrings(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int beautifulSubstrings(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def beautifulSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
```

### C

```c
int beautifulSubstrings(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int BeautifulSubstrings(string s, int k) {
        
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
var beautifulSubstrings = function(s, k) {
    
};
```

### TypeScript

```typescript
function beautifulSubstrings(s: string, k: number): number {
    
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
    function beautifulSubstrings($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func beautifulSubstrings(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun beautifulSubstrings(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int beautifulSubstrings(String s, int k) {
    
  }
}
```

### Go

```golang
func beautifulSubstrings(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def beautiful_substrings(s, k)
    
end
```

### Scala

```scala
object Solution {
    def beautifulSubstrings(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn beautiful_substrings(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (beautiful-substrings s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec beautiful_substrings(S :: unicode:unicode_binary(), K :: integer()) -> integer().
beautiful_substrings(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec beautiful_substrings(s :: String.t, k :: integer) :: integer
  def beautiful_substrings(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func beautifulSubstrings(s: String, k: Int64): Int64 {

    }
}
```

