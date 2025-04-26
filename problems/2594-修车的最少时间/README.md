# 2594. 修车的最少时间

## 题目描述

<p>给你一个整数数组&nbsp;<code>ranks</code>&nbsp;，表示一些机械工的 <strong>能力值</strong>&nbsp;。<code>ranks<sub>i</sub></code> 是第 <code>i</code> 位机械工的能力值。能力值为&nbsp;<code>r</code>&nbsp;的机械工可以在&nbsp;<code>r * n<sup>2</sup></code>&nbsp;分钟内修好&nbsp;<code>n</code>&nbsp;辆车。</p>

<p>同时给你一个整数&nbsp;<code>cars</code>&nbsp;，表示总共需要修理的汽车数目。</p>

<p>请你返回修理所有汽车&nbsp;<strong>最少</strong>&nbsp;需要多少时间。</p>

<p><strong>注意：</strong>所有机械工可以同时修理汽车。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>ranks = [4,2,3,1], cars = 10
<b>输出：</b>16
<b>解释：</b>
- 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
- 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
- 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
- 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
16 分钟是修理完所有车需要的最少时间。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>ranks = [5,1,8], cars = 6
<b>输出：</b>16
<b>解释：</b>
- 第一位机械工修 1 辆车，需要 5 * 1 * 1 = 5 分钟。
- 第二位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
- 第三位机械工修 1 辆车，需要 8 * 1 * 1 = 8 分钟。
16 分钟时修理完所有车需要的最少时间。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= ranks.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= ranks[i] &lt;= 100</code></li>
	<li><code>1 &lt;= cars &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. For a predefined fixed time, can all the cars be repaired?
2. Try using binary search on the answer.

## 示例

```
[4,2,3,1]
10
[5,1,8]
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {
        
    }
};
```

### Java

```java
class Solution {
    public long repairCars(int[] ranks, int cars) {
        
    }
}
```

### Python

```python
class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
```

### C

```c
long long repairCars(int* ranks, int ranksSize, int cars) {
    
}
```

### C#

```csharp
public class Solution {
    public long RepairCars(int[] ranks, int cars) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} ranks
 * @param {number} cars
 * @return {number}
 */
var repairCars = function(ranks, cars) {
    
};
```

### TypeScript

```typescript
function repairCars(ranks: number[], cars: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $ranks
     * @param Integer $cars
     * @return Integer
     */
    function repairCars($ranks, $cars) {
        
    }
}
```

### Swift

```swift
class Solution {
    func repairCars(_ ranks: [Int], _ cars: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun repairCars(ranks: IntArray, cars: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int repairCars(List<int> ranks, int cars) {
    
  }
}
```

### Go

```golang
func repairCars(ranks []int, cars int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} ranks
# @param {Integer} cars
# @return {Integer}
def repair_cars(ranks, cars)
    
end
```

### Scala

```scala
object Solution {
    def repairCars(ranks: Array[Int], cars: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn repair_cars(ranks: Vec<i32>, cars: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (repair-cars ranks cars)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec repair_cars(Ranks :: [integer()], Cars :: integer()) -> integer().
repair_cars(Ranks, Cars) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec repair_cars(ranks :: [integer], cars :: integer) :: integer
  def repair_cars(ranks, cars) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func repairCars(ranks: Array<Int64>, cars: Int64): Int64 {

    }
}
```

