# 2121. 相同元素的间隔之和

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、由 <code>n</code> 个整数组成的数组 <code>arr</code> 。</p>

<p><code>arr</code> 中两个元素的 <strong>间隔</strong> 定义为它们下标之间的 <strong>绝对差</strong> 。更正式地，<code>arr[i]</code> 和 <code>arr[j]</code> 之间的间隔是 <code>|i - j|</code> 。</p>

<p>返回一个长度为 <code>n</code> 的数组&nbsp;<code>intervals</code> ，其中 <code>intervals[i]</code> 是<em> </em><code>arr[i]</code><em> </em>和<em> </em><code>arr</code><em> </em>中每个相同元素（与 <code>arr[i]</code> 的值相同）的 <strong>间隔之和</strong> <em>。</em></p>

<p><strong>注意：</strong><code>|x|</code> 是 <code>x</code> 的绝对值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [2,1,3,1,2,3,3]
<strong>输出：</strong>[4,2,7,2,4,4,5]
<strong>解释：</strong>
- 下标 0 ：另一个 2 在下标 4 ，|0 - 4| = 4
- 下标 1 ：另一个 1 在下标 3 ，|1 - 3| = 2
- 下标 2 ：另两个 3 在下标 5 和 6 ，|2 - 5| + |2 - 6| = 7
- 下标 3 ：另一个 1 在下标 1 ，|3 - 1| = 2
- 下标 4 ：另一个 2 在下标 0 ，|4 - 0| = 4
- 下标 5 ：另两个 3 在下标 2 和 6 ，|5 - 2| + |5 - 6| = 4
- 下标 6 ：另两个 3 在下标 2 和 5 ，|6 - 2| + |6 - 5| = 5
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [10,5,10,10]
<strong>输出：</strong>[5,0,3,4]
<strong>解释：</strong>
- 下标 0 ：另两个 10 在下标 2 和 3 ，|0 - 2| + |0 - 3| = 5
- 下标 1 ：只有这一个 5 在数组中，所以到相同元素的间隔之和是 0
- 下标 2 ：另两个 10 在下标 0 和 3 ，|2 - 0| + |2 - 3| = 3
- 下标 3 ：另两个 10 在下标 0 和 2 ，|3 - 0| + |3 - 2| = 4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == arr.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和

## 提示

1. For each unique value found in the array, store a sorted list of indices of elements that have this value in the array.
2. One way of doing this is to use a HashMap that maps the values to their list of indices. Update this mapping as you iterate through the array.
3. Process each list of indices separately and get the sum of intervals for the elements of that value by utilizing prefix sums.
4. For each element, keep track of the sum of indices of the identical elements that have come before and that will come after respectively. Use this to calculate the sum of intervals for that element to the rest of the elements with identical values.

## 示例

```
[2,1,3,1,2,3,3]
[10,5,10,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> getDistances(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public long[] getDistances(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* getDistances(int* arr, int arrSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long[] GetDistances(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var getDistances = function(arr) {
    
};
```

### TypeScript

```typescript
function getDistances(arr: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function getDistances($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getDistances(_ arr: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getDistances(arr: IntArray): LongArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getDistances(List<int> arr) {
    
  }
}
```

### Go

```golang
func getDistances(arr []int) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer[]}
def get_distances(arr)
    
end
```

### Scala

```scala
object Solution {
    def getDistances(arr: Array[Int]): Array[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_distances(arr: Vec<i32>) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (get-distances arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_distances(Arr :: [integer()]) -> [integer()].
get_distances(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_distances(arr :: [integer]) :: [integer]
  def get_distances(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getDistances(arr: Array<Int64>): Array<Int64> {

    }
}
```

