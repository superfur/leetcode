# 920. 播放列表的数量

## 题目描述

<p>你的音乐播放器里有 <code>n</code> 首不同的歌，在旅途中，你计划听 <code>goal</code> 首歌（不一定不同，即，允许歌曲重复）。你将会按如下规则创建播放列表：</p>

<ul>
	<li>每首歌 <strong>至少播放一次</strong> 。</li>
	<li>一首歌只有在其他 <code>k</code> 首歌播放完之后才能再次播放。</li>
</ul>

<p>给你 <code>n</code>、<code>goal</code> 和 <code>k</code> ，返回可以满足要求的播放列表的数量。由于答案可能非常大，请返回对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 的结果。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, goal = 3, k = 1
<strong>输出：</strong>6
<strong>解释：</strong>有 6 种可能的播放列表。[1, 2, 3]，[1, 3, 2]，[2, 1, 3]，[2, 3, 1]，[3, 1, 2]，[3, 2, 1] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2, goal = 3, k = 0
<strong>输出：</strong>6
<strong>解释：</strong>有 6 种可能的播放列表。[1, 1, 2]，[1, 2, 1]，[2, 1, 1]，[2, 2, 1]，[2, 1, 2]，[1, 2, 2] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 2, goal = 3, k = 1
<strong>输出：</strong>2
<strong>解释：</strong>有 2 种可能的播放列表。[1, 2, 1]，[2, 1, 2] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= k &lt; n &lt;= goal &lt;= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 动态规划
- 组合数学

## 示例

```
3
3
1
2
3
0
2
3
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numMusicPlaylists(int n, int goal, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numMusicPlaylists(int n, int goal, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        
```

### C

```c
int numMusicPlaylists(int n, int goal, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumMusicPlaylists(int n, int goal, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} goal
 * @param {number} k
 * @return {number}
 */
var numMusicPlaylists = function(n, goal, k) {
    
};
```

### TypeScript

```typescript
function numMusicPlaylists(n: number, goal: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $goal
     * @param Integer $k
     * @return Integer
     */
    function numMusicPlaylists($n, $goal, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numMusicPlaylists(_ n: Int, _ goal: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numMusicPlaylists(n: Int, goal: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numMusicPlaylists(int n, int goal, int k) {
    
  }
}
```

### Go

```golang
func numMusicPlaylists(n int, goal int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} goal
# @param {Integer} k
# @return {Integer}
def num_music_playlists(n, goal, k)
    
end
```

### Scala

```scala
object Solution {
    def numMusicPlaylists(n: Int, goal: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_music_playlists(n: i32, goal: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-music-playlists n goal k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_music_playlists(N :: integer(), Goal :: integer(), K :: integer()) -> integer().
num_music_playlists(N, Goal, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_music_playlists(n :: integer, goal :: integer, k :: integer) :: integer
  def num_music_playlists(n, goal, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numMusicPlaylists(n: Int64, goal: Int64, k: Int64): Int64 {

    }
}
```

