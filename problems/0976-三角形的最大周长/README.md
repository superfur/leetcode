# 976. 三角形的最大周长

## 题目描述

<p>给定由一些正数（代表长度）组成的数组 <code>nums</code>&nbsp;，返回 <em>由其中三个长度组成的、<strong>面积不为零</strong>的三角形的最大周长</em>&nbsp;。如果不能形成任何面积不为零的三角形，返回&nbsp;<code>0</code>。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,1,2]
<strong>输出：</strong>5
<strong>解释：</strong>你可以用三个边长组成一个三角形:1 2 2。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1,10]
<strong>输出：</strong>0
<strong>解释：</strong>
你不能用边长 1,1,2 来组成三角形。
不能用边长 1,1,10 来构成三角形。
不能用边长 1、2 和 10 来构成三角形。
因为我们不能用任何三条边长来构成一个非零面积的三角形，所以我们返回 0。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 数学
- 排序

## 示例

```
[2,1,2]
[1,2,1,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestPerimeter(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
```

### C

```c
int largestPerimeter(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestPerimeter(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var largestPerimeter = function(nums) {
    
};
```

### TypeScript

```typescript
function largestPerimeter(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function largestPerimeter($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestPerimeter(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestPerimeter(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestPerimeter(List<int> nums) {
    
  }
}
```

### Go

```golang
func largestPerimeter(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def largest_perimeter(nums)
    
end
```

### Scala

```scala
object Solution {
    def largestPerimeter(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_perimeter(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-perimeter nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_perimeter(Nums :: [integer()]) -> integer().
largest_perimeter(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_perimeter(nums :: [integer]) :: integer
  def largest_perimeter(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestPerimeter(nums: Array<Int64>): Int64 {

    }
}
```

