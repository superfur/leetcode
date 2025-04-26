# 564. 寻找最近的回文数

## 题目描述

<p>给定一个表示整数的字符串&nbsp;<code>n</code> ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。</p>

<p>“最近的”定义为两个整数<strong>差的绝对值</strong>最小。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> n = "123"
<strong>输出:</strong> "121"
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> n = "1"
<strong>输出:</strong> "0"
<strong>解释:</strong> 0 和 2是最近的回文，但我们返回最小的，也就是 0。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= n.length &lt;= 18</code></li>
	<li><code>n</code>&nbsp;只由数字组成</li>
	<li><code>n</code>&nbsp;不含前导 0</li>
	<li><code>n</code>&nbsp;代表在&nbsp;<code>[1, 10<sup>18</sup>&nbsp;- 1]</code> 范围内的整数</li>
</ul>


## 难度

Hard

## 标签

- 数学
- 字符串

## 提示

1. Will brute force work for this problem? Think of something else.
2. Take some examples like 1234, 999,1000, etc and check their closest palindromes. How many different cases are possible?
3. Do we have to consider only left half or right half of the string or both?
4. Try to find the closest palindrome of these numbers- 12932, 99800, 12120. Did you observe something?

## 示例

```
"123"
"1"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string nearestPalindromic(string n) {
        
    }
};
```

### Java

```java
class Solution {
    public String nearestPalindromic(String n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
```

### C

```c
char* nearestPalindromic(char* n) {
    
}
```

### C#

```csharp
public class Solution {
    public string NearestPalindromic(string n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} n
 * @return {string}
 */
var nearestPalindromic = function(n) {
    
};
```

### TypeScript

```typescript
function nearestPalindromic(n: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $n
     * @return String
     */
    function nearestPalindromic($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func nearestPalindromic(_ n: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun nearestPalindromic(n: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String nearestPalindromic(String n) {
    
  }
}
```

### Go

```golang
func nearestPalindromic(n string) string {
    
}
```

### Ruby

```ruby
# @param {String} n
# @return {String}
def nearest_palindromic(n)
    
end
```

### Scala

```scala
object Solution {
    def nearestPalindromic(n: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn nearest_palindromic(n: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (nearest-palindromic n)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec nearest_palindromic(N :: unicode:unicode_binary()) -> unicode:unicode_binary().
nearest_palindromic(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec nearest_palindromic(n :: String.t) :: String.t
  def nearest_palindromic(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func nearestPalindromic(n: String): String {

    }
}
```

