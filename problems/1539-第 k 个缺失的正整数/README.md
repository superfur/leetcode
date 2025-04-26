# 1539. 第 k 个缺失的正整数

## 题目描述

<p>给你一个 <strong>严格升序排列</strong>&nbsp;的正整数数组 <code>arr</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>请你找到这个数组里第&nbsp;<code>k</code>&nbsp;个缺失的正整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [2,3,4,7,11], k = 5
<strong>输出：</strong>9
<strong>解释：</strong>缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3,4], k = 2
<strong>输出：</strong>6
<strong>解释：</strong>缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
	<li>对于所有&nbsp;<code>1 &lt;= i &lt; j &lt;= arr.length</code>&nbsp;的 <code>i</code>&nbsp;和 <code>j</code> 满足&nbsp;<code>arr[i] &lt; arr[j]</code>&nbsp;</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<p>你可以设计一个时间复杂度小于 O(n) 的算法解决此问题吗？</p>


## 难度

Easy

## 标签

- 数组
- 二分查找

## 提示

1. Keep track of how many positive numbers are missing as you scan the array.

## 示例

```
[2,3,4,7,11]
5
[1,2,3,4]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int findKthPositive(int[] arr, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
```

### C

```c
int findKthPositive(int* arr, int arrSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindKthPositive(int[] arr, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function(arr, k) {
    
};
```

### TypeScript

```typescript
function findKthPositive(arr: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function findKthPositive($arr, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findKthPositive(_ arr: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findKthPositive(arr: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findKthPositive(List<int> arr, int k) {
    
  }
}
```

### Go

```golang
func findKthPositive(arr []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def find_kth_positive(arr, k)
    
end
```

### Scala

```scala
object Solution {
    def findKthPositive(arr: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_kth_positive(arr: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-kth-positive arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_kth_positive(Arr :: [integer()], K :: integer()) -> integer().
find_kth_positive(Arr, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_kth_positive(arr :: [integer], k :: integer) :: integer
  def find_kth_positive(arr, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findKthPositive(arr: Array<Int64>, k: Int64): Int64 {

    }
}
```

