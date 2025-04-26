# 2023. 连接后等于目标字符串的字符串对

## 题目描述

<p>给你一个 <strong>数字</strong>&nbsp;字符串数组 <code>nums</code>&nbsp;和一个 <strong>数字</strong>&nbsp;字符串 <code>target</code>&nbsp;，请你返回 <code>nums[i] + nums[j]</code>&nbsp;（两个字符串连接）结果等于 <code>target</code>&nbsp;的下标 <code>(i, j)</code>&nbsp;（需满足 <code>i != j</code>）的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = ["777","7","77","77"], target = "7777"
<b>输出：</b>4
<b>解释：</b>符合要求的下标对包括：
- (0, 1)："777" + "7"
- (1, 0)："7" + "777"
- (2, 3)："77" + "77"
- (3, 2)："77" + "77"
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = ["123","4","12","34"], target = "1234"
<b>输出：</b>2
<b>解释：</b>符合要求的下标对包括
- (0, 1)："123" + "4"
- (2, 3)："12" + "34"
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = ["1","1","1"], target = "11"
<b>输出：</b>6
<b>解释：</b>符合要求的下标对包括
- (0, 1)："1" + "1"
- (1, 0)："1" + "1"
- (0, 2)："1" + "1"
- (2, 0)："1" + "1"
- (1, 2)："1" + "1"
- (2, 1)："1" + "1"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i].length &lt;= 100</code></li>
	<li><code>2 &lt;= target.length &lt;= 100</code></li>
	<li><code>nums[i]</code>&nbsp;和&nbsp;<code>target</code>&nbsp;只包含数字。</li>
	<li><code>nums[i]</code>&nbsp;和&nbsp;<code>target</code>&nbsp;不含有任何前导 0 。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 计数

## 提示

1. Try to concatenate every two different strings from the list.
2. Count the number of pairs with concatenation equals to target.

## 示例

```
["777","7","77","77"]
"7777"
["123","4","12","34"]
"1234"
["1","1","1"]
"11"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numOfPairs(vector<string>& nums, string target) {
        
    }
};
```

### Java

```java
class Solution {
    public int numOfPairs(String[] nums, String target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
```

### C

```c
int numOfPairs(char** nums, int numsSize, char* target) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumOfPairs(string[] nums, string target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} nums
 * @param {string} target
 * @return {number}
 */
var numOfPairs = function(nums, target) {
    
};
```

### TypeScript

```typescript
function numOfPairs(nums: string[], target: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $nums
     * @param String $target
     * @return Integer
     */
    function numOfPairs($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numOfPairs(_ nums: [String], _ target: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numOfPairs(nums: Array<String>, target: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numOfPairs(List<String> nums, String target) {
    
  }
}
```

### Go

```golang
func numOfPairs(nums []string, target string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} nums
# @param {String} target
# @return {Integer}
def num_of_pairs(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def numOfPairs(nums: Array[String], target: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_of_pairs(nums: Vec<String>, target: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-of-pairs nums target)
  (-> (listof string?) string? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_of_pairs(Nums :: [unicode:unicode_binary()], Target :: unicode:unicode_binary()) -> integer().
num_of_pairs(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_of_pairs(nums :: [String.t], target :: String.t) :: integer
  def num_of_pairs(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numOfPairs(nums: Array<String>, target: String): Int64 {

    }
}
```

