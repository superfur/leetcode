# 1023. 驼峰式匹配

## 题目描述

<p>给你一个字符串数组 <code>queries</code>，和一个表示模式的字符串&nbsp;<code>pattern</code>，请你返回一个布尔数组 <code>answer</code> 。只有在待查项&nbsp;<code>queries[i]</code> 与模式串&nbsp;<code>pattern</code> 匹配时，&nbsp;<code>answer[i]</code>&nbsp;才为 <code>true</code>，否则为 <code>false</code>。</p>

<p>如果可以将&nbsp;<strong>小写字母&nbsp;</strong>插入模式串&nbsp;<code>pattern</code>&nbsp;得到待查询项&nbsp;<code>queries[i]</code>，那么待查询项与给定模式串匹配。您可以在模式串中的任何位置插入字符，也可以选择不插入任何字符。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
<strong>输出：</strong>[true,false,true,true,false]
<strong>示例：</strong>
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
<strong>输出：</strong>[true,false,true,false,false]
<strong>解释：</strong>
"FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
"FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
<strong>输出：</strong>[false,true,false,false,false]
<strong>解释： </strong>
"FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= pattern.length, queries.length &lt;= 100</code></li>
	<li><code>1 &lt;= queries[i].length &lt;= 100</code></li>
	<li><code>queries[i]</code> 和 <code>pattern</code> 由英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 数组
- 双指针
- 字符串
- 字符串匹配

## 提示

1. Given a single pattern and word, how can we solve it?
2. One way to do it is using a DP (pos1, pos2) where pos1 is a pointer to the word and pos2 to the pattern and returns true if we can match the pattern with the given word.
3. We have two scenarios: The first one is when `word[pos1] == pattern[pos2]`, then the transition will be just DP(pos1 + 1, pos2 + 1). The second scenario is when `word[pos1]` is lowercase then we can add this character to the pattern so that the transition is just DP(pos1 + 1, pos2)
The case base is `if (pos1 == n && pos2 == m) return true;` Where n and m are the sizes of the strings word and pattern respectively.

## 示例

```
["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
"FB"
["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
"FoBa"
["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
"FoBaT"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<bool> camelMatch(vector<string>& queries, string pattern) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Boolean> camelMatch(String[] queries, String pattern) {
        
    }
}
```

### Python

```python
class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        
```

### Python3

```python3
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* camelMatch(char** queries, int queriesSize, char* pattern, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<bool> CamelMatch(string[] queries, string pattern) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} queries
 * @param {string} pattern
 * @return {boolean[]}
 */
var camelMatch = function(queries, pattern) {
    
};
```

### TypeScript

```typescript
function camelMatch(queries: string[], pattern: string): boolean[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $queries
     * @param String $pattern
     * @return Boolean[]
     */
    function camelMatch($queries, $pattern) {
        
    }
}
```

### Swift

```swift
class Solution {
    func camelMatch(_ queries: [String], _ pattern: String) -> [Bool] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun camelMatch(queries: Array<String>, pattern: String): List<Boolean> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<bool> camelMatch(List<String> queries, String pattern) {
    
  }
}
```

### Go

```golang
func camelMatch(queries []string, pattern string) []bool {
    
}
```

### Ruby

```ruby
# @param {String[]} queries
# @param {String} pattern
# @return {Boolean[]}
def camel_match(queries, pattern)
    
end
```

### Scala

```scala
object Solution {
    def camelMatch(queries: Array[String], pattern: String): List[Boolean] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn camel_match(queries: Vec<String>, pattern: String) -> Vec<bool> {
        
    }
}
```

### Racket

```racket
(define/contract (camel-match queries pattern)
  (-> (listof string?) string? (listof boolean?))
  )
```

### Erlang

```erlang
-spec camel_match(Queries :: [unicode:unicode_binary()], Pattern :: unicode:unicode_binary()) -> [boolean()].
camel_match(Queries, Pattern) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec camel_match(queries :: [String.t], pattern :: String.t) :: [boolean]
  def camel_match(queries, pattern) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func camelMatch(queries: Array<String>, pattern: String): ArrayList<Bool> {

    }
}
```

