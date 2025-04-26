# 1187. 使数组严格递增

## 题目描述

<p>给你两个整数数组&nbsp;<code>arr1</code> 和 <code>arr2</code>，返回使&nbsp;<code>arr1</code>&nbsp;严格递增所需要的最小「操作」数（可能为 0）。</p>

<p>每一步「操作」中，你可以分别从 <code>arr1</code> 和 <code>arr2</code> 中各选出一个索引，分别为&nbsp;<code>i</code> 和&nbsp;<code>j</code>，<code>0 &lt;=&nbsp;i &lt; arr1.length</code>&nbsp;和&nbsp;<code>0 &lt;= j &lt; arr2.length</code>，然后进行赋值运算&nbsp;<code>arr1[i] = arr2[j]</code>。</p>

<p>如果无法让&nbsp;<code>arr1</code>&nbsp;严格递增，请返回&nbsp;<code>-1</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
<strong>输出：</strong>1
<strong>解释：</strong>用 2 来替换 <code>5，之后</code> <code>arr1 = [1, 2, 3, 6, 7]</code>。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr1 = [1,5,3,6,7], arr2 = [4,3,1]
<strong>输出：</strong>2
<strong>解释：</strong>用 3 来替换 <code>5，然后</code>用 4 来替换 3<code>，得到</code> <code>arr1 = [1, 3, 4, 6, 7]</code>。
</pre>

<p><strong class="example">示例&nbsp;3：</strong></p>

<pre>
<strong>输入：</strong>arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
<strong>输出：</strong>-1
<strong>解释：</strong>无法使 <code>arr1 严格递增</code>。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 2000</code></li>
	<li><code>0 &lt;= arr1[i], arr2[i] &lt;= 10^9</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Hard

## 标签

- 数组
- 二分查找
- 动态规划
- 排序

## 提示

1. Use dynamic programming.
2. The state would be the index in arr1 and the index of the previous element in arr2 after sorting it and removing duplicates.

## 示例

```
[1,5,3,6,7]
[1,3,2,4]
[1,5,3,6,7]
[4,3,1]
[1,5,3,6,7]
[1,6,3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        
    }
};
```

### Java

```java
class Solution {
    public int makeArrayIncreasing(int[] arr1, int[] arr2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        
```

### C

```c
int makeArrayIncreasing(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int MakeArrayIncreasing(int[] arr1, int[] arr2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var makeArrayIncreasing = function(arr1, arr2) {
    
};
```

### TypeScript

```typescript
function makeArrayIncreasing(arr1: number[], arr2: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer
     */
    function makeArrayIncreasing($arr1, $arr2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeArrayIncreasing(_ arr1: [Int], _ arr2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeArrayIncreasing(arr1: IntArray, arr2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int makeArrayIncreasing(List<int> arr1, List<int> arr2) {
    
  }
}
```

### Go

```golang
func makeArrayIncreasing(arr1 []int, arr2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer}
def make_array_increasing(arr1, arr2)
    
end
```

### Scala

```scala
object Solution {
    def makeArrayIncreasing(arr1: Array[Int], arr2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_array_increasing(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (make-array-increasing arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec make_array_increasing(Arr1 :: [integer()], Arr2 :: [integer()]) -> integer().
make_array_increasing(Arr1, Arr2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_array_increasing(arr1 :: [integer], arr2 :: [integer]) :: integer
  def make_array_increasing(arr1, arr2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeArrayIncreasing(arr1: Array<Int64>, arr2: Array<Int64>): Int64 {

    }
}
```

