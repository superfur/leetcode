# 1848. 到目标元素的最小距离

## 题目描述

<p>给你一个整数数组 <code>nums</code> （下标 <strong>从 0 开始</strong> 计数）以及两个整数 <code>target</code> 和 <code>start</code> ，请你找出一个下标 <code>i</code> ，满足 <code>nums[i] == target</code> 且 <code>abs(i - start)</code> <strong>最小化</strong> 。注意：<code>abs(x)</code> 表示 <code>x</code> 的绝对值。</p>

<p>返回 <code>abs(i - start)</code> 。</p>

<p>题目数据保证 <code>target</code> 存在于 <code>nums</code> 中。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4,5], target = 5, start = 3
<strong>输出：</strong>1
<strong>解释：</strong>nums[4] = 5 是唯一一个等于 target 的值，所以答案是 abs(4 - 3) = 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1], target = 1, start = 0
<strong>输出：</strong>0
<strong>解释：</strong>nums[0] = 1 是唯一一个等于 target 的值，所以答案是 abs(0 - 0) = 0 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
<strong>输出：</strong>0
<strong>解释：</strong>nums 中的每个值都是 1 ，但 nums[0] 使 abs(i - start) 的结果得以最小化，所以答案是 abs(0 - 0) = 0 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 1000</code></li>
	<li><code>1 <= nums[i] <= 10<sup>4</sup></code></li>
	<li><code>0 <= start < nums.length</code></li>
	<li><code>target</code> 存在于 <code>nums</code> 中</li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Loop in both directions until you find the target element.
2. For each index i such that nums[i] == target calculate abs(i - start).

## 示例

```
[1,2,3,4,5]
5
3
[1]
1
0
[1,1,1,1,1,1,1,1,1,1]
1
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getMinDistance(vector<int>& nums, int target, int start) {
        
    }
};
```

### Java

```java
class Solution {
    public int getMinDistance(int[] nums, int target, int start) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
```

### C

```c
int getMinDistance(int* nums, int numsSize, int target, int start) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetMinDistance(int[] nums, int target, int start) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @param {number} start
 * @return {number}
 */
var getMinDistance = function(nums, target, start) {
    
};
```

### TypeScript

```typescript
function getMinDistance(nums: number[], target: number, start: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @param Integer $start
     * @return Integer
     */
    function getMinDistance($nums, $target, $start) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getMinDistance(_ nums: [Int], _ target: Int, _ start: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMinDistance(nums: IntArray, target: Int, start: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getMinDistance(List<int> nums, int target, int start) {
    
  }
}
```

### Go

```golang
func getMinDistance(nums []int, target int, start int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @param {Integer} start
# @return {Integer}
def get_min_distance(nums, target, start)
    
end
```

### Scala

```scala
object Solution {
    def getMinDistance(nums: Array[Int], target: Int, start: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_min_distance(nums: Vec<i32>, target: i32, start: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-min-distance nums target start)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec get_min_distance(Nums :: [integer()], Target :: integer(), Start :: integer()) -> integer().
get_min_distance(Nums, Target, Start) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_min_distance(nums :: [integer], target :: integer, start :: integer) :: integer
  def get_min_distance(nums, target, start) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getMinDistance(nums: Array<Int64>, target: Int64, start: Int64): Int64 {

    }
}
```

