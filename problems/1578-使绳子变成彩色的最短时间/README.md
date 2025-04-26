# 1578. 使绳子变成彩色的最短时间

## 题目描述

<p>Alice 把 <code>n</code> 个气球排列在一根绳子上。给你一个下标从 <strong>0</strong> 开始的字符串 <code>colors</code> ，其中 <code>colors[i]</code> 是第 <code>i</code> 个气球的颜色。</p>

<p>Alice 想要把绳子装扮成 <b>五颜六色的</b>&nbsp;，且她不希望两个连续的气球涂着相同的颜色，所以她喊来 Bob 帮忙。Bob 可以从绳子上移除一些气球使绳子变成 <strong>彩色</strong> 。给你一个 <strong>下标从 0 开始&nbsp;</strong>的整数数组 <code>neededTime</code> ，其中 <code>neededTime[i]</code> 是 Bob 从绳子上移除第 <code>i</code> 个气球需要的时间（以秒为单位）。</p>

<p>返回 Bob 使绳子变成 <strong>彩色</strong> 需要的 <strong>最少时间</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/ballon1.jpg" style="width: 404px; height: 243px;" />
<pre>
<strong>输入：</strong>colors = "abaac", neededTime = [1,2,3,4,5]
<strong>输出：</strong>3
<strong>解释：</strong>在上图中，'a' 是蓝色，'b' 是红色且 'c' 是绿色。
Bob 可以移除下标 2 的蓝色气球。这将花费 3 秒。
移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 3 。</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/balloon2.jpg" style="width: 244px; height: 243px;" />
<pre>
<strong>输入：</strong>colors = "abc", neededTime = [1,2,3]
<strong>输出：</strong>0
<strong>解释：</strong>绳子已经是彩色的，Bob 不需要从绳子上移除任何气球。
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/balloon3.jpg" style="width: 404px; height: 243px;" />
<pre>
<strong>输入：</strong>colors = "aabaa", neededTime = [1,2,3,4,1]
<strong>输出：</strong>2
<strong>解释：</strong>Bob 会移除下标 0 和下标 4 处的气球。这两个气球各需要 1 秒来移除。
移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 1 + 1 = 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == colors.length == neededTime.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= neededTime[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>colors</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 字符串
- 动态规划

## 提示

1. Maintain the running sum and max value for repeated letters.

## 示例

```
"abaac"
[1,2,3,4,5]
"abc"
[1,2,3]
"aabaa"
[1,2,3,4,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCost(String colors, int[] neededTime) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
```

### C

```c
int minCost(char* colors, int* neededTime, int neededTimeSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCost(string colors, int[] neededTime) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} colors
 * @param {number[]} neededTime
 * @return {number}
 */
var minCost = function(colors, neededTime) {
    
};
```

### TypeScript

```typescript
function minCost(colors: string, neededTime: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $colors
     * @param Integer[] $neededTime
     * @return Integer
     */
    function minCost($colors, $neededTime) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCost(_ colors: String, _ neededTime: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCost(colors: String, neededTime: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCost(String colors, List<int> neededTime) {
    
  }
}
```

### Go

```golang
func minCost(colors string, neededTime []int) int {
    
}
```

### Ruby

```ruby
# @param {String} colors
# @param {Integer[]} needed_time
# @return {Integer}
def min_cost(colors, needed_time)
    
end
```

### Scala

```scala
object Solution {
    def minCost(colors: String, neededTime: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost colors neededTime)
  (-> string? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost(Colors :: unicode:unicode_binary(), NeededTime :: [integer()]) -> integer().
min_cost(Colors, NeededTime) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost(colors :: String.t, needed_time :: [integer]) :: integer
  def min_cost(colors, needed_time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCost(colors: String, neededTime: Array<Int64>): Int64 {

    }
}
```

