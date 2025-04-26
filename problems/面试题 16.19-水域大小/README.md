# 面试题 16.19. 水域大小

## 题目描述

<p>你有一个用于表示一片土地的整数矩阵<code>land</code>，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。</p>
<p><strong>示例：</strong></p>
<pre><strong>输入：</strong>
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
<strong>输出：</strong> [1,2,4]
</pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>0 < len(land) <= 1000</code></li>
<li><code>0 < len(land[i]) <= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 矩阵

## 提示

1. 如果给你一个指代水的单元格的行和列，你如何找到所有相邻的水域？
2. 尝试递归计算含水单元格的数目。
3. 你如何确保不会再次访问相同的单元格？考虑一下图上的广度优先搜索或深度优先搜索是如何工作的。
4. 你应该有一个算法，其在N×N矩阵上的时间复杂度是O(N2)。如果你的算法并非如此，请考虑是否错误地计算了时间复杂度，或者是否你的算法不是最优的。

## 示例

```
[[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> pondSizes(vector<vector<int>>& land) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] pondSizes(int[][] land) {
        
    }
}
```

### Python

```python
class Solution(object):
    def pondSizes(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pondSizes(int** land, int landSize, int* landColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] PondSizes(int[][] land) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} land
 * @return {number[]}
 */
var pondSizes = function(land) {
    
};
```

### TypeScript

```typescript
function pondSizes(land: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $land
     * @return Integer[]
     */
    function pondSizes($land) {
        
    }
}
```

### Swift

```swift
class Solution {
    func pondSizes(_ land: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun pondSizes(land: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> pondSizes(List<List<int>> land) {
    
  }
}
```

### Go

```golang
func pondSizes(land [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} land
# @return {Integer[]}
def pond_sizes(land)
    
end
```

### Scala

```scala
object Solution {
    def pondSizes(land: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn pond_sizes(land: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (pond-sizes land)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec pond_sizes(Land :: [[integer()]]) -> [integer()].
pond_sizes(Land) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec pond_sizes(land :: [[integer]]) :: [integer]
  def pond_sizes(land) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func pondSizes(land: Array<Array<Int64>>): Array<Int64> {

    }
}
```

