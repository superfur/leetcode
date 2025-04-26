# 面试题 17.17. 多次搜索

## 题目描述

<p>给定一个较长字符串<code>big</code>和一个包含较短字符串的数组<code>smalls</code>，设计一个方法，根据<code>smalls</code>中的每一个较短字符串，对<code>big</code>进行搜索。输出<code>smalls</code>中的字符串在<code>big</code>里出现的所有位置<code>positions</code>，其中<code>positions[i]</code>为<code>smalls[i]</code>出现的所有位置。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>
big = &quot;mississippi&quot;
smalls = [&quot;is&quot;,&quot;ppi&quot;,&quot;hi&quot;,&quot;sis&quot;,&quot;i&quot;,&quot;ssippi&quot;]
<strong>输出：</strong> [[1,4],[8],[],[3],[1,4,7,10],[5]]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= len(big) &lt;= 1000</code></li>
	<li><code>0 &lt;= len(smalls[i]) &lt;= 1000</code></li>
	<li><code>smalls</code>的总字符数不会超过 100000。</li>
	<li>你可以认为<code>smalls</code>中没有重复字符串。</li>
	<li>所有出现的字符均为英文小写字母。</li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 数组
- 哈希表
- 字符串
- 字符串匹配
- 滑动窗口

## 提示

1. 从蛮力解法开始。运行时间是多少？
2. 你能用trie吗?
3. 一种解决方案是将较大字符串的每个后缀都插入trie。例如，如果单词是dogs，那么后缀应该是dogs、ogs、gs和s。这将如何帮助你解决该问题？其运行时间是多少？
4. 或者，可以将每个较小的字符串插入到trie中。你将如何解决这个问题？时间复杂度是什么？

## 示例

```
""
["a","b","c"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> multiSearch(string big, vector<string>& smalls) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] multiSearch(String big, String[] smalls) {
        
    }
}
```

### Python

```python
class Solution(object):
    def multiSearch(self, big, smalls):
        """
        :type big: str
        :type smalls: List[str]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** multiSearch(char* big, char** smalls, int smallsSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] MultiSearch(string big, string[] smalls) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} big
 * @param {string[]} smalls
 * @return {number[][]}
 */
var multiSearch = function(big, smalls) {
    
};
```

### TypeScript

```typescript
function multiSearch(big: string, smalls: string[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $big
     * @param String[] $smalls
     * @return Integer[][]
     */
    function multiSearch($big, $smalls) {
        
    }
}
```

### Swift

```swift
class Solution {
    func multiSearch(_ big: String, _ smalls: [String]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun multiSearch(big: String, smalls: Array<String>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> multiSearch(String big, List<String> smalls) {
    
  }
}
```

### Go

```golang
func multiSearch(big string, smalls []string) [][]int {
    
}
```

### Ruby

```ruby
# @param {String} big
# @param {String[]} smalls
# @return {Integer[][]}
def multi_search(big, smalls)
    
end
```

### Scala

```scala
object Solution {
    def multiSearch(big: String, smalls: Array[String]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn multi_search(big: String, smalls: Vec<String>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (multi-search big smalls)
  (-> string? (listof string?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec multi_search(Big :: unicode:unicode_binary(), Smalls :: [unicode:unicode_binary()]) -> [[integer()]].
multi_search(Big, Smalls) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec multi_search(big :: String.t, smalls :: [String.t]) :: [[integer]]
  def multi_search(big, smalls) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func multiSearch(big: String, smalls: Array<String>): Array<Array<Int64>> {

    }
}
```

