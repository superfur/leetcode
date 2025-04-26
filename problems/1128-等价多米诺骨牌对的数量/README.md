# 1128. 等价多米诺骨牌对的数量

## 题目描述

<p>给你一组多米诺骨牌 <code>dominoes</code> 。</p>

<p>形式上，<code>dominoes[i] = [a, b]</code> 与 <code>dominoes[j] = [c, d]</code> <strong>等价</strong> 当且仅当 (<code>a == c</code> 且 <code>b == d</code>) 或者 (<code>a == d</code> 且 <code>b == c</code>) 。即一张骨牌可以通过旋转 <code>0</code>&nbsp;度或 <code>180</code> 度得到另一张多米诺骨牌。</p>

<p>在&nbsp;<code>0 &lt;= i &lt; j &lt; dominoes.length</code>&nbsp;的前提下，找出满足&nbsp;<code>dominoes[i]</code> 和&nbsp;<code>dominoes[j]</code>&nbsp;等价的骨牌对 <code>(i, j)</code> 的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>dominoes = [[1,2],[2,1],[3,4],[5,6]]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= dominoes.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>dominoes[i].length == 2</code></li>
	<li><code>1 &lt;= dominoes[i][j] &lt;= 9</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. For each domino j, find the number of dominoes you've already seen (dominoes i with i < j) that are equivalent.
2. You can keep track of what you've seen using a hashmap.

## 示例

```
[[1,2],[2,1],[3,4],[5,6]]
[[1,2],[1,2],[1,1],[1,2],[2,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        
    }
};
```

### Java

```java
class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
```

### C

```c
int numEquivDominoPairs(int** dominoes, int dominoesSize, int* dominoesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumEquivDominoPairs(int[][] dominoes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} dominoes
 * @return {number}
 */
var numEquivDominoPairs = function(dominoes) {
    
};
```

### TypeScript

```typescript
function numEquivDominoPairs(dominoes: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $dominoes
     * @return Integer
     */
    function numEquivDominoPairs($dominoes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numEquivDominoPairs(_ dominoes: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numEquivDominoPairs(dominoes: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numEquivDominoPairs(List<List<int>> dominoes) {
    
  }
}
```

### Go

```golang
func numEquivDominoPairs(dominoes [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} dominoes
# @return {Integer}
def num_equiv_domino_pairs(dominoes)
    
end
```

### Scala

```scala
object Solution {
    def numEquivDominoPairs(dominoes: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_equiv_domino_pairs(dominoes: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-equiv-domino-pairs dominoes)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_equiv_domino_pairs(Dominoes :: [[integer()]]) -> integer().
num_equiv_domino_pairs(Dominoes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_equiv_domino_pairs(dominoes :: [[integer]]) :: integer
  def num_equiv_domino_pairs(dominoes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numEquivDominoPairs(dominoes: Array<Array<Int64>>): Int64 {

    }
}
```

