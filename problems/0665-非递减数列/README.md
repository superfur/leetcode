# 665. 非递减数列

## 题目描述

<p>给你一个长度为&nbsp;<code>n</code>&nbsp;的整数数组<meta charset="UTF-8" />&nbsp;<code>nums</code>&nbsp;，请你判断在 <strong>最多 </strong>改变&nbsp;<code>1</code> 个元素的情况下，该数组能否变成一个非递减数列。</p>

<p>我们是这样定义一个非递减数列的：&nbsp;对于数组中任意的&nbsp;<code>i</code> <code>(0 &lt;= i &lt;= n-2)</code>，总满足 <code>nums[i] &lt;= nums[i + 1]</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [4,2,3]
<strong>输出:</strong> true
<strong>解释:</strong> 你可以通过把第一个 4 变成 1 来使得它成为一个非递减数列。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [4,2,1]
<strong>输出:</strong> false
<strong>解释:</strong> 你不能在只改变一个元素的情况下将其变为非递减数列。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>
<meta charset="UTF-8" />

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组

## 示例

```
[4,2,3]
[4,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkPossibility(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
```

### C

```c
bool checkPossibility(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckPossibility(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function(nums) {
    
};
```

### TypeScript

```typescript
function checkPossibility(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function checkPossibility($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkPossibility(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkPossibility(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkPossibility(List<int> nums) {
    
  }
}
```

### Go

```golang
func checkPossibility(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def check_possibility(nums)
    
end
```

### Scala

```scala
object Solution {
    def checkPossibility(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_possibility(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-possibility nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec check_possibility(Nums :: [integer()]) -> boolean().
check_possibility(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_possibility(nums :: [integer]) :: boolean
  def check_possibility(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkPossibility(nums: Array<Int64>): Bool {

    }
}
```

