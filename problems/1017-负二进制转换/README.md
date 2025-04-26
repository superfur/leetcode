# 1017. 负二进制转换

## 题目描述

<p>给你一个整数 <code>n</code> ，以二进制字符串的形式返回该整数的 <strong>负二进制（<code>base -2</code>）</strong>表示。</p>

<p><strong>注意，</strong>除非字符串就是&nbsp;<code>"0"</code>，否则返回的字符串中不能含有前导零。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>"110"
<strong>解释：</strong>(-2)<sup>2</sup> + (-2)<sup>1</sup> = 2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>"111"
<strong>解释：</strong>(-2)<sup>2</sup> + (-2)<sup>1</sup> + (-2)<sup>0</sup> = 3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>"100"
<strong>解释：</strong>(-2)<sup>2</sup> = 4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学

## 提示

1. Figure out whether you need the ones digit placed or not, then shift by two.

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
    string baseNeg2(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public String baseNeg2(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def baseNeg2(self, n: int) -> str:
        
```

### C

```c
char* baseNeg2(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public string BaseNeg2(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {string}
 */
var baseNeg2 = function(n) {
    
};
```

### TypeScript

```typescript
function baseNeg2(n: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return String
     */
    function baseNeg2($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func baseNeg2(_ n: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun baseNeg2(n: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String baseNeg2(int n) {
    
  }
}
```

### Go

```golang
func baseNeg2(n int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {String}
def base_neg2(n)
    
end
```

### Scala

```scala
object Solution {
    def baseNeg2(n: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn base_neg2(n: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (base-neg2 n)
  (-> exact-integer? string?)
  )
```

### Erlang

```erlang
-spec base_neg2(N :: integer()) -> unicode:unicode_binary().
base_neg2(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec base_neg2(n :: integer) :: String.t
  def base_neg2(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func baseNeg2(n: Int64): String {

    }
}
```

