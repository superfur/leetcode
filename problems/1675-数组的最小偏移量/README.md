# 1675. 数组的最小偏移量

## 题目描述

<p>给你一个由 <code>n</code> 个正整数组成的数组 <code>nums</code> 。</p>

<p>你可以对数组的任意元素执行任意次数的两类操作：</p>

<ul>
	<li>如果元素是<strong> 偶数</strong> ，<strong>除以</strong> <code>2</code>

	<ul>
		<li>例如，如果数组是 <code>[1,2,3,4]</code> ，那么你可以对最后一个元素执行此操作，使其变成 <code>[1,2,3,<strong>2</strong>]</code></li>
	</ul>
	</li>
	<li>如果元素是 <strong>奇数</strong> ，<strong>乘上</strong> <code>2</code>
	<ul>
		<li>例如，如果数组是 <code>[1,2,3,4]</code> ，那么你可以对第一个元素执行此操作，使其变成 <code>[<strong>2</strong>,2,3,4]</code></li>
	</ul>
	</li>
</ul>

<p>数组的 <strong>偏移量</strong> 是数组中任意两个元素之间的 <strong>最大差值</strong> 。</p>

<p>返回数组在执行某些操作之后可以拥有的 <strong>最小偏移量</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>1
<strong>解释：</strong>你可以将数组转换为 [1,2,3,<strong>2</strong>]，然后转换成 [<strong>2</strong>,2,3,2]，偏移量是 3 - 2 = 1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,1,5,20,3]
<strong>输出：</strong>3
<strong>解释：</strong>两次操作后，你可以将数组转换为 [4,<strong>2</strong>,5,<strong>5</strong>,3]，偏移量是 5 - 2 = 3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,10,8]
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n &lt;= 5 * 10<sup><span style="font-size: 10.8333px;">4</span></sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 有序集合
- 堆（优先队列）

## 提示

1. Assume you start with the minimum possible value for each number so you can only multiply a number by 2 till it reaches its maximum possible value.
2. If there is a better solution than the current one, then it must have either its maximum value less than the current maximum value, or the minimum value larger than the current minimum value.
3. Since that we only increase numbers (multiply them by 2), we cannot decrease the current maximum value, so we must multiply the current minimum number by 2.

## 示例

```
[1,2,3,4]
[4,1,5,20,3]
[2,10,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumDeviation(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
```

### C

```c
int minimumDeviation(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumDeviation(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDeviation = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumDeviation(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumDeviation($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumDeviation(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumDeviation(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumDeviation(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumDeviation(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_deviation(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumDeviation(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_deviation(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-deviation nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_deviation(Nums :: [integer()]) -> integer().
minimum_deviation(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_deviation(nums :: [integer]) :: integer
  def minimum_deviation(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumDeviation(nums: Array<Int64>): Int64 {

    }
}
```

