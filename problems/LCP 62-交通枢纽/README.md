# LCP 62. 交通枢纽

## 题目描述

为了缓解「力扣嘉年华」期间的人流压力，组委会在活动期间开设了一些交通专线。`path[i] = [a, b]` 表示有一条从地点 `a`通往地点 `b` 的 **单向** 交通专线。
若存在一个地点，满足以下要求，我们则称之为 **交通枢纽**：
- 所有地点（除自身外）均有一条 **单向** 专线 **直接** 通往该地点；
- 该地点不存在任何 **通往其他地点** 的单向专线。

请返回交通专线的 **交通枢纽**。若不存在，则返回 `-1`。

**注意：**
- 对于任意一个地点，至少被一条专线连通。

**示例 1：**
>输入：`path = [[0,1],[0,3],[1,3],[2,0],[2,3]]`
>
>输出：`3`
>
>解释：如下图所示：
> 地点 `0,1,2` 各有一条通往地点 `3` 的交通专线，
> 且地点 `3` 不存在任何**通往其他地点**的交通专线。
>![image.png](https://pic.leetcode-cn.com/1663902572-yOlUCr-image.png){:width=200px}


**示例 2：**
>输入：`path = [[0,3],[1,0],[1,3],[2,0],[3,0],[3,2]]`
>
>输出：`-1`
>
>解释：如下图所示：不存在满足 **交通枢纽** 的地点。
>![image.png](https://pic.leetcode-cn.com/1663902595-McsEkY-image.png){:width=200px}

**提示：**
- `1 <= path.length <= 1000`
- `0 <= path[i][0], path[i][1] <= 1000`
- `path[i][0]` 与 `path[i][1]` 不相等

## 难度

Medium

## 标签

- 图

## 示例

```
[[0,1],[0,3],[1,3],[2,0],[2,3]]
[[0,3],[1,0],[1,3],[2,0],[3,0],[3,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int transportationHub(vector<vector<int>>& path) {

    }
};
```

### Java

```java
class Solution {
    public int transportationHub(int[][] path) {

    }
}
```

### Python

```python
class Solution(object):
    def transportationHub(self, path):
        """
        :type path: List[List[int]]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def transportationHub(self, path: List[List[int]]) -> int:
```

### C

```c


int transportationHub(int** path, int pathSize, int* pathColSize){

}
```

### C#

```csharp
public class Solution {
    public int TransportationHub(int[][] path) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} path
 * @return {number}
 */
var transportationHub = function(path) {

};
```

### TypeScript

```typescript
function transportationHub(path: number[][]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $path
     * @return Integer
     */
    function transportationHub($path) {

    }
}
```

### Swift

```swift
class Solution {
    func transportationHub(_ path: [[Int]]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun transportationHub(path: Array<IntArray>): Int {

    }
}
```

### Dart

```dart
class Solution {
  int transportationHub(List<List<int>> path) {

  }
}
```

### Go

```golang
func transportationHub(path [][]int) int {

}
```

### Ruby

```ruby
# @param {Integer[][]} path
# @return {Integer}
def transportation_hub(path)

end
```

### Scala

```scala
object Solution {
    def transportationHub(path: Array[Array[Int]]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn transportation_hub(path: Vec<Vec<i32>>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (transportation-hub path)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

### Erlang

```erlang
-spec transportation_hub(Path :: [[integer()]]) -> integer().
transportation_hub(Path) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec transportation_hub(path :: [[integer]]) :: integer
  def transportation_hub(path) do

  end
end
```

