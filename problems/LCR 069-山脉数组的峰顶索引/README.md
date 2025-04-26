# LCR 069. 山脉数组的峰顶索引

## 题目描述

<p>符合下列属性的数组 <code>arr</code> 称为 <strong>山峰数组</strong>（<strong>山脉数组）</strong> ：</p>

<ul>
	<li><code>arr.length &gt;= 3</code></li>
	<li>存在 <code>i</code>（<code>0 &lt; i&nbsp;&lt; arr.length - 1</code>）使得：
	<ul>
		<li><code>arr[0] &lt; arr[1] &lt; ... arr[i-1] &lt; arr[i] </code></li>
		<li><code>arr[i] &gt; arr[i+1] &gt; ... &gt; arr[arr.length - 1]</code></li>
	</ul>
	</li>
</ul>

<p>给定由整数组成的山峰数组 <code>arr</code> ，返回任何满足 <code>arr[0] &lt; arr[1] &lt; ... arr[i - 1] &lt; arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1]</code> 的下标 <code>i</code>&nbsp;，即山峰顶部。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [0,1,0]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,3,5,4,2]
<strong>输出：2</strong>
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [0,10,5,2]
<strong>输出：</strong>1
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>arr = [3,4,5,1]
<strong>输出：</strong>2
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>arr = [24,69,100,99,79,78,67,36,26,19]
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>6</sup></code></li>
	<li>题目数据保证 <code>arr</code> 是一个山脉数组</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>很容易想到时间复杂度 <code>O(n)</code> 的解决方案，你可以设计一个 <code>O(log(n))</code> 的解决方案吗？</p>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 852&nbsp;题相同：<a href="https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/">https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/</a></p>


## 难度

Easy

## 标签

- 数组
- 二分查找

## 示例

```
[0,1,0]
[0,2,1,0]
[0,10,5,2]
[3,4,5,1]
[24,69,100,99,79,78,67,36,26,19]
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


int peakIndexInMountainArray(int* arr, int arrSize){

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

