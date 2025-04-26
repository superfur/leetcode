# 944. 删列造序

## 题目描述

<p>给你由 <code>n</code> 个小写字母字符串组成的数组 <code>strs</code>，其中每个字符串长度相等。</p>

<p>这些字符串可以每个一行，排成一个网格。例如，<code>strs = ["abc", "bce", "cae"]</code> 可以排列为：</p>

<pre>
abc
bce
cae</pre>

<p>你需要找出并删除 <strong>不是按字典序非严格递增排列的</strong> 列。在上面的例子（下标从 0 开始）中，列 0（<code>'a'</code>, <code>'b'</code>, <code>'c'</code>）和列 2（<code>'c'</code>, <code>'e'</code>, <code>'e'</code>）都是按字典序非严格递增排列的，而列 1（<code>'b'</code>, <code>'c'</code>, <code>'a'</code>）不是，所以要删除列 1 。</p>

<p>返回你需要删除的列数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>strs = ["cba","daf","ghi"]
<strong>输出：</strong>1
<strong>解释：</strong>网格示意如下：
  cba
  daf
  ghi
列 0 和列 2 按升序排列，但列 1 不是，所以只需要删除列 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>strs = ["a","b"]
<strong>输出：</strong>0
<strong>解释：</strong>网格示意如下：
  a
  b
只有列 0 这一列，且已经按升序排列，所以不用删除任何列。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>strs = ["zyx","wvu","tsr"]
<strong>输出：</strong>3
<strong>解释：</strong>网格示意如下：
  zyx
  wvu
  tsr
所有 3 列都是非升序排列的，所以都要删除。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == strs.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 1000</code></li>
	<li><code>strs[i]</code> 由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 示例

```
["cba","daf","ghi"]
["a","b"]
["zyx","wvu","tsr"]
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

