# LCR 006. 两数之和 II - 输入有序数组

## 题目描述

<p>给定一个已按照<strong><em> </em>升序排列&nbsp; </strong>的整数数组&nbsp;<code>numbers</code> ，请你从数组中找出两个数满足相加之和等于目标数&nbsp;<code>target</code> 。</p>

<p>函数应该以长度为 <code>2</code> 的整数数组的形式返回这两个数的下标值<em>。</em><code>numbers</code> 的下标 <strong>从 0&nbsp;开始计数</strong> ，所以答案数组应当满足 <code>0&nbsp;&lt;= answer[0] &lt; answer[1] &lt;&nbsp;numbers.length</code>&nbsp;。</p>

<p>假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>numbers = [1,2,4,6,10], target = 8
<strong>输出：</strong>[1,3]
<strong>解释：</strong>2 与 6 之和等于目标数 8 。因此 index1 = 1, index2 = 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>numbers = [2,3,4], target = 6
<strong>输出：</strong>[0,2]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>numbers = [-1,0], target = -1
<strong>输出：</strong>[0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= numbers.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= numbers[i] &lt;= 1000</code></li>
	<li><code>numbers</code> 按 <strong>非递减顺序</strong> 排列</li>
	<li><code>-1000 &lt;= target &lt;= 1000</code></li>
	<li>仅存在一个有效答案</li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 167 题相似（下标起点不同）：<a href="https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/">https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/</a></p>


## 难度

Easy

## 标签

- 数组
- 双指针
- 二分查找

## 示例

```
[1,2,4,6,10]
8
[2,3,4]
6
[-1,0]
-1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

    }
};
```

### Java

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {

    }
}
```

### Python

```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
```

### Python3

```python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
```

### C

```c


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){

}
```

### C#

```csharp
public class Solution {
    public int[] TwoSum(int[] numbers, int target) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {

};
```

### TypeScript

```typescript
function twoSum(numbers: number[], target: number): number[] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $numbers
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($numbers, $target) {

    }
}
```

### Swift

```swift
class Solution {
    func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun twoSum(numbers: IntArray, target: Int): IntArray {

    }
}
```

### Go

```golang
func twoSum(numbers []int, target int) []int {

}
```

### Ruby

```ruby
# @param {Integer[]} numbers
# @param {Integer} target
# @return {Integer[]}
def two_sum(numbers, target)

end
```

### Scala

```scala
object Solution {
    def twoSum(numbers: Array[Int], target: Int): Array[Int] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {

    }
}
```

### Racket

```racket
(define/contract (two-sum numbers target)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))

  )
```

### Erlang

```erlang
-spec two_sum(Numbers :: [integer()], Target :: integer()) -> [integer()].
two_sum(Numbers, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec two_sum(numbers :: [integer], target :: integer) :: [integer]
  def two_sum(numbers, target) do

  end
end
```

