# 3074. 重新分装苹果

## 题目描述

<p>给你一个长度为 <code>n</code> 的数组 <code>apple</code> 和另一个长度为 <code>m</code> 的数组 <code>capacity</code> 。</p>

<p>一共有 <code>n</code> 个包裹，其中第 <code>i</code> 个包裹中装着 <code>apple[i]</code> 个苹果。同时，还有 <code>m</code> 个箱子，第 <code>i</code> 个箱子的容量为 <code>capacity[i]</code> 个苹果。</p>

<p>请你选择一些箱子来将这 <code>n</code> 个包裹中的苹果重新分装到箱子中，返回你需要选择的箱子的<strong> 最小</strong> 数量。</p>

<p><strong>注意</strong>，同一个包裹中的苹果可以分装到不同的箱子中。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>apple = [1,3,2], capacity = [4,3,1,5,2]
<strong>输出：</strong>2
<strong>解释：</strong>使用容量为 4 和 5 的箱子。
总容量大于或等于苹果的总数，所以可以完成重新分装。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>apple = [5,5,5], capacity = [2,4,2,7]
<strong>输出：</strong>4
<strong>解释：</strong>需要使用所有箱子。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == apple.length &lt;= 50</code></li>
	<li><code>1 &lt;= m == capacity.length &lt;= 50</code></li>
	<li><code>1 &lt;= apple[i], capacity[i] &lt;= 50</code></li>
	<li>输入数据保证可以将包裹中的苹果重新分装到箱子中。</li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Sort array <code>capacity</code> in non-decreasing order.
2. Greedily select boxes with the largest capacities to redistribute apples optimally.

## 示例

```
[1,3,2]
[4,3,1,5,2]
[5,5,5]
[2,4,2,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
```

### C

```c
int minimumBoxes(int* apple, int appleSize, int* capacity, int capacitySize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumBoxes(int[] apple, int[] capacity) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} apple
 * @param {number[]} capacity
 * @return {number}
 */
var minimumBoxes = function(apple, capacity) {
    
};
```

### TypeScript

```typescript
function minimumBoxes(apple: number[], capacity: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $apple
     * @param Integer[] $capacity
     * @return Integer
     */
    function minimumBoxes($apple, $capacity) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumBoxes(_ apple: [Int], _ capacity: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumBoxes(apple: IntArray, capacity: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumBoxes(List<int> apple, List<int> capacity) {
    
  }
}
```

### Go

```golang
func minimumBoxes(apple []int, capacity []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} apple
# @param {Integer[]} capacity
# @return {Integer}
def minimum_boxes(apple, capacity)
    
end
```

### Scala

```scala
object Solution {
    def minimumBoxes(apple: Array[Int], capacity: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_boxes(apple: Vec<i32>, capacity: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-boxes apple capacity)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_boxes(Apple :: [integer()], Capacity :: [integer()]) -> integer().
minimum_boxes(Apple, Capacity) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_boxes(apple :: [integer], capacity :: [integer]) :: integer
  def minimum_boxes(apple, capacity) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumBoxes(apple: Array<Int64>, capacity: Array<Int64>): Int64 {

    }
}
```

