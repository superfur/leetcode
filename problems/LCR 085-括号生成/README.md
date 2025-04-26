# LCR 085. 括号生成

## 题目描述

<p>正整数&nbsp;<code>n</code>&nbsp;代表生成括号的对数，请设计一个函数，用于能够生成所有可能的并且 <strong>有效的 </strong>括号组合。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>[&quot;((()))&quot;,&quot;(()())&quot;,&quot;(())()&quot;,&quot;()(())&quot;,&quot;()()()&quot;]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>[&quot;()&quot;]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 22&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/generate-parentheses/">https://leetcode-cn.com/problems/generate-parentheses/</a></p>


## 难度

Medium

## 标签

- 字符串
- 动态规划
- 回溯

## 示例

```
3
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {

    }
};
```

### Java

```java
class Solution {
    public List<String> generateParenthesis(int n) {

    }
}
```

### Python

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
```

### Python3

```python3
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
```

### C

```c


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** generateParenthesis(int n, int* returnSize){

}
```

### C#

```csharp
public class Solution {
    public IList<string> GenerateParenthesis(int n) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {

};
```

### TypeScript

```typescript
function generateParenthesis(n: number): string[] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return String[]
     */
    function generateParenthesis($n) {

    }
}
```

### Swift

```swift
class Solution {
    func generateParenthesis(_ n: Int) -> [String] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun generateParenthesis(n: Int): List<String> {

    }
}
```

### Go

```golang
func generateParenthesis(n int) []string {

}
```

### Ruby

```ruby
# @param {Integer} n
# @return {String[]}
def generate_parenthesis(n)

end
```

### Scala

```scala
object Solution {
    def generateParenthesis(n: Int): List[String] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {

    }
}
```

### Racket

```racket
(define/contract (generate-parenthesis n)
  (-> exact-integer? (listof string?))

  )
```

### Erlang

```erlang
-spec generate_parenthesis(N :: integer()) -> [unicode:unicode_binary()].
generate_parenthesis(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec generate_parenthesis(n :: integer) :: [String.t]
  def generate_parenthesis(n) do

  end
end
```

