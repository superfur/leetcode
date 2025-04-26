# LCP 51. 烹饪料理

## 题目描述

欢迎各位勇者来到力扣城，城内设有烹饪锅供勇者制作料理，为自己恢复状态。

勇者背包内共有编号为 `0 ~ 4` 的五种食材，其中 `materials[j]` 表示第 `j` 种食材的数量。通过这些食材可以制作若干料理，`cookbooks[i][j]` 表示制作第 `i` 种料理需要第 `j` 种食材的数量，而 `attribute[i] = [x,y]` 表示第 `i` 道料理的美味度 `x` 和饱腹感 `y`。

在饱腹感不小于 `limit` 的情况下，请返回勇者可获得的最大美味度。如果无法满足饱腹感要求，则返回 `-1`。

**注意：**
- 每种料理只能制作一次。


**示例 1：**
>输入：`materials = [3,2,4,1,2]`
>`cookbooks = [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]]`
>`attribute = [[3,2],[2,4],[7,6]]`
>`limit = 5`
>
>输出：`7`
>
>解释：
>食材数量可以满足以下两种方案：
>方案一：制作料理 0 和料理 1，可获得饱腹感 2+4、美味度 3+2
>方案二：仅制作料理 2， 可饱腹感为 6、美味度为 7
>因此在满足饱腹感的要求下，可获得最高美味度 7

**示例 2：**
>输入：`materials = [10,10,10,10,10]`
>`cookbooks = [[1,1,1,1,1],[3,3,3,3,3],[10,10,10,10,10]]`
>`attribute = [[5,5],[6,6],[10,10]]`
>`limit = 1`
>
>输出：`11`
>
>解释：通过制作料理 0 和 1，可满足饱腹感，并获得最高美味度 11

**提示：**
+ `materials.length == 5`
+ `1 <= cookbooks.length == attribute.length <= 8`
+ `cookbooks[i].length == 5`
+ `attribute[i].length == 2`
+ `0 <= materials[i], cookbooks[i][j], attribute[i][j] <= 20`
+ `1 <= limit <= 100`


## 难度

Easy

## 标签

- 位运算
- 数组
- 回溯
- 枚举

## 示例

```
[3,2,4,1,2]
[[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]]
[[3,2],[2,4],[7,6]]
5
[10,10,10,10,10]
[[1,1,1,1,1],[3,3,3,3,3],[10,10,10,10,10]]
[[5,5],[6,6],[10,10]]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int perfectMenu(vector<int>& materials, vector<vector<int>>& cookbooks, vector<vector<int>>& attribute, int limit) {

    }
};
```

### Java

```java
class Solution {
    public int perfectMenu(int[] materials, int[][] cookbooks, int[][] attribute, int limit) {

    }
}
```

### Python

```python
class Solution(object):
    def perfectMenu(self, materials, cookbooks, attribute, limit):
        """
        :type materials: List[int]
        :type cookbooks: List[List[int]]
        :type attribute: List[List[int]]
        :type limit: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
```

### C

```c


int perfectMenu(int* materials, int materialsSize, int** cookbooks, int cookbooksSize, int* cookbooksColSize, int** attribute, int attributeSize, int* attributeColSize, int limit){

}
```

### C#

```csharp
public class Solution {
    public int PerfectMenu(int[] materials, int[][] cookbooks, int[][] attribute, int limit) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} materials
 * @param {number[][]} cookbooks
 * @param {number[][]} attribute
 * @param {number} limit
 * @return {number}
 */
var perfectMenu = function(materials, cookbooks, attribute, limit) {

};
```

### TypeScript

```typescript
function perfectMenu(materials: number[], cookbooks: number[][], attribute: number[][], limit: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $materials
     * @param Integer[][] $cookbooks
     * @param Integer[][] $attribute
     * @param Integer $limit
     * @return Integer
     */
    function perfectMenu($materials, $cookbooks, $attribute, $limit) {

    }
}
```

### Swift

```swift
class Solution {
    func perfectMenu(_ materials: [Int], _ cookbooks: [[Int]], _ attribute: [[Int]], _ limit: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun perfectMenu(materials: IntArray, cookbooks: Array<IntArray>, attribute: Array<IntArray>, limit: Int): Int {

    }
}
```

### Go

```golang
func perfectMenu(materials []int, cookbooks [][]int, attribute [][]int, limit int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} materials
# @param {Integer[][]} cookbooks
# @param {Integer[][]} attribute
# @param {Integer} limit
# @return {Integer}
def perfect_menu(materials, cookbooks, attribute, limit)

end
```

### Scala

```scala
object Solution {
    def perfectMenu(materials: Array[Int], cookbooks: Array[Array[Int]], attribute: Array[Array[Int]], limit: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn perfect_menu(materials: Vec<i32>, cookbooks: Vec<Vec<i32>>, attribute: Vec<Vec<i32>>, limit: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (perfect-menu materials cookbooks attribute limit)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer? exact-integer?)

  )
```

### Erlang

```erlang
-spec perfect_menu(Materials :: [integer()], Cookbooks :: [[integer()]], Attribute :: [[integer()]], Limit :: integer()) -> integer().
perfect_menu(Materials, Cookbooks, Attribute, Limit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec perfect_menu(materials :: [integer], cookbooks :: [[integer]], attribute :: [[integer]], limit :: integer) :: integer
  def perfect_menu(materials, cookbooks, attribute, limit) do

  end
end
```

