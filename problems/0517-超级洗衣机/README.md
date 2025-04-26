# 517. 超级洗衣机

## 题目描述

<p>假设有 <code>n</code><strong>&nbsp;</strong>台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。</p>

<p>在每一步操作中，你可以选择任意 <code>m</code> (<code>1 &lt;= m &lt;= n</code>) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。</p>

<p>给定一个整数数组&nbsp;<code>machines</code> 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 <strong>最少的操作步数 </strong>。如果不能使每台洗衣机中衣物的数量相等，则返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>machines = [1,0,5]
<strong>输出：</strong>3
<strong>解释：</strong>
第一步:    1     0 &lt;-- 5    =&gt;    1     1     4
第二步:    1 &lt;-- 1 &lt;-- 4    =&gt;    2     1     3    
第三步:    2     1 &lt;-- 3    =&gt;    2     2     2   
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>machines = [0,3,0]
<strong>输出：</strong>2
<strong>解释：</strong>
第一步:    0 &lt;-- 3     0    =&gt;    1     2     0    
第二步:    1     2 --&gt; 0    =&gt;    1     1     1     
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>machines = [0,2,0]
<strong>输出：</strong>-1
<strong>解释：</strong>
不可能让所有三个洗衣机同时剩下相同数量的衣物。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == machines.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= machines[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组

## 示例

```
[1,0,5]
[0,3,0]
[0,2,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMinMoves(vector<int>& machines) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMinMoves(int[] machines) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        
```

### C

```c
int findMinMoves(int* machines, int machinesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMinMoves(int[] machines) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} machines
 * @return {number}
 */
var findMinMoves = function(machines) {
    
};
```

### TypeScript

```typescript
function findMinMoves(machines: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $machines
     * @return Integer
     */
    function findMinMoves($machines) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMinMoves(_ machines: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMinMoves(machines: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMinMoves(List<int> machines) {
    
  }
}
```

### Go

```golang
func findMinMoves(machines []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} machines
# @return {Integer}
def find_min_moves(machines)
    
end
```

### Scala

```scala
object Solution {
    def findMinMoves(machines: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_min_moves(machines: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-min-moves machines)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_min_moves(Machines :: [integer()]) -> integer().
find_min_moves(Machines) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_min_moves(machines :: [integer]) :: integer
  def find_min_moves(machines) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMinMoves(machines: Array<Int64>): Int64 {

    }
}
```

