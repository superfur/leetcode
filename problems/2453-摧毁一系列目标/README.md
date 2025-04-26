# 2453. 摧毁一系列目标

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的数组&nbsp;<code>nums</code>&nbsp;，它包含若干正整数，表示数轴上你需要摧毁的目标所在的位置。同时给你一个整数&nbsp;<code>space</code>&nbsp;。</p>

<p>你有一台机器可以摧毁目标。给机器 <strong>输入</strong>&nbsp;<code>nums[i]</code>&nbsp;，这台机器会摧毁所有位置在&nbsp;<code>nums[i] + c * space</code>&nbsp;的目标，其中&nbsp;<code>c</code>&nbsp;是任意非负整数。你想摧毁&nbsp;<code>nums</code>&nbsp;中 <strong>尽可能多</strong>&nbsp;的目标。</p>

<p>请你返回在摧毁数目最多的前提下，<code>nums[i]</code>&nbsp;的 <strong>最小值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [3,7,8,1,1,5], space = 2
<b>输出：</b>1
<b>解释：</b>如果我们输入 nums[3] ，我们可以摧毁位于 1,3,5,7,9,... 这些位置的目标。
这种情况下， 我们总共可以摧毁 5 个目标（除了 nums[2]）。
没有办法摧毁多于 5 个目标，所以我们返回 nums[3] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,3,5,2,4,6], space = 2
<b>输出：</b>1
<b>解释：</b>输入 nums[0] 或者 nums[3] 都会摧毁 3 个目标。
没有办法摧毁多于 3 个目标。
由于 nums[0] 是最小的可以摧毁 3 个目标的整数，所以我们返回 1 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [6,2,5], space = 100
<b>输出：</b>2
<b>解释：</b>无论我们输入哪个数字，都只能摧毁 1 个目标。输入的最小整数是 nums[1] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= space &lt;=&nbsp;10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. Keep track of nums[i] modulo k.
2. Iterate over nums in sorted order.

## 示例

```
[3,7,8,1,1,5]
2
[1,3,5,2,4,6]
2
[6,2,5]
100
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int destroyTargets(vector<int>& nums, int space) {
        
    }
};
```

### Java

```java
class Solution {
    public int destroyTargets(int[] nums, int space) {
        
    }
}
```

### Python

```python
class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        
```

### C

```c
int destroyTargets(int* nums, int numsSize, int space) {
    
}
```

### C#

```csharp
public class Solution {
    public int DestroyTargets(int[] nums, int space) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} space
 * @return {number}
 */
var destroyTargets = function(nums, space) {
    
};
```

### TypeScript

```typescript
function destroyTargets(nums: number[], space: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $space
     * @return Integer
     */
    function destroyTargets($nums, $space) {
        
    }
}
```

### Swift

```swift
class Solution {
    func destroyTargets(_ nums: [Int], _ space: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun destroyTargets(nums: IntArray, space: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int destroyTargets(List<int> nums, int space) {
    
  }
}
```

### Go

```golang
func destroyTargets(nums []int, space int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} space
# @return {Integer}
def destroy_targets(nums, space)
    
end
```

### Scala

```scala
object Solution {
    def destroyTargets(nums: Array[Int], space: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn destroy_targets(nums: Vec<i32>, space: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (destroy-targets nums space)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec destroy_targets(Nums :: [integer()], Space :: integer()) -> integer().
destroy_targets(Nums, Space) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec destroy_targets(nums :: [integer], space :: integer) :: integer
  def destroy_targets(nums, space) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func destroyTargets(nums: Array<Int64>, space: Int64): Int64 {

    }
}
```

