# LCP 25. 古董键盘

## 题目描述

小扣在秋日市集购买了一个古董键盘。由于古董键盘年久失修，键盘上只有 26 个字母 **a~z** 可以按下，且每个字母最多仅能被按 `k` 次。

小扣随机按了 `n` 次按键，请返回小扣总共有可能按出多少种内容。由于数字较大，最终答案需要对 1000000007 (1e9 + 7) 取模。


**示例 1：**
>输入：`k = 1, n = 1`
> 
>输出：`26`
> 
>解释：由于只能按一次按键，所有可能的字符串为 "a", "b", ... "z" 

**示例 2：**
>输入：`k = 1, n = 2`
> 
>输出：`650`
> 
>解释：由于只能按两次按键，且每个键最多只能按一次，所有可能的字符串（按字典序排序）为 "ab", "ac", ... "zy" 

**提示：**
- `1 <= k <= 5`
- `1 <= n <= 26*k`
 



## 难度

Hard

## 标签

- 数学
- 动态规划
- 组合数学

## 示例

```
1
1
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int keyboard(int k, int n) {

    }
};
```

### Java

```java
class Solution {
    public int keyboard(int k, int n) {

    }
}
```

### Python

```python
class Solution(object):
    def keyboard(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def keyboard(self, k: int, n: int) -> int:
```

### C

```c


int keyboard(int k, int n){

}
```

### C#

```csharp
public class Solution {
    public int Keyboard(int k, int n) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var keyboard = function(k, n) {

};
```

### TypeScript

```typescript
function keyboard(k: number, n: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer $n
     * @return Integer
     */
    function keyboard($k, $n) {

    }
}
```

### Swift

```swift
class Solution {
    func keyboard(_ k: Int, _ n: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun keyboard(k: Int, n: Int): Int {

    }
}
```

### Go

```golang
func keyboard(k int, n int) int {

}
```

### Ruby

```ruby
# @param {Integer} k
# @param {Integer} n
# @return {Integer}
def keyboard(k, n)

end
```

### Scala

```scala
object Solution {
    def keyboard(k: Int, n: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn keyboard(k: i32, n: i32) -> i32 {

    }
}
```

