# 475. 供暖器

## 题目描述

<p>冬季已经来临。&nbsp;你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。</p>

<p>在加热器的加热半径范围内的每个房屋都可以获得供暖。</p>

<p>现在，给出位于一条水平线上的房屋&nbsp;<code>houses</code> 和供暖器&nbsp;<code>heaters</code> 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。</p>

<p><b>注意</b>：所有供暖器 <code>heaters</code> 都遵循你的半径标准，加热的半径也一样。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> houses = [1,2,3], heaters = [2]
<strong>输出:</strong> 1
<strong>解释:</strong> 仅在位置 2 上有一个供暖器。如果我们将加热半径设为 1，那么所有房屋就都能得到供暖。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> houses = [1,2,3,4], heaters = [1,4]
<strong>输出:</strong> 1
<strong>解释:</strong> 在位置 1, 4 上有两个供暖器。我们需要将加热半径设为 1，这样所有房屋就都能得到供暖。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>houses = [1,5], heaters = [2]
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= houses.length, heaters.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= houses[i], heaters[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 二分查找
- 排序

## 示例

```
[1,2,3]
[2]
[1,2,3,4]
[1,4]
[1,5]
[2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        
    }
};
```

### Java

```java
class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
```

### C

```c
int findRadius(int* houses, int housesSize, int* heaters, int heatersSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindRadius(int[] houses, int[] heaters) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} houses
 * @param {number[]} heaters
 * @return {number}
 */
var findRadius = function(houses, heaters) {
    
};
```

### TypeScript

```typescript
function findRadius(houses: number[], heaters: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $houses
     * @param Integer[] $heaters
     * @return Integer
     */
    function findRadius($houses, $heaters) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findRadius(_ houses: [Int], _ heaters: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findRadius(houses: IntArray, heaters: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findRadius(List<int> houses, List<int> heaters) {
    
  }
}
```

### Go

```golang
func findRadius(houses []int, heaters []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} houses
# @param {Integer[]} heaters
# @return {Integer}
def find_radius(houses, heaters)
    
end
```

### Scala

```scala
object Solution {
    def findRadius(houses: Array[Int], heaters: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_radius(houses: Vec<i32>, heaters: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-radius houses heaters)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_radius(Houses :: [integer()], Heaters :: [integer()]) -> integer().
find_radius(Houses, Heaters) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_radius(houses :: [integer], heaters :: [integer]) :: integer
  def find_radius(houses, heaters) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findRadius(houses: Array<Int64>, heaters: Array<Int64>): Int64 {

    }
}
```

