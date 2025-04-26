# 2032. 至少在两个数组中出现的值

## 题目描述

给你三个整数数组 <code>nums1</code>、<code>nums2</code> 和 <code>nums3</code> ，请你构造并返回一个 <strong>元素各不相同的</strong> 数组，且由 <strong>至少</strong> 在 <strong>两个</strong> 数组中出现的所有值组成<em>。</em>数组中的元素可以按 <strong>任意</strong> 顺序排列。
<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
<strong>输出：</strong>[3,2]
<strong>解释：</strong>至少在两个数组中出现的所有值为：
- 3 ，在全部三个数组中都出现过。
- 2 ，在数组 nums1 和 nums2 中出现过。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
<strong>输出：</strong>[2,3,1]
<strong>解释：</strong>至少在两个数组中出现的所有值为：
- 2 ，在数组 nums2 和 nums3 中出现过。
- 3 ，在数组 nums1 和 nums2 中出现过。
- 1 ，在数组 nums1 和 nums3 中出现过。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
<strong>输出：</strong>[]
<strong>解释：</strong>不存在至少在两个数组中出现的值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length, nums3.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums1[i], nums2[j], nums3[k] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组
- 哈希表

## 提示

1. What data structure can we use to help us quickly find whether an element belongs in an array?
2. Can we count the frequencies of the elements in each array?

## 示例

```
[1,1,3,2]
[2,3]
[3]
[3,1]
[2,3]
[1,2]
[1,2,2]
[4,3,3]
[5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        
    }
}
```

### Python

```python
class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoOutOfThree(int* nums1, int nums1Size, int* nums2, int nums2Size, int* nums3, int nums3Size, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> TwoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @return {number[]}
 */
var twoOutOfThree = function(nums1, nums2, nums3) {
    
};
```

### TypeScript

```typescript
function twoOutOfThree(nums1: number[], nums2: number[], nums3: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer[] $nums3
     * @return Integer[]
     */
    function twoOutOfThree($nums1, $nums2, $nums3) {
        
    }
}
```

### Swift

```swift
class Solution {
    func twoOutOfThree(_ nums1: [Int], _ nums2: [Int], _ nums3: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun twoOutOfThree(nums1: IntArray, nums2: IntArray, nums3: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> twoOutOfThree(List<int> nums1, List<int> nums2, List<int> nums3) {
    
  }
}
```

### Go

```golang
func twoOutOfThree(nums1 []int, nums2 []int, nums3 []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[]} nums3
# @return {Integer[]}
def two_out_of_three(nums1, nums2, nums3)
    
end
```

### Scala

```scala
object Solution {
    def twoOutOfThree(nums1: Array[Int], nums2: Array[Int], nums3: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn two_out_of_three(nums1: Vec<i32>, nums2: Vec<i32>, nums3: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (two-out-of-three nums1 nums2 nums3)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec two_out_of_three(Nums1 :: [integer()], Nums2 :: [integer()], Nums3 :: [integer()]) -> [integer()].
two_out_of_three(Nums1, Nums2, Nums3) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec two_out_of_three(nums1 :: [integer], nums2 :: [integer], nums3 :: [integer]) :: [integer]
  def two_out_of_three(nums1, nums2, nums3) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func twoOutOfThree(nums1: Array<Int64>, nums2: Array<Int64>, nums3: Array<Int64>): ArrayList<Int64> {

    }
}
```

