# 2578. 最小和分割

## 题目描述

<p>给你一个正整数&nbsp;<code>num</code>&nbsp;，请你将它分割成两个非负整数&nbsp;<code>num1</code> 和&nbsp;<code>num2</code>&nbsp;，满足：</p>

<ul>
	<li><code>num1</code> 和&nbsp;<code>num2</code>&nbsp;直接连起来，得到&nbsp;<code>num</code>&nbsp;各数位的一个排列。

	<ul>
		<li>换句话说，<code>num1</code> 和&nbsp;<code>num2</code>&nbsp;中所有数字出现的次数之和等于&nbsp;<code>num</code>&nbsp;中所有数字出现的次数。</li>
	</ul>
	</li>
	<li><code>num1</code> 和&nbsp;<code>num2</code>&nbsp;可以包含前导 0 。</li>
</ul>

<p>请你返回&nbsp;<code>num1</code> 和 <code>num2</code>&nbsp;可以得到的和的 <strong>最小</strong> 值。</p>

<p><strong>注意：</strong></p>

<ul>
	<li><code>num</code>&nbsp;保证没有前导 0 。</li>
	<li><code>num1</code> 和&nbsp;<code>num2</code>&nbsp;中数位顺序可以与&nbsp;<code>num</code>&nbsp;中数位顺序不同。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>num = 4325
<b>输出：</b>59
<b>解释：</b>我们可以将 4325 分割成 <code>num1 </code>= 24 和 <code>num2 </code>= 35 ，和为 59 ，59 是最小和。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>num = 687
<b>输出：</b>75
<b>解释：</b>我们可以将 687 分割成 <code>num1</code> = 68 和 <code>num2 </code>= 7 ，和为最优值 75 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>10 &lt;= num &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数学
- 排序

## 提示

1. Sort the digits of num in non decreasing order.
2. Assign digits to num1 and num2 alternatively.

## 示例

```
4325
687
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int splitNum(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public int splitNum(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def splitNum(self, num: int) -> int:
        
```

### C

```c
int splitNum(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public int SplitNum(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var splitNum = function(num) {
    
};
```

### TypeScript

```typescript
function splitNum(num: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function splitNum($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func splitNum(_ num: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun splitNum(num: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int splitNum(int num) {
    
  }
}
```

### Go

```golang
func splitNum(num int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def split_num(num)
    
end
```

### Scala

```scala
object Solution {
    def splitNum(num: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn split_num(num: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (split-num num)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec split_num(Num :: integer()) -> integer().
split_num(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec split_num(num :: integer) :: integer
  def split_num(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func splitNum(num: Int64): Int64 {

    }
}
```

