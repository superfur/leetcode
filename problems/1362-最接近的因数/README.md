# 1362. 最接近的因数

## 题目描述

<p>给你一个整数&nbsp;<code>num</code>，请你找出同时满足下面全部要求的两个整数：</p>

<ul>
	<li>两数乘积等于 &nbsp;<code>num + 1</code>&nbsp;或&nbsp;<code>num + 2</code></li>
	<li>以绝对差进行度量，两数大小最接近</li>
</ul>

<p>你可以按任意顺序返回这两个整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>num = 8
<strong>输出：</strong>[3,3]
<strong>解释：</strong>对于 num + 1 = 9，最接近的两个因数是 3 &amp; 3；对于 num + 2 = 10, 最接近的两个因数是 2 &amp; 5，因此返回 3 &amp; 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>num = 123
<strong>输出：</strong>[5,25]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>num = 999
<strong>输出：</strong>[40,25]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10^9</code></li>
</ul>


## 难度

Medium

## 标签

- 数学

## 提示

1. Find the divisors of n+1 and n+2.
2. To find the divisors of a number, you only need to iterate to the square root of that number.

## 示例

```
8
123
999
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> closestDivisors(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] closestDivisors(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* closestDivisors(int num, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ClosestDivisors(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number[]}
 */
var closestDivisors = function(num) {
    
};
```

### TypeScript

```typescript
function closestDivisors(num: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer[]
     */
    function closestDivisors($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func closestDivisors(_ num: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun closestDivisors(num: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> closestDivisors(int num) {
    
  }
}
```

### Go

```golang
func closestDivisors(num int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer[]}
def closest_divisors(num)
    
end
```

### Scala

```scala
object Solution {
    def closestDivisors(num: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn closest_divisors(num: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (closest-divisors num)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec closest_divisors(Num :: integer()) -> [integer()].
closest_divisors(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec closest_divisors(num :: integer) :: [integer]
  def closest_divisors(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func closestDivisors(num: Int64): Array<Int64> {

    }
}
```

