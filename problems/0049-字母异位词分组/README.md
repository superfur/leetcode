# 49. 字母异位词分组

## 题目描述

<p>给你一个字符串数组，请你将 <strong>字母异位词</strong> 组合在一起。可以按任意顺序返回结果列表。</p>

<p><strong>字母异位词</strong> 是由重新排列源单词的所有字母得到的一个新单词。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> strs = <code>["eat", "tea", "tan", "ate", "nat", "bat"]</code>
<strong>输出: </strong>[["bat"],["nat","tan"],["ate","eat","tea"]]</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> strs = <code>[""]</code>
<strong>输出: </strong>[[""]]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> strs = <code>["a"]</code>
<strong>输出: </strong>[["a"]]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code>&nbsp;仅包含小写字母</li>
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
["eat","tea","tan","ate","nat","bat"]
[""]
["a"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
```

### Python3

```python3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** groupAnagrams(char** strs, int strsSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    
};
```

### TypeScript

```typescript
function groupAnagrams(strs: string[]): string[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $strs
     * @return String[][]
     */
    function groupAnagrams($strs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<String>> groupAnagrams(List<String> strs) {
    
  }
}
```

### Go

```golang
func groupAnagrams(strs []string) [][]string {
    
}
```

### Ruby

```ruby
# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
    
end
```

### Scala

```scala
object Solution {
    def groupAnagrams(strs: Array[String]): List[List[String]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        
    }
}
```

### Racket

```racket
(define/contract (group-anagrams strs)
  (-> (listof string?) (listof (listof string?)))
  )
```

### Erlang

```erlang
-spec group_anagrams(Strs :: [unicode:unicode_binary()]) -> [[unicode:unicode_binary()]].
group_anagrams(Strs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec group_anagrams(strs :: [String.t]) :: [[String.t]]
  def group_anagrams(strs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func groupAnagrams(strs: Array<String>): ArrayList<ArrayList<String>> {

    }
}
```

