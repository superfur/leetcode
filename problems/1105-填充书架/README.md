# 1105. 填充书架

## 题目描述

<p>给定一个数组 <code>books</code> ，其中&nbsp;<code>books[i] = [thickness<sub>i</sub>, height<sub>i</sub>]</code>&nbsp;表示第 <code>i</code> 本书的厚度和高度。你也会得到一个整数 <code>shelfWidth</code> 。</p>

<p><strong>按顺序</strong>&nbsp;将这些书摆放到总宽度为 <code>shelfWidth</code> 的书架上。</p>

<p>先选几本书放在书架上（它们的厚度之和小于等于书架的宽度 <code>shelfWidth</code> ），然后再建一层书架。重复这个过程，直到把所有的书都放在书架上。</p>

<p>需要注意的是，在上述过程的每个步骤中，<strong>摆放书的顺序与给定图书数组 </strong><code>books</code><strong> 顺序相同</strong>。</p>

<ul>
	<li>例如，如果这里有 5 本书，那么可能的一种摆放情况是：第一和第二本书放在第一层书架上，第三本书放在第二层书架上，第四和第五本书放在最后一层书架上。</li>
</ul>

<p>每一层所摆放的书的最大高度就是这一层书架的层高，书架整体的高度为各层高之和。</p>

<p>以这种方式布置书架，返回书架整体可能的最小高度。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2019/06/24/shelves.png" style="width: 337px; height: 500px;" /></p>

<pre>
<strong>输入：</strong>books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
<strong>输出：</strong>6
<strong>解释：</strong>
3 层书架的高度和为 1 + 3 + 2 = 6 。
第 2 本书不必放在第一层书架上。
</pre>

<p><strong class="example">示例 2:</strong></p>

<pre>
<strong>输入:</strong> books = [[1,3],[2,4],[3,2]], shelfWidth = 6
<strong>输出:</strong> 4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= books.length &lt;= 1000</code></li>
	<li><code>1 &lt;= thickness<sub>i</sub>&nbsp;&lt;= shelfWidth &lt;= 1000</code></li>
	<li><code>1 &lt;= height<sub>i</sub>&nbsp;&lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Use dynamic programming:  dp(i) will be the answer to the problem for books[i:].

## 示例

```
[[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
4
[[1,3],[2,4],[3,2]]
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        
    }
};
```

### Java

```java
class Solution {
    public int minHeightShelves(int[][] books, int shelfWidth) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
```

### C

```c
int minHeightShelves(int** books, int booksSize, int* booksColSize, int shelfWidth) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinHeightShelves(int[][] books, int shelfWidth) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} books
 * @param {number} shelfWidth
 * @return {number}
 */
var minHeightShelves = function(books, shelfWidth) {
    
};
```

### TypeScript

```typescript
function minHeightShelves(books: number[][], shelfWidth: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $books
     * @param Integer $shelfWidth
     * @return Integer
     */
    function minHeightShelves($books, $shelfWidth) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minHeightShelves(_ books: [[Int]], _ shelfWidth: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minHeightShelves(books: Array<IntArray>, shelfWidth: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minHeightShelves(List<List<int>> books, int shelfWidth) {
    
  }
}
```

### Go

```golang
func minHeightShelves(books [][]int, shelfWidth int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} books
# @param {Integer} shelf_width
# @return {Integer}
def min_height_shelves(books, shelf_width)
    
end
```

### Scala

```scala
object Solution {
    def minHeightShelves(books: Array[Array[Int]], shelfWidth: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_height_shelves(books: Vec<Vec<i32>>, shelf_width: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-height-shelves books shelfWidth)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_height_shelves(Books :: [[integer()]], ShelfWidth :: integer()) -> integer().
min_height_shelves(Books, ShelfWidth) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_height_shelves(books :: [[integer]], shelf_width :: integer) :: integer
  def min_height_shelves(books, shelf_width) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minHeightShelves(books: Array<Array<Int64>>, shelfWidth: Int64): Int64 {

    }
}
```

