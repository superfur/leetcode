# 1338. 数组大小减半

## 题目描述

<p>给你一个整数数组&nbsp;<code>arr</code>。你可以从中选出一个整数集合，并删除这些整数在数组中的每次出现。</p>

<p>返回&nbsp;<strong>至少</strong>&nbsp;能删除数组中的一半整数的整数集合的最小大小。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [3,3,3,3,5,5,5,2,2,7]
<strong>输出：</strong>2
<strong>解释：</strong>选择 {3,7} 使得结果数组为 [5,5,5,2,2]、长度为 5（原数组长度的一半）。
大小为 2 的可行集合有 {3,5},{3,2},{5,2}。
选择 {2,7} 是不可行的，它的结果数组为 [3,3,3,3,5,5,5]，新数组长度大于原数组的二分之一。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [7,7,7,7,7,7]
<strong>输出：</strong>1
<strong>解释：</strong>我们只能选择集合 {7}，结果数组为空。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>arr.length</code>&nbsp;为偶数</li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 排序
- 堆（优先队列）

## 提示

1. Count the frequency of each integer in the array.
2. Start with an empty set, add to the set the integer with the maximum frequency.
3. Keep Adding the integer with the max frequency until you remove at least half of the integers.

## 示例

```
[3,3,3,3,5,5,5,2,2,7]
[7,7,7,7,7,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSetSize(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSetSize(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
```

### C

```c
int minSetSize(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSetSize(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function(arr) {
    
};
```

### TypeScript

```typescript
function minSetSize(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function minSetSize($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSetSize(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSetSize(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSetSize(List<int> arr) {
    
  }
}
```

### Go

```golang
func minSetSize(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def min_set_size(arr)
    
end
```

### Scala

```scala
object Solution {
    def minSetSize(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_set_size(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-set-size arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_set_size(Arr :: [integer()]) -> integer().
min_set_size(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_set_size(arr :: [integer]) :: integer
  def min_set_size(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSetSize(arr: Array<Int64>): Int64 {

    }
}
```

