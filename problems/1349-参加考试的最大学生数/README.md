# 1349. 参加考试的最大学生数

## 题目描述

<p>给你一个&nbsp;<code>m&nbsp;* n</code>&nbsp;的矩阵 <code>seats</code>&nbsp;表示教室中的座位分布。如果座位是坏的（不可用），就用&nbsp;<code>'#'</code>&nbsp;表示；否则，用&nbsp;<code>'.'</code>&nbsp;表示。</p>

<p>学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的同时参加考试且无法作弊的&nbsp;<strong>最大&nbsp;</strong>学生人数。</p>

<p>学生必须坐在状况良好的座位上。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/09/image.png" style="height: 197px; width: 339px;" /></p>

<pre>
<strong>输入：</strong>seats = [["#",".","#","#",".","#"],
&nbsp;             [".","#","#","#","#","."],
&nbsp;             ["#",".","#","#",".","#"]]
<strong>输出：</strong>4
<strong>解释：</strong>教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>seats = [[".","#"],
&nbsp;             ["#","#"],
&nbsp;             ["#","."],
&nbsp;             ["#","#"],
&nbsp;             [".","#"]]
<strong>输出：</strong>3
<strong>解释：</strong>让所有学生坐在可用的座位上。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>seats = [["#",".","<strong>.</strong>",".","#"],
&nbsp;             ["<strong>.</strong>","#","<strong>.</strong>","#","<strong>.</strong>"],
&nbsp;             ["<strong>.</strong>",".","#",".","<strong>.</strong>"],
&nbsp;             ["<strong>.</strong>","#","<strong>.</strong>","#","<strong>.</strong>"],
&nbsp;             ["#",".","<strong>.</strong>",".","#"]]
<strong>输出：</strong>10
<strong>解释：</strong>让学生坐在第 1、3 和 5 列的可用座位上。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>seats</code>&nbsp;只包含字符&nbsp;<code>'.'&nbsp;和</code><code>'#'</code></li>
	<li><code>m ==&nbsp;seats.length</code></li>
	<li><code>n ==&nbsp;seats[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 8</code></li>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划
- 状态压缩
- 矩阵

## 提示

1. Students in row i only can see exams in row i+1.
2. Use Dynamic programming to compute the result given a (current row, bitmask people seated in previous row).

## 示例

```
[["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]
[[".","#"],["#","#"],["#","."],["#","#"],[".","#"]]
[["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxStudents(vector<vector<char>>& seats) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxStudents(char[][] seats) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        
```

### C

```c
int maxStudents(char** seats, int seatsSize, int* seatsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxStudents(char[][] seats) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} seats
 * @return {number}
 */
var maxStudents = function(seats) {
    
};
```

### TypeScript

```typescript
function maxStudents(seats: string[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $seats
     * @return Integer
     */
    function maxStudents($seats) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxStudents(_ seats: [[Character]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxStudents(seats: Array<CharArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxStudents(List<List<String>> seats) {
    
  }
}
```

### Go

```golang
func maxStudents(seats [][]byte) int {
    
}
```

### Ruby

```ruby
# @param {Character[][]} seats
# @return {Integer}
def max_students(seats)
    
end
```

### Scala

```scala
object Solution {
    def maxStudents(seats: Array[Array[Char]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_students(seats: Vec<Vec<char>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-students seats)
  (-> (listof (listof char?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_students(Seats :: [[char()]]) -> integer().
max_students(Seats) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_students(seats :: [[char]]) :: integer
  def max_students(seats) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxStudents(seats: Array<Array<Rune>>): Int64 {

    }
}
```

