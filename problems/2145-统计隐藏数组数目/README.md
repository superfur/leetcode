# 2145. 统计隐藏数组数目

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始且长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>differences</code>&nbsp;，它表示一个长度为&nbsp;<code>n + 1</code>&nbsp;的&nbsp;<strong>隐藏</strong>&nbsp;数组&nbsp;<strong>相邻</strong>&nbsp;元素之间的&nbsp;<strong>差值</strong>&nbsp;。更正式的表述为：我们将隐藏数组记作&nbsp;<code>hidden</code>&nbsp;，那么&nbsp;<code>differences[i] = hidden[i + 1] - hidden[i]</code>&nbsp;。</p>

<p>同时给你两个整数&nbsp;<code>lower</code> 和&nbsp;<code>upper</code>&nbsp;，它们表示隐藏数组中所有数字的值都在 <strong>闭</strong>&nbsp;区间&nbsp;<code>[lower, upper]</code>&nbsp;之间。</p>

<ul>
	<li>比方说，<code>differences = [1, -3, 4]</code>&nbsp;，<code>lower = 1</code>&nbsp;，<code>upper = 6</code>&nbsp;，那么隐藏数组是一个长度为 <code>4</code>&nbsp;且所有值都在&nbsp;<code>1</code>&nbsp;和&nbsp;<code>6</code>&nbsp;（包含两者）之间的数组。

	<ul>
		<li><code>[3, 4, 1, 5]</code> 和&nbsp;<code>[4, 5, 2, 6]</code>&nbsp;都是符合要求的隐藏数组。</li>
		<li><code>[5, 6, 3, 7]</code>&nbsp;不符合要求，因为它包含大于 <code>6</code>&nbsp;的元素。</li>
		<li><code>[1, 2, 3, 4]</code>&nbsp;不符合要求，因为相邻元素的差值不符合给定数据。</li>
	</ul>
	</li>
</ul>

<p>请你返回 <strong>符合</strong>&nbsp;要求的隐藏数组的数目。如果没有符合要求的隐藏数组，请返回 <code>0</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>differences = [1,-3,4], lower = 1, upper = 6
<b>输出：</b>2
<b>解释：</b>符合要求的隐藏数组为：
- [3, 4, 1, 5]
- [4, 5, 2, 6]
所以返回 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>differences = [3,-4,5,1,-2], lower = -4, upper = 5
<b>输出：</b>4
<b>解释：</b>符合要求的隐藏数组为：
- [-3, 0, -4, 1, 2, 0]
- [-2, 1, -3, 2, 3, 1]
- [-1, 2, -2, 3, 4, 2]
- [0, 3, -1, 4, 5, 3]
所以返回 4 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>differences = [4,-7,2], lower = 3, upper = 6
<b>输出：</b>0
<b>解释：</b>没有符合要求的隐藏数组，所以返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == differences.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= differences[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= lower &lt;= upper &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 前缀和

## 提示

1. Fix the first element of the hidden sequence to any value x and ignore the given bounds. Notice that we can then determine all the other elements of the sequence by using the differences array.
2. We will also be able to determine the difference between the minimum and maximum elements of the sequence. Notice that the value of x does not affect this.
3. We now have the ‘range’ of the sequence (difference between min and max element), we can then calculate how many ways there are to fit this range into the given range of lower to upper.
4. Answer is (upper - lower + 1) - (range of sequence)

## 示例

```
[1,-3,4]
1
6
[3,-4,5,1,-2]
-4
5
[4,-7,2]
3
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfArrays(int[] differences, int lower, int upper) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
```

### C

```c
int numberOfArrays(int* differences, int differencesSize, int lower, int upper) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfArrays(int[] differences, int lower, int upper) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} differences
 * @param {number} lower
 * @param {number} upper
 * @return {number}
 */
var numberOfArrays = function(differences, lower, upper) {
    
};
```

### TypeScript

```typescript
function numberOfArrays(differences: number[], lower: number, upper: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $differences
     * @param Integer $lower
     * @param Integer $upper
     * @return Integer
     */
    function numberOfArrays($differences, $lower, $upper) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfArrays(_ differences: [Int], _ lower: Int, _ upper: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfArrays(differences: IntArray, lower: Int, upper: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfArrays(List<int> differences, int lower, int upper) {
    
  }
}
```

### Go

```golang
func numberOfArrays(differences []int, lower int, upper int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} differences
# @param {Integer} lower
# @param {Integer} upper
# @return {Integer}
def number_of_arrays(differences, lower, upper)
    
end
```

### Scala

```scala
object Solution {
    def numberOfArrays(differences: Array[Int], lower: Int, upper: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_arrays(differences: Vec<i32>, lower: i32, upper: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-arrays differences lower upper)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_arrays(Differences :: [integer()], Lower :: integer(), Upper :: integer()) -> integer().
number_of_arrays(Differences, Lower, Upper) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_arrays(differences :: [integer], lower :: integer, upper :: integer) :: integer
  def number_of_arrays(differences, lower, upper) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfArrays(differences: Array<Int64>, lower: Int64, upper: Int64): Int64 {

    }
}
```

