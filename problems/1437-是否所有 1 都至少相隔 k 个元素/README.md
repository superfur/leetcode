# 1437. 是否所有 1 都至少相隔 k 个元素

## 题目描述

<p>给你一个由若干 <code>0</code> 和 <code>1</code> 组成的数组 <code>nums</code> 以及整数 <code>k</code>。如果所有 <code>1</code> 都至少相隔 <code>k</code> 个元素，则返回 <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size: 12.6px; background-color: rgb(249, 242, 244);">true</span></font>&nbsp;；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_1_1791.png" style="width: 214px;" /></strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,0,0,1,0,0,1], k = 2
<strong>输出：</strong>true
<strong>解释：</strong>每个 1 都至少相隔 2 个元素。</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_2_1791.png" style="height: 86px; width: 160px;" /></strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,0,1,0,1], k = 2
<strong>输出：</strong>false
<strong>解释：</strong>第二个 1 和第三个 1 之间只隔了 1 个元素。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= nums.length</code></li>
	<li><code>nums[i]</code> 的值为 <code>0</code> 或 <code>1</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.

## 示例

```
[1,0,0,0,1,0,0,1]
2
[1,0,0,1,0,1]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
```

### C

```c
bool kLengthApart(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        
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
var kLengthApart = function(nums, k) {
    
};
```

### TypeScript

```typescript
function kLengthApart(nums: number[], k: number): boolean {
    
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
    function kLengthApart($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kLengthApart(_ nums: [Int], _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kLengthApart(nums: IntArray, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool kLengthApart(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func kLengthApart(nums []int, k int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def k_length_apart(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def kLengthApart(nums: Array[Int], k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (k-length-apart nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec k_length_apart(Nums :: [integer()], K :: integer()) -> boolean().
k_length_apart(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec k_length_apart(nums :: [integer], k :: integer) :: boolean
  def k_length_apart(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kLengthApart(nums: Array<Int64>, k: Int64): Bool {

    }
}
```

