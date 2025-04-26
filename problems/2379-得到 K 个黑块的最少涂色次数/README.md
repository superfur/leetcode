# 2379. 得到 K 个黑块的最少涂色次数

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>blocks</code>&nbsp;，<code>blocks[i]</code>&nbsp;要么是&nbsp;<code>'W'</code>&nbsp;要么是&nbsp;<code>'B'</code>&nbsp;，表示第&nbsp;<code>i</code>&nbsp;块的颜色。字符&nbsp;<code>'W'</code> 和&nbsp;<code>'B'</code>&nbsp;分别表示白色和黑色。</p>

<p>给你一个整数&nbsp;<code>k</code>&nbsp;，表示想要&nbsp;<strong>连续</strong>&nbsp;黑色块的数目。</p>

<p>每一次操作中，你可以选择一个白色块将它 <strong>涂成</strong>&nbsp;黑色块。</p>

<p>请你返回至少出现 <strong>一次</strong>&nbsp;连续 <code>k</code>&nbsp;个黑色块的 <strong>最少</strong>&nbsp;操作次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>blocks = "WBBWWBBWBW", k = 7
<b>输出：</b>3
<strong>解释：</strong>
一种得到 7 个连续黑色块的方法是把第 0 ，3 和 4 个块涂成黑色。
得到 blocks = "BBBBBBBWBW" 。
可以证明无法用少于 3 次操作得到 7 个连续的黑块。
所以我们返回 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>blocks = "WBWBBBW", k = 2
<b>输出：</b>0
<strong>解释：</strong>
不需要任何操作，因为已经有 2 个连续的黑块。
所以我们返回 0 。
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>n == blocks.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>blocks[i]</code>&nbsp;要么是&nbsp;<code>'W'</code>&nbsp;，要么是&nbsp;<code>'B'</code> 。</li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 滑动窗口

## 提示

1. Iterate through all possible consecutive substrings of k characters.
2. Find the number of changes for each substring to make all blocks black, and return the minimum of these.

## 示例

```
"WBBWWBBWBW"
7
"WBWBBBW"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumRecolors(String blocks, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
```

### C

```c
int minimumRecolors(char* blocks, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumRecolors(string blocks, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} blocks
 * @param {number} k
 * @return {number}
 */
var minimumRecolors = function(blocks, k) {
    
};
```

### TypeScript

```typescript
function minimumRecolors(blocks: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $blocks
     * @param Integer $k
     * @return Integer
     */
    function minimumRecolors($blocks, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumRecolors(_ blocks: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumRecolors(blocks: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumRecolors(String blocks, int k) {
    
  }
}
```

### Go

```golang
func minimumRecolors(blocks string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} blocks
# @param {Integer} k
# @return {Integer}
def minimum_recolors(blocks, k)
    
end
```

### Scala

```scala
object Solution {
    def minimumRecolors(blocks: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_recolors(blocks: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-recolors blocks k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_recolors(Blocks :: unicode:unicode_binary(), K :: integer()) -> integer().
minimum_recolors(Blocks, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_recolors(blocks :: String.t, k :: integer) :: integer
  def minimum_recolors(blocks, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumRecolors(blocks: String, k: Int64): Int64 {

    }
}
```

