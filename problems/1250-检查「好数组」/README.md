# 1250. 检查「好数组」

## 题目描述

<p>给你一个正整数数组 <code>nums</code>，你需要从中任选一些子集，然后将子集中每一个数乘以一个 <strong>任意整数</strong>，并求出他们的和。</p>

<p>假如该和结果为&nbsp;<code>1</code>，那么原数组就是一个「<strong>好数组</strong>」，则返回 <code>True</code>；否则请返回 <code>False</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [12,5,7,23]
<strong>输出：</strong>true
<strong>解释：</strong>挑选数字 5 和 7。
5*3 + 7*(-2) = 1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [29,6,10]
<strong>输出：</strong>true
<strong>解释：</strong>挑选数字 29, 6 和 10。
29*1 + 6*(-3) + 10*(-1) = 1
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [3,6]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^9</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 数论

## 提示

1. Eq.  ax+by=1 has solution x, y if gcd(a,b) = 1.
2. Can you generalize the formula?.  Check Bézout's lemma.

## 示例

```
[12,5,7,23]
[29,6,10]
[3,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isGoodArray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isGoodArray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        
```

### C

```c
bool isGoodArray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsGoodArray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isGoodArray = function(nums) {
    
};
```

### TypeScript

```typescript
function isGoodArray(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function isGoodArray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isGoodArray(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isGoodArray(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isGoodArray(List<int> nums) {
    
  }
}
```

### Go

```golang
func isGoodArray(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def is_good_array(nums)
    
end
```

### Scala

```scala
object Solution {
    def isGoodArray(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_good_array(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-good-array nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec is_good_array(Nums :: [integer()]) -> boolean().
is_good_array(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_good_array(nums :: [integer]) :: boolean
  def is_good_array(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isGoodArray(nums: Array<Int64>): Bool {

    }
}
```

