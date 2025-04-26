# 1423. 可获得的最大点数

## 题目描述

<p>几张卡牌<strong> 排成一行</strong>，每张卡牌都有一个对应的点数。点数由整数数组 <code>cardPoints</code> 给出。</p>

<p>每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 <code>k</code> 张卡牌。</p>

<p>你的点数就是你拿到手中的所有卡牌的点数之和。</p>

<p>给你一个整数数组 <code>cardPoints</code> 和整数 <code>k</code>，请你返回可以获得的最大点数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>cardPoints = [1,2,3,4,5,6,1], k = 3
<strong>输出：</strong>12
<strong>解释：</strong>第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>cardPoints = [2,2,2], k = 2
<strong>输出：</strong>4
<strong>解释：</strong>无论你拿起哪两张卡牌，可获得的点数总是 4 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>cardPoints = [9,7,7,9,7,7,9], k = 7
<strong>输出：</strong>55
<strong>解释：</strong>你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>cardPoints = [1,1000,1], k = 1
<strong>输出：</strong>1
<strong>解释：</strong>你无法拿到中间那张卡牌，所以可以获得的最大点数为 1 。 
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>cardPoints = [1,79,80,1,1,1,200,1], k = 3
<strong>输出：</strong>202
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= cardPoints.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= cardPoints[i] &lt;= 10^4</code></li>
	<li><code>1 &lt;= k &lt;= cardPoints.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 前缀和
- 滑动窗口

## 提示

1. Let the sum of all points be total_pts. You need to remove a sub-array from cardPoints with length n - k.
2. Keep a window of size n - k over the array. The answer is max(answer, total_pts - sumOfCurrentWindow)

## 示例

```
[1,2,3,4,5,6,1]
3
[2,2,2]
2
[9,7,7,9,7,7,9]
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxScore(int[] cardPoints, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
```

### C

```c
int maxScore(int* cardPoints, int cardPointsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxScore(int[] cardPoints, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} cardPoints
 * @param {number} k
 * @return {number}
 */
var maxScore = function(cardPoints, k) {
    
};
```

### TypeScript

```typescript
function maxScore(cardPoints: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $cardPoints
     * @param Integer $k
     * @return Integer
     */
    function maxScore($cardPoints, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxScore(_ cardPoints: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxScore(cardPoints: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxScore(List<int> cardPoints, int k) {
    
  }
}
```

### Go

```golang
func maxScore(cardPoints []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} card_points
# @param {Integer} k
# @return {Integer}
def max_score(card_points, k)
    
end
```

### Scala

```scala
object Solution {
    def maxScore(cardPoints: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_score(card_points: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-score cardPoints k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_score(CardPoints :: [integer()], K :: integer()) -> integer().
max_score(CardPoints, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_score(card_points :: [integer], k :: integer) :: integer
  def max_score(card_points, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxScore(cardPoints: Array<Int64>, k: Int64): Int64 {

    }
}
```

