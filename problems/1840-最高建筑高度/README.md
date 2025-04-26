# 1840. 最高建筑高度

## 题目描述

<p>在一座城市里，你需要建 <code>n</code> 栋新的建筑。这些新的建筑会从 <code>1</code> 到 <code>n</code> 编号排成一列。</p>

<p>这座城市对这些新建筑有一些规定：</p>

<ul>
	<li>每栋建筑的高度必须是一个非负整数。</li>
	<li>第一栋建筑的高度 <strong>必须</strong> 是 <code>0</code> 。</li>
	<li>任意两栋相邻建筑的高度差 <strong>不能超过</strong>  <code>1</code> 。</li>
</ul>

<p>除此以外，某些建筑还有额外的最高高度限制。这些限制会以二维整数数组 <code>restrictions</code> 的形式给出，其中 <code>restrictions[i] = [id<sub>i</sub>, maxHeight<sub>i</sub>]</code> ，表示建筑 <code>id<sub>i</sub></code> 的高度 <strong>不能超过</strong> <code>maxHeight<sub>i</sub></code> 。</p>

<p>题目保证每栋建筑在 <code>restrictions</code> 中<strong> 至多出现一次</strong> ，同时建筑 <code>1</code> <strong>不会</strong> 出现在 <code>restrictions</code> 中。</p>

<p>请你返回 <strong>最高</strong> 建筑能达到的 <strong>最高高度</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/25/ic236-q4-ex1-1.png" style="width: 400px; height: 253px;" />
<pre>
<b>输入：</b>n = 5, restrictions = [[2,1],[4,1]]
<b>输出：</b>2
<b>解释：</b>上图中的绿色区域为每栋建筑被允许的最高高度。
我们可以使建筑高度分别为 [0,1,2,1,2] ，最高建筑的高度为 2 。</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/25/ic236-q4-ex2.png" style="width: 500px; height: 269px;" />
<pre>
<b>输入：</b>n = 6, restrictions = []
<b>输出：</b>5
<b>解释：</b>上图中的绿色区域为每栋建筑被允许的最高高度。
我们可以使建筑高度分别为 [0,1,2,3,4,5] ，最高建筑的高度为 5 。
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/25/ic236-q4-ex3.png" style="width: 500px; height: 187px;" />
<pre>
<b>输入：</b>n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
<b>输出：</b>5
<b>解释：</b>上图中的绿色区域为每栋建筑被允许的最高高度。
我们可以使建筑高度分别为 [0,1,2,3,3,4,4,5,4,3] ，最高建筑的高度为 5 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= n <= 10<sup>9</sup></code></li>
	<li><code>0 <= restrictions.length <= min(n - 1, 10<sup>5</sup>)</code></li>
	<li><code>2 <= id<sub>i</sub> <= n</code></li>
	<li><code>id<sub>i</sub></code> 是 <strong>唯一的</strong> 。</li>
	<li><code>0 <= maxHeight<sub>i</sub> <= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 排序

## 提示

1. Is it possible to find the max height if given the height range of a particular building?
2. You can find the height range of a restricted building by doing 2 passes from the left and right.

## 示例

```
5
[[2,1],[4,1]]
6
[]
10
[[5,3],[2,5],[7,4],[10,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxBuilding(int n, vector<vector<int>>& restrictions) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxBuilding(int n, int[][] restrictions) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        
```

### C

```c
int maxBuilding(int n, int** restrictions, int restrictionsSize, int* restrictionsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxBuilding(int n, int[][] restrictions) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} restrictions
 * @return {number}
 */
var maxBuilding = function(n, restrictions) {
    
};
```

### TypeScript

```typescript
function maxBuilding(n: number, restrictions: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $restrictions
     * @return Integer
     */
    function maxBuilding($n, $restrictions) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxBuilding(_ n: Int, _ restrictions: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxBuilding(n: Int, restrictions: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxBuilding(int n, List<List<int>> restrictions) {
    
  }
}
```

### Go

```golang
func maxBuilding(n int, restrictions [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} restrictions
# @return {Integer}
def max_building(n, restrictions)
    
end
```

### Scala

```scala
object Solution {
    def maxBuilding(n: Int, restrictions: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_building(n: i32, restrictions: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-building n restrictions)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_building(N :: integer(), Restrictions :: [[integer()]]) -> integer().
max_building(N, Restrictions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_building(n :: integer, restrictions :: [[integer]]) :: integer
  def max_building(n, restrictions) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxBuilding(n: Int64, restrictions: Array<Array<Int64>>): Int64 {

    }
}
```

