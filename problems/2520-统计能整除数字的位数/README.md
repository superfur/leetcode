# 2520. 统计能整除数字的位数

## 题目描述

<p>给你一个整数 <code>num</code> ，返回 <code>num</code> 中能整除 <code>num</code> 的数位的数目。</p>

<p>如果满足&nbsp;<code>nums % val == 0</code> ，则认为整数 <code>val</code> 可以整除 <code>nums</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>num = 7
<strong>输出：</strong>1
<strong>解释：</strong>7 被自己整除，因此答案是 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>num = 121
<strong>输出：</strong>2
<strong>解释：</strong>121 可以被 1 整除，但无法被 2 整除。由于 1 出现两次，所以返回 2 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>num = 1248
<strong>输出：</strong>4
<strong>解释：</strong>1248 可以被它每一位上的数字整除，因此答案是 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>9</sup></code></li>
	<li><code>num</code> 的数位中不含 <code>0</code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. Use mod by 10 to retrieve the least significant digit of the number
2. Divide the number by 10, then round it down so that the second least significant digit becomes the least significant digit of the number
3. Use your language’s mod operator to see if a number is a divisor of another.

## 示例

```
7
121
1248
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countDigits(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public int countDigits(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countDigits(self, num: int) -> int:
        
```

### C

```c
int countDigits(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountDigits(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var countDigits = function(num) {
    
};
```

### TypeScript

```typescript
function countDigits(num: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function countDigits($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countDigits(_ num: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countDigits(num: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countDigits(int num) {
    
  }
}
```

### Go

```golang
func countDigits(num int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def count_digits(num)
    
end
```

### Scala

```scala
object Solution {
    def countDigits(num: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_digits(num: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-digits num)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_digits(Num :: integer()) -> integer().
count_digits(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_digits(num :: integer) :: integer
  def count_digits(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countDigits(num: Int64): Int64 {

    }
}
```

