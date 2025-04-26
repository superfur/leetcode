# 3179. K 秒后第 N 个元素的值

## 题目描述

<p>给你两个整数 <code>n</code> 和 <code>k</code>。</p>

<p>最初，你有一个长度为 <code>n</code> 的整数数组 <code>a</code>，对所有 <code>0 &lt;= i &lt;= n - 1</code>，都有 <code>a[i] = 1</code> 。每过一秒，你会同时更新每个元素为其前面所有元素的和加上该元素本身。例如，一秒后，<code>a[0]</code> 保持不变，<code>a[1]</code> 变为 <code>a[0] + a[1]</code>，<code>a[2]</code> 变为 <code>a[0] + a[1] + a[2]</code>，以此类推。</p>

<p>返回 <code>k</code> 秒后 <code>a[n - 1]</code> 的<strong>值</strong>。</p>

<p>由于答案可能非常大，返回其对 <code>10<sup>9</sup> + 7</code> <strong>取余 </strong>后的结果。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">n = 4, k = 5</span></p>

<p><strong>输出：</strong><span class="example-io">56</span></p>

<p><strong>解释：</strong></p>

<table border="1">
	<tbody>
		<tr>
			<th>时间（秒）</th>
			<th>数组状态</th>
		</tr>
		<tr>
			<td>0</td>
			<td>[1,1,1,1]</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[1,2,3,4]</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[1,3,6,10]</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[1,4,10,20]</td>
		</tr>
		<tr>
			<td>4</td>
			<td>[1,5,15,35]</td>
		</tr>
		<tr>
			<td>5</td>
			<td>[1,6,21,56]</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">n = 5, k = 3</span></p>

<p><strong>输出：</strong><span class="example-io">35</span></p>

<p><strong>解释：</strong></p>

<table border="1">
	<tbody>
		<tr>
			<th>时间（秒）</th>
			<th>数组状态</th>
		</tr>
		<tr>
			<td>0</td>
			<td>[1,1,1,1,1]</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[1,2,3,4,5]</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[1,3,6,10,15]</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[1,4,10,20,35]</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, k &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 组合数学
- 前缀和
- 模拟

## 提示

1. Calculate the prefix sum array of <code>nums</code>, <code>k</code> times.

## 示例

```
4
5
5
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int valueAfterKSeconds(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int valueAfterKSeconds(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def valueAfterKSeconds(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        
```

### C

```c
int valueAfterKSeconds(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int ValueAfterKSeconds(int n, int k) {
        
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
var valueAfterKSeconds = function(n, k) {
    
};
```

### TypeScript

```typescript
function valueAfterKSeconds(n: number, k: number): number {
    
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
    function valueAfterKSeconds($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func valueAfterKSeconds(_ n: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun valueAfterKSeconds(n: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int valueAfterKSeconds(int n, int k) {
    
  }
}
```

### Go

```golang
func valueAfterKSeconds(n int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def value_after_k_seconds(n, k)
    
end
```

### Scala

```scala
object Solution {
    def valueAfterKSeconds(n: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn value_after_k_seconds(n: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (value-after-k-seconds n k)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec value_after_k_seconds(N :: integer(), K :: integer()) -> integer().
value_after_k_seconds(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec value_after_k_seconds(n :: integer, k :: integer) :: integer
  def value_after_k_seconds(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func valueAfterKSeconds(n: Int64, k: Int64): Int64 {

    }
}
```

