# 1404. 将二进制表示减到 1 的步骤数

## 题目描述

<p>给你一个以二进制形式表示的数字 <code>s</code> 。请你返回按下述规则将其减少到 1 所需要的步骤数：</p>

<ul>
	<li>
	<p>如果当前数字为偶数，则将其除以 <code>2</code> 。</p>
	</li>
	<li>
	<p>如果当前数字为奇数，则将其加上 <code>1</code> 。</p>
	</li>
</ul>

<p>题目保证你总是可以按上述规则将测试用例变为 1 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "1101"
<strong>输出：</strong>6
<strong>解释：</strong>"1101" 表示十进制数 13 。
Step 1) 13 是奇数，加 1 得到 14&nbsp;
Step 2) 14 是偶数，除 2 得到 7
Step 3) 7  是奇数，加 1 得到 8
Step 4) 8  是偶数，除 2 得到 4&nbsp; 
Step 5) 4  是偶数，除 2 得到 2&nbsp;
Step 6) 2  是偶数，除 2 得到 1&nbsp; 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "10"
<strong>输出：</strong>1
<strong>解释：</strong>"10" 表示十进制数 2 。
Step 1) 2 是偶数，除 2 得到 1 
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "1"
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length&nbsp;&lt;= 500</code></li>
	<li><code>s</code> 由字符 <code>'0'</code> 或 <code>'1'</code> 组成。</li>
	<li><code>s[0] == '1'</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 字符串
- 模拟

## 提示

1. Read the string from right to left, if the string ends in '0' then the number is even otherwise it is odd.
2. Simulate the steps described in the binary string.

## 示例

```
"1101"
"10"
"1"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numSteps(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int numSteps(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numSteps(self, s: str) -> int:
        
```

### C

```c
int numSteps(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumSteps(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numSteps = function(s) {
    
};
```

### TypeScript

```typescript
function numSteps(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numSteps($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numSteps(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numSteps(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numSteps(String s) {
    
  }
}
```

### Go

```golang
func numSteps(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def num_steps(s)
    
end
```

### Scala

```scala
object Solution {
    def numSteps(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_steps(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-steps s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_steps(S :: unicode:unicode_binary()) -> integer().
num_steps(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_steps(s :: String.t) :: integer
  def num_steps(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numSteps(s: String): Int64 {

    }
}
```

