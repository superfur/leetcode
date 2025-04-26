# 81. 搜索旋转排序数组 II

## 题目描述

<p>已知存在一个按非降序排列的整数数组 <code>nums</code> ，数组中的值不必互不相同。</p>

<p>在传递给函数之前，<code>nums</code> 在预先未知的某个下标 <code>k</code>（<code>0 &lt;= k &lt; nums.length</code>）上进行了 <strong>旋转 </strong>，使数组变为 <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code>（下标 <strong>从 0 开始</strong> 计数）。例如， <code>[0,1,2,4,4,4,5,6,6,7]</code> 在下标 <code>5</code> 处经旋转后可能变为 <code>[4,5,6,6,7,0,1,2,4,4]</code> 。</p>

<p>给你 <strong>旋转后</strong> 的数组 <code>nums</code> 和一个整数 <code>target</code> ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 <code>nums</code> 中存在这个目标值 <code>target</code> ，则返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p>你必须尽可能减少整个操作步骤。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>nums = <code>[2,5,6,0,0,1,2]</code>, target = 0
<strong>输出：</strong>true
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>nums = <code>[2,5,6,0,0,1,2]</code>, target = 3
<strong>输出：</strong>false</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li>题目数据保证 <code>nums</code> 在预先未知的某个下标上进行了旋转</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>此题与&nbsp;<a href="https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/">搜索旋转排序数组</a>&nbsp;相似，但本题中的&nbsp;<code>nums</code>&nbsp; 可能包含 <strong>重复</strong> 元素。这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？</li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 示例

```
[2,5,6,0,0,1,2]
0
[2,5,6,0,0,1,2]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean search(int[] nums, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
```

### C

```c
bool search(int* nums, int numsSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public bool Search(int[] nums, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function(nums, target) {
    
};
```

### TypeScript

```typescript
function search(nums: number[], target: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Boolean
     */
    function search($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func search(_ nums: [Int], _ target: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun search(nums: IntArray, target: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool search(List<int> nums, int target) {
    
  }
}
```

### Go

```golang
func search(nums []int, target int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Boolean}
def search(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def search(nums: Array[Int], target: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (search nums target)
  (-> (listof exact-integer?) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec search(Nums :: [integer()], Target :: integer()) -> boolean().
search(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec search(nums :: [integer], target :: integer) :: boolean
  def search(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func search(nums: Array<Int64>, target: Int64): Bool {

    }
}
```

