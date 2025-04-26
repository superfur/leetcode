# 1470. 重新排列数组

## 题目描述

<p>给你一个数组 <code>nums</code> ，数组中有 <code>2n</code> 个元素，按 <code>[x<sub>1</sub>,x<sub>2</sub>,...,x<sub>n</sub>,y<sub>1</sub>,y<sub>2</sub>,...,y<sub>n</sub>]</code> 的格式排列。</p>

<p>请你将数组按 <code>[x<sub>1</sub>,y<sub>1</sub>,x<sub>2</sub>,y<sub>2</sub>,...,x<sub>n</sub>,y<sub>n</sub>]</code> 格式重新排列，返回重排后的数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [2,5,1,3,4,7], n = 3
<strong>输出：</strong>[2,3,5,4,1,7] 
<strong>解释：</strong>由于 x<sub>1</sub>=2, x<sub>2</sub>=5, x<sub>3</sub>=1, y<sub>1</sub>=3, y<sub>2</sub>=4, y<sub>3</sub>=7 ，所以答案为 [2,3,5,4,1,7]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,4,4,3,2,1], n = 4
<strong>输出：</strong>[1,4,2,3,3,2,4,1]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [1,1,2,2], n = 2
<strong>输出：</strong>[1,2,1,2]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>nums.length == 2n</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^3</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Use two pointers to create the new array of 2n elements. The first starting at the beginning and the other starting at (n+1)th position. Alternate between them and create the new array.

## 示例

```
[2,5,1,3,4,7]
3
[1,2,3,4,4,3,2,1]
4
[1,1,2,2]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] shuffle(int[] nums, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] Shuffle(int[] nums, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    
};
```

### TypeScript

```typescript
function shuffle(nums: number[], n: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $n
     * @return Integer[]
     */
    function shuffle($nums, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shuffle(_ nums: [Int], _ n: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shuffle(nums: IntArray, n: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> shuffle(List<int> nums, int n) {
    
  }
}
```

### Go

```golang
func shuffle(nums []int, n int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} n
# @return {Integer[]}
def shuffle(nums, n)
    
end
```

### Scala

```scala
object Solution {
    def shuffle(nums: Array[Int], n: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (shuffle nums n)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec shuffle(Nums :: [integer()], N :: integer()) -> [integer()].
shuffle(Nums, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shuffle(nums :: [integer], n :: integer) :: [integer]
  def shuffle(nums, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shuffle(nums: Array<Int64>, n: Int64): Array<Int64> {

    }
}
```

