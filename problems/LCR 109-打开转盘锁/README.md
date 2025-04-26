# LCR 109. 打开转盘锁

## 题目描述

<p>一个密码锁由 4&nbsp;个环形拨轮组成，每个拨轮都有 10 个数字： <code>&#39;0&#39;, &#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;, &#39;5&#39;, &#39;6&#39;, &#39;7&#39;, &#39;8&#39;, &#39;9&#39;</code> 。每个拨轮可以自由旋转：例如把 <code>&#39;9&#39;</code> 变为&nbsp;<code>&#39;0&#39;</code>，<code>&#39;0&#39;</code> 变为 <code>&#39;9&#39;</code> 。每次旋转都只能旋转一个拨轮的一位数字。</p>

<p>锁的初始数字为 <code>&#39;0000&#39;</code> ，一个代表四个拨轮的数字的字符串。</p>

<p>列表 <code>deadends</code> 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。</p>

<p>字符串 <code>target</code> 代表可以解锁的数字，请给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>deadends = [&quot;0201&quot;,&quot;0101&quot;,&quot;0102&quot;,&quot;1212&quot;,&quot;2002&quot;], target = &quot;0202&quot;
<strong>输出：</strong>6
<strong>解释：</strong>
可能的移动序列为 &quot;0000&quot; -&gt; &quot;1000&quot; -&gt; &quot;1100&quot; -&gt; &quot;1200&quot; -&gt; &quot;1201&quot; -&gt; &quot;1202&quot; -&gt; &quot;0202&quot;。
注意 &quot;0000&quot; -&gt; &quot;0001&quot; -&gt; &quot;0002&quot; -&gt; &quot;0102&quot; -&gt; &quot;0202&quot; 这样的序列是不能解锁的，因为当拨动到 &quot;0102&quot; 时这个锁就会被锁定。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> deadends = [&quot;8888&quot;], target = &quot;0009&quot;
<strong>输出：</strong>1
<strong>解释：</strong>
把最后一位反向旋转一次即可 &quot;0000&quot; -&gt; &quot;0009&quot;。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入:</strong> deadends = [&quot;8887&quot;,&quot;8889&quot;,&quot;8878&quot;,&quot;8898&quot;,&quot;8788&quot;,&quot;8988&quot;,&quot;7888&quot;,&quot;9888&quot;], target = &quot;8888&quot;
<strong>输出：</strong>-1
<strong>解释：
</strong>无法旋转到目标数字且不被锁定。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入:</strong> deadends = [&quot;0000&quot;], target = &quot;8888&quot;
<strong>输出：</strong>-1
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

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 752&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/open-the-lock/">https://leetcode-cn.com/problems/open-the-lock/</a></p>


## 难度

Medium

## 标签

- 广度优先搜索
- 数组
- 哈希表
- 字符串

## 示例

```
["0201","0101","0102","1212","2002"]
"0202"
["8888"]
"0009"
["8887","8889","8878","8898","8788","8988","7888","9888"]
"8888"
["0000"]
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


int openLock(char ** deadends, int deadendsSize, char * target){

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

