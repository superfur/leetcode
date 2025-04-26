# 3289. 数字小镇中的捣蛋鬼

## 题目描述

<p>数字小镇 Digitville 中，存在一个数字列表 <code>nums</code>，其中包含从 <code>0</code> 到 <code>n - 1</code> 的整数。每个数字本应 <strong>只出现一次</strong>，然而，有 <strong>两个 </strong>顽皮的数字额外多出现了一次，使得列表变得比正常情况下更长。</p>

<p>为了恢复 Digitville 的和平，作为小镇中的名侦探，请你找出这两个顽皮的数字。</p>

<p>返回一个长度为 2 的数组，包含这两个数字（顺序任意）。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [0,1,1,0]</span></p>

<p><strong>输出：</strong> <span class="example-io">[0,1]</span></p>

<p><strong>解释：</strong></p>

<p>数字 0 和 1 分别在数组中出现了两次。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [0,3,2,1,3,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">[2,3]</span></p>

<p><strong>解释: </strong></p>

<p>数字 2 和 3 分别在数组中出现了两次。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [7,1,5,4,3,4,6,0,9,5,8,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">[4,5]</span></p>

<p><strong>解释: </strong></p>

<p>数字 4 和 5 分别在数组中出现了两次。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>nums.length == n + 2</code></li>
	<li><code>0 &lt;= nums[i] &lt; n</code></li>
	<li>输入保证 <code>nums</code> 中<strong> 恰好 </strong>包含两个重复的元素。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 数学

## 提示

1. To solve the problem without the extra space, we need to think about how many times each number occurs in relation to the index.

## 示例

```
[0,1,1,0]
[0,3,2,1,3,2]
[7,1,5,4,3,4,6,0,9,5,8,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getSneakyNumbers(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] GetSneakyNumbers(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSneakyNumbers = function(nums) {
    
};
```

### TypeScript

```typescript
function getSneakyNumbers(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function getSneakyNumbers($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getSneakyNumbers(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getSneakyNumbers(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getSneakyNumbers(List<int> nums) {
    
  }
}
```

### Go

```golang
func getSneakyNumbers(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def get_sneaky_numbers(nums)
    
end
```

### Scala

```scala
object Solution {
    def getSneakyNumbers(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_sneaky_numbers(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-sneaky-numbers nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_sneaky_numbers(Nums :: [integer()]) -> [integer()].
get_sneaky_numbers(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_sneaky_numbers(nums :: [integer]) :: [integer]
  def get_sneaky_numbers(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getSneakyNumbers(nums: Array<Int64>): Array<Int64> {

    }
}
```

