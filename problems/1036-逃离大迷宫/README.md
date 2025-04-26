# 1036. 逃离大迷宫

## 题目描述

<p>在一个 10<sup>6</sup> x 10<sup>6</sup> 的网格中，每个网格上方格的坐标为 <code>(x, y)</code> 。</p>

<p>现在从源方格 <code>source = [s<sub>x</sub>, s<sub>y</sub>]</code> 开始出发，意图赶往目标方格 <code>target = [t<sub>x</sub>, t<sub>y</sub>]</code> 。数组 <code>blocked</code> 是封锁的方格列表，其中每个 <code>blocked[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 表示坐标为 <code>(x<sub>i</sub>, y<sub>i</sub>)</code> 的方格是禁止通行的。</p>

<p>每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 <strong>不</strong> 在给出的封锁列表 <code>blocked</code> 上。同时，不允许走出网格。</p>

<p>只有在可以通过一系列的移动从源方格 <code>source</code> 到达目标方格 <code>target</code> 时才返回 <code>true</code>。否则，返回 <code>false</code>。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
<strong>输出：</strong>false
<strong>解释：</strong>
从源方格无法到达目标方格，因为我们无法在网格中移动。
无法向北或者向东移动是因为方格禁止通行。
无法向南或者向西移动是因为不能走出网格。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>blocked = [], source = [0,0], target = [999999,999999]
<strong>输出：</strong>true
<strong>解释：</strong>
因为没有方格被封锁，所以一定可以到达目标方格。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= blocked.length <= 200</code></li>
	<li><code>blocked[i].length == 2</code></li>
	<li><code>0 <= x<sub>i</sub>, y<sub>i</sub> < 10<sup>6</sup></code></li>
	<li><code>source.length == target.length == 2</code></li>
	<li><code>0 <= s<sub>x</sub>, s<sub>y</sub>, t<sub>x</sub>, t<sub>y</sub> < 10<sup>6</sup></code></li>
	<li><code>source != target</code></li>
	<li>题目数据保证 <code>source</code> 和 <code>target</code> 不在封锁列表内</li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 数组
- 哈希表

## 提示

1. If we become stuck, there's either a loop around the source or around the target.
2. If there is a loop around say, the source, what is the maximum number of squares it can have?

## 示例

```
[[0,1],[1,0]]
[0,0]
[0,2]
[]
[0,0]
[999999,999999]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isEscapePossible(vector<vector<int>>& blocked, vector<int>& source, vector<int>& target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isEscapePossible(int[][] blocked, int[] source, int[] target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
```

### C

```c
bool isEscapePossible(int** blocked, int blockedSize, int* blockedColSize, int* source, int sourceSize, int* target, int targetSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsEscapePossible(int[][] blocked, int[] source, int[] target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} blocked
 * @param {number[]} source
 * @param {number[]} target
 * @return {boolean}
 */
var isEscapePossible = function(blocked, source, target) {
    
};
```

### TypeScript

```typescript
function isEscapePossible(blocked: number[][], source: number[], target: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $blocked
     * @param Integer[] $source
     * @param Integer[] $target
     * @return Boolean
     */
    function isEscapePossible($blocked, $source, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isEscapePossible(_ blocked: [[Int]], _ source: [Int], _ target: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isEscapePossible(blocked: Array<IntArray>, source: IntArray, target: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isEscapePossible(List<List<int>> blocked, List<int> source, List<int> target) {
    
  }
}
```

### Go

```golang
func isEscapePossible(blocked [][]int, source []int, target []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} blocked
# @param {Integer[]} source
# @param {Integer[]} target
# @return {Boolean}
def is_escape_possible(blocked, source, target)
    
end
```

### Scala

```scala
object Solution {
    def isEscapePossible(blocked: Array[Array[Int]], source: Array[Int], target: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_escape_possible(blocked: Vec<Vec<i32>>, source: Vec<i32>, target: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-escape-possible blocked source target)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec is_escape_possible(Blocked :: [[integer()]], Source :: [integer()], Target :: [integer()]) -> boolean().
is_escape_possible(Blocked, Source, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_escape_possible(blocked :: [[integer]], source :: [integer], target :: [integer]) :: boolean
  def is_escape_possible(blocked, source, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isEscapePossible(blocked: Array<Array<Int64>>, source: Array<Int64>, target: Array<Int64>): Bool {

    }
}
```

