# 2002. 两个回文子序列长度的最大乘积

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，请你找到&nbsp;<code>s</code>&nbsp;中两个&nbsp;<strong>不相交回文子序列</strong>&nbsp;，使得它们长度的&nbsp;<strong>乘积最大</strong>&nbsp;。两个子序列在原字符串中如果没有任何相同下标的字符，则它们是&nbsp;<strong>不相交</strong>&nbsp;的。</p>

<p>请你返回两个回文子序列长度可以达到的<strong>&nbsp;最大乘积</strong>&nbsp;。</p>

<p><strong>子序列</strong>&nbsp;指的是从原字符串中删除若干个字符（可以一个也不删除）后，剩余字符不改变顺序而得到的结果。如果一个字符串从前往后读和从后往前读一模一样，那么这个字符串是一个 <strong>回文字符串</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="example-1" src="https://assets.leetcode.com/uploads/2021/08/24/two-palindromic-subsequences.png" style="width: 550px; height: 124px;"></p>

<pre><b>输入：</b>s = "leetcodecom"
<b>输出：</b>9
<b>解释：</b>最优方案是选择 "ete" 作为第一个子序列，"cdc" 作为第二个子序列。
它们的乘积为 3 * 3 = 9 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "bb"
<b>输出：</b>1
<b>解释：</b>最优方案为选择 "b" （第一个字符）作为第一个子序列，"b" （第二个字符）作为第二个子序列。
它们的乘积为 1 * 1 = 1 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>s = "accbcaxxcxx"
<b>输出：</b>25
<b>解释：</b>最优方案为选择 "accca" 作为第一个子序列，"xxcxx" 作为第二个子序列。
它们的乘积为 5 * 5 = 25 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 12</code></li>
	<li><code>s</code>&nbsp;只含有小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 字符串
- 动态规划
- 回溯
- 状态压缩

## 提示

1. Could you generate all possible pairs of disjoint subsequences?
2. Could you find the maximum length palindrome in each subsequence for a pair of disjoint subsequences?

## 示例

```
"leetcodecom"
"bb"
"accbcaxxcxx"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxProduct(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxProduct(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxProduct(self, s: str) -> int:
        
```

### C

```c
int maxProduct(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxProduct(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxProduct = function(s) {
    
};
```

### TypeScript

```typescript
function maxProduct(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxProduct($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxProduct(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxProduct(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxProduct(String s) {
    
  }
}
```

### Go

```golang
func maxProduct(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def max_product(s)
    
end
```

### Scala

```scala
object Solution {
    def maxProduct(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_product(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-product s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_product(S :: unicode:unicode_binary()) -> integer().
max_product(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_product(s :: String.t) :: integer
  def max_product(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxProduct(s: String): Int64 {

    }
}
```

