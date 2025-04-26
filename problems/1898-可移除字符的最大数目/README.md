# 1898. 可移除字符的最大数目

## 题目描述

<p>给你两个字符串 <code>s</code> 和 <code>p</code> ，其中 <code>p</code> 是 <code>s</code> 的一个 <strong>子序列</strong> 。同时，给你一个元素 <strong>互不相同</strong> 且下标 <strong>从 0 开始</strong> 计数的整数数组 <code>removable</code> ，该数组是 <code>s</code> 中下标的一个子集（<code>s</code> 的下标也 <strong>从 0 开始</strong> 计数）。</p>

<p>请你找出一个整数 <code>k</code>（<code>0 <= k <= removable.length</code>），选出 <code>removable</code> 中的 <strong>前</strong> <code>k</code> 个下标，然后从 <code>s</code> 中移除这些下标对应的 <code>k</code> 个字符。整数 <code>k</code> 需满足：在执行完上述步骤后， <code>p</code> 仍然是 <code>s</code> 的一个 <strong>子序列</strong> 。更正式的解释是，对于每个 <code>0 <= i < k</code> ，先标记出位于 <code>s[removable[i]]</code> 的字符，接着移除所有标记过的字符，然后检查 <code>p</code> 是否仍然是 <code>s</code> 的一个子序列。</p>

<p>返回你可以找出的 <strong>最大</strong><em> </em><code>k</code><em> </em>，满足在移除字符后<em> </em><code>p</code><em> </em>仍然是 <code>s</code> 的一个子序列。</p>

<p>字符串的一个 <strong>子序列</strong> 是一个由原字符串生成的新字符串，生成过程中可能会移除原字符串中的一些字符（也可能不移除）但不改变剩余字符之间的相对顺序。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abcacb", p = "ab", removable = [3,1,0]
<strong>输出：</strong>2
<strong>解释：</strong>在移除下标 3 和 1 对应的字符后，"a<strong>b</strong>c<strong>a</strong>cb" 变成 "accb" 。
"ab" 是 "<strong>a</strong>cc<strong>b</strong>" 的一个子序列。
如果移除下标 3、1 和 0 对应的字符后，"<strong>ab</strong>c<strong>a</strong>cb" 变成 "ccb" ，那么 "ab" 就不再是 s 的一个子序列。
因此，最大的 k 是 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
<strong>输出：</strong>1
<strong>解释：</strong>在移除下标 3 对应的字符后，"abc<strong>b</strong>ddddd" 变成 "abcddddd" 。
"abcd" 是 "<strong>abcd</strong>dddd" 的一个子序列。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "abcab", p = "abc", removable = [0,1,2,3,4]
<strong>输出：</strong>0
<strong>解释：</strong>如果移除数组 removable 的第一个下标，"abc" 就不再是 s 的一个子序列。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= p.length <= s.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= removable.length < s.length</code></li>
	<li><code>0 <= removable[i] < s.length</code></li>
	<li><code>p</code> 是 <code>s</code> 的一个 <strong>子字符串</strong></li>
	<li><code>s</code> 和 <code>p</code> 都由小写英文字母组成</li>
	<li><code>removable</code> 中的元素 <strong>互不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 字符串
- 二分查找

## 提示

1. First, we need to think about solving an easier problem, If we remove a set of indices from the string does P exist in S as a subsequence
2. We can binary search the K and check by solving the above problem.

## 示例

```
"abcacb"
"ab"
[3,1,0]
"abcbddddd"
"abcd"
[3,2,1,4,5,6]
"abcab"
"abc"
[0,1,2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumRemovals(string s, string p, vector<int>& removable) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumRemovals(String s, String p, int[] removable) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
```

### C

```c
int maximumRemovals(char* s, char* p, int* removable, int removableSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumRemovals(string s, string p, int[] removable) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} p
 * @param {number[]} removable
 * @return {number}
 */
var maximumRemovals = function(s, p, removable) {
    
};
```

### TypeScript

```typescript
function maximumRemovals(s: string, p: string, removable: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $p
     * @param Integer[] $removable
     * @return Integer
     */
    function maximumRemovals($s, $p, $removable) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumRemovals(_ s: String, _ p: String, _ removable: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumRemovals(s: String, p: String, removable: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumRemovals(String s, String p, List<int> removable) {
    
  }
}
```

### Go

```golang
func maximumRemovals(s string, p string, removable []int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} p
# @param {Integer[]} removable
# @return {Integer}
def maximum_removals(s, p, removable)
    
end
```

### Scala

```scala
object Solution {
    def maximumRemovals(s: String, p: String, removable: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_removals(s: String, p: String, removable: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-removals s p removable)
  (-> string? string? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_removals(S :: unicode:unicode_binary(), P :: unicode:unicode_binary(), Removable :: [integer()]) -> integer().
maximum_removals(S, P, Removable) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_removals(s :: String.t, p :: String.t, removable :: [integer]) :: integer
  def maximum_removals(s, p, removable) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumRemovals(s: String, p: String, removable: Array<Int64>): Int64 {

    }
}
```

