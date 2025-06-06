# 960. 删列造序 III

## 题目描述

<p>给定由<meta charset="UTF-8" />&nbsp;<code>n</code>&nbsp;个小写字母字符串组成的数组<meta charset="UTF-8" />&nbsp;<code>strs</code>&nbsp;，其中每个字符串长度相等。</p>

<p>选取一个删除索引序列，对于<meta charset="UTF-8" />&nbsp;<code>strs</code>&nbsp;中的每个字符串，删除对应每个索引处的字符。</p>

<p>比如，有<meta charset="UTF-8" />&nbsp;<code>strs = ["abcdef","uvwxyz"]</code>&nbsp;，删除索引序列<meta charset="UTF-8" />&nbsp;<code>{0, 2, 3}</code>&nbsp;，删除后为<meta charset="UTF-8" />&nbsp;<code>["bef", "vyz"]</code>&nbsp;。</p>

<p>假设，我们选择了一组删除索引<meta charset="UTF-8" />&nbsp;<code>answer</code>&nbsp;，那么在执行删除操作之后，最终得到的数组的行中的 <strong>每个元素</strong> 都是按<strong>字典序</strong>排列的（即&nbsp;<code>(strs[0][0] &lt;= strs[0][1] &lt;= ... &lt;= strs[0][strs[0].length - 1])</code>&nbsp;和&nbsp;<code>(strs[1][0] &lt;= strs[1][1] &lt;= ... &lt;= strs[1][strs[1].length - 1])</code> ，依此类推）。</p>

<p>请返回<meta charset="UTF-8" /><em>&nbsp;<code>answer.length</code>&nbsp;的最小可能值</em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>strs = ["babca","bbazb"]
<strong>输出：</strong>3
<strong>解释：
</strong>删除 0、1 和 4 这三列后，最终得到的数组是 strs = ["bc", "az"]。
这两行是分别按字典序排列的（即，strs[0][0] &lt;= strs[0][1] 且 strs[1][0] &lt;= strs[1][1]）。
注意，strs[0] &gt; strs[1] —— 数组 strs 不一定是按字典序排列的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>strs = ["edcba"]
<strong>输出：</strong>4
<strong>解释：</strong>如果删除的列少于 4 列，则剩下的行都不会按字典序排列。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>strs = ["ghi","def","abc"]
<strong>输出：</strong>0
<strong>解释：</strong>所有行都已按字典序排列。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>
<meta charset="UTF-8" />

<ul>
	<li><code>n == strs.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code>&nbsp;由小写英文字母组成</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 字符串
- 动态规划

## 示例

```
["babca","bbazb"]
["edcba"]
["ghi","def","abc"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        
    }
};
```

### Java

```java
class Solution {
    public int minDeletionSize(String[] strs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
```

### C

```c
int minDeletionSize(char** strs, int strsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinDeletionSize(string[] strs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} strs
 * @return {number}
 */
var minDeletionSize = function(strs) {
    
};
```

### TypeScript

```typescript
function minDeletionSize(strs: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $strs
     * @return Integer
     */
    function minDeletionSize($strs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minDeletionSize(strs: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minDeletionSize(List<String> strs) {
    
  }
}
```

### Go

```golang
func minDeletionSize(strs []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} strs
# @return {Integer}
def min_deletion_size(strs)
    
end
```

### Scala

```scala
object Solution {
    def minDeletionSize(strs: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-deletion-size strs)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_deletion_size(Strs :: [unicode:unicode_binary()]) -> integer().
min_deletion_size(Strs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_deletion_size(strs :: [String.t]) :: integer
  def min_deletion_size(strs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minDeletionSize(strs: Array<String>): Int64 {

    }
}
```

