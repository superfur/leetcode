# 668. 乘法表中第k小的数

## 题目描述

<p>几乎每一个人都用&nbsp;<a href="https://baike.baidu.com/item/%E4%B9%98%E6%B3%95%E8%A1%A8">乘法表</a>。但是你能在乘法表中快速找到第 <code>k</code> 小的数字吗？</p>

<p>乘法表是大小为 <code>m x n</code> 的一个整数矩阵，其中&nbsp;<code>mat[i][j] == i * j</code>（下标从 <strong>1</strong> 开始）。</p>

<p>给你三个整数 <code>m</code>、<code>n</code> 和 <code>k</code>，请你在大小为&nbsp;<code>m x n</code> 的乘法表中，找出并返回第 <code>k</code>&nbsp;小的数字。</p>

<div class="original__bRMd">
<div>
<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/02/multtable1-grid.jpg" style="width: 500px; height: 254px;" />
<pre>
<strong>输入：</strong>m = 3, n = 3, k = 5
<strong>输出：</strong>3
<strong>解释：</strong>第 5 小的数字是 3 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/02/multtable2-grid.jpg" style="width: 493px; height: 293px;" />
<pre>
<strong>输入：</strong>m = 2, n = 3, k = 6
<strong>输出：</strong>6
<strong>解释：</strong>第 6 小的数字是 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= m * n</code></li>
</ul>
</div>
</div>


## 难度

Hard

## 标签

- 数学
- 二分查找

## 示例

```
3
3
5
2
3
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findKthNumber(int m, int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int findKthNumber(int m, int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
```

### C

```c
int findKthNumber(int m, int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindKthNumber(int m, int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findKthNumber = function(m, n, k) {
    
};
```

### TypeScript

```typescript
function findKthNumber(m: number, n: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function findKthNumber($m, $n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findKthNumber(_ m: Int, _ n: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findKthNumber(m: Int, n: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findKthNumber(int m, int n, int k) {
    
  }
}
```

### Go

```golang
func findKthNumber(m int, n int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} m
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def find_kth_number(m, n, k)
    
end
```

### Scala

```scala
object Solution {
    def findKthNumber(m: Int, n: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_kth_number(m: i32, n: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-kth-number m n k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_kth_number(M :: integer(), N :: integer(), K :: integer()) -> integer().
find_kth_number(M, N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_kth_number(m :: integer, n :: integer, k :: integer) :: integer
  def find_kth_number(m, n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findKthNumber(m: Int64, n: Int64, k: Int64): Int64 {

    }
}
```

