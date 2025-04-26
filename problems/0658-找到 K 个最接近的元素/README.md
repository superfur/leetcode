# 658. 找到 K 个最接近的元素

## 题目描述

<p>给定一个 <strong>排序好</strong> 的数组&nbsp;<code>arr</code> ，两个整数 <code>k</code> 和 <code>x</code> ，从数组中找到最靠近 <code>x</code>（两数之差最小）的 <code>k</code> 个数。返回的结果必须要是按升序排好的。</p>

<p>整数 <code>a</code> 比整数 <code>b</code> 更接近 <code>x</code> 需要满足：</p>

<ul>
	<li><code>|a - x| &lt; |b - x|</code> 或者</li>
	<li><code>|a - x| == |b - x|</code> 且 <code>a &lt; b</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3,4,5], k = 4, x = 3
<strong>输出：</strong>[1,2,3,4]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,1,2,3,4,5], k = 4, x = -1
<strong>输出：</strong>[1,1,2,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= arr.length</code></li>
	<li><code>1 &lt;= arr.length&nbsp;&lt;= 10<sup>4</sup></code><meta charset="UTF-8" /></li>
	<li><code>arr</code>&nbsp;按 <strong>升序</strong> 排列</li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= arr[i], x &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 二分查找
- 排序
- 滑动窗口
- 堆（优先队列）

## 示例

```
[1,2,3,4,5]
4
3
[1,1,2,3,4,5]
4
-1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findClosestElements(int* arr, int arrSize, int k, int x, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> FindClosestElements(int[] arr, int k, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findClosestElements = function(arr, k, x) {
    
};
```

### TypeScript

```typescript
function findClosestElements(arr: number[], k: number, x: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @param Integer $x
     * @return Integer[]
     */
    function findClosestElements($arr, $k, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findClosestElements(_ arr: [Int], _ k: Int, _ x: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findClosestElements(arr: IntArray, k: Int, x: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findClosestElements(List<int> arr, int k, int x) {
    
  }
}
```

### Go

```golang
func findClosestElements(arr []int, k int, x int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def find_closest_elements(arr, k, x)
    
end
```

### Scala

```scala
object Solution {
    def findClosestElements(arr: Array[Int], k: Int, x: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_closest_elements(arr: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-closest-elements arr k x)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_closest_elements(Arr :: [integer()], K :: integer(), X :: integer()) -> [integer()].
find_closest_elements(Arr, K, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_closest_elements(arr :: [integer], k :: integer, x :: integer) :: [integer]
  def find_closest_elements(arr, k, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findClosestElements(arr: Array<Int64>, k: Int64, x: Int64): ArrayList<Int64> {

    }
}
```

