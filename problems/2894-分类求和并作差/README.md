# 2894. 分类求和并作差

## 题目描述

<p>给你两个正整数 <code>n</code> 和 <code>m</code> 。</p>

<p>现定义两个整数 <code>num1</code> 和 <code>num2</code> ，如下所示：</p>

<ul>
	<li><code>num1</code>：范围 <code>[1, n]</code> 内所有 <strong>无法被 </strong><code>m</code><strong> 整除</strong> 的整数之和。</li>
	<li><code>num2</code>：范围 <code>[1, n]</code> 内所有 <strong>能够被 </strong><code>m</code><strong> 整除</strong> 的整数之和。</li>
</ul>

<p>返回整数 <code>num1 - num2</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 10, m = 3
<strong>输出：</strong>19
<strong>解释：</strong>在这个示例中：
- 范围 [1, 10] 内无法被 3 整除的整数为 [1,2,4,5,7,8,10] ，num1 = 这些整数之和 = 37 。
- 范围 [1, 10] 内能够被 3 整除的整数为 [3,6,9] ，num2 = 这些整数之和 = 18 。
返回 37 - 18 = 19 作为答案。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 5, m = 6
<strong>输出：</strong>15
<strong>解释：</strong>在这个示例中：
- 范围 [1, 5] 内无法被 6 整除的整数为 [1,2,3,4,5] ，num1 = 这些整数之和 =  15 。
- 范围 [1, 5] 内能够被 6 整除的整数为 [] ，num2 = 这些整数之和 = 0 。
返回 15 - 0 = 15 作为答案。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 5, m = 1
<strong>输出：</strong>-15
<strong>解释：</strong>在这个示例中：
- 范围 [1, 5] 内无法被 1 整除的整数为 [] ，num1 = 这些整数之和 = 0 。 
- 范围 [1, 5] 内能够被 1 整除的整数为 [1,2,3,4,5] ，num2 = 这些整数之和 = 15 。
返回 0 - 15 = -15 作为答案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. With arithmetic progression we know that the sum of integers in the range <code>[1, n]</code> is <code>n * (n + 1) / 2 </code>.

## 示例

```
10
3
5
6
5
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int differenceOfSums(int n, int m) {
        
    }
};
```

### Java

```java
class Solution {
    public int differenceOfSums(int n, int m) {
        
    }
}
```

### Python

```python
class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
```

### C

```c
int differenceOfSums(int n, int m) {
    
}
```

### C#

```csharp
public class Solution {
    public int DifferenceOfSums(int n, int m) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var differenceOfSums = function(n, m) {
    
};
```

### TypeScript

```typescript
function differenceOfSums(n: number, m: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @return Integer
     */
    function differenceOfSums($n, $m) {
        
    }
}
```

### Swift

```swift
class Solution {
    func differenceOfSums(_ n: Int, _ m: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun differenceOfSums(n: Int, m: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int differenceOfSums(int n, int m) {
    
  }
}
```

### Go

```golang
func differenceOfSums(n int, m int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} m
# @return {Integer}
def difference_of_sums(n, m)
    
end
```

### Scala

```scala
object Solution {
    def differenceOfSums(n: Int, m: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn difference_of_sums(n: i32, m: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (difference-of-sums n m)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec difference_of_sums(N :: integer(), M :: integer()) -> integer().
difference_of_sums(N, M) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec difference_of_sums(n :: integer, m :: integer) :: integer
  def difference_of_sums(n, m) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func differenceOfSums(n: Int64, m: Int64): Int64 {

    }
}
```

