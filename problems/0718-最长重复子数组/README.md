# 718. 最长重复子数组

## 题目描述

<p>给两个整数数组&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;，返回 <em>两个数组中 <strong>公共的</strong> 、长度最长的子数组的长度&nbsp;</em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
<strong>输出：</strong>3
<strong>解释：</strong>长度最长的公共子数组是 [3,2,1] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
<strong>输出：</strong>5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 动态规划
- 滑动窗口
- 哈希函数
- 滚动哈希

## 提示

1. Use dynamic programming.  dp[i][j] will be the longest common prefix of A[i:] and B[j:].
2. The answer is max(dp[i][j]) over all i, j.

## 示例

```
[1,2,3,2,1]
[3,2,1,4,7]
[0,0,0,0,0]
[0,0,0,0,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int findLength(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
int findLength(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindLength(int[] nums1, int[] nums2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findLength = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function findLength(nums1: number[], nums2: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function findLength($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLength(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLength(nums1: IntArray, nums2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findLength(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func findLength(nums1 []int, nums2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def find_length(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def findLength(nums1: Array[Int], nums2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_length(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-length nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_length(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
find_length(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_length(nums1 :: [integer], nums2 :: [integer]) :: integer
  def find_length(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLength(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

