# 1478. 安排邮筒

## 题目描述

<p>给你一个房屋数组<code>houses</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;，其中&nbsp;<code>houses[i]</code>&nbsp;是第 <code>i</code>&nbsp;栋房子在一条街上的位置，现需要在这条街上安排 <code>k</code>&nbsp;个邮筒。</p>

<p>请你返回每栋房子与离它最近的邮筒之间的距离的 <strong>最小 </strong>总和。</p>

<p>答案保证在 32 位有符号整数范围以内。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/13/sample_11_1816.png" style="height: 154px; width: 454px;"></p>

<pre><strong>输入：</strong>houses = [1,4,8,10,20], k = 3
<strong>输出：</strong>5
<strong>解释：</strong>将邮筒分别安放在位置 3， 9 和 20 处。
每个房子到最近邮筒的距离和为 |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/13/sample_2_1816.png" style="height: 154px; width: 433px;"></strong></p>

<pre><strong>输入：</strong>houses = [2,3,5,12,18], k = 2
<strong>输出：</strong>9
<strong>解释：</strong>将邮筒分别安放在位置 3 和 14 处。
每个房子到最近邮筒距离和为 |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>houses = [7,4,6,1], k = 1
<strong>输出：</strong>8
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>houses = [3,6,14,10], k = 4
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == houses.length</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 100</code></li>
	<li><code>1 &lt;= houses[i] &lt;= 10^4</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
	<li>数组&nbsp;<code>houses</code>&nbsp;中的整数互不相同。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 动态规划
- 排序

## 提示

1. If k =1, the minimum distance is obtained allocating the mailbox in the median of the array houses.
2. Generalize this idea, using dynamic programming allocating k mailboxes.

## 示例

```
[1,4,8,10,20]
3
[2,3,5,12,18]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minDistance(vector<int>& houses, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minDistance(int[] houses, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minDistance(self, houses, k):
        """
        :type houses: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        
```

### C

```c
int minDistance(int* houses, int housesSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinDistance(int[] houses, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} houses
 * @param {number} k
 * @return {number}
 */
var minDistance = function(houses, k) {
    
};
```

### TypeScript

```typescript
function minDistance(houses: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $houses
     * @param Integer $k
     * @return Integer
     */
    function minDistance($houses, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minDistance(_ houses: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minDistance(houses: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minDistance(List<int> houses, int k) {
    
  }
}
```

### Go

```golang
func minDistance(houses []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} houses
# @param {Integer} k
# @return {Integer}
def min_distance(houses, k)
    
end
```

### Scala

```scala
object Solution {
    def minDistance(houses: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_distance(houses: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-distance houses k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_distance(Houses :: [integer()], K :: integer()) -> integer().
min_distance(Houses, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_distance(houses :: [integer], k :: integer) :: integer
  def min_distance(houses, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minDistance(houses: Array<Int64>, k: Int64): Int64 {

    }
}
```

