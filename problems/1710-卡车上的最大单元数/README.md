# 1710. 卡车上的最大单元数

## 题目描述

<p>请你将一些箱子装在 <strong>一辆卡车</strong> 上。给你一个二维数组 <code>boxTypes</code> ，其中 <code>boxTypes[i] = [numberOfBoxes<sub>i</sub>, numberOfUnitsPerBox<sub>i</sub>]</code> ：</p>

<ul>
	<li><code>numberOfBoxes<sub>i</sub></code> 是类型 <code>i</code> 的箱子的数量。</li>
	<li><code>numberOfUnitsPerBox<sub>i</sub></code><sub> </sub>是类型 <code>i</code> 每个箱子可以装载的单元数量。</li>
</ul>

<p>整数 <code>truckSize</code> 表示卡车上可以装载 <strong>箱子</strong> 的 <strong>最大数量</strong> 。只要箱子数量不超过 <code>truckSize</code> ，你就可以选择任意箱子装到卡车上。</p>

<p>返回卡车可以装载 <strong>单元</strong> 的 <strong>最大</strong> 总数<em>。</em></p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
<strong>输出：</strong>8
<strong>解释：</strong>箱子的情况如下：
- 1 个第一类的箱子，里面含 3 个单元。
- 2 个第二类的箱子，每个里面含 2 个单元。
- 3 个第三类的箱子，每个里面含 1 个单元。
可以选择第一类和第二类的所有箱子，以及第三类的一个箱子。
单元总数 = (1 * 3) + (2 * 2) + (1 * 1) = 8</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
<strong>输出：</strong>91
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= boxTypes.length <= 1000</code></li>
	<li><code>1 <= numberOfBoxes<sub>i</sub>, numberOfUnitsPerBox<sub>i</sub> <= 1000</code></li>
	<li><code>1 <= truckSize <= 10<sup>6</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 排序

## 提示

1. If we have space for at least one box, it's always optimal to put the box with the most units.
2. Sort the box types with the number of units per box non-increasingly.
3. Iterate on the box types and take from each type as many as you can.

## 示例

```
[[1,3],[2,2],[3,1]]
4
[[5,10],[2,5],[4,7],[3,9]]
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
```

### C

```c
int maximumUnits(int** boxTypes, int boxTypesSize, int* boxTypesColSize, int truckSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumUnits(int[][] boxTypes, int truckSize) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} boxTypes
 * @param {number} truckSize
 * @return {number}
 */
var maximumUnits = function(boxTypes, truckSize) {
    
};
```

### TypeScript

```typescript
function maximumUnits(boxTypes: number[][], truckSize: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $boxTypes
     * @param Integer $truckSize
     * @return Integer
     */
    function maximumUnits($boxTypes, $truckSize) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumUnits(_ boxTypes: [[Int]], _ truckSize: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumUnits(boxTypes: Array<IntArray>, truckSize: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumUnits(List<List<int>> boxTypes, int truckSize) {
    
  }
}
```

### Go

```golang
func maximumUnits(boxTypes [][]int, truckSize int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} box_types
# @param {Integer} truck_size
# @return {Integer}
def maximum_units(box_types, truck_size)
    
end
```

### Scala

```scala
object Solution {
    def maximumUnits(boxTypes: Array[Array[Int]], truckSize: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_units(box_types: Vec<Vec<i32>>, truck_size: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-units boxTypes truckSize)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_units(BoxTypes :: [[integer()]], TruckSize :: integer()) -> integer().
maximum_units(BoxTypes, TruckSize) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_units(box_types :: [[integer]], truck_size :: integer) :: integer
  def maximum_units(box_types, truck_size) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumUnits(boxTypes: Array<Array<Int64>>, truckSize: Int64): Int64 {

    }
}
```

