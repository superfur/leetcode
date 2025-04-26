# 1737. 满足三条件之一需改变的最少字符数

## 题目描述

<p>给你两个字符串 <code>a</code> 和 <code>b</code> ，二者均由小写字母组成。一步操作中，你可以将 <code>a</code> 或 <code>b</code> 中的 <strong>任一字符</strong> 改变为 <strong>任一小写字母</strong> 。</p>

<p>操作的最终目标是满足下列三个条件 <strong>之一</strong> ：</p>

<ul>
	<li><code>a</code> 中的 <strong>每个字母</strong> 在字母表中 <strong>严格小于</strong> <code>b</code> 中的 <strong>每个字母</strong> 。</li>
	<li><code>b</code> 中的 <strong>每个字母</strong> 在字母表中 <strong>严格小于</strong> <code>a</code> 中的 <strong>每个字母</strong> 。</li>
	<li><code>a</code> 和 <code>b</code> <strong>都</strong> 由 <strong>同一个</strong> 字母组成。</li>
</ul>

<p>返回达成目标所需的 <strong>最少</strong> 操作数<em>。</em></p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>a = "aba", b = "caa"
<strong>输出：</strong>2
<strong>解释：</strong>满足每个条件的最佳方案分别是：
1) 将 b 变为 "ccc"，2 次操作，满足 a 中的每个字母都小于 b 中的每个字母；
2) 将 a 变为 "bbb" 并将 b 变为 "aaa"，3 次操作，满足 b 中的每个字母都小于 a 中的每个字母；
3) 将 a 变为 "aaa" 并将 b 变为 "aaa"，2 次操作，满足 a 和 b 由同一个字母组成。
最佳的方案只需要 2 次操作（满足条件 1 或者条件 3）。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>a = "dabadd", b = "cda"
<strong>输出：</strong>3
<strong>解释：</strong>满足条件 1 的最佳方案是将 b 变为 "eee" 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>5</sup></code></li>
	<li><code>a</code> 和 <code>b</code> 只由小写字母组成</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 计数
- 前缀和

## 提示

1. Iterate on each letter in the alphabet, and check the smallest number of operations needed to make it one of the following: the largest letter in a and smaller than the smallest one in b, vice versa, or let a and b consist only of this letter.
2. For the first 2 conditions, take care that you can only change characters to lowercase letters, so you can't make 'z' the smallest letter in one of the strings or 'a' the largest letter in one of them.

## 示例

```
"aba"
"caa"
"dabadd"
"cda"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCharacters(string a, string b) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCharacters(String a, String b) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        
```

### C

```c
int minCharacters(char* a, char* b) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCharacters(string a, string b) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
var minCharacters = function(a, b) {
    
};
```

### TypeScript

```typescript
function minCharacters(a: string, b: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $a
     * @param String $b
     * @return Integer
     */
    function minCharacters($a, $b) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCharacters(_ a: String, _ b: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCharacters(a: String, b: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCharacters(String a, String b) {
    
  }
}
```

### Go

```golang
func minCharacters(a string, b string) int {
    
}
```

### Ruby

```ruby
# @param {String} a
# @param {String} b
# @return {Integer}
def min_characters(a, b)
    
end
```

### Scala

```scala
object Solution {
    def minCharacters(a: String, b: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_characters(a: String, b: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-characters a b)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_characters(A :: unicode:unicode_binary(), B :: unicode:unicode_binary()) -> integer().
min_characters(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_characters(a :: String.t, b :: String.t) :: integer
  def min_characters(a, b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCharacters(a: String, b: String): Int64 {

    }
}
```

