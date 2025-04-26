# 3003. 执行操作后的最大分割数量

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串&nbsp;<code>s</code>&nbsp;和一个整数&nbsp;<code>k</code>。</p>

<p>你需要执行以下分割操作，直到字符串&nbsp;<code>s&nbsp;</code>变为&nbsp;<strong>空</strong>：</p>

<ul>
	<li>选择&nbsp;<code>s</code>&nbsp;的最长&nbsp;<strong>前缀</strong>，该前缀最多包含&nbsp;<code>k&nbsp;</code>个&nbsp;<strong>不同&nbsp;</strong>字符。</li>
	<li><strong>删除&nbsp;</strong>这个前缀，并将分割数量加一。如果有剩余字符，它们在&nbsp;<code>s</code>&nbsp;中保持原来的顺序。</li>
</ul>

<p>执行操作之 <strong>前</strong> ，你可以将&nbsp;<code>s</code>&nbsp;中&nbsp;<strong>至多一处 </strong>下标的对应字符更改为另一个小写英文字母。</p>

<p>在最优选择情形下改变至多一处下标对应字符后，用整数表示并返回操作结束时得到的 <strong>最大</strong> 分割数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "accca", k = 2</span></p>

<p><strong>输出：</strong><span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>最好的方式是把&nbsp;<code>s[2]</code>&nbsp;变为除了 a 和 c 之外的东西，比如&nbsp;b。然后它变成了&nbsp;<code>"acbca"</code>。</p>

<p>然后我们执行以下操作：</p>

<ol>
	<li>最多包含 2 个不同字符的最长前缀是 <code>"ac"</code>，我们删除它然后&nbsp;<code>s</code> 变为&nbsp;<code>"bca"</code>。</li>
	<li>现在最多包含 2 个不同字符的最长前缀是&nbsp;<code>"bc"</code>，所以我们删除它然后&nbsp;<code>s</code> 变为&nbsp;<code>"a"</code>。</li>
	<li>最后，我们删除&nbsp;<code>"a"</code>&nbsp;并且&nbsp;<code>s</code>&nbsp;变成空串，所以该过程结束。</li>
</ol>

<p>进行操作时，字符串被分成 3 个部分，所以答案是 3。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "aabaab", k = 3</span></p>

<p><strong>输出：</strong><span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>一开始&nbsp;<code>s</code>&nbsp;包含 2 个不同的字符，所以无论我们改变哪个，&nbsp;它最多包含 3 个不同字符，因此最多包含 3 个不同字符的最长前缀始终是所有字符，因此答案是 1。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "xxyz", k = 1</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><strong>解释：</strong></p>

<p>最好的方式是将&nbsp;<code>s[0]</code>&nbsp;或&nbsp;<code>s[1]</code>&nbsp;变为&nbsp;<code>s</code>&nbsp;中字符以外的东西，例如将&nbsp;<code>s[0]</code>&nbsp;变为&nbsp;<code>w</code>。</p>

<p>然后&nbsp;<code>s</code>&nbsp;变为&nbsp;<code>"wxyz"</code>，包含 4 个不同的字符，所以当&nbsp;<code>k</code>&nbsp;为 1，它将分为 4 个部分。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
	<li><code>1 &lt;= k &lt;= 26</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 字符串
- 动态规划
- 状态压缩

## 提示

1. For each position, try to brute-force the replacements.
2. To speed up the brute-force solution, we can precompute the following (without changing any index) using prefix sums and binary search:<ul>
<li><code>pref[i]</code>: The number of resulting partitions from the operations by performing the operations on <code>s[0:i]</code>.</li>
<li><code>suff[i]</code>: The number of resulting partitions from the operations by performing the operations on <code>s[i:n - 1]</code>, where <code>n == s.length</code>.</li>
<li><code>partition_start[i]</code>: The start index of the partition containing the <code>i<sup>th</sup></code> index after performing the operations.</li>
</ul>
3. Now, for a position <code>i</code>, we can try all possible <code>25</code> replacements:<br />
For a replacement, using prefix sums and binary search, we need to find the rightmost index, <code>r</code>, such that the number of distinct characters in the range <code>[partition_start[i], r]</code> is at most <code>k</code>.<br />
There are <code>2</code> cases:<ul>
<li><code>r >= i</code>: the number of resulting partitions in this case is <code>1 + pref[partition_start[i] - 1] + suff[r + 1]</code>.</li>
<li>Otherwise, we need to find the rightmost index <code>r<sub>2</sub></code> such that the number of distinct characters in the range <code>[r:r<sub>2</sub>]</code> is at most <code>k</code>. The answer in this case is <code>2 + pref[partition_start[i] - 1] + suff[r<sub>2</sub> + 1]</code></li>
</ul>
4. The answer is the maximum among all replacements.

## 示例

```
"accca"
2
"aabaab"
3
"xxyz"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxPartitionsAfterOperations(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxPartitionsAfterOperations(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxPartitionsAfterOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        
```

### C

```c
int maxPartitionsAfterOperations(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxPartitionsAfterOperations(string s, int k) {
        
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
var maxPartitionsAfterOperations = function(s, k) {
    
};
```

### TypeScript

```typescript
function maxPartitionsAfterOperations(s: string, k: number): number {
    
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
    function maxPartitionsAfterOperations($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxPartitionsAfterOperations(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxPartitionsAfterOperations(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxPartitionsAfterOperations(String s, int k) {
    
  }
}
```

### Go

```golang
func maxPartitionsAfterOperations(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_partitions_after_operations(s, k)
    
end
```

### Scala

```scala
object Solution {
    def maxPartitionsAfterOperations(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_partitions_after_operations(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-partitions-after-operations s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_partitions_after_operations(S :: unicode:unicode_binary(), K :: integer()) -> integer().
max_partitions_after_operations(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_partitions_after_operations(s :: String.t, k :: integer) :: integer
  def max_partitions_after_operations(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxPartitionsAfterOperations(s: String, k: Int64): Int64 {

    }
}
```

