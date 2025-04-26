# 852. 山脉数组的峰顶索引

## 题目描述

<p>给定一个长度为&nbsp;<code>n</code>&nbsp;的整数 <strong>山脉&nbsp;</strong>数组&nbsp;<code>arr</code>&nbsp;，其中的值递增到一个&nbsp;<strong>峰值元素</strong>&nbsp;然后递减。</p>

<p>返回峰值元素的下标。</p>

<p>你必须设计并实现时间复杂度为 <code>O(log(n))</code> 的解决方案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [0,1,0]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [0,2,1,0]
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [0,10,5,2]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>6</sup></code></li>
	<li>题目数据 <strong>保证</strong> <code>arr</code> 是一个山脉数组</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 示例

```
[0,1,0]
[0,2,1,0]
[0,10,5,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
```

### C

```c
int peakIndexInMountainArray(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int PeakIndexInMountainArray(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function(arr) {
    
};
```

### TypeScript

```typescript
function peakIndexInMountainArray(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function peakIndexInMountainArray($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func peakIndexInMountainArray(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun peakIndexInMountainArray(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int peakIndexInMountainArray(List<int> arr) {
    
  }
}
```

### Go

```golang
func peakIndexInMountainArray(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def peak_index_in_mountain_array(arr)
    
end
```

### Scala

```scala
object Solution {
    def peakIndexInMountainArray(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (peak-index-in-mountain-array arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec peak_index_in_mountain_array(Arr :: [integer()]) -> integer().
peak_index_in_mountain_array(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec peak_index_in_mountain_array(arr :: [integer]) :: integer
  def peak_index_in_mountain_array(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func peakIndexInMountainArray(arr: Array<Int64>): Int64 {

    }
}
```

