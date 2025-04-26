# 2844. 生成特殊数字的最少操作

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>num</code> ，表示一个非负整数。</p>

<p>在一次操作中，您可以选择 <code>num</code> 的任意一位数字并将其删除。请注意，如果你删除 <code>num</code> 中的所有数字，则 <code>num</code> 变为 <code>0</code>。</p>

<p>返回最少需要多少次操作可以使 <code>num</code> 变成特殊数字。</p>

<p>如果整数 <code>x</code> 能被 <code>25</code> 整除，则该整数 <code>x</code> 被认为是特殊数字。</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = "2245047"
<strong>输出：</strong>2
<strong>解释：</strong>删除数字 num[5] 和 num[6] ，得到数字 "22450" ，可以被 25 整除。
可以证明要使数字变成特殊数字，最少需要删除 2 位数字。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = "2908305"
<strong>输出：</strong>3
<strong>解释：</strong>删除 num[3]、num[4] 和 num[6] ，得到数字 "2900" ，可以被 25 整除。
可以证明要使数字变成特殊数字，最少需要删除 3 位数字。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>num = "10"
<strong>输出：</strong>1
<strong>解释：</strong>删除 num[0] ，得到数字 "0" ，可以被 25 整除。
可以证明要使数字变成特殊数字，最少需要删除 1 位数字。
</pre>

<p>&nbsp;</p>

<p><strong>提示</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 100</code></li>
	<li><code>num</code> 仅由数字 <code>'0'</code> 到 <code>'9'</code> 组成</li>
	<li><code>num</code> 不含任何前导零</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学
- 字符串
- 枚举

## 提示

1. If <code>num</code> contains a single zero digit then the answer is at most <code>n - 1</code>.
2. A number is divisible by <code>25</code> if its last two digits are <code>75</code>, <code>50</code>, <code>25</code>, or <code>00</code>.
3. Iterate over all possible pairs of indices <code>i &lt; j</code> such that <code>num[i] * 10 + num[j]</code> is in <code>[00,25,50,75]</code>. Then, set the answer to <code> min(answer, n - i - 2) </code>.

## 示例

```
"2245047"
"2908305"
"10"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumOperations(string num) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumOperations(String num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumOperations(self, num):
        """
        :type num: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumOperations(self, num: str) -> int:
        
```

### C

```c
int minimumOperations(char* num) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumOperations(string num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @return {number}
 */
var minimumOperations = function(num) {
    
};
```

### TypeScript

```typescript
function minimumOperations(num: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @return Integer
     */
    function minimumOperations($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumOperations(_ num: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumOperations(num: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumOperations(String num) {
    
  }
}
```

### Go

```golang
func minimumOperations(num string) int {
    
}
```

### Ruby

```ruby
# @param {String} num
# @return {Integer}
def minimum_operations(num)
    
end
```

### Scala

```scala
object Solution {
    def minimumOperations(num: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_operations(num: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-operations num)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_operations(Num :: unicode:unicode_binary()) -> integer().
minimum_operations(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(num :: String.t) :: integer
  def minimum_operations(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumOperations(num: String): Int64 {

    }
}
```

