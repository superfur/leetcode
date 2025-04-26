# 2481. 分割圆的最少切割次数

## 题目描述

<p>圆内一个 <strong>有效切割</strong>&nbsp;，符合以下二者之一：</p>

<ul>
	<li>该切割是两个端点在圆上的线段，且该线段经过圆心。</li>
	<li>该切割是一端在圆心另一端在圆上的线段。</li>
</ul>

<p>一些有效和无效的切割如下图所示。</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/29/alldrawio.png" style="width: 450px; height: 174px;" /></p>

<p>给你一个整数&nbsp;<code>n</code>&nbsp;，请你返回将圆切割成相等的&nbsp;<code>n</code>&nbsp;等分的&nbsp;<strong>最少</strong>&nbsp;切割次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/24/11drawio.png" style="width: 200px; height: 200px;" /></p>

<pre>
<b>输入：</b>n = 4
<b>输出：</b>2
<b>解释：</b>
上图展示了切割圆 2 次，得到四等分。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/10/24/22drawio.png" style="width: 200px; height: 201px;" /></p>

<pre>
<b>输入：</b>n = 3
<b>输出：</b>3
<strong>解释：</strong>
最少需要切割 3 次，将圆切成三等分。
少于 3 次切割无法将圆切成大小相等面积相同的 3 等分。
同时可以观察到，第一次切割无法将圆切割开。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 几何
- 数学

## 提示

1. Think about odd and even values separately.
2. When will we not have to cut the circle at all?

## 示例

```
4
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfCuts(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfCuts(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfCuts(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfCuts(self, n: int) -> int:
        
```

### C

```c
int numberOfCuts(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfCuts(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var numberOfCuts = function(n) {
    
};
```

### TypeScript

```typescript
function numberOfCuts(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function numberOfCuts($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfCuts(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfCuts(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfCuts(int n) {
    
  }
}
```

### Go

```golang
func numberOfCuts(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def number_of_cuts(n)
    
end
```

### Scala

```scala
object Solution {
    def numberOfCuts(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_cuts(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-cuts n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_cuts(N :: integer()) -> integer().
number_of_cuts(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_cuts(n :: integer) :: integer
  def number_of_cuts(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfCuts(n: Int64): Int64 {

    }
}
```

