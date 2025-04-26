# 3282. 到达数组末尾的最大得分

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>你的目标是从下标 <code>0</code>&nbsp;出发，到达下标 <code>n - 1</code>&nbsp;处。每次你只能移动到&nbsp;<strong>更大</strong>&nbsp;的下标处。</p>

<p>从下标 <code>i</code>&nbsp;跳到下标 <code>j</code>&nbsp;的得分为&nbsp;<code>(j - i) * nums[i]</code>&nbsp;。</p>

<p>请你返回你到达最后一个下标处能得到的 <strong>最大总得分</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,3,1,5]</span></p>

<p><b>输出：</b>7</p>

<p><b>解释：</b></p>

<p>一开始跳到下标 1 处，然后跳到最后一个下标处。总得分为&nbsp;<code>1 * 1 + 2 * 3 = 7</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [4,3,1,3,2]</span></p>

<p><b>输出：</b>16</p>

<p><strong>解释：</strong></p>

<p>直接跳到最后一个下标处。总得分为&nbsp;<code>4 * 4 = 16</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组

## 提示

1. It can be proven that from each index <code>i</code>, the optimal solution is to jump to the nearest index <code>j > i</code> such that <code>nums[j] > nums[i]</code>.

## 示例

```
[1,3,1,5]
[4,3,1,3,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long findMaximumScore(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long findMaximumScore(List<Integer> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMaximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        
```

### C

```c
long long findMaximumScore(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long FindMaximumScore(IList<int> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaximumScore = function(nums) {
    
};
```

### TypeScript

```typescript
function findMaximumScore(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaximumScore($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMaximumScore(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaximumScore(nums: List<Int>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMaximumScore(List<int> nums) {
    
  }
}
```

### Go

```golang
func findMaximumScore(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_maximum_score(nums)
    
end
```

### Scala

```scala
object Solution {
    def findMaximumScore(nums: List[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_maximum_score(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (find-maximum-score nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_maximum_score(Nums :: [integer()]) -> integer().
find_maximum_score(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_maximum_score(nums :: [integer]) :: integer
  def find_maximum_score(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMaximumScore(nums: ArrayList<Int64>): Int64 {

    }
}
```

