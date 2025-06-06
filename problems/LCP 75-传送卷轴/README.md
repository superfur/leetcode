# LCP 75. 传送卷轴

## 题目描述

随着不断的深入，小扣来到了守护者之森寻找的魔法水晶。首先，他必须先通过守护者的考验。

考验的区域是一个正方形的迷宫，`maze[i][j]` 表示在迷宫 `i` 行 `j` 列的地形：
- 若为 `.` ，表示可以到达的空地；
- 若为 `#` ，表示不可到达的墙壁；
- 若为 `S` ，表示小扣的初始位置；
- 若为 `T` ，表示魔法水晶的位置。

小扣每次可以向 上、下、左、右 相邻的位置移动一格。而守护者拥有一份「传送魔法卷轴」，使用规则如下：
- 魔法需要在小扣位于 **空地** 时才能释放，发动后卷轴消失；；
- 发动后，小扣会被传送到水平或者竖直的镜像位置，且目标位置不得为墙壁(如下图所示)；
![image.png](https://pic.leetcode.cn/1681789509-wTekFu-image.png){:width=400px}

在使用卷轴后，小扣将被「附加负面效果」，因此小扣需要尽可能缩短传送后到达魔法水晶的距离。而守护者的目标是阻止小扣到达魔法水晶的位置；如果无法阻止，则尽可能 **增加** 小扣传送后到达魔法水晶的距离。
假设小扣和守护者都按最优策略行事，返回小扣需要在 「附加负面效果」的情况下 **最少** 移动多少次才能到达魔法水晶。如果无法到达，返回 `-1`。

**注意：**
- 守护者可以不使用卷轴；
- 传送后的镜像位置可能与原位置相同。

**示例 1：**
>输入：`maze = [".....","##S..","...#.","T.#..","###.."]`
>
>输出：`7`
>
>解释：如下图所示：
>守护者释放魔法的两个最佳的位置为 [2,0] 或 [3,1]：
>若小扣经过 [2,0]，守护者在该位置释放魔法，
>小扣被传送至 [2,4] 处且加上负面效果，此时小扣还需要移动 7 次才能到达魔法水晶；
>若小扣经过 [3,1]，守护者在该位置释放魔法，
>小扣被传送至 [3,3] 处且加上负面效果，此时小扣还需要移动 9 次才能到达魔法水晶；
>因此小扣负面效果下最少需要移动 7 次才能到达魔法水晶。
![image.png](https://pic.leetcode.cn/1681714676-gksEMT-image.png){:width=300px}


**示例 2：**
>输入：`maze = [".#..","..##",".#S.",".#.T"]`
>
>输出：`-1`
>
>解释：如下图所示。
>若小扣向下移动至 [3,2]，守护者使其传送至 [0,2]，小扣将无法到达魔法水晶；
>若小扣向右移动至 [2,3]，守护者使其传送至 [2,0]，小扣将无法到达魔法水晶；
![image.png](https://pic.leetcode.cn/1681714693-LsxKAh-image.png){:width=300px}


**示例 3：**
>输入：`maze = ["S###.","..###","#..##","##..#","###.T"]`
>
>输出：`5`
>
>解释：如下图所示：
>守护者需要小扣在空地才能释放，因此初始无法将其从 [0,0] 传送至 [0,4];
>当小扣移动至 [2,1] 时，释放卷轴将其传送至水平方向的镜像位置 [2,1]（为原位置）
>而后小扣需要移动 5 次到达魔法水晶
![image.png](https://pic.leetcode.cn/1681800985-KrSdru-image.png){:width=300px}

**提示：**
- `4 <= maze.length == maze[i].length <= 200`
- `maze[i][j]` 仅包含 `"."`、`"#"`、`"S"`、`"T"`

## 难度

Hard

## 示例

```
[".....","##S..","...#.","T.#..","###.."]
[".#..","..##",".#S.",".#.T"]
["S###.","..###","#..##","##..#","###.T"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int challengeOfTheKeeper(vector<string>& maze) {

    }
};
```

### Java

```java
class Solution {
    public int challengeOfTheKeeper(String[] maze) {

    }
}
```

### Python

```python
class Solution(object):
    def challengeOfTheKeeper(self, maze):
        """
        :type maze: List[str]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def challengeOfTheKeeper(self, maze: List[str]) -> int:
```

### C

```c
int challengeOfTheKeeper(char** maze, int mazeSize){

}
```

### C#

```csharp
public class Solution {
    public int ChallengeOfTheKeeper(string[] maze) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} maze
 * @return {number}
 */
var challengeOfTheKeeper = function(maze) {

};
```

### TypeScript

```typescript
function challengeOfTheKeeper(maze: string[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $maze
     * @return Integer
     */
    function challengeOfTheKeeper($maze) {

    }
}
```

### Swift

```swift
class Solution {
    func challengeOfTheKeeper(_ maze: [String]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun challengeOfTheKeeper(maze: Array<String>): Int {

    }
}
```

### Dart

```dart
class Solution {
  int challengeOfTheKeeper(List<String> maze) {

  }
}
```

### Go

```golang
func challengeOfTheKeeper(maze []string) int {

}
```

### Ruby

```ruby
# @param {String[]} maze
# @return {Integer}
def challenge_of_the_keeper(maze)

end
```

### Scala

```scala
object Solution {
    def challengeOfTheKeeper(maze: Array[String]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn challenge_of_the_keeper(maze: Vec<String>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (challenge-of-the-keeper maze)
  (-> (listof string?) exact-integer?)

  )
```

### Erlang

```erlang
-spec challenge_of_the_keeper(Maze :: [unicode:unicode_binary()]) -> integer().
challenge_of_the_keeper(Maze) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec challenge_of_the_keeper(maze :: [String.t]) :: integer
  def challenge_of_the_keeper(maze) do

  end
end
```

