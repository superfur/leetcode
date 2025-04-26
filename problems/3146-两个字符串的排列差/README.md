# 3146. 两个字符串的排列差

## 题目描述

<p>给你两个字符串 <code>s</code> 和 <code>t</code>，每个字符串中的字符都不重复，且 <code>t</code> 是 <code>s</code> 的一个排列。</p>

<p><strong>排列差</strong> 定义为 <code>s</code> 和 <code>t</code> 中每个字符在两个字符串中位置的绝对差值之和。</p>

<p>返回 <code>s</code> 和 <code>t</code> 之间的<strong> 排列差 </strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "abc", t = "bac"</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>对于 <code>s = "abc"</code> 和 <code>t = "bac"</code>，排列差是：</p>

<ul>
	<li><code>"a"</code> 在 <code>s</code> 中的位置与在 <code>t</code> 中的位置之差的绝对值。</li>
	<li><code>"b"</code> 在 <code>s</code> 中的位置与在 <code>t</code> 中的位置之差的绝对值。</li>
	<li><code>"c"</code> 在 <code>s</code> 中的位置与在 <code>t</code> 中的位置之差的绝对值。</li>
</ul>

<p>即，<code>s</code> 和 <code>t</code> 的排列差等于 <code>|0 - 1| + |1 - 0| + |2&nbsp;- 2| = 2</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "abcde", t = "edbac"</span></p>

<p><strong>输出：</strong><span class="example-io">12</span></p>

<p><strong>解释：</strong> <code>s</code> 和 <code>t</code> 的排列差等于 <code>|0 - 3| + |1 - 2| + |2 - 4| + |3 - 1| + |4 - 0| = 12</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 26</code></li>
	<li>每个字符在 <code>s</code> 中最多出现一次。</li>
	<li><code>t</code> 是 <code>s</code> 的一个排列。</li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. For each character, find the indices of its occurrences in string <code>s</code> then in string <code>t</code>.

## 示例

```
"abc"
"bac"
"abcde"
"edbac"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findPermutationDifference(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public int findPermutationDifference(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
```

### C

```c
int findPermutationDifference(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindPermutationDifference(string s, string t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var findPermutationDifference = function(s, t) {
    
};
```

### TypeScript

```typescript
function findPermutationDifference(s: string, t: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function findPermutationDifference($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findPermutationDifference(_ s: String, _ t: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findPermutationDifference(s: String, t: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findPermutationDifference(String s, String t) {
    
  }
}
```

### Go

```golang
func findPermutationDifference(s string, t string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Integer}
def find_permutation_difference(s, t)
    
end
```

### Scala

```scala
object Solution {
    def findPermutationDifference(s: String, t: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_permutation_difference(s: String, t: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-permutation-difference s t)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_permutation_difference(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
find_permutation_difference(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_permutation_difference(s :: String.t, t :: String.t) :: integer
  def find_permutation_difference(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findPermutationDifference(s: String, t: String): Int64 {

    }
}
```

