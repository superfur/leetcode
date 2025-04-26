# 442. 数组中重复的数据

## 题目描述

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code> ，其中 <code>nums</code> 的所有整数都在范围 <code>[1, n]</code> 内，且每个整数出现 <strong>最多</strong><strong>两次</strong> 。请你找出所有出现 <strong>两次</strong> 的整数，并以数组形式返回。</p>

<p>你必须设计并实现一个时间复杂度为 <code>O(n)</code> 且仅使用常量额外空间（不包括存储输出所需的空间）的算法解决此问题。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,3,2,7,8,2,3,1]
<strong>输出：</strong>[2,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,2]
<strong>输出：</strong>[1]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
	<li><code>nums</code> 中的每个元素出现 <strong>一次</strong> 或 <strong>两次</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表

## 示例

```
[4,3,2,7,8,2,3,1]
[1,1,2]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDuplicates(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> FindDuplicates(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    
};
```

### TypeScript

```typescript
function findDuplicates(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findDuplicates($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findDuplicates(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findDuplicates(nums: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findDuplicates(List<int> nums) {
    
  }
}
```

### Go

```golang
func findDuplicates(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def find_duplicates(nums)
    
end
```

### Scala

```scala
object Solution {
    def findDuplicates(nums: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_duplicates(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-duplicates nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_duplicates(Nums :: [integer()]) -> [integer()].
find_duplicates(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_duplicates(nums :: [integer]) :: [integer]
  def find_duplicates(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findDuplicates(nums: Array<Int64>): ArrayList<Int64> {

    }
}
```

