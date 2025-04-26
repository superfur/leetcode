# 315. 计算右侧小于当前元素的个数

## 题目描述

<p>给你一个整数数组 <code>nums</code><em> </em>，按要求返回一个新数组&nbsp;<code>counts</code><em> </em>。数组 <code>counts</code> 有该性质： <code>counts[i]</code> 的值是&nbsp; <code>nums[i]</code> 右侧小于&nbsp;<code>nums[i]</code> 的元素的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,2,6,1]
<strong>输出：</strong><code>[2,1,1,0] 
<strong>解释：</strong></code>
5 的右侧有 <strong>2 </strong>个更小的元素 (2 和 1)
2 的右侧仅有 <strong>1 </strong>个更小的元素 (1)
6 的右侧有 <strong>1 </strong>个更小的元素 (1)
1 的右侧有 <strong>0 </strong>个更小的元素
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1]
<strong>输出：</strong>[0]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,-1]
<strong>输出：</strong>[0,0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 线段树
- 数组
- 二分查找
- 分治
- 有序集合
- 归并排序

## 示例

```
[5,2,6,1]
[-1]
[-1,-1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> countSmaller(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countSmaller(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> CountSmaller(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var countSmaller = function(nums) {
    
};
```

### TypeScript

```typescript
function countSmaller(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function countSmaller($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSmaller(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSmaller(nums: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countSmaller(List<int> nums) {
    
  }
}
```

### Go

```golang
func countSmaller(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def count_smaller(nums)
    
end
```

### Scala

```scala
object Solution {
    def countSmaller(nums: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_smaller(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (count-smaller nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_smaller(Nums :: [integer()]) -> [integer()].
count_smaller(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_smaller(nums :: [integer]) :: [integer]
  def count_smaller(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSmaller(nums: Array<Int64>): ArrayList<Int64> {

    }
}
```

