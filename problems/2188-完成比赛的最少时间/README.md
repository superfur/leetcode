# 2188. 完成比赛的最少时间

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>tires</code>&nbsp;，其中&nbsp;<code>tires[i] = [f<sub>i</sub>, r<sub>i</sub>]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;种轮胎如果连续使用，第&nbsp;<code>x</code>&nbsp;圈需要耗时&nbsp;<code>f<sub>i</sub> * r<sub>i</sub><sup>(x-1)</sup></code>&nbsp;秒。</p>

<ul>
	<li>比方说，如果&nbsp;<code>f<sub>i</sub> = 3</code>&nbsp;且&nbsp;<code>r<sub>i</sub> = 2</code>&nbsp;，且一直使用这种类型的同一条轮胎，那么该轮胎完成第&nbsp;<code>1</code>&nbsp;圈赛道耗时 <code>3</code>&nbsp;秒，完成第 <code>2</code>&nbsp;圈耗时&nbsp;<code>3 * 2 = 6</code>&nbsp;秒，完成第 <code>3</code>&nbsp;圈耗时&nbsp;<code>3 * 2<sup>2</sup> = 12</code>&nbsp;秒，依次类推。</li>
</ul>

<p>同时给你一个整数&nbsp;<code>changeTime</code>&nbsp;和一个整数&nbsp;<code>numLaps</code>&nbsp;。</p>

<p>比赛总共包含&nbsp;<code>numLaps</code>&nbsp;圈，你可以选择 <strong>任意</strong>&nbsp;一种轮胎开始比赛。每一种轮胎都有 <strong>无数条</strong>&nbsp;。每一圈后，你可以选择耗费 <code>changeTime</code>&nbsp;秒 <strong>换成</strong>&nbsp;任意一种轮胎（也可以换成当前种类的新轮胎）。</p>

<p>请你返回完成比赛需要耗费的 <strong>最少</strong>&nbsp;时间。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>tires = [[2,3],[3,4]], changeTime = 5, numLaps = 4
<b>输出：</b>21
<b>解释：</b>
第 1 圈：使用轮胎 0 ，耗时 2 秒。
第 2 圈：继续使用轮胎 0 ，耗时 2 * 3 = 6 秒。
第 3 圈：耗费 5 秒换一条新的轮胎 0 ，然后耗时 2 秒完成这一圈。
第 4 圈：继续使用轮胎 0 ，耗时 2 * 3 = 6 秒。
总耗时 = 2 + 6 + 5 + 2 + 6 = 21 秒。
完成比赛的最少时间为 21 秒。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>tires = [[1,10],[2,2],[3,4]], changeTime = 6, numLaps = 5
<b>输出：</b>25
<b>解释：</b>
第 1 圈：使用轮胎 1 ，耗时 2 秒。
第 2 圈：继续使用轮胎 1 ，耗时 2 * 2 = 4 秒。
第 3 圈：耗时 6 秒换一条新的轮胎 1 ，然后耗时 2 秒完成这一圈。
第 4 圈：继续使用轮胎 1 ，耗时 2 * 2 = 4 秒。
第 5 圈：耗时 6 秒换成轮胎 0 ，然后耗时 1 秒完成这一圈。
总耗时 = 2 + 4 + 6 + 2 + 4 + 6 + 1 = 25 秒。
完成比赛的最少时间为 25 秒。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= tires.length &lt;= 10<sup>5</sup></code></li>
	<li><code>tires[i].length == 2</code></li>
	<li><code>1 &lt;= f<sub>i</sub>, changeTime &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= r<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= numLaps &lt;= 1000</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. What is the maximum number of times we would want to go around the track without changing tires?
2. Can we precompute the minimum time to go around the track x times without changing tires?
3. Can we use dynamic programming to solve this efficiently using the precomputed values?

## 示例

```
[[2,3],[3,4]]
5
4
[[1,10],[2,2],[3,4]]
6
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumFinishTime(vector<vector<int>>& tires, int changeTime, int numLaps) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumFinishTime(int[][] tires, int changeTime, int numLaps) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumFinishTime(self, tires, changeTime, numLaps):
        """
        :type tires: List[List[int]]
        :type changeTime: int
        :type numLaps: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        
```

### C

```c
int minimumFinishTime(int** tires, int tiresSize, int* tiresColSize, int changeTime, int numLaps) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumFinishTime(int[][] tires, int changeTime, int numLaps) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} tires
 * @param {number} changeTime
 * @param {number} numLaps
 * @return {number}
 */
var minimumFinishTime = function(tires, changeTime, numLaps) {
    
};
```

### TypeScript

```typescript
function minimumFinishTime(tires: number[][], changeTime: number, numLaps: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $tires
     * @param Integer $changeTime
     * @param Integer $numLaps
     * @return Integer
     */
    function minimumFinishTime($tires, $changeTime, $numLaps) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumFinishTime(_ tires: [[Int]], _ changeTime: Int, _ numLaps: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumFinishTime(tires: Array<IntArray>, changeTime: Int, numLaps: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumFinishTime(List<List<int>> tires, int changeTime, int numLaps) {
    
  }
}
```

### Go

```golang
func minimumFinishTime(tires [][]int, changeTime int, numLaps int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} tires
# @param {Integer} change_time
# @param {Integer} num_laps
# @return {Integer}
def minimum_finish_time(tires, change_time, num_laps)
    
end
```

### Scala

```scala
object Solution {
    def minimumFinishTime(tires: Array[Array[Int]], changeTime: Int, numLaps: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_finish_time(tires: Vec<Vec<i32>>, change_time: i32, num_laps: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-finish-time tires changeTime numLaps)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_finish_time(Tires :: [[integer()]], ChangeTime :: integer(), NumLaps :: integer()) -> integer().
minimum_finish_time(Tires, ChangeTime, NumLaps) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_finish_time(tires :: [[integer]], change_time :: integer, num_laps :: integer) :: integer
  def minimum_finish_time(tires, change_time, num_laps) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumFinishTime(tires: Array<Array<Int64>>, changeTime: Int64, numLaps: Int64): Int64 {

    }
}
```

