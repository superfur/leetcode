# 728. 自除数

## 题目描述

<p><strong>自除数</strong><em>&nbsp;</em>是指可以被它包含的每一位数整除的数。</p>

<ul>
	<li>例如，<code>128</code> 是一个 <strong>自除数</strong> ，因为&nbsp;<code>128 % 1 == 0</code>，<code>128 % 2 == 0</code>，<code>128 % 8 == 0</code>。</li>
</ul>

<p><strong>自除数</strong> 不允许包含 0 。</p>

<p>给定两个整数&nbsp;<code>left</code>&nbsp;和&nbsp;<code>right</code> ，返回一个列表，<em>列表的元素是范围&nbsp;<code>[left, right]</code>（包括两个端点）内所有的 <strong>自除数</strong></em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>left = 1, right = 22
<strong>输出：</strong>[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<b>输入：</b>left = 47, right = 85
<b>输出：</b>[48,55,66,77]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= left &lt;= right &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. For each number in the range, check whether it is self dividing by converting that number to a character array (or string in Python), then checking that each digit is nonzero and divides the original number.

## 示例

```
1
22
47
85
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        
    }
}
```

### Python

```python
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* selfDividingNumbers(int left, int right, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> SelfDividingNumbers(int left, int right) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    
};
```

### TypeScript

```typescript
function selfDividingNumbers(left: number, right: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer[]
     */
    function selfDividingNumbers($left, $right) {
        
    }
}
```

### Swift

```swift
class Solution {
    func selfDividingNumbers(_ left: Int, _ right: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun selfDividingNumbers(left: Int, right: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> selfDividingNumbers(int left, int right) {
    
  }
}
```

### Go

```golang
func selfDividingNumbers(left int, right int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} left
# @param {Integer} right
# @return {Integer[]}
def self_dividing_numbers(left, right)
    
end
```

### Scala

```scala
object Solution {
    def selfDividingNumbers(left: Int, right: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn self_dividing_numbers(left: i32, right: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (self-dividing-numbers left right)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec self_dividing_numbers(Left :: integer(), Right :: integer()) -> [integer()].
self_dividing_numbers(Left, Right) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec self_dividing_numbers(left :: integer, right :: integer) :: [integer]
  def self_dividing_numbers(left, right) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func selfDividingNumbers(left: Int64, right: Int64): ArrayList<Int64> {

    }
}
```

