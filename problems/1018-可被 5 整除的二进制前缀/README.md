# 1018. 可被 5 整除的二进制前缀

## 题目描述

<p>给定一个二进制数组 <code>nums</code> (&nbsp;<strong>索引从0开始&nbsp;</strong>)。</p>

<p>我们将<code>x<sub>i</sub></code>&nbsp;定义为其二进制表示形式为子数组&nbsp;<code>nums[0..i]</code>&nbsp;(从最高有效位到最低有效位)。</p>

<ul>
	<li>例如，如果 <code>nums =[1,0,1]</code> ，那么&nbsp;<code>x<sub>0</sub>&nbsp;= 1</code>,&nbsp;<code>x<sub>1</sub>&nbsp;= 2</code>, 和&nbsp;<code>x<sub>2</sub>&nbsp;= 5</code>。</li>
</ul>

<p>返回布尔值列表&nbsp;<code>answer</code>，只有当&nbsp;<code>x<sub>i</sub></code><em>&nbsp;</em>可以被 <code>5</code>&nbsp;整除时，答案&nbsp;<code>answer[i]</code> 为&nbsp;<code>true</code>，否则为 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,1]
<strong>输出：</strong>[true,false,false]
<strong>解释：</strong>
输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为 true 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1]
<strong>输出：</strong>[false,false,false]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code><sup>&nbsp;</sup></li>
	<li><code>nums[i]</code>&nbsp;仅为&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组

## 提示

1. If X is the first i digits of the array as a binary number, then 2X + A[i] is the first i+1 digits.

## 示例

```
[0,1,1]
[1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        
```

### Python3

```python3
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* prefixesDivBy5(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<bool> PrefixesDivBy5(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean[]}
 */
var prefixesDivBy5 = function(nums) {
    
};
```

### TypeScript

```typescript
function prefixesDivBy5(nums: number[]): boolean[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean[]
     */
    function prefixesDivBy5($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func prefixesDivBy5(_ nums: [Int]) -> [Bool] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun prefixesDivBy5(nums: IntArray): List<Boolean> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<bool> prefixesDivBy5(List<int> nums) {
    
  }
}
```

### Go

```golang
func prefixesDivBy5(nums []int) []bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean[]}
def prefixes_div_by5(nums)
    
end
```

### Scala

```scala
object Solution {
    def prefixesDivBy5(nums: Array[Int]): List[Boolean] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn prefixes_div_by5(nums: Vec<i32>) -> Vec<bool> {
        
    }
}
```

### Racket

```racket
(define/contract (prefixes-div-by5 nums)
  (-> (listof exact-integer?) (listof boolean?))
  )
```

### Erlang

```erlang
-spec prefixes_div_by5(Nums :: [integer()]) -> [boolean()].
prefixes_div_by5(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec prefixes_div_by5(nums :: [integer]) :: [boolean]
  def prefixes_div_by5(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func prefixesDivBy5(nums: Array<Int64>): ArrayList<Bool> {

    }
}
```

