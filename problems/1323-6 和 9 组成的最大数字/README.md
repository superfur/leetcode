# 1323. 6 和 9 组成的最大数字

## 题目描述

<p>给你一个仅由数字 6 和 9 组成的正整数&nbsp;<code>num</code>。</p>

<p>你最多只能翻转一位数字，将 6 变成&nbsp;9，或者把&nbsp;9 变成&nbsp;6 。</p>

<p>请返回你可以得到的最大数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>num = 9669
<strong>输出：</strong>9969
<strong>解释：</strong>
改变第一位数字可以得到 6669 。
改变第二位数字可以得到 9969 。
改变第三位数字可以得到 9699 。
改变第四位数字可以得到 9666 。
其中最大的数字是 9969 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>num = 9996
<strong>输出：</strong>9999
<strong>解释：</strong>将最后一位从 6 变到 9，其结果 9999 是最大的数。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>num = 9999
<strong>输出：</strong>9999
<strong>解释：</strong>无需改变就已经是最大的数字了。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10^4</code></li>
	<li><code>num</code>&nbsp;每一位上的数字都是 6 或者&nbsp;9 。</li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数学

## 提示

1. Convert the number in an array of its digits.
2. Brute force on every digit to get the maximum number.

## 示例

```
9669
9996
9999
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximum69Number (int num) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximum69Number (int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximum69Number (self, num: int) -> int:
        
```

### C

```c
int maximum69Number (int num) {
    
}
```

### C#

```csharp
public class Solution {
    public int Maximum69Number (int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number  = function(num) {
    
};
```

### TypeScript

```typescript
function maximum69Number (num: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function maximum69Number ($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximum69Number (_ num: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximum69Number (num: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximum69Number (int num) {
    
  }
}
```

### Go

```golang
func maximum69Number (num int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def maximum69_number (num)
    
end
```

### Scala

```scala
object Solution {
    def maximum69Number (num: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum69_number (num: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum69-number  num)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum69_number (Num :: integer()) -> integer().
maximum69_number (Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum69_number (num :: integer) :: integer
  def maximum69_number (num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximum69Number (num: Int64): Int64 {

    }
}
```

