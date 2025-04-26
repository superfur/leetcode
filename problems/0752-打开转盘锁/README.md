# 752. 打开转盘锁

## 题目描述

<p>你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： <code>'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'</code> 。每个拨轮可以自由旋转：例如把 <code>'9'</code> 变为&nbsp;<code>'0'</code>，<code>'0'</code> 变为 <code>'9'</code> 。每次旋转都只能旋转一个拨轮的一位数字。</p>

<p>锁的初始数字为 <code>'0000'</code> ，一个代表四个拨轮的数字的字符串。</p>

<p>列表 <code>deadends</code> 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。</p>

<p>字符串 <code>target</code> 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：</strong>deadends = ["0201","0101","0102","1212","2002"], target = "0202"
<strong>输出：</strong>6
<strong>解释：</strong>
可能的移动序列为 "0000" -&gt; "1000" -&gt; "1100" -&gt; "1200" -&gt; "1201" -&gt; "1202" -&gt; "0202"。
注意 "0000" -&gt; "0001" -&gt; "0002" -&gt; "0102" -&gt; "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> deadends = ["8888"], target = "0009"
<strong>输出：</strong>1
<strong>解释：</strong>把最后一位反向旋转一次即可 "0000" -&gt; "0009"。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
<strong>输出：</strong>-1
<strong>解释：</strong>无法旋转到目标数字且不被锁定。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;deadends.length &lt;= 500</code></li>
	<li><code><font face="monospace">deadends[i].length == 4</font></code></li>
	<li><code><font face="monospace">target.length == 4</font></code></li>
	<li><code>target</code> <strong>不在</strong> <code>deadends</code> 之中</li>
	<li><code>target</code> 和 <code>deadends[i]</code> 仅由若干位数字组成</li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 数组
- 哈希表
- 字符串

## 提示

1. We can think of this problem as a shortest path problem on a graph: there are `10000` nodes (strings `'0000'` to `'9999'`), and there is an edge between two nodes if they differ in one digit, that digit differs by 1 (wrapping around, so `'0'` and `'9'` differ by 1), and if *both* nodes are not in `deadends`.

## 示例

```
["0201","0101","0102","1212","2002"]
"0202"
["8888"]
"0009"
["8887","8889","8878","8898","8788","8988","7888","9888"]
"8888"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        
    }
};
```

### Java

```java
class Solution {
    public int openLock(String[] deadends, String target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
```

### C

```c
int openLock(char** deadends, int deadendsSize, char* target) {
    
}
```

### C#

```csharp
public class Solution {
    public int OpenLock(string[] deadends, string target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} deadends
 * @param {string} target
 * @return {number}
 */
var openLock = function(deadends, target) {
    
};
```

### TypeScript

```typescript
function openLock(deadends: string[], target: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $deadends
     * @param String $target
     * @return Integer
     */
    function openLock($deadends, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func openLock(_ deadends: [String], _ target: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun openLock(deadends: Array<String>, target: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int openLock(List<String> deadends, String target) {
    
  }
}
```

### Go

```golang
func openLock(deadends []string, target string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} deadends
# @param {String} target
# @return {Integer}
def open_lock(deadends, target)
    
end
```

### Scala

```scala
object Solution {
    def openLock(deadends: Array[String], target: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn open_lock(deadends: Vec<String>, target: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (open-lock deadends target)
  (-> (listof string?) string? exact-integer?)
  )
```

### Erlang

```erlang
-spec open_lock(Deadends :: [unicode:unicode_binary()], Target :: unicode:unicode_binary()) -> integer().
open_lock(Deadends, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec open_lock(deadends :: [String.t], target :: String.t) :: integer
  def open_lock(deadends, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func openLock(deadends: Array<String>, target: String): Int64 {

    }
}
```

