# LCP 49. 环形闯关游戏

## 题目描述

「力扣挑战赛」中有一个由 `N` 个关卡组成的**环形**闯关游戏，关卡编号为 `0`~`N-1`，编号 `0` 的关卡和编号 `N-1` 的关卡相邻。每个关卡均有积分要求，`challenge[i]` 表示挑战编号 `i` 的关卡最少需要拥有的积分。
![图片.png](https://pic.leetcode-cn.com/1630392170-ucncVS-%E5%9B%BE%E7%89%87.png){:width="240px"}


小扣想要挑战关卡，闯关具体规则如下：

- 初始小扣可以指定其中一个关卡为「开启」状态，其余关卡将处于「未开启」状态。
- 小扣可以挑战处于「开启」状态且**满足最少积分要求**的关卡，若小扣挑战该关卡前积分为 `score`，挑战结束后，积分将增长为 `score|challenge[i]`（即位运算中的 `"OR"` 运算）
- 在挑战某个关卡后，该关卡两侧相邻的关卡将会开启（若之前未开启）

请帮助小扣进行计算，初始最少需要多少积分，可以挑战 **环形闯关游戏** 的所有关卡。

**示例1：**

> 输入：`challenge = [5,4,6,2,7]`
>
> 输出：`4`
> 
> 解释： 初始选择编号 3 的关卡开启，积分为 4
>挑战编号 3 的关卡，积分变为 $4 | 2 = 6$，开启 2、4 处的关卡
>挑战编号 2 的关卡，积分变为 $6 | 6 = 6$，开启 1 处的关卡
>挑战编号 1 的关卡，积分变为 $6 | 4 = 6$，开启 0 处的关卡
>挑战编号 0 的关卡，积分变为 $6 | 5 = 7$
>挑战编号 4 的关卡，顺利完成全部的关卡


**示例2：**

> 输入：`challenge = [12,7,11,3,9]`
>
> 输出：`8`
>
> 解释： 初始选择编号 3 的关卡开启，积分为 8
>挑战编号 3 的关卡，积分变为 $8 | 3 = 11$，开启 2、4 处的关卡
>挑战编号 2 的关卡，积分变为 $11 | 11 = 11$，开启 1 处的关卡
>挑战编号 4 的关卡，积分变为 $11 | 9 = 11$，开启 0 处的关卡
>挑战编号 1 的关卡，积分变为 $11 | 7 = 15$
>挑战编号 0 的关卡，顺利完成全部的关卡

**示例3：**

> 输入：`challenge = [1,1,1]`
>
> 输出：`1`

**提示：** 
- `1 <= challenge.length <= 5*10^4`
- `1 <= challenge[i] <= 10^14`

## 难度

Hard

## 标签

- 位运算
- 并查集
- 数组
- 堆（优先队列）

## 示例

```
[5,4,6,2,7]
[1,17,1,19,1]
[12,7,11,3,9]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long ringGame(vector<long long>& challenge) {

    }
};
```

### Java

```java
class Solution {
    public long ringGame(long[] challenge) {

    }
}
```

### Python

```python
class Solution(object):
    def ringGame(self, challenge):
        """
        :type challenge: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def ringGame(self, challenge: List[int]) -> int:
```

### C

```c


long long ringGame(long long* challenge, int challengeSize){

}
```

### C#

```csharp
public class Solution {
    public long RingGame(long[] challenge) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {BigInt[]} challenge
 * @return {BigInt}
 */
var ringGame = function(challenge) {

};
```

### TypeScript

```typescript
function ringGame(challenge: BigInt[]): BigInt {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $challenge
     * @return Integer
     */
    function ringGame($challenge) {

    }
}
```

### Swift

```swift
class Solution {
    func ringGame(_ challenge: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun ringGame(challenge: LongArray): Long {

    }
}
```

### Go

```golang
func ringGame(challenge []int64) int64 {

}
```

### Ruby

```ruby
# @param {Integer[]} challenge
# @return {Integer}
def ring_game(challenge)

end
```

### Scala

```scala
object Solution {
    def ringGame(challenge: Array[Long]): Long = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn ring_game(challenge: Vec<i64>) -> i64 {

    }
}
```

### Racket

```racket
(define/contract (ring-game challenge)
  (-> (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec ring_game(Challenge :: [integer()]) -> integer().
ring_game(Challenge) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ring_game(challenge :: [integer]) :: integer
  def ring_game(challenge) do

  end
end
```

