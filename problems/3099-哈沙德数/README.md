# 3099. 哈沙德数

## 题目描述

<p>如果一个整数能够被其各个数位上的数字之和整除，则称之为<strong> 哈沙德数</strong>（Harshad number）。给你一个整数 <code>x</code> 。如果 <code>x</code> 是 <strong>哈沙德数 </strong>，则返回<em> </em><code>x</code> 各个数位上的数字之和，否则，返回<em> </em><code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">x = 18</span></p>

<p><strong>输出：</strong> <span class="example-io">9</span></p>

<p><strong>解释：</strong></p>

<p><code>x</code> 各个数位上的数字之和为 <code>9</code> 。<code>18</code> 能被 <code>9</code> 整除。因此 <code>18</code> 是哈沙德数，答案是 <code>9</code> 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">x = 23</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<p><code>x</code> 各个数位上的数字之和为 <code>5</code> 。<code>23</code> 不能被 <code>5</code> 整除。因此 <code>23</code> 不是哈沙德数，答案是 <code>-1</code> 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. Use a while loop and divide <code>x</code> by <code>10</code> to find the sum of the digits of <code>x</code>.

## 示例

```
18
23
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
```

### C

```c
int sumOfTheDigitsOfHarshadNumber(int x) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumOfTheDigitsOfHarshadNumber(int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} x
 * @return {number}
 */
var sumOfTheDigitsOfHarshadNumber = function(x) {
    
};
```

### TypeScript

```typescript
function sumOfTheDigitsOfHarshadNumber(x: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $x
     * @return Integer
     */
    function sumOfTheDigitsOfHarshadNumber($x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumOfTheDigitsOfHarshadNumber(_ x: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumOfTheDigitsOfHarshadNumber(x: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumOfTheDigitsOfHarshadNumber(int x) {
    
  }
}
```

### Go

```golang
func sumOfTheDigitsOfHarshadNumber(x int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} x
# @return {Integer}
def sum_of_the_digits_of_harshad_number(x)
    
end
```

### Scala

```scala
object Solution {
    def sumOfTheDigitsOfHarshadNumber(x: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_of_the_digits_of_harshad_number(x: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-of-the-digits-of-harshad-number x)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_of_the_digits_of_harshad_number(X :: integer()) -> integer().
sum_of_the_digits_of_harshad_number(X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_of_the_digits_of_harshad_number(x :: integer) :: integer
  def sum_of_the_digits_of_harshad_number(x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumOfTheDigitsOfHarshadNumber(x: Int64): Int64 {

    }
}
```

