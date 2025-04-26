# 2262. 字符串的总引力

## 题目描述

<p>字符串的 <strong>引力</strong> 定义为：字符串中 <strong>不同</strong> 字符的数量。</p>

<ul>
	<li>例如，<code>"abbca"</code> 的引力为 <code>3</code> ，因为其中有 <code>3</code> 个不同字符 <code>'a'</code>、<code>'b'</code> 和 <code>'c'</code> 。</li>
</ul>

<p>给你一个字符串 <code>s</code> ，返回 <strong>其所有子字符串的总引力</strong> <strong>。</strong></p>

<p><strong>子字符串</strong> 定义为：字符串中的一个连续字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "abbca"
<strong>输出：</strong>28
<strong>解释：</strong>"abbca" 的子字符串有：
- 长度为 1 的子字符串："a"、"b"、"b"、"c"、"a" 的引力分别为 1、1、1、1、1，总和为 5 。
- 长度为 2 的子字符串："ab"、"bb"、"bc"、"ca" 的引力分别为 2、1、2、2 ，总和为 7 。
- 长度为 3 的子字符串："abb"、"bbc"、"bca" 的引力分别为 2、2、3 ，总和为 7 。
- 长度为 4 的子字符串："abbc"、"bbca" 的引力分别为 3、3 ，总和为 6 。
- 长度为 5 的子字符串："abbca" 的引力为 3 ，总和为 3 。
引力总和为 5 + 7 + 7 + 6 + 3 = 28 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "code"
<strong>输出：</strong>20
<strong>解释：</strong>"code" 的子字符串有：
- 长度为 1 的子字符串："c"、"o"、"d"、"e" 的引力分别为 1、1、1、1 ，总和为 4 。
- 长度为 2 的子字符串："co"、"od"、"de" 的引力分别为 2、2、2 ，总和为 6 。
- 长度为 3 的子字符串："cod"、"ode" 的引力分别为 3、3 ，总和为 6 。
- 长度为 4 的子字符串："code" 的引力为 4 ，总和为 4 。
引力总和为 4 + 6 + 6 + 4 = 20 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 哈希表
- 字符串
- 动态规划

## 提示

1. Consider the set of substrings that end at a certain index i. Then, consider a specific alphabetic character. How do you count the number of substrings ending at index i that contain that character?
2. The number of substrings that contain the alphabetic character is equivalent to 1 plus the index of the last occurrence of the character before index i + 1.
3. The total appeal of all substrings ending at index i is the total sum of the number of substrings that contain each alphabetic character.
4. To find the total appeal of all substrings, we simply sum up the total appeal for each index.

## 示例

```
"abbca"
"code"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long appealSum(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public long appealSum(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def appealSum(self, s: str) -> int:
        
```

### C

```c
long long appealSum(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public long AppealSum(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var appealSum = function(s) {
    
};
```

### TypeScript

```typescript
function appealSum(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function appealSum($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func appealSum(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun appealSum(s: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int appealSum(String s) {
    
  }
}
```

### Go

```golang
func appealSum(s string) int64 {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def appeal_sum(s)
    
end
```

### Scala

```scala
object Solution {
    def appealSum(s: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn appeal_sum(s: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (appeal-sum s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec appeal_sum(S :: unicode:unicode_binary()) -> integer().
appeal_sum(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec appeal_sum(s :: String.t) :: integer
  def appeal_sum(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func appealSum(s: String): Int64 {

    }
}
```

