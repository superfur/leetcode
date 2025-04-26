# 753. 破解保险箱

## 题目描述

<p>有一个需要密码才能打开的保险箱。密码是&nbsp;<code>n</code> 位数, 密码的每一位都是范围&nbsp;<code>[0, k - 1]</code>&nbsp;中的一个数字。</p>

<p>保险箱有一种特殊的密码校验方法，你可以随意输入密码序列，保险箱会自动记住 <strong>最后&nbsp;<code>n</code>&nbsp;位输入</strong> ，如果匹配，则能够打开保险箱。</p>

<ul>
	<li>例如，正确的密码是 <code>"345"</code> ，并且你输入的是 <code>"012345"</code> ：

	<ul>
		<li>输入 <code>0</code> 之后，最后 <code>3</code> 位输入是 <code>"0"</code> ，不正确。</li>
		<li>输入 <code>1</code> 之后，最后 <code>3</code> 位输入是 <code>"01"</code> ，不正确。</li>
		<li>输入 <code>2</code> 之后，最后 <code>3</code> 位输入是 <code>"012"</code> ，不正确。</li>
		<li>输入 <code>3</code> 之后，最后 <code>3</code> 位输入是 <code>"123"</code> ，不正确。</li>
		<li>输入 <code>4</code> 之后，最后 <code>3</code> 位输入是 <code>"234"</code> ，不正确。</li>
		<li>输入 <code>5</code> 之后，最后 <code>3</code> 位输入是 <code>"345"</code> ，正确，打开保险箱。</li>
	</ul>
	</li>
</ul>

<p>在只知道密码位数 <code>n</code> 和范围边界 <code>k</code> 的前提下，请你找出并返回确保在输入的 <strong>某个时刻</strong> 能够打开保险箱的任一 <strong>最短</strong> 密码序列 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1, k = 2
<strong>输出：</strong>"10"
<strong>解释：</strong>密码只有 1 位，所以输入每一位就可以。"01" 也能够确保打开保险箱。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2, k = 2
<strong>输出：</strong>"01100"
<strong>解释：</strong>对于每种可能的密码：
- "00" 从第 4 位开始输入。
- "01" 从第 1 位开始输入。
- "10" 从第 3 位开始输入。
- "11" 从第 2 位开始输入。
因此 "01100" 可以确保打开保险箱。"01100"、"10011" 和 "11001" 也可以确保打开保险箱。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 4</code></li>
	<li><code>1 &lt;= k &lt;= 10</code></li>
	<li><code>1 &lt;= k<sup>n</sup> &lt;= 4096</code></li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 图
- 欧拉回路

## 提示

1. We can think of this problem as the problem of finding an Euler path (a path visiting every edge exactly once) on the following graph: there are $$k^{n-1}$$ nodes with each node having $$k$$ edges.  It turns out this graph always has an Eulerian circuit (path starting where it ends.)

We should visit each node in "post-order" so as to not get stuck in the graph prematurely.

## 示例

```
1
2
2
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string crackSafe(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String crackSafe(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        
```

### C

```c
char* crackSafe(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string CrackSafe(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var crackSafe = function(n, k) {
    
};
```

### TypeScript

```typescript
function crackSafe(n: number, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function crackSafe($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func crackSafe(_ n: Int, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun crackSafe(n: Int, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String crackSafe(int n, int k) {
    
  }
}
```

### Go

```golang
func crackSafe(n int, k int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {String}
def crack_safe(n, k)
    
end
```

### Scala

```scala
object Solution {
    def crackSafe(n: Int, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn crack_safe(n: i32, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (crack-safe n k)
  (-> exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec crack_safe(N :: integer(), K :: integer()) -> unicode:unicode_binary().
crack_safe(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec crack_safe(n :: integer, k :: integer) :: String.t
  def crack_safe(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func crackSafe(n: Int64, k: Int64): String {

    }
}
```

