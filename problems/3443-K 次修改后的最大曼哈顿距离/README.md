# 3443. K 次修改后的最大曼哈顿距离

## 题目描述

<p>给你一个由字符 <code>'N'</code>、<code>'S'</code>、<code>'E'</code> 和 <code>'W'</code> 组成的字符串 <code>s</code>，其中 <code>s[i]</code> 表示在无限网格中的移动操作：</p>

<ul>
	<li><code>'N'</code>：向北移动 1 个单位。</li>
	<li><code>'S'</code>：向南移动 1 个单位。</li>
	<li><code>'E'</code>：向东移动 1 个单位。</li>
	<li><code>'W'</code>：向西移动 1 个单位。</li>
</ul>

<p>初始时，你位于原点 <code>(0, 0)</code>。你 <strong>最多</strong> 可以修改 <code>k</code> 个字符为任意四个方向之一。</p>

<p>请找出在 <strong>按顺序</strong> 执行所有移动操作过程中的 <strong>任意时刻</strong> ，所能达到的离原点的&nbsp;<strong>最大曼哈顿距离&nbsp;</strong>。</p>

<p><strong>曼哈顿距离&nbsp;</strong>定义为两个坐标点 <code>(x<sub>i</sub>, y<sub>i</sub>)</code> 和 <code>(x<sub>j</sub>, y<sub>j</sub>)</code> 的横向距离绝对值与纵向距离绝对值之和，即 <code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "NWSE", k = 1</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><b>解释：</b></p>

<p>将&nbsp;<code>s[2]</code>&nbsp;从&nbsp;<code>'S'</code>&nbsp;改为&nbsp;<code>'N'</code> ，字符串&nbsp;<code>s</code>&nbsp;变为&nbsp;<code>"NWNE"</code> 。</p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">移动操作</th>
			<th style="border: 1px solid black;">位置 (x, y)</th>
			<th style="border: 1px solid black;">曼哈顿距离</th>
			<th style="border: 1px solid black;">最大值</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">s[0] == 'N'</td>
			<td style="border: 1px solid black;">(0, 1)</td>
			<td style="border: 1px solid black;">0 + 1 = 1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">s[1] == 'W'</td>
			<td style="border: 1px solid black;">(-1, 1)</td>
			<td style="border: 1px solid black;">1 + 1 = 2</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">s[2] == 'N'</td>
			<td style="border: 1px solid black;">(-1, 2)</td>
			<td style="border: 1px solid black;">1 + 2 = 3</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">s[3] == 'E'</td>
			<td style="border: 1px solid black;">(0, 2)</td>
			<td style="border: 1px solid black;">0 + 2 = 2</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
	</tbody>
</table>

<p>执行移动操作过程中，距离原点的最大曼哈顿距离是 3 。</p>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "NSWWEW", k = 3</span></p>

<p><span class="example-io"><b>输出：</b>6</span></p>

<p><b>解释：</b></p>

<p>将&nbsp;<code>s[1]</code>&nbsp;从&nbsp;<code>'S'</code>&nbsp;改为&nbsp;<code>'N'</code> ，将&nbsp;<code>s[4]</code>&nbsp;从&nbsp;<code>'E'</code>&nbsp;改为&nbsp;<code>'W'</code> 。字符串&nbsp;<code>s</code>&nbsp;变为&nbsp;<code>"NNWWWW"</code>&nbsp;。</p>

<p>执行移动操作过程中，距离原点的最大曼哈顿距离是 6&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
	<li><code>s</code>&nbsp;仅由&nbsp;<code>'N'</code>、<code>'S'</code>、<code>'E'</code>&nbsp;和&nbsp;<code>'W'</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 数学
- 字符串
- 计数

## 提示

1. We can brute force all the possible directions (NE, NW, SE, SW).
2. Change up to <code>k</code> characters to maximize the distance in the chosen direction.

## 示例

```
"NWSE"
1
"NSWWEW"
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxDistance(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxDistance(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        
```

### C

```c
int maxDistance(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxDistance(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxDistance = function(s, k) {
    
};
```

### TypeScript

```typescript
function maxDistance(s: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function maxDistance($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxDistance(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxDistance(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxDistance(String s, int k) {
    
  }
}
```

### Go

```golang
func maxDistance(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_distance(s, k)
    
end
```

### Scala

```scala
object Solution {
    def maxDistance(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_distance(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-distance s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_distance(S :: unicode:unicode_binary(), K :: integer()) -> integer().
max_distance(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_distance(s :: String.t, k :: integer) :: integer
  def max_distance(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxDistance(s: String, k: Int64): Int64 {

    }
}
```

