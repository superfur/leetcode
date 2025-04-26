# LCP 76. 魔法棋盘

## 题目描述

在大小为 `n * m` 的棋盘中，有两种不同的棋子：黑色，红色。当两颗颜色不同的棋子同时满足以下两种情况时，将会产生魔法共鸣：
- 两颗异色棋子在同一行或者同一列
- 两颗异色棋子之间恰好只有一颗棋子
    > 注：异色棋子之间可以有空位

由于棋盘上被施加了魔法禁制，棋盘上的部分格子变成问号。`chessboard[i][j]` 表示棋盘第 `i` 行 `j` 列的状态：
- 若为 `.` ，表示当前格子确定为空
- 若为 `B` ，表示当前格子确定为 黑棋
- 若为 `R` ，表示当前格子确定为 红棋
- 若为 `?` ，表示当前格子待定

现在，探险家小扣的任务是确定所有问号位置的状态（留空/放黑棋/放红棋），使最终的棋盘上，任意两颗棋子间都 **无法** 产生共鸣。请返回可以满足上述条件的放置方案数量。

**示例1：**
> 输入：`n = 3, m = 3, chessboard = ["..R","..B","?R?"]`
>
> 输出：`5`
>
> 解释：给定的棋盘如图：
>![image.png](https://pic.leetcode.cn/1681714583-unbRox-image.png){:height=150px}
> 所有符合题意的最终局面如图：
>![image.png](https://pic.leetcode.cn/1681714596-beaOHK-image.png){:height=150px}

**示例2：**
> 输入：`n = 3, m = 3, chessboard = ["?R?","B?B","?R?"]`
>
> 输出：`105`

**提示：**
- `n == chessboard.length`
- `m == chessboard[i].length`
- `1 <= n*m <= 30`
- `chessboard` 中仅包含 `"."、"B"、"R"、"?"`

## 难度

Hard

## 示例

```
3
3
["..R","..B","?R?"]
3
3
["?R?","B?B","?R?"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long getSchemeCount(int n, int m, vector<string>& chessboard) {

    }
};
```

### Java

```java
class Solution {
    public long getSchemeCount(int n, int m, String[] chessboard) {

    }
}
```

### Python

```python
class Solution(object):
    def getSchemeCount(self, n, m, chessboard):
        """
        :type n: int
        :type m: int
        :type chessboard: List[str]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def getSchemeCount(self, n: int, m: int, chessboard: List[str]) -> int:
```

### C

```c
long long getSchemeCount(int n, int m, char** chessboard, int chessboardSize){

}
```

### C#

```csharp
public class Solution {
    public long GetSchemeCount(int n, int m, string[] chessboard) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} m
 * @param {string[]} chessboard
 * @return {number}
 */
var getSchemeCount = function(n, m, chessboard) {

};
```

### TypeScript

```typescript
function getSchemeCount(n: number, m: number, chessboard: string[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @param String[] $chessboard
     * @return Integer
     */
    function getSchemeCount($n, $m, $chessboard) {

    }
}
```

### Swift

```swift
class Solution {
    func getSchemeCount(_ n: Int, _ m: Int, _ chessboard: [String]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getSchemeCount(n: Int, m: Int, chessboard: Array<String>): Long {

    }
}
```

### Dart

```dart
class Solution {
  int getSchemeCount(int n, int m, List<String> chessboard) {

  }
}
```

### Go

```golang
func getSchemeCount(n int, m int, chessboard []string) int64 {

}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} m
# @param {String[]} chessboard
# @return {Integer}
def get_scheme_count(n, m, chessboard)

end
```

### Scala

```scala
object Solution {
    def getSchemeCount(n: Int, m: Int, chessboard: Array[String]): Long = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_scheme_count(n: i32, m: i32, chessboard: Vec<String>) -> i64 {

    }
}
```

### Racket

```racket
(define/contract (get-scheme-count n m chessboard)
  (-> exact-integer? exact-integer? (listof string?) exact-integer?)

  )
```

### Erlang

```erlang
-spec get_scheme_count(N :: integer(), M :: integer(), Chessboard :: [unicode:unicode_binary()]) -> integer().
get_scheme_count(N, M, Chessboard) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_scheme_count(n :: integer, m :: integer, chessboard :: [String.t]) :: integer
  def get_scheme_count(n, m, chessboard) do

  end
end
```

