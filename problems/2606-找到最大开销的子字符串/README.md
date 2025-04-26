# 2606. 找到最大开销的子字符串

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，一个字符&nbsp;<strong>互不相同</strong>&nbsp;的字符串&nbsp;<code>chars</code>&nbsp;和一个长度与 <code>chars</code>&nbsp;相同的整数数组&nbsp;<code>vals</code>&nbsp;。</p>

<p><strong>子字符串的开销</strong>&nbsp;是一个子字符串中所有字符对应价值之和。空字符串的开销是 <code>0</code>&nbsp;。</p>

<p><strong>字符的价值</strong>&nbsp;定义如下：</p>

<ul>
	<li>如果字符不在字符串&nbsp;<code>chars</code>&nbsp;中，那么它的价值是它在字母表中的位置（下标从 <strong>1</strong>&nbsp;开始）。

	<ul>
		<li>比方说，<code>'a'</code>&nbsp;的价值为&nbsp;<code>1</code>&nbsp;，<code>'b'</code>&nbsp;的价值为&nbsp;<code>2</code>&nbsp;，以此类推，<code>'z'</code>&nbsp;的价值为&nbsp;<code>26</code>&nbsp;。</li>
	</ul>
	</li>
	<li>否则，如果这个字符在 <code>chars</code>&nbsp;中的位置为 <code>i</code>&nbsp;，那么它的价值就是&nbsp;<code>vals[i]</code>&nbsp;。</li>
</ul>

<p>请你返回字符串 <code>s</code>&nbsp;的所有子字符串中的最大开销。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "adaa", chars = "d", vals = [-1000]
<b>输出：</b>2
<b>解释：</b>字符 "a" 和 "d" 的价值分别为 1 和 -1000 。
最大开销子字符串是 "aa" ，它的开销为 1 + 1 = 2 。
2 是最大开销。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "abc", chars = "abc", vals = [-1,-1,-1]
<b>输出：</b>0
<b>解释：</b>字符 "a" ，"b" 和 "c" 的价值分别为 -1 ，-1 和 -1 。
最大开销子字符串是 "" ，它的开销为 0 。
0 是最大开销。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
	<li><code>1 &lt;= chars.length &lt;= 26</code></li>
	<li><code>chars</code>&nbsp;只包含小写英文字母，且 <strong>互不相同</strong>&nbsp;。</li>
	<li><code>vals.length == chars.length</code></li>
	<li><code>-1000 &lt;= vals[i] &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 动态规划

## 提示

1. Create a new integer array where arr[i] denotes the value of character s[i].
2. We can use Kadane’s maximum subarray sum algorithm to find the maximum cost.

## 示例

```
"adaa"
"d"
[-1000]
"abc"
"abc"
[-1,-1,-1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumCostSubstring(String s, String chars, int[] vals) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumCostSubstring(self, s, chars, vals):
        """
        :type s: str
        :type chars: str
        :type vals: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        
```

### C

```c
int maximumCostSubstring(char* s, char* chars, int* vals, int valsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumCostSubstring(string s, string chars, int[] vals) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} chars
 * @param {number[]} vals
 * @return {number}
 */
var maximumCostSubstring = function(s, chars, vals) {
    
};
```

### TypeScript

```typescript
function maximumCostSubstring(s: string, chars: string, vals: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $chars
     * @param Integer[] $vals
     * @return Integer
     */
    function maximumCostSubstring($s, $chars, $vals) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumCostSubstring(_ s: String, _ chars: String, _ vals: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumCostSubstring(s: String, chars: String, vals: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumCostSubstring(String s, String chars, List<int> vals) {
    
  }
}
```

### Go

```golang
func maximumCostSubstring(s string, chars string, vals []int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} chars
# @param {Integer[]} vals
# @return {Integer}
def maximum_cost_substring(s, chars, vals)
    
end
```

### Scala

```scala
object Solution {
    def maximumCostSubstring(s: String, chars: String, vals: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_cost_substring(s: String, chars: String, vals: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-cost-substring s chars vals)
  (-> string? string? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_cost_substring(S :: unicode:unicode_binary(), Chars :: unicode:unicode_binary(), Vals :: [integer()]) -> integer().
maximum_cost_substring(S, Chars, Vals) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_cost_substring(s :: String.t, chars :: String.t, vals :: [integer]) :: integer
  def maximum_cost_substring(s, chars, vals) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumCostSubstring(s: String, chars: String, vals: Array<Int64>): Int64 {

    }
}
```

