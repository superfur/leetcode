# 228. 汇总区间

## 题目描述

<p>给定一个 &nbsp;<strong>无重复元素</strong> 的&nbsp;<strong>有序</strong> 整数数组 <code>nums</code> 。</p>

<p>返回 <em><strong>恰好覆盖数组中所有数字</strong> 的 <strong>最小有序</strong> 区间范围列表&nbsp;</em>。也就是说，<code>nums</code> 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 <code>nums</code> 的数字 <code>x</code> 。</p>

<p>列表中的每个区间范围 <code>[a,b]</code> 应该按如下格式输出：</p>

<ul>
	<li><code>"a-&gt;b"</code> ，如果 <code>a != b</code></li>
	<li><code>"a"</code> ，如果 <code>a == b</code></li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,2,4,5,7]
<strong>输出：</strong>["0-&gt;2","4-&gt;5","7"]
<strong>解释：</strong>区间范围是：
[0,2] --&gt; "0-&gt;2"
[4,5] --&gt; "4-&gt;5"
[7,7] --&gt; "7"
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,2,3,4,6,8,9]
<strong>输出：</strong>["0","2-&gt;4","6","8-&gt;9"]
<strong>解释：</strong>区间范围是：
[0,0] --&gt; "0"
[2,4] --&gt; "2-&gt;4"
[6,6] --&gt; "6"
[8,9] --&gt; "8-&gt;9"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 20</code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>nums</code> 中的所有值都 <strong>互不相同</strong></li>
	<li><code>nums</code> 按升序排列</li>
</ul>


## 难度

Easy

## 标签

- 数组

## 示例

```
[0,1,2,4,5,7]
[0,2,3,4,6,8,9]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> summaryRanges(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** summaryRanges(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> SummaryRanges(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    
};
```

### TypeScript

```typescript
function summaryRanges(nums: number[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return String[]
     */
    function summaryRanges($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func summaryRanges(_ nums: [Int]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun summaryRanges(nums: IntArray): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> summaryRanges(List<int> nums) {
    
  }
}
```

### Go

```golang
func summaryRanges(nums []int) []string {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {String[]}
def summary_ranges(nums)
    
end
```

### Scala

```scala
object Solution {
    def summaryRanges(nums: Array[Int]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (summary-ranges nums)
  (-> (listof exact-integer?) (listof string?))
  )
```

### Erlang

```erlang
-spec summary_ranges(Nums :: [integer()]) -> [unicode:unicode_binary()].
summary_ranges(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec summary_ranges(nums :: [integer]) :: [String.t]
  def summary_ranges(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func summaryRanges(nums: Array<Int64>): ArrayList<String> {

    }
}
```

