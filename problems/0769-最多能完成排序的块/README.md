# 769. 最多能完成排序的块

## 题目描述

<p>给定一个长度为 <code>n</code> 的整数数组 <code>arr</code> ，它表示在 <code>[0, n - 1]</code> 范围内的整数的排列。</p>

<p>我们将 <code>arr</code> 分割成若干 <strong>块</strong> (即分区)，并对每个块单独排序。将它们连接起来后，使得连接的结果和按升序排序后的原数组相同。</p>

<p>返回数组能分成的最多块数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> arr = [4,3,2,1,0]
<strong>输出:</strong> 1
<strong>解释:</strong>
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> arr = [1,0,2,3,4]
<strong>输出:</strong> 4
<strong>解释:</strong>
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
对每个块单独排序后，结果为 [0, 1], [2], [3], [4]
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>n == arr.length</code></li>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>0 &lt;= arr[i] &lt; n</code></li>
	<li><code>arr</code>&nbsp;中每个元素都 <strong>不同</strong></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 数组
- 排序
- 单调栈

## 提示

1. The first chunk can be found as the smallest k for which A[:k+1] == [0, 1, 2, ...k]; then we repeat this process.

## 示例

```
[4,3,2,1,0]
[1,0,2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxChunksToSorted(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
```

### C

```c
int maxChunksToSorted(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxChunksToSorted(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var maxChunksToSorted = function(arr) {
    
};
```

### TypeScript

```typescript
function maxChunksToSorted(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function maxChunksToSorted($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxChunksToSorted(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxChunksToSorted(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxChunksToSorted(List<int> arr) {
    
  }
}
```

### Go

```golang
func maxChunksToSorted(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def max_chunks_to_sorted(arr)
    
end
```

### Scala

```scala
object Solution {
    def maxChunksToSorted(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_chunks_to_sorted(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-chunks-to-sorted arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_chunks_to_sorted(Arr :: [integer()]) -> integer().
max_chunks_to_sorted(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_chunks_to_sorted(arr :: [integer]) :: integer
  def max_chunks_to_sorted(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxChunksToSorted(arr: Array<Int64>): Int64 {

    }
}
```

