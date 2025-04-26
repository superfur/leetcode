# LCP 58. 积木拼接

## 题目描述

欢迎各位勇者来到力扣城，本次试炼主题为「积木拼接」。
勇者面前有 `6` 片积木（厚度均为 1），每片积木的形状记录于二维字符串数组 `shapes` 中，`shapes[i]` 表示第 `i` 片积木，其中 `1` 表示积木对应位置无空缺，`0` 表示积木对应位置有空缺。
例如 `["010","111","010"]` 对应积木形状为
![image.png](https://pic.leetcode-cn.com/1616125620-nXMCxX-image.png)

拼接积木的规则如下：
- 积木片可以旋转、翻面
- 积木片边缘必须完全吻合才能拼接在一起
- **每片积木片 `shapes[i]` 的中心点在拼接时必须处于正方体对应面的中心点**

例如 `3*3`、`4*4` 的积木片的中心点如图所示（红色点）：
![middle_img_v2_c2d91eb5-9beb-4c06-9726-f7dae149d86g.png](https://pic.leetcode-cn.com/1650509082-wObiEp-middle_img_v2_c2d91eb5-9beb-4c06-9726-f7dae149d86g.png){:height="150px"}


请返回这 6 片积木能否拼接成一个**严丝合缝的正方体**且每片积木正好对应正方体的一个面。

**注意：**
- 输入确保每片积木均无空心情况（即输入数据保证对于大小 `N*N` 的 `shapes[i]`，内部的 `(N-2)*(N-2)` 的区域必然均为 1）
- 输入确保每片积木的所有 `1` 位置均连通

**示例 1：**
>输入：`shapes = [["000","110","000"],["110","011","000"],["110","011","110"],["000","010","111"],["011","111","011"],["011","010","000"]]`
>
>输出：`true`
>
>解释：
![cube.gif](https://pic.leetcode-cn.com/1616125823-hkXAeN-cube.gif)

**示例 2：**
>输入：`shapes = [["101","111","000"],["000","010","111"],["010","011","000"],["010","111","010"],["101","111","010"],["000","010","011"]]`
>
>输出：`false`
>
>解释： 
>由于每片积木片的中心点在拼接时必须处于正方体对应面的中心点，积木片 `["010","011","000"]` 不能作为 `["100","110","000"]` 使用，因此无法构成正方体


**提示：**
- `shapes.length == 6`
- `shapes[i].length == shapes[j].length`
- `shapes[i].length == shapes[i][j].length`
- `3 <= shapes[i].length <= 10`







## 难度

Hard

## 标签

- 数组
- 回溯
- 矩阵

## 示例

```
[["000","110","000"],["110","011","000"],["110","011","110"],["000","010","111"],["011","111","011"],["011","010","000"]]
[["101","111","000"],["000","010","111"],["010","011","000"],["010","111","010"],["101","111","010"],["000","010","011"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool composeCube(vector<vector<string>>& shapes) {

    }
};
```

### Java

```java
class Solution {
    public boolean composeCube(String[][] shapes) {

    }
}
```

### Python

```python
class Solution(object):
    def composeCube(self, shapes):
        """
        :type shapes: List[List[str]]
        :rtype: bool
        """
```

### Python3

```python3
class Solution:
    def composeCube(self, shapes: List[List[str]]) -> bool:
```

### C

```c


bool composeCube(char*** shapes, int shapesSize, int* shapesColSize){

}
```

### C#

```csharp
public class Solution {
    public bool ComposeCube(string[][] shapes) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string[][]} shapes
 * @return {boolean}
 */
var composeCube = function(shapes) {

};
```

### TypeScript

```typescript
function composeCube(shapes: string[][]): boolean {

};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $shapes
     * @return Boolean
     */
    function composeCube($shapes) {

    }
}
```

### Swift

```swift
class Solution {
    func composeCube(_ shapes: [[String]]) -> Bool {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun composeCube(shapes: Array<Array<String>>): Boolean {

    }
}
```

### Go

```golang
func composeCube(shapes [][]string) bool {

}
```

### Ruby

```ruby
# @param {String[][]} shapes
# @return {Boolean}
def compose_cube(shapes)

end
```

### Scala

```scala
object Solution {
    def composeCube(shapes: Array[Array[String]]): Boolean = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn compose_cube(shapes: Vec<Vec<String>>) -> bool {

    }
}
```

### Racket

```racket
(define/contract (compose-cube shapes)
  (-> (listof (listof string?)) boolean?)

  )
```

### Erlang

```erlang
-spec compose_cube(Shapes :: [[unicode:unicode_binary()]]) -> boolean().
compose_cube(Shapes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec compose_cube(shapes :: [[String.t]]) :: boolean
  def compose_cube(shapes) do

  end
end
```

