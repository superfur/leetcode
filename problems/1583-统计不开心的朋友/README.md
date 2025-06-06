# 1583. 统计不开心的朋友

## 题目描述

<p>给你一份 <code>n</code> 位朋友的亲近程度列表，其中 <code>n</code> 总是 <strong>偶数</strong> 。</p>

<p>对每位朋友 <code>i</code>，<code>preferences[i]</code> 包含一份 <strong>按亲近程度从高</strong><strong>到低排列</strong> 的朋友列表。换句话说，排在列表前面的朋友与 <code>i</code> 的亲近程度比排在列表后面的朋友更高。每个列表中的朋友均以 <code>0</code> 到 <code>n-1</code> 之间的整数表示。</p>

<p>所有的朋友被分成几对，配对情况以列表 <code>pairs</code> 给出，其中 <code>pairs[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 表示 <code>x<sub>i</sub></code> 与 <code>y<sub>i</sub></code> 配对，且 <code>y<sub>i</sub></code> 与 <code>x<sub>i</sub></code> 配对。</p>

<p>但是，这样的配对情况可能会使其中部分朋友感到不开心。在 <code>x</code> 与 <code>y</code> 配对且 <code>u</code> 与 <code>v</code> 配对的情况下，如果同时满足下述两个条件，<code>x</code> 就会不开心：</p>

<ul>
	<li><code>x</code> 与 <code>u</code> 的亲近程度胜过 <code>x</code> 与 <code>y</code>，且</li>
	<li><code>u</code> 与 <code>x</code> 的亲近程度胜过 <code>u</code> 与 <code>v</code></li>
</ul>

<p>返回 <strong>不开心的朋友的数目</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
<strong>输出：</strong>2
<strong>解释：</strong>
朋友 1 不开心，因为：
- <strong>1 与 0 </strong>配对，但 <strong>1 与 3</strong> 的亲近程度比 <strong>1 与 0</strong> 高，且
- <strong>3 与 1</strong> 的亲近程度比 <strong>3 与 2</strong> 高。
朋友 3 不开心，因为：
- 3 与 2 配对，但 <strong>3 与 1</strong> 的亲近程度比 <strong>3 与 2</strong> 高，且
- <strong>1 与 3</strong> 的亲近程度比 <strong>1 与 0</strong> 高。
朋友 0 和 2 都是开心的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
<strong>输出：</strong>0
<strong>解释：</strong>朋友 0 和 1 都开心。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 500</code></li>
	<li><code>n</code> 是偶数</li>
	<li><code>preferences.length&nbsp;== n</code></li>
	<li><code>preferences[i].length&nbsp;== n - 1</code></li>
	<li><code>0 &lt;= preferences[i][j] &lt;= n - 1</code></li>
	<li><code>preferences[i]</code> 不包含 <code>i</code></li>
	<li><code>preferences[i]</code> 中的所有值都是独一无二的</li>
	<li><code>pairs.length&nbsp;== n/2</code></li>
	<li><code>pairs[i].length&nbsp;== 2</code></li>
	<li><code>x<sub>i</sub> != y<sub>i</sub></code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub>&nbsp;&lt;= n - 1</code></li>
	<li>每位朋友都 <strong>恰好</strong> 被包含在一对中</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 模拟

## 提示

1. Create a matrix “rank” where rank[i][j] holds how highly friend ‘i' views ‘j’. This allows for O(1) comparisons between people

## 示例

```
4
[[1,2,3],[3,2,0],[3,1,0],[1,2,0]]
[[0,1],[2,3]]
2
[[1],[0]]
[[1,0]]
4
[[1,3,2],[2,3,0],[1,3,0],[0,2,1]]
[[1,3],[0,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int unhappyFriends(int n, vector<vector<int>>& preferences, vector<vector<int>>& pairs) {
        
    }
};
```

### Java

```java
class Solution {
    public int unhappyFriends(int n, int[][] preferences, int[][] pairs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
```

### C

```c
int unhappyFriends(int n, int** preferences, int preferencesSize, int* preferencesColSize, int** pairs, int pairsSize, int* pairsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int UnhappyFriends(int n, int[][] preferences, int[][] pairs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} preferences
 * @param {number[][]} pairs
 * @return {number}
 */
var unhappyFriends = function(n, preferences, pairs) {
    
};
```

### TypeScript

```typescript
function unhappyFriends(n: number, preferences: number[][], pairs: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $preferences
     * @param Integer[][] $pairs
     * @return Integer
     */
    function unhappyFriends($n, $preferences, $pairs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func unhappyFriends(_ n: Int, _ preferences: [[Int]], _ pairs: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun unhappyFriends(n: Int, preferences: Array<IntArray>, pairs: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int unhappyFriends(int n, List<List<int>> preferences, List<List<int>> pairs) {
    
  }
}
```

### Go

```golang
func unhappyFriends(n int, preferences [][]int, pairs [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} preferences
# @param {Integer[][]} pairs
# @return {Integer}
def unhappy_friends(n, preferences, pairs)
    
end
```

### Scala

```scala
object Solution {
    def unhappyFriends(n: Int, preferences: Array[Array[Int]], pairs: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn unhappy_friends(n: i32, preferences: Vec<Vec<i32>>, pairs: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (unhappy-friends n preferences pairs)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec unhappy_friends(N :: integer(), Preferences :: [[integer()]], Pairs :: [[integer()]]) -> integer().
unhappy_friends(N, Preferences, Pairs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec unhappy_friends(n :: integer, preferences :: [[integer]], pairs :: [[integer]]) :: integer
  def unhappy_friends(n, preferences, pairs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func unhappyFriends(n: Int64, preferences: Array<Array<Int64>>, pairs: Array<Array<Int64>>): Int64 {

    }
}
```

