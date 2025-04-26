# 990. 等式方程的可满足性

## 题目描述

<p>给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 <code>equations[i]</code> 的长度为 <code>4</code>，并采用两种不同的形式之一：<code>&quot;a==b&quot;</code> 或&nbsp;<code>&quot;a!=b&quot;</code>。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。</p>

<p>只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回&nbsp;<code>true</code>，否则返回 <code>false</code>。&nbsp;</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[&quot;a==b&quot;,&quot;b!=a&quot;]
<strong>输出：</strong>false
<strong>解释：</strong>如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[&quot;b==a&quot;,&quot;a==b&quot;]
<strong>输出：</strong>true
<strong>解释：</strong>我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[&quot;a==b&quot;,&quot;b==c&quot;,&quot;a==c&quot;]
<strong>输出：</strong>true
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>[&quot;a==b&quot;,&quot;b!=c&quot;,&quot;c==a&quot;]
<strong>输出：</strong>false
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>[&quot;c==c&quot;,&quot;b==d&quot;,&quot;x!=z&quot;]
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= equations.length &lt;= 500</code></li>
	<li><code>equations[i].length == 4</code></li>
	<li><code>equations[i][0]</code> 和&nbsp;<code>equations[i][3]</code>&nbsp;是小写字母</li>
	<li><code>equations[i][1]</code> 要么是&nbsp;<code>&#39;=&#39;</code>，要么是&nbsp;<code>&#39;!&#39;</code></li>
	<li><code>equations[i][2]</code>&nbsp;是&nbsp;<code>&#39;=&#39;</code></li>
</ol>


## 难度

Medium

## 标签

- 并查集
- 图
- 数组
- 字符串

## 示例

```
["a==b","b!=a"]
["b==a","a==b"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean equationsPossible(String[] equations) {
        
    }
}
```

### Python

```python
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
```

### C

```c
bool equationsPossible(char** equations, int equationsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool EquationsPossible(string[] equations) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} equations
 * @return {boolean}
 */
var equationsPossible = function(equations) {
    
};
```

### TypeScript

```typescript
function equationsPossible(equations: string[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $equations
     * @return Boolean
     */
    function equationsPossible($equations) {
        
    }
}
```

### Swift

```swift
class Solution {
    func equationsPossible(_ equations: [String]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun equationsPossible(equations: Array<String>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool equationsPossible(List<String> equations) {
    
  }
}
```

### Go

```golang
func equationsPossible(equations []string) bool {
    
}
```

### Ruby

```ruby
# @param {String[]} equations
# @return {Boolean}
def equations_possible(equations)
    
end
```

### Scala

```scala
object Solution {
    def equationsPossible(equations: Array[String]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn equations_possible(equations: Vec<String>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (equations-possible equations)
  (-> (listof string?) boolean?)
  )
```

### Erlang

```erlang
-spec equations_possible(Equations :: [unicode:unicode_binary()]) -> boolean().
equations_possible(Equations) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec equations_possible(equations :: [String.t]) :: boolean
  def equations_possible(equations) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func equationsPossible(equations: Array<String>): Bool {

    }
}
```

