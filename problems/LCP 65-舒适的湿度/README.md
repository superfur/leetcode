# LCP 65. 舒适的湿度

## 题目描述

力扣嘉年华为了确保更舒适的游览环境条件，在会场的各处设置了湿度调节装置，这些调节装置受控于总控室中的一台控制器。
控制器中已经预设了一些调节指令，整数数组`operate[i]` 表示第 `i` 条指令增加空气湿度的大小。现在你可以将任意数量的指令修改为降低湿度（变化的数值不变），以确保湿度尽可能的适宜：
- 控制器会选择 **一段连续的指令** ，从而进行湿度调节的操作；
- 这段指令最终对湿度影响的绝对值，即为当前操作的「不适宜度」
- 在控制器所有可能的操作中，**最大** 的「不适宜度」即为「整体不适宜度」

请返回在所有修改指令的方案中，可以得到的 **最小** 「整体不适宜度」。

**示例 1：**
> 输入：`operate = [5,3,7]`
>
> 输出：`8`
>
> 解释：对于方案 `2` 的 `[5,3,-7]`
>操作指令 `[5],[3],[-7]` 的「不适宜度」分别为 `5,3,7`
>操作指令 `[5,3],[3,-7]` 的「不适宜度」分别为 `8,4`
>操作指令 `[5,3,-7]` 的「不适宜度」为 `1`，
>因此对于方案 `[5,3,-7]`的「整体不适宜度」为 `8`，其余方案的「整体不适宜度」均不小于 `8`，如下表所示：
![image.png](https://pic.leetcode-cn.com/1663902759-dgDCxn-image.png){:width=650px}

**示例 2：**
> 输入：`operate = [20,10]`
>
> 输出：`20`

**提示：**
- `1 <= operate.length <= 1000`
- `1 <= operate[i] <= 1000`

## 难度

Hard

## 标签

- 数组
- 动态规划

## 示例

```
[5,3,7]
[10,20]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int unSuitability(vector<int>& operate) {

    }
};
```

### Java

```java
class Solution {
    public int unSuitability(int[] operate) {

    }
}
```

### Python

```python
class Solution(object):
    def unSuitability(self, operate):
        """
        :type operate: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def unSuitability(self, operate: List[int]) -> int:
```

### C

```c


int unSuitability(int* operate, int operateSize){

}
```

### C#

```csharp
public class Solution {
    public int UnSuitability(int[] operate) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} operate
 * @return {number}
 */
var unSuitability = function(operate) {

};
```

### TypeScript

```typescript
function unSuitability(operate: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $operate
     * @return Integer
     */
    function unSuitability($operate) {

    }
}
```

### Swift

```swift
class Solution {
    func unSuitability(_ operate: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun unSuitability(operate: IntArray): Int {

    }
}
```

### Go

```golang
func unSuitability(operate []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} operate
# @return {Integer}
def un_suitability(operate)

end
```

### Scala

```scala
object Solution {
    def unSuitability(operate: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn un_suitability(operate: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (un-suitability operate)
  (-> (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec un_suitability(Operate :: [integer()]) -> integer().
un_suitability(Operate) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec un_suitability(operate :: [integer]) :: integer
  def un_suitability(operate) do

  end
end
```

