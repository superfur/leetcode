# 2180. 统计各位数字之和为偶数的整数个数

## 题目描述

<p>给你一个正整数 <code>num</code> ，请你统计并返回 <strong>小于或等于</strong> <code>num</code> 且各位数字之和为 <strong>偶数</strong> 的正整数的数目。</p>

<p>正整数的 <strong>各位数字之和</strong> 是其所有位上的对应数字相加的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = 4
<strong>输出：</strong>2
<strong>解释：</strong>
只有 2 和 4 满足小于等于 4 且各位数字之和为偶数。    
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = 30
<strong>输出：</strong>14
<strong>解释：</strong>
只有 14 个整数满足小于等于 30 且各位数字之和为偶数，分别是： 
2、4、6、8、11、13、15、17、19、20、22、24、26 和 28 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 模拟

## 提示

1. Iterate through all integers from 1 to num.
2. For any integer, extract the individual digits to compute their sum and check if it is even.

## 示例

```
4
30
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countEven(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public int countEven(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countEven(self, num: int) -> int:
        
```

### C

```c
int countEven(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountEven(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var countEven = function(num) {
    
};
```

### TypeScript

```typescript
function countEven(num: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function countEven($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countEven(_ num: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countEven(num: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countEven(int num) {
    
  }
}
```

### Go

```golang
func countEven(num int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def count_even(num)
    
end
```

### Scala

```scala
object Solution {
    def countEven(num: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_even(num: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-even num)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_even(Num :: integer()) -> integer().
count_even(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_even(num :: integer) :: integer
  def count_even(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countEven(num: Int64): Int64 {

    }
}
```

