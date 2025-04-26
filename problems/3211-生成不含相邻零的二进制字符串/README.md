# 3211. 生成不含相邻零的二进制字符串

## 题目描述

<p>给你一个正整数 <code>n</code>。</p>

<p>如果一个二进制字符串 <code>x</code> 的所有长度为 2 的<span data-keyword="substring-nonempty">子字符串</span>中包含 <strong>至少</strong> 一个 <code>"1"</code>，则称 <code>x</code> 是一个<strong> 有效</strong> 字符串。</p>

<p>返回所有长度为 <code>n</code> 的<strong> 有效</strong> 字符串，可以以任意顺序排列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 3</span></p>

<p><strong>输出：</strong> <span class="example-io">["010","011","101","110","111"]</span></p>

<p><strong>解释：</strong></p>

<p>长度为 3 的有效字符串有：<code>"010"</code>、<code>"011"</code>、<code>"101"</code>、<code>"110"</code> 和 <code>"111"</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">["0","1"]</span></p>

<p><strong>解释：</strong></p>

<p>长度为 1 的有效字符串有：<code>"0"</code> 和 <code>"1"</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 18</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 字符串
- 回溯

## 提示

1. If we have a string <code>s</code> of length <code>x</code>, we can generate all strings of length <code>x + 1</code>.
2. If <code>s</code> has 0 as the last character, we can only append 1, whereas if the last character is 1, we can append both 0 and 1.
3. We can use recursion and backtracking to generate all such strings.

## 示例

```
3
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> validStrings(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> validStrings(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def validStrings(self, n: int) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** validStrings(int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> ValidStrings(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {string[]}
 */
var validStrings = function(n) {
    
};
```

### TypeScript

```typescript
function validStrings(n: number): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return String[]
     */
    function validStrings($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validStrings(_ n: Int) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validStrings(n: Int): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> validStrings(int n) {
    
  }
}
```

### Go

```golang
func validStrings(n int) []string {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {String[]}
def valid_strings(n)
    
end
```

### Scala

```scala
object Solution {
    def validStrings(n: Int): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn valid_strings(n: i32) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (valid-strings n)
  (-> exact-integer? (listof string?))
  )
```

### Erlang

```erlang
-spec valid_strings(N :: integer()) -> [unicode:unicode_binary()].
valid_strings(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec valid_strings(n :: integer) :: [String.t]
  def valid_strings(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validStrings(n: Int64): ArrayList<String> {

    }
}
```

