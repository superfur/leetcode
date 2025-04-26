# 2202. K 次操作后最大化顶端元素

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，它表示一个 <strong>堆</strong> ，其中 <code>nums[0]</code>&nbsp;是堆顶的元素。</p>

<p>每一次操作中，你可以执行以下操作 <strong>之一</strong>&nbsp;：</p>

<ul>
	<li>如果堆非空，那么 <strong>删除</strong>&nbsp;堆顶端的元素。</li>
	<li>如果存在 1 个或者多个被删除的元素，你可以从它们中选择任何一个，<b>添加</b>&nbsp;回堆顶，这个元素成为新的堆顶元素。</li>
</ul>

<p>同时给你一个整数&nbsp;<code>k</code>&nbsp;，它表示你总共需要执行操作的次数。</p>

<p>请你返回 <strong>恰好</strong>&nbsp;执行 <code>k</code>&nbsp;次操作以后，堆顶元素的 <strong>最大值</strong>&nbsp;。如果执行完 <code>k</code>&nbsp;次操作以后，堆一定为空，请你返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [5,2,2,4,0,6], k = 4
<b>输出：</b>5
<strong>解释：</strong>
4 次操作后，堆顶元素为 5 的方法之一为：
- 第 1 次操作：删除堆顶元素 5 ，堆变为 [2,2,4,0,6] 。
- 第 2 次操作：删除堆顶元素 2 ，堆变为 [2,4,0,6] 。
- 第 3 次操作：删除堆顶元素 2 ，堆变为 [4,0,6] 。
- 第 4 次操作：将 5 添加回堆顶，堆变为 [5,4,0,6] 。
注意，这不是最后堆顶元素为 5 的唯一方式。但可以证明，4 次操作以后 5 是能得到的最大堆顶元素。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2], k = 1
<b>输出：</b>-1
<b>解释：</b>
第 1 次操作中，我们唯一的选择是将堆顶元素弹出堆。
由于 1 次操作后无法得到一个非空的堆，所以我们返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i], k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组

## 提示

1. For each index i, how can we check if nums[i] can be present at the top of the pile or not after k moves?
2. For which conditions will we end up with an empty pile?

## 示例

```
[5,2,2,4,0,6]
4
[2]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumTop(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumTop(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int maximumTop(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumTop(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumTop = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maximumTop(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maximumTop($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumTop(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumTop(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumTop(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maximumTop(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_top(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumTop(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_top(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-top nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_top(Nums :: [integer()], K :: integer()) -> integer().
maximum_top(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_top(nums :: [integer], k :: integer) :: integer
  def maximum_top(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumTop(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

