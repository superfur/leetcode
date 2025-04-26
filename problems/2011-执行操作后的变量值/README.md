# 2011. 执行操作后的变量值

## 题目描述

<p>存在一种仅支持 4 种操作和 1 个变量 <code>X</code> 的编程语言：</p>

<ul>
	<li><code>++X</code> 和 <code>X++</code> 使变量 <code>X</code> 的值 <strong>加</strong> <code>1</code></li>
	<li><code>--X</code> 和 <code>X--</code> 使变量 <code>X</code> 的值 <strong>减</strong> <code>1</code></li>
</ul>

<p>最初，<code>X</code> 的值是 <code>0</code></p>

<p>给你一个字符串数组 <code>operations</code> ，这是由操作组成的一个列表，返回执行所有操作后，<em> </em><code>X</code> 的 <strong>最终值</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>operations = ["--X","X++","X++"]
<strong>输出：</strong>1
<strong>解释：</strong>操作按下述步骤执行：
最初，X = 0
--X：X 减 1 ，X =  0 - 1 = -1
X++：X 加 1 ，X = -1 + 1 =  0
X++：X 加 1 ，X =  0 + 1 =  1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>operations = ["++X","++X","X++"]
<strong>输出：</strong>3
<strong>解释：</strong>操作按下述步骤执行： 
最初，X = 0
++X：X 加 1 ，X = 0 + 1 = 1
++X：X 加 1 ，X = 1 + 1 = 2
X++：X 加 1 ，X = 2 + 1 = 3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>operations = ["X++","++X","--X","X--"]
<strong>输出：</strong>0
<strong>解释：</strong>操作按下述步骤执行：
最初，X = 0
X++：X 加 1 ，X = 0 + 1 = 1
++X：X 加 1 ，X = 1 + 1 = 2
--X：X 减 1 ，X = 2 - 1 = 1
X--：X 减 1 ，X = 1 - 1 = 0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= operations.length &lt;= 100</code></li>
	<li><code>operations[i]</code> 将会是 <code>"++X"</code>、<code>"X++"</code>、<code>"--X"</code> 或 <code>"X--"</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串
- 模拟

## 提示

1. There are only two operations to keep track of.
2. Use a variable to store the value after each operation.

## 示例

```
["--X","X++","X++"]
["++X","++X","X++"]
["X++","++X","--X","X--"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        
    }
};
```

### Java

```java
class Solution {
    public int finalValueAfterOperations(String[] operations) {
        
    }
}
```

### Python

```python
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
```

### C

```c
int finalValueAfterOperations(char** operations, int operationsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FinalValueAfterOperations(string[] operations) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    
};
```

### TypeScript

```typescript
function finalValueAfterOperations(operations: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $operations
     * @return Integer
     */
    function finalValueAfterOperations($operations) {
        
    }
}
```

### Swift

```swift
class Solution {
    func finalValueAfterOperations(_ operations: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun finalValueAfterOperations(operations: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int finalValueAfterOperations(List<String> operations) {
    
  }
}
```

### Go

```golang
func finalValueAfterOperations(operations []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} operations
# @return {Integer}
def final_value_after_operations(operations)
    
end
```

### Scala

```scala
object Solution {
    def finalValueAfterOperations(operations: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (final-value-after-operations operations)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec final_value_after_operations(Operations :: [unicode:unicode_binary()]) -> integer().
final_value_after_operations(Operations) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec final_value_after_operations(operations :: [String.t]) :: integer
  def final_value_after_operations(operations) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func finalValueAfterOperations(operations: Array<String>): Int64 {

    }
}
```

