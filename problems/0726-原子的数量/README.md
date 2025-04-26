# 726. 原子的数量

## 题目描述

<p>给你一个字符串化学式 <code>formula</code> ，返回 <strong>每种原子的数量</strong> 。</p>

<p>原子总是以一个大写字母开始，接着跟随 0 个或任意个小写字母，表示原子的名字。</p>

<p>如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。</p>

<ul>
	<li>例如，<code>"H2O"</code> 和 <code>"H2O2"</code> 是可行的，但 <code>"H1O2"</code> 这个表达是不可行的。</li>
</ul>

<p>两个化学式连在一起可以构成新的化学式。</p>

<ul>
	<li>例如 <code>"H2O2He3Mg4"</code> 也是化学式。</li>
</ul>

<p>由括号括起的化学式并佐以数字（可选择性添加）也是化学式。</p>

<ul>
	<li>例如 <code>"(H2O2)"</code> 和 <code>"(H2O2)3"</code> 是化学式。</li>
</ul>

<p>返回所有原子的数量，格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>formula = "H2O"
<strong>输出：</strong>"H2O"
<strong>解释：</strong>原子的数量是 {'H': 2, 'O': 1}。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>formula = "Mg(OH)2"
<strong>输出：</strong>"H2MgO2"
<strong>解释：</strong>原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>formula = "K4(ON(SO3)2)2"
<strong>输出：</strong>"K4N2O14S4"
<strong>解释：</strong>原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= formula.length&nbsp;&lt;= 1000</code></li>
	<li><code>formula</code> 由英文字母、数字、<code>'('</code> 和 <code>')'</code> 组成</li>
	<li><code>formula</code> 总是有效的化学式</li>
</ul>


## 难度

Hard

## 标签

- 栈
- 哈希表
- 字符串
- 排序

## 提示

1. To parse formula[i:], when we see a `'('`, we will parse recursively whatever is inside the brackets (up to the correct closing ending bracket) and add it to our count, multiplying by the following multiplicity if there is one.

Otherwise, we should see an uppercase character: we will parse the rest of the letters to get the name, and add that (plus the multiplicity if there is one.)

## 示例

```
"H2O"
"Mg(OH)2"
"K4(ON(SO3)2)2"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string countOfAtoms(string formula) {
        
    }
};
```

### Java

```java
class Solution {
    public String countOfAtoms(String formula) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
```

### C

```c
char* countOfAtoms(char* formula) {
    
}
```

### C#

```csharp
public class Solution {
    public string CountOfAtoms(string formula) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} formula
 * @return {string}
 */
var countOfAtoms = function(formula) {
    
};
```

### TypeScript

```typescript
function countOfAtoms(formula: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $formula
     * @return String
     */
    function countOfAtoms($formula) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countOfAtoms(_ formula: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countOfAtoms(formula: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String countOfAtoms(String formula) {
    
  }
}
```

### Go

```golang
func countOfAtoms(formula string) string {
    
}
```

### Ruby

```ruby
# @param {String} formula
# @return {String}
def count_of_atoms(formula)
    
end
```

### Scala

```scala
object Solution {
    def countOfAtoms(formula: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_of_atoms(formula: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (count-of-atoms formula)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec count_of_atoms(Formula :: unicode:unicode_binary()) -> unicode:unicode_binary().
count_of_atoms(Formula) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_of_atoms(formula :: String.t) :: String.t
  def count_of_atoms(formula) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countOfAtoms(formula: String): String {

    }
}
```

