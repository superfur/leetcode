# 1860. 增长的内存泄露

## 题目描述

<p>给你两个整数 <code>memory1</code> 和 <code>memory2</code> 分别表示两个内存条剩余可用内存的位数。现在有一个程序每秒递增的速度消耗着内存。</p>

<p>在第 <code>i</code> 秒（秒数从 1 开始），有 <code>i</code> 位内存被分配到 <strong>剩余内存较多</strong> 的内存条（如果两者一样多，则分配到第一个内存条）。如果两者剩余内存都不足 <code>i</code> 位，那么程序将 <b>意外退出</b> 。</p>

<p>请你返回一个数组，包含<em> </em><code>[crashTime, memory1<sub>crash</sub>, memory2<sub>crash</sub>]</code> ，其中 <code>crashTime</code>是程序意外退出的时间（单位为秒），<em> </em><code>memory1<sub>crash</sub></code><em> </em>和<em> </em><code>memory2<sub>crash</sub></code><em> </em>分别是两个内存条最后剩余内存的位数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>memory1 = 2, memory2 = 2
<b>输出：</b>[3,1,0]
<b>解释：</b>内存分配如下：
- 第 1 秒，内存条 1 被占用 1 位内存。内存条 1 现在有 1 位剩余可用内存。
- 第 2 秒，内存条 2 被占用 2 位内存。内存条 2 现在有 0 位剩余可用内存。
- 第 3 秒，程序意外退出，两个内存条分别有 1 位和 0 位剩余可用内存。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>memory1 = 8, memory2 = 11
<b>输出：</b>[6,0,4]
<b>解释：</b>内存分配如下：
- 第 1 秒，内存条 2 被占用 1 位内存，内存条 2 现在有 10 位剩余可用内存。
- 第 2 秒，内存条 2 被占用 2 位内存，内存条 2 现在有 8 位剩余可用内存。
- 第 3 秒，内存条 1 被占用 3 位内存，内存条 1 现在有 5 位剩余可用内存。
- 第 4 秒，内存条 2 被占用 4 位内存，内存条 2 现在有 4 位剩余可用内存。
- 第 5 秒，内存条 1 被占用 5 位内存，内存条 1 现在有 0 位剩余可用内存。
- 第 6 秒，程序意外退出，两个内存条分别有 0 位和 4 位剩余可用内存。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= memory1, memory2 &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 模拟

## 提示

1. What is the upper bound for the number of seconds?
2. Simulate the process of allocating memory.

## 示例

```
2
2
8
11
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> memLeak(int memory1, int memory2) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] memLeak(int memory1, int memory2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* memLeak(int memory1, int memory2, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MemLeak(int memory1, int memory2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} memory1
 * @param {number} memory2
 * @return {number[]}
 */
var memLeak = function(memory1, memory2) {
    
};
```

### TypeScript

```typescript
function memLeak(memory1: number, memory2: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $memory1
     * @param Integer $memory2
     * @return Integer[]
     */
    function memLeak($memory1, $memory2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func memLeak(_ memory1: Int, _ memory2: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun memLeak(memory1: Int, memory2: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> memLeak(int memory1, int memory2) {
    
  }
}
```

### Go

```golang
func memLeak(memory1 int, memory2 int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} memory1
# @param {Integer} memory2
# @return {Integer[]}
def mem_leak(memory1, memory2)
    
end
```

### Scala

```scala
object Solution {
    def memLeak(memory1: Int, memory2: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn mem_leak(memory1: i32, memory2: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (mem-leak memory1 memory2)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec mem_leak(Memory1 :: integer(), Memory2 :: integer()) -> [integer()].
mem_leak(Memory1, Memory2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec mem_leak(memory1 :: integer, memory2 :: integer) :: [integer]
  def mem_leak(memory1, memory2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func memLeak(memory1: Int64, memory2: Int64): Array<Int64> {

    }
}
```

