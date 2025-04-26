# LCR 080. 组合

## 题目描述

<p>给定两个整数 <code>n</code> 和 <code>k</code>，返回 <code>1 ... n</code> 中所有可能的 <code>k</code> 个数的组合。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong>&nbsp;n = 4, k = 2
<strong>输出:</strong>
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong>&nbsp;n = 1, k = 1
<strong>输出: </strong>[[1]]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 77&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/combinations/">https://leetcode-cn.com/problems/combinations/</a></p>


## 难度

Medium

## 标签

- 数组
- 回溯

## 示例

```
4
2
1
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {

    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> combine(int n, int k) {

    }
}
```

### Python

```python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
```

### Python3

```python3
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
```

### C

```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** combine(int n, int k, int* returnSize, int** returnColumnSizes){

}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> Combine(int n, int k) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {

};
```

### TypeScript

```typescript
function combine(n: number, k: number): number[][] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer[][]
     */
    function combine($n, $k) {

    }
}
```

### Swift

```swift
class Solution {
    func combine(_ n: Int, _ k: Int) -> [[Int]] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun combine(n: Int, k: Int): List<List<Int>> {

    }
}
```

### Go

```golang
func combine(n int, k int) [][]int {

}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer[][]}
def combine(n, k)

end
```

### Scala

```scala
object Solution {
    def combine(n: Int, k: Int): List[List[Int]] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn combine(n: i32, k: i32) -> Vec<Vec<i32>> {

    }
}
```

### Racket

```racket
(define/contract (combine n k)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)))

  )
```

### Erlang

```erlang
-spec combine(N :: integer(), K :: integer()) -> [[integer()]].
combine(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec combine(n :: integer, k :: integer) :: [[integer]]
  def combine(n, k) do

  end
end
```

