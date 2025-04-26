# 面试题 16.16. 部分排序

## 题目描述

<p>给定一个整数数组，编写一个函数，找出索引<code>m</code>和<code>n</code>，只要将索引区间<code>[m,n]</code>的元素排好序，整个数组就是有序的。注意：<code>n-m</code>尽量最小，也就是说，找出符合条件的最短序列。函数返回值为<code>[m,n]</code>，若不存在这样的<code>m</code>和<code>n</code>（例如整个数组是有序的），请返回<code>[-1,-1]</code>。</p>
<p><strong>示例：</strong></p>
<pre><strong>输入：</strong> [1,2,4,7,10,11,7,12,6,7,16,18,19]
<strong>输出：</strong> [3,9]
</pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>0 <= len(array) <= 1000000</code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 数组
- 双指针
- 排序
- 单调栈

## 提示

1. 在开始和结束时知道最长的排序序列会有帮助吗？
2. 我们可以把这个数组分成3个子数组：LEFT、MIDDLE和RIGHT。LEFT和RIGHT都是有序的。MIDDLE的元素顺序是任意的。我们需要展开MIDDLE，直到可以对这些元素排序并使整个数组有序。
3. 考虑3个子数组：LEFT、MIDDLE和RIGHT。只关注这个问题：是否可以排序MIDDLE以使整个数组有序？如何进行验证？
4. 为了能够对MIDDLE进行排序并对整个数组进行排序，需要MAX(LEFT) <= MIN(MIDDLE, RIGHT)和MAX(LEFT, MIDDLE) <= MIN(RIGHT)。
5. 你能把中间部分展开直到满足前面的条件吗？
6. 你应该能在O(N)时间内解出来。

## 示例

```
[]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> subSort(vector<int>& array) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] subSort(int[] array) {
        
    }
}
```

### Python

```python
class Solution(object):
    def subSort(self, array):
        """
        :type array: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* subSort(int* array, int arraySize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SubSort(int[] array) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} array
 * @return {number[]}
 */
var subSort = function(array) {
    
};
```

### TypeScript

```typescript
function subSort(array: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $array
     * @return Integer[]
     */
    function subSort($array) {
        
    }
}
```

### Swift

```swift
class Solution {
    func subSort(_ array: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subSort(array: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> subSort(List<int> array) {
    
  }
}
```

### Go

```golang
func subSort(array []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} array
# @return {Integer[]}
def sub_sort(array)
    
end
```

### Scala

```scala
object Solution {
    def subSort(array: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sub_sort(array: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (sub-sort array)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec sub_sort(Array :: [integer()]) -> [integer()].
sub_sort(Array) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sub_sort(array :: [integer]) :: [integer]
  def sub_sort(array) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func subSort(array: Array<Int64>): Array<Int64> {

    }
}
```

