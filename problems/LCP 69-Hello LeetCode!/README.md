# LCP 69. Hello LeetCode!

## 题目描述

力扣嘉年华同样准备了纪念品展位，参观者只需要集齐 `helloleetcode` 的 `13` 张字母卡片即可获得力扣纪念章。

在展位上有一些由字母卡片拼成的单词，`words[i][j]` 表示第 `i` 个单词的第 `j` 个字母。

你可以从这些单词中取出一些卡片，但每次拿取卡片都需要消耗游戏代币，规则如下：

- 从一个单词中取一个字母所需要的代币数量，为该字母左边和右边字母数量之积

- 可以从一个单词中多次取字母，每个字母仅可被取一次

> 例如：从 `example` 中取出字母 `a`，需要消耗代币 `2*4=8`，字母取出后单词变为 `exmple`；
再从中取出字母 `m`，需要消耗代币 `2*3=6`，字母取出后单词变为 `exple`；

请返回取得 `helloleetcode` 这些字母需要消耗代币的 **最少** 数量。如果无法取得，返回 `-1`。

**注意：**
- 取出字母的顺序没有要求
- 取出的所有字母恰好可以拼成 `helloleetcode` 

**示例 1：**
>输入：`words = ["hold","engineer","cost","level"]`
>
>输出：`5`
>
>解释：最优方法为：
>从 `hold` 依次取出 `h`、`o`、`l`、`d`， 代价均为 `0`
>从 `engineer` 依次取出第 `1` 个 `e` 与最后一个 `e`， 代价为 `0` 和 `5*1=5`
>从 `cost` 取出 `c`、`o`、`t`， 代价均为 `0`
>从 `level` 依次取出 `l`、`l`、`e`、`e`， 代价均为 `0`
>所有字母恰好可以拼成 `helloleetcode`，因此最小的代价为 `5`

**示例 2：**
>输入：`words = ["hello","leetcode"]`
>
>输出：`0`

**提示：**
+ `n == words.length`
+ `m == words[i].length`
+ `1 <= n <= 24`
+ `1 <= m <= 8`
+ `words[i][j]` 仅为小写字母

## 难度

Hard

## 标签

- 位运算
- 数组
- 字符串
- 动态规划
- 状态压缩

## 示例

```
["hold","engineer","cost","level"]
["hello","leetcode"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int Leetcode(vector<string>& words) {

    }
};
```

### Java

```java
class Solution {
    public int Leetcode(String[] words) {

    }
}
```

### Python

```python
class Solution(object):
    def Leetcode(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def Leetcode(self, words: List[str]) -> int:
```

### C

```c


int Leetcode(char** words, int wordsSize){

}
```

### C#

```csharp
public class Solution {
    public int Leetcode(string[] words) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var Leetcode = function(words) {

};
```

### TypeScript

```typescript
function Leetcode(words: string[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return Integer
     */
    function Leetcode($words) {

    }
}
```

### Swift

```swift
class Solution {
    func Leetcode(_ words: [String]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun Leetcode(words: Array<String>): Int {

    }
}
```

### Go

```golang
func Leetcode(words []string) int {

}
```

### Ruby

```ruby
# @param {String[]} words
# @return {Integer}
def leetcode(words)

end
```

### Scala

```scala
object Solution {
    def Leetcode(words: Array[String]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn leetcode(words: Vec<String>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (leetcode words)
  (-> (listof string?) exact-integer?)

  )
```

### Erlang

```erlang
-spec leetcode(Words :: [unicode:unicode_binary()]) -> integer().
leetcode(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec leetcode(words :: [String.t]) :: integer
  def leetcode(words) do

  end
end
```

