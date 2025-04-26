# 2150. 找出数组中的所有孤独数字

## 题目描述

<p>给你一个整数数组 <code>nums</code> 。如果数字 <code>x</code> 在数组中仅出现 <strong>一次</strong> ，且没有 <strong>相邻</strong> 数字（即，<code>x + 1</code> 和 <code>x - 1</code>）出现在数组中，则认为数字 <code>x</code> 是 <strong>孤独数字</strong> 。</p>

<p>返回<em> </em><code>nums</code> 中的 <strong>所有</strong> 孤独数字。你可以按 <strong>任何顺序</strong> 返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [10,6,5,8]
<strong>输出：</strong>[10,8]
<strong>解释：</strong>
- 10 是一个孤独数字，因为它只出现一次，并且 9 和 11 没有在 nums 中出现。
- 8 是一个孤独数字，因为它只出现一次，并且 7 和 9 没有在 nums 中出现。
- 5 不是一个孤独数字，因为 6 出现在 nums 中，反之亦然。
因此，nums 中的孤独数字是 [10, 8] 。
注意，也可以返回 [8, 10] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,3,5,3]
<strong>输出：</strong>[1,5]
<strong>解释：</strong>
- 1 是一个孤独数字，因为它只出现一次，并且 0 和 2 没有在 nums 中出现。
- 5 是一个孤独数字，因为它只出现一次，并且 4 和 6 没有在 nums 中出现。
- 3 不是一个孤独数字，因为它出现两次。
因此，nums 中的孤独数字是 [1, 5] 。
注意，也可以返回 [5, 1] 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. For a given element x, how can you quickly check if x - 1 and x + 1 are present in the array without reiterating through the entire array?
2. Use a set or a hash map.

## 示例

```
[10,6,5,8]
[1,3,5,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findLonely(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> findLonely(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findLonely(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> FindLonely(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findLonely = function(nums) {
    
};
```

### TypeScript

```typescript
function findLonely(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findLonely($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLonely(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLonely(nums: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findLonely(List<int> nums) {
    
  }
}
```

### Go

```golang
func findLonely(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def find_lonely(nums)
    
end
```

### Scala

```scala
object Solution {
    def findLonely(nums: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_lonely(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-lonely nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_lonely(Nums :: [integer()]) -> [integer()].
find_lonely(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_lonely(nums :: [integer]) :: [integer]
  def find_lonely(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLonely(nums: Array<Int64>): ArrayList<Int64> {

    }
}
```

