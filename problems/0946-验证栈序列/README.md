# 946. 验证栈序列

## 题目描述

<p>给定&nbsp;<code>pushed</code>&nbsp;和&nbsp;<code>popped</code>&nbsp;两个序列，每个序列中的 <strong>值都不重复</strong>，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 <code>true</code>；否则，返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
<strong>输出：</strong>true
<strong>解释：</strong>我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -&gt; 4,
push(5), pop() -&gt; 5, pop() -&gt; 3, pop() -&gt; 2, pop() -&gt; 1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
<strong>输出：</strong>false
<strong>解释：</strong>1 不能在 2 之前弹出。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= pushed.length &lt;= 1000</code></li>
	<li><code>0 &lt;= pushed[i] &lt;= 1000</code></li>
	<li><code>pushed</code> 的所有元素 <strong>互不相同</strong></li>
	<li><code>popped.length == pushed.length</code></li>
	<li><code>popped</code> 是 <code>pushed</code> 的一个排列</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 模拟

## 示例

```
[1,2,3,4,5]
[4,5,3,2,1]
[1,2,3,4,5]
[4,3,5,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
```

### C

```c
bool validateStackSequences(int* pushed, int pushedSize, int* popped, int poppedSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ValidateStackSequences(int[] pushed, int[] popped) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function(pushed, popped) {
    
};
```

### TypeScript

```typescript
function validateStackSequences(pushed: number[], popped: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $pushed
     * @param Integer[] $popped
     * @return Boolean
     */
    function validateStackSequences($pushed, $popped) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validateStackSequences(_ pushed: [Int], _ popped: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validateStackSequences(pushed: IntArray, popped: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool validateStackSequences(List<int> pushed, List<int> popped) {
    
  }
}
```

### Go

```golang
func validateStackSequences(pushed []int, popped []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} pushed
# @param {Integer[]} popped
# @return {Boolean}
def validate_stack_sequences(pushed, popped)
    
end
```

### Scala

```scala
object Solution {
    def validateStackSequences(pushed: Array[Int], popped: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (validate-stack-sequences pushed popped)
  (-> (listof exact-integer?) (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec validate_stack_sequences(Pushed :: [integer()], Popped :: [integer()]) -> boolean().
validate_stack_sequences(Pushed, Popped) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec validate_stack_sequences(pushed :: [integer], popped :: [integer]) :: boolean
  def validate_stack_sequences(pushed, popped) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validateStackSequences(pushed: Array<Int64>, popped: Array<Int64>): Bool {

    }
}
```

