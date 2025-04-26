# 3085. 成为 K 特殊字符串需要删除的最少字符数

## 题目描述

<p>给你一个字符串 <code>word</code> 和一个整数 <code>k</code>。</p>

<p>如果&nbsp;<code>|freq(word[i]) - freq(word[j])| &lt;= k</code> 对于字符串中所有下标 <code>i</code> 和 <code>j</code>&nbsp; 都成立，则认为 <code>word</code> 是 <strong>k 特殊字符串</strong>。</p>

<p>此处，<code>freq(x)</code> 表示字符 <code>x</code> 在 <code>word</code> 中的<span data-keyword="frequency-letter">出现频率</span>，而 <code>|y|</code> 表示 <code>y</code> 的绝对值。</p>

<p>返回使 <code>word</code> 成为 <strong>k 特殊字符串</strong> 需要删除的字符的最小数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">word = "aabcaba", k = 0</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">3</span></p>

<p><strong>解释：</strong>可以删除 <code>2</code> 个 <code>"a"</code> 和 <code>1</code> 个 <code>"c"</code> 使 <code>word</code> 成为 <code>0</code> 特殊字符串。<code>word</code> 变为 <code>"baba"</code>，此时 <code>freq('a') == freq('b') == 2</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">word = "dabdcbdcdcd", k = 2</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">2</span></p>

<p><strong>解释：</strong>可以删除 <code>1</code> 个 <code>"a"</code> 和 <code>1</code> 个 <code>"d"</code> 使 <code>word</code> 成为 <code>2</code> 特殊字符串。<code>word</code> 变为 <code>"bdcbdcdcd"</code>，此时 <code>freq('b') == 2</code>，<code>freq('c') == 3</code>，<code>freq('d') == 4</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">word = "aaabaaa", k = 2</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">1</span></p>

<p><strong>解释：</strong>可以删除<strong> </strong>1 个 <code>"b"</code> 使 <code>word</code> 成为 <code>2</code>特殊字符串。因此，<code>word</code> 变为 <code>"aaaaaa"</code>，此时每个字母的频率都是 <code>6</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>5</sup></code></li>
	<li><code>word</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 哈希表
- 字符串
- 计数
- 排序

## 提示

1. Count the frequency of each letter.
2. Suppose we select several characters as the final answer, and let <code>x</code> be the character with the smallest frequency in the answer. It can be shown that out of the selected characters, the optimal solution will never delete an occurrence of character <code>x</code> to obtain the answer.
3. We will fix a character <code>c</code> and assume that it will be the character with the smallest frequency in the answer. Suppose its frequency is <code>x</code>.
4. Then, for every other character, we will count the number of occurrences that will be deleted. Suppose that the current character has <code>y</code> occurrences. <ol> <li>If y < x, we need to delete all of them.</li> <li> if y > x + k, we should delete y - x - k of such character.</li> <li> Otherwise we don’t need to delete it.</li></ol>

## 示例

```
"aabcaba"
0
"dabdcbdcdcd"
2
"aaabaaa"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumDeletions(string word, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumDeletions(String word, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
```

### C

```c
int minimumDeletions(char* word, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumDeletions(string word, int k) {
        
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
var minimumDeletions = function(word, k) {
    
};
```

### TypeScript

```typescript
function minimumDeletions(word: string, k: number): number {
    
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
    function minimumDeletions($word, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumDeletions(_ word: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumDeletions(word: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumDeletions(String word, int k) {
    
  }
}
```

### Go

```golang
func minimumDeletions(word string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @param {Integer} k
# @return {Integer}
def minimum_deletions(word, k)
    
end
```

### Scala

```scala
object Solution {
    def minimumDeletions(word: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_deletions(word: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-deletions word k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_deletions(Word :: unicode:unicode_binary(), K :: integer()) -> integer().
minimum_deletions(Word, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_deletions(word :: String.t, k :: integer) :: integer
  def minimum_deletions(word, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumDeletions(word: String, k: Int64): Int64 {

    }
}
```

