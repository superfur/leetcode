# 2155. 分组得分最高的所有下标

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的二进制数组 <code>nums</code> ，数组长度为 <code>n</code> 。<code>nums</code> 可以按下标 <code>i</code>（ <code>0 &lt;= i &lt;= n</code> ）拆分成两个数组（可能为空）：<code>nums<sub>left</sub></code> 和 <code>nums<sub>right</sub></code> 。</p>

<ul>
	<li><code>nums<sub>left</sub></code> 包含 <code>nums</code> 中从下标 <code>0</code> 到 <code>i - 1</code> 的所有元素<strong>（包括 </strong><code>0</code><strong> 和 </strong><code>i - 1</code><strong> ）</strong>，而 <code>nums<sub>right</sub></code> 包含 <code>nums</code> 中从下标 <code>i</code> 到 <code>n - 1</code> 的所有元素<strong>（包括 </strong><code>i</code><strong> 和 </strong><code>n - 1</code><strong> ）。</strong></li>
	<li>如果 <code>i == 0</code> ，<code>nums<sub>left</sub></code> 为 <strong>空</strong> ，而 <code>nums<sub>right</sub></code> 将包含 <code>nums</code> 中的所有元素。</li>
	<li>如果 <code>i == n</code> ，<code>nums<sub>left</sub></code> 将包含 <code>nums</code> 中的所有元素，而 <code>nums<sub>right</sub></code> 为 <strong>空</strong> 。</li>
</ul>

<p>下标 <code>i</code><strong> </strong>的<strong> 分组得分</strong> 为 <code>nums<sub>left</sub></code> 中 <code>0</code> 的个数和 <code>nums<sub>right</sub></code> 中 <code>1</code> 的个数之<strong> 和</strong> 。</p>

<p>返回 <strong>分组得分 最高</strong> 的 <strong>所有不同下标</strong> 。你可以按 <strong>任意顺序</strong> 返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [0,0,1,0]
<strong>输出：</strong>[2,4]
<strong>解释：</strong>按下标分组
- 0 ：nums<sub>left</sub> 为 [] 。nums<sub>right</sub> 为 [0,0,<em><strong>1</strong></em>,0] 。得分为 0 + 1 = 1 。
- 1 ：nums<sub>left</sub> 为 [<em><strong>0</strong></em>] 。nums<sub>right</sub> 为 [0,<em><strong>1</strong></em>,0] 。得分为 1 + 1 = 2 。
- 2 ：nums<sub>left</sub> 为 [<em><strong>0</strong></em>,<em><strong>0</strong></em>] 。nums<sub>right</sub> 为 [<em><strong>1</strong></em>,0] 。得分为 2 + 1 = 3 。
- 3 ：nums<sub>left</sub> 为 [<em><strong>0</strong></em>,<em><strong>0</strong></em>,1] 。nums<sub>right</sub> 为 [0] 。得分为 2 + 0 = 2 。
- 4 ：nums<sub>left</sub> 为 [<em><strong>0</strong></em>,<em><strong>0</strong></em>,1,<em><strong>0</strong></em>] 。nums<sub>right</sub> 为 [] 。得分为 3 + 0 = 3 。
下标 2 和 4 都可以得到最高的分组得分 3 。
注意，答案 [4,2] 也被视为正确答案。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [0,0,0]
<strong>输出：</strong>[3]
<strong>解释：</strong>按下标分组
- 0 ：nums<sub>left</sub> 为 [] 。nums<sub>right</sub> 为 [0,0,0] 。得分为 0 + 0 = 0 。
- 1 ：nums<sub>left</sub> 为 [<em><strong>0</strong></em>] 。nums<sub>right</sub> 为 [0,0] 。得分为 1 + 0 = 1 。
- 2 ：nums<sub>left</sub> 为 [<em><strong>0</strong></em>,<em><strong>0</strong></em>] 。nums<sub>right</sub> 为 [0] 。得分为 2 + 0 = 2 。
- 3 ：nums<sub>left</sub> 为 [<em><strong>0</strong></em>,<em><strong>0</strong></em>,<em><strong>0</strong></em>] 。nums<sub>right</sub> 为 [] 。得分为 3 + 0 = 3 。
只有下标 3 可以得到最高的分组得分 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [1,1]
<strong>输出：</strong>[0]
<strong>解释：</strong>按下标分组
- 0 ：nums<sub>left</sub> 为 [] 。nums<sub>right</sub> 为 [<em><strong>1</strong></em>,<em><strong>1</strong></em>] 。得分为 0 + 2 = 2 。
- 1 ：nums<sub>left</sub> 为 [1] 。nums<sub>right</sub> 为 [<em><strong>1</strong></em>] 。得分为 0 + 1 = 1 。
- 2 ：nums<sub>left</sub> 为 [1,1] 。nums<sub>right</sub> 为 [] 。得分为 0 + 0 = 0 。
只有下标 0 可以得到最高的分组得分 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组

## 提示

1. When you iterate the array, maintain the number of zeros and ones on the left side. Can you quickly calculate the number of ones on the right side?
2. The number of ones on the right side equals the number of ones in the whole array minus the number of ones on the left side.
3. Alternatively, you can quickly calculate it by using a prefix sum array.

## 示例

```
[0,0,1,0]
[0,0,0]
[1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> maxScoreIndices(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> maxScoreIndices(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxScoreIndices(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> MaxScoreIndices(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var maxScoreIndices = function(nums) {
    
};
```

### TypeScript

```typescript
function maxScoreIndices(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function maxScoreIndices($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxScoreIndices(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxScoreIndices(nums: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> maxScoreIndices(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxScoreIndices(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def max_score_indices(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxScoreIndices(nums: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_score_indices(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (max-score-indices nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec max_score_indices(Nums :: [integer()]) -> [integer()].
max_score_indices(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_score_indices(nums :: [integer]) :: [integer]
  def max_score_indices(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxScoreIndices(nums: Array<Int64>): ArrayList<Int64> {

    }
}
```

