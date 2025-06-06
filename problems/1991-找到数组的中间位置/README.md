# 1991. 找到数组的中间位置

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，请你找到 <strong>最左边</strong>&nbsp;的中间位置&nbsp;<code>middleIndex</code>&nbsp;（也就是所有可能中间位置下标最小的一个）。</p>

<p>中间位置&nbsp;<code>middleIndex</code>&nbsp;是满足&nbsp;<code>nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]</code>&nbsp;的数组下标。</p>

<p>如果&nbsp;<code>middleIndex == 0</code>&nbsp;，左边部分的和定义为 <code>0</code>&nbsp;。类似的，如果&nbsp;<code>middleIndex == nums.length - 1</code>&nbsp;，右边部分的和定义为&nbsp;<code>0</code>&nbsp;。</p>

<p>请你返回满足上述条件 <strong>最左边</strong>&nbsp;的<em>&nbsp;</em><code>middleIndex</code>&nbsp;，如果不存在这样的中间位置，请你返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,3,-1,<em><strong>8</strong></em>,4]
<b>输出：</b>3
<strong>解释：</strong>
下标 3 之前的数字和为：2 + 3 + -1 = 4
下标 3 之后的数字和为：4 = 4
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,-1,<em><strong>4</strong></em>]
<b>输出：</b>2
<strong>解释：</strong>
下标 2 之前的数字和为：1 + -1 = 0
下标 2 之后的数字和为：0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [2,5]
<b>输出：</b>-1
<b>解释：</b>
不存在符合要求的 middleIndex 。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>nums = [<em><strong>1</strong></em>]
<b>输出：</b>0
<strong>解释：</strong>
下标 0 之前的数字和为：0
下标 0 之后的数字和为：0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与主站 724 题相同：<a href="https://leetcode-cn.com/problems/find-pivot-index/" target="_blank">https://leetcode-cn.com/problems/find-pivot-index/</a></p>


## 难度

Easy

## 标签

- 数组
- 前缀和

## 提示

1. Could we go from left to right and check to see if an index is a middle index?
2. Do we need to sum every number to the left and right of an index each time?
3. Use a prefix sum array where prefix[i] = nums[0] + nums[1] + ... + nums[i].

## 示例

```
[2,3,-1,8,4]
[1,-1,4]
[2,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMiddleIndex(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
```

### C

```c
int findMiddleIndex(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMiddleIndex(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMiddleIndex = function(nums) {
    
};
```

### TypeScript

```typescript
function findMiddleIndex(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMiddleIndex($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMiddleIndex(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMiddleIndex(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMiddleIndex(List<int> nums) {
    
  }
}
```

### Go

```golang
func findMiddleIndex(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_middle_index(nums)
    
end
```

### Scala

```scala
object Solution {
    def findMiddleIndex(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_middle_index(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-middle-index nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_middle_index(Nums :: [integer()]) -> integer().
find_middle_index(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_middle_index(nums :: [integer]) :: integer
  def find_middle_index(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMiddleIndex(nums: Array<Int64>): Int64 {

    }
}
```

