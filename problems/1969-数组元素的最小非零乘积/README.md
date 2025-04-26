# 1969. 数组元素的最小非零乘积

## 题目描述

<p>给你一个正整数&nbsp;<code>p</code>&nbsp;。你有一个下标从 <strong>1</strong>&nbsp;开始的数组&nbsp;<code>nums</code>&nbsp;，这个数组包含范围&nbsp;<code>[1, 2<sup>p</sup> - 1]</code>&nbsp;内所有整数的二进制形式（两端都 <strong>包含</strong>）。你可以进行以下操作 <strong>任意</strong>&nbsp;次：</p>

<ul>
	<li>从 <code>nums</code>&nbsp;中选择两个元素&nbsp;<code>x</code>&nbsp;和&nbsp;<code>y</code>&nbsp; 。</li>
	<li>选择 <code>x</code>&nbsp;中的一位与 <code>y</code>&nbsp;对应位置的位交换。对应位置指的是两个整数 <strong>相同位置</strong>&nbsp;的二进制位。</li>
</ul>

<p>比方说，如果&nbsp;<code>x = 11<em><strong>0</strong></em>1</code>&nbsp;且&nbsp;<code>y = 00<em><strong>1</strong></em>1</code>&nbsp;，交换右边数起第 <code>2</code>&nbsp;位后，我们得到&nbsp;<code>x = 11<em><strong>1</strong></em>1</code> 和&nbsp;<code>y = 00<em><strong>0</strong></em>1</code>&nbsp;。</p>

<p>请你算出进行以上操作 <strong>任意次</strong>&nbsp;以后，<code>nums</code>&nbsp;能得到的 <strong>最小非零</strong>&nbsp;乘积。将乘积对<em>&nbsp;</em><code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong> 后返回。</p>

<p><strong>注意：</strong>答案应为取余 <strong>之前</strong>&nbsp;的最小值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>p = 1
<b>输出：</b>1
<b>解释：</b>nums = [1] 。
只有一个元素，所以乘积为该元素。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>p = 2
<b>输出：</b>6
<b>解释：</b>nums = [01, 10, 11] 。
所有交换要么使乘积变为 0 ，要么乘积与初始乘积相同。
所以，数组乘积 1 * 2 * 3 = 6 已经是最小值。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>p = 3
<b>输出：</b>1512
<b>解释：</b>nums = [001, 010, 011, 100, 101, 110, 111]
- 第一次操作中，我们交换第二个和第五个元素最左边的数位。
    - 结果数组为 [001, <em><strong>1</strong></em>10, 011, 100, <em><strong>0</strong></em>01, 110, 111] 。
- 第二次操作中，我们交换第三个和第四个元素中间的数位。
    - 结果数组为 [001, 110, 0<em><strong>0</strong></em>1, 1<em><strong>1</strong></em>0, 001, 110, 111] 。
数组乘积 1 * 6 * 1 * 6 * 1 * 6 * 7 = 1512 是最小乘积。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= p &lt;= 60</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 递归
- 数学

## 提示

1. Try to minimize each element by swapping bits with any of the elements after it.
2. If you swap out all the 1s in some element, this will lead to a product of zero.

## 示例

```
1
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minNonZeroProduct(int p) {
        
    }
};
```

### Java

```java
class Solution {
    public int minNonZeroProduct(int p) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        
```

### C

```c
int minNonZeroProduct(int p) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinNonZeroProduct(int p) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} p
 * @return {number}
 */
var minNonZeroProduct = function(p) {
    
};
```

### TypeScript

```typescript
function minNonZeroProduct(p: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $p
     * @return Integer
     */
    function minNonZeroProduct($p) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minNonZeroProduct(_ p: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minNonZeroProduct(p: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minNonZeroProduct(int p) {
    
  }
}
```

### Go

```golang
func minNonZeroProduct(p int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} p
# @return {Integer}
def min_non_zero_product(p)
    
end
```

### Scala

```scala
object Solution {
    def minNonZeroProduct(p: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_non_zero_product(p: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-non-zero-product p)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_non_zero_product(P :: integer()) -> integer().
min_non_zero_product(P) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_non_zero_product(p :: integer) :: integer
  def min_non_zero_product(p) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minNonZeroProduct(p: Int64): Int64 {

    }
}
```

