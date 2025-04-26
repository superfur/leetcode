# 740. 删除并获得点数

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，你可以对它进行一些操作。</p>

<p>每次操作中，选择任意一个 <code>nums[i]</code> ，删除它并获得 <code>nums[i]</code> 的点数。之后，你必须删除 <strong>所有 </strong>等于 <code>nums[i] - 1</code> 和 <code>nums[i] + 1</code> 的元素。</p>

<p>开始你拥有 <code>0</code> 个点数。返回你能通过这些操作获得的最大点数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,4,2]
<strong>输出：</strong>6
<strong>解释：</strong>
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,3,3,3,4]
<strong>输出：</strong>9
<strong>解释：</strong>
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 2 * 10<sup>4</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 动态规划

## 提示

1. If you take a number, you might as well take them all.  Keep track of what the value is of the subset of the input with maximum M when you either take or don't take M.

## 示例

```
[3,4,2]
[2,2,3,3,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int deleteAndEarn(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
```

### C

```c
int deleteAndEarn(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int DeleteAndEarn(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var deleteAndEarn = function(nums) {
    
};
```

### TypeScript

```typescript
function deleteAndEarn(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function deleteAndEarn($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func deleteAndEarn(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun deleteAndEarn(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int deleteAndEarn(List<int> nums) {
    
  }
}
```

### Go

```golang
func deleteAndEarn(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def delete_and_earn(nums)
    
end
```

### Scala

```scala
object Solution {
    def deleteAndEarn(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn delete_and_earn(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (delete-and-earn nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec delete_and_earn(Nums :: [integer()]) -> integer().
delete_and_earn(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec delete_and_earn(nums :: [integer]) :: integer
  def delete_and_earn(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func deleteAndEarn(nums: Array<Int64>): Int64 {

    }
}
```

