# 898. 子数组按位或操作

## 题目描述

<p>给定一个整数数组<meta charset="UTF-8" />&nbsp;<code>arr</code>，返回所有&nbsp;<code>arr</code>&nbsp;的非空子数组的不同按位或的数量。</p>

<p>子数组的按位或是子数组中每个整数的按位或。含有一个整数的子数组的按位或就是该整数。</p>

<p><strong>子数组</strong> 是数组内连续的非空元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [0]
<strong>输出：</strong>1
<strong>解释：</strong>
只有一个可能的结果 0 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,1,2]
<strong>输出：</strong>3
<strong>解释：</strong>
可能的子数组为 [1]，[1]，[2]，[1, 1]，[1, 2]，[1, 1, 2]。
产生的结果为 1，1，2，1，3，3 。
有三个唯一值，所以答案是 3 。
</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,4]
<strong>输出：</strong>6
<strong>解释：</strong>
可能的结果是 1，2，3，4，6，以及 7 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong><meta charset="UTF-8" /></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 动态规划

## 示例

```
[0]
[1,1,2]
[1,2,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int subarrayBitwiseORs(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        
```

### C

```c
int subarrayBitwiseORs(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SubarrayBitwiseORs(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var subarrayBitwiseORs = function(arr) {
    
};
```

### TypeScript

```typescript
function subarrayBitwiseORs(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function subarrayBitwiseORs($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func subarrayBitwiseORs(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subarrayBitwiseORs(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int subarrayBitwiseORs(List<int> arr) {
    
  }
}
```

### Go

```golang
func subarrayBitwiseORs(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def subarray_bitwise_o_rs(arr)
    
end
```

### Scala

```scala
object Solution {
    def subarrayBitwiseORs(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn subarray_bitwise_o_rs(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (subarray-bitwise-o-rs arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec subarray_bitwise_o_rs(Arr :: [integer()]) -> integer().
subarray_bitwise_o_rs(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec subarray_bitwise_o_rs(arr :: [integer]) :: integer
  def subarray_bitwise_o_rs(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func subarrayBitwiseORs(arr: Array<Int64>): Int64 {

    }
}
```

