# 1447. 最简分数

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于&nbsp;&nbsp;<code>n</code>&nbsp;的 <strong>最简&nbsp;</strong>分数&nbsp;。分数可以以 <strong>任意&nbsp;</strong>顺序返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>[&quot;1/2&quot;]
<strong>解释：</strong>&quot;1/2&quot; 是唯一一个分母小于等于 2 的最简分数。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 3
<strong>输出：</strong>[&quot;1/2&quot;,&quot;1/3&quot;,&quot;2/3&quot;]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 4
<strong>输出：</strong>[&quot;1/2&quot;,&quot;1/3&quot;,&quot;1/4&quot;,&quot;2/3&quot;,&quot;3/4&quot;]
<strong>解释：</strong>&quot;2/4&quot; 不是最简分数，因为它可以化简为 &quot;1/2&quot; 。</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>n = 1
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 字符串
- 数论

## 提示

1. A fraction is fully simplified if there is no integer that divides cleanly into the numerator and denominator.
2. In other words the greatest common divisor of the numerator and the denominator of a simplified fraction is 1.

## 示例

```
2
3
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> simplifiedFractions(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> simplifiedFractions(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** simplifiedFractions(int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> SimplifiedFractions(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {string[]}
 */
var simplifiedFractions = function(n) {
    
};
```

### TypeScript

```typescript
function simplifiedFractions(n: number): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return String[]
     */
    function simplifiedFractions($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func simplifiedFractions(_ n: Int) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun simplifiedFractions(n: Int): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> simplifiedFractions(int n) {
    
  }
}
```

### Go

```golang
func simplifiedFractions(n int) []string {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {String[]}
def simplified_fractions(n)
    
end
```

### Scala

```scala
object Solution {
    def simplifiedFractions(n: Int): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn simplified_fractions(n: i32) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (simplified-fractions n)
  (-> exact-integer? (listof string?))
  )
```

### Erlang

```erlang
-spec simplified_fractions(N :: integer()) -> [unicode:unicode_binary()].
simplified_fractions(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec simplified_fractions(n :: integer) :: [String.t]
  def simplified_fractions(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func simplifiedFractions(n: Int64): ArrayList<String> {

    }
}
```

