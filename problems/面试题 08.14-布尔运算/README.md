# 面试题 08.14. 布尔运算

## 题目描述

<p>给定一个布尔表达式和一个期望的布尔结果 result，布尔表达式由 <code>0</code> (false)、<code>1</code> (true)、<code>&amp;</code> (AND)、 <code>|</code> (OR) 和 <code>^</code> (XOR) 符号组成。实现一个函数，算出有几种可使该表达式得出 result 值的括号方法。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "1^0|0|1", result = 0

<strong>输出：</strong>2
<strong>解释：</strong>两种可能的括号方法是
1^(0|(0|1))
1^((0|0)|1)
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "0&amp;0&amp;0&amp;1^1|0", result = 1

<strong>输出：</strong>10</pre>

<p><strong>提示：</strong></p>

<ul>
	<li>运算符的数量不超过 19 个</li>
</ul>


## 难度

Medium

## 标签

- 记忆化搜索
- 字符串
- 动态规划

## 提示

1. 我们能试试所有的可能性吗？这看起来像什么？
2. 我们可以把每种可能性都看作是每个可以放置括号的地方。这意味着围绕每个操作符，使表达式在运算符上被分割。基线条件是什么？
3. 基本情况是我们有一个值，1或0。
4. 如果你的代码看起来很长，有很多的if（基于每个可能的操作符、“目标”布尔结果和左/右侧），考虑不同部分之间的关系。尽量简化代码。它不需要大量复杂的if语句。例如，考虑<LEFT>OR<RIGHT>与<LEFT>AND<RIGHT>的表达式。两者可能都需要知道<LEFT>计算结果为true的数量。看看你可以重用哪些代码。
5. 着眼于你的递归上。有重复调用吗？可以将结果存起来吗？

## 示例

```
"1"
0
"0"
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countEval(string s, int result) {
        
    }
};
```

### Java

```java
class Solution {
    public int countEval(String s, int result) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countEval(self, s, result):
        """
        :type s: str
        :type result: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countEval(self, s: str, result: int) -> int:
        
```

### C

```c
int countEval(char* s, int result) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountEval(string s, int result) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} result
 * @return {number}
 */
var countEval = function(s, result) {
    
};
```

### TypeScript

```typescript
function countEval(s: string, result: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $result
     * @return Integer
     */
    function countEval($s, $result) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countEval(_ s: String, _ result: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countEval(s: String, result: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countEval(String s, int result) {
    
  }
}
```

### Go

```golang
func countEval(s string, result int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} result
# @return {Integer}
def count_eval(s, result)
    
end
```

### Scala

```scala
object Solution {
    def countEval(s: String, result: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_eval(s: String, result: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-eval s result)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_eval(S :: unicode:unicode_binary(), Result :: integer()) -> integer().
count_eval(S, Result) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_eval(s :: String.t, result :: integer) :: integer
  def count_eval(s, result) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countEval(s: String, result: Int64): Int64 {

    }
}
```

