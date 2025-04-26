# 2209. 用地毯覆盖后的最少白色砖块

## 题目描述

<p>给你一个下标从<strong>&nbsp;0</strong>&nbsp;开始的 <strong>二进制</strong>&nbsp;字符串&nbsp;<code>floor</code>&nbsp;，它表示地板上砖块的颜色。</p>

<ul>
	<li><code>floor[i] = '0'</code>&nbsp;表示地板上第&nbsp;<code>i</code>&nbsp;块砖块的颜色是 <strong>黑色</strong>&nbsp;。</li>
	<li><code>floor[i] = '1'</code>&nbsp;表示地板上第&nbsp;<code>i</code>&nbsp;块砖块的颜色是 <strong>白色</strong>&nbsp;。</li>
</ul>

<p>同时给你&nbsp;<code>numCarpets</code> 和&nbsp;<code>carpetLen</code>&nbsp;。你有&nbsp;<code>numCarpets</code>&nbsp;条&nbsp;<strong>黑色</strong>&nbsp;的地毯，每一条&nbsp;<strong>黑色</strong>&nbsp;的地毯长度都为&nbsp;<code>carpetLen</code>&nbsp;块砖块。请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余 <strong>白色</strong>&nbsp;砖块的数目 <strong>最小</strong>&nbsp;。地毯相互之间可以覆盖。</p>

<p>请你返回没被覆盖的白色砖块的 <strong>最少</strong>&nbsp;数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/02/10/ex1-1.png" style="width: 400px; height: 73px;"></p>

<pre><b>输入：</b>floor = "10110101", numCarpets = 2, carpetLen = 2
<b>输出：</b>2
<b>解释：</b>
上图展示了剩余 2 块白色砖块的方案。
没有其他方案可以使未被覆盖的白色砖块少于 2 块。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/02/10/ex2.png" style="width: 353px; height: 123px;"></p>

<pre><b>输入：</b>floor = "11111", numCarpets = 2, carpetLen = 3
<b>输出：</b>0
<b>解释：</b>
上图展示了所有白色砖块都被覆盖的一种方案。
注意，地毯相互之间可以覆盖。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= carpetLen &lt;= floor.length &lt;= 1000</code></li>
	<li><code>floor[i]</code> 要么是&nbsp;<code>'0'</code>&nbsp;，要么是&nbsp;<code>'1'</code>&nbsp;。</li>
	<li><code>1 &lt;= numCarpets &lt;= 1000</code></li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划
- 前缀和

## 提示

1. Can you think of a DP solution?
2. Let DP[i][j] denote the minimum number of white tiles still visible from indices i to floor.length-1 after covering with at most j carpets.
3. The transition will be whether to put down the carpet at position i (if possible), or not.

## 示例

```
"10110101"
2
2
"11111"
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumWhiteTiles(string floor, int numCarpets, int carpetLen) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumWhiteTiles(String floor, int numCarpets, int carpetLen) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        """
        :type floor: str
        :type numCarpets: int
        :type carpetLen: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        
```

### C

```c
int minimumWhiteTiles(char* floor, int numCarpets, int carpetLen) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumWhiteTiles(string floor, int numCarpets, int carpetLen) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} floor
 * @param {number} numCarpets
 * @param {number} carpetLen
 * @return {number}
 */
var minimumWhiteTiles = function(floor, numCarpets, carpetLen) {
    
};
```

### TypeScript

```typescript
function minimumWhiteTiles(floor: string, numCarpets: number, carpetLen: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $floor
     * @param Integer $numCarpets
     * @param Integer $carpetLen
     * @return Integer
     */
    function minimumWhiteTiles($floor, $numCarpets, $carpetLen) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumWhiteTiles(_ floor: String, _ numCarpets: Int, _ carpetLen: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumWhiteTiles(floor: String, numCarpets: Int, carpetLen: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumWhiteTiles(String floor, int numCarpets, int carpetLen) {
    
  }
}
```

### Go

```golang
func minimumWhiteTiles(floor string, numCarpets int, carpetLen int) int {
    
}
```

### Ruby

```ruby
# @param {String} floor
# @param {Integer} num_carpets
# @param {Integer} carpet_len
# @return {Integer}
def minimum_white_tiles(floor, num_carpets, carpet_len)
    
end
```

### Scala

```scala
object Solution {
    def minimumWhiteTiles(floor: String, numCarpets: Int, carpetLen: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_white_tiles(floor: String, num_carpets: i32, carpet_len: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-white-tiles floor numCarpets carpetLen)
  (-> string? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_white_tiles(Floor :: unicode:unicode_binary(), NumCarpets :: integer(), CarpetLen :: integer()) -> integer().
minimum_white_tiles(Floor, NumCarpets, CarpetLen) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_white_tiles(floor :: String.t, num_carpets :: integer, carpet_len :: integer) :: integer
  def minimum_white_tiles(floor, num_carpets, carpet_len) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumWhiteTiles(floor: String, numCarpets: Int64, carpetLen: Int64): Int64 {

    }
}
```

