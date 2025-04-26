# 547. 省份数量

## 题目描述

<div class="original__bRMd">
<div>
<p>有 <code>n</code> 个城市，其中一些彼此相连，另一些没有相连。如果城市 <code>a</code> 与城市 <code>b</code> 直接相连，且城市 <code>b</code> 与城市 <code>c</code> 直接相连，那么城市 <code>a</code> 与城市 <code>c</code> 间接相连。</p>

<p><strong>省份</strong> 是一组直接或间接相连的城市，组内不含其他没有相连的城市。</p>

<p>给你一个 <code>n x n</code> 的矩阵 <code>isConnected</code> ，其中 <code>isConnected[i][j] = 1</code> 表示第 <code>i</code> 个城市和第 <code>j</code> 个城市直接相连，而 <code>isConnected[i][j] = 0</code> 表示二者不直接相连。</p>

<p>返回矩阵中 <strong>省份</strong> 的数量。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg" style="width: 222px; height: 142px;" />
<pre>
<strong>输入：</strong>isConnected = [[1,1,0],[1,1,0],[0,0,1]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg" style="width: 222px; height: 142px;" />
<pre>
<strong>输入：</strong>isConnected = [[1,0,0],[0,1,0],[0,0,1]]
<strong>输出：</strong>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 200</code></li>
	<li><code>n == isConnected.length</code></li>
	<li><code>n == isConnected[i].length</code></li>
	<li><code>isConnected[i][j]</code> 为 <code>1</code> 或 <code>0</code></li>
	<li><code>isConnected[i][i] == 1</code></li>
	<li><code>isConnected[i][j] == isConnected[j][i]</code></li>
</ul>
</div>
</div>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 图

## 示例

```
[[1,1,0],[1,1,0],[0,0,1]]
[[1,0,0],[0,1,0],[0,0,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        
    }
};
```

### Java

```java
class Solution {
    public int findCircleNum(int[][] isConnected) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
```

### C

```c
int findCircleNum(int** isConnected, int isConnectedSize, int* isConnectedColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindCircleNum(int[][] isConnected) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function(isConnected) {
    
};
```

### TypeScript

```typescript
function findCircleNum(isConnected: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $isConnected
     * @return Integer
     */
    function findCircleNum($isConnected) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findCircleNum(_ isConnected: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findCircleNum(isConnected: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findCircleNum(List<List<int>> isConnected) {
    
  }
}
```

### Go

```golang
func findCircleNum(isConnected [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} is_connected
# @return {Integer}
def find_circle_num(is_connected)
    
end
```

### Scala

```scala
object Solution {
    def findCircleNum(isConnected: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-circle-num isConnected)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_circle_num(IsConnected :: [[integer()]]) -> integer().
find_circle_num(IsConnected) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_circle_num(is_connected :: [[integer]]) :: integer
  def find_circle_num(is_connected) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findCircleNum(isConnected: Array<Array<Int64>>): Int64 {

    }
}
```

