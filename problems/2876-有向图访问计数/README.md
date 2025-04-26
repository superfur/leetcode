# 2876. 有向图访问计数

## 题目描述

<p>现有一个有向图，其中包含 <code>n</code> 个节点，节点编号从 <code>0</code> 到 <code>n - 1</code> 。此外，该图还包含了 <code>n</code> 条有向边。</p>

<p>给你一个下标从 <strong>0</strong> 开始的数组 <code>edges</code> ，其中 <code>edges[i]</code> 表示存在一条从节点 <code>i</code> 到节点 <code>edges[i]</code> 的边。</p>

<p>想象在图上发生以下过程：</p>

<ul>
	<li>你从节点 <code>x</code> 开始，通过边访问其他节点，直到你在<strong> 此过程 </strong>中再次访问到之前已经访问过的节点。</li>
</ul>

<p>返回数组 <code>answer</code> 作为答案，其中 <code>answer[i]</code> 表示如果从节点 <code>i</code> 开始执行该过程，你可以访问到的不同节点数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/08/31/graaphdrawio-1.png" />
<pre>
<strong>输入：</strong>edges = [1,2,0,0]
<strong>输出：</strong>[3,3,3,4]
<strong>解释：</strong>从每个节点开始执行该过程，记录如下：
- 从节点 0 开始，访问节点 0 -&gt; 1 -&gt; 2 -&gt; 0 。访问的不同节点数是 3 。
- 从节点 1 开始，访问节点 1 -&gt; 2 -&gt; 0 -&gt; 1 。访问的不同节点数是 3 。
- 从节点 2 开始，访问节点 2 -&gt; 0 -&gt; 1 -&gt; 2 。访问的不同节点数是 3 。
- 从节点 3 开始，访问节点 3 -&gt; 0 -&gt; 1 -&gt; 2 -&gt; 0 。访问的不同节点数是 4 。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/08/31/graaph2drawio.png" style="width: 191px; height: 251px;" />
<pre>
<strong>输入：</strong>edges = [1,2,3,4,0]
<strong>输出：</strong>[5,5,5,5,5]
<strong>解释：</strong>无论从哪个节点开始，在这个过程中，都可以访问到图中的每一个节点。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= edges[i] &lt;= n - 1</code></li>
	<li><code>edges[i] != i</code></li>
</ul>


## 难度

Hard

## 标签

- 图
- 记忆化搜索
- 动态规划

## 提示

1. Consider if the graph was only one cycle, what will be the answer for each node?
2. The actual graph will always consist of at least one cycle and some other nodes.
3. Calculate the answer for nodes in cycles the same way as in hint 1. How do you calculate the answer for the remaining nodes?

## 示例

```
[1,2,0,0]
[1,2,3,4,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> countVisitedNodes(vector<int>& edges) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] countVisitedNodes(List<Integer> edges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countVisitedNodes(self, edges):
        """
        :type edges: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countVisitedNodes(int* edges, int edgesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] CountVisitedNodes(IList<int> edges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} edges
 * @return {number[]}
 */
var countVisitedNodes = function(edges) {
    
};
```

### TypeScript

```typescript
function countVisitedNodes(edges: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $edges
     * @return Integer[]
     */
    function countVisitedNodes($edges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countVisitedNodes(_ edges: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countVisitedNodes(edges: List<Int>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countVisitedNodes(List<int> edges) {
    
  }
}
```

### Go

```golang
func countVisitedNodes(edges []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} edges
# @return {Integer[]}
def count_visited_nodes(edges)
    
end
```

### Scala

```scala
object Solution {
    def countVisitedNodes(edges: List[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_visited_nodes(edges: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (count-visited-nodes edges)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_visited_nodes(Edges :: [integer()]) -> [integer()].
count_visited_nodes(Edges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_visited_nodes(edges :: [integer]) :: [integer]
  def count_visited_nodes(edges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countVisitedNodes(edges: ArrayList<Int64>): Array<Int64> {

    }
}
```

