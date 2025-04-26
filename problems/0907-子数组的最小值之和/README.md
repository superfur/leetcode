# 907. 子数组的最小值之和

## 题目描述

<p>给定一个整数数组 <code>arr</code>，找到 <code>min(b)</code> 的总和，其中 <code>b</code> 的范围为 <code>arr</code> 的每个（连续）子数组。</p>

<p>由于答案可能很大，因此<strong> 返回答案模 <code>10^9 + 7</code></strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [3,1,2,4]
<strong>输出：</strong>17
<strong>解释：
</strong>子数组为<strong> </strong>[3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [11,81,94,43,3]
<strong>输出：</strong>444
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= arr.length <= 3 * 10<sup>4</sup></code></li>
	<li><code>1 <= arr[i] <= 3 * 10<sup>4</sup></code></li>
</ul>

<p> </p>


## 难度

Medium

## 标签

- 栈
- 数组
- 动态规划
- 单调栈

## 示例

```
[3,1,2,4]
[11,81,94,43,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumSubarrayMins(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
```

### C

```c
int sumSubarrayMins(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumSubarrayMins(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var sumSubarrayMins = function(arr) {
    
};
```

### TypeScript

```typescript
function sumSubarrayMins(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function sumSubarrayMins($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumSubarrayMins(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumSubarrayMins(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumSubarrayMins(List<int> arr) {
    
  }
}
```

### Go

```golang
func sumSubarrayMins(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def sum_subarray_mins(arr)
    
end
```

### Scala

```scala
object Solution {
    def sumSubarrayMins(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_subarray_mins(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-subarray-mins arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_subarray_mins(Arr :: [integer()]) -> integer().
sum_subarray_mins(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_subarray_mins(arr :: [integer]) :: integer
  def sum_subarray_mins(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumSubarrayMins(arr: Array<Int64>): Int64 {

    }
}
```

