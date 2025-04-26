# 1233. 删除子文件夹

## 题目描述

<p>你是一位系统管理员，手里有一份文件夹列表 <code>folder</code>，你的任务是要删除该列表中的所有 <strong>子文件夹</strong>，并以 <strong>任意顺序</strong> 返回剩下的文件夹。</p>

<p>如果文件夹&nbsp;<code>folder[i]</code>&nbsp;位于另一个文件夹&nbsp;<code>folder[j]</code>&nbsp;下，那么&nbsp;<code>folder[i]</code>&nbsp;就是&nbsp;<code>folder[j]</code>&nbsp;的 <strong>子文件夹</strong> 。<code>folder[j]</code>&nbsp;的子文件夹必须以&nbsp;<code>folder[j]</code> 开头，后跟一个 <code>"/"</code>。例如，<code>"/a/b"</code> 是&nbsp;<code>"/a"</code>&nbsp;的一个子文件夹，但&nbsp;<code>"/b"</code> 不是&nbsp;<code>"/a/b/c"</code> 的一个子文件夹。</p>

<p>文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：<font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'/'</span></span></font></font>&nbsp;后跟一个或者多个小写英文字母。</p>

<ul>
	<li>例如，<code>"/leetcode"</code>&nbsp;和&nbsp;<code>"/leetcode/problems"</code>&nbsp;都是有效的路径，而空字符串和&nbsp;<code>"/"</code>&nbsp;不是。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
<strong>输出：</strong>["/a","/c/d","/c/f"]
<strong>解释：</strong>"/a/b" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>folder = ["/a","/a/b/c","/a/b/d"]
<strong>输出：</strong>["/a"]
<strong>解释：</strong>文件夹 "/a/b/c" 和 "/a/b/d" 都会被删除，因为它们都是 "/a" 的子文件夹。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入:</strong> folder = ["/a/b/c","/a/b/ca","/a/b/d"]
<strong>输出:</strong> ["/a/b/c","/a/b/ca","/a/b/d"]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= folder.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>2 &lt;= folder[i].length &lt;= 100</code></li>
	<li><code>folder[i]</code>&nbsp;只包含小写字母和 <code>'/'</code></li>
	<li><code>folder[i]</code>&nbsp;总是以字符 <code>'/'</code>&nbsp;起始</li>
	<li><code>folder</code>&nbsp;每个元素都是 <strong>唯一</strong> 的</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 字典树
- 数组
- 字符串

## 提示

1. Sort the folders lexicographically.
2. Insert the current element in an array and then loop until we get rid of all of their subfolders, repeat this until no element is left.

## 示例

```
["/a","/a/b","/c/d","/c/d/e","/c/f"]
["/a","/a/b/c","/a/b/d"]
["/a/b/c","/a/b/ca","/a/b/d"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> removeSubfolders(String[] folder) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** removeSubfolders(char** folder, int folderSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> RemoveSubfolders(string[] folder) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} folder
 * @return {string[]}
 */
var removeSubfolders = function(folder) {
    
};
```

### TypeScript

```typescript
function removeSubfolders(folder: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $folder
     * @return String[]
     */
    function removeSubfolders($folder) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeSubfolders(_ folder: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeSubfolders(folder: Array<String>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> removeSubfolders(List<String> folder) {
    
  }
}
```

### Go

```golang
func removeSubfolders(folder []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} folder
# @return {String[]}
def remove_subfolders(folder)
    
end
```

### Scala

```scala
object Solution {
    def removeSubfolders(folder: Array[String]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_subfolders(folder: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (remove-subfolders folder)
  (-> (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec remove_subfolders(Folder :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
remove_subfolders(Folder) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_subfolders(folder :: [String.t]) :: [String.t]
  def remove_subfolders(folder) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeSubfolders(folder: Array<String>): ArrayList<String> {

    }
}
```

