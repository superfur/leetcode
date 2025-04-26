# 241. 为运算表达式设计优先级

## 题目描述

<p>给你一个由数字和运算符组成的字符串&nbsp;<code>expression</code> ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 <strong>按任意顺序</strong> 返回答案。</p>

<p>生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 <code>10<sup>4</sup></code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>expression = "2-1-1"
<strong>输出：</strong>[0,2]
<strong>解释：</strong>
((2-1)-1) = 0 
(2-(1-1)) = 2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>expression = "2*3-4*5"
<strong>输出：</strong>[-34,-14,-10,-10,10]
<strong>解释：</strong>
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 20</code></li>
	<li><code>expression</code> 由数字和算符 <code>'+'</code>、<code>'-'</code> 和 <code>'*'</code> 组成。</li>
	<li>输入表达式中的所有整数值在范围 <code>[0, 99]</code>&nbsp;</li>
	<li>输入表达式中的所有整数都没有前导&nbsp;<code>'-'</code>&nbsp;或&nbsp;<code>'+'</code> 表示符号。</li>
</ul>


## 难度

Medium

## 标签

- 递归
- 记忆化搜索
- 数学
- 字符串
- 动态规划

## 示例

```
"2-1-1"
"2*3-4*5"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> diffWaysToCompute(String expression) {
        
    }
}
```

### Python

```python
class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* diffWaysToCompute(char* expression, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> DiffWaysToCompute(string expression) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} expression
 * @return {number[]}
 */
var diffWaysToCompute = function(expression) {
    
};
```

### TypeScript

```typescript
function diffWaysToCompute(expression: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $expression
     * @return Integer[]
     */
    function diffWaysToCompute($expression) {
        
    }
}
```

### Swift

```swift
class Solution {
    func diffWaysToCompute(_ expression: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun diffWaysToCompute(expression: String): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> diffWaysToCompute(String expression) {
    
  }
}
```

### Go

```golang
func diffWaysToCompute(expression string) []int {
    
}
```

### Ruby

```ruby
# @param {String} expression
# @return {Integer[]}
def diff_ways_to_compute(expression)
    
end
```

### Scala

```scala
object Solution {
    def diffWaysToCompute(expression: String): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn diff_ways_to_compute(expression: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (diff-ways-to-compute expression)
  (-> string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec diff_ways_to_compute(Expression :: unicode:unicode_binary()) -> [integer()].
diff_ways_to_compute(Expression) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec diff_ways_to_compute(expression :: String.t) :: [integer]
  def diff_ways_to_compute(expression) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func diffWaysToCompute(expression: String): ArrayList<Int64> {

    }
}
```

