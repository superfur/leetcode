# 282. 给表达式添加运算符

## 题目描述

<p>给定一个仅包含数字&nbsp;<code>0-9</code>&nbsp;的字符串 <code>num</code> 和一个目标值整数 <code>target</code> ，在 <code>num</code> 的数字之间添加 <strong>二元 </strong>运算符（不是一元）<code>+</code>、<code>-</code>&nbsp;或&nbsp;<code>*</code>&nbsp;，返回 <strong>所有</strong> 能够得到 <code>target </code>的表达式。</p>

<p>注意，返回表达式中的操作数 <strong>不应该</strong> 包含前导零。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <code>num = </code>"123", target = 6
<strong>输出: </strong>["1+2+3", "1*2*3"] 
<strong>解释: </strong>“1*2*3” 和 “1+2+3” 的值都是6。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> <code>num = </code>"232", target = 8
<strong>输出: </strong>["2*3+2", "2+3*2"]
<strong>解释:</strong> “2*3+2” 和 “2+3*2” 的值都是8。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> <code>num = </code>"3456237490", target = 9191
<strong>输出: </strong>[]
<strong>解释: </strong>表达式 “3456237490” 无法得到 9191 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10</code></li>
	<li><code>num</code> 仅含数字</li>
	<li><code>-2<sup>31</sup> &lt;= target &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 字符串
- 回溯

## 提示

1. Note that a number can contain multiple digits.
2. Since the question asks us to find <b>all</b> of the valid expressions, we need a way to iterate over all of them. (<b>Hint:</b> Recursion!)
3. We can keep track of the expression string and evaluate it at the very end. But that would take a lot of time. Can we keep track of the expression's value as well so as to avoid the evaluation at the very end of recursion?
4. Think carefully about the multiply operator. It has a higher precedence than the addition and subtraction operators. 

<br> 1 + 2 = 3  <br>
1 + 2 - 4 --> 3 - 4 --> -1 <br>
1 + 2 - 4 * 12 --> -1 * 12 --> -12 (WRONG!) <br>
1 + 2 - 4 * 12 --> -1 - (-4) + (-4 * 12) --> 3 + (-48) --> -45 (CORRECT!)
5. We simply need to keep track of the last operand in our expression and reverse it's effect on the expression's value while considering the multiply operator.

## 示例

```
"123"
6
"232"
8
"3456237490"
9191
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> addOperators(string num, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> addOperators(String num, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** addOperators(char* num, int target, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> AddOperators(string num, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @param {number} target
 * @return {string[]}
 */
var addOperators = function(num, target) {
    
};
```

### TypeScript

```typescript
function addOperators(num: string, target: number): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @param Integer $target
     * @return String[]
     */
    function addOperators($num, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func addOperators(_ num: String, _ target: Int) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun addOperators(num: String, target: Int): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> addOperators(String num, int target) {
    
  }
}
```

### Go

```golang
func addOperators(num string, target int) []string {
    
}
```

### Ruby

```ruby
# @param {String} num
# @param {Integer} target
# @return {String[]}
def add_operators(num, target)
    
end
```

### Scala

```scala
object Solution {
    def addOperators(num: String, target: Int): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn add_operators(num: String, target: i32) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (add-operators num target)
  (-> string? exact-integer? (listof string?))
  )
```

### Erlang

```erlang
-spec add_operators(Num :: unicode:unicode_binary(), Target :: integer()) -> [unicode:unicode_binary()].
add_operators(Num, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec add_operators(num :: String.t, target :: integer) :: [String.t]
  def add_operators(num, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func addOperators(num: String, target: Int64): ArrayList<String> {

    }
}
```

