# LCP 19. 秋叶收藏集

## 题目描述

小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 `leaves`， 字符串 `leaves` 仅包含小写字符 `r` 和 `y`， 其中字符 `r` 表示一片红叶，字符 `y` 表示一片黄叶。
出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。

**示例 1：**
>输入：`leaves = "rrryyyrryyyrr"`
>
>输出：`2`
>
>解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"

**示例 2：**
>输入：`leaves = "ryr"`
>
>输出：`0`
>
>解释：已符合要求，不需要额外操作

**提示：**
- `3 <= leaves.length <= 10^5`
- `leaves` 中只包含字符 `'r'` 和字符 `'y'`

## 难度

Medium

## 标签

- 字符串
- 动态规划

## 示例

```
"rrryyyrryyyrr"
"ryr"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumOperations(string leaves) {

    }
};
```

### Java

```java
class Solution {
    public int minimumOperations(String leaves) {

    }
}
```

### Python

```python
class Solution(object):
    def minimumOperations(self, leaves):
        """
        :type leaves: str
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def minimumOperations(self, leaves: str) -> int:
```

### C

```c


int minimumOperations(char* leaves){

}
```

### C#

```csharp
public class Solution {
    public int MinimumOperations(string leaves) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string} leaves
 * @return {number}
 */
var minimumOperations = function(leaves) {

};
```

### TypeScript

```typescript
function minimumOperations(leaves: string): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $leaves
     * @return Integer
     */
    function minimumOperations($leaves) {

    }
}
```

### Swift

```swift
class Solution {
    func minimumOperations(_ leaves: String) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumOperations(leaves: String): Int {

    }
}
```

### Go

```golang
func minimumOperations(leaves string) int {

}
```

### Ruby

```ruby
# @param {String} leaves
# @return {Integer}
def minimum_operations(leaves)

end
```

### Scala

```scala
object Solution {
    def minimumOperations(leaves: String): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_operations(leaves: String) -> i32 {

    }
}
```

