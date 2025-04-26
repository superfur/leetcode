# 2111. 使数组 K 递增的最少操作次数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始包含 <code>n</code>&nbsp;个正整数的数组&nbsp;<code>arr</code>&nbsp;，和一个正整数&nbsp;<code>k</code>&nbsp;。</p>

<p>如果对于每个满足&nbsp;<code>k &lt;= i &lt;= n-1</code>&nbsp;的下标&nbsp;<code>i</code>&nbsp;，都有&nbsp;<code>arr[i-k] &lt;= arr[i]</code>&nbsp;，那么我们称&nbsp;<code>arr</code>&nbsp;是 <strong>K</strong>&nbsp;<strong>递增</strong> 的。</p>

<ul>
	<li>比方说，<code>arr = [4, 1, 5, 2, 6, 2]</code>&nbsp;对于&nbsp;<code>k = 2</code>&nbsp;是 K 递增的，因为：

	<ul>
		<li><code>arr[0] &lt;= arr[2] (4 &lt;= 5)</code></li>
		<li><code>arr[1] &lt;= arr[3] (1 &lt;= 2)</code></li>
		<li><code>arr[2] &lt;= arr[4] (5 &lt;= 6)</code></li>
		<li><code>arr[3] &lt;= arr[5] (2 &lt;= 2)</code></li>
	</ul>
	</li>
	<li>但是，相同的数组&nbsp;<code>arr</code>&nbsp;对于&nbsp;<code>k = 1</code>&nbsp;不是 K 递增的（因为&nbsp;<code>arr[0] &gt; arr[1]</code>），对于&nbsp;<code>k = 3</code>&nbsp;也不是 K 递增的（因为&nbsp;<code>arr[0] &gt; arr[3]</code>&nbsp;）。</li>
</ul>

<p>每一次 <strong>操作</strong>&nbsp;中，你可以选择一个下标&nbsp;<code>i</code> 并将&nbsp;<code>arr[i]</code> <strong>改成任意&nbsp;</strong>正整数。</p>

<p>请你返回对于给定的 <code>k</code>&nbsp;，使数组变成 K 递增的 <strong>最少操作次数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>arr = [5,4,3,2,1], k = 1
<b>输出：</b>4
<strong>解释：
</strong>对于 k = 1 ，数组最终必须变成非递减的。
可行的 K 递增结果数组为 [5,<em><strong>6</strong></em>,<em><strong>7</strong></em>,<em><strong>8</strong></em>,<em><strong>9</strong></em>]，[<em><strong>1</strong></em>,<em><strong>1</strong></em>,<em><strong>1</strong></em>,<em><strong>1</strong></em>,1]，[<em><strong>2</strong></em>,<em><strong>2</strong></em>,3,<em><strong>4</strong></em>,<em><strong>4</strong></em>] 。它们都需要 4 次操作。
次优解是将数组变成比方说 [<em><strong>6</strong></em>,<em><strong>7</strong></em>,<em><strong>8</strong></em>,<em><strong>9</strong></em>,<em><strong>10</strong></em>] ，因为需要 5 次操作。
显然我们无法使用少于 4 次操作将数组变成 K 递增的。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>arr = [4,1,5,2,6,2], k = 2
<b>输出：</b>0
<strong>解释：</strong>
这是题目描述中的例子。
对于每个满足 2 &lt;= i &lt;= 5 的下标 i ，有 arr[i-2] &lt;=<b> </b>arr[i] 。
由于给定数组已经是 K 递增的，我们不需要进行任何操作。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [4,1,5,2,6,2], k = 3
<b>输出：</b>2
<strong>解释：</strong>
下标 3 和 5 是仅有的 3 &lt;= i &lt;= 5 且不满足 arr[i-3] &lt;= arr[i] 的下标。
将数组变成 K 递增的方法之一是将 arr[3] 变为 4 ，且将 arr[5] 变成 5 。
数组变为 [4,1,5,<em><strong>4</strong></em>,6,<em><strong>5</strong></em>] 。
可能有其他方法将数组变为 K 递增的，但没有任何一种方法需要的操作次数小于 2 次。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i], k &lt;= arr.length</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 二分查找

## 提示

1. Can we divide the array into non-overlapping subsequences and simplify the problem?
2. In the final array, arr[i-k] ≤ arr[i] should hold. We can use this to divide the array into at most k non-overlapping sequences, where arr[i] will belong to the (i%k)th sequence.
3. Now our problem boils down to performing the minimum operations on each sequence such that it becomes non-decreasing. Our answer will be the sum of operations on each sequence.
4. Which indices of a sequence should we not change in order to count the minimum operations? Can finding the longest non-decreasing subsequence of the sequence help?

## 示例

```
[5,4,3,2,1]
1
[4,1,5,2,6,2]
2
[4,1,5,2,6,2]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int kIncreasing(vector<int>& arr, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int kIncreasing(int[] arr, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kIncreasing(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        
```

### C

```c
int kIncreasing(int* arr, int arrSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int KIncreasing(int[] arr, int k) {
        
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
var kIncreasing = function(arr, k) {
    
};
```

### TypeScript

```typescript
function kIncreasing(arr: number[], k: number): number {
    
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
    function kIncreasing($arr, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kIncreasing(_ arr: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kIncreasing(arr: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int kIncreasing(List<int> arr, int k) {
    
  }
}
```

### Go

```golang
func kIncreasing(arr []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def k_increasing(arr, k)
    
end
```

### Scala

```scala
object Solution {
    def kIncreasing(arr: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn k_increasing(arr: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (k-increasing arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec k_increasing(Arr :: [integer()], K :: integer()) -> integer().
k_increasing(Arr, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec k_increasing(arr :: [integer], k :: integer) :: integer
  def k_increasing(arr, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kIncreasing(arr: Array<Int64>, k: Int64): Int64 {

    }
}
```

