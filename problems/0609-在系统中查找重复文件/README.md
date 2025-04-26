# 609. 在系统中查找重复文件

## 题目描述

<p>给你一个目录信息列表&nbsp;<code>paths</code> ，包括目录路径，以及该目录中的所有文件及其内容，请你按路径返回文件系统中的所有重复文件。答案可按 <strong>任意顺序</strong> 返回。</p>

<p>一组重复的文件至少包括 <strong>两个 </strong>具有完全相同内容的文件。</p>

<p><strong>输入 </strong>列表中的单个目录信息字符串的格式如下：</p>

<ul>
	<li><code>"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"</code></li>
</ul>

<p>这意味着，在目录&nbsp;<code>root/d1/d2/.../dm</code>&nbsp;下，有 <code>n</code> 个文件 ( <code>f1.txt</code>,&nbsp;<code>f2.txt</code>&nbsp;...&nbsp;<code>fn.txt</code> ) 的内容分别是 ( <code>f1_content</code>,&nbsp;<code>f2_content</code>&nbsp;...&nbsp;<code>fn_content</code> ) 。注意：<code>n &gt;= 1</code> 且 <code>m &gt;= 0</code> 。如果 <code>m = 0</code> ，则表示该目录是根目录。</p>

<p><strong>输出 </strong>是由 <strong>重复文件路径组</strong> 构成的列表。其中每个组由所有具有相同内容文件的文件路径组成。文件路径是具有下列格式的字符串：</p>

<ul>
	<li><code>"directory_path/file_name.txt"</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
<strong>输出：</strong>[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
<strong>输出：</strong>[["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= paths.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= paths[i].length &lt;= 3000</code></li>
	<li><code>1 &lt;= sum(paths[i].length) &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>paths[i]</code> 由英文字母、数字、字符 <code>'/'</code>、<code>'.'</code>、<code>'('</code>、<code>')'</code> 和 <code>' '</code> 组成</li>
	<li>你可以假设在同一目录中没有任何文件或目录共享相同的名称。</li>
	<li>你可以假设每个给定的目录信息代表一个唯一的目录。目录路径和文件信息用单个空格分隔。</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>假设您有一个真正的文件系统，您将如何搜索文件？广度搜索还是宽度搜索？</li>
	<li>如果文件内容非常大（GB级别），您将如何修改您的解决方案？</li>
	<li>如果每次只能读取 1 kb 的文件，您将如何修改解决方案？</li>
	<li>修改后的解决方案的时间复杂度是多少？其中最耗时的部分和消耗内存的部分是什么？如何优化？</li>
	<li>如何确保您发现的重复文件不是误报？</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串

## 示例

```
["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        
```

### Python3

```python3
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** findDuplicate(char** paths, int pathsSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<string>> FindDuplicate(string[] paths) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} paths
 * @return {string[][]}
 */
var findDuplicate = function(paths) {
    
};
```

### TypeScript

```typescript
function findDuplicate(paths: string[]): string[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $paths
     * @return String[][]
     */
    function findDuplicate($paths) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findDuplicate(_ paths: [String]) -> [[String]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findDuplicate(paths: Array<String>): List<List<String>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<String>> findDuplicate(List<String> paths) {
    
  }
}
```

### Go

```golang
func findDuplicate(paths []string) [][]string {
    
}
```

### Ruby

```ruby
# @param {String[]} paths
# @return {String[][]}
def find_duplicate(paths)
    
end
```

### Scala

```scala
object Solution {
    def findDuplicate(paths: Array[String]): List[List[String]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_duplicate(paths: Vec<String>) -> Vec<Vec<String>> {
        
    }
}
```

### Racket

```racket
(define/contract (find-duplicate paths)
  (-> (listof string?) (listof (listof string?)))
  )
```

### Erlang

```erlang
-spec find_duplicate(Paths :: [unicode:unicode_binary()]) -> [[unicode:unicode_binary()]].
find_duplicate(Paths) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_duplicate(paths :: [String.t]) :: [[String.t]]
  def find_duplicate(paths) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findDuplicate(paths: Array<String>): ArrayList<ArrayList<String>> {

    }
}
```

