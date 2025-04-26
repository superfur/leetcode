# 面试题 16.01. 交换数字

## 题目描述

<p>编写一个函数，不用临时变量，直接交换<code>numbers = [a, b]</code>中<code>a</code>与<code>b</code>的值。</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入:</strong> numbers = [1,2]
<strong>输出:</strong> [2,1]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>numbers.length == 2</code></li>
	<li><code>-2147483647 <= numbers[i] <= 2147483647</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数学

## 提示

1. 尝试在数轴上画出a和b两个数字。
2. 定义diff为a和b之间的差。你能以某种方式使用diff吗？那么你能去掉这个临时变量吗？
3. 你也可以尝试使用XOR。

## 示例

```
[0,2147483647]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> swapNumbers(vector<int>& numbers) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] swapNumbers(int[] numbers) {
        
    }
}
```

### Python

```python
class Solution(object):
    def swapNumbers(self, numbers):
        """
        :type numbers: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* swapNumbers(int* numbers, int numbersSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SwapNumbers(int[] numbers) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} numbers
 * @return {number[]}
 */
var swapNumbers = function(numbers) {
    
};
```

### TypeScript

```typescript
function swapNumbers(numbers: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $numbers
     * @return Integer[]
     */
    function swapNumbers($numbers) {
        
    }
}
```

### Swift

```swift
class Solution {
    func swapNumbers(_ numbers: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun swapNumbers(numbers: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> swapNumbers(List<int> numbers) {
    
  }
}
```

### Go

```golang
func swapNumbers(numbers []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} numbers
# @return {Integer[]}
def swap_numbers(numbers)
    
end
```

### Scala

```scala
object Solution {
    def swapNumbers(numbers: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn swap_numbers(numbers: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (swap-numbers numbers)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec swap_numbers(Numbers :: [integer()]) -> [integer()].
swap_numbers(Numbers) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec swap_numbers(numbers :: [integer]) :: [integer]
  def swap_numbers(numbers) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func swapNumbers(numbers: Array<Int64>): Array<Int64> {

    }
}
```

