# LCS 01. 下载插件

## 题目描述

小扣打算给自己的 **VS code** 安装使用插件，初始状态下带宽每分钟可以完成 `1` 个插件的下载。假定每分钟选择以下两种策略之一:
- 使用当前带宽下载插件
- 将带宽加倍（下载插件数量随之加倍）

请返回小扣完成下载 `n` 个插件最少需要多少分钟。

注意：实际的下载的插件数量可以超过 `n` 个


**示例 1：**
>输入：`n = 2`
>
>输出：`2`
>
>解释：
> 以下两个方案，都能实现 2 分钟内下载 2 个插件
>- 方案一：第一分钟带宽加倍，带宽可每分钟下载 2 个插件；第二分钟下载 2 个插件
>- 方案二：第一分钟下载 1 个插件，第二分钟下载 1 个插件

**示例 2：**
>输入：`n = 4`
>
>输出：`3`
>
>解释：
> 最少需要 3 分钟可完成 4 个插件的下载，以下是其中一种方案:
> 第一分钟带宽加倍，带宽可每分钟下载 2 个插件;
> 第二分钟下载 2 个插件;
> 第三分钟下载 2 个插件。



**提示：**
- `1 <= n <= 10^5`


## 难度

Easy

## 标签

- 贪心
- 数学
- 动态规划

## 示例

```
2
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int leastMinutes(int n) {

    }
};
```

### Java

```java
class Solution {
    public int leastMinutes(int n) {

    }
}
```

### Python

```python
class Solution(object):
    def leastMinutes(self, n):
        """
        :type n: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def leastMinutes(self, n: int) -> int:
```

### C

```c


int leastMinutes(int n){

}
```

### C#

```csharp
public class Solution {
    public int LeastMinutes(int n) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var leastMinutes = function(n) {

};
```

### TypeScript

```typescript
function leastMinutes(n: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function leastMinutes($n) {

    }
}
```

### Swift

```swift
class Solution {
    func leastMinutes(_ n: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun leastMinutes(n: Int): Int {

    }
}
```

### Go

```golang
func leastMinutes(n int) int {

}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def least_minutes(n)

end
```

### Scala

```scala
object Solution {
    def leastMinutes(n: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn least_minutes(n: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (least-minutes n)
  (-> exact-integer? exact-integer?)

  )
```

