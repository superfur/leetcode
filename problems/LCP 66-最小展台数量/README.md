# LCP 66. 最小展台数量

## 题目描述

力扣嘉年华将举办一系列展览活动，后勤部将负责为每场展览提供所需要的展台。
已知后勤部得到了一份需求清单，记录了近期展览所需要的展台类型， `demand[i][j]` 表示第 `i` 天展览时第 `j` 个展台的类型。
在满足每一天展台需求的基础上，请返回后勤部需要准备的 **最小** 展台数量。

**注意：**
- 同一展台在不同天中可以重复使用。

**示例 1：**
>输入：`demand = ["acd","bed","accd"]`
>
>输出：`6`
>
>解释：
>第 `0` 天需要展台 `a、c、d`；
>第 `1` 天需要展台 `b、e、d`；
>第 `2` 天需要展台 `a、c、c、d`；
>因此，后勤部准备 `abccde` 的展台，可以满足每天的展览需求;

**示例 2：**
>输入：`demand = ["abc","ab","ac","b"]`
>
>输出：`3`


**提示：**
- `1 <= demand.length,demand[i].length <= 100`
- `demand[i][j]` 仅为小写字母

## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串
- 计数

## 示例

```
["acd","bed","accd"]
["abc","ab","ac","b"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minNumBooths(vector<string>& demand) {

    }
};
```

### Java

```java
class Solution {
    public int minNumBooths(String[] demand) {

    }
}
```

### Python

```python
class Solution(object):
    def minNumBooths(self, demand):
        """
        :type demand: List[str]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
```

### C

```c


int minNumBooths(char** demand, int demandSize){

}
```

### C#

```csharp
public class Solution {
    public int MinNumBooths(string[] demand) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} demand
 * @return {number}
 */
var minNumBooths = function(demand) {

};
```

### TypeScript

```typescript
function minNumBooths(demand: string[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $demand
     * @return Integer
     */
    function minNumBooths($demand) {

    }
}
```

### Swift

```swift
class Solution {
    func minNumBooths(_ demand: [String]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minNumBooths(demand: Array<String>): Int {

    }
}
```

### Go

```golang
func minNumBooths(demand []string) int {

}
```

### Ruby

```ruby
# @param {String[]} demand
# @return {Integer}
def min_num_booths(demand)

end
```

### Scala

```scala
object Solution {
    def minNumBooths(demand: Array[String]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_num_booths(demand: Vec<String>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (min-num-booths demand)
  (-> (listof string?) exact-integer?)

  )
```

### Erlang

```erlang
-spec min_num_booths(Demand :: [unicode:unicode_binary()]) -> integer().
min_num_booths(Demand) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_num_booths(demand :: [String.t]) :: integer
  def min_num_booths(demand) do

  end
end
```

