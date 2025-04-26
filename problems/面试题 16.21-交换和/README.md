# 面试题 16.21. 交换和

## 题目描述

<p>给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。</p>

<p>返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
<strong>输出：</strong>[1, 3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>array1 = <code>[1, 2, 3], array2 = [4, 5, 6]</code>
<strong>输出：</strong>[]</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= array1.length, array2.length &lt;= 100000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 二分查找
- 排序

## 提示

1. 在这里用一些例子做些数学计算。这一对数值有什么需求？你发现它们的值有什么特点？
2. 当你把一个值a从数组A移动到数组B时，A的和减少了a, B的和增加了a。当你交换两个值时会发生什么？交换两个值并得到相同的和需要什么？
3. 如果你交换两个值，即a和b，那么A的和变成sumA - a + b，而B的和变成sumB - b + a。这两个和需要相等。
4. 你在寻找a和b的值，其中sumA - a + b = sumB - b + a。用数学方法算出这对a和b的值意味着什么。
5. 如果计算一下，那我们要找一对这样的值，即a - b = (sumA - sumB) / 2。然后，问题归结为寻找具有特定差的一对值。
6. 一种蛮力解法是遍历所有的数值对，以找到一个具有正确差值的数值对。这可能看起来为：对A进行外循环，对B进行内循环。对于每个值，计算差值并与目标差值进行比较。能说得更具体些吗？给定A中的值和目标差，可以知道要找的B中的元素的确切值吗?
7. 蛮力解法其实是在B中寻找一个等于a - target的值。你如何能更快地找到这个元素？什么方法可以帮助我们快速找到数组中是否存在某个元素?
8. 可以用散列表，也可以尝试排序。两者都能帮助我们更快地定位元素。
9. 如果A的和是11，B的和是8呢？能有一对数刚好有目标差吗？检查你的解决方案是否恰当地处理了这种情况。

## 示例

```
[4, 1, 2, 1, 1, 2]
[3, 6, 3, 3]
[1, 2, 3]
[4, 5, 6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findSwapValues(vector<int>& array1, vector<int>& array2) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findSwapValues(int[] array1, int[] array2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findSwapValues(self, array1, array2):
        """
        :type array1: List[int]
        :type array2: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findSwapValues(int* array1, int array1Size, int* array2, int array2Size, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindSwapValues(int[] array1, int[] array2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} array1
 * @param {number[]} array2
 * @return {number[]}
 */
var findSwapValues = function(array1, array2) {
    
};
```

### TypeScript

```typescript
function findSwapValues(array1: number[], array2: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $array1
     * @param Integer[] $array2
     * @return Integer[]
     */
    function findSwapValues($array1, $array2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findSwapValues(_ array1: [Int], _ array2: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findSwapValues(array1: IntArray, array2: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findSwapValues(List<int> array1, List<int> array2) {
    
  }
}
```

### Go

```golang
func findSwapValues(array1 []int, array2 []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} array1
# @param {Integer[]} array2
# @return {Integer[]}
def find_swap_values(array1, array2)
    
end
```

### Scala

```scala
object Solution {
    def findSwapValues(array1: Array[Int], array2: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_swap_values(array1: Vec<i32>, array2: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-swap-values array1 array2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_swap_values(Array1 :: [integer()], Array2 :: [integer()]) -> [integer()].
find_swap_values(Array1, Array2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_swap_values(array1 :: [integer], array2 :: [integer]) :: [integer]
  def find_swap_values(array1, array2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findSwapValues(array1: Array<Int64>, array2: Array<Int64>): Array<Int64> {

    }
}
```

