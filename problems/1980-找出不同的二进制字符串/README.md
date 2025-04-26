# 1980. 找出不同的二进制字符串

## 题目描述

<p>给你一个字符串数组 <code>nums</code> ，该数组由 <code>n</code> 个 <strong>互不相同</strong> 的二进制字符串组成，且每个字符串长度都是 <code>n</code> 。请你找出并返回一个长度为&nbsp;<code>n</code>&nbsp;且&nbsp;<strong>没有出现</strong> 在 <code>nums</code> 中的二进制字符串<em>。</em>如果存在多种答案，只需返回 <strong>任意一个</strong> 即可。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = ["01","10"]
<strong>输出：</strong>"11"
<strong>解释：</strong>"11" 没有出现在 nums 中。"00" 也是正确答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = ["00","01"]
<strong>输出：</strong>"11"
<strong>解释：</strong>"11" 没有出现在 nums 中。"10" 也是正确答案。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = ["111","011","001"]
<strong>输出：</strong>"101"
<strong>解释：</strong>"101" 没有出现在 nums 中。"000"、"010"、"100"、"110" 也是正确答案。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 16</code></li>
	<li><code>nums[i].length == n</code></li>
	<li><code>nums[i] </code>为 <code>'0'</code> 或 <code>'1'</code></li>
	<li><code>nums</code> 中的所有字符串 <strong>互不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 回溯

## 提示

1. We can convert the given strings into base 10 integers.
2. Can we use recursion to generate all possible strings?

## 示例

```
["01","10"]
["00","01"]
["111","011","001"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public String findDifferentBinaryString(String[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
```

### C

```c
char* findDifferentBinaryString(char** nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string FindDifferentBinaryString(string[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function(nums) {
    
};
```

### TypeScript

```typescript
function findDifferentBinaryString(nums: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $nums
     * @return String
     */
    function findDifferentBinaryString($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findDifferentBinaryString(_ nums: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findDifferentBinaryString(nums: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String findDifferentBinaryString(List<String> nums) {
    
  }
}
```

### Go

```golang
func findDifferentBinaryString(nums []string) string {
    
}
```

### Ruby

```ruby
# @param {String[]} nums
# @return {String}
def find_different_binary_string(nums)
    
end
```

### Scala

```scala
object Solution {
    def findDifferentBinaryString(nums: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (find-different-binary-string nums)
  (-> (listof string?) string?)
  )
```

### Erlang

```erlang
-spec find_different_binary_string(Nums :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
find_different_binary_string(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_different_binary_string(nums :: [String.t]) :: String.t
  def find_different_binary_string(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findDifferentBinaryString(nums: Array<String>): String {

    }
}
```

