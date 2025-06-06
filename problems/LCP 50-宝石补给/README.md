# LCP 50. 宝石补给

## 题目描述

欢迎各位勇者来到力扣新手村，在开始试炼之前，请各位勇者先进行「宝石补给」。

每位勇者初始都拥有一些能量宝石， `gem[i]` 表示第 `i` 位勇者的宝石数量。现在这些勇者们进行了一系列的赠送，`operations[j] = [x, y]` 表示在第 `j` 次的赠送中 第 `x` 位勇者将自己一半的宝石（需向下取整）赠送给第 `y` 位勇者。

在完成所有的赠送后，请找到拥有**最多**宝石的勇者和拥有**最少**宝石的勇者，并返回他们二者的宝石数量**之差**。

**注意：**
- 赠送将按顺序逐步进行。

**示例 1：**
>输入：`gem = [3,1,2], operations = [[0,2],[2,1],[2,0]]`
>
>输出：`2`
>
>解释：
>第 1 次操作，勇者 `0` 将一半的宝石赠送给勇者 `2`， `gem = [2,1,3]`
>第 2 次操作，勇者 `2` 将一半的宝石赠送给勇者 `1`， `gem = [2,2,2]`
>第 3 次操作，勇者 `2` 将一半的宝石赠送给勇者 `0`， `gem = [3,2,1]`
>返回 3 - 1 = 2

**示例 2：**
>输入：`gem = [100,0,50,100], operations = [[0,2],[0,1],[3,0],[3,0]]`
>
>输出：`75`
>
>解释：
>第 1 次操作，勇者 `0` 将一半的宝石赠送给勇者 `2`， `gem = [50,0,100,100]`
>第 2 次操作，勇者 `0` 将一半的宝石赠送给勇者 `1`， `gem = [25,25,100,100]`
>第 3 次操作，勇者 `3` 将一半的宝石赠送给勇者 `0`， `gem = [75,25,100,50]`
>第 4 次操作，勇者 `3` 将一半的宝石赠送给勇者 `0`， `gem = [100,25,100,25]`
>返回 100 - 25 = 75

**示例 3：**
>输入：`gem = [0,0,0,0], operations = [[1,2],[3,1],[1,2]]`
>
>输出：`0`

**提示：**
- `2 <= gem.length <= 10^3`
- `0 <= gem[i] <= 10^3`
- `0 <= operations.length <= 10^4`
- `operations[i].length == 2`
- `0 <= operations[i][0], operations[i][1] < gem.length`

## 难度

Easy

## 标签

- 数组
- 模拟

## 示例

```
[3,1,2]
[[0,2],[2,1],[2,0]]
[100,0,50,100]
[[0,2],[0,1],[3,0],[3,0]]
[0,0,0,0]
[[1,2],[3,1],[1,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int giveGem(vector<int>& gem, vector<vector<int>>& operations) {

    }
};
```

### Java

```java
class Solution {
    public int giveGem(int[] gem, int[][] operations) {

    }
}
```

### Python

```python
class Solution(object):
    def giveGem(self, gem, operations):
        """
        :type gem: List[int]
        :type operations: List[List[int]]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
```

### C

```c


int giveGem(int* gem, int gemSize, int** operations, int operationsSize, int* operationsColSize){

}
```

### C#

```csharp
public class Solution {
    public int GiveGem(int[] gem, int[][] operations) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} gem
 * @param {number[][]} operations
 * @return {number}
 */
var giveGem = function(gem, operations) {

};
```

### TypeScript

```typescript
function giveGem(gem: number[], operations: number[][]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $gem
     * @param Integer[][] $operations
     * @return Integer
     */
    function giveGem($gem, $operations) {

    }
}
```

### Swift

```swift
class Solution {
    func giveGem(_ gem: [Int], _ operations: [[Int]]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun giveGem(gem: IntArray, operations: Array<IntArray>): Int {

    }
}
```

### Go

```golang
func giveGem(gem []int, operations [][]int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} gem
# @param {Integer[][]} operations
# @return {Integer}
def give_gem(gem, operations)

end
```

### Scala

```scala
object Solution {
    def giveGem(gem: Array[Int], operations: Array[Array[Int]]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn give_gem(gem: Vec<i32>, operations: Vec<Vec<i32>>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (give-gem gem operations)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)

  )
```

### Erlang

```erlang
-spec give_gem(Gem :: [integer()], Operations :: [[integer()]]) -> integer().
give_gem(Gem, Operations) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec give_gem(gem :: [integer], operations :: [[integer]]) :: integer
  def give_gem(gem, operations) do

  end
end
```

