# 2813. 子序列最大优雅度

## 题目描述

<p>给你一个长度为 <code>n</code> 的二维整数数组 <code>items</code> 和一个整数 <code>k</code> 。</p>

<p><code>items[i] = [profit<sub>i</sub>, category<sub>i</sub>]</code>，其中 <code>profit<sub>i</sub></code> 和 <code>category<sub>i</sub></code> 分别表示第 <code>i</code> 个项目的利润和类别。</p>

<p>现定义&nbsp;<code>items</code> 的 <strong>子序列</strong> 的 <strong>优雅度</strong> 可以用 <code>total_profit + distinct_categories<sup>2</sup></code> 计算，其中 <code>total_profit</code> 是子序列中所有项目的利润总和，<code>distinct_categories</code> 是所选子序列所含的所有类别中不同类别的数量。</p>

<p>你的任务是从 <code>items</code> 所有长度为 <code>k</code> 的子序列中，找出 <strong>最大优雅度</strong> 。</p>

<p>用整数形式表示并返回 <code>items</code> 中所有长度恰好为 <code>k</code> 的子序列的最大优雅度。</p>

<p><strong>注意：</strong>数组的子序列是经由原数组删除一些元素（可能不删除）而产生的新数组，且删除不改变其余元素相对顺序。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>items = [[3,2],[5,1],[10,1]], k = 2
<strong>输出：</strong>17
<strong>解释：
</strong>在这个例子中，我们需要选出长度为 2 的子序列。
其中一种方案是 items[0] = [3,2] 和 items[2] = [10,1] 。
子序列的总利润为 3 + 10 = 13 ，子序列包含 2 种不同类别 [2,1] 。
因此，优雅度为 13 + 2<sup>2</sup> = 17 ，可以证明 17 是可以获得的最大优雅度。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>items = [[3,1],[3,1],[2,2],[5,3]], k = 3
<strong>输出：</strong>19
<strong>解释：</strong>
在这个例子中，我们需要选出长度为 3 的子序列。 
其中一种方案是 items[0] = [3,1] ，items[2] = [2,2] 和 items[3] = [5,3] 。
子序列的总利润为 3 + 2 + 5 = 10 ，子序列包含 3 种不同类别 [1, 2, 3] 。 
因此，优雅度为 10 + 3<sup>2</sup> = 19 ，可以证明 19 是可以获得的最大优雅度。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>items = [[1,1],[2,1],[3,1]], k = 3
<strong>输出：</strong>7
<strong>解释：
</strong>在这个例子中，我们需要选出长度为 3 的子序列。
我们需要选中所有项目。
子序列的总利润为 1 + 2 + 3 = 6，子序列包含 1 种不同类别 [1] 。
因此，最大优雅度为 6 + 1<sup>2</sup> = 7 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= items.length == n &lt;= 10<sup>5</sup></code></li>
	<li><code>items[i].length == 2</code></li>
	<li><code>items[i][0] == profit<sub>i</sub></code></li>
	<li><code>items[i][1] == category<sub>i</sub></code></li>
	<li><code>1 &lt;= profit<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= category<sub>i</sub> &lt;= n </code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 贪心
- 数组
- 哈希表
- 排序
- 堆（优先队列）

## 提示

1. <div class="_1l1MA">Greedy algorithm.</div>
2. <div class="_1l1MA">Sort items in non-increasing order of profits.</div>
3. <div class="_1l1MA">Select the first <code>k</code> items (the top <code>k</code> most profitable items). Keep track of the items as the candidate set.</div>
4. <div class="_1l1MA">For the remaining <code>n - k</code> items sorted in non-increasing order of profits, try replacing an item in the candidate set using the current item.</div>
5. <div class="_1l1MA">The replacing item should add a new category to the candidate set and should remove the item with the minimum profit that occurs more than once in the candidate set.</div>

## 示例

```
[[3,2],[5,1],[10,1]]
2
[[3,1],[3,1],[2,2],[5,3]]
3
[[1,1],[2,1],[3,1]]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long findMaximumElegance(vector<vector<int>>& items, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long findMaximumElegance(int[][] items, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMaximumElegance(self, items, k):
        """
        :type items: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        
```

### C

```c
long long findMaximumElegance(int** items, int itemsSize, int* itemsColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long FindMaximumElegance(int[][] items, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} items
 * @param {number} k
 * @return {number}
 */
var findMaximumElegance = function(items, k) {
    
};
```

### TypeScript

```typescript
function findMaximumElegance(items: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $items
     * @param Integer $k
     * @return Integer
     */
    function findMaximumElegance($items, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMaximumElegance(_ items: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaximumElegance(items: Array<IntArray>, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMaximumElegance(List<List<int>> items, int k) {
    
  }
}
```

### Go

```golang
func findMaximumElegance(items [][]int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} items
# @param {Integer} k
# @return {Integer}
def find_maximum_elegance(items, k)
    
end
```

### Scala

```scala
object Solution {
    def findMaximumElegance(items: Array[Array[Int]], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_maximum_elegance(items: Vec<Vec<i32>>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (find-maximum-elegance items k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_maximum_elegance(Items :: [[integer()]], K :: integer()) -> integer().
find_maximum_elegance(Items, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_maximum_elegance(items :: [[integer]], k :: integer) :: integer
  def find_maximum_elegance(items, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMaximumElegance(items: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

