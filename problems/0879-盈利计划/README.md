# 879. 盈利计划

## 题目描述

<p>集团里有 <code>n</code> 名员工，他们可以完成各种各样的工作创造利润。</p>

<p>第 <code>i</code> 种工作会产生 <code>profit[i]</code> 的利润，它要求 <code>group[i]</code> 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。</p>

<p>工作的任何至少产生 <code>minProfit</code> 利润的子集称为 <strong>盈利计划</strong> 。并且工作的成员总数最多为 <code>n</code> 。</p>

<p>有多少种计划可以选择？因为答案很大，所以<strong> 返回结果模 </strong><code>10^9 + 7</code><strong> 的值</strong>。</p>

<div class="original__bRMd">
<div>
<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 5, minProfit = 3, group = [2,2], profit = [2,3]
<strong>输出：</strong>2
<strong>解释：</strong>至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
总的来说，有两种计划。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
<strong>输出：</strong>7
<strong>解释：</strong>至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。</pre>
</div>
</div>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 100</code></li>
	<li><code>0 <= minProfit <= 100</code></li>
	<li><code>1 <= group.length <= 100</code></li>
	<li><code>1 <= group[i] <= 100</code></li>
	<li><code>profit.length == group.length</code></li>
	<li><code>0 <= profit[i] <= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 示例

```
5
3
[2,2]
[2,3]
10
5
[2,3,5]
[6,7,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int profitableSchemes(int n, int minProfit, vector<int>& group, vector<int>& profit) {
        
    }
};
```

### Java

```java
class Solution {
    public int profitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        
```

### C

```c
int profitableSchemes(int n, int minProfit, int* group, int groupSize, int* profit, int profitSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ProfitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} minProfit
 * @param {number[]} group
 * @param {number[]} profit
 * @return {number}
 */
var profitableSchemes = function(n, minProfit, group, profit) {
    
};
```

### TypeScript

```typescript
function profitableSchemes(n: number, minProfit: number, group: number[], profit: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $minProfit
     * @param Integer[] $group
     * @param Integer[] $profit
     * @return Integer
     */
    function profitableSchemes($n, $minProfit, $group, $profit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func profitableSchemes(_ n: Int, _ minProfit: Int, _ group: [Int], _ profit: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun profitableSchemes(n: Int, minProfit: Int, group: IntArray, profit: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int profitableSchemes(int n, int minProfit, List<int> group, List<int> profit) {
    
  }
}
```

### Go

```golang
func profitableSchemes(n int, minProfit int, group []int, profit []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} min_profit
# @param {Integer[]} group
# @param {Integer[]} profit
# @return {Integer}
def profitable_schemes(n, min_profit, group, profit)
    
end
```

### Scala

```scala
object Solution {
    def profitableSchemes(n: Int, minProfit: Int, group: Array[Int], profit: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn profitable_schemes(n: i32, min_profit: i32, group: Vec<i32>, profit: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (profitable-schemes n minProfit group profit)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec profitable_schemes(N :: integer(), MinProfit :: integer(), Group :: [integer()], Profit :: [integer()]) -> integer().
profitable_schemes(N, MinProfit, Group, Profit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec profitable_schemes(n :: integer, min_profit :: integer, group :: [integer], profit :: [integer]) :: integer
  def profitable_schemes(n, min_profit, group, profit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func profitableSchemes(n: Int64, minProfit: Int64, group: Array<Int64>, profit: Array<Int64>): Int64 {

    }
}
```

