# LCR 075. 数组的相对排序

## 题目描述

<p>给定两个数组，<code>arr1</code> 和&nbsp;<code>arr2</code>，</p>

<ul>
	<li><code>arr2</code>&nbsp;中的元素各不相同</li>
	<li><code>arr2</code> 中的每个元素都出现在&nbsp;<code>arr1</code>&nbsp;中</li>
</ul>

<p>对 <code>arr1</code>&nbsp;中的元素进行排序，使 <code>arr1</code> 中项的相对顺序和&nbsp;<code>arr2</code>&nbsp;中的相对顺序相同。未在&nbsp;<code>arr2</code>&nbsp;中出现过的元素需要按照升序放在&nbsp;<code>arr1</code>&nbsp;的末尾。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
<strong>输出：</strong>[2,2,2,1,4,3,3,9,6,7,19]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= arr1[i], arr2[i] &lt;= 1000</code></li>
	<li><code>arr2</code>&nbsp;中的元素&nbsp;<code>arr2[i]</code>&nbsp;各不相同</li>
	<li><code>arr2</code> 中的每个元素&nbsp;<code>arr2[i]</code>&nbsp;都出现在&nbsp;<code>arr1</code>&nbsp;中</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 1122&nbsp;题相同：<a href="https://leetcode-cn.com/problems/relative-sort-array/">https://leetcode-cn.com/problems/relative-sort-array/</a>&nbsp;</p>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 计数排序
- 排序

## 示例

```
[2,3,1,3,2,4,6,7,9,2,19]
[2,1,4,3,9,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {

    }
};
```

### Java

```java
class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {

    }
}
```

### Python

```python
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
```

### Python3

```python3
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
```

### C

```c


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* relativeSortArray(int* arr1, int arr1Size, int* arr2, int arr2Size, int* returnSize){

}
```

### C#

```csharp
public class Solution {
    public int[] RelativeSortArray(int[] arr1, int[] arr2) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function(arr1, arr2) {

};
```

### TypeScript

```typescript
function relativeSortArray(arr1: number[], arr2: number[]): number[] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer[]
     */
    function relativeSortArray($arr1, $arr2) {

    }
}
```

### Swift

```swift
class Solution {
    func relativeSortArray(_ arr1: [Int], _ arr2: [Int]) -> [Int] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun relativeSortArray(arr1: IntArray, arr2: IntArray): IntArray {

    }
}
```

### Go

```golang
func relativeSortArray(arr1 []int, arr2 []int) []int {

}
```

### Ruby

```ruby
# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer[]}
def relative_sort_array(arr1, arr2)

end
```

### Scala

```scala
object Solution {
    def relativeSortArray(arr1: Array[Int], arr2: Array[Int]): Array[Int] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn relative_sort_array(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {

    }
}
```

### Racket

```racket
(define/contract (relative-sort-array arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))

  )
```

### Erlang

```erlang
-spec relative_sort_array(Arr1 :: [integer()], Arr2 :: [integer()]) -> [integer()].
relative_sort_array(Arr1, Arr2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec relative_sort_array(arr1 :: [integer], arr2 :: [integer]) :: [integer]
  def relative_sort_array(arr1, arr2) do

  end
end
```

