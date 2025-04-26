# 957. N 天后的牢房

## 题目描述

<p>监狱中 <code>8</code> 间牢房排成一排，每间牢房可能被占用或空置。</p>

<p>每天，无论牢房是被占用或空置，都会根据以下规则进行变更：</p>

<ul>
	<li>如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。</li>
	<li>否则，它就会被空置。</li>
</ul>

<p><strong>注意</strong>：由于监狱中的牢房排成一行，所以行中的第一个和最后一个牢房不存在两个相邻的房间。</p>

<p>给你一个整数数组 <code>cells</code> ，用于表示牢房的初始状态：如果第 <code>i</code> 间牢房被占用，则 <code>cell[i]==1</code>，否则 <code>cell[i]==0</code> 。另给你一个整数 <code>n</code> 。</p>

<p>请你返回 <code>n</code> 天后监狱的状况（即，按上文描述进行 <code>n</code> 次变更）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>cells = [0,1,0,1,1,0,0,1], n = 7
<strong>输出：</strong>[0,0,1,1,0,0,0,0]
<strong>解释：</strong>下表总结了监狱每天的状况：
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>cells = [1,0,0,1,0,0,1,0], n = 1000000000
<strong>输出：</strong>[0,0,1,1,1,1,1,0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>cells.length == 8</code></li>
	<li><code>cells[i]</code> 为 <code>0</code> 或 <code>1</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 哈希表
- 数学

## 示例

```
[0,1,0,1,1,0,0,1]
7
[1,0,0,1,0,0,1,0]
1000000000
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] prisonAfterNDays(int[] cells, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* prisonAfterNDays(int* cells, int cellsSize, int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] PrisonAfterNDays(int[] cells, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} cells
 * @param {number} n
 * @return {number[]}
 */
var prisonAfterNDays = function(cells, n) {
    
};
```

### TypeScript

```typescript
function prisonAfterNDays(cells: number[], n: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $cells
     * @param Integer $n
     * @return Integer[]
     */
    function prisonAfterNDays($cells, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func prisonAfterNDays(_ cells: [Int], _ n: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun prisonAfterNDays(cells: IntArray, n: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> prisonAfterNDays(List<int> cells, int n) {
    
  }
}
```

### Go

```golang
func prisonAfterNDays(cells []int, n int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} cells
# @param {Integer} n
# @return {Integer[]}
def prison_after_n_days(cells, n)
    
end
```

### Scala

```scala
object Solution {
    def prisonAfterNDays(cells: Array[Int], n: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn prison_after_n_days(cells: Vec<i32>, n: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (prison-after-n-days cells n)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec prison_after_n_days(Cells :: [integer()], N :: integer()) -> [integer()].
prison_after_n_days(Cells, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec prison_after_n_days(cells :: [integer], n :: integer) :: [integer]
  def prison_after_n_days(cells, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func prisonAfterNDays(cells: Array<Int64>, n: Int64): Array<Int64> {

    }
}
```

