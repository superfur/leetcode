# 1155. 掷骰子等于目标和的方法数

## 题目描述

<p>这里有&nbsp;<code>n</code>&nbsp;个一样的骰子，每个骰子上都有&nbsp;<code>k</code>&nbsp;个面，分别标号为&nbsp;<code>1</code>&nbsp;到 <code>k</code> 。</p>

<p>给定三个整数 <code>n</code>、<code>k</code> 和 <code>target</code>，请返回投掷骰子的所有可能得到的结果（共有 <code>k<sup>n</sup></code> 种方式），使得骰子面朝上的数字总和等于 <code>target</code>。</p>

<p>由于答案可能很大，你需要对 <code>10<sup>9</sup> + 7</code> <strong>取模</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1, k = 6, target = 3
<strong>输出：</strong>1
<strong>解释：</strong>你掷了一个有 6 个面的骰子。
得到总和为 3 的结果的方式只有一种。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2, k = 6, target = 7
<strong>输出：</strong>6
<strong>解释：</strong>你掷了两个骰子，每个骰子有 6 个面。
有 6 种方式得到总和为 7 的结果: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 30, k = 30, target = 500
<strong>输出：</strong>222616187
<strong>解释：</strong>返回的结果必须对 10<sup>9</sup> + 7 取模。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, k &lt;= 30</code></li>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 动态规划

## 提示

1. Use dynamic programming.  The states are how many dice are remaining, and what sum total you have rolled so far.

## 示例

```
1
6
3
2
6
7
30
30
500
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int numRollsToTarget(int n, int k, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
```

### C

```c
int numRollsToTarget(int n, int k, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumRollsToTarget(int n, int k, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @param {number} target
 * @return {number}
 */
var numRollsToTarget = function(n, k, target) {
    
};
```

### TypeScript

```typescript
function numRollsToTarget(n: number, k: number, target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $target
     * @return Integer
     */
    function numRollsToTarget($n, $k, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numRollsToTarget(_ n: Int, _ k: Int, _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numRollsToTarget(n: Int, k: Int, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numRollsToTarget(int n, int k, int target) {
    
  }
}
```

### Go

```golang
func numRollsToTarget(n int, k int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @param {Integer} target
# @return {Integer}
def num_rolls_to_target(n, k, target)
    
end
```

### Scala

```scala
object Solution {
    def numRollsToTarget(n: Int, k: Int, target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_rolls_to_target(n: i32, k: i32, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-rolls-to-target n k target)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_rolls_to_target(N :: integer(), K :: integer(), Target :: integer()) -> integer().
num_rolls_to_target(N, K, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_rolls_to_target(n :: integer, k :: integer, target :: integer) :: integer
  def num_rolls_to_target(n, k, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numRollsToTarget(n: Int64, k: Int64, target: Int64): Int64 {

    }
}
```

