# 1356. 根据数字二进制下 1 的数目排序

## 题目描述

<p>给你一个整数数组&nbsp;<code>arr</code>&nbsp;。请你将数组中的元素按照其二进制表示中数字 <strong>1</strong> 的数目升序排序。</p>

<p>如果存在多个数字二进制中&nbsp;<strong>1</strong>&nbsp;的数目相同，则必须将它们按照数值大小升序排列。</p>

<p>请你返回排序后的数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [0,1,2,3,4,5,6,7,8]
<strong>输出：</strong>[0,1,2,4,8,3,5,6,7]
<strong>解释：</strong>[0] 是唯一一个有 0 个 1 的数。
[1,2,4,8] 都有 1 个 1 。
[3,5,6] 有 2 个 1 。
[7] 有 3 个 1 。
按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [1024,512,256,128,64,32,16,8,4,2,1]
<strong>输出：</strong>[1,2,4,8,16,32,64,128,256,512,1024]
<strong>解释：</strong>数组中所有整数二进制下都只有 1 个 1 ，所以你需要按照数值大小将它们排序。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [10000,10000]
<strong>输出：</strong>[10000,10000]
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>arr = [2,3,5,7,11,13,17,19]
<strong>输出：</strong>[2,3,5,17,7,11,13,19]
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>arr = [10,100,1000,10000]
<strong>输出：</strong>[10,100,10000,1000]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 500</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10^4</code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组
- 计数
- 排序

## 提示

1. Simulate the problem. Count the number of 1's in the binary representation of each integer.
2. Sort by the number of 1's ascending and by the value in case of tie.

## 示例

```
[0,1,2,3,4,5,6,7,8]
[1024,512,256,128,64,32,16,8,4,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] sortByBits(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortByBits(int* arr, int arrSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SortByBits(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {
    
};
```

### TypeScript

```typescript
function sortByBits(arr: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function sortByBits($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sortByBits(_ arr: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sortByBits(arr: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> sortByBits(List<int> arr) {
    
  }
}
```

### Go

```golang
func sortByBits(arr []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer[]}
def sort_by_bits(arr)
    
end
```

### Scala

```scala
object Solution {
    def sortByBits(arr: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sort_by_bits(arr: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (sort-by-bits arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec sort_by_bits(Arr :: [integer()]) -> [integer()].
sort_by_bits(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sort_by_bits(arr :: [integer]) :: [integer]
  def sort_by_bits(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sortByBits(arr: Array<Int64>): Array<Int64> {

    }
}
```

