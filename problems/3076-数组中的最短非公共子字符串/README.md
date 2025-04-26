# 3076. 数组中的最短非公共子字符串

## 题目描述

<p>给你一个数组 <code>arr</code>&nbsp;，数组中有 <code>n</code>&nbsp;个 <b>非空</b>&nbsp;字符串。</p>

<p>请你求出一个长度为 <code>n</code>&nbsp;的字符串数组&nbsp;<code>answer</code>&nbsp;，满足：</p>

<ul>
	<li><code>answer[i]</code>&nbsp;是 <code>arr[i]</code>&nbsp;<strong>最短</strong>&nbsp;的子字符串，且它不是 <code>arr</code>&nbsp;中其他任何字符串的子字符串。如果有多个这样的子字符串存在，<code>answer[i]</code>&nbsp;应该是它们中字典序最小的一个。如果不存在这样的子字符串，<code>answer[i]</code>&nbsp;为空字符串。</li>
</ul>

<p>请你返回数组<em>&nbsp;</em><code>answer</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>arr = ["cab","ad","bad","c"]
<b>输出：</b>["ab","","ba",""]
<b>解释：</b>求解过程如下：
- 对于字符串 "cab" ，最短没有在其他字符串中出现过的子字符串是 "ca" 或者 "ab" ，我们选择字典序更小的子字符串，也就是 "ab" 。
- 对于字符串 "ad" ，不存在没有在其他字符串中出现过的子字符串。
- 对于字符串 "bad" ，最短没有在其他字符串中出现过的子字符串是 "ba" 。
- 对于字符串 "c" ，不存在没有在其他字符串中出现过的子字符串。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>arr = ["abc","bcd","abcd"]
<b>输出：</b>["","","abcd"]
<b>解释：</b>求解过程如下：
- 对于字符串 "abc" ，不存在没有在其他字符串中出现过的子字符串。
- 对于字符串 "bcd" ，不存在没有在其他字符串中出现过的子字符串。
- 对于字符串 "abcd" ，最短没有在其他字符串中出现过的子字符串是 "abcd" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == arr.length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= arr[i].length &lt;= 20</code></li>
	<li><code>arr[i]</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 数组
- 哈希表
- 字符串

## 提示

1. Try a brute force solution where you check every substring.
2. Use a Hash map to keep track of the substrings.

## 示例

```
["cab","ad","bad","c"]
["abc","bcd","abcd"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> shortestSubstrings(vector<string>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public String[] shortestSubstrings(String[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestSubstrings(self, arr):
        """
        :type arr: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** shortestSubstrings(char** arr, int arrSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string[] ShortestSubstrings(string[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} arr
 * @return {string[]}
 */
var shortestSubstrings = function(arr) {
    
};
```

### TypeScript

```typescript
function shortestSubstrings(arr: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $arr
     * @return String[]
     */
    function shortestSubstrings($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestSubstrings(_ arr: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestSubstrings(arr: Array<String>): Array<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> shortestSubstrings(List<String> arr) {
    
  }
}
```

### Go

```golang
func shortestSubstrings(arr []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} arr
# @return {String[]}
def shortest_substrings(arr)
    
end
```

### Scala

```scala
object Solution {
    def shortestSubstrings(arr: Array[String]): Array[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_substrings(arr: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-substrings arr)
  (-> (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec shortest_substrings(Arr :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
shortest_substrings(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_substrings(arr :: [String.t]) :: [String.t]
  def shortest_substrings(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestSubstrings(arr: Array<String>): Array<String> {

    }
}
```

