# 2271. 毯子覆盖的最多白色砖块数

## 题目描述

<p>给你一个二维整数数组&nbsp;<code>tiles</code>&nbsp;，其中&nbsp;<code>tiles[i] = [l<sub>i</sub>, r<sub>i</sub>]</code>&nbsp;，表示所有在&nbsp;<code>l<sub>i</sub> &lt;= j &lt;= r<sub>i</sub></code>&nbsp;之间的每个瓷砖位置 <code>j</code>&nbsp;都被涂成了白色。</p>

<p>同时给你一个整数&nbsp;<code>carpetLen</code>&nbsp;，表示可以放在&nbsp;<strong>任何位置</strong>&nbsp;的一块毯子的长度。</p>

<p>请你返回使用这块毯子，<strong>最多</strong>&nbsp;可以盖住多少块瓷砖。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/25/example1drawio3.png" style="width: 644px; height: 158px;" /></p>

<pre>
<b>输入：</b>tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
<b>输出：</b>9
<b>解释：</b>将毯子从瓷砖 10 开始放置。
总共覆盖 9 块瓷砖，所以返回 9 。
注意可能有其他方案也可以覆盖 9 块瓷砖。
可以看出，瓷砖无法覆盖超过 9 块瓷砖。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/24/example2drawio.png" style="width: 231px; height: 168px;" /></p>

<pre>
<strong>输入：</strong>tiles = [[10,11],[1,1]], carpetLen = 2
<b>输出：</b>2
<b>解释：</b>将毯子从瓷砖 10 开始放置。
总共覆盖 2 块瓷砖，所以我们返回 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= tiles.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>tiles[i].length == 2</code></li>
	<li><code>1 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= carpetLen &lt;= 10<sup>9</sup></code></li>
	<li><code>tiles</code>&nbsp;互相 <strong>不会重叠</strong>&nbsp;。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 二分查找
- 前缀和
- 排序
- 滑动窗口

## 提示

1. Think about the potential placements of the carpet in an optimal solution.
2. Can we use Prefix Sum and Binary Search to determine how many tiles are covered for a given placement?

## 示例

```
[[1,5],[10,11],[12,18],[20,25],[30,32]]
10
[[10,11],[1,1]]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumWhiteTiles(vector<vector<int>>& tiles, int carpetLen) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumWhiteTiles(int[][] tiles, int carpetLen) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        :type tiles: List[List[int]]
        :type carpetLen: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        
```

### C

```c
int maximumWhiteTiles(int** tiles, int tilesSize, int* tilesColSize, int carpetLen) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumWhiteTiles(int[][] tiles, int carpetLen) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} tiles
 * @param {number} carpetLen
 * @return {number}
 */
var maximumWhiteTiles = function(tiles, carpetLen) {
    
};
```

### TypeScript

```typescript
function maximumWhiteTiles(tiles: number[][], carpetLen: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $tiles
     * @param Integer $carpetLen
     * @return Integer
     */
    function maximumWhiteTiles($tiles, $carpetLen) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumWhiteTiles(_ tiles: [[Int]], _ carpetLen: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumWhiteTiles(tiles: Array<IntArray>, carpetLen: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumWhiteTiles(List<List<int>> tiles, int carpetLen) {
    
  }
}
```

### Go

```golang
func maximumWhiteTiles(tiles [][]int, carpetLen int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} tiles
# @param {Integer} carpet_len
# @return {Integer}
def maximum_white_tiles(tiles, carpet_len)
    
end
```

### Scala

```scala
object Solution {
    def maximumWhiteTiles(tiles: Array[Array[Int]], carpetLen: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_white_tiles(tiles: Vec<Vec<i32>>, carpet_len: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-white-tiles tiles carpetLen)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_white_tiles(Tiles :: [[integer()]], CarpetLen :: integer()) -> integer().
maximum_white_tiles(Tiles, CarpetLen) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_white_tiles(tiles :: [[integer]], carpet_len :: integer) :: integer
  def maximum_white_tiles(tiles, carpet_len) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumWhiteTiles(tiles: Array<Array<Int64>>, carpetLen: Int64): Int64 {

    }
}
```

