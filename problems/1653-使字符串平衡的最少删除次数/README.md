# 1653. 使字符串平衡的最少删除次数

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，它仅包含字符&nbsp;<code>'a'</code> 和&nbsp;<code>'b'</code>​​​​ 。</p>

<p>你可以删除&nbsp;<code>s</code>&nbsp;中任意数目的字符，使得&nbsp;<code>s</code> <strong>平衡</strong>&nbsp;。当不存在下标对&nbsp;<code>(i,j)</code>&nbsp;满足&nbsp;<code>i &lt; j</code> ，且&nbsp;<code>s[i] = 'b'</code> 的同时&nbsp;<code>s[j]= 'a'</code> ，此时认为 <code>s</code> 是 <strong>平衡 </strong>的。</p>

<p>请你返回使 <code>s</code>&nbsp;<strong>平衡</strong>&nbsp;的 <strong>最少</strong>&nbsp;删除次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "aababbab"
<b>输出：</b>2
<b>解释：</b>你可以选择以下任意一种方案：
下标从 0 开始，删除第 2 和第 6 个字符（"aa<strong>b</strong>abb<strong>a</strong>b" -&gt; "aaabbb"），
下标从 0 开始，删除第 3 和第 6 个字符（"aab<strong>a</strong>bb<strong>a</strong>b" -&gt; "aabbbb"）。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "bbaaaaabb"
<b>输出：</b>2
<b>解释：</b>唯一的最优解是删除最前面两个字符。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code>&nbsp;要么是&nbsp;<code>'a'</code> 要么是&nbsp;<code>'b'</code>​<strong>&nbsp;</strong>。​</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 字符串
- 动态规划

## 提示

1. You need to find for every index the number of Bs before it and the number of A's after it
2. You can speed up the finding of A's and B's in suffix and prefix using preprocessing

## 示例

```
"aababbab"
"bbaaaaabb"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumDeletions(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumDeletions(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumDeletions(self, s: str) -> int:
        
```

### C

```c
int minimumDeletions(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumDeletions(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumDeletions = function(s) {
    
};
```

### TypeScript

```typescript
function minimumDeletions(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumDeletions($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumDeletions(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumDeletions(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumDeletions(String s) {
    
  }
}
```

### Go

```golang
func minimumDeletions(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def minimum_deletions(s)
    
end
```

### Scala

```scala
object Solution {
    def minimumDeletions(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_deletions(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-deletions s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_deletions(S :: unicode:unicode_binary()) -> integer().
minimum_deletions(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_deletions(s :: String.t) :: integer
  def minimum_deletions(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumDeletions(s: String): Int64 {

    }
}
```

