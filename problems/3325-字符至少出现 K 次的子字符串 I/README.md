# 3325. 字符至少出现 K 次的子字符串 I

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个整数 <code>k</code>，在 <code>s</code> 的所有子字符串中，请你统计并返回 <strong>至少有一个 </strong>字符 <strong>至少出现</strong> <code>k</code> 次的子字符串总数。</p>

<p><strong>子字符串 </strong>是字符串中的一个连续、<b> 非空</b> 的字符序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "abacb", k = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>符合条件的子字符串如下：</p>

<ul>
	<li><code>"aba"</code>（字符 <code>'a'</code> 出现 2 次）。</li>
	<li><code>"abac"</code>（字符 <code>'a'</code> 出现 2 次）。</li>
	<li><code>"abacb"</code>（字符 <code>'a'</code> 出现 2 次）。</li>
	<li><code>"bacb"</code>（字符 <code>'b'</code> 出现 2 次）。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "abcde", k = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">15</span></p>

<p><strong>解释：</strong></p>

<p>所有子字符串都有效，因为每个字符至少出现一次。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3000</code></li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 提示

1. Fix the <code>left</code> index of the substring.
2. For the fixed <code>left</code> index, find the first <code>right</code> index for which substring <code>s[left..right]</code> satisfies the condition.
3. Every substring that starts at <code>left</code> and ends after <code>right</code> satisfies the condition.

## 示例

```
"abacb"
2
"abcde"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfSubstrings(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfSubstrings(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        
```

### C

```c
int numberOfSubstrings(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfSubstrings(string s, int k) {
        
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
var numberOfSubstrings = function(s, k) {
    
};
```

### TypeScript

```typescript
function numberOfSubstrings(s: string, k: number): number {
    
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
    function numberOfSubstrings($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfSubstrings(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfSubstrings(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfSubstrings(String s, int k) {
    
  }
}
```

### Go

```golang
func numberOfSubstrings(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def number_of_substrings(s, k)
    
end
```

### Scala

```scala
object Solution {
    def numberOfSubstrings(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_substrings(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-substrings s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_substrings(S :: unicode:unicode_binary(), K :: integer()) -> integer().
number_of_substrings(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_substrings(s :: String.t, k :: integer) :: integer
  def number_of_substrings(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfSubstrings(s: String, k: Int64): Int64 {

    }
}
```

