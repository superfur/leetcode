# 466. 统计重复个数

## 题目描述

<p>定义 <code>str = [s, n]</code> 表示 <code>str</code> 由 <code>n</code> 个字符串 <code>s</code> 连接构成。</p>

<ul>
	<li>例如，<code>str == ["abc", 3] =="abcabcabc"</code> 。</li>
</ul>

<p>如果可以从 <code>s2</code><sub> </sub>中删除某些字符使其变为 <code>s1</code>，则称字符串 <code>s1</code><sub> </sub>可以从字符串 <code>s2</code> 获得。</p>

<ul>
	<li>例如，根据定义，<code>s1 = "abc"</code> 可以从 <code>s2 = "ab<em><strong>dbe</strong></em>c"</code> 获得，仅需要删除加粗且用斜体标识的字符。</li>
</ul>

<p>现在给你两个字符串 <code>s1</code> 和 <code>s2</code> 和两个整数 <code>n1</code> 和 <code>n2</code> 。由此构造得到两个字符串，其中 <code>str1 = [s1, n1]</code>、<code>str2 = [s2, n2]</code> 。</p>

<p>请你找出一个最大整数 <code>m</code> ，以满足 <code>str = [str2, m]</code> 可以从 <code>str1</code> 获得。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s1.length, s2.length <= 100</code></li>
	<li><code>s1</code> 和 <code>s2</code> 由小写英文字母组成</li>
	<li><code>1 <= n1, n2 <= 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 示例

```
"acb"
4
"ab"
2
"acb"
1
"acb"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getMaxRepetitions(string s1, int n1, string s2, int n2) {
        
    }
};
```

### Java

```java
class Solution {
    public int getMaxRepetitions(String s1, int n1, String s2, int n2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        
```

### C

```c
int getMaxRepetitions(char* s1, int n1, char* s2, int n2) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetMaxRepetitions(string s1, int n1, string s2, int n2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {number} n1
 * @param {string} s2
 * @param {number} n2
 * @return {number}
 */
var getMaxRepetitions = function(s1, n1, s2, n2) {
    
};
```

### TypeScript

```typescript
function getMaxRepetitions(s1: string, n1: number, s2: string, n2: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param Integer $n1
     * @param String $s2
     * @param Integer $n2
     * @return Integer
     */
    function getMaxRepetitions($s1, $n1, $s2, $n2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getMaxRepetitions(_ s1: String, _ n1: Int, _ s2: String, _ n2: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMaxRepetitions(s1: String, n1: Int, s2: String, n2: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getMaxRepetitions(String s1, int n1, String s2, int n2) {
    
  }
}
```

### Go

```golang
func getMaxRepetitions(s1 string, n1 int, s2 string, n2 int) int {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {Integer} n1
# @param {String} s2
# @param {Integer} n2
# @return {Integer}
def get_max_repetitions(s1, n1, s2, n2)
    
end
```

### Scala

```scala
object Solution {
    def getMaxRepetitions(s1: String, n1: Int, s2: String, n2: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_max_repetitions(s1: String, n1: i32, s2: String, n2: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-max-repetitions s1 n1 s2 n2)
  (-> string? exact-integer? string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec get_max_repetitions(S1 :: unicode:unicode_binary(), N1 :: integer(), S2 :: unicode:unicode_binary(), N2 :: integer()) -> integer().
get_max_repetitions(S1, N1, S2, N2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_max_repetitions(s1 :: String.t, n1 :: integer, s2 :: String.t, n2 :: integer) :: integer
  def get_max_repetitions(s1, n1, s2, n2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getMaxRepetitions(s1: String, n1: Int64, s2: String, n2: Int64): Int64 {

    }
}
```

