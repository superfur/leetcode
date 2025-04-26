# 1997. 访问完所有房间的第一天

## 题目描述

<p>你需要访问&nbsp;<code>n</code> 个房间，房间从 <code>0</code> 到 <code>n - 1</code> 编号。同时，每一天都有一个日期编号，从 <code>0</code> 开始，依天数递增。你每天都会访问一个房间。</p>

<p>最开始的第 <code>0</code> 天，你访问&nbsp;<code>0</code> 号房间。给你一个长度为 <code>n</code> 且 <strong>下标从 0 开始</strong> 的数组 <code>nextVisit</code> 。在接下来的几天中，你访问房间的 <strong>次序</strong> 将根据下面的 <strong>规则</strong> 决定：</p>

<ul>
	<li>假设某一天，你访问&nbsp;<code>i</code> 号房间。</li>
	<li>如果算上本次访问，访问&nbsp;<code>i</code> 号房间的次数为 <strong>奇数</strong> ，那么 <strong>第二天</strong> 需要访问&nbsp;<code>nextVisit[i]</code> 所指定的房间，其中 <code>0 &lt;= nextVisit[i] &lt;= i</code> 。</li>
	<li>如果算上本次访问，访问&nbsp;<code>i</code> 号房间的次数为 <strong>偶数</strong> ，那么 <strong>第二天</strong> 需要访问&nbsp;<code>(i + 1) mod n</code> 号房间。</li>
</ul>

<p>请返回你访问完所有房间的第一天的日期编号。题目数据保证总是存在这样的一天。由于答案可能很大，返回对 <code>10<sup>9</sup> + 7</code> 取余后的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nextVisit = [0,0]
<strong>输出：</strong>2
<strong>解释：</strong>
- 第 0 天，你访问房间 0 。访问 0 号房间的总次数为 1 ，次数为奇数。
&nbsp; 下一天你需要访问房间的编号是 nextVisit[0] = 0
- 第 1 天，你访问房间 0 。访问 0 号房间的总次数为 2 ，次数为偶数。
&nbsp; 下一天你需要访问房间的编号是 (0 + 1) mod 2 = 1
- 第 2 天，你访问房间 1 。这是你第一次完成访问所有房间的那天。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nextVisit = [0,0,2]
<strong>输出：</strong>6
<strong>解释：</strong>
你每天访问房间的次序是 [0,0,1,0,0,1,2,...] 。
第 6 天是你访问完所有房间的第一天。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nextVisit = [0,1,2,0]
<strong>输出：</strong>6
<strong>解释：</strong>
你每天访问房间的次序是 [0,0,1,1,2,2,3,...] 。
第 6 天是你访问完所有房间的第一天。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nextVisit.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nextVisit[i] &lt;= i</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. The only way to get to room i+1 is when you are visiting room i and room i has been visited an even number of times.
2. After visiting room i an odd number of times, you are required to visit room nextVisit[i] where nextVisit[i] <= i. It takes a fixed amount of days for you to come back from room nextVisit[i] to room i. Then, you have visited room i even number of times.nextVisit[i]
3. Can you use Dynamic Programming to avoid recomputing the number of days it takes to visit room i from room nextVisit[i]?

## 示例

```
[0,0]
[0,0,2]
[0,1,2,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int firstDayBeenInAllRooms(vector<int>& nextVisit) {
        
    }
};
```

### Java

```java
class Solution {
    public int firstDayBeenInAllRooms(int[] nextVisit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        """
        :type nextVisit: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        
```

### C

```c
int firstDayBeenInAllRooms(int* nextVisit, int nextVisitSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FirstDayBeenInAllRooms(int[] nextVisit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nextVisit
 * @return {number}
 */
var firstDayBeenInAllRooms = function(nextVisit) {
    
};
```

### TypeScript

```typescript
function firstDayBeenInAllRooms(nextVisit: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nextVisit
     * @return Integer
     */
    function firstDayBeenInAllRooms($nextVisit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func firstDayBeenInAllRooms(_ nextVisit: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun firstDayBeenInAllRooms(nextVisit: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int firstDayBeenInAllRooms(List<int> nextVisit) {
    
  }
}
```

### Go

```golang
func firstDayBeenInAllRooms(nextVisit []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} next_visit
# @return {Integer}
def first_day_been_in_all_rooms(next_visit)
    
end
```

### Scala

```scala
object Solution {
    def firstDayBeenInAllRooms(nextVisit: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn first_day_been_in_all_rooms(next_visit: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (first-day-been-in-all-rooms nextVisit)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec first_day_been_in_all_rooms(NextVisit :: [integer()]) -> integer().
first_day_been_in_all_rooms(NextVisit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec first_day_been_in_all_rooms(next_visit :: [integer]) :: integer
  def first_day_been_in_all_rooms(next_visit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func firstDayBeenInAllRooms(nextVisit: Array<Int64>): Int64 {

    }
}
```

