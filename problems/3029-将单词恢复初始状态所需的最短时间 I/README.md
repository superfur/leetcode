# 3029. 将单词恢复初始状态所需的最短时间 I

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>word</code> 和一个整数 <code>k</code> 。</p>

<p>在每一秒，你必须执行以下操作：</p>

<ul>
	<li>移除 <code>word</code> 的前 <code>k</code> 个字符。</li>
	<li>在 <code>word</code> 的末尾添加 <code>k</code> 个任意字符。</li>
</ul>

<p><strong>注意 </strong>添加的字符不必和移除的字符相同。但是，必须在每一秒钟都执行 <strong>两种 </strong>操作。</p>

<p>返回将 <code>word</code> 恢复到其 <strong>初始 </strong>状态所需的 <strong>最短 </strong>时间（该时间必须大于零）。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>word = "abacaba", k = 3
<strong>输出：</strong>2
<strong>解释：</strong>
第 1 秒，移除 word 的前缀 "aba"，并在末尾添加 "bac" 。因此，word 变为 "cababac"。
第 2 秒，移除 word 的前缀 "cab"，并在末尾添加 "aba" 。因此，word 变为 "abacaba" 并恢复到始状态。
可以证明，2 秒是 word 恢复到其初始状态所需的最短时间。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>word = "abacaba", k = 4
<strong>输出：</strong>1
<strong>解释：
</strong>第 1 秒，移除 word 的前缀 "abac"，并在末尾添加 "caba" 。因此，word 变为 "abacaba" 并恢复到初始状态。
可以证明，1 秒是 word 恢复到其初始状态所需的最短时间。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>word = "abcbabcd", k = 2
<strong>输出：</strong>4
<strong>解释：</strong>
每一秒，我们都移除 word 的前 2 个字符，并在 word 末尾添加相同的字符。
4 秒后，word 变为 "abcbabcd" 并恢复到初始状态。
可以证明，4 秒是 word 恢复到其初始状态所需的最短时间。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 50</code></li>
	<li><code>1 &lt;= k &lt;= word.length</code></li>
	<li><code>word</code>仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 字符串匹配
- 哈希函数
- 滚动哈希

## 提示

1. Find the longest suffix which is also a prefix and the length is multiple of <code>k</code>.

## 示例

```
"abacaba"
3
"abacaba"
4
"abcbabcd"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumTimeToInitialState(string word, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumTimeToInitialState(String word, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumTimeToInitialState(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        
```

### C

```c
int minimumTimeToInitialState(char* word, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumTimeToInitialState(string word, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var minimumTimeToInitialState = function(word, k) {
    
};
```

### TypeScript

```typescript
function minimumTimeToInitialState(word: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @param Integer $k
     * @return Integer
     */
    function minimumTimeToInitialState($word, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumTimeToInitialState(_ word: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumTimeToInitialState(word: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumTimeToInitialState(String word, int k) {
    
  }
}
```

### Go

```golang
func minimumTimeToInitialState(word string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @param {Integer} k
# @return {Integer}
def minimum_time_to_initial_state(word, k)
    
end
```

### Scala

```scala
object Solution {
    def minimumTimeToInitialState(word: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_time_to_initial_state(word: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-time-to-initial-state word k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_time_to_initial_state(Word :: unicode:unicode_binary(), K :: integer()) -> integer().
minimum_time_to_initial_state(Word, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_time_to_initial_state(word :: String.t, k :: integer) :: integer
  def minimum_time_to_initial_state(word, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumTimeToInitialState(word: String, k: Int64): Int64 {

    }
}
```

