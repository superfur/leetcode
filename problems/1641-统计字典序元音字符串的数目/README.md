# 1641. 统计字典序元音字符串的数目

## 题目描述

<p>给你一个整数 <code>n</code>，请返回长度为 <code>n</code> 、仅由元音 (<code>a</code>, <code>e</code>, <code>i</code>, <code>o</code>, <code>u</code>) 组成且按 <strong>字典序排列</strong> 的字符串数量。</p>

<p>字符串 <code>s</code> 按 <strong>字典序排列</strong> 需要满足：对于所有有效的 <code>i</code>，<code>s[i]</code> 在字母表中的位置总是与 <code>s[i+1]</code> 相同或在 <code>s[i+1]</code> 之前。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>5
<strong>解释：</strong>仅由元音组成的 5 个字典序字符串为 <code>["a","e","i","o","u"]</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>15
<strong>解释：</strong>仅由元音组成的 15 个字典序字符串为
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 33
<strong>输出：</strong>66045
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 50</code> </li>
</ul>


## 难度

Medium

## 标签

- 数学
- 动态规划
- 组合数学

## 提示

1. For each character, its possible values will depend on the value of its previous character, because it needs to be not smaller than it.
2. Think backtracking. Build a recursive function count(n, last_character) that counts the number of valid strings of length n and whose first characters are not less than last_character.
3. In this recursive function, iterate on the possible characters for the first character, which will be all the vowels not less than last_character, and for each possible value c, increase the answer by count(n-1, c).

## 示例

```
1
2
33
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countVowelStrings(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int countVowelStrings(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countVowelStrings(self, n: int) -> int:
        
```

### C

```c
int countVowelStrings(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountVowelStrings(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countVowelStrings = function(n) {
    
};
```

### TypeScript

```typescript
function countVowelStrings(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countVowelStrings($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countVowelStrings(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countVowelStrings(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countVowelStrings(int n) {
    
  }
}
```

### Go

```golang
func countVowelStrings(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def count_vowel_strings(n)
    
end
```

### Scala

```scala
object Solution {
    def countVowelStrings(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_vowel_strings(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-vowel-strings n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_vowel_strings(N :: integer()) -> integer().
count_vowel_strings(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_vowel_strings(n :: integer) :: integer
  def count_vowel_strings(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countVowelStrings(n: Int64): Int64 {

    }
}
```

