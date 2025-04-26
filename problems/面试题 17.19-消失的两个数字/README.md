# 面试题 17.19. 消失的两个数字

## 题目描述

<p>给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？</p>

<p>以任意顺序返回这两个数字均可。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong><code>[1]</code>
<strong>输出：</strong>[2,3]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong><code>[2,3]</code>
<strong>输出：</strong>[1,4]</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums.length &lt;=&nbsp;30000</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 哈希表

## 提示

1. 从第一部分开始：如果只缺少一个数字，那么找到它。
2. 第1部分：如果你必须在O(1)的空间复杂度和O(N)的时间复杂度下找到丢失的数字，那么只能在数组中执行常数次遍历，并且只能存储少许变量。
3. 第1部分：如果将数组中的所有值相加会怎么样？然后你能算出缺失的数字吗？
4. 第2部分：我们现在正在寻找两个缺失的数字，可以称其为a和b。第1部分中的计算方法将告诉我们a和b的和，但它实际上不会告诉我们a和b。还需要做什么计算？
5. 第2部分：有很多不同的计算方法可以试一试。例如，可以把所有的数都相乘，但这只会得到a和b的乘积。
6. 第2部分：把数字加在一起会得到a + b的结果。把数字相乘会得到a × b的结果。怎样才能得到a和b的确切值？
7. 第2部分：我们可以两者都计算。如果知道a + b = 87，a×b = 962，那么就解出a和b : a = 13且b = 74。但这也将导致必须对非常大的数相乘。所有数的乘积可以大于10^157。还有更简单的计算方法吗？
8. 第2部分：几乎任何我们能想到的“方程”都可以用在这里（只要它和线性和不等价）。只要保持这个和很小就可以。
9. 第2部分：试着求所有值的平方的和。
10. 第2部分：你可能需要二次公式。如果你不记得也没什么大不了的，大多数人都不会记得。知道二次公式的存在即可。

## 示例

```
[1]
[2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> missingTwo(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] missingTwo(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def missingTwo(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* missingTwo(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MissingTwo(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var missingTwo = function(nums) {
    
};
```

### TypeScript

```typescript
function missingTwo(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function missingTwo($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func missingTwo(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun missingTwo(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> missingTwo(List<int> nums) {
    
  }
}
```

### Go

```golang
func missingTwo(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def missing_two(nums)
    
end
```

### Scala

```scala
object Solution {
    def missingTwo(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn missing_two(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (missing-two nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec missing_two(Nums :: [integer()]) -> [integer()].
missing_two(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec missing_two(nums :: [integer]) :: [integer]
  def missing_two(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func missingTwo(nums: Array<Int64>): Array<Int64> {

    }
}
```

