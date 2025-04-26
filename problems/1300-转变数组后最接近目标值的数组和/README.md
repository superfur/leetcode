# 1300. 转变数组后最接近目标值的数组和

## 题目描述

<p>给你一个整数数组&nbsp;<code>arr</code> 和一个目标值&nbsp;<code>target</code> ，请你返回一个整数&nbsp;<code>value</code>&nbsp;，使得将数组中所有大于&nbsp;<code>value</code> 的值变成&nbsp;<code>value</code> 后，数组的和最接近&nbsp; <code>target</code>&nbsp;（最接近表示两者之差的绝对值最小）。</p>

<p>如果有多种使得和最接近&nbsp;<code>target</code>&nbsp;的方案，请你返回这些整数中的最小值。</p>

<p>请注意，答案不一定是&nbsp;<code>arr</code> 中的数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [4,9,3], target = 10
<strong>输出：</strong>3
<strong>解释：</strong>当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [2,3,5], target = 10
<strong>输出：</strong>5
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [60864,25176,27249,21296,20204], target = 56803
<strong>输出：</strong>11361
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10^4</code></li>
	<li><code>1 &lt;= arr[i], target &lt;= 10^5</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 排序

## 提示

1. If you draw a graph with the value on one axis and the absolute difference between the target and the array sum, what will you get?
2. That graph is uni-modal.
3. Use ternary search on that graph to find the best value.

## 示例

```
[4,9,3]
10
[2,3,5]
10
[60864,25176,27249,21296,20204]
56803
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findBestValue(vector<int>& arr, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int findBestValue(int[] arr, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
```

### C

```c
int findBestValue(int* arr, int arrSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindBestValue(int[] arr, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var findBestValue = function(arr, target) {
    
};
```

### TypeScript

```typescript
function findBestValue(arr: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $target
     * @return Integer
     */
    function findBestValue($arr, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findBestValue(_ arr: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findBestValue(arr: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findBestValue(List<int> arr, int target) {
    
  }
}
```

### Go

```golang
func findBestValue(arr []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} target
# @return {Integer}
def find_best_value(arr, target)
    
end
```

### Scala

```scala
object Solution {
    def findBestValue(arr: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_best_value(arr: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-best-value arr target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_best_value(Arr :: [integer()], Target :: integer()) -> integer().
find_best_value(Arr, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_best_value(arr :: [integer], target :: integer) :: integer
  def find_best_value(arr, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findBestValue(arr: Array<Int64>, target: Int64): Int64 {

    }
}
```

