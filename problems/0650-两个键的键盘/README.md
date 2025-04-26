# 650. 两个键的键盘

## 题目描述

<p>最初记事本上只有一个字符 <code>'A'</code> 。你每次可以对这个记事本进行两种操作：</p>

<ul>
	<li><code>Copy All</code>（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。</li>
	<li><code>Paste</code>（粘贴）：粘贴<strong> 上一次 </strong>复制的字符。</li>
</ul>

<p>给你一个数字&nbsp;<code>n</code> ，你需要使用最少的操作次数，在记事本上输出 <strong>恰好</strong>&nbsp;<code>n</code>&nbsp;个 <code>'A'</code> 。返回能够打印出&nbsp;<code>n</code>&nbsp;个 <code>'A'</code> 的最少操作次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>3
<strong>输出：</strong>3
<strong>解释：</strong>
最初, 只有一个字符 'A'。
第 1 步, 使用 <strong>Copy All</strong> 操作。
第 2 步, 使用 <strong>Paste </strong>操作来获得 'AA'。
第 3 步, 使用 <strong>Paste</strong> 操作来获得 'AAA'。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 动态规划

## 提示

1. How many characters may be there in the clipboard at the last step if n = 3? n = 7? n = 10? n = 24?

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
    int minSteps(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSteps(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSteps(self, n: int) -> int:
        
```

### C

```c
int minSteps(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSteps(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var minSteps = function(n) {
    
};
```

### TypeScript

```typescript
function minSteps(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function minSteps($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSteps(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSteps(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSteps(int n) {
    
  }
}
```

### Go

```golang
func minSteps(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def min_steps(n)
    
end
```

### Scala

```scala
object Solution {
    def minSteps(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_steps(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-steps n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_steps(N :: integer()) -> integer().
min_steps(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_steps(n :: integer) :: integer
  def min_steps(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSteps(n: Int64): Int64 {

    }
}
```

