# LCR 117. 相似字符串组

## 题目描述

<p>如果交换字符串&nbsp;<code>X</code> 中的两个不同位置的字母，使得它和字符串&nbsp;<code>Y</code> 相等，那么称 <code>X</code> 和 <code>Y</code> 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。</p>

<p>例如，<code>&quot;tars&quot;</code> 和 <code>&quot;rats&quot;</code> 是相似的 (交换 <code>0</code> 与 <code>2</code> 的位置)；&nbsp;<code>&quot;rats&quot;</code> 和 <code>&quot;arts&quot;</code> 也是相似的，但是 <code>&quot;star&quot;</code> 不与 <code>&quot;tars&quot;</code>，<code>&quot;rats&quot;</code>，或 <code>&quot;arts&quot;</code> 相似。</p>

<p>总之，它们通过相似性形成了两个关联组：<code>{&quot;tars&quot;, &quot;rats&quot;, &quot;arts&quot;}</code> 和 <code>{&quot;star&quot;}</code>。注意，<code>&quot;tars&quot;</code> 和 <code>&quot;arts&quot;</code> 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。</p>

<p>给定一个字符串列表 <code>strs</code>。列表中的每个字符串都是 <code>strs</code> 中其它所有字符串的一个&nbsp;<strong>字母异位词&nbsp;</strong>。请问 <code>strs</code> 中有多少个相似字符串组？</p>

<p><strong>字母异位词（anagram）</strong>，一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>strs = [&quot;tars&quot;,&quot;rats&quot;,&quot;arts&quot;,&quot;star&quot;]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>strs = [&quot;omv&quot;,&quot;ovm&quot;]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 300</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 300</code></li>
	<li><code>strs[i]</code> 只包含小写字母。</li>
	<li><code>strs</code> 中的所有单词都具有相同的长度，且是彼此的字母异位词。</li>
</ul>

<p>&nbsp; &nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 839&nbsp;题相同：<a href="https://leetcode-cn.com/problems/similar-string-groups/">https://leetcode-cn.com/problems/similar-string-groups/</a></p>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 数组
- 哈希表
- 字符串

## 示例

```
["tars","rats","arts","star"]
["omv","ovm"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numSimilarGroups(vector<string>& strs) {

    }
};
```

### Java

```java
class Solution {
    public int numSimilarGroups(String[] strs) {

    }
}
```

### Python

```python
class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
```

### C

```c


int numSimilarGroups(char ** strs, int strsSize){

}
```

### C#

```csharp
public class Solution {
    public int NumSimilarGroups(string[] strs) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} strs
 * @return {number}
 */
var numSimilarGroups = function(strs) {

};
```

### TypeScript

```typescript
function numSimilarGroups(strs: string[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $strs
     * @return Integer
     */
    function numSimilarGroups($strs) {

    }
}
```

### Swift

```swift
class Solution {
    func numSimilarGroups(_ strs: [String]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numSimilarGroups(strs: Array<String>): Int {

    }
}
```

### Go

```golang
func numSimilarGroups(strs []string) int {

}
```

### Ruby

```ruby
# @param {String[]} strs
# @return {Integer}
def num_similar_groups(strs)

end
```

### Scala

```scala
object Solution {
    def numSimilarGroups(strs: Array[String]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_similar_groups(strs: Vec<String>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (num-similar-groups strs)
  (-> (listof string?) exact-integer?)

  )
```

### Erlang

```erlang
-spec num_similar_groups(Strs :: [unicode:unicode_binary()]) -> integer().
num_similar_groups(Strs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_similar_groups(strs :: [String.t]) :: integer
  def num_similar_groups(strs) do

  end
end
```

