# 面试题 17.16. 按摩师

## 题目描述

<p>一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。</p>

<p><strong>注意：</strong>本题相对原题稍作改动</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong> [1,2,3,1]
<strong>输出：</strong> 4
<strong>解释：</strong> 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong> [2,7,9,3,1]
<strong>输出：</strong> 12
<strong>解释：</strong> 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong> [2,1,4,5,3,1,1,3]
<strong>输出：</strong> 12
<strong>解释：</strong> 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
</pre>


## 难度

Easy

## 标签

- 数组
- 动态规划

## 提示

1. 此题有递归和遍历两种解法，但从递归开始可能更容易一些。
2. 递归解法：每个预约都有两个选择（接受预约或拒绝预约）。作为一种蛮力方法，你可以在所有可能性的地方递归。但是请注意，如果接收了预约请求i，那么你的递归算法应该跳过预约请求i + 1。
3. 递归解法：你可以通过制表法优化这种方法。这种方法的运行时间是多少？
4. 递归解法：记忆法的时间复杂度为O(N)，空间复杂度也为O(N)。
5. 迭代法：对递归法进一步研究。你可以迭代地实现类似的策略吗？
6. 迭代法：从数组的末尾开始，然后向后计算可能是最简单的。
7. 迭代法：注意，你永远不会连续跳过3个预约。为什么不会？因为你总是可以接受中间的预约。
8. 迭代法：如果你选择i，那么将永远不会选择i + 1，但是总会选择i + 2或i + 3。
9. 迭代法：使用一个例子并从后往前计算。你可以很容易地找到子数组{rn}、{rn-1, rn}和{rn-2, ..., rn}。如何使用这些结果快速找到{rn-3, ..., rn}的最优解？
10. 迭代法：如果你预约某一时间段，那就不能预约紧邻的下一时间段，但可以预约之后的任何时间。因此，optimal(ri, ..., rn) = max(ri + optimal(ri+2, ..., rn)，optimal(ri+1, ..., rn))。你可以通过从后往前迭代来解决这个问题。
11. 迭代解法：如果你仔细考虑真正需要的数据，应该能够在O(n)时间复杂度和O(1)额外空间复杂度内解出它。

## 示例

```
[1,2,3,1]
[2,7,9,3,1]
[]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int massage(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int massage(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def massage(self, nums: List[int]) -> int:
        
```

### C

```c
int massage(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int Massage(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var massage = function(nums) {
    
};
```

### TypeScript

```typescript
function massage(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function massage($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func massage(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun massage(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int massage(List<int> nums) {
    
  }
}
```

### Go

```golang
func massage(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def massage(nums)
    
end
```

### Scala

```scala
object Solution {
    def massage(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn massage(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (massage nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec massage(Nums :: [integer()]) -> integer().
massage(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec massage(nums :: [integer]) :: integer
  def massage(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func massage(nums: Array<Int64>): Int64 {

    }
}
```

