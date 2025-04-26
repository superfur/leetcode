# 1552. 两球之间的磁力

## 题目描述

<p>在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有&nbsp;<code>n</code>&nbsp;个空的篮子，第&nbsp;<code>i</code>&nbsp;个篮子的位置在&nbsp;<code>position[i]</code>&nbsp;，Morty&nbsp;想把&nbsp;<code>m</code>&nbsp;个球放到这些篮子里，使得任意两球间&nbsp;<strong>最小磁力</strong>&nbsp;最大。</p>

<p>已知两个球如果分别位于&nbsp;<code>x</code>&nbsp;和&nbsp;<code>y</code>&nbsp;，那么它们之间的磁力为&nbsp;<code>|x - y|</code>&nbsp;。</p>

<p>给你一个整数数组&nbsp;<code>position</code>&nbsp;和一个整数&nbsp;<code>m</code>&nbsp;，请你返回最大化的最小磁力。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/16/q3v1.jpg" style="height: 195px; width: 562px;"></p>

<pre><strong>输入：</strong>position = [1,2,3,4,7], m = 3
<strong>输出：</strong>3
<strong>解释：</strong>将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>position = [5,4,3,2,1,1000000000], m = 2
<strong>输出：</strong>999999999
<strong>解释：</strong>我们使用位于 1 和 1000000000 的篮子时最小磁力最大。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == position.length</code></li>
	<li><code>2 &lt;= n &lt;= 10^5</code></li>
	<li><code>1 &lt;= position[i] &lt;= 10^9</code></li>
	<li>所有&nbsp;<code>position</code>&nbsp;中的整数 <strong>互不相同</strong>&nbsp;。</li>
	<li><code>2 &lt;= m &lt;= position.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 排序

## 提示

1. If you can place balls such that the answer is x then you can do it for y where y < x.
2. Similarly if you cannot place balls such that the answer is x then you can do it for y where y > x.
3. Binary search on the answer and greedily see if it is possible.

## 示例

```
[1,2,3,4,7]
3
[5,4,3,2,1,1000000000]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxDistance(int[] position, int m) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
```

### C

```c
int maxDistance(int* position, int positionSize, int m) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxDistance(int[] position, int m) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} position
 * @param {number} m
 * @return {number}
 */
var maxDistance = function(position, m) {
    
};
```

### TypeScript

```typescript
function maxDistance(position: number[], m: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $position
     * @param Integer $m
     * @return Integer
     */
    function maxDistance($position, $m) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxDistance(_ position: [Int], _ m: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxDistance(position: IntArray, m: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxDistance(List<int> position, int m) {
    
  }
}
```

### Go

```golang
func maxDistance(position []int, m int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} position
# @param {Integer} m
# @return {Integer}
def max_distance(position, m)
    
end
```

### Scala

```scala
object Solution {
    def maxDistance(position: Array[Int], m: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_distance(position: Vec<i32>, m: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-distance position m)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_distance(Position :: [integer()], M :: integer()) -> integer().
max_distance(Position, M) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_distance(position :: [integer], m :: integer) :: integer
  def max_distance(position, m) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxDistance(position: Array<Int64>, m: Int64): Int64 {

    }
}
```

