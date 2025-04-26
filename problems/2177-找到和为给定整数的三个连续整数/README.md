# 2177. 找到和为给定整数的三个连续整数

## 题目描述

<p>给你一个整数&nbsp;<code>num</code>&nbsp;，请你返回三个连续的整数，它们的&nbsp;<strong>和</strong>&nbsp;为<em>&nbsp;</em><code>num</code>&nbsp;。如果&nbsp;<code>num</code>&nbsp;无法被表示成三个连续整数的和，请你返回一个 <strong>空</strong>&nbsp;数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>num = 33
<b>输出：</b>[10,11,12]
<b>解释：</b>33 可以表示为 10 + 11 + 12 = 33 。
10, 11, 12 是 3 个连续整数，所以返回 [10, 11, 12] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>num = 4
<b>输出：</b>[]
<b>解释：</b>没有办法将 4 表示成 3 个连续整数的和。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 10<sup>15</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 模拟

## 提示

1. Notice that if a solution exists, we can represent them as x-1, x, x+1. What does this tell us about the number?
2. Notice the sum of the numbers will be 3x. Can you solve for x?

## 示例

```
33
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> sumOfThree(long long num) {
        
    }
};
```

### Java

```java
class Solution {
    public long[] sumOfThree(long num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* sumOfThree(long long num, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long[] SumOfThree(long num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number[]}
 */
var sumOfThree = function(num) {
    
};
```

### TypeScript

```typescript
function sumOfThree(num: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer[]
     */
    function sumOfThree($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumOfThree(_ num: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumOfThree(num: Long): LongArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> sumOfThree(int num) {
    
  }
}
```

### Go

```golang
func sumOfThree(num int64) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer[]}
def sum_of_three(num)
    
end
```

### Scala

```scala
object Solution {
    def sumOfThree(num: Long): Array[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_of_three(num: i64) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (sum-of-three num)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec sum_of_three(Num :: integer()) -> [integer()].
sum_of_three(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_of_three(num :: integer) :: [integer]
  def sum_of_three(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumOfThree(num: Int64): Array<Int64> {

    }
}
```

