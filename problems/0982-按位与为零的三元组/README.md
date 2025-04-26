# 982. 按位与为零的三元组

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，返回其中 <strong>按位与三元组</strong> 的数目。</p>

<p><strong>按位与三元组</strong> 是由下标 <code>(i, j, k)</code> 组成的三元组，并满足下述全部条件：</p>

<ul>
	<li><code>0 &lt;= i &lt; nums.length</code></li>
	<li><code>0 &lt;= j &lt; nums.length</code></li>
	<li><code>0 &lt;= k &lt; nums.length</code></li>
	<li><code>nums[i] &amp; nums[j] &amp; nums[k] == 0</code> ，其中 <code>&amp;</code> 表示按位与运算符。</li>
</ul>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,1,3]
<strong>输出：</strong>12
<strong>解释：</strong>可以选出如下 i, j, k 三元组：
(i=0, j=0, k=1) : 2 &amp; 2 &amp; 1
(i=0, j=1, k=0) : 2 &amp; 1 &amp; 2
(i=0, j=1, k=1) : 2 &amp; 1 &amp; 1
(i=0, j=1, k=2) : 2 &amp; 1 &amp; 3
(i=0, j=2, k=1) : 2 &amp; 3 &amp; 1
(i=1, j=0, k=0) : 1 &amp; 2 &amp; 2
(i=1, j=0, k=1) : 1 &amp; 2 &amp; 1
(i=1, j=0, k=2) : 1 &amp; 2 &amp; 3
(i=1, j=1, k=0) : 1 &amp; 1 &amp; 2
(i=1, j=2, k=0) : 1 &amp; 3 &amp; 2
(i=2, j=0, k=1) : 3 &amp; 2 &amp; 1
(i=2, j=1, k=0) : 3 &amp; 1 &amp; 2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,0,0]
<strong>输出：</strong>27
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt; 2<sup>16</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 哈希表

## 示例

```
[2,1,3]
[0,0,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countTriplets(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countTriplets(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        
```

### C

```c
int countTriplets(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountTriplets(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countTriplets = function(nums) {
    
};
```

### TypeScript

```typescript
function countTriplets(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countTriplets($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countTriplets(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countTriplets(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countTriplets(List<int> nums) {
    
  }
}
```

### Go

```golang
func countTriplets(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_triplets(nums)
    
end
```

### Scala

```scala
object Solution {
    def countTriplets(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_triplets(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-triplets nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_triplets(Nums :: [integer()]) -> integer().
count_triplets(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_triplets(nums :: [integer]) :: integer
  def count_triplets(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countTriplets(nums: Array<Int64>): Int64 {

    }
}
```

