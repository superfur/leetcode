# 575. 分糖果

## 题目描述

<p>Alice 有 <code>n</code> 枚糖，其中第 <code>i</code> 枚糖的类型为 <code>candyType[i]</code> 。Alice 注意到她的体重正在增长，所以前去拜访了一位医生。</p>

<p>医生建议 Alice 要少摄入糖分，只吃掉她所有糖的 <code>n / 2</code> 即可（<code>n</code> 是一个偶数）。Alice 非常喜欢这些糖，她想要在遵循医生建议的情况下，尽可能吃到最多不同种类的糖。</p>

<p>给你一个长度为 <code>n</code> 的整数数组 <code>candyType</code> ，返回： Alice <em>在仅吃掉 <code>n / 2</code> 枚糖的情况下，可以吃到糖的 <strong>最多</strong> 种类数</em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>candyType = [1,1,2,2,3,3]
<strong>输出：</strong>3
<strong>解释：</strong>Alice 只能吃 6 / 2 = 3 枚糖，由于只有 3 种糖，她可以每种吃一枚。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>candyType = [1,1,2,3]
<strong>输出：</strong>2
<strong>解释：</strong>Alice 只能吃 4 / 2 = 2 枚糖，不管她选择吃的种类是 [1,2]、[1,3] 还是 [2,3]，她只能吃到两种不同类的糖。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>candyType = [6,6,6,6]
<strong>输出：</strong>1
<strong>解释：</strong>Alice 只能吃 4 / 2 = 2 枚糖，尽管她能吃 2 枚，但只能吃到 1 种糖。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == candyType.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>n</code> 是一个偶数</li>
	<li><code>-10<sup>5</sup> &lt;= candyType[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表

## 提示

1. To maximize the number of kinds of candies, we should try to distribute candies such that Alice will gain all kinds.
2. What is the upper limit of the number of kinds of candies Alice will gain? Remember candies are to distributed equally.
3. Which data structure is the most suitable for finding the number of kinds of candies?
4. Will hashset solves the problem? Inserting all candies kind in the hashset and then checking its size with upper limit.

## 示例

```
[1,1,2,2,3,3]
[1,1,2,3]
[6,6,6,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        
    }
};
```

### Java

```java
class Solution {
    public int distributeCandies(int[] candyType) {
        
    }
}
```

### Python

```python
class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
```

### C

```c
int distributeCandies(int* candyType, int candyTypeSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int DistributeCandies(int[] candyType) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function(candyType) {
    
};
```

### TypeScript

```typescript
function distributeCandies(candyType: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $candyType
     * @return Integer
     */
    function distributeCandies($candyType) {
        
    }
}
```

### Swift

```swift
class Solution {
    func distributeCandies(_ candyType: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun distributeCandies(candyType: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int distributeCandies(List<int> candyType) {
    
  }
}
```

### Go

```golang
func distributeCandies(candyType []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} candy_type
# @return {Integer}
def distribute_candies(candy_type)
    
end
```

### Scala

```scala
object Solution {
    def distributeCandies(candyType: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn distribute_candies(candy_type: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (distribute-candies candyType)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec distribute_candies(CandyType :: [integer()]) -> integer().
distribute_candies(CandyType) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec distribute_candies(candy_type :: [integer]) :: integer
  def distribute_candies(candy_type) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func distributeCandies(candyType: Array<Int64>): Int64 {

    }
}
```

