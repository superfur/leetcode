# 2554. 从一个范围内选择最多整数 I

## 题目描述

<p>给你一个整数数组&nbsp;<code>banned</code>&nbsp;和两个整数&nbsp;<code>n</code> 和&nbsp;<code>maxSum</code>&nbsp;。你需要按照以下规则选择一些整数：</p>

<ul>
	<li>被选择整数的范围是&nbsp;<code>[1, n]</code>&nbsp;。</li>
	<li>每个整数 <strong>至多</strong>&nbsp;选择 <strong>一次</strong>&nbsp;。</li>
	<li>被选择整数不能在数组&nbsp;<code>banned</code>&nbsp;中。</li>
	<li>被选择整数的和不超过&nbsp;<code>maxSum</code>&nbsp;。</li>
</ul>

<p>请你返回按照上述规则 <strong>最多</strong>&nbsp;可以选择的整数数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>banned = [1,6,5], n = 5, maxSum = 6
<b>输出：</b>2
<b>解释：</b>你可以选择整数 2 和 4 。
2 和 4 在范围 [1, 5] 内，且它们都不在 banned 中，它们的和是 6 ，没有超过 maxSum 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
<b>输出：</b>0
<b>解释：</b>按照上述规则无法选择任何整数。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>banned = [11], n = 7, maxSum = 50
<b>输出：</b>7
<b>解释：</b>你可以选择整数 1, 2, 3, 4, 5, 6 和 7 。
它们都在范围 [1, 7] 中，且都没出现在 banned 中，它们的和是 28 ，没有超过 maxSum 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= banned.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= banned[i], n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= maxSum &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 二分查找
- 排序

## 提示

1. Keep the banned numbers that are less than or equal to n in a set.
2. Loop over the numbers from 1 to n and if the number is not banned, use it.
3. Keep adding numbers while they are not banned, and their sum is less than or equal to k.

## 示例

```
[1,6,5]
5
6
[1,2,3,4,5,6,7]
8
1
[11]
7
50
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxCount(int[] banned, int n, int maxSum) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
```

### C

```c
int maxCount(int* banned, int bannedSize, int n, int maxSum) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxCount(int[] banned, int n, int maxSum) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} banned
 * @param {number} n
 * @param {number} maxSum
 * @return {number}
 */
var maxCount = function(banned, n, maxSum) {
    
};
```

### TypeScript

```typescript
function maxCount(banned: number[], n: number, maxSum: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $banned
     * @param Integer $n
     * @param Integer $maxSum
     * @return Integer
     */
    function maxCount($banned, $n, $maxSum) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxCount(_ banned: [Int], _ n: Int, _ maxSum: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxCount(banned: IntArray, n: Int, maxSum: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxCount(List<int> banned, int n, int maxSum) {
    
  }
}
```

### Go

```golang
func maxCount(banned []int, n int, maxSum int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} banned
# @param {Integer} n
# @param {Integer} max_sum
# @return {Integer}
def max_count(banned, n, max_sum)
    
end
```

### Scala

```scala
object Solution {
    def maxCount(banned: Array[Int], n: Int, maxSum: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_count(banned: Vec<i32>, n: i32, max_sum: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-count banned n maxSum)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_count(Banned :: [integer()], N :: integer(), MaxSum :: integer()) -> integer().
max_count(Banned, N, MaxSum) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_count(banned :: [integer], n :: integer, max_sum :: integer) :: integer
  def max_count(banned, n, max_sum) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxCount(banned: Array<Int64>, n: Int64, maxSum: Int64): Int64 {

    }
}
```

