# 面试题 08.04. 幂集

## 题目描述

<p>幂集。编写一种方法，返回某集合的所有子集。集合中&nbsp;<strong>不包含重复的元素</strong>。</p>

<p>说明：解集不能包含重复的子集。</p>

<p><strong>示例：</strong></p>

<pre>
<strong> 输入：</strong>nums = [1,2,3]
<strong> 输出：</strong>
[
  [3],
&nbsp; [1],
&nbsp; [2],
&nbsp; [1,2,3],
&nbsp; [1,3],
&nbsp; [2,3],
&nbsp; [1,2],
&nbsp; []
]
</pre>


## 难度

Medium

## 标签

- 位运算
- 数组
- 回溯

## 提示

1. 如何从子集{a, b}中构建{a, b, c}的所有子集？
2. 任何属于{a, b}的子集都是{a, b, c}的子集。哪个集合是{a, b, c}的子集却不是{a, b}的子集。
3. 包含c的子集是{a, b, c}，而非{a, b}。你能使用子集{a, b}构建这些子集吗？
4. 通过把c加到所有{a, b}的子集里，你可以构建剩余的子集。
5. 你也可以将每个子集映射成二进制数。第i位可以表示元素是否在集合中的“布尔”标志。

## 示例

```
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** subsets(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> Subsets(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    
};
```

### TypeScript

```typescript
function subsets(nums: number[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function subsets($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func subsets(_ nums: [Int]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subsets(nums: IntArray): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> subsets(List<int> nums) {
    
  }
}
```

### Go

```golang
func subsets(nums []int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[][]}
def subsets(nums)
    
end
```

### Scala

```scala
object Solution {
    def subsets(nums: Array[Int]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (subsets nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec subsets(Nums :: [integer()]) -> [[integer()]].
subsets(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec subsets(nums :: [integer]) :: [[integer]]
  def subsets(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func subsets(nums: Array<Int64>): ArrayList<ArrayList<Int64>> {

    }
}
```

