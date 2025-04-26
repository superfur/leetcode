# 2117. 一个区间内所有数乘积的缩写

## 题目描述

<p>给你两个正整数&nbsp;<code>left</code>&nbsp;和&nbsp;<code>right</code>&nbsp;，满足&nbsp;<code>left &lt;= right</code>&nbsp;。请你计算&nbsp;<strong>闭区间</strong>&nbsp;<code>[left, right]</code>&nbsp;中所有整数的&nbsp;<strong>乘积</strong>&nbsp;。</p>

<p>由于乘积可能非常大，你需要将它按照以下步骤 <strong>缩写</strong>&nbsp;：</p>

<ol>
	<li>统计乘积中&nbsp;<strong>后缀</strong> 0 的数目，并 <strong>移除</strong> 这些 0 ，将这个数目记为&nbsp;<code>C</code>&nbsp;。

	<ul>
		<li>比方说，<code>1000</code>&nbsp;中有 <code>3</code> 个后缀 0&nbsp;，<code>546</code>&nbsp;中没有后缀 0 。</li>
	</ul>
	</li>
	<li>将乘积中剩余数字的位数记为&nbsp;<code>d</code>&nbsp;。如果&nbsp;<code>d &gt; 10</code>&nbsp;，那么将乘积表示为&nbsp;<code>&lt;pre&gt;...&lt;suf&gt;</code>&nbsp;的形式，其中&nbsp;<code>&lt;pre&gt;</code>&nbsp;表示乘积最 <strong>开始</strong>&nbsp;的 <code>5</code>&nbsp;个数位，<code>&lt;suf&gt;</code>&nbsp;表示删除后缀 0 <strong>之后</strong>&nbsp;结尾的 <code>5</code>&nbsp;个数位。如果&nbsp;<code>d &lt;= 10</code>&nbsp;，我们不对它做修改。
	<ul>
		<li>比方说，我们将&nbsp;<code>1234567654321</code>&nbsp;表示为&nbsp;<code>12345...54321</code>&nbsp;，但是&nbsp;<code>1234567</code>&nbsp;仍然表示为&nbsp;<code>1234567</code>&nbsp;。</li>
	</ul>
	</li>
	<li>最后，将乘积表示为 <strong>字符串</strong>&nbsp;<code>"&lt;pre&gt;...&lt;suf&gt;eC"</code>&nbsp;。
	<ul>
		<li>比方说，<code>12345678987600000</code>&nbsp;被表示为&nbsp;<code>"12345...89876e5"</code>&nbsp;。</li>
	</ul>
	</li>
</ol>

<p>请你返回一个字符串，表示 <strong>闭区间</strong>&nbsp;<code>[left, right]</code>&nbsp;中所有整数&nbsp;<strong>乘积</strong>&nbsp;的&nbsp;<strong>缩写</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>left = 1, right = 4
<b>输出：</b>"24e0"
<strong>解释：</strong>
乘积为 1 × 2 × 3 × 4 = 24 。
由于没有后缀 0 ，所以 24 保持不变，缩写的结尾为 "e0" 。
因为乘积的结果是 2 位数，小于 10 ，所欲我们不进一步将它缩写。
所以，最终将乘积表示为 "24e0" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>left = 2, right = 11
<strong>输出：</strong>"399168e2"
<strong>解释：</strong>乘积为 39916800 。
有 2 个后缀 0 ，删除后得到 399168 。缩写的结尾为 "e2" 。 
删除后缀 0 后是 6 位数，不需要进一步缩写。 
所以，最终将乘积表示为 "399168e2" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>left = 371, right = 375
<strong>输出：</strong>"7219856259e3"
<strong>解释：</strong>乘积为 7219856259000 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= left &lt;= right &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数学

## 提示

1. Calculating the number of trailing zeros, the last five digits, and the first five digits can all be done separately.
2. Use a prime factorization property to find the number of trailing zeros. Use modulo to find the last 5 digits. Use a logarithm property to find the first 5 digits.
3. The number of trailing zeros C is nothing but the number of times the product is completely divisible by 10. Since 2 and 5 are the only prime factors of 10,  C will be equal to the minimum number of times 2 or 5 appear in the prime factorization of the product.
4. Iterate through the integers from left to right. For every integer, keep dividing it by 2 as long as it is divisible by 2 and C occurrences of 2 haven't been removed in total. Repeat this process for 5. Finally, multiply the integer under modulo of 10^5 with the product obtained till now to obtain the last five digits.
5. The product P can be represented as P=10^(x+y) where x is the integral part and y is the fractional part of x+y. Using the property "if S = A * B, then log(S) = log(A) + log(B)", we can write x+y = log_10(P) = sum(log_10(i)) for each integer i in [left, right]. Once we obtain the sum, the first five digits can be represented as floor(10^(y+4)).

## 示例

```
1
4
2
11
371
375
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string abbreviateProduct(int left, int right) {
        
    }
};
```

### Java

```java
class Solution {
    public String abbreviateProduct(int left, int right) {
        
    }
}
```

### Python

```python
class Solution(object):
    def abbreviateProduct(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        
```

### C

```c
char* abbreviateProduct(int left, int right) {
    
}
```

### C#

```csharp
public class Solution {
    public string AbbreviateProduct(int left, int right) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} left
 * @param {number} right
 * @return {string}
 */
var abbreviateProduct = function(left, right) {
    
};
```

### TypeScript

```typescript
function abbreviateProduct(left: number, right: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $left
     * @param Integer $right
     * @return String
     */
    function abbreviateProduct($left, $right) {
        
    }
}
```

### Swift

```swift
class Solution {
    func abbreviateProduct(_ left: Int, _ right: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun abbreviateProduct(left: Int, right: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String abbreviateProduct(int left, int right) {
    
  }
}
```

### Go

```golang
func abbreviateProduct(left int, right int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} left
# @param {Integer} right
# @return {String}
def abbreviate_product(left, right)
    
end
```

### Scala

```scala
object Solution {
    def abbreviateProduct(left: Int, right: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn abbreviate_product(left: i32, right: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (abbreviate-product left right)
  (-> exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec abbreviate_product(Left :: integer(), Right :: integer()) -> unicode:unicode_binary().
abbreviate_product(Left, Right) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec abbreviate_product(left :: integer, right :: integer) :: String.t
  def abbreviate_product(left, right) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func abbreviateProduct(left: Int64, right: Int64): String {

    }
}
```

