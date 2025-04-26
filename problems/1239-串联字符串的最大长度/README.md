# 1239. 串联字符串的最大长度

## 题目描述

<p>给定一个字符串数组 <code>arr</code>，字符串 <code>s</code> 是将 <code>arr</code>&nbsp;的含有 <strong>不同字母</strong> 的&nbsp;<strong>子序列</strong> 字符串 <strong>连接</strong> 所得的字符串。</p>

<p>请返回所有可行解 <code>s</code> 中最长长度。</p>

<p><strong>子序列</strong> 是一种可以从另一个数组派生而来的数组，通过删除某些元素或不删除元素而不改变其余元素的顺序。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = ["un","iq","ue"]
<strong>输出：</strong>4
<strong>解释：</strong>所有可能的串联组合是：
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
最大长度为 4。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = ["cha","r","act","ers"]
<strong>输出：</strong>6
<strong>解释：</strong>可能的解答有 "chaers" 和 "acters"。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = ["abcdefghijklmnopqrstuvwxyz"]
<strong>输出：</strong>26
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 16</code></li>
	<li><code>1 &lt;= arr[i].length &lt;= 26</code></li>
	<li><code>arr[i]</code>&nbsp;中只含有小写英文字母</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 字符串
- 回溯

## 提示

1. You can try all combinations and keep mask of characters you have.
2. You can use DP.

## 示例

```
["un","iq","ue"]
["cha","r","act","ers"]
["abcdefghijklmnopqrstuvwxyz"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxLength(vector<string>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxLength(List<String> arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
```

### C

```c
int maxLength(char** arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxLength(IList<string> arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} arr
 * @return {number}
 */
var maxLength = function(arr) {
    
};
```

### TypeScript

```typescript
function maxLength(arr: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $arr
     * @return Integer
     */
    function maxLength($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxLength(_ arr: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxLength(arr: List<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxLength(List<String> arr) {
    
  }
}
```

### Go

```golang
func maxLength(arr []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} arr
# @return {Integer}
def max_length(arr)
    
end
```

### Scala

```scala
object Solution {
    def maxLength(arr: List[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_length(arr: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-length arr)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_length(Arr :: [unicode:unicode_binary()]) -> integer().
max_length(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_length(arr :: [String.t]) :: integer
  def max_length(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxLength(arr: ArrayList<String>): Int64 {

    }
}
```

