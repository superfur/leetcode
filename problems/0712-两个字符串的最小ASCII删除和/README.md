# 712. 两个字符串的最小ASCII删除和

## 题目描述

<p>给定两个字符串<code>s1</code>&nbsp;和&nbsp;<code>s2</code>，返回 <em>使两个字符串相等所需删除字符的&nbsp;<strong>ASCII&nbsp;</strong>值的最小和&nbsp;</em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> s1 = "sea", s2 = "eat"
<strong>输出:</strong> 231
<strong>解释:</strong> 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> s1 = "delete", s2 = "leet"
<strong>输出:</strong> 403
<strong>解释:</strong> 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>0 &lt;= s1.length, s2.length &lt;= 1000</code></li>
	<li><code>s1</code>&nbsp;和&nbsp;<code>s2</code>&nbsp;由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 动态规划

## 提示

1. Let dp(i, j) be the answer for inputs s1[i:] and s2[j:].

## 示例

```
"sea"
"eat"
"delete"
"leet"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
```

### C

```c
int minimumDeleteSum(char* s1, char* s2) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumDeleteSum(string s1, string s2) {
        
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
var minimumDeleteSum = function(s1, s2) {
    
};
```

### TypeScript

```typescript
function minimumDeleteSum(s1: string, s2: string): number {
    
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
    function minimumDeleteSum($s1, $s2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumDeleteSum(_ s1: String, _ s2: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumDeleteSum(s1: String, s2: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumDeleteSum(String s1, String s2) {
    
  }
}
```

### Go

```golang
func minimumDeleteSum(s1 string, s2 string) int {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @return {Integer}
def minimum_delete_sum(s1, s2)
    
end
```

### Scala

```scala
object Solution {
    def minimumDeleteSum(s1: String, s2: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-delete-sum s1 s2)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_delete_sum(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> integer().
minimum_delete_sum(S1, S2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_delete_sum(s1 :: String.t, s2 :: String.t) :: integer
  def minimum_delete_sum(s1, s2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumDeleteSum(s1: String, s2: String): Int64 {

    }
}
```

