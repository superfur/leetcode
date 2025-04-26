# 2848. 与车相交的点

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的二维整数数组 <code>nums</code> 表示汽车停放在数轴上的坐标。对于任意下标 <code>i</code>，<code>nums[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> ，其中 <code>start<sub>i</sub></code> 是第 <code>i</code> 辆车的起点，<code>end<sub>i</sub></code> 是第 <code>i</code> 辆车的终点。</p>

<p>返回数轴上被车 <strong>任意部分</strong> 覆盖的整数点的数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [[3,6],[1,5],[4,7]]
<strong>输出：</strong>7
<strong>解释：</strong>从 1 到 7 的所有点都至少与一辆车相交，因此答案为 7 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [[1,3],[5,8]]
<strong>输出：</strong>7
<strong>解释：</strong>1、2、3、5、6、7、8 共计 7 个点满足至少与一辆车相交，因此答案为 7 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>nums[i].length == 2</code></li>
	<li><code><font face="monospace">1 &lt;= start<sub>i</sub>&nbsp;&lt;= end<sub>i</sub>&nbsp;&lt;= 100</font></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 前缀和

## 提示

1. Sort the array according to first element and then starting from the <code>0<sup>th</sup></code> index remove the overlapping parts and return the count of non-overlapping points.

## 示例

```
[[3,6],[1,5],[4,7]]
[[1,3],[5,8]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfPoints(vector<vector<int>>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfPoints(List<List<Integer>> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
```

### C

```c
int numberOfPoints(int** nums, int numsSize, int* numsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfPoints(IList<IList<int>> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} nums
 * @return {number}
 */
var numberOfPoints = function(nums) {
    
};
```

### TypeScript

```typescript
function numberOfPoints(nums: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $nums
     * @return Integer
     */
    function numberOfPoints($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfPoints(_ nums: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfPoints(nums: List<List<Int>>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfPoints(List<List<int>> nums) {
    
  }
}
```

### Go

```golang
func numberOfPoints(nums [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} nums
# @return {Integer}
def number_of_points(nums)
    
end
```

### Scala

```scala
object Solution {
    def numberOfPoints(nums: List[List[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_points(nums: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-points nums)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_points(Nums :: [[integer()]]) -> integer().
number_of_points(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_points(nums :: [[integer]]) :: integer
  def number_of_points(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfPoints(nums: ArrayList<ArrayList<Int64>>): Int64 {

    }
}
```

