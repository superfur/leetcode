# 2522. 将字符串分割成值不超过 K 的子字符串

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，它每一位都是&nbsp;<code>1</code>&nbsp;到&nbsp;<code>9</code>&nbsp;之间的数字组成，同时给你一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>如果一个字符串 <code>s</code>&nbsp;的分割满足以下条件，我们称它是一个 <strong>好</strong>&nbsp;分割：</p>

<ul>
	<li><code>s</code>&nbsp;中每个数位 <strong>恰好</strong>&nbsp;属于一个子字符串。</li>
	<li>每个子字符串的值都小于等于&nbsp;<code>k</code>&nbsp;。</li>
</ul>

<p>请你返回 <code>s</code>&nbsp;所有的 <strong>好</strong>&nbsp;分割中，子字符串的&nbsp;<strong>最少</strong>&nbsp;数目。如果不存在 <code>s</code>&nbsp;的<strong>&nbsp;好</strong>&nbsp;分割，返回&nbsp;<code>-1</code>&nbsp;。</p>

<p><b>注意：</b></p>

<ul>
	<li>一个字符串的 <strong>值</strong>&nbsp;是这个字符串对应的整数。比方说，<code>"123"</code>&nbsp;的值为&nbsp;<code>123</code>&nbsp;，<code>"1"</code>&nbsp;的值是&nbsp;<code>1</code>&nbsp;。</li>
	<li><strong>子字符串</strong>&nbsp;是字符串中一段连续的字符序列。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "165462", k = 60
<b>输出：</b>4
<b>解释：</b>我们将字符串分割成子字符串 "16" ，"54" ，"6" 和 "2" 。每个子字符串的值都小于等于 k = 60 。
不存在小于 4 个子字符串的好分割。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "238182", k = 5
<b>输出：</b>-1
<strong>解释：</strong>这个字符串不存在好分割。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code>&nbsp;是&nbsp;<code>'1'</code>&nbsp;到&nbsp;<code>'9'</code>&nbsp;之间的数字。</li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串
- 动态规划

## 示例

```
"165462"
60
"238182"
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumPartition(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumPartition(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumPartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        
```

### C

```c
int minimumPartition(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumPartition(string s, int k) {
        
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
var minimumPartition = function(s, k) {
    
};
```

### TypeScript

```typescript
function minimumPartition(s: string, k: number): number {
    
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
    function minimumPartition($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumPartition(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumPartition(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumPartition(String s, int k) {
    
  }
}
```

### Go

```golang
func minimumPartition(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def minimum_partition(s, k)
    
end
```

### Scala

```scala
object Solution {
    def minimumPartition(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_partition(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-partition s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_partition(S :: unicode:unicode_binary(), K :: integer()) -> integer().
minimum_partition(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_partition(s :: String.t, k :: integer) :: integer
  def minimum_partition(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumPartition(s: String, k: Int64): Int64 {

    }
}
```

