# 1011. 在 D 天内送达包裹的能力

## 题目描述

<p>传送带上的包裹必须在 <code>days</code> 天内从一个港口运送到另一个港口。</p>

<p>传送带上的第 <code>i</code>&nbsp;个包裹的重量为&nbsp;<code>weights[i]</code>。每一天，我们都会按给出重量（<code>weights</code>）的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。</p>

<p>返回能在 <code>days</code> 天内将传送带上的所有包裹送达的船的最低运载能力。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>weights = [1,2,3,4,5,6,7,8,9,10], days = 5
<strong>输出：</strong>15
<strong>解释：</strong>
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>weights = [3,2,2,4,1,4], days = 3
<strong>输出：</strong>6
<strong>解释：</strong>
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>weights = [1,2,3,1,1], days = 4
<strong>输出：</strong>3
<strong>解释：</strong>
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= days &lt;= weights.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= weights[i] &lt;= 500</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. Binary search on the answer.  We need a function possible(capacity) which returns true if and only if we can do the task in D days.

## 示例

```
[1,2,3,4,5,6,7,8,9,10]
5
[3,2,2,4,1,4]
3
[1,2,3,1,1]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        
    }
};
```

### Java

```java
class Solution {
    public int shipWithinDays(int[] weights, int days) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
```

### C

```c
int shipWithinDays(int* weights, int weightsSize, int days) {
    
}
```

### C#

```csharp
public class Solution {
    public int ShipWithinDays(int[] weights, int days) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} weights
 * @param {number} days
 * @return {number}
 */
var shipWithinDays = function(weights, days) {
    
};
```

### TypeScript

```typescript
function shipWithinDays(weights: number[], days: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $weights
     * @param Integer $days
     * @return Integer
     */
    function shipWithinDays($weights, $days) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shipWithinDays(_ weights: [Int], _ days: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shipWithinDays(weights: IntArray, days: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int shipWithinDays(List<int> weights, int days) {
    
  }
}
```

### Go

```golang
func shipWithinDays(weights []int, days int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} weights
# @param {Integer} days
# @return {Integer}
def ship_within_days(weights, days)
    
end
```

### Scala

```scala
object Solution {
    def shipWithinDays(weights: Array[Int], days: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ship_within_days(weights: Vec<i32>, days: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (ship-within-days weights days)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec ship_within_days(Weights :: [integer()], Days :: integer()) -> integer().
ship_within_days(Weights, Days) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ship_within_days(weights :: [integer], days :: integer) :: integer
  def ship_within_days(weights, days) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shipWithinDays(weights: Array<Int64>, days: Int64): Int64 {

    }
}
```

