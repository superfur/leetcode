# 面试题 17.04. 消失的数字

## 题目描述

<p>数组<code>nums</code>包含从<code>0</code>到<code>n</code>的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？</p>

<p><strong>注意：</strong>本题相对书上原题稍作改动</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[3,0,1]
<strong>输出：</strong>2</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[9,6,4,2,3,5,7,0,1]
<strong>输出：</strong>8
</pre>


## 难度

Easy

## 标签

- 位运算
- 数组
- 哈希表
- 数学
- 排序

## 提示

1. 你需要多长时间才能算出缺失数字的最小有效位?
2. 要找到缺失的数字中的最小有效位，你其实知道有多少个 0 和 1。例如，如果你看到最小有效位有 3 个 0 和 3 个 1，那么缺失的数字的最小值必定是 1。想想看:在任何 0 和 1 的序列中，你会得到 0，然后是 1，然后又是 0，然后又是 1，以此类推。
3. 一旦确定最小有效位是 0(或 1)，就可以排除所有不以 0 作为最小有效位的数。这个问题和前面的有什么不同?

## 示例

```
[3,0,1]
[9,6,4,2,3,5,7,0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int missingNumber(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
```

### C

```c
int missingNumber(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MissingNumber(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    
};
```

### TypeScript

```typescript
function missingNumber(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function missingNumber($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func missingNumber(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun missingNumber(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int missingNumber(List<int> nums) {
    
  }
}
```

### Go

```golang
func missingNumber(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def missing_number(nums)
    
end
```

### Scala

```scala
object Solution {
    def missingNumber(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (missing-number nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec missing_number(Nums :: [integer()]) -> integer().
missing_number(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec missing_number(nums :: [integer]) :: integer
  def missing_number(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func missingNumber(nums: Array<Int64>): Int64 {

    }
}
```

