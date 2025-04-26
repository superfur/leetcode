# 2698. 求一个整数的惩罚数

## 题目描述

<p>给你一个正整数&nbsp;<code>n</code>&nbsp;，请你返回&nbsp;<code>n</code>&nbsp;的&nbsp;<strong>惩罚数</strong>&nbsp;。</p>

<p><code>n</code>&nbsp;的 <strong>惩罚数</strong>&nbsp;定义为所有满足以下条件 <code>i</code>&nbsp;的数的平方和：</p>

<ul>
	<li><code>1 &lt;= i &lt;= n</code></li>
	<li><code>i * i</code> 的十进制表示的字符串可以分割成若干连续子字符串，且这些子字符串对应的整数值之和等于 <code>i</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>n = 10
<b>输出：</b>182
<b>解释：</b>总共有 3 个范围在 [1, 10] 的整数 i 满足要求：
- 1 ，因为 1 * 1 = 1
- 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。
- 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。
因此，10 的惩罚数为 1 + 81 + 100 = 182
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>n = 37
<b>输出：</b>1478
<b>解释：</b>总共有 4 个范围在 [1, 37] 的整数 i 满足要求：
- 1 ，因为 1 * 1 = 1
- 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。
- 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。
- 36 ，因为 36 * 36 = 1296 ，且 1296 可以分割成 1 + 29 + 6 。
因此，37 的惩罚数为 1 + 81 + 100 + 1296 = 1478
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
- 回溯

## 提示

1. Can we generate all possible partitions of a number?
2. Use a recursive algorithm that splits the number into two parts, generates all possible partitions of each part recursively, and then combines them in all possible ways.

## 示例

```
10
37
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int punishmentNumber(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int punishmentNumber(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def punishmentNumber(self, n: int) -> int:
        
```

### C

```c
int punishmentNumber(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int PunishmentNumber(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var punishmentNumber = function(n) {
    
};
```

### TypeScript

```typescript
function punishmentNumber(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function punishmentNumber($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func punishmentNumber(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun punishmentNumber(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int punishmentNumber(int n) {
    
  }
}
```

### Go

```golang
func punishmentNumber(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def punishment_number(n)
    
end
```

### Scala

```scala
object Solution {
    def punishmentNumber(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn punishment_number(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (punishment-number n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec punishment_number(N :: integer()) -> integer().
punishment_number(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec punishment_number(n :: integer) :: integer
  def punishment_number(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func punishmentNumber(n: Int64): Int64 {

    }
}
```

