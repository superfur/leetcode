# 2575. 找出字符串的可整除数组

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>word</code> ，长度为 <code>n</code> ，由从 <code>0</code> 到 <code>9</code> 的数字组成。另给你一个正整数 <code>m</code> 。</p>

<p><code>word</code> 的 <strong>可整除数组</strong> <code>div</code>&nbsp; 是一个长度为 <code>n</code> 的整数数组，并满足：</p>

<ul>
	<li>如果 <code>word[0,...,i]</code> 所表示的 <strong>数值</strong> 能被 <code>m</code> 整除，<code>div[i] = 1</code></li>
	<li>否则，<code>div[i] = 0</code></li>
</ul>

<p>返回<em> </em><code>word</code> 的可整除数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>word = "998244353", m = 3
<strong>输出：</strong>[1,1,0,0,0,1,1,0,0]
<strong>解释：</strong>仅有 4 个前缀可以被 3 整除："9"、"99"、"998244" 和 "9982443" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>word = "1010", m = 10
<strong>输出：</strong>[0,1,0,1]
<strong>解释：</strong>仅有 2 个前缀可以被 10 整除："10" 和 "1010" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>word.length == n</code></li>
	<li><code>word</code> 由数字 <code>0</code> 到 <code>9</code> 组成</li>
	<li><code>1 &lt;= m &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 字符串

## 提示

1. We can check if the numeric value of the prefix of the given string is divisible by m by computing the remainder of the numeric value of the prefix when divided by m.
2. The remainder of the numeric value of a prefix ending at index i can be computed from the remainder of the prefix ending at index i-1.

## 示例

```
"998244353"
3
"1010"
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> divisibilityArray(string word, int m) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] divisibilityArray(String word, int m) {
        
    }
}
```

### Python

```python
class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* divisibilityArray(char* word, int m, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] DivisibilityArray(string word, int m) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @param {number} m
 * @return {number[]}
 */
var divisibilityArray = function(word, m) {
    
};
```

### TypeScript

```typescript
function divisibilityArray(word: string, m: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @param Integer $m
     * @return Integer[]
     */
    function divisibilityArray($word, $m) {
        
    }
}
```

### Swift

```swift
class Solution {
    func divisibilityArray(_ word: String, _ m: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun divisibilityArray(word: String, m: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> divisibilityArray(String word, int m) {
    
  }
}
```

### Go

```golang
func divisibilityArray(word string, m int) []int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @param {Integer} m
# @return {Integer[]}
def divisibility_array(word, m)
    
end
```

### Scala

```scala
object Solution {
    def divisibilityArray(word: String, m: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn divisibility_array(word: String, m: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (divisibility-array word m)
  (-> string? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec divisibility_array(Word :: unicode:unicode_binary(), M :: integer()) -> [integer()].
divisibility_array(Word, M) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec divisibility_array(word :: String.t, m :: integer) :: [integer]
  def divisibility_array(word, m) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func divisibilityArray(word: String, m: Int64): Array<Int64> {

    }
}
```

