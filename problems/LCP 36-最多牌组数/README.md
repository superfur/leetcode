# LCP 36. 最多牌组数

## 题目描述

麻将的游戏规则中，共有两种方式凑成「一组牌」：
- 顺子：三张牌面数字连续的麻将，例如 [4,5,6]
- 刻子：三张牌面数字相同的麻将，例如 [10,10,10]

给定若干数字作为麻将牌的数值（记作一维数组 `tiles`），请返回所给 `tiles` 最多可组成的牌组数。

注意：凑成牌组时，每张牌仅能使用一次。

**示例 1：**
>输入：`tiles = [2,2,2,3,4]`
>
>输出：`1`
>
>解释：最多可以组合出 [2,2,2] 或者 [2,3,4] 其中一组牌。

**示例 2：**
>输入：`tiles = [2,2,2,3,4,1,3]`
>
>输出：`2`
>
>解释：最多可以组合出 [1,2,3] 与 [2,3,4] 两组牌。

**提示：**
- `1 <= tiles.length <= 10^5`
- `1 <= tiles[i] <= 10^9`

## 难度

Hard

## 标签

- 数组
- 动态规划
- 排序

## 示例

```
[2,2,2,3,4]
[2,2,2,3,4,1,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxGroupNumber(vector<int>& tiles) {

    }
};
```

### Java

```java
class Solution {
    public int maxGroupNumber(int[] tiles) {

    }
}
```

### Python

```python
class Solution(object):
    def maxGroupNumber(self, tiles):
        """
        :type tiles: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def maxGroupNumber(self, tiles: List[int]) -> int:
```

### C

```c


int maxGroupNumber(int* tiles, int tilesSize){

}
```

### C#

```csharp
public class Solution {
    public int MaxGroupNumber(int[] tiles) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} tiles
 * @return {number}
 */
var maxGroupNumber = function(tiles) {

};
```

### TypeScript

```typescript
function maxGroupNumber(tiles: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $tiles
     * @return Integer
     */
    function maxGroupNumber($tiles) {

    }
}
```

### Swift

```swift
class Solution {
    func maxGroupNumber(_ tiles: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxGroupNumber(tiles: IntArray): Int {

    }
}
```

### Go

```golang
func maxGroupNumber(tiles []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} tiles
# @return {Integer}
def max_group_number(tiles)

end
```

### Scala

```scala
object Solution {
    def maxGroupNumber(tiles: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_group_number(tiles: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (max-group-number tiles)
  (-> (listof exact-integer?) exact-integer?)

  )
```

