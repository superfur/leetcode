# 457. 环形数组是否存在循环

## 题目描述

<p>存在一个不含 <code>0</code> 的<strong> 环形 </strong>数组&nbsp;<code>nums</code> ，每个 <code>nums[i]</code> 都表示位于下标 <code>i</code> 的角色应该向前或向后移动的下标个数：</p>

<ul>
	<li>如果 <code>nums[i]</code> 是正数，<strong>向前</strong>（下标递增方向）移动 <code>|nums[i]|</code> 步</li>
	<li>如果&nbsp;<code>nums[i]</code> 是负数，<strong>向后</strong>（下标递减方向）移动 <code>|nums[i]|</code> 步</li>
</ul>

<p>因为数组是 <strong>环形</strong> 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。</p>

<p>数组中的 <strong>循环</strong> 由长度为 <code>k</code> 的下标序列 <code>seq</code> 标识：</p>

<ul>
	<li>遵循上述移动规则将导致一组重复下标序列 <code>seq[0] -&gt; seq[1] -&gt; ... -&gt; seq[k - 1] -&gt; seq[0] -&gt; ...</code></li>
	<li>所有 <code>nums[seq[j]]</code> 应当不是 <strong>全正</strong> 就是 <strong>全负</strong></li>
	<li><code>k &gt; 1</code></li>
</ul>

<p>如果 <code>nums</code> 中存在循环，返回 <code>true</code> ；否则，返回<em> </em><code>false</code><em> </em>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1723688159-qYjpWT-image.png" style="width: 402px; height: 289px;" />
<pre>
<strong>输入：</strong>nums = [2,-1,1,2,2]
<strong>输出：</strong>true
<strong>解释：</strong>图片展示了节点间如何连接。白色节点向前跳跃，而红色节点向后跳跃。
我们可以看到存在循环，按下标 0 -&gt; 2 -&gt; 3 -&gt; 0 --&gt; ...，并且其中的所有节点都是白色（以相同方向跳跃）。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1723688183-lRSkjp-image.png" style="width: 402px; height: 390px;" />
<pre>
<strong>输入：</strong>nums = [-1,-2,-3,-4,-5,6]
<strong>输出：</strong>false
<strong>解释：</strong>图片展示了节点间如何连接。白色节点向前跳跃，而红色节点向后跳跃。
唯一的循环长度为 1，所以返回 false。
</pre>

<p><strong class="example">示例 3：</strong></p>
<img alt="" src="https://pic.leetcode.cn/1723688199-nhaMuF-image.png" style="width: 497px; height: 242px;" />
<pre>
<strong>输入：</strong>nums = [1,-1,5,1,4]
<strong>输出：</strong>true
<strong>解释：</strong>图片展示了节点间如何连接。白色节点向前跳跃，而红色节点向后跳跃。
我们可以看到存在循环，按下标 0 --&gt; 1 --&gt; 0 --&gt; ...，当它的大小大于 1 时，它有一个向前跳的节点和一个向后跳的节点，所以 <strong>它不是一个循环</strong>。
我们可以看到存在循环，按下标 3 --&gt; 4 --&gt; 3 --&gt; ...，并且其中的所有节点都是白色（以相同方向跳跃）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>nums[i] != 0</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能设计一个时间复杂度为 <code>O(n)</code> 且额外空间复杂度为 <code>O(1)</code> 的算法吗？</p>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 双指针

## 示例

```
[2,-1,1,2,2]
[-1,-2,-3,-4,-5,6]
[1,-1,5,1,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool circularArrayLoop(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean circularArrayLoop(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
```

### C

```c
bool circularArrayLoop(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CircularArrayLoop(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var circularArrayLoop = function(nums) {
    
};
```

### TypeScript

```typescript
function circularArrayLoop(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function circularArrayLoop($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func circularArrayLoop(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun circularArrayLoop(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool circularArrayLoop(List<int> nums) {
    
  }
}
```

### Go

```golang
func circularArrayLoop(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def circular_array_loop(nums)
    
end
```

### Scala

```scala
object Solution {
    def circularArrayLoop(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn circular_array_loop(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (circular-array-loop nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec circular_array_loop(Nums :: [integer()]) -> boolean().
circular_array_loop(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec circular_array_loop(nums :: [integer]) :: boolean
  def circular_array_loop(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func circularArrayLoop(nums: Array<Int64>): Bool {

    }
}
```

