# LCP 77. 符文储备

## 题目描述

远征队在出发前需要携带一些「符文」，作为后续的冒险储备。`runes[i]` 表示第 `i` 枚符文的魔力值。

他们将从中选取若干符文进行携带，并对这些符文进行重新排列，以确保任意相邻的两块符文之间的魔力值相差不超过 `1`。

请返回他们能够携带的符文 **最大数量**。

**示例 1：**
>输入：`runes = [1,3,5,4,1,7]`
>
>输出：`3`
>
>解释：最佳的选择方案为[3,5,4]
>将其排列为 [3,4,5] 后，任意相邻的两块符文魔力值均不超过 `1`，携带数量为 `3`
>其他满足条件的方案为 [1,1] 和 [7]，数量均小于 3。
>因此返回可携带的最大数量 `3`。

**示例 2：**
>输入：`runes = [1,1,3,3,2,4]`
>
>输出：`6`
>
>解释：排列为 [1,1,2,3,3,4]，可携带所有的符文

**提示：**
- `1 <= runes.length <= 10^4`
- `0 <= runes[i] <= 10^4`


## 难度

Easy

## 示例

```
[1,3,5,4,1,7]
[1,1,3,3,2,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int runeReserve(vector<int>& runes) {

    }
};
```

### Java

```java
class Solution {
    public int runeReserve(int[] runes) {

    }
}
```

### Python

```python
class Solution(object):
    def runeReserve(self, runes):
        """
        :type runes: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def runeReserve(self, runes: List[int]) -> int:
```

### C

```c
int runeReserve(int* runes, int runesSize){

}
```

### C#

```csharp
public class Solution {
    public int RuneReserve(int[] runes) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} runes
 * @return {number}
 */
var runeReserve = function(runes) {

};
```

### TypeScript

```typescript
function runeReserve(runes: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $runes
     * @return Integer
     */
    function runeReserve($runes) {

    }
}
```

### Swift

```swift
class Solution {
    func runeReserve(_ runes: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun runeReserve(runes: IntArray): Int {

    }
}
```

### Dart

```dart
class Solution {
  int runeReserve(List<int> runes) {

  }
}
```

### Go

```golang
func runeReserve(runes []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} runes
# @return {Integer}
def rune_reserve(runes)

end
```

### Scala

```scala
object Solution {
    def runeReserve(runes: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn rune_reserve(runes: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (rune-reserve runes)
  (-> (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec rune_reserve(Runes :: [integer()]) -> integer().
rune_reserve(Runes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec rune_reserve(runes :: [integer]) :: integer
  def rune_reserve(runes) do

  end
end
```

