# 3129. 找出所有稳定的二进制数组 I

## 题目描述

<p>给你 3 个正整数&nbsp;<code>zero</code>&nbsp;，<code>one</code>&nbsp;和&nbsp;<code>limit</code>&nbsp;。</p>

<p>一个 <span data-keyword="binary-array">二进制数组</span> <code>arr</code> 如果满足以下条件，那么我们称它是 <strong>稳定的</strong> ：</p>

<ul>
	<li>0 在&nbsp;<code>arr</code>&nbsp;中出现次数 <strong>恰好</strong>&nbsp;为<strong>&nbsp;</strong><code>zero</code>&nbsp;。</li>
	<li>1 在&nbsp;<code>arr</code>&nbsp;中出现次数 <strong>恰好</strong>&nbsp;为&nbsp;<code>one</code>&nbsp;。</li>
	<li><code>arr</code> 中每个长度超过 <code>limit</code>&nbsp;的 <span data-keyword="subarray-nonempty">子数组</span> 都 <strong>同时</strong> 包含 0 和 1 。</li>
</ul>

<p>请你返回 <strong>稳定</strong>&nbsp;二进制数组的 <em>总</em> 数目。</p>

<p>由于答案可能很大，将它对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<b>取余</b>&nbsp;后返回。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>zero = 1, one = 1, limit = 2</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>两个稳定的二进制数组为&nbsp;<code>[1,0]</code> 和&nbsp;<code>[0,1]</code>&nbsp;，两个数组都有一个 0 和一个 1 ，且没有子数组长度大于 2 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">zero = 1, one = 2, limit = 1</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><strong>解释：</strong></p>

<p>唯一稳定的二进制数组是&nbsp;<code>[1,0,1]</code>&nbsp;。</p>

<p>二进制数组&nbsp;<code>[1,1,0]</code> 和&nbsp;<code>[0,1,1]</code>&nbsp;都有长度为 2 且元素全都相同的子数组，所以它们不稳定。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>zero = 3, one = 3, limit = 2</span></p>

<p><span class="example-io"><b>输出：</b>14</span></p>

<p><strong>解释：</strong></p>

<p>所有稳定的二进制数组包括&nbsp;<code>[0,0,1,0,1,1]</code>&nbsp;，<code>[0,0,1,1,0,1]</code>&nbsp;，<code>[0,1,0,0,1,1]</code>&nbsp;，<code>[0,1,0,1,0,1]</code>&nbsp;，<code>[0,1,0,1,1,0]</code>&nbsp;，<code>[0,1,1,0,0,1]</code>&nbsp;，<code>[0,1,1,0,1,0]</code>&nbsp;，<code>[1,0,0,1,0,1]</code>&nbsp;，<code>[1,0,0,1,1,0]</code>&nbsp;，<code>[1,0,1,0,0,1]</code>&nbsp;，<code>[1,0,1,0,1,0]</code>&nbsp;，<code>[1,0,1,1,0,0]</code>&nbsp;，<code>[1,1,0,0,1,0]</code>&nbsp;和&nbsp;<code>[1,1,0,1,0,0]</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= zero, one, limit &lt;= 200</code></li>
</ul>


## 难度

Medium

## 标签

- 动态规划
- 前缀和

## 提示

1. Let <code>dp[a][b][c = 0/1][d]</code> be the number of stable arrays with exactly <code>a</code> 0s, <code>b</code> 1s and consecutive <code>d</code> value of <code>c</code>’s at the end.
2. Try each case by appending a 0/1 at last to get the inductions.

## 示例

```
1
1
2
1
2
1
3
3
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfStableArrays(int zero, int one, int limit) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfStableArrays(int zero, int one, int limit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        
```

### C

```c
int numberOfStableArrays(int zero, int one, int limit) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfStableArrays(int zero, int one, int limit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} zero
 * @param {number} one
 * @param {number} limit
 * @return {number}
 */
var numberOfStableArrays = function(zero, one, limit) {
    
};
```

### TypeScript

```typescript
function numberOfStableArrays(zero: number, one: number, limit: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $zero
     * @param Integer $one
     * @param Integer $limit
     * @return Integer
     */
    function numberOfStableArrays($zero, $one, $limit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfStableArrays(_ zero: Int, _ one: Int, _ limit: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfStableArrays(zero: Int, one: Int, limit: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfStableArrays(int zero, int one, int limit) {
    
  }
}
```

### Go

```golang
func numberOfStableArrays(zero int, one int, limit int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} zero
# @param {Integer} one
# @param {Integer} limit
# @return {Integer}
def number_of_stable_arrays(zero, one, limit)
    
end
```

### Scala

```scala
object Solution {
    def numberOfStableArrays(zero: Int, one: Int, limit: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_stable_arrays(zero: i32, one: i32, limit: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-stable-arrays zero one limit)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_stable_arrays(Zero :: integer(), One :: integer(), Limit :: integer()) -> integer().
number_of_stable_arrays(Zero, One, Limit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_stable_arrays(zero :: integer, one :: integer, limit :: integer) :: integer
  def number_of_stable_arrays(zero, one, limit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfStableArrays(zero: Int64, one: Int64, limit: Int64): Int64 {

    }
}
```

