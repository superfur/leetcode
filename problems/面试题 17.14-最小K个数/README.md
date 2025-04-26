# 面试题 17.14. 最小K个数

## 题目描述

<p>设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong> arr = [1,3,5,7,2,4,6,8], k = 4
<strong>输出：</strong> [1,2,3,4]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= len(arr) &lt;= 100000</code></li>
	<li><code>0 &lt;= k &lt;= min(100000, len(arr))</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 分治
- 快速选择
- 排序
- 堆（优先队列）

## 提示

1. 实际上有几种方法。动脑筋想一想。从简单的方法开始也没问题。
2. 考虑以某种方式重新组织数据或者使用其他数据结构。
3. 你能把这些数字排序吗?
4. 使用堆或某种树怎么样?
5. 如果你选了一个任意的元素，那么需要多长时间才能算出它的元素的排序（比它大或比它小的元素的个数）?
6. 如果你选择一个任意的元素，平均来说，就会得到一个在第50百分位数附近的元素（一半的元素比它大，一半的元素比它小）。如果反复这样做呢?
7. 回想一下前面的提示，特别是与快速排序相关的提示。
8. 如果当你选择一个元素时，你交换周围的元素（就像在快速排序中所做的那样），使它所有下方的元素都位于上方的元素之前，那会怎么样？如果你重复做这个，能找到最小的一百万个数吗？

## 示例

```
[1,2,3]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> smallestK(vector<int>& arr, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] smallestK(int[] arr, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* smallestK(int* arr, int arrSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SmallestK(int[] arr, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number[]}
 */
var smallestK = function(arr, k) {
    
};
```

### TypeScript

```typescript
function smallestK(arr: number[], k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer[]
     */
    function smallestK($arr, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestK(_ arr: [Int], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestK(arr: IntArray, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> smallestK(List<int> arr, int k) {
    
  }
}
```

### Go

```golang
func smallestK(arr []int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer[]}
def smallest_k(arr, k)
    
end
```

### Scala

```scala
object Solution {
    def smallestK(arr: Array[Int], k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_k(arr: Vec<i32>, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-k arr k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec smallest_k(Arr :: [integer()], K :: integer()) -> [integer()].
smallest_k(Arr, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_k(arr :: [integer], k :: integer) :: [integer]
  def smallest_k(arr, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestK(arr: Array<Int64>, k: Int64): Array<Int64> {

    }
}
```

