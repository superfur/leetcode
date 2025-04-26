# 2772. 使数组中的所有元素都等于零

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 和一个正整数 <code>k</code> 。</p>

<p>你可以对数组执行下述操作 <strong>任意次</strong> ：</p>

<ul>
	<li>从数组中选出长度为 <code>k</code> 的 <strong>任一</strong> 子数组，并将子数组中每个元素都 <strong>减去</strong> <code>1</code> 。</li>
</ul>

<p>如果你可以使数组中的所有元素都等于 <code>0</code> ，返回&nbsp; <code>true</code><em> </em>；否则，返回<em> </em><code>false</code><em> </em>。</p>

<p><strong>子数组</strong> 是数组中的一个非空连续元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [2,2,3,1,1,0], k = 3
<strong>输出：</strong>true
<strong>解释：</strong>可以执行下述操作：
- 选出子数组 [2,2,3] ，执行操作后，数组变为 nums = [<em><strong>1</strong></em>,<em><strong>1</strong></em>,<em><strong>2</strong></em>,1,1,0] 。
- 选出子数组 [2,1,1] ，执行操作后，数组变为 nums = [1,1,<em><strong>1</strong></em>,<em><strong>0</strong></em>,<em><strong>0</strong></em>,0] 。
- 选出子数组 [1,1,1] ，执行操作后，数组变为 nums = [<em><strong>0</strong></em>,<em><strong>0</strong></em>,<em><strong>0</strong></em>,0,0,0] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,3,1,1], k = 2
<strong>输出：</strong>false
<strong>解释：</strong>无法使数组中的所有元素等于 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 前缀和

## 提示

1. In case it is possible, then how can you do the operations? which subarrays do you choose and in what order?
2. The order of the chosen subarrays should be from the left to the right of the array

## 示例

```
[2,2,3,1,1,0]
3
[1,3,1,1]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkArray(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkArray(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        
```

### C

```c
bool checkArray(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckArray(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var checkArray = function(nums, k) {
    
};
```

### TypeScript

```typescript
function checkArray(nums: number[], k: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function checkArray($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkArray(_ nums: [Int], _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkArray(nums: IntArray, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkArray(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func checkArray(nums []int, k int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def check_array(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def checkArray(nums: Array[Int], k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_array(nums: Vec<i32>, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-array nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec check_array(Nums :: [integer()], K :: integer()) -> boolean().
check_array(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_array(nums :: [integer], k :: integer) :: boolean
  def check_array(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkArray(nums: Array<Int64>, k: Int64): Bool {

    }
}
```

