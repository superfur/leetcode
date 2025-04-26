# 947. 移除最多的同行或同列石头

## 题目描述

<p><code>n</code> 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。</p>

<p>如果一块石头的 <strong>同行或者同列</strong> 上有其他石头存在，那么就可以移除这块石头。</p>

<p>给你一个长度为 <code>n</code> 的数组 <code>stones</code> ，其中 <code>stones[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 表示第 <code>i</code> 块石头的位置，返回 <strong>可以移除的石子</strong> 的最大数量。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
<strong>输出：</strong>5
<strong>解释：</strong>一种移除 5 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
<strong>输出：</strong>3
<strong>解释：</strong>一种移除 3 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>stones = [[0,0]]
<strong>输出：</strong>0
<strong>解释：</strong>[0,0] 是平面上唯一一块石头，所以不可以移除它。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= stones.length <= 1000</code></li>
	<li><code>0 <= x<sub>i</sub>, y<sub>i</sub> <= 10<sup>4</sup></code></li>
	<li>不会有两块石头放在同一个坐标点上</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 并查集
- 图
- 哈希表

## 示例

```
[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
[[0,0],[0,2],[1,1],[2,0],[2,2]]
[[0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        
    }
};
```

### Java

```java
class Solution {
    public int removeStones(int[][] stones) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
```

### C

```c
int removeStones(int** stones, int stonesSize, int* stonesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int RemoveStones(int[][] stones) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} stones
 * @return {number}
 */
var removeStones = function(stones) {
    
};
```

### TypeScript

```typescript
function removeStones(stones: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $stones
     * @return Integer
     */
    function removeStones($stones) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeStones(_ stones: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeStones(stones: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int removeStones(List<List<int>> stones) {
    
  }
}
```

### Go

```golang
func removeStones(stones [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} stones
# @return {Integer}
def remove_stones(stones)
    
end
```

### Scala

```scala
object Solution {
    def removeStones(stones: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_stones(stones: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (remove-stones stones)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec remove_stones(Stones :: [[integer()]]) -> integer().
remove_stones(Stones) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_stones(stones :: [[integer]]) :: integer
  def remove_stones(stones) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeStones(stones: Array<Array<Int64>>): Int64 {

    }
}
```

