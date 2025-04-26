# LCR 086. 分割回文串

## 题目描述

<p>给定一个字符串 <code>s</code> ，请将 <code>s</code> 分割成一些子串，使每个子串都是 <strong>回文串</strong> ，返回 s 所有可能的分割方案。</p>

<p><meta charset="UTF-8" /><strong>回文串</strong>&nbsp;是正着读和反着读都一样的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s =<strong> </strong>&quot;google&quot;
<strong>输出：</strong>[[&quot;g&quot;,&quot;o&quot;,&quot;o&quot;,&quot;g&quot;,&quot;l&quot;,&quot;e&quot;],[&quot;g&quot;,&quot;oo&quot;,&quot;g&quot;,&quot;l&quot;,&quot;e&quot;],[&quot;goog&quot;,&quot;l&quot;,&quot;e&quot;]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;aab&quot;
<strong>输出：</strong>[[&quot;a&quot;,&quot;a&quot;,&quot;b&quot;],[&quot;aa&quot;,&quot;b&quot;]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;a&quot;
<strong>输出：</strong>[[&quot;a&quot;]]</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s </code>仅由小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 131&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/palindrome-partitioning/">https://leetcode-cn.com/problems/palindrome-partitioning/</a></p>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 哈希表

## 示例

```
"google"
"aab"
"a"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {

    }
};
```

### Java

```java
class Solution {
    public String[][] partition(String s) {

    }
}
```

### Python

```python
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
```

### Python3

```python3
class Solution:
    def partition(self, s: str) -> List[List[str]]:
```

### C

```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** partition(char* s, int* returnSize, int** returnColumnSizes){

}
```

### C#

```csharp
public class Solution {
    public string[][] Partition(string s) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {

};
```

### TypeScript

```typescript
function partition(s: string): string[][] {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String[][]
     */
    function partition($s) {

    }
}
```

### Swift

```swift
class Solution {
    func partition(_ s: String) -> [[String]] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun partition(s: String): Array<Array<String>> {

    }
}
```

### Go

```golang
func partition(s string) [][]string {

}
```

### Ruby

```ruby
# @param {String} s
# @return {String[][]}
def partition(s)

end
```

### Scala

```scala
object Solution {
    def partition(s: String): Array[Array[String]] = {

    }
}
```

### Racket

```racket
(define/contract (partition s)
  (-> string? (listof (listof string?)))

  )
```

