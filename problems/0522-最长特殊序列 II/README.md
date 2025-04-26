# 522. 最长特殊序列 II

## 题目描述

<p>给定字符串列表&nbsp;<code>strs</code> ，返回其中 <strong>最长的特殊序列</strong>&nbsp;的长度。如果最长特殊序列不存在，返回 <code>-1</code> 。</p>

<p><strong>特殊序列</strong> 定义如下：该序列为某字符串 <strong>独有的子序列（即不能是其他字符串的子序列）</strong>。</p>

<p>&nbsp;<code>s</code>&nbsp;的&nbsp;<strong>子序列</strong>可以通过删去字符串&nbsp;<code>s</code>&nbsp;中的某些字符实现。</p>

<ul>
	<li>例如，<code>"abc"</code>&nbsp;是 <code>"aebdc"</code>&nbsp;的子序列，因为您可以删除<code>"a<u>e</u>b<u>d</u>c"</code>中的下划线字符来得到 <code>"abc"</code>&nbsp;。<code>"aebdc"</code>的子序列还包括<code>"aebdc"</code>、 <code>"aeb"</code>&nbsp;和 <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size: 12.6px; background-color: rgb(249, 242, 244);">""</span></font>&nbsp;(空字符串)。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> strs = ["aba","cdc","eae"]
<strong>输出:</strong> 3
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> strs = ["aaa","aaa","aa"]
<strong>输出:</strong> -1
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>2 &lt;= strs.length &lt;= 50</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 10</code></li>
	<li><code>strs[i]</code>&nbsp;只包含小写英文字母</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 双指针
- 字符串
- 排序

## 示例

```
["aba","cdc","eae"]
["aaa","aaa","aa"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        
    }
};
```

### Java

```java
class Solution {
    public int findLUSlength(String[] strs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
```

### C

```c
int findLUSlength(char** strs, int strsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindLUSlength(string[] strs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} strs
 * @return {number}
 */
var findLUSlength = function(strs) {
    
};
```

### TypeScript

```typescript
function findLUSlength(strs: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $strs
     * @return Integer
     */
    function findLUSlength($strs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLUSlength(_ strs: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLUSlength(strs: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findLUSlength(List<String> strs) {
    
  }
}
```

### Go

```golang
func findLUSlength(strs []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} strs
# @return {Integer}
def find_lu_slength(strs)
    
end
```

### Scala

```scala
object Solution {
    def findLUSlength(strs: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_lu_slength(strs: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-lu-slength strs)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_lu_slength(Strs :: [unicode:unicode_binary()]) -> integer().
find_lu_slength(Strs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_lu_slength(strs :: [String.t]) :: integer
  def find_lu_slength(strs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLUSlength(strs: Array<String>): Int64 {

    }
}
```

