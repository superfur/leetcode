# 1186. 删除一次得到子数组最大和

## 题目描述

<p>给你一个整数数组，返回它的某个&nbsp;<strong>非空</strong> 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。</p>

<p>注意，删除一个元素后，子数组 <strong>不能为空</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,-2,0,3]
<strong>输出：</strong>4
<strong>解释：</strong>我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,-2,-2,3]
<strong>输出：</strong>3
<strong>解释：</strong>我们直接选出 [3]，这就是最大和。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [-1,-1,-1,-1]
<strong>输出：</strong>-1
<strong>解释：</strong>最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
     我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>
<meta charset="UTF-8" />

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. How to solve this problem if no deletions are allowed ?
2. Try deleting each element and find the maximum subarray sum to both sides of that element.
3. To do that efficiently, use the idea of Kadane's algorithm.

## 示例

```
[1,-2,0,3]
[1,-2,-2,3]
[-1,-1,-1,-1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumSum(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumSum(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        
```

### C

```c
int maximumSum(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumSum(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var maximumSum = function(arr) {
    
};
```

### TypeScript

```typescript
function maximumSum(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function maximumSum($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSum(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSum(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumSum(List<int> arr) {
    
  }
}
```

### Go

```golang
func maximumSum(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def maximum_sum(arr)
    
end
```

### Scala

```scala
object Solution {
    def maximumSum(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_sum(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-sum arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_sum(Arr :: [integer()]) -> integer().
maximum_sum(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_sum(arr :: [integer]) :: integer
  def maximum_sum(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSum(arr: Array<Int64>): Int64 {

    }
}
```

