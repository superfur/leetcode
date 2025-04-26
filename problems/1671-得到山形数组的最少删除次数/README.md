# 1671. 得到山形数组的最少删除次数

## 题目描述

<p>我们定义&nbsp;<code>arr</code>&nbsp;是 <b>山形数组</b>&nbsp;当且仅当它满足：</p>

<ul>
	<li><code>arr.length &gt;= 3</code></li>
	<li>存在某个下标&nbsp;<code>i</code>&nbsp;（<strong>从 0 开始</strong>）&nbsp;满足&nbsp;<code>0 &lt; i &lt; arr.length - 1</code>&nbsp;且：
	<ul>
		<li><code>arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i]</code></li>
		<li><code>arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1]</code></li>
	</ul>
	</li>
</ul>

<p>给你整数数组&nbsp;<code>nums</code>​ ，请你返回将 <code>nums</code>&nbsp;变成 <strong>山形状数组</strong>&nbsp;的​ <strong>最少</strong>&nbsp;删除次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,3,1]
<b>输出：</b>0
<b>解释：</b>数组本身就是山形数组，所以我们不需要删除任何元素。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2,1,1,5,6,2,3,1]
<b>输出：</b>3
<b>解释：</b>一种方法是将下标为 0，1 和 5 的元素删除，剩余元素为 [1,5,6,3,1] ，是山形数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>题目保证&nbsp;<code>nums</code> 删除一些元素后一定能得到山形数组。</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 二分查找
- 动态规划

## 提示

1. Think the opposite direction instead of minimum elements to remove the maximum mountain subsequence
2. Think of LIS it's kind of close

## 示例

```
[1,3,1]
[2,1,1,5,6,2,3,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumMountainRemovals(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumMountainRemovals(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
```

### C

```c
int minimumMountainRemovals(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumMountainRemovals(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumMountainRemovals = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumMountainRemovals(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumMountainRemovals($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumMountainRemovals(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumMountainRemovals(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumMountainRemovals(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumMountainRemovals(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_mountain_removals(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumMountainRemovals(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_mountain_removals(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-mountain-removals nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_mountain_removals(Nums :: [integer()]) -> integer().
minimum_mountain_removals(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_mountain_removals(nums :: [integer]) :: integer
  def minimum_mountain_removals(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumMountainRemovals(nums: Array<Int64>): Int64 {

    }
}
```

