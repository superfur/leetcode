# 2053. 数组中第 K 个独一无二的字符串

## 题目描述

<p><strong>独一无二的字符串</strong>&nbsp;指的是在一个数组中只出现过 <strong>一次</strong>&nbsp;的字符串。</p>

<p>给你一个字符串数组&nbsp;<code>arr</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;，请你返回&nbsp;<code>arr</code>&nbsp;中第&nbsp;<code>k</code>&nbsp;个&nbsp;<strong>独一无二的字符串</strong>&nbsp;。如果&nbsp;<strong>少于</strong>&nbsp;<code>k</code>&nbsp;个独一无二的字符串，那么返回&nbsp;<strong>空字符串</strong>&nbsp;<code>""</code>&nbsp;。</p>

<p>注意，按照字符串在原数组中的 <strong>顺序</strong>&nbsp;找到第 <code>k</code>&nbsp;个独一无二字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><b>输入：</b>arr = ["d","b","c","b","c","a"], k = 2
<b>输出：</b>"a"
<strong>解释：</strong>
arr 中独一无二字符串包括 "d" 和 "a"<code>&nbsp;。</code>
"d" 首先出现，所以它是第 1 个独一无二字符串。
"a" 第二个出现，所以它是 2 个独一无二字符串。
由于 k == 2 ，返回 "a" 。
</pre>

<p><strong>示例 2:</strong></p>

<pre><b>输入：</b>arr = ["aaa","aa","a"], k = 1
<b>输出：</b>"aaa"
<strong>解释：</strong>
arr 中所有字符串都是独一无二的，所以返回第 1 个字符串 "aaa" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>arr = ["a","b","a"], k = 3
<b>输出：</b>""
<strong>解释：</strong>
唯一一个独一无二字符串是 "b" 。由于少于 3 个独一无二字符串，我们返回空字符串 "" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= arr.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr[i].length &lt;= 5</code></li>
	<li><code>arr[i]</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 字符串
- 计数

## 提示

1. Try 'mapping' the strings to check if they are unique or not.

## 示例

```
["d","b","c","b","c","a"]
2
["aaa","aa","a"]
1
["a","b","a"]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String kthDistinct(String[] arr, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
```

### C

```c
char* kthDistinct(char** arr, int arrSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string KthDistinct(string[] arr, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} arr
 * @param {number} k
 * @return {string}
 */
var kthDistinct = function(arr, k) {
    
};
```

### TypeScript

```typescript
function kthDistinct(arr: string[], k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $arr
     * @param Integer $k
     * @return String
     */
    function kthDistinct($arr, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kthDistinct(_ arr: [String], _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kthDistinct(arr: Array<String>, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String kthDistinct(List<String> arr, int k) {
    
  }
}
```

### Go

```golang
func kthDistinct(arr []string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String[]} arr
# @param {Integer} k
# @return {String}
def kth_distinct(arr, k)
    
end
```

### Scala

```scala
object Solution {
    def kthDistinct(arr: Array[String], k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn kth_distinct(arr: Vec<String>, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (kth-distinct arr k)
  (-> (listof string?) exact-integer? string?)
  )
```

### Erlang

```erlang
-spec kth_distinct(Arr :: [unicode:unicode_binary()], K :: integer()) -> unicode:unicode_binary().
kth_distinct(Arr, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec kth_distinct(arr :: [String.t], k :: integer) :: String.t
  def kth_distinct(arr, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kthDistinct(arr: Array<String>, k: Int64): String {

    }
}
```

