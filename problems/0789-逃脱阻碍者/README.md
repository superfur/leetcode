# 789. 逃脱阻碍者

## 题目描述

<p>你在进行一个简化版的吃豆人游戏。你从 <code>[0, 0]</code> 点开始出发，你的目的地是&nbsp;<code>target = [x<sub>target</sub>, y<sub>target</sub>]</code> 。地图上有一些阻碍者，以数组 <code>ghosts</code> 给出，第 <code>i</code> 个阻碍者从&nbsp;<code>ghosts[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;出发。所有输入均为 <strong>整数坐标</strong> 。</p>

<p>每一回合，你和阻碍者们可以同时向东，西，南，北四个方向移动，每次可以移动到距离原位置 <strong>1 个单位</strong> 的新位置。当然，也可以选择 <strong>不动</strong> 。所有动作 <strong>同时</strong> 发生。</p>

<p>如果你可以在任何阻碍者抓住你 <strong>之前</strong> 到达目的地（阻碍者可以采取任意行动方式），则被视为逃脱成功。如果你和阻碍者 <strong>同时</strong> 到达了一个位置（包括目的地）&nbsp;<strong>都不算</strong>&nbsp;是逃脱成功。</p>

<p>如果不管阻碍者怎么移动都可以成功逃脱时，输出 <code>true</code> ；否则，输出 <code>false</code> 。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>ghosts = [[1,0],[0,3]], target = [0,1]
<strong>输出：</strong>true
<strong>解释：</strong>你可以直接一步到达目的地 (0,1) ，在 (1, 0) 或者 (0, 3) 位置的阻碍者都不可能抓住你。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>ghosts = [[1,0]], target = [2,0]
<strong>输出：</strong>false
<strong>解释：</strong>你需要走到位于 (2, 0) 的目的地，但是在 (1, 0) 的阻碍者位于你和目的地之间。 
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>ghosts = [[2,0]], target = [1,0]
<strong>输出：</strong>false
<strong>解释：</strong>阻碍者可以和你同时达到目的地。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= ghosts.length &lt;= 100</code></li>
	<li><code>ghosts[i].length == 2</code></li>
	<li><code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li>同一位置可能有 <strong>多个阻碍者</strong> 。</li>
	<li><code>target.length == 2</code></li>
	<li><code>-10<sup>4</sup> &lt;= x<sub>target</sub>, y<sub>target</sub> &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学

## 示例

```
[[1,0],[0,3]]
[0,1]
[[1,0]]
[2,0]
[[2,0]]
[1,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean escapeGhosts(int[][] ghosts, int[] target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
```

### C

```c
bool escapeGhosts(int** ghosts, int ghostsSize, int* ghostsColSize, int* target, int targetSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool EscapeGhosts(int[][] ghosts, int[] target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} ghosts
 * @param {number[]} target
 * @return {boolean}
 */
var escapeGhosts = function(ghosts, target) {
    
};
```

### TypeScript

```typescript
function escapeGhosts(ghosts: number[][], target: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $ghosts
     * @param Integer[] $target
     * @return Boolean
     */
    function escapeGhosts($ghosts, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func escapeGhosts(_ ghosts: [[Int]], _ target: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun escapeGhosts(ghosts: Array<IntArray>, target: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool escapeGhosts(List<List<int>> ghosts, List<int> target) {
    
  }
}
```

### Go

```golang
func escapeGhosts(ghosts [][]int, target []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} ghosts
# @param {Integer[]} target
# @return {Boolean}
def escape_ghosts(ghosts, target)
    
end
```

### Scala

```scala
object Solution {
    def escapeGhosts(ghosts: Array[Array[Int]], target: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn escape_ghosts(ghosts: Vec<Vec<i32>>, target: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (escape-ghosts ghosts target)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec escape_ghosts(Ghosts :: [[integer()]], Target :: [integer()]) -> boolean().
escape_ghosts(Ghosts, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec escape_ghosts(ghosts :: [[integer]], target :: [integer]) :: boolean
  def escape_ghosts(ghosts, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func escapeGhosts(ghosts: Array<Array<Int64>>, target: Array<Int64>): Bool {

    }
}
```

