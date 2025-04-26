# 1442. 形成两个异或相等数组的三元组数目

## 题目描述

<p>给你一个整数数组 <code>arr</code> 。</p>

<p>现需要从数组中取三个下标 <code>i</code>、<code>j</code> 和 <code>k</code> ，其中 <code>(0 &lt;= i &lt; j &lt;= k &lt; arr.length)</code> 。</p>

<p><code>a</code> 和 <code>b</code> 定义如下：</p>

<ul>
	<li><code>a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]</code></li>
	<li><code>b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]</code></li>
</ul>

<p>注意：<strong>^</strong> 表示 <strong>按位异或</strong> 操作。</p>

<p>请返回能够令 <code>a == b</code> 成立的三元组 (<code>i</code>, <code>j</code> , <code>k</code>) 的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [2,3,1,6,7]
<strong>输出：</strong>4
<strong>解释：</strong>满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [1,1,1,1,1]
<strong>输出：</strong>10
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [2,3]
<strong>输出：</strong>0
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>arr = [1,3,5,7,9]
<strong>输出：</strong>3
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>arr = [7,11,12,9,5,2,7,17,22]
<strong>输出：</strong>8
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 300</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10^8</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 哈希表
- 数学
- 前缀和

## 提示

1. We are searching for sub-array of length ≥ 2 and we need to split it to 2 non-empty arrays so that the xor of the first array is equal to the xor of the second array. This is equivalent to searching for sub-array with xor = 0.
2. Keep the prefix xor of arr in another array, check the xor of all sub-arrays in O(n^2), if the xor of sub-array of length x is 0 add x-1 to the answer.

## 示例

```
[2,3,1,6,7]
[1,1,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countTriplets(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int countTriplets(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
```

### C

```c
int countTriplets(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountTriplets(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var countTriplets = function(arr) {
    
};
```

### TypeScript

```typescript
function countTriplets(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function countTriplets($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countTriplets(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countTriplets(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countTriplets(List<int> arr) {
    
  }
}
```

### Go

```golang
func countTriplets(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def count_triplets(arr)
    
end
```

### Scala

```scala
object Solution {
    def countTriplets(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_triplets(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-triplets arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_triplets(Arr :: [integer()]) -> integer().
count_triplets(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_triplets(arr :: [integer]) :: integer
  def count_triplets(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countTriplets(arr: Array<Int64>): Int64 {

    }
}
```

