# LCP 37. 最小矩形面积

## 题目描述

二维平面上有 $N$ 条直线，形式为 `y = kx + b`，其中 `k`、`b`为整数 且 `k > 0`。所有直线以 `[k,b]` 的形式存于二维数组 `lines` 中，不存在重合的两条直线。两两直线之间可能存在一个交点，最多会有 $C_N^2$ 个交点。我们用一个平行于坐标轴的矩形覆盖所有的交点，请问这个矩形最小面积是多少。若直线之间无交点、仅有一个交点或所有交点均在同一条平行坐标轴的直线上，则返回0。

注意：返回结果是浮点数，与标准答案 **绝对误差或相对误差** 在 10^-4 以内的结果都被视为正确结果


**示例 1：**
> 输入：`lines = [[2,3],[3,0],[4,1]]`
>
> 输出：`48.00000`
>
> 解释：三条直线的三个交点为 (3, 9) (1, 5) 和 (-1, -3)。最小覆盖矩形左下角为 (-1, -3) 右上角为 (3,9)，面积为 48


**示例 2：**
> 输入：`lines = [[1,1],[2,3]]`
>
> 输出：`0.00000`
>
> 解释：仅有一个交点 (-2，-1）


**限制：**
+ `1 <= lines.length <= 10^5 且 lines[i].length == 2`
+ `1 <= lines[0] <= 10000`
+ `-10000 <= lines[1] <= 10000`
+ `与标准答案绝对误差或相对误差在 10^-4 以内的结果都被视为正确结果`

## 难度

Hard

## 标签

- 贪心
- 几何
- 数组
- 数学
- 组合数学
- 排序

## 示例

```
[[2,3],[3,0],[4,1]]
[[1,1],[2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double minRecSize(vector<vector<int>>& lines) {

    }
};
```

### Java

```java
class Solution {
    public double minRecSize(int[][] lines) {

    }
}
```

### Python

```python
class Solution(object):
    def minRecSize(self, lines):
        """
        :type lines: List[List[int]]
        :rtype: float
        """
```

### Python3

```python3
class Solution:
    def minRecSize(self, lines: List[List[int]]) -> float:
```

### C

```c


double minRecSize(int** lines, int linesSize, int* linesColSize){

}

```

### C#

```csharp
public class Solution {
    public double MinRecSize(int[][] lines) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} lines
 * @return {number}
 */
var minRecSize = function(lines) {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $lines
     * @return Float
     */
    function minRecSize($lines) {

    }
}
```

### Swift

```swift
class Solution {
    func minRecSize(_ lines: [[Int]]) -> Double {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minRecSize(lines: Array<IntArray>): Double {

    }
}
```

### Go

```golang
func minRecSize(lines [][]int) float64 {

}
```

### Ruby

```ruby
# @param {Integer[][]} lines
# @return {Float}
def min_rec_size(lines)

end
```

### Scala

```scala
object Solution {
    def minRecSize(lines: Array[Array[Int]]): Double = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_rec_size(lines: Vec<Vec<i32>>) -> f64 {

    }
}
```

