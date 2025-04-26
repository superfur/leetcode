# LCP 17. 速算机器人

## 题目描述

小扣在秋日市集发现了一款速算机器人。店家对机器人说出两个数字（记作 `x` 和 `y`），请小扣说出计算指令：
- `"A"` 运算：使 `x = 2 * x + y`；
- `"B"` 运算：使 `y = 2 * y + x`。

在本次游戏中，店家说出的数字为 `x = 1` 和 `y = 0`，小扣说出的计算指令记作仅由大写字母 `A`、`B` 组成的字符串 `s`，字符串中字符的顺序表示计算顺序，请返回最终 `x` 与 `y` 的和为多少。

**示例 1：**
>输入：`s = "AB"`
> 
>输出：`4`
> 
>解释：
>经过一次 A 运算后，x = 2, y = 0。
>再经过一次 B 运算，x = 2, y = 2。
>最终 x 与 y 之和为 4。

**提示：**
- `0 <= s.length <= 10`
- `s` 由 `'A'` 和 `'B'` 组成




## 难度

Easy

## 标签

- 数学
- 字符串
- 模拟

## 示例

```
"AB"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int calculate(string s) {

    }
};
```

### Java

```java
class Solution {
    public int calculate(String s) {

    }
}
```

### Python

```python
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def calculate(self, s: str) -> int:
```

### C

```c


int calculate(char* s){

}
```

### C#

```csharp
public class Solution {
    public int Calculate(string s) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {

};
```

### TypeScript

```typescript
function calculate(s: string): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function calculate($s) {

    }
}
```

### Swift

```swift
class Solution {
    func calculate(_ s: String) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun calculate(s: String): Int {

    }
}
```

### Go

```golang
func calculate(s string) int {

}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def calculate(s)

end
```

### Scala

```scala
object Solution {
    def calculate(s: String): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn calculate(s: String) -> i32 {

    }
}
```

