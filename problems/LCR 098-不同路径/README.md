# LCR 098. 不同路径

## 题目描述

<p>一个机器人位于一个 <code>m x n</code><em>&nbsp;</em>网格的左上角 （起始点在下图中标记为 &ldquo;Start&rdquo; ）。</p>

<p>机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 &ldquo;Finish&rdquo; ）。</p>

<p>问总共有多少条不同的路径？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" /></p>

<pre>
<strong>输入：</strong>m = 3, n = 7
<strong>输出：</strong>28</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>m = 3, n = 2
<strong>输出：</strong>3
<strong>解释：</strong>
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -&gt; 向下 -&gt; 向下
2. 向下 -&gt; 向下 -&gt; 向右
3. 向下 -&gt; 向右 -&gt; 向下
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>m = 7, n = 3
<strong>输出：</strong>28
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>m = 3, n = 3
<strong>输出：</strong>6</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li>题目数据保证答案小于等于 <code>2 * 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 62&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/unique-paths/">https://leetcode-cn.com/problems/unique-paths/</a></p>


## 难度

Medium

## 标签

- 数学
- 动态规划
- 组合数学

## 示例

```
3
7
3
2
7
3
3
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {

    }
};
```

### Java

```java
class Solution {
    public int uniquePaths(int m, int n) {

    }
}
```

### Python

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
```

### C

```c


int uniquePaths(int m, int n){

}
```

### C#

```csharp
public class Solution {
    public int UniquePaths(int m, int n) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {

};
```

### TypeScript

```typescript
function uniquePaths(m: number, n: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function uniquePaths($m, $n) {

    }
}
```

### Swift

```swift
class Solution {
    func uniquePaths(_ m: Int, _ n: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun uniquePaths(m: Int, n: Int): Int {

    }
}
```

### Go

```golang
func uniquePaths(m int, n int) int {

}
```

### Ruby

```ruby
# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def unique_paths(m, n)

end
```

### Scala

```scala
object Solution {
    def uniquePaths(m: Int, n: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (unique-paths m n)
  (-> exact-integer? exact-integer? exact-integer?)

  )
```

### Erlang

```erlang
-spec unique_paths(M :: integer(), N :: integer()) -> integer().
unique_paths(M, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec unique_paths(m :: integer, n :: integer) :: integer
  def unique_paths(m, n) do

  end
end
```

