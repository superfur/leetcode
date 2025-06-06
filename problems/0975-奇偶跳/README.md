# 975. 奇偶跳

## 题目描述

<p>给定一个整数数组 <code>arr</code>，你可以从某一起始索引出发，跳跃一定次数。在你跳跃的过程中，第 1、3、5... 次跳跃称为奇数跳跃，而第 2、4、6... 次跳跃称为偶数跳跃。</p>

<p>你可以按以下方式从索引 <code>i</code>&nbsp;向后跳转到索引 <code>j</code>（其中 <code>i &lt; j</code>）：</p>

<ul>
	<li>在进行奇数跳跃时（如，第&nbsp;1，3，5... 次跳跃），你将会跳到索引 <code>j</code>，使得 <code>arr[i] &lt;=&nbsp;arr[j]</code>，且 <code>arr[j]</code> 的值尽可能小。如果存在多个这样的索引 <code>j</code>，你只能跳到满足要求的<strong>最小</strong>索引 <code>j</code> 上。</li>
	<li>在进行偶数跳跃时（如，第&nbsp;2，4，6... 次跳跃），你将会跳到索引&nbsp;<code>j</code>，使得 <code>arr[i] &gt;= arr[j]</code>，且 <code>arr[j]</code> 的值尽可能大。如果存在多个这样的索引 <code>j</code>，你只能跳到满足要求的<strong>最小</strong>索引 <code>j</code>&nbsp;上。</li>
	<li>（对于某些索引 <code>i</code>，可能无法进行合乎要求的跳跃。）</li>
</ul>

<p>如果从某一索引开始跳跃一定次数（可能是 0 次或多次），就可以到达数组的末尾（索引 <code>arr.length - 1</code>），那么该索引就会被认为是好的起始索引。</p>

<p>返回好的起始索引的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>[10,13,12,14,15]
<strong>输出：</strong>2
<strong>解释： </strong>
从起始索引 i = 0 出发，我们可以跳到 i = 2，（因为 arr[2] 是 arr[1]，arr[2]，arr[3]，arr[4] 中大于或等于 arr[0] 的最小值），然后我们就无法继续跳下去了。
从起始索引 i = 1 和 i = 2 出发，我们可以跳到 i = 3，然后我们就无法继续跳下去了。
从起始索引 i = 3 出发，我们可以跳到 i = 4，到达数组末尾。
从起始索引 i = 4 出发，我们已经到达数组末尾。
总之，我们可以从 2 个不同的起始索引（i = 3, i = 4）出发，通过一定数量的跳跃到达数组末尾。
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>[2,3,1,1,4]
<strong>输出：</strong>3
<strong>解释：</strong>
从起始索引 i=0 出发，我们依次可以跳到 i = 1，i = 2，i = 3：

在我们的第一次跳跃（奇数）中，我们先跳到 i = 1，因为 arr[1] 是（arr[1]，arr[2]，arr[3]，arr[4]）中大于或等于 arr[0] 的最小值。

在我们的第二次跳跃（偶数）中，我们从 i = 1 跳到 i = 2，因为 arr[2] 是（arr[2]，arr[3]，arr[4]）中小于或等于 arr[1] 的最大值。arr[3] 也是最大的值，但 2 是一个较小的索引，所以我们只能跳到 i = 2，而不能跳到 i = 3。

在我们的第三次跳跃（奇数）中，我们从 i = 2 跳到 i = 3，因为 arr[3] 是（arr[3]，arr[4]）中大于或等于 arr[2] 的最小值。

我们不能从 i = 3 跳到 i = 4，所以起始索引 i = 0 不是好的起始索引。

类似地，我们可以推断：
从起始索引 i = 1 出发， 我们跳到 i = 4，这样我们就到达数组末尾。
从起始索引 i = 2 出发， 我们跳到 i = 3，然后我们就不能再跳了。
从起始索引 i = 3 出发， 我们跳到 i = 4，这样我们就到达数组末尾。
从起始索引 i = 4 出发，我们已经到达数组末尾。
总之，我们可以从 3 个不同的起始索引（i = 1, i = 3, i = 4）出发，通过一定数量的跳跃到达数组末尾。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>[5,1,3,4,2]
<strong>输出：</strong>3
<strong>解释： </strong>
我们可以从起始索引 1，2，4 出发到达数组末尾。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= arr.length &lt;= 20000</code></li>
	<li><code>0 &lt;= arr[i] &lt; 100000</code></li>
</ol>


## 难度

Hard

## 标签

- 栈
- 数组
- 动态规划
- 有序集合
- 单调栈

## 示例

```
[10,13,12,14,15]
[2,3,1,1,4]
[5,1,3,4,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int oddEvenJumps(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int oddEvenJumps(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        
```

### C

```c
int oddEvenJumps(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int OddEvenJumps(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var oddEvenJumps = function(arr) {
    
};
```

### TypeScript

```typescript
function oddEvenJumps(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function oddEvenJumps($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func oddEvenJumps(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun oddEvenJumps(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int oddEvenJumps(List<int> arr) {
    
  }
}
```

### Go

```golang
func oddEvenJumps(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def odd_even_jumps(arr)
    
end
```

### Scala

```scala
object Solution {
    def oddEvenJumps(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn odd_even_jumps(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (odd-even-jumps arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec odd_even_jumps(Arr :: [integer()]) -> integer().
odd_even_jumps(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec odd_even_jumps(arr :: [integer]) :: integer
  def odd_even_jumps(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func oddEvenJumps(arr: Array<Int64>): Int64 {

    }
}
```

