# 2731. 移动机器人

## 题目描述

<p>有一些机器人分布在一条无限长的数轴上，他们初始坐标用一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;表示。当你给机器人下达命令时，它们以每秒钟一单位的速度开始移动。</p>

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;，每个字符按顺序分别表示每个机器人移动的方向。<code>'L'</code>&nbsp;表示机器人往左或者数轴的负方向移动，<code>'R'</code>&nbsp;表示机器人往右或者数轴的正方向移动。</p>

<p>当两个机器人相撞时，它们开始沿着原本相反的方向移动。</p>

<p>请你返回指令重复执行 <code>d</code>&nbsp;秒后，所有机器人之间两两距离之和。由于答案可能很大，请你将答案对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;取余后返回。</p>

<p><b>注意：</b></p>

<ul>
	<li>对于坐标在&nbsp;<code>i</code> 和&nbsp;<code>j</code>&nbsp;的两个机器人，<code>(i,j)</code>&nbsp;和&nbsp;<code>(j,i)</code>&nbsp;视为相同的坐标对。也就是说，机器人视为无差别的。</li>
	<li>当机器人相撞时，它们 <strong>立即改变</strong>&nbsp;它们的前进方向，这个过程不消耗任何时间。</li>
	<li>
	<p>当两个机器人在同一时刻占据相同的位置时，就会相撞。</p>

	<ul>
		<li>
		<p>例如，如果一个机器人位于位置 0 并往右移动，另一个机器人位于位置 2 并往左移动，下一秒，它们都将占据位置 1，并改变方向。再下一秒钟后，第一个机器人位于位置 0 并往左移动，而另一个机器人位于位置 2 并往右移动。</p>
		</li>
		<li>
		<p>例如，如果一个机器人位于位置 0 并往右移动，另一个机器人位于位置 1 并往左移动，下一秒，第一个机器人位于位置 0 并往左行驶，而另一个机器人位于位置 1 并往右移动。</p>
		</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [-2,0,2], s = "RLL", d = 3
<b>输出：</b>8
<b>解释：</b>
1 秒后，机器人的位置为 [-1,-1,1] 。现在下标为 0 的机器人开始往左移动，下标为 1 的机器人开始往右移动。
2 秒后，机器人的位置为 [-2,0,0] 。现在下标为 1 的机器人开始往左移动，下标为 2 的机器人开始往右移动。
3 秒后，机器人的位置为 [-3,-1,1] 。
下标为 0 和 1 的机器人之间距离为 abs(-3 - (-1)) = 2 。
下标为 0 和 2 的机器人之间的距离为 abs(-3 - 1) = 4 。
下标为 1 和 2 的机器人之间的距离为 abs(-1 - 1) = 2 。
所有机器人对之间的总距离为 2 + 4 + 2 = 8 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,0], s = "RL", d = 2
<b>输出：</b>5
<b>解释：</b>
1 秒后，机器人的位置为 [2,-1] 。
2 秒后，机器人的位置为 [3,-2] 。
两个机器人的距离为 abs(-2 - 3) = 5 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2 * 10<sup>9</sup>&nbsp;&lt;= nums[i] &lt;= 2 * 10<sup>9</sup></code></li>
	<li><code>0 &lt;= d &lt;= 10<sup>9</sup></code></li>
	<li><code>nums.length == s.length&nbsp;</code></li>
	<li><code>s</code>&nbsp;只包含&nbsp;<code>'L'</code> 和 <code>'R'</code>&nbsp;。</li>
	<li><code>nums[i]</code>&nbsp;互不相同。</li>
</ul>


## 难度

Medium

## 标签

- 脑筋急转弯
- 数组
- 前缀和
- 排序

## 提示

1. Observe that if you ignore collisions, the resultant positions of robots after d seconds would be the same.
2. After d seconds, sort the ending positions and use prefix sum to calculate the distance sum.

## 示例

```
[-2,0,2]
"RLL"
3
[1,0]
"RL"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumDistance(vector<int>& nums, string s, int d) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumDistance(int[] nums, String s, int d) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumDistance(self, nums, s, d):
        """
        :type nums: List[int]
        :type s: str
        :type d: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        
```

### C

```c
int sumDistance(int* nums, int numsSize, char* s, int d) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumDistance(int[] nums, string s, int d) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {string} s
 * @param {number} d
 * @return {number}
 */
var sumDistance = function(nums, s, d) {
    
};
```

### TypeScript

```typescript
function sumDistance(nums: number[], s: string, d: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param String $s
     * @param Integer $d
     * @return Integer
     */
    function sumDistance($nums, $s, $d) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumDistance(_ nums: [Int], _ s: String, _ d: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumDistance(nums: IntArray, s: String, d: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumDistance(List<int> nums, String s, int d) {
    
  }
}
```

### Go

```golang
func sumDistance(nums []int, s string, d int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {String} s
# @param {Integer} d
# @return {Integer}
def sum_distance(nums, s, d)
    
end
```

### Scala

```scala
object Solution {
    def sumDistance(nums: Array[Int], s: String, d: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_distance(nums: Vec<i32>, s: String, d: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-distance nums s d)
  (-> (listof exact-integer?) string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_distance(Nums :: [integer()], S :: unicode:unicode_binary(), D :: integer()) -> integer().
sum_distance(Nums, S, D) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_distance(nums :: [integer], s :: String.t, d :: integer) :: integer
  def sum_distance(nums, s, d) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumDistance(nums: Array<Int64>, s: String, d: Int64): Int64 {

    }
}
```

