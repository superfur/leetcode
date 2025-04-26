# 1480. 一维数组的动态和

## 题目描述

<p>给你一个数组 <code>nums</code> 。数组「动态和」的计算公式为：<code>runningSum[i] = sum(nums[0]&hellip;nums[i])</code> 。</p>

<p>请返回 <code>nums</code> 的动态和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>[1,3,6,10]
<strong>解释：</strong>动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,1,1,1,1]
<strong>输出：</strong>[1,2,3,4,5]
<strong>解释：</strong>动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [3,1,2,10,1]
<strong>输出：</strong>[3,4,6,16,17]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10^6&nbsp;&lt;= nums[i] &lt;=&nbsp;10^6</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 前缀和

## 提示

1. Think about how we can calculate the i-th number in the running sum from the (i-1)-th number.

## 示例

```
[1,2,3,4]
[1,1,1,1,1]
[3,1,2,10,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] runningSum(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] RunningSum(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    
};
```

### TypeScript

```typescript
function runningSum(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function runningSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func runningSum(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun runningSum(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> runningSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func runningSum(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def running_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def runningSum(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (running-sum nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec running_sum(Nums :: [integer()]) -> [integer()].
running_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec running_sum(nums :: [integer]) :: [integer]
  def running_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func runningSum(nums: Array<Int64>): Array<Int64> {

    }
}
```

