# 833. 字符串中的查找与替换

## 题目描述

<p>你会得到一个字符串 <code>s</code>&nbsp;(索引从 0 开始)，你必须对它执行 <code>k</code> 个替换操作。替换操作以三个长度均为 <code>k</code> 的并行数组给出：<code>indices</code>,&nbsp;<code>sources</code>,&nbsp;&nbsp;<code>targets</code>。</p>

<p>要完成第 <code>i</code> 个替换操作:</p>

<ol>
	<li>检查 <strong>子字符串</strong> &nbsp;<code>sources[i]</code>&nbsp;是否出现在 <strong>原字符串</strong> <code>s</code> 的索引&nbsp;<code>indices[i]</code>&nbsp;处。</li>
	<li>如果没有出现，&nbsp;<strong>什么也不做</strong>&nbsp;。</li>
	<li>如果出现，则用&nbsp;<code>targets[i]</code>&nbsp;<strong>替换</strong>&nbsp;该子字符串。</li>
</ol>

<p>例如，如果 <code>s = "abcd"</code>&nbsp;，&nbsp;<code>indices[i] = 0</code> ,&nbsp;<code>sources[i] = "ab"</code>， <code>targets[i] = "eee"</code> ，那么替换的结果将是 <code>"<u>eee</u>cd"</code> 。</p>

<p>所有替换操作必须 <strong>同时</strong> 发生，这意味着替换操作不应该影响彼此的索引。测试用例保证元素间<strong>不会重叠 </strong>。</p>

<ul>
	<li>例如，一个 <code>s = "abc"</code> ，&nbsp; <code>indices = [0,1]</code> ， <code>sources = ["ab"，"bc"]</code>&nbsp;的测试用例将不会生成，因为 <code>"ab"</code> 和 <code>"bc"</code> 替换重叠。</li>
</ul>

<p><em>在对 <code>s</code>&nbsp;执行所有替换操作后返回 <strong>结果字符串</strong> 。</em></p>

<p><strong>子字符串</strong> 是字符串中连续的字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/06/12/833-ex1.png" /></p>

<pre>
<strong>输入：</strong>s = "abcd", indices = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
<strong>输出：</strong>"eeebffff"
<strong>解释：
</strong>"a" 从 s 中的索引 0 开始，所以它被替换为 "eee"。
"cd" 从 s 中的索引 2 开始，所以它被替换为 "ffff"。
</pre>

<p><strong>示例 2：</strong><img src="https://assets.leetcode.com/uploads/2021/06/12/833-ex2-1.png" /></p>

<pre>
<strong>输入：</strong>s = "abcd", indices = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
<strong>输出：</strong>"eeecd"
<strong>解释：
</strong>"ab" 从 s 中的索引 0 开始，所以它被替换为 "eee"。
"ec" 没有从<strong>原始的</strong> S 中的索引 2 开始，所以它没有被替换。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>k == indices.length == sources.length == targets.length</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
	<li><code>0 &lt;= indices[i] &lt; s.length</code></li>
	<li><code>1 &lt;= sources[i].length, targets[i].length &lt;= 50</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
	<li><code>sources[i]</code> 和 <code>targets[i]</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 排序

## 示例

```
"abcd"
[0, 2]
["a", "cd"]
["eee", "ffff"]
"abcd"
[0, 2]
["ab","ec"]
["eee","ffff"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string findReplaceString(string s, vector<int>& indices, vector<string>& sources, vector<string>& targets) {
        
    }
};
```

### Java

```java
class Solution {
    public String findReplaceString(String s, int[] indices, String[] sources, String[] targets) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
```

### C

```c
char* findReplaceString(char* s, int* indices, int indicesSize, char** sources, int sourcesSize, char** targets, int targetsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string FindReplaceString(string s, int[] indices, string[] sources, string[] targets) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number[]} indices
 * @param {string[]} sources
 * @param {string[]} targets
 * @return {string}
 */
var findReplaceString = function(s, indices, sources, targets) {
    
};
```

### TypeScript

```typescript
function findReplaceString(s: string, indices: number[], sources: string[], targets: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[] $indices
     * @param String[] $sources
     * @param String[] $targets
     * @return String
     */
    function findReplaceString($s, $indices, $sources, $targets) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findReplaceString(_ s: String, _ indices: [Int], _ sources: [String], _ targets: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findReplaceString(s: String, indices: IntArray, sources: Array<String>, targets: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String findReplaceString(String s, List<int> indices, List<String> sources, List<String> targets) {
    
  }
}
```

### Go

```golang
func findReplaceString(s string, indices []int, sources []string, targets []string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer[]} indices
# @param {String[]} sources
# @param {String[]} targets
# @return {String}
def find_replace_string(s, indices, sources, targets)
    
end
```

### Scala

```scala
object Solution {
    def findReplaceString(s: String, indices: Array[Int], sources: Array[String], targets: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_replace_string(s: String, indices: Vec<i32>, sources: Vec<String>, targets: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (find-replace-string s indices sources targets)
  (-> string? (listof exact-integer?) (listof string?) (listof string?) string?)
  )
```

### Erlang

```erlang
-spec find_replace_string(S :: unicode:unicode_binary(), Indices :: [integer()], Sources :: [unicode:unicode_binary()], Targets :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
find_replace_string(S, Indices, Sources, Targets) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_replace_string(s :: String.t, indices :: [integer], sources :: [String.t], targets :: [String.t]) :: String.t
  def find_replace_string(s, indices, sources, targets) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findReplaceString(s: String, indices: Array<Int64>, sources: Array<String>, targets: Array<String>): String {

    }
}
```

