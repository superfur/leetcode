# LCP 61. 气温变化趋势

## 题目描述

力扣城计划在两地设立「力扣嘉年华」的分会场，气象小组正在分析两地区的气温变化趋势，对于第 `i ~ (i+1)` 天的气温变化趋势，将根据以下规则判断：
- 若第 `i+1` 天的气温 **高于** 第 `i` 天，为 **上升** 趋势
- 若第 `i+1` 天的气温 **等于** 第 `i` 天，为 **平稳** 趋势
- 若第 `i+1` 天的气温 **低于** 第 `i` 天，为 **下降** 趋势

已知 `temperatureA[i]` 和 `temperatureB[i]` 分别表示第 `i` 天两地区的气温。
组委会希望找到一段天数尽可能多，且两地气温变化趋势相同的时间举办嘉年华活动。请分析并返回两地气温变化趋势**相同的最大连续天数**。
> 即最大的 `n`，使得第 `i~i+n` 天之间，两地气温变化趋势相同

**示例 1：**
>输入：
>`temperatureA = [21,18,18,18,31]`
>`temperatureB = [34,32,16,16,17]`
>
>输出：`2`
>
>解释：如下表所示， 第 `2～4` 天两地气温变化趋势相同，且持续时间最长，因此返回 `4-2=2`
![image.png](https://pic.leetcode-cn.com/1663902654-hlrSvs-image.png){:width=1000px}


**示例 2：**
>输入：
>`temperatureA = [5,10,16,-6,15,11,3]`
>`temperatureB = [16,22,23,23,25,3,-16]`
>
>输出：`3`

**提示：**
- `2 <= temperatureA.length == temperatureB.length <= 1000`
- `-20 <= temperatureA[i], temperatureB[i] <= 40`


## 难度

Easy

## 标签

- 数组

## 示例

```
[21,18,18,18,31]
[34,32,16,16,17]
[5,10,16,-6,15,11,3]
[16,22,23,23,25,3,-16]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int temperatureTrend(vector<int>& temperatureA, vector<int>& temperatureB) {

    }
};
```

### Java

```java
class Solution {
    public int temperatureTrend(int[] temperatureA, int[] temperatureB) {

    }
}
```

### Python

```python
class Solution(object):
    def temperatureTrend(self, temperatureA, temperatureB):
        """
        :type temperatureA: List[int]
        :type temperatureB: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
```

### C

```c


int temperatureTrend(int* temperatureA, int temperatureASize, int* temperatureB, int temperatureBSize){

}
```

### C#

```csharp
public class Solution {
    public int TemperatureTrend(int[] temperatureA, int[] temperatureB) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} temperatureA
 * @param {number[]} temperatureB
 * @return {number}
 */
var temperatureTrend = function(temperatureA, temperatureB) {

};
```

### TypeScript

```typescript
function temperatureTrend(temperatureA: number[], temperatureB: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $temperatureA
     * @param Integer[] $temperatureB
     * @return Integer
     */
    function temperatureTrend($temperatureA, $temperatureB) {

    }
}
```

### Swift

```swift
class Solution {
    func temperatureTrend(_ temperatureA: [Int], _ temperatureB: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun temperatureTrend(temperatureA: IntArray, temperatureB: IntArray): Int {

    }
}
```

### Dart

```dart
class Solution {
  int temperatureTrend(List<int> temperatureA, List<int> temperatureB) {

  }
}
```

### Go

```golang
func temperatureTrend(temperatureA []int, temperatureB []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} temperature_a
# @param {Integer[]} temperature_b
# @return {Integer}
def temperature_trend(temperature_a, temperature_b)

end
```

### Scala

```scala
object Solution {
    def temperatureTrend(temperatureA: Array[Int], temperatureB: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn temperature_trend(temperature_a: Vec<i32>, temperature_b: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (temperature-trend temperatureA temperatureB)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec temperature_trend(TemperatureA :: [integer()], TemperatureB :: [integer()]) -> integer().
temperature_trend(TemperatureA, TemperatureB) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec temperature_trend(temperature_a :: [integer], temperature_b :: [integer]) :: integer
  def temperature_trend(temperature_a, temperature_b) do

  end
end
```

