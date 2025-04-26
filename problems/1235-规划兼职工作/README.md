# 1235. 规划兼职工作

## 题目描述

<p>你打算利用空闲时间来做兼职工作赚些零花钱。</p>

<p>这里有&nbsp;<code>n</code>&nbsp;份兼职工作，每份工作预计从&nbsp;<code>startTime[i]</code>&nbsp;开始到&nbsp;<code>endTime[i]</code>&nbsp;结束，报酬为&nbsp;<code>profit[i]</code>。</p>

<p>给你一份兼职工作表，包含开始时间&nbsp;<code>startTime</code>，结束时间&nbsp;<code>endTime</code>&nbsp;和预计报酬&nbsp;<code>profit</code>&nbsp;三个数组，请你计算并返回可以获得的最大报酬。</p>

<p>注意，时间上出现重叠的 2 份工作不能同时进行。</p>

<p>如果你选择的工作在时间&nbsp;<code>X</code>&nbsp;结束，那么你可以立刻进行在时间&nbsp;<code>X</code>&nbsp;开始的下一份工作。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/sample1_1584.png" style="width: 300px;" /></strong></p>

<pre>
<strong>输入：</strong>startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
<strong>输出：</strong>120
<strong>解释：
</strong>我们选出第 1 份和第 4 份工作， 
时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/sample22_1584.png" style="height: 112px; width: 600px;" /> </strong></p>

<pre>
<strong>输入：</strong>startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
<strong>输出：</strong>150
<strong>解释：
</strong>我们选择第 1，4，5 份工作。 
共获得报酬 150 = 20 + 70 + 60。
</pre>

<p><strong class="example">示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/sample3_1584.png" style="height: 112px; width: 400px;" /></strong></p>

<pre>
<strong>输入：</strong>startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
<strong>输出：</strong>6
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= startTime.length == endTime.length ==&nbsp;profit.length&nbsp;&lt;= 5 * 10^4</code></li>
	<li><code>1 &lt;=&nbsp;startTime[i] &lt;&nbsp;endTime[i] &lt;= 10^9</code></li>
	<li><code>1 &lt;=&nbsp;profit[i] &lt;= 10^4</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 二分查找
- 动态规划
- 排序

## 提示

1. Think on DP.
2. Sort the elements by starting time, then define the dp[i] as the maximum profit taking elements from the suffix starting at i.
3. Use binarySearch (lower_bound/upper_bound on C++) to get the next index for the DP transition.

## 示例

```
[1,2,3,3]
[3,4,5,6]
[50,10,40,70]
[1,2,3,4,6]
[3,5,10,6,9]
[20,20,100,70,60]
[1,1,1]
[2,3,4]
[5,6,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        
    }
};
```

### Java

```java
class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
```

### C

```c
int jobScheduling(int* startTime, int startTimeSize, int* endTime, int endTimeSize, int* profit, int profitSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int JobScheduling(int[] startTime, int[] endTime, int[] profit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number[]} profit
 * @return {number}
 */
var jobScheduling = function(startTime, endTime, profit) {
    
};
```

### TypeScript

```typescript
function jobScheduling(startTime: number[], endTime: number[], profit: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $startTime
     * @param Integer[] $endTime
     * @param Integer[] $profit
     * @return Integer
     */
    function jobScheduling($startTime, $endTime, $profit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func jobScheduling(_ startTime: [Int], _ endTime: [Int], _ profit: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun jobScheduling(startTime: IntArray, endTime: IntArray, profit: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int jobScheduling(List<int> startTime, List<int> endTime, List<int> profit) {
    
  }
}
```

### Go

```golang
func jobScheduling(startTime []int, endTime []int, profit []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} start_time
# @param {Integer[]} end_time
# @param {Integer[]} profit
# @return {Integer}
def job_scheduling(start_time, end_time, profit)
    
end
```

### Scala

```scala
object Solution {
    def jobScheduling(startTime: Array[Int], endTime: Array[Int], profit: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn job_scheduling(start_time: Vec<i32>, end_time: Vec<i32>, profit: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (job-scheduling startTime endTime profit)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec job_scheduling(StartTime :: [integer()], EndTime :: [integer()], Profit :: [integer()]) -> integer().
job_scheduling(StartTime, EndTime, Profit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec job_scheduling(start_time :: [integer], end_time :: [integer], profit :: [integer]) :: integer
  def job_scheduling(start_time, end_time, profit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func jobScheduling(startTime: Array<Int64>, endTime: Array<Int64>, profit: Array<Int64>): Int64 {

    }
}
```

