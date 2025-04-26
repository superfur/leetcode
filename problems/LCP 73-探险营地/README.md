# LCP 73. 探险营地

## 题目描述

探险家小扣的行动轨迹，都将保存在记录仪中。`expeditions[i]` 表示小扣第 `i` 次探险记录，用一个字符串数组表示。其中的每个「营地」由大小写字母组成，通过子串 `->` 连接。
> 例："Leet->code->Campsite"，表示到访了 "Leet"、"code"、"Campsite" 三个营地。

`expeditions[0]` 包含了初始小扣已知的所有营地；对于之后的第 `i` 次探险(即 `expeditions[i]` 且 i > 0)，如果记录中包含了之前均没出现的营地，则表示小扣 **新发现** 的营地。

请你找出小扣发现新营地最多且索引最小的那次探险，并返回对应的记录索引。如果所有探险记录都没有发现新的营地，返回 `-1`

**注意：**
- 大小写不同的营地视为不同的营地；
- 营地的名称长度均大于 `0`。

**示例 1：**
>输入：`expeditions = ["leet->code","leet->code->Campsite->Leet","leet->code->leet->courier"]`
>
>输出：`1`
>
>解释：
>初始已知的所有营地为 "leet" 和 "code"
>第 1 次，到访了 "leet"、"code"、"Campsite"、"Leet"，新发现营地 2 处："Campsite"、"Leet"
>第 2 次，到访了 "leet"、"code"、"courier"，新发现营地 1 处："courier"
>第 1 次探险发现的新营地数量最多，因此返回 `1`

**示例 2：**
>输入：`expeditions = ["Alice->Dex","","Dex"]`
>
>输出：`-1`
>
>解释：
>初始已知的所有营地为 "Alice" 和 "Dex"
>第 1 次，未到访任何营地；
>第 2 次，到访了 "Dex"，未新发现营地；
>因为两次探险均未发现新的营地，返回 `-1`

**示例 3：**
>输入：`expeditions = ["","Gryffindor->Slytherin->Gryffindor","Hogwarts->Hufflepuff->Ravenclaw"]`
>
>输出：`2`
>
>解释：
>初始未发现任何营地；
>第 1 次，到访 "Gryffindor"、"Slytherin" 营地，其中重复到访 "Gryffindor" 两次，
>因此新发现营地为 2 处："Gryffindor"、"Slytherin"
>第 2 次，到访 "Hogwarts"、"Hufflepuff"、"Ravenclaw" 营地；
>新发现营地 3 处："Hogwarts"、"Hufflepuff"、"Ravenclaw"；
>第 2 次探险发现的新营地数量最多，因此返回 `2`

**提示：**
- `1 <= expeditions.length <= 1000`
- `0 <= expeditions[i].length <= 1000`
- 探险记录中只包含大小写字母和子串"->"

## 难度

Medium

## 示例

```
["leet->code","leet->code->Campsite->Leet","leet->code->leet->courier"]
["Alice->Dex","","Dex"]
["","Gryffindor->Slytherin->Gryffindor","Hogwarts->Hufflepuff->Ravenclaw"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int adventureCamp(vector<string>& expeditions) {

    }
};
```

### Java

```java
class Solution {
    public int adventureCamp(String[] expeditions) {

    }
}
```

### Python

```python
class Solution(object):
    def adventureCamp(self, expeditions):
        """
        :type expeditions: List[str]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def adventureCamp(self, expeditions: List[str]) -> int:
```

### C

```c
int adventureCamp(char** expeditions, int expeditionsSize){

}
```

### C#

```csharp
public class Solution {
    public int AdventureCamp(string[] expeditions) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} expeditions
 * @return {number}
 */
var adventureCamp = function(expeditions) {

};
```

### TypeScript

```typescript
function adventureCamp(expeditions: string[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $expeditions
     * @return Integer
     */
    function adventureCamp($expeditions) {

    }
}
```

### Swift

```swift
class Solution {
    func adventureCamp(_ expeditions: [String]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun adventureCamp(expeditions: Array<String>): Int {

    }
}
```

### Dart

```dart
class Solution {
  int adventureCamp(List<String> expeditions) {

  }
}
```

### Go

```golang
func adventureCamp(expeditions []string) int {

}
```

### Ruby

```ruby
# @param {String[]} expeditions
# @return {Integer}
def adventure_camp(expeditions)

end
```

### Scala

```scala
object Solution {
    def adventureCamp(expeditions: Array[String]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn adventure_camp(expeditions: Vec<String>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (adventure-camp expeditions)
  (-> (listof string?) exact-integer?)

  )
```

### Erlang

```erlang
-spec adventure_camp(Expeditions :: [unicode:unicode_binary()]) -> integer().
adventure_camp(Expeditions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec adventure_camp(expeditions :: [String.t]) :: integer
  def adventure_camp(expeditions) do

  end
end
```

