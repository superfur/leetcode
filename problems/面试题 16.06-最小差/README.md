# 面试题 16.06. 最小差

## 题目描述

<p>给定两个整数数组<code>a</code>和<code>b</code>，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差</p>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
<strong>输出：</strong>3，即数值对(11, 8)
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= a.length, b.length <= 100000</code></li>
	<li><code>-2147483648 <= a[i], b[i] <= 2147483647</code></li>
	<li>正确结果在区间 <code>[0, 2147483647]</code> 内</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 二分查找
- 排序

## 提示

1. 如果你对数组排序呢?
2. 考虑如何合并两个有序数组。
3. 假设你把两个数组排序，然后遍历它们。如果第一个数组中的指针指向3，第二个数组中的指针指向9，那么移动第二个指针会对这一对数字的差产生什么影响?

## 示例

```
[0]
[2147483647]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int smallestDifference(vector<int>& a, vector<int>& b) {
        
    }
};
```

### Java

```java
class Solution {
    public int smallestDifference(int[] a, int[] b) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestDifference(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        
```

### C

```c
int smallestDifference(int* a, int aSize, int* b, int bSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SmallestDifference(int[] a, int[] b) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} a
 * @param {number[]} b
 * @return {number}
 */
var smallestDifference = function(a, b) {
    
};
```

### TypeScript

```typescript
function smallestDifference(a: number[], b: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $a
     * @param Integer[] $b
     * @return Integer
     */
    function smallestDifference($a, $b) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestDifference(_ a: [Int], _ b: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestDifference(a: IntArray, b: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int smallestDifference(List<int> a, List<int> b) {
    
  }
}
```

### Go

```golang
func smallestDifference(a []int, b []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer}
def smallest_difference(a, b)
    
end
```

### Scala

```scala
object Solution {
    def smallestDifference(a: Array[Int], b: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_difference(a: Vec<i32>, b: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-difference a b)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec smallest_difference(A :: [integer()], B :: [integer()]) -> integer().
smallest_difference(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_difference(a :: [integer], b :: [integer]) :: integer
  def smallest_difference(a, b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestDifference(a: Array<Int64>, b: Array<Int64>): Int64 {

    }
}
```

