# 526. 优美的排列

## 题目描述

<p>假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 <code>perm</code>（<strong>下标从 1 开始</strong>），只要满足下述条件 <strong>之一</strong> ，该数组就是一个 <strong>优美的排列</strong> ：</p>

<ul>
	<li><code>perm[i]</code> 能够被 <code>i</code> 整除</li>
	<li><code>i</code> 能够被 <code>perm[i]</code> 整除</li>
</ul>

<p>给你一个整数 <code>n</code> ，返回可以构造的 <strong>优美排列 </strong>的 <strong>数量</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>2
<b>解释：</b>
第 1 个优美的排列是 [1,2]：
    - perm[1] = 1 能被 i = 1 整除
    - perm[2] = 2 能被 i = 2 整除
第 2 个优美的排列是 [2,1]:
    - perm[1] = 2 能被 i = 1 整除
    - i = 2 能被 perm[2] = 1 整除
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 15</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 动态规划
- 回溯
- 状态压缩

## 示例

```
2
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countArrangement(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int countArrangement(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countArrangement(self, n: int) -> int:
        
```

### C

```c
int countArrangement(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountArrangement(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countArrangement = function(n) {
    
};
```

### TypeScript

```typescript
function countArrangement(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countArrangement($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countArrangement(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countArrangement(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countArrangement(int n) {
    
  }
}
```

### Go

```golang
func countArrangement(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def count_arrangement(n)
    
end
```

### Scala

```scala
object Solution {
    def countArrangement(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_arrangement(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-arrangement n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_arrangement(N :: integer()) -> integer().
count_arrangement(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_arrangement(n :: integer) :: integer
  def count_arrangement(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countArrangement(n: Int64): Int64 {

    }
}
```

