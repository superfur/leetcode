# 768. 最多能完成排序的块 II

## 题目描述

<p>给你一个整数数组 <code>arr</code> 。</p>

<p>将 <code>arr</code> 分割成若干 <strong>块</strong> ，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。</p>

<p>返回能将数组分成的最多块数？</p>
&nbsp;

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [5,4,3,2,1]
<strong>输出：</strong>1
<strong>解释：</strong>
将数组分成2块或者更多块，都无法得到所需的结果。 
例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。 
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [2,1,3,4,4]
<strong>输出：</strong>4
<strong>解释：</strong>
可以把它分成两块，例如 [2, 1], [3, 4, 4]。 
然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 2000</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>8</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 贪心
- 数组
- 排序
- 单调栈

## 提示

1. Each k for which some permutation of arr[:k] is equal to sorted(arr)[:k] is where we should cut each chunk.

## 示例

```
[5,4,3,2,1]
[2,1,3,4,4]
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

