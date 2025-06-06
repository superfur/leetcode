# 71. 简化路径

## 题目描述

<p>给你一个字符串 <code>path</code> ，表示指向某一文件或目录的&nbsp;Unix 风格 <strong>绝对路径 </strong>（以 <code>'/'</code> 开头），请你将其转化为 <strong>更加简洁的规范路径</strong>。</p>

<p class="MachineTrans-lang-zh-CN">在 Unix 风格的文件系统中规则如下：</p>

<ul>
	<li class="MachineTrans-lang-zh-CN">一个点&nbsp;<code>'.'</code>&nbsp;表示当前目录本身。</li>
	<li class="MachineTrans-lang-zh-CN">此外，两个点 <code>'..'</code>&nbsp;表示将目录切换到上一级（指向父目录）。</li>
	<li class="MachineTrans-lang-zh-CN">任意多个连续的斜杠（即，<code>'//'</code>&nbsp;或 <code>'///'</code>）都被视为单个斜杠 <code>'/'</code>。</li>
	<li class="MachineTrans-lang-zh-CN">任何其他格式的点（例如，<code>'...'</code>&nbsp;或 <code>'....'</code>）均被视为有效的文件/目录名称。</li>
</ul>

<p>返回的 <strong>简化路径</strong> 必须遵循下述格式：</p>

<ul>
	<li>始终以斜杠 <code>'/'</code> 开头。</li>
	<li>两个目录名之间必须只有一个斜杠 <code>'/'</code> 。</li>
	<li>最后一个目录名（如果存在）<strong>不能 </strong>以 <code>'/'</code> 结尾。</li>
	<li>此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 <code>'.'</code> 或 <code>'..'</code>）。</li>
</ul>

<p>返回简化后得到的 <strong>规范路径</strong> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">path = "/home/"</span></p>

<p><span class="example-io"><b>输出：</b>"/home"</span></p>

<p><strong>解释：</strong></p>

<p>应删除尾随斜杠。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>path = "/home//foo/"</span></p>

<p><span class="example-io"><b>输出：</b>"/home/foo"</span></p>

<p><strong>解释：</strong></p>

<p>多个连续的斜杠被单个斜杠替换。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">path = "/home/user/Documents/../Pictures"</span></p>

<p><span class="example-io"><b>输出：</b>"/home/user/Pictures"</span></p>

<p><strong>解释：</strong></p>

<p>两个点&nbsp;<code>".."</code>&nbsp;表示上一级目录（父目录）。</p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>path = "/../"</span></p>

<p><span class="example-io"><b>输出：</b>"/"</span></p>

<p><strong>解释：</strong></p>

<p>不可能从根目录上升一级目录。</p>
</div>

<p><strong class="example">示例 5：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>path = "/.../a/../b/c/../d/./"</span></p>

<p><span class="example-io"><b>输出：</b>"/.../b/d"</span></p>

<p><strong>解释：</strong></p>

<p><code>"..."</code>&nbsp;在这个问题中是一个合法的目录名。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= path.length &lt;= 3000</code></li>
	<li><code>path</code> 由英文字母，数字，<code>'.'</code>，<code>'/'</code> 或 <code>'_'</code> 组成。</li>
	<li><code>path</code> 是一个有效的 Unix 风格绝对路径。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 字符串

## 示例

```
"/home/"
"/home//foo/"
"/home/user/Documents/../Pictures"
"/../"
"/.../a/../b/c/../d/./"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string simplifyPath(string path) {
        
    }
};
```

### Java

```java
class Solution {
    public String simplifyPath(String path) {
        
    }
}
```

### Python

```python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def simplifyPath(self, path: str) -> str:
        
```

### C

```c
char* simplifyPath(char* path) {
    
}
```

### C#

```csharp
public class Solution {
    public string SimplifyPath(string path) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function(path) {
    
};
```

### TypeScript

```typescript
function simplifyPath(path: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $path
     * @return String
     */
    function simplifyPath($path) {
        
    }
}
```

### Swift

```swift
class Solution {
    func simplifyPath(_ path: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun simplifyPath(path: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String simplifyPath(String path) {
    
  }
}
```

### Go

```golang
func simplifyPath(path string) string {
    
}
```

### Ruby

```ruby
# @param {String} path
# @return {String}
def simplify_path(path)
    
end
```

### Scala

```scala
object Solution {
    def simplifyPath(path: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn simplify_path(path: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (simplify-path path)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec simplify_path(Path :: unicode:unicode_binary()) -> unicode:unicode_binary().
simplify_path(Path) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec simplify_path(path :: String.t) :: String.t
  def simplify_path(path) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func simplifyPath(path: String): String {

    }
}
```

