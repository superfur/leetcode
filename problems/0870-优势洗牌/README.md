# 870. 优势洗牌

## 题目描述

<p>给定两个长度相等的数组&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>，<code>nums1</code>&nbsp;相对于 <code>nums2</code> 的<em>优势</em>可以用满足&nbsp;<code>nums1[i] &gt; nums2[i]</code>&nbsp;的索引 <code>i</code>&nbsp;的数目来描述。</p>

<p>返回 <code>nums1</code> 的&nbsp;<strong>任意&nbsp;</strong>排列，使其相对于 <code>nums2</code>&nbsp;的优势最大化。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [2,7,11,15], nums2 = [1,10,4,11]
<strong>输出：</strong>[2,11,7,15]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [12,24,8,32], nums2 = [13,25,32,11]
<strong>输出：</strong>[24,32,8,12]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums2.length == nums1.length</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 双指针
- 排序

## 示例

```
[2,7,11,15]
[1,10,4,11]
[12,24,8,32]
[13,25,32,11]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> advantageCount(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] advantageCount(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* advantageCount(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] AdvantageCount(int[] nums1, int[] nums2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var advantageCount = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function advantageCount(nums1: number[], nums2: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function advantageCount($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func advantageCount(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun advantageCount(nums1: IntArray, nums2: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> advantageCount(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func advantageCount(nums1 []int, nums2 []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def advantage_count(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def advantageCount(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn advantage_count(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (advantage-count nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec advantage_count(Nums1 :: [integer()], Nums2 :: [integer()]) -> [integer()].
advantage_count(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec advantage_count(nums1 :: [integer], nums2 :: [integer]) :: [integer]
  def advantage_count(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func advantageCount(nums1: Array<Int64>, nums2: Array<Int64>): Array<Int64> {

    }
}
```

