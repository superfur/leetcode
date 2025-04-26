# 915. 分割数组

## 题目描述

<p>给定一个数组&nbsp;<code>nums</code>&nbsp;，将其划分为两个连续子数组&nbsp;<code>left</code>&nbsp;和&nbsp;<code>right</code>，&nbsp;使得：</p>

<ul>
	<li><code>left</code>&nbsp;中的每个元素都小于或等于&nbsp;<code>right</code>&nbsp;中的每个元素。</li>
	<li><code>left</code> 和&nbsp;<code>right</code>&nbsp;都是非空的。</li>
	<li><code>left</code> 的长度要尽可能小。</li>
</ul>

<p><em>在完成这样的分组后返回&nbsp;<code>left</code>&nbsp;的&nbsp;<strong>长度&nbsp;</strong></em>。</p>

<p>用例可以保证存在这样的划分方法。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,0,3,8,6]
<strong>输出：</strong>3
<strong>解释：</strong>left = [5,0,3]，right = [8,6]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,0,6,12]
<strong>输出：</strong>4
<strong>解释：</strong>left = [1,1,1,0]，right = [6,12]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li>可以保证至少有一种方法能够按题目所描述的那样对 <code>nums</code> 进行划分。</li>
</ul>


## 难度

Medium

## 标签

- 数组

## 示例

```
[5,0,3,8,6]
[1,1,1,0,6,12]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int partitionDisjoint(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        
```

### C

```c
int partitionDisjoint(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int PartitionDisjoint(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var partitionDisjoint = function(nums) {
    
};
```

### TypeScript

```typescript
function partitionDisjoint(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function partitionDisjoint($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func partitionDisjoint(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun partitionDisjoint(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int partitionDisjoint(List<int> nums) {
    
  }
}
```

### Go

```golang
func partitionDisjoint(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def partition_disjoint(nums)
    
end
```

### Scala

```scala
object Solution {
    def partitionDisjoint(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn partition_disjoint(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (partition-disjoint nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec partition_disjoint(Nums :: [integer()]) -> integer().
partition_disjoint(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec partition_disjoint(nums :: [integer]) :: integer
  def partition_disjoint(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func partitionDisjoint(nums: Array<Int64>): Int64 {

    }
}
```

