# 1487. 保证文件名唯一

## 题目描述

<p>给你一个长度为 <code>n</code> 的字符串数组 <code>names</code> 。你将会在文件系统中创建 <code>n</code> 个文件夹：在第 <code>i</code> 分钟，新建名为 <code>names[i]</code> 的文件夹。</p>

<p>由于两个文件 <strong>不能</strong> 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 <code>(k)</code> 的形式为新文件夹的文件名添加后缀，其中 <code>k</code> 是能保证文件名唯一的 <strong>最小正整数</strong> 。</p>

<p>返回长度为<em> <code>n</code></em> 的字符串数组，其中 <code>ans[i]</code> 是创建第 <code>i</code> 个文件夹时系统分配给该文件夹的实际名称。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>names = [&quot;pes&quot;,&quot;fifa&quot;,&quot;gta&quot;,&quot;pes(2019)&quot;]
<strong>输出：</strong>[&quot;pes&quot;,&quot;fifa&quot;,&quot;gta&quot;,&quot;pes(2019)&quot;]
<strong>解释：</strong>文件系统将会这样创建文件名：
&quot;pes&quot; --&gt; 之前未分配，仍为 &quot;pes&quot;
&quot;fifa&quot; --&gt; 之前未分配，仍为 &quot;fifa&quot;
&quot;gta&quot; --&gt; 之前未分配，仍为 &quot;gta&quot;
&quot;pes(2019)&quot; --&gt; 之前未分配，仍为 &quot;pes(2019)&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>names = [&quot;gta&quot;,&quot;gta(1)&quot;,&quot;gta&quot;,&quot;avalon&quot;]
<strong>输出：</strong>[&quot;gta&quot;,&quot;gta(1)&quot;,&quot;gta(2)&quot;,&quot;avalon&quot;]
<strong>解释：</strong>文件系统将会这样创建文件名：
&quot;gta&quot; --&gt; 之前未分配，仍为 &quot;gta&quot;
&quot;gta(1)&quot; --&gt; 之前未分配，仍为 &quot;gta(1)&quot;
&quot;gta&quot; --&gt; 文件名被占用，系统为该名称添加后缀 (k)，由于 &quot;gta(1)&quot; 也被占用，所以 k = 2 。实际创建的文件名为 &quot;gta(2)&quot; 。
&quot;avalon&quot; --&gt; 之前未分配，仍为 &quot;avalon&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>names = [&quot;onepiece&quot;,&quot;onepiece(1)&quot;,&quot;onepiece(2)&quot;,&quot;onepiece(3)&quot;,&quot;onepiece&quot;]
<strong>输出：</strong>[&quot;onepiece&quot;,&quot;onepiece(1)&quot;,&quot;onepiece(2)&quot;,&quot;onepiece(3)&quot;,&quot;onepiece(4)&quot;]
<strong>解释：</strong>当创建最后一个文件夹时，最小的正有效 k 为 4 ，文件名变为 &quot;onepiece(4)&quot;。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>names = [&quot;wano&quot;,&quot;wano&quot;,&quot;wano&quot;,&quot;wano&quot;]
<strong>输出：</strong>[&quot;wano&quot;,&quot;wano(1)&quot;,&quot;wano(2)&quot;,&quot;wano(3)&quot;]
<strong>解释：</strong>每次创建文件夹 &quot;wano&quot; 时，只需增加后缀中 k 的值即可。</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>names = [&quot;kaido&quot;,&quot;kaido(1)&quot;,&quot;kaido&quot;,&quot;kaido(1)&quot;]
<strong>输出：</strong>[&quot;kaido&quot;,&quot;kaido(1)&quot;,&quot;kaido(2)&quot;,&quot;kaido(1)(1)&quot;]
<strong>解释：</strong>注意，如果含后缀文件名被占用，那么系统也会按规则在名称后添加新的后缀 (k) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= names.length &lt;= 5 * 10^4</code></li>
	<li><code>1 &lt;= names[i].length &lt;= 20</code></li>
	<li><code>names[i]</code> 由小写英文字母、数字和/或圆括号组成。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串

## 提示

1. Keep a map of each name and the smallest valid integer that can be appended as a suffix to it.
2. If the name is not present in the map, you can use it without adding any suffixes.
3. If the name is present in the map, append the smallest proper suffix, and add the new name to the map.

## 示例

```
["pes","fifa","gta","pes(2019)"]
["gta","gta(1)","gta","avalon"]
["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> getFolderNames(vector<string>& names) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] getFolderNames(String[] names) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** getFolderNames(char** names, int namesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] GetFolderNames(string[] names) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} names
 * @return {string[]}
 */
var getFolderNames = function(names) {
    
};
```

### TypeScript

```typescript
function getFolderNames(names: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $names
     * @return String[]
     */
    function getFolderNames($names) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getFolderNames(_ names: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getFolderNames(names: Array<String>): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> getFolderNames(List<String> names) {
    
  }
}
```

### Go

```golang
func getFolderNames(names []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} names
# @return {String[]}
def get_folder_names(names)
    
end
```

### Scala

```scala
object Solution {
    def getFolderNames(names: Array[String]): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_folder_names(names: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (get-folder-names names)
  (-> (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec get_folder_names(Names :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
get_folder_names(Names) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_folder_names(names :: [String.t]) :: [String.t]
  def get_folder_names(names) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getFolderNames(names: Array<String>): Array<String> {

    }
}
```

