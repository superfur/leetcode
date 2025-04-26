# 438. 找到字符串中所有字母异位词

## 题目描述

<p>给定两个字符串&nbsp;<code>s</code>&nbsp;和 <code>p</code>，找到&nbsp;<code>s</code><strong>&nbsp;</strong>中所有&nbsp;<code>p</code><strong>&nbsp;</strong>的&nbsp;<strong><span data-keyword="anagram">异位词</span>&nbsp;</strong>的子串，返回这些子串的起始索引。不考虑答案输出的顺序。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入: </strong>s = "cbaebabacd", p = "abc"
<strong>输出: </strong>[0,6]
<strong>解释:</strong>
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
</pre>

<p><strong>&nbsp;示例 2:</strong></p>

<pre>
<strong>输入: </strong>s = "abab", p = "ab"
<strong>输出: </strong>[0,1,2]
<strong>解释:</strong>
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, p.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp;和&nbsp;<code>p</code>&nbsp;仅包含小写字母</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 示例

```
"cbaebabacd"
"abc"
"abab"
"ab"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findAnagrams(char* s, char* p, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> FindAnagrams(string s, string p) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    
};
```

### TypeScript

```typescript
function findAnagrams(s: string, p: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $p
     * @return Integer[]
     */
    function findAnagrams($s, $p) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findAnagrams(_ s: String, _ p: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findAnagrams(s: String, p: String): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findAnagrams(String s, String p) {
    
  }
}
```

### Go

```golang
func findAnagrams(s string, p string) []int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} p
# @return {Integer[]}
def find_anagrams(s, p)
    
end
```

### Scala

```scala
object Solution {
    def findAnagrams(s: String, p: String): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-anagrams s p)
  (-> string? string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_anagrams(S :: unicode:unicode_binary(), P :: unicode:unicode_binary()) -> [integer()].
find_anagrams(S, P) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_anagrams(s :: String.t, p :: String.t) :: [integer]
  def find_anagrams(s, p) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findAnagrams(s: String, p: String): ArrayList<Int64> {

    }
}
```

