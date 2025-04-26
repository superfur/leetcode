# 1936. 新增的最少台阶数

## 题目描述

<p>给你一个 <strong>严格递增</strong> 的整数数组 <code>rungs</code> ，用于表示梯子上每一台阶的 <strong>高度</strong> 。当前你正站在高度为 <code>0</code> 的地板上，并打算爬到最后一个台阶。</p>

<p>另给你一个整数 <code>dist</code> 。每次移动中，你可以到达下一个距离你当前位置（地板或台阶）<strong>不超过</strong> <code>dist</code> 高度的台阶。当然，你也可以在任何正 <strong>整数</strong> 高度处插入尚不存在的新台阶。</p>

<p>返回爬到最后一阶时必须添加到梯子上的 <strong>最少</strong> 台阶数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>rungs = [1,3,5,10], dist = 2
<strong>输出：</strong>2
<strong>解释：
</strong>现在无法到达最后一阶。
在高度为 7 和 8 的位置增设新的台阶，以爬上梯子。 
梯子在高度为 [1,3,5,<strong><em>7</em></strong>,<strong><em>8</em></strong>,10] 的位置上有台阶。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>rungs = [3,6,8,10], dist = 3
<strong>输出：</strong>0
<strong>解释：</strong>
这个梯子无需增设新台阶也可以爬上去。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>rungs = [3,4,6,7], dist = 2
<strong>输出：</strong>1
<strong>解释：</strong>
现在无法从地板到达梯子的第一阶。 
在高度为 1 的位置增设新的台阶，以爬上梯子。 
梯子在高度为 [<strong><em>1</em></strong>,3,4,6,7] 的位置上有台阶。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>rungs = [5], dist = 10
<strong>输出：</strong>0
<strong>解释：</strong>这个梯子无需增设新台阶也可以爬上去。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= rungs.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= rungs[i] <= 10<sup>9</sup></code></li>
	<li><code>1 <= dist <= 10<sup>9</sup></code></li>
	<li><code>rungs</code> <strong>严格递增</strong></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组

## 提示

1. Go as far as you can on the available rungs before adding new rungs.
2. If you have to add a new rung, add it as high up as possible.
3. Try using division to decrease the number of computations.

## 示例

```
[1,3,5,10]
2
[3,6,8,10]
3
[3,4,6,7]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int addRungs(vector<int>& rungs, int dist) {
        
    }
};
```

### Java

```java
class Solution {
    public int addRungs(int[] rungs, int dist) {
        
    }
}
```

### Python

```python
class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        
```

### C

```c
int addRungs(int* rungs, int rungsSize, int dist) {
    
}
```

### C#

```csharp
public class Solution {
    public int AddRungs(int[] rungs, int dist) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} rungs
 * @param {number} dist
 * @return {number}
 */
var addRungs = function(rungs, dist) {
    
};
```

### TypeScript

```typescript
function addRungs(rungs: number[], dist: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $rungs
     * @param Integer $dist
     * @return Integer
     */
    function addRungs($rungs, $dist) {
        
    }
}
```

### Swift

```swift
class Solution {
    func addRungs(_ rungs: [Int], _ dist: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun addRungs(rungs: IntArray, dist: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int addRungs(List<int> rungs, int dist) {
    
  }
}
```

### Go

```golang
func addRungs(rungs []int, dist int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} rungs
# @param {Integer} dist
# @return {Integer}
def add_rungs(rungs, dist)
    
end
```

### Scala

```scala
object Solution {
    def addRungs(rungs: Array[Int], dist: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn add_rungs(rungs: Vec<i32>, dist: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (add-rungs rungs dist)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec add_rungs(Rungs :: [integer()], Dist :: integer()) -> integer().
add_rungs(Rungs, Dist) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec add_rungs(rungs :: [integer], dist :: integer) :: integer
  def add_rungs(rungs, dist) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func addRungs(rungs: Array<Int64>, dist: Int64): Int64 {

    }
}
```

