# 1481. 不同整数的最少数目

## 题目描述

<p>给你一个整数数组 <code>arr</code> 和一个整数 <code>k</code> 。现需要从数组中恰好移除 <code>k</code> 个元素，请找出移除后数组中不同整数的最少数目。</p>

<ol>
</ol>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [5,5,4], k = 1
<strong>输出：</strong>1
<strong>解释：</strong>移除 1 个 4 ，数组中只剩下 5 一种整数。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [4,3,1,1,3,3,2], k = 3
<strong>输出：</strong>2
<strong>解释：</strong>先移除 4、2 ，然后再移除两个 1 中的任意 1 个或者三个 3 中的任意 1 个，最后剩下 1 和 3 两种整数。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length&nbsp;&lt;= 10^5</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10^9</code></li>
	<li><code>0 &lt;= k&nbsp;&lt;= arr.length</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 计数
- 排序

## 提示

1. Use a map to count the frequencies of the numbers in the array.
2. An optimal strategy is to remove the numbers with the smallest count first.

## 示例

```
[5,5,4]
1
[4,3,1,1,3,3,2]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findLeastNumOfUniqueInts(vector<int>& arr, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
```

### C

```c
int findLeastNumOfUniqueInts(int* arr, int arrSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindLeastNumOfUniqueInts(int[] arr, int k) {
        
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
var findLeastNumOfUniqueInts = function(arr, k) {
    
};
```

### TypeScript

```typescript
function findLeastNumOfUniqueInts(arr: number[], k: number): number {
    
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
    function findLeastNumOfUniqueInts($arr, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLeastNumOfUniqueInts(_ arr: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLeastNumOfUniqueInts(arr: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findLeastNumOfUniqueInts(List<int> arr, int k) {
    
  }
}
```

### Go

```golang
func findLeastNumOfUniqueInts(arr []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def find_least_num_of_unique_ints(arr, k)
    
end
```

### Scala

```scala
object Solution {
    def findLeastNumOfUniqueInts(arr: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_least_num_of_unique_ints(arr: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-least-num-of-unique-ints arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_least_num_of_unique_ints(Arr :: [integer()], K :: integer()) -> integer().
find_least_num_of_unique_ints(Arr, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_least_num_of_unique_ints(arr :: [integer], k :: integer) :: integer
  def find_least_num_of_unique_ints(arr, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLeastNumOfUniqueInts(arr: Array<Int64>, k: Int64): Int64 {

    }
}
```

