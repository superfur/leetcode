# 3144. 分割字符频率相等的最少子字符串

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，你需要将它分割成一个或者更多的&nbsp;<strong>平衡</strong>&nbsp;子字符串。比方说，<code>s == "ababcc"</code>&nbsp;那么&nbsp;<code>("abab", "c", "c")</code>&nbsp;，<code>("ab", "abc", "c")</code>&nbsp;和&nbsp;<code>("ababcc")</code>&nbsp;都是合法分割，但是&nbsp;<code>("a", <strong>"bab"</strong>, "cc")</code>&nbsp;，<code>(<strong>"aba"</strong>, "bc", "c")</code>&nbsp;和&nbsp;<code>("ab", <strong>"abcc"</strong>)</code>&nbsp;不是，不平衡的子字符串用粗体表示。</p>

<p>请你返回 <code>s</code>&nbsp;<strong>最少</strong> 能分割成多少个平衡子字符串。</p>

<p><b>注意：</b>一个 <strong>平衡</strong>&nbsp;字符串指的是字符串中所有字符出现的次数都相同。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "fabccddg"</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p>我们可以将 <code>s</code>&nbsp;分割成 3 个子字符串：<code>("fab, "ccdd", "g")</code>&nbsp;或者&nbsp;<code>("fabc", "cd", "dg")</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "abababaccddb"</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>我们可以将&nbsp;<code>s</code>&nbsp;分割成 2 个子字符串：<code>("abab", "abaccddb")</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 动态规划
- 计数

## 提示

1. Let <code>dp[i]</code> be the minimum number of partitions for the prefix ending at index <code>i + 1</code>.
2. <code>dp[i]</code> can be calculated as the <code>min(dp[j])</code> over all <code>j</code> such that <code>j < i</code> and <code>word[j+1…i]</code> is valid.

## 示例

```
"fabccddg"
"abababaccddb"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumSubstringsInPartition(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumSubstringsInPartition(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumSubstringsInPartition(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        
```

### C

```c
int minimumSubstringsInPartition(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumSubstringsInPartition(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumSubstringsInPartition = function(s) {
    
};
```

### TypeScript

```typescript
function minimumSubstringsInPartition(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumSubstringsInPartition($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumSubstringsInPartition(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumSubstringsInPartition(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumSubstringsInPartition(String s) {
    
  }
}
```

### Go

```golang
func minimumSubstringsInPartition(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def minimum_substrings_in_partition(s)
    
end
```

### Scala

```scala
object Solution {
    def minimumSubstringsInPartition(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_substrings_in_partition(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-substrings-in-partition s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_substrings_in_partition(S :: unicode:unicode_binary()) -> integer().
minimum_substrings_in_partition(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_substrings_in_partition(s :: String.t) :: integer
  def minimum_substrings_in_partition(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumSubstringsInPartition(s: String): Int64 {

    }
}
```

