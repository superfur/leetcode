# 502. IPO

## 题目描述

<p>假设 力扣（LeetCode）即将开始 <strong>IPO</strong> 。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，它只能在 IPO 之前完成最多 <code>k</code> 个不同的项目。帮助 力扣 设计完成最多 <code>k</code> 个不同项目后得到最大总资本的方式。</p>

<p>给你 <code>n</code> 个项目。对于每个项目 <code>i</code><strong> </strong>，它都有一个纯利润 <code>profits[i]</code> ，和启动该项目需要的最小资本 <code>capital[i]</code> 。</p>

<p>最初，你的资本为 <code>w</code> 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。</p>

<p>总而言之，从给定项目中选择 <strong>最多</strong> <code>k</code> 个不同项目的列表，以 <strong>最大化最终资本</strong> ，并输出最终可获得的最多资本。</p>

<p>答案保证在 32 位有符号整数范围内。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
<strong>输出：</strong>4
<strong>解释：
</strong>由于你的初始资本为 0，你仅可以从 0 号项目开始。
在完成后，你将获得 1 的利润，你的总资本将变为 1。
此时你可以选择开始 1 号或 2 号项目。
由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
<strong>输出：</strong>6
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= w &lt;= 10<sup>9</sup></code></li>
	<li><code>n == profits.length</code></li>
	<li><code>n == capital.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= profits[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= capital[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 排序
- 堆（优先队列）

## 示例

```
2
0
[1,2,3]
[0,1,1]
3
0
[1,2,3]
[0,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
```

### C

```c
int findMaximizedCapital(int k, int w, int* profits, int profitsSize, int* capital, int capitalSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @param {number} w
 * @param {number[]} profits
 * @param {number[]} capital
 * @return {number}
 */
var findMaximizedCapital = function(k, w, profits, capital) {
    
};
```

### TypeScript

```typescript
function findMaximizedCapital(k: number, w: number, profits: number[], capital: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer $w
     * @param Integer[] $profits
     * @param Integer[] $capital
     * @return Integer
     */
    function findMaximizedCapital($k, $w, $profits, $capital) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMaximizedCapital(_ k: Int, _ w: Int, _ profits: [Int], _ capital: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaximizedCapital(k: Int, w: Int, profits: IntArray, capital: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMaximizedCapital(int k, int w, List<int> profits, List<int> capital) {
    
  }
}
```

### Go

```golang
func findMaximizedCapital(k int, w int, profits []int, capital []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @param {Integer} w
# @param {Integer[]} profits
# @param {Integer[]} capital
# @return {Integer}
def find_maximized_capital(k, w, profits, capital)
    
end
```

### Scala

```scala
object Solution {
    def findMaximizedCapital(k: Int, w: Int, profits: Array[Int], capital: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_maximized_capital(k: i32, w: i32, profits: Vec<i32>, capital: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-maximized-capital k w profits capital)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_maximized_capital(K :: integer(), W :: integer(), Profits :: [integer()], Capital :: [integer()]) -> integer().
find_maximized_capital(K, W, Profits, Capital) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_maximized_capital(k :: integer, w :: integer, profits :: [integer], capital :: [integer]) :: integer
  def find_maximized_capital(k, w, profits, capital) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMaximizedCapital(k: Int64, w: Int64, profits: Array<Int64>, capital: Array<Int64>): Int64 {

    }
}
```

