# 969. 煎饼排序

## 题目描述

<p>给你一个整数数组 <code>arr</code> ，请使用 <strong>煎饼翻转</strong><em> </em>完成对数组的排序。</p>

<p>一次煎饼翻转的执行过程如下：</p>

<ul>
	<li>选择一个整数 <code>k</code> ，<code>1 <= k <= arr.length</code></li>
	<li>反转子数组 <code>arr[0...k-1]</code>（<strong>下标从 0 开始</strong>）</li>
</ul>

<p>例如，<code>arr = [3,2,1,4]</code> ，选择 <code>k = 3</code> 进行一次煎饼翻转，反转子数组 <code>[3,2,1]</code> ，得到 <code>arr = [<strong>1</strong>,<strong>2</strong>,<strong>3</strong>,4]</code> 。</p>

<p>以数组形式返回能使 <code>arr</code> 有序的煎饼翻转操作所对应的 <code>k</code> 值序列。任何将数组排序且翻转次数在 <code>10 * arr.length</code> 范围内的有效答案都将被判断为正确。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>[3,2,4,1]
<strong>输出：</strong>[4,2,4,3]
<strong>解释：</strong>
我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
初始状态 arr = [3, 2, 4, 1]
第一次翻转后（k = 4）：arr = [<strong>1</strong>, <strong>4</strong>, <strong>2</strong>, <strong>3</strong>]
第二次翻转后（k = 2）：arr = [<strong>4</strong>, <strong>1</strong>, 2, 3]
第三次翻转后（k = 4）：arr = [<strong>3</strong>, <strong>2</strong>, <strong>1</strong>, <strong>4</strong>]
第四次翻转后（k = 3）：arr = [<strong>1</strong>, <strong>2</strong>, <strong>3</strong>, 4]，此时已完成排序。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>[1,2,3]
<strong>输出：</strong>[]
<strong>解释：
</strong>输入已经排序，因此不需要翻转任何内容。
请注意，其他可能的答案，如 [3，3] ，也将被判断为正确。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= arr.length <= 100</code></li>
	<li><code>1 <= arr[i] <= arr.length</code></li>
	<li><code>arr</code> 中的所有整数互不相同（即，<code>arr</code> 是从 <code>1</code> 到 <code>arr.length</code> 整数的一个排列）</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 双指针
- 排序

## 示例

```
[3,2,4,1]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> pancakeSort(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pancakeSort(int* arr, int arrSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> PancakeSort(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var pancakeSort = function(arr) {
    
};
```

### TypeScript

```typescript
function pancakeSort(arr: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function pancakeSort($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func pancakeSort(_ arr: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun pancakeSort(arr: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> pancakeSort(List<int> arr) {
    
  }
}
```

### Go

```golang
func pancakeSort(arr []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer[]}
def pancake_sort(arr)
    
end
```

### Scala

```scala
object Solution {
    def pancakeSort(arr: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn pancake_sort(arr: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (pancake-sort arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec pancake_sort(Arr :: [integer()]) -> [integer()].
pancake_sort(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec pancake_sort(arr :: [integer]) :: [integer]
  def pancake_sort(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func pancakeSort(arr: Array<Int64>): ArrayList<Int64> {

    }
}
```

