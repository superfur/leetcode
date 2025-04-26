# LCP 72. 补给马车

## 题目描述

远征队即将开启未知的冒险之旅，不过在此之前，将对补给车队进行最后的检查。`supplies[i]` 表示编号为 `i` 的补给马车装载的物资数量。
考虑到车队过长容易被野兽偷袭，他们决定将车队的长度变为原来的一半（向下取整），计划为：
- 找出车队中 **物资之和最小** 两辆 **相邻** 马车，将它们车辆的物资整合为一辆。若存在多组物资之和相同的马车，则取编号最小的两辆马车进行整合；
- 重复上述操作直到车队长度符合要求。

请返回车队长度符合要求后，物资的分布情况。

**示例 1：**
>输入：`supplies = [7,3,6,1,8]`
>
>输出：`[10,15]`
>
>解释：
> 第 1 次合并，符合条件的两辆马车为 6,1，合并后的车队为 [7,3,7,8]；
> 第 2 次合并，符合条件的两辆马车为 (7,3) 和 (3,7)，取编号最小的 (7,3)，合并后的车队为 [10,7,8]；
> 第 3 次合并，符合条件的两辆马车为 7,8，合并后的车队为 [10,15]；
>返回 `[10,15]`

**示例 2：**
>输入：`supplies = [1,3,1,5]`
>
>输出：`[5,5]`

**解释：**
- `2 <= supplies.length <= 1000`
- `1 <= supplies[i] <= 1000`

## 难度

Easy

## 示例

```
[7,3,6,1,8]
[1,3,1,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> supplyWagon(vector<int>& supplies) {

    }
};
```

### Java

```java
class Solution {
    public int[] supplyWagon(int[] supplies) {

    }
}
```

### Python

```python
class Solution(object):
    def supplyWagon(self, supplies):
        """
        :type supplies: List[int]
        :rtype: List[int]
        """
```

### Python3

```python3
class Solution:
    def supplyWagon(self, supplies: List[int]) -> List[int]:
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* supplyWagon(int* supplies, int suppliesSize, int* returnSize){

}
```

### C#

```csharp
public class Solution {
    public int[] SupplyWagon(int[] supplies) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} supplies
 * @return {number[]}
 */
var supplyWagon = function(supplies) {

};
```

### TypeScript

```typescript
function supplyWagon(supplies: number[]): number[] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $supplies
     * @return Integer[]
     */
    function supplyWagon($supplies) {

    }
}
```

### Swift

```swift
class Solution {
    func supplyWagon(_ supplies: [Int]) -> [Int] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun supplyWagon(supplies: IntArray): IntArray {

    }
}
```

### Dart

```dart
class Solution {
  List<int> supplyWagon(List<int> supplies) {

  }
}
```

### Go

```golang
func supplyWagon(supplies []int) []int {

}
```

### Ruby

```ruby
# @param {Integer[]} supplies
# @return {Integer[]}
def supply_wagon(supplies)

end
```

### Scala

```scala
object Solution {
    def supplyWagon(supplies: Array[Int]): Array[Int] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn supply_wagon(supplies: Vec<i32>) -> Vec<i32> {

    }
}
```

### Racket

```racket
(define/contract (supply-wagon supplies)
  (-> (listof exact-integer?) (listof exact-integer?))

  )
```

### Erlang

```erlang
-spec supply_wagon(Supplies :: [integer()]) -> [integer()].
supply_wagon(Supplies) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec supply_wagon(supplies :: [integer]) :: [integer]
  def supply_wagon(supplies) do

  end
end
```

