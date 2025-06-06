# 645. 错误的集合

## 题目描述

<p>集合 <code>s</code> 包含从 <code>1</code> 到 <code>n</code> 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 <strong>丢失了一个数字</strong> 并且 <strong>有一个数字重复</strong> 。</p>

<p>给定一个数组 <code>nums</code> 代表了集合 <code>S</code> 发生错误后的结果。</p>

<p>请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,2,4]
<strong>输出：</strong>[2,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1]
<strong>输出：</strong>[1,2]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= nums.length <= 10<sup>4</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组
- 哈希表
- 排序

## 示例

```
[1,2,2,4]
[1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findErrorNums(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findErrorNums(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindErrorNums(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {
    
};
```

### TypeScript

```typescript
function findErrorNums(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findErrorNums($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findErrorNums(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findErrorNums(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findErrorNums(List<int> nums) {
    
  }
}
```

### Go

```golang
func findErrorNums(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def find_error_nums(nums)
    
end
```

### Scala

```scala
object Solution {
    def findErrorNums(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-error-nums nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_error_nums(Nums :: [integer()]) -> [integer()].
find_error_nums(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_error_nums(nums :: [integer]) :: [integer]
  def find_error_nums(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findErrorNums(nums: Array<Int64>): Array<Int64> {

    }
}
```

