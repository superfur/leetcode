# LCR 040. 最大矩形

## 题目描述

<p>给定一个由&nbsp;<code>0</code> 和 <code>1</code>&nbsp;组成的矩阵 <code>matrix</code>&nbsp;，找出只包含 <code>1</code> 的最大矩形，并返回其面积。</p>

<p><strong>注意：</strong>此题 <code>matrix</code>&nbsp;输入格式为一维 <code>01</code> 字符串数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg" style="width: 402px; height: 322px;" /></p>

<pre>
<strong>输入：</strong>matrix = ["10100","10111","11111","10010"]
<strong>输出：</strong>6
<strong>解释：</strong>最大矩形如上图所示。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = []
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = ["0"]
<strong>输出：</strong>0
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>matrix = ["1"]
<strong>输出：</strong>1
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>matrix = ["00"]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>rows == matrix.length</code></li>
	<li><code>cols == matrix[0].length</code></li>
	<li><code>0 &lt;= row, cols &lt;= 200</code></li>
	<li><code>matrix[i][j]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 85 题相同（输入参数格式不同）：&nbsp;<a href="https://leetcode-cn.com/problems/maximal-rectangle/">https://leetcode-cn.com/problems/maximal-rectangle/</a></p>


## 难度

Hard

## 标签

- 栈
- 数组
- 动态规划
- 矩阵
- 单调栈

## 示例

```
["10100","10111","11111","10010"]
[]
["0"]
["1"]
["00"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximalRectangle(vector<string>& matrix) {

    }
};
```

### Java

```java
class Solution {
    public int maximalRectangle(String[] matrix) {

    }
}
```

### Python

```python
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[str]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
```

### C

```c


int maximalRectangle(char** matrix, int matrixSize){

}
```

### C#

```csharp
public class Solution {
    public int MaximalRectangle(string[] matrix) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} matrix
 * @return {number}
 */
var maximalRectangle = function(matrix) {

};
```

### TypeScript

```typescript
function maximalRectangle(matrix: string[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $matrix
     * @return Integer
     */
    function maximalRectangle($matrix) {

    }
}
```

### Swift

```swift
class Solution {
    func maximalRectangle(_ matrix: [String]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximalRectangle(matrix: Array<String>): Int {

    }
}
```

### Go

```golang
func maximalRectangle(matrix []string) int {

}
```

### Ruby

```ruby
# @param {String[]} matrix
# @return {Integer}
def maximal_rectangle(matrix)

end
```

### Scala

```scala
object Solution {
    def maximalRectangle(matrix: Array[String]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximal_rectangle(matrix: Vec<String>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (maximal-rectangle matrix)
  (-> (listof string?) exact-integer?)

  )
```

### Erlang

```erlang
-spec maximal_rectangle(Matrix :: [unicode:unicode_binary()]) -> integer().
maximal_rectangle(Matrix) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximal_rectangle(matrix :: [String.t]) :: integer
  def maximal_rectangle(matrix) do

  end
end
```

