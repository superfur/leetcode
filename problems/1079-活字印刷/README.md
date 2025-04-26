# 1079. 活字印刷

## 题目描述

<p>你有一套活字字模&nbsp;<code>tiles</code>，其中每个字模上都刻有一个字母&nbsp;<code>tiles[i]</code>。返回你可以印出的非空字母序列的数目。</p>

<p><strong>注意：</strong>本题中，每个活字字模只能使用一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>"AAB"
<strong>输出：</strong>8
<strong>解释：</strong>可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>"AAABBC"
<strong>输出：</strong>188
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>"V"
<strong>输出：</strong>1</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= tiles.length &lt;= 7</code></li>
	<li><code>tiles</code> 由大写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 回溯
- 计数

## 提示

1. Try to build the string with a backtracking DFS by considering what you can put in every position.

## 示例

```
"AAB"
"AAABBC"
"V"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numTilePossibilities(string tiles) {
        
    }
};
```

### Java

```java
class Solution {
    public int numTilePossibilities(String tiles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
```

### C

```c
int numTilePossibilities(char* tiles) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumTilePossibilities(string tiles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} tiles
 * @return {number}
 */
var numTilePossibilities = function(tiles) {
    
};
```

### TypeScript

```typescript
function numTilePossibilities(tiles: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $tiles
     * @return Integer
     */
    function numTilePossibilities($tiles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numTilePossibilities(_ tiles: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numTilePossibilities(tiles: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numTilePossibilities(String tiles) {
    
  }
}
```

### Go

```golang
func numTilePossibilities(tiles string) int {
    
}
```

### Ruby

```ruby
# @param {String} tiles
# @return {Integer}
def num_tile_possibilities(tiles)
    
end
```

### Scala

```scala
object Solution {
    def numTilePossibilities(tiles: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_tile_possibilities(tiles: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-tile-possibilities tiles)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_tile_possibilities(Tiles :: unicode:unicode_binary()) -> integer().
num_tile_possibilities(Tiles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_tile_possibilities(tiles :: String.t) :: integer
  def num_tile_possibilities(tiles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numTilePossibilities(tiles: String): Int64 {

    }
}
```

