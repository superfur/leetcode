# 3154. 到达第 K 级台阶的方案数

## 题目描述

<p>给你有一个 <strong>非负</strong>&nbsp;整数&nbsp;<code>k</code>&nbsp;。有一个无限长度的台阶，<strong>最低</strong>&nbsp;一层编号为 0 。</p>

<p>Alice&nbsp;有一个整数&nbsp;<code>jump</code>&nbsp;，一开始值为 0 。Alice 从台阶 1 开始，可以使用 <strong>任意</strong>&nbsp;次操作，目标是到达第&nbsp;<code>k</code> 级台阶。假设 Alice 位于台阶 <code>i</code> ，一次 <strong>操作</strong> 中，Alice 可以：</p>

<ul>
	<li>向下走一级到&nbsp;<code>i - 1</code>&nbsp;，但该操作&nbsp;<strong>不能</strong>&nbsp;连续使用，如果在台阶第 0 级也不能使用。</li>
	<li>向上走到台阶&nbsp;<code>i + 2<sup>jump</sup></code>&nbsp;处，然后&nbsp;<code>jump</code>&nbsp;变为&nbsp;<code>jump + 1</code>&nbsp;。</li>
</ul>

<p>请你返回 Alice 到达台阶 <code>k</code>&nbsp;处的总方案数。</p>

<p><b>注意</b>，Alice 可能到达台阶 <code>k</code>&nbsp;处后，通过一些操作重新回到台阶 <code>k</code>&nbsp;处，这视为不同的方案。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>k = 0</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>2 种到达台阶 0 的方案为：</p>

<ul>
	<li>Alice&nbsp;从台阶&nbsp;1 开始。
	<ul>
		<li>执行第一种操作，从台阶 1 向下走到台阶 0 。</li>
	</ul>
	</li>
	<li>Alice&nbsp;从台阶 1 开始。
	<ul>
		<li>执行第一种操作，从台阶 1 向下走到台阶 0 。</li>
		<li>执行第二种操作，向上走 2<sup>0</sup>&nbsp;级台阶到台阶 1 。</li>
		<li>执行第一种操作，从台阶 1 向下走到台阶 0 。</li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>k = 1</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><strong>解释：</strong></p>

<p>4 种到达台阶 1 的方案为：</p>

<ul>
	<li>Alice&nbsp;从台阶 1 开始，已经到达台阶 1 。</li>
	<li>Alice&nbsp;从台阶 1 开始。
	<ul>
		<li>执行第一种操作，从台阶 1 向下走到台阶 0 。</li>
		<li>执行第二种操作，向上走 2<sup>0</sup>&nbsp;级台阶到台阶 1 。</li>
	</ul>
	</li>
	<li>Alice&nbsp;从台阶 1 开始。
	<ul>
		<li>执行第二种操作，向上走 2<sup>0</sup>&nbsp;级台阶到台阶 2 。</li>
		<li>执行第一种操作，向下走 1 级台阶到台阶 1 。</li>
	</ul>
	</li>
	<li>Alice&nbsp;从台阶 1 开始。
	<ul>
		<li>执行第一种操作，从台阶 1 向下走到台阶 0 。</li>
		<li>执行第二种操作，向上走&nbsp;2<sup>0</sup>&nbsp;级台阶到台阶 1 。</li>
		<li>执行第一种操作，向下走 1 级台阶到台阶 0 。</li>
		<li>执行第二种操作，向上走 2<sup>1</sup>&nbsp;级台阶到台阶 2 。</li>
		<li>执行第一种操作，向下走&nbsp;1 级台阶到台阶 1 。</li>
	</ul>
	</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 记忆化搜索
- 数学
- 动态规划
- 组合数学

## 提示

1. On using <code>x</code> operations of the second type and <code>y</code> operations of the first type, the stair <code>2<sup>x</sup> - y</code> is reached.
2. Since first operations cannot be consecutive, there are exactly <code>x + 1</code> positions (before and after each power of 2) to perform the second operation.
3. Using combinatorics, we have <sup>x + 1</sup>C<sub>y</sub> number of ways to select the positions of second operations.

## 示例

```
0
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int waysToReachStair(int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int waysToReachStair(int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def waysToReachStair(self, k):
        """
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def waysToReachStair(self, k: int) -> int:
        
```

### C

```c
int waysToReachStair(int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int WaysToReachStair(int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @return {number}
 */
var waysToReachStair = function(k) {
    
};
```

### TypeScript

```typescript
function waysToReachStair(k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @return Integer
     */
    function waysToReachStair($k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func waysToReachStair(_ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun waysToReachStair(k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int waysToReachStair(int k) {
    
  }
}
```

### Go

```golang
func waysToReachStair(k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @return {Integer}
def ways_to_reach_stair(k)
    
end
```

### Scala

```scala
object Solution {
    def waysToReachStair(k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ways_to_reach_stair(k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (ways-to-reach-stair k)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec ways_to_reach_stair(K :: integer()) -> integer().
ways_to_reach_stair(K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ways_to_reach_stair(k :: integer) :: integer
  def ways_to_reach_stair(k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func waysToReachStair(k: Int64): Int64 {

    }
}
```

