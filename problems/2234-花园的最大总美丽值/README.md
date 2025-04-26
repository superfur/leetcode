# 2234. 花园的最大总美丽值

## 题目描述

<p>Alice 是&nbsp;<code>n</code>&nbsp;个花园的园丁，她想通过种花，最大化她所有花园的总美丽值。</p>

<p>给你一个下标从 <strong>0</strong>&nbsp;开始大小为 <code>n</code>&nbsp;的整数数组&nbsp;<code>flowers</code>&nbsp;，其中&nbsp;<code>flowers[i]</code>&nbsp;是第 <code>i</code>&nbsp;个花园里已经种的花的数目。已经种了的花 <strong>不能</strong>&nbsp;移走。同时给你&nbsp;<code>newFlowers</code>&nbsp;，表示 Alice 额外可以种花的&nbsp;<strong>最大数目</strong>&nbsp;。同时给你的还有整数&nbsp;<code>target</code>&nbsp;，<code>full</code>&nbsp;和&nbsp;<code>partial</code>&nbsp;。</p>

<p>如果一个花园有 <strong>至少</strong>&nbsp;<code>target</code>&nbsp;朵花，那么这个花园称为 <strong>完善的</strong>&nbsp;，花园的 <strong>总美丽值</strong>&nbsp;为以下分数之 <strong>和</strong> ：</p>

<ul>
	<li><b>完善</b> 花园数目乘以&nbsp;<code>full</code>.</li>
	<li>剩余 <strong>不完善</strong>&nbsp;花园里，花的 <strong>最少数目</strong>&nbsp;乘以&nbsp;<code>partial</code>&nbsp;。如果没有不完善花园，那么这一部分的值为&nbsp;<code>0</code>&nbsp;。</li>
</ul>

<p>请你返回 Alice 种最多 <code>newFlowers</code>&nbsp;朵花以后，能得到的<strong>&nbsp;最大</strong>&nbsp;总美丽值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1
<b>输出：</b>14
<b>解释：</b>Alice 可以按以下方案种花
- 在第 0 个花园种 2 朵花
- 在第 1 个花园种 3 朵花
- 在第 2 个花园种 1 朵花
- 在第 3 个花园种 1 朵花
花园里花的数目为 [3,6,2,2] 。总共种了 2 + 3 + 1 + 1 = 7 朵花。
只有 1 个花园是完善的。
不完善花园里花的最少数目是 2 。
所以总美丽值为 1 * 12 + 2 * 1 = 12 + 2 = 14 。
没有其他方案可以让花园总美丽值超过 14 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6
<b>输出：</b>30
<b>解释：</b>Alice 可以按以下方案种花
- 在第 0 个花园种 3 朵花
- 在第 1 个花园种 0 朵花
- 在第 2 个花园种 0 朵花
- 在第 3 个花园种 2 朵花
花园里花的数目为 [5,4,5,5] 。总共种了 3 + 0 + 0 + 2 = 5 朵花。
有 3 个花园是完善的。
不完善花园里花的最少数目为 4 。
所以总美丽值为 3 * 2 + 4 * 6 = 6 + 24 = 30 。
没有其他方案可以让花园总美丽值超过 30 。
注意，Alice可以让所有花园都变成完善的，但这样她的总美丽值反而更小。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= flowers.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= flowers[i], target &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= newFlowers &lt;= 10<sup>10</sup></code></li>
	<li><code>1 &lt;= full, partial &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 双指针
- 二分查找
- 枚举
- 前缀和
- 排序

## 提示

1. Say we choose k gardens to be complete, is there an optimal way of choosing which gardens to plant more flowers to achieve this?
2. For a given k, we should greedily fill-up the k gardens with the most flowers planted already. This gives us the most remaining flowers to fill up the other gardens.
3. After sorting flowers, we can thus try every possible k and what is left is to find the highest minimum flowers we can obtain by planting the remaining flowers in the other gardens.
4. To find the highest minimum in the other gardens, we can use binary search to find the most optimal way of planting.

## 示例

```
[1,3,1,1]
7
6
12
1
[2,4,5,3]
10
5
2
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumBeauty(vector<int>& flowers, long long newFlowers, int target, int full, int partial) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumBeauty(int[] flowers, long newFlowers, int target, int full, int partial) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        """
        :type flowers: List[int]
        :type newFlowers: int
        :type target: int
        :type full: int
        :type partial: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        
```

### C

```c
long long maximumBeauty(int* flowers, int flowersSize, long long newFlowers, int target, int full, int partial) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumBeauty(int[] flowers, long newFlowers, int target, int full, int partial) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} flowers
 * @param {number} newFlowers
 * @param {number} target
 * @param {number} full
 * @param {number} partial
 * @return {number}
 */
var maximumBeauty = function(flowers, newFlowers, target, full, partial) {
    
};
```

### TypeScript

```typescript
function maximumBeauty(flowers: number[], newFlowers: number, target: number, full: number, partial: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $flowers
     * @param Integer $newFlowers
     * @param Integer $target
     * @param Integer $full
     * @param Integer $partial
     * @return Integer
     */
    function maximumBeauty($flowers, $newFlowers, $target, $full, $partial) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumBeauty(_ flowers: [Int], _ newFlowers: Int, _ target: Int, _ full: Int, _ partial: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumBeauty(flowers: IntArray, newFlowers: Long, target: Int, full: Int, partial: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumBeauty(List<int> flowers, int newFlowers, int target, int full, int partial) {
    
  }
}
```

### Go

```golang
func maximumBeauty(flowers []int, newFlowers int64, target int, full int, partial int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} flowers
# @param {Integer} new_flowers
# @param {Integer} target
# @param {Integer} full
# @param {Integer} partial
# @return {Integer}
def maximum_beauty(flowers, new_flowers, target, full, partial)
    
end
```

### Scala

```scala
object Solution {
    def maximumBeauty(flowers: Array[Int], newFlowers: Long, target: Int, full: Int, partial: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_beauty(flowers: Vec<i32>, new_flowers: i64, target: i32, full: i32, partial: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-beauty flowers newFlowers target full partial)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_beauty(Flowers :: [integer()], NewFlowers :: integer(), Target :: integer(), Full :: integer(), Partial :: integer()) -> integer().
maximum_beauty(Flowers, NewFlowers, Target, Full, Partial) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_beauty(flowers :: [integer], new_flowers :: integer, target :: integer, full :: integer, partial :: integer) :: integer
  def maximum_beauty(flowers, new_flowers, target, full, partial) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumBeauty(flowers: Array<Int64>, newFlowers: Int64, target: Int64, full: Int64, partial: Int64): Int64 {

    }
}
```

