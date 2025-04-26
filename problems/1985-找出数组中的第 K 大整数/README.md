# 1985. 找出数组中的第 K 大整数

## 题目描述

<p>给你一个字符串数组 <code>nums</code> 和一个整数 <code>k</code> 。<code>nums</code> 中的每个字符串都表示一个不含前导零的整数。</p>

<p>返回 <code>nums</code> 中表示第 <code>k</code> 大整数的字符串。</p>

<p><strong>注意：</strong>重复的数字在统计时会视为不同元素考虑。例如，如果 <code>nums</code> 是 <code>["1","2","2"]</code>，那么 <code>"2"</code> 是最大的整数，<code>"2"</code> 是第二大的整数，<code>"1"</code> 是第三大的整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = ["3","6","7","10"], k = 4
<strong>输出：</strong>"3"
<strong>解释：</strong>
nums 中的数字按非递减顺序排列为 ["3","6","7","10"]
其中第 4 大整数是 "3"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = ["2","21","12","1"], k = 3
<strong>输出：</strong>"2"
<strong>解释：</strong>
nums 中的数字按非递减顺序排列为 ["1","2","12","21"]
其中第 3 大整数是 "2"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = ["0","0"], k = 2
<strong>输出：</strong>"0"
<strong>解释：</strong>
nums 中的数字按非递减顺序排列为 ["0","0"]
其中第 2 大整数是 "0"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i].length &lt;= 100</code></li>
	<li><code>nums[i]</code> 仅由数字组成</li>
	<li><code>nums[i]</code> 不含任何前导零</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 字符串
- 分治
- 快速选择
- 排序
- 堆（优先队列）

## 提示

1. If two numbers have different lengths, which one will be larger?
2. The longer number is the larger number.
3. If two numbers have the same length, which one will be larger?
4. Compare the two numbers starting from the most significant digit. Once you have found the first digit that differs, the one with the larger digit is the larger number.

## 示例

```
["3","6","7","10"]
4
["2","21","12","1"]
3
["0","0"]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string kthLargestNumber(vector<string>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String kthLargestNumber(String[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
```

### C

```c
char* kthLargestNumber(char** nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string KthLargestNumber(string[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} nums
 * @param {number} k
 * @return {string}
 */
var kthLargestNumber = function(nums, k) {
    
};
```

### TypeScript

```typescript
function kthLargestNumber(nums: string[], k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $nums
     * @param Integer $k
     * @return String
     */
    function kthLargestNumber($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kthLargestNumber(_ nums: [String], _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kthLargestNumber(nums: Array<String>, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String kthLargestNumber(List<String> nums, int k) {
    
  }
}
```

### Go

```golang
func kthLargestNumber(nums []string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String[]} nums
# @param {Integer} k
# @return {String}
def kth_largest_number(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def kthLargestNumber(nums: Array[String], k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn kth_largest_number(nums: Vec<String>, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (kth-largest-number nums k)
  (-> (listof string?) exact-integer? string?)
  )
```

### Erlang

```erlang
-spec kth_largest_number(Nums :: [unicode:unicode_binary()], K :: integer()) -> unicode:unicode_binary().
kth_largest_number(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec kth_largest_number(nums :: [String.t], k :: integer) :: String.t
  def kth_largest_number(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kthLargestNumber(nums: Array<String>, k: Int64): String {

    }
}
```

