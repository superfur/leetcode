# 1647. 字符频次唯一的最小删除次数

## 题目描述

<p>如果字符串 <code>s</code> 中 <strong>不存在</strong> 两个不同字符 <strong>频次</strong> 相同的情况，就称 <code>s</code> 是 <strong>优质字符串</strong> 。</p>

<p>给你一个字符串 <code>s</code>，返回使 <code>s</code> 成为 <strong>优质字符串</strong> 需要删除的 <strong>最小</strong> 字符数。</p>

<p>字符串中字符的 <strong>频次</strong> 是该字符在字符串中的出现次数。例如，在字符串 <code>"aab"</code> 中，<code>'a'</code> 的频次是 <code>2</code>，而 <code>'b'</code> 的频次是 <code>1</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aab"
<strong>输出：</strong>0
<strong>解释：</strong><code>s</code> 已经是优质字符串。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "aaabbbcc"
<strong>输出：</strong>2
<strong>解释：</strong>可以删除两个 'b' , 得到优质字符串 "aaabcc" 。
另一种方式是删除一个 'b' 和一个 'c' ，得到优质字符串 "aaabbc" 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "ceabaacb"
<strong>输出：</strong>2
<strong>解释：</strong>可以删除两个 'c' 得到优质字符串 "eabaab" 。
注意，只需要关注结果字符串中仍然存在的字符。（即，频次为 0 的字符会忽略不计。）
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅含小写英文字母</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 哈希表
- 字符串
- 排序

## 提示

1. As we can only delete characters, if we have multiple characters having the same frequency, we must decrease all the frequencies of them, except one.
2. Sort the alphabet characters by their frequencies non-increasingly.
3. Iterate on the alphabet characters, keep decreasing the frequency of the current character until it reaches a value that has not appeared before.

## 示例

```
"aab"
"aaabbbcc"
"ceabaacb"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minDeletions(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minDeletions(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minDeletions(self, s: str) -> int:
        
```

### C

```c
int minDeletions(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinDeletions(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minDeletions = function(s) {
    
};
```

### TypeScript

```typescript
function minDeletions(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minDeletions($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minDeletions(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minDeletions(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minDeletions(String s) {
    
  }
}
```

### Go

```golang
func minDeletions(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_deletions(s)
    
end
```

### Scala

```scala
object Solution {
    def minDeletions(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_deletions(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-deletions s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_deletions(S :: unicode:unicode_binary()) -> integer().
min_deletions(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_deletions(s :: String.t) :: integer
  def min_deletions(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minDeletions(s: String): Int64 {

    }
}
```

