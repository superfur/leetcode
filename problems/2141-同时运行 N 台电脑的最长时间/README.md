# 2141. 同时运行 N 台电脑的最长时间

## 题目描述

<p>你有&nbsp;<code>n</code>&nbsp;台电脑。给你整数&nbsp;<code>n</code>&nbsp;和一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>batteries</code>&nbsp;，其中第&nbsp;<code>i</code>&nbsp;个电池可以让一台电脑 <strong>运行&nbsp;</strong><code>batteries[i]</code>&nbsp;分钟。你想使用这些电池让&nbsp;<strong>全部</strong>&nbsp;<code>n</code>&nbsp;台电脑 <b>同时</b>&nbsp;运行。</p>

<p>一开始，你可以给每台电脑连接 <strong>至多一个电池</strong>&nbsp;。然后在任意整数时刻，你都可以将一台电脑与它的电池断开连接，并连接另一个电池，你可以进行这个操作 <strong>任意次</strong>&nbsp;。新连接的电池可以是一个全新的电池，也可以是别的电脑用过的电池。断开连接和连接新的电池不会花费任何时间。</p>

<p>注意，你不能给电池充电。</p>

<p>请你返回你可以让 <code>n</code>&nbsp;台电脑同时运行的 <strong>最长</strong>&nbsp;分钟数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/01/06/example1-fit.png" style="width: 762px; height: 150px;"></p>

<pre><b>输入：</b>n = 2, batteries = [3,3,3]
<b>输出：</b>4
<b>解释：</b>
一开始，将第一台电脑与电池 0 连接，第二台电脑与电池 1 连接。
2 分钟后，将第二台电脑与电池 1 断开连接，并连接电池 2 。注意，电池 0 还可以供电 1 分钟。
在第 3 分钟结尾，你需要将第一台电脑与电池 0 断开连接，然后连接电池 1 。
在第 4 分钟结尾，电池 1 也被耗尽，第一台电脑无法继续运行。
我们最多能同时让两台电脑同时运行 4 分钟，所以我们返回 4 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/01/06/example2.png" style="width: 629px; height: 150px;"></p>

<pre><b>输入：</b>n = 2, batteries = [1,1,1,1]
<b>输出：</b>2
<b>解释：</b>
一开始，将第一台电脑与电池 0 连接，第二台电脑与电池 2 连接。
一分钟后，电池 0 和电池 2 同时耗尽，所以你需要将它们断开连接，并将电池 1 和第一台电脑连接，电池 3 和第二台电脑连接。
1 分钟后，电池 1 和电池 3 也耗尽了，所以两台电脑都无法继续运行。
我们最多能让两台电脑同时运行 2 分钟，所以我们返回 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= batteries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= batteries[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 二分查找
- 排序

## 提示

1. For a given running time, can you determine if it is possible to run all n computers simultaneously?
2. Try to use Binary Search to find the maximal running time

## 示例

```
2
[3,3,3]
2
[1,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxRunTime(int n, vector<int>& batteries) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxRunTime(int n, int[] batteries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
```

### C

```c
long long maxRunTime(int n, int* batteries, int batteriesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxRunTime(int n, int[] batteries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} batteries
 * @return {number}
 */
var maxRunTime = function(n, batteries) {
    
};
```

### TypeScript

```typescript
function maxRunTime(n: number, batteries: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $batteries
     * @return Integer
     */
    function maxRunTime($n, $batteries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxRunTime(_ n: Int, _ batteries: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxRunTime(n: Int, batteries: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxRunTime(int n, List<int> batteries) {
    
  }
}
```

### Go

```golang
func maxRunTime(n int, batteries []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} batteries
# @return {Integer}
def max_run_time(n, batteries)
    
end
```

### Scala

```scala
object Solution {
    def maxRunTime(n: Int, batteries: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_run_time(n: i32, batteries: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-run-time n batteries)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_run_time(N :: integer(), Batteries :: [integer()]) -> integer().
max_run_time(N, Batteries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_run_time(n :: integer, batteries :: [integer]) :: integer
  def max_run_time(n, batteries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxRunTime(n: Int64, batteries: Array<Int64>): Int64 {

    }
}
```

