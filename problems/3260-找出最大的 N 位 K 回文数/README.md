# 3260. 找出最大的 N 位 K 回文数

## 题目描述

<p>给你两个 <strong>正整数</strong> <code>n</code> 和 <code>k</code>。</p>

<p>如果整数 <code>x</code> 满足以下全部条件，则该整数是一个 <strong>k 回文数</strong>：</p>

<ul>
	<li><code>x</code> 是一个 <span data-keyword="palindrome-integer">回文数</span>。</li>
	<li><code>x</code> 可以被 <code>k</code> 整除。</li>
</ul>

<p>以字符串形式返回 <strong>最大的&nbsp;</strong> <code>n</code> 位 <strong>k 回文数</strong>。</p>

<p><strong>注意</strong>，该整数 <strong>不 </strong>含前导零。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 3, k = 5</span></p>

<p><strong>输出：</strong> <span class="example-io">"595"</span></p>

<p><strong>解释：</strong></p>

<p>595 是最大的 3 位 k 回文数。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 1, k = 4</span></p>

<p><strong>输出：</strong> <span class="example-io">"8"</span></p>

<p><strong>解释：</strong></p>

<p>1 位 k 回文数只有 4 和 8。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 5, k = 6</span></p>

<p><strong>输出：</strong> <span class="example-io">"89898"</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 9</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数学
- 字符串
- 动态规划
- 数论

## 提示

1. It must have a solution since we can have all digits equal to <code>k</code>.
2. Use string dp, store modulus along with length of number currently formed.
3. Is it possible to solve greedily using divisibility rules?

## 示例

```
3
5
1
4
5
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string largestPalindrome(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String largestPalindrome(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestPalindrome(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        
```

### C

```c
char* largestPalindrome(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string LargestPalindrome(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var largestPalindrome = function(n, k) {
    
};
```

### TypeScript

```typescript
function largestPalindrome(n: number, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function largestPalindrome($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestPalindrome(_ n: Int, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestPalindrome(n: Int, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String largestPalindrome(int n, int k) {
    
  }
}
```

### Go

```golang
func largestPalindrome(n int, k int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {String}
def largest_palindrome(n, k)
    
end
```

### Scala

```scala
object Solution {
    def largestPalindrome(n: Int, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_palindrome(n: i32, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (largest-palindrome n k)
  (-> exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec largest_palindrome(N :: integer(), K :: integer()) -> unicode:unicode_binary().
largest_palindrome(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_palindrome(n :: integer, k :: integer) :: String.t
  def largest_palindrome(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestPalindrome(n: Int64, k: Int64): String {

    }
}
```

