# 1575. 统计所有可行路径

## 题目描述

<p>给你一个 <strong>互不相同</strong>&nbsp;的整数数组，其中&nbsp;<code>locations[i]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个城市的位置。同时给你&nbsp;<code>start</code>，<code>finish</code>&nbsp;和&nbsp;<code>fuel</code>&nbsp;分别表示出发城市、目的地城市和你初始拥有的汽油总量</p>

<p>每一步中，如果你在城市 <code>i</code>&nbsp;，你可以选择任意一个城市 <code>j</code>&nbsp;，满足 &nbsp;<code>j != i</code>&nbsp;且&nbsp;<code>0 &lt;= j &lt; locations.length</code>&nbsp;，并移动到城市&nbsp;<code>j</code>&nbsp;。从城市&nbsp;<code>i</code>&nbsp;移动到&nbsp;<code>j</code>&nbsp;消耗的汽油量为&nbsp;<code>|locations[i] - locations[j]|</code>，<code>|x|</code>&nbsp;表示&nbsp;<code>x</code>&nbsp;的绝对值。</p>

<p>请注意，&nbsp;<code>fuel</code>&nbsp;任何时刻都&nbsp;<strong>不能</strong>&nbsp;为负，且你&nbsp;<strong>可以</strong>&nbsp;经过任意城市超过一次（包括&nbsp;<code>start</code>&nbsp;和&nbsp;<code>finish</code>&nbsp;）。</p>

<p>请你返回从<em>&nbsp;</em><code>start</code>&nbsp;到&nbsp;<code>finish</code>&nbsp;所有可能路径的数目。</p>

<p>由于答案可能很大， 请将它对&nbsp;<code>10^9 + 7</code>&nbsp;取余后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
<strong>输出：</strong>4
<strong>解释：</strong>以下为所有可能路径，每一条都用了 5 单位的汽油：
1 -&gt; 3
1 -&gt; 2 -&gt; 3
1 -&gt; 4 -&gt; 3
1 -&gt; 4 -&gt; 2 -&gt; 3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>locations = [4,3,1], start = 1, finish = 0, fuel = 6
<strong>输出：</strong>5
<strong>解释：</strong>以下为所有可能的路径：
1 -&gt; 0，使用汽油量为 fuel = 1
1 -&gt; 2 -&gt; 0，使用汽油量为 fuel = 5
1 -&gt; 2 -&gt; 1 -&gt; 0，使用汽油量为 fuel = 5
1 -&gt; 0 -&gt; 1 -&gt; 0，使用汽油量为 fuel = 3
1 -&gt; 0 -&gt; 1 -&gt; 0 -&gt; 1 -&gt; 0，使用汽油量为 fuel = 5
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>locations = [5,2,1], start = 0, finish = 2, fuel = 3
<strong>输出：</strong>0
<strong>解释：</strong>没有办法只用 3 单位的汽油从 0 到达 2 。因为最短路径需要 4 单位的汽油。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= locations.length &lt;= 100</code></li>
	<li><code>1 &lt;= locations[i] &lt;= 10<sup>9</sup></code></li>
	<li>所有&nbsp;<code>locations</code>&nbsp;中的整数 <strong>互不相同</strong>&nbsp;。</li>
	<li><code>0 &lt;= start, finish &lt;&nbsp;locations.length</code></li>
	<li><code>1 &lt;= fuel &lt;= 200</code></li>
</ul>


## 难度

Hard

## 标签

- 记忆化搜索
- 数组
- 动态规划

## 提示

1. Use dynamic programming to solve this problem with each state defined by the city index and fuel left.
2. Since the array contains distinct integers fuel will always be spent in each move and so there can be no cycles.

## 示例

```
[2,3,6,8,4]
1
3
5
[4,3,1]
1
0
6
[5,2,1]
0
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countRoutes(vector<int>& locations, int start, int finish, int fuel) {
        
    }
};
```

### Java

```java
class Solution {
    public int countRoutes(int[] locations, int start, int finish, int fuel) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
```

### C

```c
int countRoutes(int* locations, int locationsSize, int start, int finish, int fuel) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountRoutes(int[] locations, int start, int finish, int fuel) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} locations
 * @param {number} start
 * @param {number} finish
 * @param {number} fuel
 * @return {number}
 */
var countRoutes = function(locations, start, finish, fuel) {
    
};
```

### TypeScript

```typescript
function countRoutes(locations: number[], start: number, finish: number, fuel: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $locations
     * @param Integer $start
     * @param Integer $finish
     * @param Integer $fuel
     * @return Integer
     */
    function countRoutes($locations, $start, $finish, $fuel) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countRoutes(_ locations: [Int], _ start: Int, _ finish: Int, _ fuel: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countRoutes(locations: IntArray, start: Int, finish: Int, fuel: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countRoutes(List<int> locations, int start, int finish, int fuel) {
    
  }
}
```

### Go

```golang
func countRoutes(locations []int, start int, finish int, fuel int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} locations
# @param {Integer} start
# @param {Integer} finish
# @param {Integer} fuel
# @return {Integer}
def count_routes(locations, start, finish, fuel)
    
end
```

### Scala

```scala
object Solution {
    def countRoutes(locations: Array[Int], start: Int, finish: Int, fuel: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_routes(locations: Vec<i32>, start: i32, finish: i32, fuel: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-routes locations start finish fuel)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_routes(Locations :: [integer()], Start :: integer(), Finish :: integer(), Fuel :: integer()) -> integer().
count_routes(Locations, Start, Finish, Fuel) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_routes(locations :: [integer], start :: integer, finish :: integer, fuel :: integer) :: integer
  def count_routes(locations, start, finish, fuel) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countRoutes(locations: Array<Int64>, start: Int64, finish: Int64, fuel: Int64): Int64 {

    }
}
```

