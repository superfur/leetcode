# 2914. 使二进制字符串变美丽的最少修改次数

## 题目描述

<p>给你一个长度为偶数下标从 <strong>0</strong>&nbsp;开始的二进制字符串&nbsp;<code>s</code>&nbsp;。</p>

<p>如果可以将一个字符串分割成一个或者更多满足以下条件的子字符串，那么我们称这个字符串是 <strong>美丽的</strong>&nbsp;：</p>

<ul>
	<li>每个子字符串的长度都是 <strong>偶数</strong>&nbsp;。</li>
	<li>每个子字符串都 <strong>只</strong>&nbsp;包含 <code>1</code>&nbsp;或 <strong>只</strong>&nbsp;包含 <code>0</code>&nbsp;。</li>
</ul>

<p>你可以将 <code>s</code>&nbsp;中任一字符改成&nbsp;<code>0</code>&nbsp;或者&nbsp;<code>1</code>&nbsp;。</p>

<p>请你返回让字符串 <code>s</code>&nbsp;美丽的<strong>&nbsp;最少</strong>&nbsp;字符修改次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>s = "1001"
<b>输出：</b>2
<b>解释：</b>我们将 s[1] 改为 1 ，且将 s[3] 改为 0 ，得到字符串 "1100" 。
字符串 "1100" 是美丽的，因为我们可以将它分割成 "11|00" 。
将字符串变美丽最少需要 2 次修改。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>s = "10"
<b>输出：</b>1
<b>解释：</b>我们将 s[1] 改为 1 ，得到字符串 "11" 。
字符串 "11" 是美丽的，因为它已经是美丽的。
将字符串变美丽最少需要 1 次修改。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>s = "0000"
<b>输出：</b>0
<b>解释：</b>不需要进行任何修改，字符串 "0000" 已经是美丽字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;的长度为偶数。</li>
	<li><code>s[i]</code>&nbsp;要么是&nbsp;<code>'0'</code>&nbsp;，要么是&nbsp;<code>'1'</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 字符串

## 提示

1. For any valid partition, since each part consists of an even number of the same characters, we can further partition each part into lengths of exactly <code>2</code>.
2. After noticing the first hint, we can decompose the whole string into disjoint blocks of size <code>2</code> and find the minimum number of changes required to make those blocks beautiful.

## 示例

```
"1001"
"10"
"0000"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minChanges(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minChanges(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minChanges(self, s: str) -> int:
        
```

### C

```c
int minChanges(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinChanges(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minChanges = function(s) {
    
};
```

### TypeScript

```typescript
function minChanges(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minChanges($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minChanges(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minChanges(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minChanges(String s) {
    
  }
}
```

### Go

```golang
func minChanges(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_changes(s)
    
end
```

### Scala

```scala
object Solution {
    def minChanges(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_changes(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-changes s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_changes(S :: unicode:unicode_binary()) -> integer().
min_changes(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_changes(s :: String.t) :: integer
  def min_changes(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minChanges(s: String): Int64 {

    }
}
```

