# 1389. 按既定顺序创建目标数组

## 题目描述

<p>给你两个整数数组 <code>nums</code> 和 <code>index</code>。你需要按照以下规则创建目标数组：</p>

<ul>
	<li>目标数组 <code>target</code> 最初为空。</li>
	<li>按从左到右的顺序依次读取 <code>nums[i]</code> 和 <code>index[i]</code>，在 <code>target</code> 数组中的下标 <code>index[i]</code> 处插入值 <code>nums[i]</code> 。</li>
	<li>重复上一步，直到在 <code>nums</code> 和 <code>index</code> 中都没有要读取的元素。</li>
</ul>

<p>请你返回目标数组。</p>

<p>题目保证数字插入位置总是存在。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [0,1,2,3,4], index = [0,1,2,2,1]
<strong>输出：</strong>[0,4,1,3,2]
<strong>解释：</strong>
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,4,0], index = [0,1,2,3,0]
<strong>输出：</strong>[0,1,2,3,4]
<strong>解释：</strong>
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [1], index = [0]
<strong>输出：</strong>[1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length, index.length &lt;= 100</code></li>
	<li><code>nums.length == index.length</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>0 &lt;= index[i] &lt;= i</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 模拟

## 提示

1. Simulate the process and fill corresponding numbers in the designated spots.

## 示例

```
[0,1,2,3,4]
[0,1,2,2,1]
[1,2,3,4,0]
[0,1,2,3,0]
[1]
[0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        
    }
}
```

### Python

```python
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* createTargetArray(int* nums, int numsSize, int* index, int indexSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] CreateTargetArray(int[] nums, int[] index) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} index
 * @return {number[]}
 */
var createTargetArray = function(nums, index) {
    
};
```

### TypeScript

```typescript
function createTargetArray(nums: number[], index: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $index
     * @return Integer[]
     */
    function createTargetArray($nums, $index) {
        
    }
}
```

### Swift

```swift
class Solution {
    func createTargetArray(_ nums: [Int], _ index: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun createTargetArray(nums: IntArray, index: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> createTargetArray(List<int> nums, List<int> index) {
    
  }
}
```

### Go

```golang
func createTargetArray(nums []int, index []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} index
# @return {Integer[]}
def create_target_array(nums, index)
    
end
```

### Scala

```scala
object Solution {
    def createTargetArray(nums: Array[Int], index: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn create_target_array(nums: Vec<i32>, index: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (create-target-array nums index)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec create_target_array(Nums :: [integer()], Index :: [integer()]) -> [integer()].
create_target_array(Nums, Index) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec create_target_array(nums :: [integer], index :: [integer]) :: [integer]
  def create_target_array(nums, index) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func createTargetArray(nums: Array<Int64>, index: Array<Int64>): Array<Int64> {

    }
}
```

