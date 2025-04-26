# 594. 最长和谐子序列

## 题目描述

<p>和谐数组是指一个数组里元素的最大值和最小值之间的差别 <strong>正好是 <code>1</code></strong> 。</p>

<p>给你一个整数数组 <code>nums</code> ，请你在所有可能的 <span data-keyword="subsequence-array">子序列</span> 中找到最长的和谐子序列的长度。</p>

<p>数组的 <strong>子序列</strong> 是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,3,2,2,5,2,3,7]</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><strong>解释：</strong></p>

<p>最长和谐子序列是&nbsp;<code>[3,2,2,2,3]</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>最长和谐子序列是&nbsp;<code>[1,2]</code>，<code>[2,3]</code>&nbsp;和&nbsp;<code>[3,4]</code>，长度都为 2。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,1,1,1]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<p>不存在和谐子序列。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 计数
- 排序
- 滑动窗口

## 示例

```
[1,3,2,2,5,2,3,7]
[1,2,3,4]
[1,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findLHS(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findLHS(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
```

### C

```c
int findLHS(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindLHS(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findLHS = function(nums) {
    
};
```

### TypeScript

```typescript
function findLHS(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findLHS($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLHS(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLHS(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findLHS(List<int> nums) {
    
  }
}
```

### Go

```golang
func findLHS(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_lhs(nums)
    
end
```

### Scala

```scala
object Solution {
    def findLHS(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_lhs(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-lhs nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_lhs(Nums :: [integer()]) -> integer().
find_lhs(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_lhs(nums :: [integer]) :: integer
  def find_lhs(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLHS(nums: Array<Int64>): Int64 {

    }
}
```

