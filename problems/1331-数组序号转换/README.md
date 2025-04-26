# 1331. 数组序号转换

## 题目描述

<p>给你一个整数数组&nbsp;<code>arr</code> ，请你将数组中的每个元素替换为它们排序后的序号。</p>

<p>序号代表了一个元素有多大。序号编号的规则如下：</p>

<ul>
	<li>序号从 1 开始编号。</li>
	<li>一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。</li>
	<li>每个数字的序号都应该尽可能地小。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [40,10,20,30]
<strong>输出：</strong>[4,1,2,3]
<strong>解释：</strong>40 是最大的元素。 10 是最小的元素。 20 是第二小的数字。 30 是第三小的数字。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [100,100,100]
<strong>输出：</strong>[1,1,1]
<strong>解释：</strong>所有元素有相同的序号。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [37,12,28,9,100,56,80,5,12]
<strong>输出：</strong>[5,3,4,2,8,6,7,1,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 排序

## 提示

1. Use a temporary array to copy the array and sort it.
2. The rank of each element is the number of unique elements smaller than it in the sorted array plus one.

## 示例

```
[40,10,20,30]
[100,100,100]
[37,12,28,9,100,56,80,5,12]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] arrayRankTransform(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* arrayRankTransform(int* arr, int arrSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ArrayRankTransform(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    
};
```

### TypeScript

```typescript
function arrayRankTransform(arr: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function arrayRankTransform($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func arrayRankTransform(_ arr: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun arrayRankTransform(arr: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> arrayRankTransform(List<int> arr) {
    
  }
}
```

### Go

```golang
func arrayRankTransform(arr []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer[]}
def array_rank_transform(arr)
    
end
```

### Scala

```scala
object Solution {
    def arrayRankTransform(arr: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (array-rank-transform arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec array_rank_transform(Arr :: [integer()]) -> [integer()].
array_rank_transform(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec array_rank_transform(arr :: [integer]) :: [integer]
  def array_rank_transform(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func arrayRankTransform(arr: Array<Int64>): Array<Int64> {

    }
}
```

