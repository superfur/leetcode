# 3477. 将水果放入篮子 II

## 题目描述

<p>给你两个长度为 <code>n</code>&nbsp;的整数数组，<code>fruits</code> 和 <code>baskets</code>，其中 <code>fruits[i]</code> 表示第 <code>i</code>&nbsp;种水果的 <strong>数量</strong>，<code>baskets[j]</code> 表示第 <code>j</code>&nbsp;个篮子的 <strong>容量</strong>。</p>

<p>你需要对 <code>fruits</code> 数组从左到右按照以下规则放置水果：</p>

<ul>
	<li>每种水果必须放入第一个 <strong>容量大于等于</strong> 该水果数量的 <strong>最左侧可用篮子</strong> 中。</li>
	<li>每个篮子只能装 <b>一种</b> 水果。</li>
	<li>如果一种水果 <b>无法放入</b> 任何篮子，它将保持 <b>未放置</b>。</li>
</ul>

<p>返回所有可能分配完成后，剩余未放置的水果种类的数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">fruits = [4,2,5], baskets = [3,5,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>fruits[0] = 4</code> 放入 <code>baskets[1] = 5</code>。</li>
	<li><code>fruits[1] = 2</code> 放入 <code>baskets[0] = 3</code>。</li>
	<li><code>fruits[2] = 5</code> 无法放入 <code>baskets[2] = 4</code>。</li>
</ul>

<p>由于有一种水果未放置，我们返回 1。</p>
</div>

<p><strong class="example">示例 2</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">fruits = [3,6,1], baskets = [6,4,7]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>fruits[0] = 3</code> 放入 <code>baskets[0] = 6</code>。</li>
	<li><code>fruits[1] = 6</code> 无法放入 <code>baskets[1] = 4</code>（容量不足），但可以放入下一个可用的篮子 <code>baskets[2] = 7</code>。</li>
	<li><code>fruits[2] = 1</code> 放入 <code>baskets[1] = 4</code>。</li>
</ul>

<p>由于所有水果都已成功放置，我们返回 0。</p>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>n == fruits.length == baskets.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= fruits[i], baskets[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 线段树
- 数组
- 二分查找
- 模拟

## 提示

1. Simulate the operations for each fruit as described

## 示例

```
[4,2,5]
[3,5,4]
[3,6,1]
[6,4,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        
    }
};
```

### Java

```java
class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
```

### C

```c
int numOfUnplacedFruits(int* fruits, int fruitsSize, int* baskets, int basketsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumOfUnplacedFruits(int[] fruits, int[] baskets) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} fruits
 * @param {number[]} baskets
 * @return {number}
 */
var numOfUnplacedFruits = function(fruits, baskets) {
    
};
```

### TypeScript

```typescript
function numOfUnplacedFruits(fruits: number[], baskets: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $fruits
     * @param Integer[] $baskets
     * @return Integer
     */
    function numOfUnplacedFruits($fruits, $baskets) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numOfUnplacedFruits(_ fruits: [Int], _ baskets: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numOfUnplacedFruits(fruits: IntArray, baskets: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numOfUnplacedFruits(List<int> fruits, List<int> baskets) {
    
  }
}
```

### Go

```golang
func numOfUnplacedFruits(fruits []int, baskets []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} fruits
# @param {Integer[]} baskets
# @return {Integer}
def num_of_unplaced_fruits(fruits, baskets)
    
end
```

### Scala

```scala
object Solution {
    def numOfUnplacedFruits(fruits: Array[Int], baskets: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_of_unplaced_fruits(fruits: Vec<i32>, baskets: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-of-unplaced-fruits fruits baskets)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_of_unplaced_fruits(Fruits :: [integer()], Baskets :: [integer()]) -> integer().
num_of_unplaced_fruits(Fruits, Baskets) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_of_unplaced_fruits(fruits :: [integer], baskets :: [integer]) :: integer
  def num_of_unplaced_fruits(fruits, baskets) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numOfUnplacedFruits(fruits: Array<Int64>, baskets: Array<Int64>): Int64 {

    }
}
```

