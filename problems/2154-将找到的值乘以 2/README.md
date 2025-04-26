# 2154. 将找到的值乘以 2

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，另给你一个整数 <code>original</code> ，这是需要在 <code>nums</code> 中搜索的第一个数字。</p>

<p>接下来，你需要按下述步骤操作：</p>

<ol>
	<li>如果在 <code>nums</code> 中找到 <code>original</code> ，将 <code>original</code>&nbsp;<strong>乘以</strong> 2 ，得到新 <code>original</code>（即，令 <code>original = 2 * original</code>）。</li>
	<li>否则，停止这一过程。</li>
	<li>只要能在数组中找到新 <code>original</code> ，就对新 <code>original</code> 继续 <strong>重复</strong> 这一过程<strong>。</strong></li>
</ol>

<p>返回<em> </em><code>original</code> 的 <strong>最终</strong> 值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,3,6,1,12], original = 3
<strong>输出：</strong>24
<strong>解释：</strong> 
- 3 能在 nums 中找到。3 * 2 = 6 。
- 6 能在 nums 中找到。6 * 2 = 12 。
- 12 能在 nums 中找到。12 * 2 = 24 。
- 24 不能在 nums 中找到。因此，返回 24 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,7,9], original = 4
<strong>输出：</strong>4
<strong>解释：</strong>
- 4 不能在 nums 中找到。因此，返回 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], original &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 排序
- 模拟

## 提示

1. Repeatedly iterate through the array and check if the current value of original is in the array.
2. If original is not found, stop and return its current value.
3. Otherwise, multiply original by 2 and repeat the process.
4. Use set data structure to check the existence faster.

## 示例

```
[5,3,6,1,12]
3
[2,7,9]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        
    }
};
```

### Java

```java
class Solution {
    public int findFinalValue(int[] nums, int original) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
```

### C

```c
int findFinalValue(int* nums, int numsSize, int original) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindFinalValue(int[] nums, int original) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} original
 * @return {number}
 */
var findFinalValue = function(nums, original) {
    
};
```

### TypeScript

```typescript
function findFinalValue(nums: number[], original: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $original
     * @return Integer
     */
    function findFinalValue($nums, $original) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findFinalValue(_ nums: [Int], _ original: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findFinalValue(nums: IntArray, original: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findFinalValue(List<int> nums, int original) {
    
  }
}
```

### Go

```golang
func findFinalValue(nums []int, original int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} original
# @return {Integer}
def find_final_value(nums, original)
    
end
```

### Scala

```scala
object Solution {
    def findFinalValue(nums: Array[Int], original: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_final_value(nums: Vec<i32>, original: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-final-value nums original)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_final_value(Nums :: [integer()], Original :: integer()) -> integer().
find_final_value(Nums, Original) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_final_value(nums :: [integer], original :: integer) :: integer
  def find_final_value(nums, original) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findFinalValue(nums: Array<Int64>, original: Int64): Int64 {

    }
}
```

