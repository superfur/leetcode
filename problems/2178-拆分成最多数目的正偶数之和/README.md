# 2178. 拆分成最多数目的正偶数之和

## 题目描述

<p>给你一个整数&nbsp;<code>finalSum</code>&nbsp;。请你将它拆分成若干个&nbsp;<strong>互不相同</strong> 的正偶数之和，且拆分出来的正偶数数目&nbsp;<strong>最多</strong>&nbsp;。</p>

<ul>
	<li>比方说，给你&nbsp;<code>finalSum = 12</code>&nbsp;，那么这些拆分是&nbsp;<strong>符合要求</strong> 的（互不相同的正偶数且和为&nbsp;<code>finalSum</code>）：<code>(2 + 10)</code>&nbsp;，<code>(2 + 4 + 6)</code>&nbsp;和&nbsp;<code>(4 + 8)</code>&nbsp;。它们中，<code>(2 + 4 + 6)</code>&nbsp;包含最多数目的整数。注意&nbsp;<code>finalSum</code>&nbsp;不能拆分成&nbsp;<code>(2 + 2 + 4 + 4)</code>&nbsp;，因为拆分出来的整数必须互不相同。</li>
</ul>

<p>请你返回一个整数数组，表示将整数拆分成 <strong>最多</strong> 数目的正偶数数组。如果没有办法将&nbsp;<code>finalSum</code>&nbsp;进行拆分，请你返回一个&nbsp;<strong>空</strong>&nbsp;数组。你可以按 <b>任意</b>&nbsp;顺序返回这些整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>finalSum = 12
<b>输出：</b>[2,4,6]
<b>解释：</b>以下是一些符合要求的拆分：<code>(2 + 10)<span style="">，</span></code><code>(2 + 4 + 6) </code>和 <code>(4 + 8) 。</code>
(2 + 4 + 6) 为最多数目的整数，数目为 3 ，所以我们返回 [2,4,6] 。
[2,6,4] ，[6,2,4] 等等也都是可行的解。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>finalSum = 7
<b>输出：</b>[]
<b>解释：</b>没有办法将 finalSum 进行拆分。
所以返回空数组。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>finalSum = 28
<b>输出：</b>[6,8,2,12]
<b>解释：</b>以下是一些符合要求的拆分：<code>(2 + 26)<span style="">，</span></code><code>(6 + 8 + 2 + 12)</code> 和 <code>(4 + 24) 。</code>
<code>(6 + 8 + 2 + 12)</code> 有最多数目的整数，数目为 4 ，所以我们返回 [6,8,2,12] 。
[10,2,4,12] ，[6,2,4,16] 等等也都是可行的解。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= finalSum &lt;= 10<sup>10</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学
- 回溯

## 提示

1. First, check if finalSum is divisible by 2. If it isn’t, then we cannot split it into even integers.
2. Let k be the number of elements in our split. As we want the maximum number of elements, we should try to use the first k - 1 even elements to grow our sum as slowly as possible.
3. Thus, we find the maximum sum of the first k - 1 even elements which is less than finalSum.
4. We then add the difference over to the kth element.

## 示例

```
12
7
28
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<long long> maximumEvenSplit(long long finalSum) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Long> maximumEvenSplit(long finalSum) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumEvenSplit(self, finalSum):
        """
        :type finalSum: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* maximumEvenSplit(long long finalSum, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<long> MaximumEvenSplit(long finalSum) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} finalSum
 * @return {number[]}
 */
var maximumEvenSplit = function(finalSum) {
    
};
```

### TypeScript

```typescript
function maximumEvenSplit(finalSum: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $finalSum
     * @return Integer[]
     */
    function maximumEvenSplit($finalSum) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumEvenSplit(_ finalSum: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumEvenSplit(finalSum: Long): List<Long> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> maximumEvenSplit(int finalSum) {
    
  }
}
```

### Go

```golang
func maximumEvenSplit(finalSum int64) []int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} final_sum
# @return {Integer[]}
def maximum_even_split(final_sum)
    
end
```

### Scala

```scala
object Solution {
    def maximumEvenSplit(finalSum: Long): List[Long] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_even_split(final_sum: i64) -> Vec<i64> {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-even-split finalSum)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec maximum_even_split(FinalSum :: integer()) -> [integer()].
maximum_even_split(FinalSum) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_even_split(final_sum :: integer) :: [integer]
  def maximum_even_split(final_sum) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumEvenSplit(finalSum: Int64): ArrayList<Int64> {

    }
}
```

