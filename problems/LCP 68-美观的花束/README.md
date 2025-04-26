# LCP 68. 美观的花束

## 题目描述

力扣嘉年华的花店中从左至右摆放了一排鲜花，记录于整型一维矩阵 `flowers` 中每个数字表示该位置所种鲜花的品种编号。你可以选择一段区间的鲜花做成插花，且不能丢弃。
在你选择的插花中，如果每一品种的鲜花数量都不超过 `cnt` 朵，那么我们认为这束插花是 「美观的」。
> - 例如：`[5,5,5,6,6]` 中品种为 `5` 的花有 `3` 朵， 品种为 `6` 的花有 `2` 朵，**每一品种** 的数量均不超过 `3`

请返回在这一排鲜花中，共有多少种可选择的区间，使得插花是「美观的」。

**注意：**
- 答案需要以 `1e9 + 7 (1000000007)` 为底取模，如：计算初始结果为：`1000000008`，请返回 `1`

**示例 1：**
>输入：`flowers = [1,2,3,2], cnt = 1`
>
>输出：`8`
>
>解释：相同的鲜花不超过 `1` 朵，共有 `8` 种花束是美观的；
>长度为 `1` 的区间 `[1]、[2]、[3]、[2]` 均满足条件，共 `4` 种可选择区间
>长度为 `2` 的区间 `[1,2]、[2,3]、[3,2]` 均满足条件，共 `3` 种可选择区间
>长度为 `3` 的区间 `[1,2,3]` 满足条件，共 `1` 种可选择区间。
>区间 `[2,3,2],[1,2,3,2]` 都包含了 `2` 朵鲜花 `2` ，不满足条件。
>返回总数 `4+3+1 = 8`

**示例 2：**
>输入：`flowers = [5,3,3,3], cnt = 2`
>
>输出：`8`

**提示：**
- `1 <= flowers.length <= 10^5`
- `1 <= flowers[i] <= 10^5`
- `1 <= cnt <= 10^5`

## 难度

Medium

## 标签

- 数组
- 滑动窗口

## 示例

```
[1,2,3,2]
1
[5,3,3,3]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int beautifulBouquet(vector<int>& flowers, int cnt) {

    }
};
```

### Java

```java
class Solution {
    public int beautifulBouquet(int[] flowers, int cnt) {

    }
}
```

### Python

```python
class Solution(object):
    def beautifulBouquet(self, flowers, cnt):
        """
        :type flowers: List[int]
        :type cnt: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
```

### C

```c


int beautifulBouquet(int* flowers, int flowersSize, int cnt){

}
```

### C#

```csharp
public class Solution {
    public int BeautifulBouquet(int[] flowers, int cnt) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} flowers
 * @param {number} cnt
 * @return {number}
 */
var beautifulBouquet = function(flowers, cnt) {

};
```

### TypeScript

```typescript
function beautifulBouquet(flowers: number[], cnt: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $flowers
     * @param Integer $cnt
     * @return Integer
     */
    function beautifulBouquet($flowers, $cnt) {

    }
}
```

### Swift

```swift
class Solution {
    func beautifulBouquet(_ flowers: [Int], _ cnt: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun beautifulBouquet(flowers: IntArray, cnt: Int): Int {

    }
}
```

### Go

```golang
func beautifulBouquet(flowers []int, cnt int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} flowers
# @param {Integer} cnt
# @return {Integer}
def beautiful_bouquet(flowers, cnt)

end
```

### Scala

```scala
object Solution {
    def beautifulBouquet(flowers: Array[Int], cnt: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn beautiful_bouquet(flowers: Vec<i32>, cnt: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (beautiful-bouquet flowers cnt)
  (-> (listof exact-integer?) exact-integer? exact-integer?)

  )
```

### Erlang

```erlang
-spec beautiful_bouquet(Flowers :: [integer()], Cnt :: integer()) -> integer().
beautiful_bouquet(Flowers, Cnt) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec beautiful_bouquet(flowers :: [integer], cnt :: integer) :: integer
  def beautiful_bouquet(flowers, cnt) do

  end
end
```

