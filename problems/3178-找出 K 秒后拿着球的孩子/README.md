# 3178. 找出 K 秒后拿着球的孩子

## 题目描述

<p>给你两个 <strong>正整数 </strong><code>n</code> 和 <code>k</code>。有 <code>n</code> 个编号从 <code>0</code> 到 <code>n - 1</code> 的孩子按顺序从左到右站成一队。</p>

<p>最初，编号为 0 的孩子拿着一个球，并且向右传球。每过一秒，拿着球的孩子就会将球传给他旁边的孩子。一旦球到达队列的 <strong>任一端 </strong>，即编号为 0 的孩子或编号为 <code>n - 1</code> 的孩子处，传球方向就会<strong> 反转 </strong>。</p>

<p>返回 <code>k</code> 秒后接到球的孩子的编号。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">n = 3, k = 5</span></p>

<p><strong>输出：</strong><span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>经过的时间</th>
			<th>孩子队列</th>
		</tr>
		<tr>
			<td><code>0</code></td>
			<td><code>[<u>0</u>, 1, 2]</code></td>
		</tr>
		<tr>
			<td><code>1</code></td>
			<td><code>[0, <u>1</u>, 2]</code></td>
		</tr>
		<tr>
			<td><code>2</code></td>
			<td><code>[0, 1, <u>2</u>]</code></td>
		</tr>
		<tr>
			<td><code>3</code></td>
			<td><code>[0, <u>1</u>, 2]</code></td>
		</tr>
		<tr>
			<td><code>4</code></td>
			<td><code>[<u>0</u>, 1, 2]</code></td>
		</tr>
		<tr>
			<td><code>5</code></td>
			<td><code>[0, <u>1</u>, 2]</code></td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">n = 5, k = 6</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>经过的时间</th>
			<th>孩子队列</th>
		</tr>
		<tr>
			<td><code>0</code></td>
			<td><code>[<u>0</u>, 1, 2, 3, 4]</code></td>
		</tr>
		<tr>
			<td><code>1</code></td>
			<td><code>[0, <u>1</u>, 2, 3, 4]</code></td>
		</tr>
		<tr>
			<td><code>2</code></td>
			<td><code>[0, 1, <u>2</u>, 3, 4]</code></td>
		</tr>
		<tr>
			<td><code>3</code></td>
			<td><code>[0, 1, 2, <u>3</u>, 4]</code></td>
		</tr>
		<tr>
			<td><code>4</code></td>
			<td><code>[0, 1, 2, 3, <u>4</u>]</code></td>
		</tr>
		<tr>
			<td><code>5</code></td>
			<td><code>[0, 1, 2, <u>3</u>, 4]</code></td>
		</tr>
		<tr>
			<td><code>6</code></td>
			<td><code>[0, 1, <u>2</u>, 3, 4]</code></td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">n = 4, k = 2</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>经过的时间</th>
			<th>孩子队列</th>
		</tr>
		<tr>
			<td><code>0</code></td>
			<td><code>[<u>0</u>, 1, 2, 3]</code></td>
		</tr>
		<tr>
			<td><code>1</code></td>
			<td><code>[0, <u>1</u>, 2, 3]</code></td>
		</tr>
		<tr>
			<td><code>2</code></td>
			<td><code>[0, 1, <u>2</u>, 3]</code></td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>此问题与 <a href="https://leetcode.cn/problems/pass-the-pillow/">2582. 递枕头</a>&nbsp;一致。</p>


## 难度

Easy

## 标签

- 数学
- 模拟

## 提示

1. The ball will go back to child 0 after <code>2 * (n - 1)</code> seconds and everything is the same as time 0.
2. So the answer for <code>k</code> is the same as the answer for <code>k % (2 * (n - 1))</code>.

## 示例

```
3
5
5
6
4
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfChild(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfChild(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        
```

### C

```c
int numberOfChild(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfChild(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var numberOfChild = function(n, k) {
    
};
```

### TypeScript

```typescript
function numberOfChild(n: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function numberOfChild($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfChild(_ n: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfChild(n: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfChild(int n, int k) {
    
  }
}
```

### Go

```golang
func numberOfChild(n int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def number_of_child(n, k)
    
end
```

### Scala

```scala
object Solution {
    def numberOfChild(n: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_child(n: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-child n k)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_child(N :: integer(), K :: integer()) -> integer().
number_of_child(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_child(n :: integer, k :: integer) :: integer
  def number_of_child(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfChild(n: Int64, k: Int64): Int64 {

    }
}
```

