# 903. DI 序列的有效排列

## 题目描述

<p>给定一个长度为 <code>n</code> 的字符串 <code>s</code> ，其中 <code>s[i]</code> 是:</p>

<ul>
	<li><code>“D”</code> 意味着减少，或者</li>
	<li><code>“I”</code> 意味着增加</li>
</ul>

<p><strong>有效排列</strong>&nbsp;是对有&nbsp;<code>n + 1</code>&nbsp;个在&nbsp;<code>[0, n]</code>&nbsp; 范围内的整数的一个排列&nbsp;<code>perm</code>&nbsp;，使得对所有的&nbsp;<code>i</code>：</p>

<ul>
	<li>如果 <code>s[i] == 'D'</code>，那么&nbsp;<code>perm[i] &gt; perm[i+1]</code>，以及；</li>
	<li>如果 <code>s[i] == 'I'</code>，那么 <code>perm[i] &lt; perm[i+1]</code>。</li>
</ul>

<p>返回 <em><strong>有效排列 </strong>&nbsp;</em><code>perm</code><em>的数量 </em>。因为答案可能很大，所以请<strong>返回你的答案对</strong>&nbsp;<code>10<sup>9</sup>&nbsp;+ 7</code><strong>&nbsp;取余</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "DID"
<strong>输出：</strong>5
<strong>解释：</strong>
(0, 1, 2, 3) 的五个有效排列是：
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> s = "D"
<strong>输出:</strong> 1
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>n == s.length</code></li>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>s[i]</code>&nbsp;不是&nbsp;<code>'I'</code>&nbsp;就是&nbsp;<code>'D'</code></li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划
- 前缀和

## 示例

```
"DID"
"D"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numPermsDISequence(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int numPermsDISequence(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numPermsDISequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        
```

### C

```c
int numPermsDISequence(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumPermsDISequence(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numPermsDISequence = function(s) {
    
};
```

### TypeScript

```typescript
function numPermsDISequence(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numPermsDISequence($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numPermsDISequence(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numPermsDISequence(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numPermsDISequence(String s) {
    
  }
}
```

### Go

```golang
func numPermsDISequence(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def num_perms_di_sequence(s)
    
end
```

### Scala

```scala
object Solution {
    def numPermsDISequence(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_perms_di_sequence(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-perms-di-sequence s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_perms_di_sequence(S :: unicode:unicode_binary()) -> integer().
num_perms_di_sequence(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_perms_di_sequence(s :: String.t) :: integer
  def num_perms_di_sequence(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numPermsDISequence(s: String): Int64 {

    }
}
```

