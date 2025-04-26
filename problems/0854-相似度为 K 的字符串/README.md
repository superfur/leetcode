# 854. 相似度为 K 的字符串

## 题目描述

<p>对于某些非负整数 <code>k</code> ，如果交换 <code>s1</code> 中两个字母的位置恰好 <code>k</code> 次，能够使结果字符串等于 <code>s2</code> ，则认为字符串 <code>s1</code> 和 <code>s2</code> 的<strong> 相似度为 </strong><code>k</code><strong> </strong><strong>。</strong></p>

<p>给你两个字母异位词 <code>s1</code> 和 <code>s2</code> ，返回 <code>s1</code> 和 <code>s2</code> 的相似度 <code>k</code><strong> </strong>的最小值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s1 = "ab", s2 = "ba"
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s1 = "abc", s2 = "bca"
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s1.length &lt;= 20</code></li>
	<li><code>s2.length == s1.length</code></li>
	<li><code>s1</code>&nbsp;和&nbsp;<code>s2</code>&nbsp;&nbsp;只包含集合&nbsp;<code>{'a', 'b', 'c', 'd', 'e', 'f'}</code>&nbsp;中的小写字母</li>
	<li><code>s2</code> 是 <code>s1</code> 的一个字母异位词</li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 字符串

## 示例

```
"ab"
"ba"
"abc"
"bca"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int kSimilarity(string s1, string s2) {
        
    }
};
```

### Java

```java
class Solution {
    public int kSimilarity(String s1, String s2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kSimilarity(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        
```

### C

```c
int kSimilarity(char* s1, char* s2) {
    
}
```

### C#

```csharp
public class Solution {
    public int KSimilarity(string s1, string s2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var kSimilarity = function(s1, s2) {
    
};
```

### TypeScript

```typescript
function kSimilarity(s1: string, s2: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Integer
     */
    function kSimilarity($s1, $s2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kSimilarity(_ s1: String, _ s2: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kSimilarity(s1: String, s2: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int kSimilarity(String s1, String s2) {
    
  }
}
```

### Go

```golang
func kSimilarity(s1 string, s2 string) int {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @return {Integer}
def k_similarity(s1, s2)
    
end
```

### Scala

```scala
object Solution {
    def kSimilarity(s1: String, s2: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn k_similarity(s1: String, s2: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (k-similarity s1 s2)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec k_similarity(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> integer().
k_similarity(S1, S2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec k_similarity(s1 :: String.t, s2 :: String.t) :: integer
  def k_similarity(s1, s2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kSimilarity(s1: String, s2: String): Int64 {

    }
}
```

