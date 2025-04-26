# 1471. 数组中的 k 个最强值

## 题目描述

<p>给你一个整数数组 <code>arr</code> 和一个整数 <code>k</code> 。</p>

<p>设 <code>m</code> 为数组的中位数，只要满足下述两个前提之一，就可以判定 <code>arr[i]</code> 的值比 <code>arr[j]</code> 的值更强：</p>

<ul>
	<li>&nbsp;<code>|arr[i] - m| &gt; |arr[j]&nbsp;- m|</code></li>
	<li>&nbsp;<code>|arr[i] - m| == |arr[j] - m|</code>，且 <code>arr[i] &gt; arr[j]</code></li>
</ul>

<p>请返回由数组中最强的 <code>k</code> 个值组成的列表。答案可以以 <strong>任意顺序</strong> 返回。</p>

<p><strong>中位数</strong> 是一个有序整数列表中处于中间位置的值。形式上，如果列表的长度为 <code>n</code> ，那么中位数就是该有序列表（下标从 0 开始）中位于 <code>((n - 1) / 2)</code> 的元素。</p>

<ul>
	<li>例如 <code>arr =&nbsp;[6, -3, 7, 2, 11]</code>，<code>n = 5</code>：数组排序后得到 <code>arr = [-3, 2, 6, 7, 11]</code> ，数组的中间位置为 <code>m = ((5 - 1) / 2) = 2</code> ，中位数 <code>arr[m]</code> 的值为 <code>6</code> 。</li>
	<li>例如 <code>arr =&nbsp;[-7, 22, 17, 3]</code>，<code>n = 4</code>：数组排序后得到&nbsp;<code>arr = [-7, 3, 17, 22]</code> ，数组的中间位置为&nbsp;<code>m = ((4 - 1) / 2) = 1</code> ，中位数 <code>arr[m]</code> 的值为 <code>3</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3,4,5], k = 2
<strong>输出：</strong>[5,1]
<strong>解释：</strong>中位数为 3，按从强到弱顺序排序后，数组变为 [5,1,4,2,3]。最强的两个元素是 [5, 1]。[1, 5] 也是正确答案。
注意，尽管 |5 - 3| == |1 - 3| ，但是 5 比 1 更强，因为 5 &gt; 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,1,3,5,5], k = 2
<strong>输出：</strong>[5,5]
<strong>解释：</strong>中位数为 3, 按从强到弱顺序排序后，数组变为 [5,5,1,1,3]。最强的两个元素是 [5, 5]。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [6,7,11,7,6,8], k = 5
<strong>输出：</strong>[11,8,6,6,7]
<strong>解释：</strong>中位数为 7, 按从强到弱顺序排序后，数组变为 [11,8,6,6,7,7]。
[11,8,6,6,7] 的任何排列都是正确答案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= arr.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 排序

## 提示

1. Calculate the centre of the array as defined in the statement.
2. Use custom sort function to sort values (Strongest first), then slice the first k.

## 示例

```
[1,2,3,4,5]
2
[1,1,3,5,5]
2
[6,7,11,7,6,8]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getStrongest(vector<int>& arr, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] getStrongest(int[] arr, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getStrongest(int* arr, int arrSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] GetStrongest(int[] arr, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number[]}
 */
var getStrongest = function(arr, k) {
    
};
```

### TypeScript

```typescript
function getStrongest(arr: number[], k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer[]
     */
    function getStrongest($arr, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getStrongest(_ arr: [Int], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getStrongest(arr: IntArray, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getStrongest(List<int> arr, int k) {
    
  }
}
```

### Go

```golang
func getStrongest(arr []int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer[]}
def get_strongest(arr, k)
    
end
```

### Scala

```scala
object Solution {
    def getStrongest(arr: Array[Int], k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_strongest(arr: Vec<i32>, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-strongest arr k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_strongest(Arr :: [integer()], K :: integer()) -> [integer()].
get_strongest(Arr, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_strongest(arr :: [integer], k :: integer) :: [integer]
  def get_strongest(arr, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getStrongest(arr: Array<Int64>, k: Int64): Array<Int64> {

    }
}
```

