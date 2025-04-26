# LCR 121. 寻找目标值 - 二维数组

## 题目描述

<p><code>m</code>*<code>n</code> 的二维数组 <code>plants</code> 记录了园林景观的植物排布情况，具有以下特性：</p>

<ul>
	<li>每行中，每棵植物的右侧相邻植物不矮于该植物；</li>
	<li>每列中，每棵植物的下侧相邻植物不矮于该植物。</li>
</ul>

<p>&nbsp;</p>

<p>请判断 <code>plants</code> 中是否存在目标高度值 <code>target</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>plants = [[2,3,6,8],[4,5,8,9],[5,9,10,12]], target = 8

<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>plants = [[1,3,5],[2,5,7]], target = 4

<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= m &lt;= 1000</code></li>
</ul>

<p>注意：本题与主站 240 题相同：<a href="https://leetcode-cn.com/problems/search-a-2d-matrix-ii/" rel="noopener noreferrer" target="_blank">https://leetcode-cn.com/problems/search-a-2d-matrix-ii/</a></p>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 分治
- 矩阵

## 示例

```
[[2,3,6,8],[4,5,8,9],[5,9,10,12]]
8
[[1,3,5],[2,5,7]]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool findTargetIn2DPlants(vector<vector<int>>& plants, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean findTargetIn2DPlants(int[][] plants, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findTargetIn2DPlants(self, plants, target):
        """
        :type plants: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        
```

### C

```c
bool findTargetIn2DPlants(int** plants, int plantsSize, int* plantsColSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public bool FindTargetIn2DPlants(int[][] plants, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} plants
 * @param {number} target
 * @return {boolean}
 */
var findTargetIn2DPlants = function(plants, target) {
    
};
```

### TypeScript

```typescript
function findTargetIn2DPlants(plants: number[][], target: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $plants
     * @param Integer $target
     * @return Boolean
     */
    function findTargetIn2DPlants($plants, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findTargetIn2DPlants(_ plants: [[Int]], _ target: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findTargetIn2DPlants(plants: Array<IntArray>, target: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool findTargetIn2DPlants(List<List<int>> plants, int target) {
    
  }
}
```

### Go

```golang
func findTargetIn2DPlants(plants [][]int, target int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} plants
# @param {Integer} target
# @return {Boolean}
def find_target_in2_d_plants(plants, target)
    
end
```

### Scala

```scala
object Solution {
    def findTargetIn2DPlants(plants: Array[Array[Int]], target: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_target_in2_d_plants(plants: Vec<Vec<i32>>, target: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (find-target-in2-d-plants plants target)
  (-> (listof (listof exact-integer?)) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec find_target_in2_d_plants(Plants :: [[integer()]], Target :: integer()) -> boolean().
find_target_in2_d_plants(Plants, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_target_in2_d_plants(plants :: [[integer]], target :: integer) :: boolean
  def find_target_in2_d_plants(plants, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findTargetIn2DPlants(plants: Array<Array<Int64>>, target: Int64): Bool {

    }
}
```

