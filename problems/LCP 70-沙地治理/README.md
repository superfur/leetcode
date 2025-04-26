# LCP 70. 沙地治理

## 题目描述

在力扣城的沙漠分会场展示了一种沙柳树，这种沙柳树能够将沙地转化为坚实的绿地。
展示的区域为正三角形，这片区域可以拆分为若干个子区域，每个子区域都是边长为 `1` 的小三角形，其中第 `i` 行有 `2i - 1` 个小三角形。

初始情况下，区域中的所有位置都为沙地，你需要指定一些子区域种植沙柳树成为绿地，以达到转化整片区域为绿地的最终目的，规则如下：
- 若两个子区域共用一条边，则视为相邻；
>如下图所示，(1,1)和(2,2)相邻，(3,2)和(3,3)相邻；(2,2)和(3,3)不相邻，因为它们没有共用边。
- 若至少有两片绿地与同一片沙地相邻，则这片沙地也会转化为绿地
- 转化为绿地的区域会影响其相邻的沙地
![image.png](https://pic.leetcode-cn.com/1662692397-VlvErS-image.png)

现要将一片边长为 `size` 的沙地全部转化为绿地，请找到任意一种初始指定 **最少** 数量子区域种植沙柳的方案，并返回所有初始种植沙柳树的绿地坐标。

**示例 1：**
>输入：`size = 3`
>输出：`[[1,1],[2,1],[2,3],[3,1],[3,5]]`
>解释：如下图所示，一种方案为：
>指定所示的 5 个子区域为绿地。
>相邻至少两片绿地的 (2,2)，(3,2) 和 (3,4) 演变为绿地。
>相邻两片绿地的 (3,3) 演变为绿地。
![image.png](https://pic.leetcode-cn.com/1662692503-ncjywh-image.png){:width=500px}


**示例 2：**
>输入：`size = 2`
>输出：`[[1,1],[2,1],[2,3]]`
>解释：如下图所示：
>指定所示的 3 个子区域为绿地。
>相邻三片绿地的 (2,2) 演变为绿地。
![image.png](https://pic.leetcode-cn.com/1662692507-mgFXRj-image.png){:width=276px}



**提示：**
- `1 <= size <= 1000`

## 难度

Hard

## 标签

- 数组
- 数学

## 示例

```
3
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> sandyLandManagement(int size) {

    }
};
```

### Java

```java
class Solution {
    public int[][] sandyLandManagement(int size) {

    }
}
```

### Python

```python
class Solution(object):
    def sandyLandManagement(self, size):
        """
        :type size: int
        :rtype: List[List[int]]
        """
```

### Python3

```python3
class Solution:
    def sandyLandManagement(self, size: int) -> List[List[int]]:
```

### C

```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** sandyLandManagement(int size, int* returnSize, int** returnColumnSizes){

}
```

### C#

```csharp
public class Solution {
    public int[][] SandyLandManagement(int size) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number} size
 * @return {number[][]}
 */
var sandyLandManagement = function(size) {

};
```

### TypeScript

```typescript
function sandyLandManagement(size: number): number[][] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $size
     * @return Integer[][]
     */
    function sandyLandManagement($size) {

    }
}
```

### Swift

```swift
class Solution {
    func sandyLandManagement(_ size: Int) -> [[Int]] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sandyLandManagement(size: Int): Array<IntArray> {

    }
}
```

### Go

```golang
func sandyLandManagement(size int) [][]int {

}
```

### Ruby

```ruby
# @param {Integer} size
# @return {Integer[][]}
def sandy_land_management(size)

end
```

### Scala

```scala
object Solution {
    def sandyLandManagement(size: Int): Array[Array[Int]] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn sandy_land_management(size: i32) -> Vec<Vec<i32>> {

    }
}
```

### Racket

```racket
(define/contract (sandy-land-management size)
  (-> exact-integer? (listof (listof exact-integer?)))

  )
```

### Erlang

```erlang
-spec sandy_land_management(Size :: integer()) -> [[integer()]].
sandy_land_management(Size) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sandy_land_management(size :: integer) :: [[integer]]
  def sandy_land_management(size) do

  end
end
```

