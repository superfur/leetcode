# 1606. 找到处理最多请求的服务器

## 题目描述

<p>你有 <code>k</code>&nbsp;个服务器，编号为 <code>0</code>&nbsp;到 <code>k-1</code>&nbsp;，它们可以同时处理多个请求组。每个服务器有无穷的计算能力但是 <strong>不能同时处理超过一个请求</strong>&nbsp;。请求分配到服务器的规则如下：</p>

<ul>
	<li>第&nbsp;<code>i</code>&nbsp;（序号从 0 开始）个请求到达。</li>
	<li>如果所有服务器都已被占据，那么该请求被舍弃（完全不处理）。</li>
	<li>如果第&nbsp;<code>(i % k)</code>&nbsp;个服务器空闲，那么对应服务器会处理该请求。</li>
	<li>否则，将请求安排给下一个空闲的服务器（服务器构成一个环，必要的话可能从第 0 个服务器开始继续找下一个空闲的服务器）。比方说，如果第 <code>i</code>&nbsp;个服务器在忙，那么会查看第 <code>(i+1)</code>&nbsp;个服务器，第 <code>(i+2)</code>&nbsp;个服务器等等。</li>
</ul>

<p>给你一个 <strong>严格递增</strong>&nbsp;的正整数数组&nbsp;<code>arrival</code>&nbsp;，表示第&nbsp;<code>i</code>&nbsp;个任务的到达时间，和另一个数组&nbsp;<code>load</code>&nbsp;，其中&nbsp;<code>load[i]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个请求的工作量（也就是服务器完成它所需要的时间）。你的任务是找到 <strong>最繁忙的服务器</strong>&nbsp;。最繁忙定义为一个服务器处理的请求数是所有服务器里最多的。</p>

<p>请你返回包含所有&nbsp;<strong>最繁忙服务器</strong>&nbsp;序号的列表，你可以以任意顺序返回这个列表。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/03/load-1.png" style="height: 221px; width: 389px;" /></p>

<pre>
<strong>输入：</strong>k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
<strong>输出：</strong>[1] 
<strong>解释：</strong>
所有服务器一开始都是空闲的。
前 3 个请求分别由前 3 台服务器依次处理。
请求 3 进来的时候，服务器 0 被占据，所以它被安排到下一台空闲的服务器，也就是服务器 1 。
请求 4 进来的时候，由于所有服务器都被占据，该请求被舍弃。
服务器 0 和 2 分别都处理了一个请求，服务器 1 处理了两个请求。所以服务器 1 是最忙的服务器。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
<strong>输出：</strong>[0]
<strong>解释：</strong>
前 3 个请求分别被前 3 个服务器处理。
请求 3 进来，由于服务器 0 空闲，它被服务器 0 处理。
服务器 0 处理了两个请求，服务器 1 和 2 分别处理了一个请求。所以服务器 0 是最忙的服务器。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>k = 3, arrival = [1,2,3], load = [10,12,11]
<strong>输出：</strong>[0,1,2]
<strong>解释：</strong>每个服务器分别处理了一个请求，所以它们都是最忙的服务器。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2]
<strong>输出：</strong>[1]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>k = 1, arrival = [1], load = [1]
<strong>输出：</strong>[0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arrival.length, load.length &lt;= 10<sup>5</sup></code></li>
	<li><code>arrival.length == load.length</code></li>
	<li><code>1 &lt;= arrival[i], load[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>arrival</code>&nbsp;保证 <strong>严格递增</strong>&nbsp;。</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 有序集合
- 堆（优先队列）

## 提示

1. To speed up the next available server search, keep track of the available servers in a sorted structure such as an ordered set.
2. To determine if a server is available, keep track of the end times for each task in a heap and add the server to the available set once the soonest task ending time is less than or equal to the next task to add.

## 示例

```
3
[1,2,3,4,5]
[5,2,3,3,3]
3
[1,2,3,4]
[1,2,1,2]
3
[1,2,3]
[10,12,11]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {
        
    }
}
```

### Python

```python
class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* busiestServers(int k, int* arrival, int arrivalSize, int* load, int loadSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> BusiestServers(int k, int[] arrival, int[] load) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @param {number[]} arrival
 * @param {number[]} load
 * @return {number[]}
 */
var busiestServers = function(k, arrival, load) {
    
};
```

### TypeScript

```typescript
function busiestServers(k: number, arrival: number[], load: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer[] $arrival
     * @param Integer[] $load
     * @return Integer[]
     */
    function busiestServers($k, $arrival, $load) {
        
    }
}
```

### Swift

```swift
class Solution {
    func busiestServers(_ k: Int, _ arrival: [Int], _ load: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun busiestServers(k: Int, arrival: IntArray, load: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> busiestServers(int k, List<int> arrival, List<int> load) {
    
  }
}
```

### Go

```golang
func busiestServers(k int, arrival []int, load []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @param {Integer[]} arrival
# @param {Integer[]} load
# @return {Integer[]}
def busiest_servers(k, arrival, load)
    
end
```

### Scala

```scala
object Solution {
    def busiestServers(k: Int, arrival: Array[Int], load: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn busiest_servers(k: i32, arrival: Vec<i32>, load: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (busiest-servers k arrival load)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec busiest_servers(K :: integer(), Arrival :: [integer()], Load :: [integer()]) -> [integer()].
busiest_servers(K, Arrival, Load) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec busiest_servers(k :: integer, arrival :: [integer], load :: [integer]) :: [integer]
  def busiest_servers(k, arrival, load) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func busiestServers(k: Int64, arrival: Array<Int64>, load: Array<Int64>): ArrayList<Int64> {

    }
}
```

