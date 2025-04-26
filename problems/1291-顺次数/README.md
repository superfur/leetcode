# 1291. 顺次数

## 题目描述

<p>我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 <code>1</code> 的整数。</p>

<p>请你返回由&nbsp;<code>[low, high]</code>&nbsp;范围内所有顺次数组成的 <strong>有序</strong> 列表（从小到大排序）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输出：</strong>low = 100, high = 300
<strong>输出：</strong>[123,234]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输出：</strong>low = 1000, high = 13000
<strong>输出：</strong>[1234,2345,3456,4567,5678,6789,12345]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>10 &lt;= low &lt;= high &lt;= 10^9</code></li>
</ul>


## 难度

Medium

## 标签

- 枚举

## 提示

1. Generate all numbers with sequential digits and check if they are in the given range.
2. Fix the starting digit then do a recursion that tries to append all valid digits.

## 示例

```
100
300
1000
13000
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sequentialDigits(int low, int high, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> SequentialDigits(int low, int high) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low, high) {
    
};
```

### TypeScript

```typescript
function sequentialDigits(low: number, high: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer[]
     */
    function sequentialDigits($low, $high) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sequentialDigits(_ low: Int, _ high: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sequentialDigits(low: Int, high: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> sequentialDigits(int low, int high) {
    
  }
}
```

### Go

```golang
func sequentialDigits(low int, high int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} low
# @param {Integer} high
# @return {Integer[]}
def sequential_digits(low, high)
    
end
```

### Scala

```scala
object Solution {
    def sequentialDigits(low: Int, high: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (sequential-digits low high)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec sequential_digits(Low :: integer(), High :: integer()) -> [integer()].
sequential_digits(Low, High) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sequential_digits(low :: integer, high :: integer) :: [integer]
  def sequential_digits(low, high) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sequentialDigits(low: Int64, high: Int64): ArrayList<Int64> {

    }
}
```

