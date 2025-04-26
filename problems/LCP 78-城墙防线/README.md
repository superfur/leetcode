# LCP 78. 城墙防线

## 题目描述

在探险营地间，小扣意外发现了一片城墙遗迹，在探索期间，却不巧遇到迁徙中的兽群向他迎面冲来。情急之下小扣吹响了他的苍蓝笛，随着笛声响起，遗迹中的城墙逐渐发生了横向膨胀。
已知 `rampart[i] = [x,y]` 表示第 `i` 段城墙的初始所在区间。当城墙发生膨胀时，将遵循以下规则：
- 所有的城墙会同时膨胀相等的长度；
- 每个城墙可以向左、向右或向两个方向膨胀。

小扣为了确保自身的安全，需要在所有城墙均无重叠的情况下，让城墙尽可能的膨胀。请返回城墙可以膨胀的 **最大值** 。

**注意：**
- 初始情况下，所有城墙均不重叠，且 `rampart` 中的元素升序排列；
- 两侧的城墙可以向外无限膨胀。

**示例 1：**
>输入：`rampart = [[0,3],[4,5],[7,9]]`
>
>输出：`3`
>
>解释：如下图所示：
>`rampart[0]` 向左侧膨胀 3 个单位；
>`rampart[2]` 向右侧膨胀 3 个单位；
>`rampart[1]` 向左侧膨胀 1 个单位，向右膨胀 2 个单位。
>不存在膨胀更多的方案，返回 3。
![image.png](https://pic.leetcode.cn/1681717918-tWywrp-image.png){:width=750px}

**示例 2：**
>输入：`rampart = [[1,2],[5,8],[11,15],[18,25]]`
>
>输出：`4`

**提示：**
- `3 <= rampart.length <= 10^4`
- `rampart[i].length == 2`
- `0 <= rampart[i][0] < rampart[i][1] <= rampart[i+1][0] <= 10^8`

## 难度

Medium

## 示例

```
[[0,3],[4,5],[7,9]]
[[1,2],[5,8],[11,15],[18,25]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int rampartDefensiveLine(vector<vector<int>>& rampart) {

    }
};
```

### Java

```java
class Solution {
    public int rampartDefensiveLine(int[][] rampart) {

    }
}
```

### Python

```python
class Solution(object):
    def rampartDefensiveLine(self, rampart):
        """
        :type rampart: List[List[int]]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def rampartDefensiveLine(self, rampart: List[List[int]]) -> int:
```

### C

```c
int rampartDefensiveLine(int** rampart, int rampartSize, int* rampartColSize){

}
```

### C#

```csharp
public class Solution {
    public int RampartDefensiveLine(int[][] rampart) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} rampart
 * @return {number}
 */
var rampartDefensiveLine = function(rampart) {

};
```

### TypeScript

```typescript
function rampartDefensiveLine(rampart: number[][]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $rampart
     * @return Integer
     */
    function rampartDefensiveLine($rampart) {

    }
}
```

### Swift

```swift
class Solution {
    func rampartDefensiveLine(_ rampart: [[Int]]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rampartDefensiveLine(rampart: Array<IntArray>): Int {

    }
}
```

### Dart

```dart
class Solution {
  int rampartDefensiveLine(List<List<int>> rampart) {

  }
}
```

### Go

```golang
func rampartDefensiveLine(rampart [][]int) int {

}
```

### Ruby

```ruby
# @param {Integer[][]} rampart
# @return {Integer}
def rampart_defensive_line(rampart)

end
```

### Scala

```scala
object Solution {
    def rampartDefensiveLine(rampart: Array[Array[Int]]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn rampart_defensive_line(rampart: Vec<Vec<i32>>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (rampart-defensive-line rampart)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

### Erlang

```erlang
-spec rampart_defensive_line(Rampart :: [[integer()]]) -> integer().
rampart_defensive_line(Rampart) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec rampart_defensive_line(rampart :: [[integer]]) :: integer
  def rampart_defensive_line(rampart) do

  end
end
```

