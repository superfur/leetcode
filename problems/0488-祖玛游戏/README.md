# 488. 祖玛游戏

## 题目描述

<p>你正在参与祖玛游戏的一个变种。</p>

<p>在这个祖玛游戏变体中，桌面上有 <strong>一排</strong> 彩球，每个球的颜色可能是：红色 <code>'R'</code>、黄色 <code>'Y'</code>、蓝色 <code>'B'</code>、绿色 <code>'G'</code> 或白色 <code>'W'</code> 。你的手中也有一些彩球。</p>

<p>你的目标是 <strong>清空</strong> 桌面上所有的球。每一回合：</p>

<ul>
	<li>从你手上的彩球中选出 <strong>任意一颗</strong> ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。</li>
	<li>接着，如果有出现 <strong>三个或者三个以上</strong> 且 <strong>颜色相同</strong> 的球相连的话，就把它们移除掉。
	<ul>
		<li>如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。</li>
	</ul>
	</li>
	<li>如果桌面上所有球都被移除，则认为你赢得本场游戏。</li>
	<li>重复这个过程，直到你赢了游戏或者手中没有更多的球。</li>
</ul>

<p>给你一个字符串 <code>board</code> ，表示桌面上最开始的那排球。另给你一个字符串 <code>hand</code> ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，计算并返回所需的 <strong>最少</strong> 球数。如果不能移除桌上所有的球，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>board = "WRRBBW", hand = "RB"
<strong>输出：</strong>-1
<strong>解释：</strong>无法移除桌面上的所有球。可以得到的最好局面是：
- 插入一个 'R' ，使桌面变为 WRR<em><strong>R</strong></em>BBW 。W<em><strong>RRR</strong></em>BBW -&gt; WBBW
- 插入一个 'B' ，使桌面变为 WBB<em><strong>B</strong></em>W 。W<em><strong>BBB</strong></em>W -&gt; WW
桌面上还剩着球，没有其他球可以插入。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>board = "WWRRBBWW", hand = "WRBRW"
<strong>输出：</strong>2
<strong>解释：</strong>要想清空桌面上的球，可以按下述步骤：
- 插入一个 'R' ，使桌面变为 WWRR<strong><em>R</em></strong>BBWW 。WW<em><strong>RRR</strong></em>BBWW -&gt; WWBBWW
- 插入一个 'B' ，使桌面变为 WWBB<em><strong>B</strong></em>WW 。WW<em><strong>BBB</strong></em>WW -&gt; <em><strong>WWWW</strong></em> -&gt; empty
只需从手中出 2 个球就可以清空桌面。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>board = "G", hand = "GGGGG"
<strong>输出：</strong>2
<strong>解释：</strong>要想清空桌面上的球，可以按下述步骤：
- 插入一个 'G' ，使桌面变为 G<em><strong>G</strong></em> 。
- 插入一个 'G' ，使桌面变为 GG<em><strong>G</strong></em> 。<em><strong>GGG</strong></em> -&gt; empty
只需从手中出 2 个球就可以清空桌面。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>board = "RBYYBBRRB", hand = "YRBGB"
<strong>输出：</strong>3
<strong>解释：</strong>要想清空桌面上的球，可以按下述步骤：
- 插入一个 'Y' ，使桌面变为 RBYY<em><strong>Y</strong></em>BBRRB 。RB<em><strong>YYY</strong></em>BBRRB -&gt; R<em><strong>BBB</strong></em>RRB -&gt; <em><strong>RRR</strong></em>B -&gt; B
- 插入一个 'B' ，使桌面变为 B<em><strong>B</strong></em> 。
- 插入一个 'B' ，使桌面变为 BB<em><strong>B</strong></em> 。<em><strong>BBB</strong></em> -&gt; empty
只需从手中出 3 个球就可以清空桌面。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= board.length &lt;= 16</code></li>
	<li><code>1 &lt;= hand.length &lt;= 5</code></li>
	<li><code>board</code> 和 <code>hand</code> 由字符 <code>'R'</code>、<code>'Y'</code>、<code>'B'</code>、<code>'G'</code> 和 <code>'W'</code> 组成</li>
	<li>桌面上一开始的球中，不会有三个及三个以上颜色相同且连着的球</li>
</ul>


## 难度

Hard

## 标签

- 栈
- 广度优先搜索
- 记忆化搜索
- 字符串
- 动态规划

## 示例

```
"WRRBBW"
"RB"
"WWRRBBWW"
"WRBRW"
"G"
"GGGGG"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMinStep(string board, string hand) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMinStep(String board, String hand) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
```

### C

```c
int findMinStep(char* board, char* hand) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMinStep(string board, string hand) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} board
 * @param {string} hand
 * @return {number}
 */
var findMinStep = function(board, hand) {
    
};
```

### TypeScript

```typescript
function findMinStep(board: string, hand: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $board
     * @param String $hand
     * @return Integer
     */
    function findMinStep($board, $hand) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMinStep(_ board: String, _ hand: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMinStep(board: String, hand: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMinStep(String board, String hand) {
    
  }
}
```

### Go

```golang
func findMinStep(board string, hand string) int {
    
}
```

### Ruby

```ruby
# @param {String} board
# @param {String} hand
# @return {Integer}
def find_min_step(board, hand)
    
end
```

### Scala

```scala
object Solution {
    def findMinStep(board: String, hand: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_min_step(board: String, hand: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-min-step board hand)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_min_step(Board :: unicode:unicode_binary(), Hand :: unicode:unicode_binary()) -> integer().
find_min_step(Board, Hand) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_min_step(board :: String.t, hand :: String.t) :: integer
  def find_min_step(board, hand) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMinStep(board: String, hand: String): Int64 {

    }
}
```

