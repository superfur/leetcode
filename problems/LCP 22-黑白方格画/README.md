# LCP 22. 黑白方格画

## 题目描述

小扣注意到秋日市集上有一个创作黑白方格画的摊位。摊主给每个顾客提供一个固定在墙上的白色画板，画板不能转动。画板上有 `n * n` 的网格。绘画规则为，小扣可以选择任意多行以及任意多列的格子涂成黑色（选择的整行、整列均需涂成黑色），所选行数、列数均可为 0。

小扣希望最终的成品上需要有 `k` 个黑色格子，请返回小扣共有多少种涂色方案。

注意：两个方案中任意一个相同位置的格子颜色不同，就视为不同的方案。

**示例 1：**
>输入：`n = 2, k = 2`
>
>输出：`4`
> 
>解释：一共有四种不同的方案：
>第一种方案：涂第一列；
>第二种方案：涂第二列；
>第三种方案：涂第一行；
>第四种方案：涂第二行。

**示例 2：**
>输入：`n = 2, k = 1`
> 
>输出：`0`
> 
>解释：不可行，因为第一次涂色至少会涂两个黑格。

**示例 3：**
>输入：`n = 2, k = 4`
> 
>输出：`1`
>
>解释：共有 2*2=4 个格子，仅有一种涂色方案。

**限制：**
- `1 <= n <= 6`
- `0 <= k <= n * n`




## 难度

Easy

## 标签

- 数学

## 示例

```
2
2
2
1
2
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int paintingPlan(int n, int k) {

    }
};
```

### Java

```java
class Solution {
    public int paintingPlan(int n, int k) {

    }
}
```

### Python

```python
class Solution(object):
    def paintingPlan(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
```

### C

```c


int paintingPlan(int n, int k){

}
```

### C#

```csharp
public class Solution {
    public int PaintingPlan(int n, int k) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var paintingPlan = function(n, k) {

};
```

### TypeScript

```typescript
function paintingPlan(n: number, k: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function paintingPlan($n, $k) {

    }
}
```

### Swift

```swift
class Solution {
    func paintingPlan(_ n: Int, _ k: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun paintingPlan(n: Int, k: Int): Int {

    }
}
```

### Go

```golang
func paintingPlan(n int, k int) int {

}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def painting_plan(n, k)

end
```

### Scala

```scala
object Solution {
    def paintingPlan(n: Int, k: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn painting_plan(n: i32, k: i32) -> i32 {

    }
}
```

