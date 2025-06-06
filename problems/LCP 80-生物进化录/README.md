# LCP 80. 生物进化录

## 题目描述

在永恒之森中，存在着一本生物进化录，以 **一个树形结构** 记载了所有生物的演化过程。经过观察并整理了各节点间的关系，`parents[i]` 表示编号 `i` 节点的父节点编号(根节点的父节点为 `-1`)。

为了探索和记录其中的演化规律，队伍中的炼金术师提出了一种方法，可以以字符串的形式将其复刻下来，规则如下：
- 初始只有一个根节点，表示演化的起点，依次记录 `01` 字符串中的字符，
- 如果记录 `0`，则在当前节点下添加一个子节点，并将指针指向新添加的子节点；
- 如果记录 `1`，则将指针回退到当前节点的父节点处。

现在需要应用上述的记录方法，复刻下它的演化过程。请返回能够复刻演化过程的字符串中， **字典序最小** 的 `01` 字符串。

**注意：**
- 节点指针最终可以停在任何节点上，不一定要回到根节点。

**示例 1：**
> 输入：`parents = [-1,0,0,2]`
>
> 输出：`"00110"`
>
>解释：树结构如下图所示，共存在 2 种记录方案：
>第 1 种方案为：0(记录编号 1 的节点) -> 1(回退至节点 0) -> 0(记录编号 2 的节点) -> 0((记录编号 3 的节点))
>第 2 种方案为：0(记录编号 2 的节点) -> 0(记录编号 3 的节点) -> 1(回退至节点 2) -> 1(回退至节点 0) -> 0(记录编号 1 的节点)
>返回字典序更小的 `"00110"`
![image.png](https://pic.leetcode.cn/1682319485-cRVudI-image.png){:width=120px}![进化 (3).gif](https://pic.leetcode.cn/1682412701-waHdnm-%E8%BF%9B%E5%8C%96%20\(3\).gif){:width=320px}



**示例 2：**
> 输入：`parents = [-1,0,0,1,2,2]`
>
> 输出：`"00101100"`

**提示：**

- `1 <= parents.length <= 10^4`
- `-1 <= parents[i] < i` (即父节点编号小于子节点)

## 难度

Hard

## 示例

```
[-1,0,0,2]
[-1,0,0,1,2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string evolutionaryRecord(vector<int>& parents) {
        
    }
};
```

### Java

```java
class Solution {
    public String evolutionaryRecord(int[] parents) {
        
    }
}
```

### Python

```python
class Solution(object):
    def evolutionaryRecord(self, parents):
        """
        :type parents: List[int]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def evolutionaryRecord(self, parents: List[int]) -> str:
        
```

### C

```c
char* evolutionaryRecord(int* parents, int parentsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string EvolutionaryRecord(int[] parents) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} parents
 * @return {string}
 */
var evolutionaryRecord = function(parents) {
    
};
```

### TypeScript

```typescript
function evolutionaryRecord(parents: number[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $parents
     * @return String
     */
    function evolutionaryRecord($parents) {
        
    }
}
```

### Swift

```swift
class Solution {
    func evolutionaryRecord(_ parents: [Int]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun evolutionaryRecord(parents: IntArray): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String evolutionaryRecord(List<int> parents) {
    
  }
}
```

### Go

```golang
func evolutionaryRecord(parents []int) string {
    
}
```

### Ruby

```ruby
# @param {Integer[]} parents
# @return {String}
def evolutionary_record(parents)
    
end
```

### Scala

```scala
object Solution {
    def evolutionaryRecord(parents: Array[Int]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn evolutionary_record(parents: Vec<i32>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (evolutionary-record parents)
  (-> (listof exact-integer?) string?)
  )
```

### Erlang

```erlang
-spec evolutionary_record(Parents :: [integer()]) -> unicode:unicode_binary().
evolutionary_record(Parents) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec evolutionary_record(parents :: [integer]) :: String.t
  def evolutionary_record(parents) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func evolutionaryRecord(parents: Array<Int64>): String {

    }
}
```

