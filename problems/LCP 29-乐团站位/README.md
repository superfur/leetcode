# LCP 29. 乐团站位

## 题目描述

某乐团的演出场地可视作 `num * num` 的二维矩阵 `grid`（左上角坐标为 `[0,0]`)，每个位置站有一位成员。乐团共有 `9` 种乐器，乐器编号为 `1~9`，每位成员持有 `1` 个乐器。

为保证声乐混合效果，成员站位规则为：自 `grid` 左上角开始顺时针螺旋形向内循环以 `1，2，...，9` 循环重复排列。例如当 num = `5` 时，站位如图所示

![image.png](https://pic.leetcode-cn.com/1616125411-WOblWH-image.png)


请返回位于场地坐标 [`Xpos`,`Ypos`] 的成员所持乐器编号。

**示例 1：**
>输入：`num = 3, Xpos = 0, Ypos = 2`
>
>输出：`3`
>
>解释：
![image.png](https://pic.leetcode-cn.com/1616125437-WUOwsu-image.png)


**示例 2：**
>输入：`num = 4, Xpos = 1, Ypos = 2`
>
>输出：`5`
>
>解释：
![image.png](https://pic.leetcode-cn.com/1616125453-IIDpxg-image.png)


**提示：**
- `1 <= num <= 10^9`
- `0 <= Xpos, Ypos < num`

## 难度

Medium

## 标签

- 数学

## 示例

```
3
0
2
4
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int orchestraLayout(int num, int xPos, int yPos) {

    }
};
```

### Java

```java
class Solution {
    public int orchestraLayout(int num, int xPos, int yPos) {

    }
}
```

### Python

```python
class Solution(object):
    def orchestraLayout(self, num, xPos, yPos):
        """
        :type num: int
        :type xPos: int
        :type yPos: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
```

### C

```c


int orchestraLayout(int num, int xPos, int yPos){

}
```

### C#

```csharp
public class Solution {
    public int OrchestraLayout(int num, int xPos, int yPos) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @param {number} xPos
 * @param {number} yPos
 * @return {number}
 */
var orchestraLayout = function(num, xPos, yPos) {

};
```

### TypeScript

```typescript
function orchestraLayout(num: number, xPos: number, yPos: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @param Integer $xPos
     * @param Integer $yPos
     * @return Integer
     */
    function orchestraLayout($num, $xPos, $yPos) {

    }
}
```

### Swift

```swift
class Solution {
    func orchestraLayout(_ num: Int, _ xPos: Int, _ yPos: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun orchestraLayout(num: Int, xPos: Int, yPos: Int): Int {

    }
}
```

### Go

```golang
func orchestraLayout(num int, xPos int, yPos int) int {

}
```

### Ruby

```ruby
# @param {Integer} num
# @param {Integer} x_pos
# @param {Integer} y_pos
# @return {Integer}
def orchestra_layout(num, x_pos, y_pos)

end
```

### Scala

```scala
object Solution {
    def orchestraLayout(num: Int, xPos: Int, yPos: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn orchestra_layout(num: i32, x_pos: i32, y_pos: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (orchestra-layout num xPos yPos)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)

  )
```

