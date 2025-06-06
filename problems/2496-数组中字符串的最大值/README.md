# 2496. 数组中字符串的最大值

## 题目描述

<p>一个由字母和数字组成的字符串的 <strong>值</strong>&nbsp;定义如下：</p>

<ul>
	<li>如果字符串 <strong>只</strong> 包含数字，那么值为该字符串在 <code>10</code>&nbsp;进制下的所表示的数字。</li>
	<li>否则，值为字符串的 <strong>长度&nbsp;</strong>。</li>
</ul>

<p>给你一个字符串数组&nbsp;<code>strs</code>&nbsp;，每个字符串都只由字母和数字组成，请你返回 <code>strs</code>&nbsp;中字符串的 <strong>最大值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>strs = ["alic3","bob","3","4","00000"]
<b>输出：</b>5
<b>解释：</b>
- "alic3" 包含字母和数字，所以值为长度 5 。
- "bob" 只包含字母，所以值为长度 3 。
- "3" 只包含数字，所以值为 3 。
- "4" 只包含数字，所以值为 4 。
- "00000" 只包含数字，所以值为 0 。
所以最大的值为 5 ，是字符串 "alic3" 的值。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>strs = ["1","01","001","0001"]
<b>输出：</b>1
<b>解释：</b>
数组中所有字符串的值都是 1 ，所以我们返回 1 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 100</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 9</code></li>
	<li><code>strs[i]</code>&nbsp;只包含小写英文字母和数字。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. For strings comprising only of digits, convert them into integers.
2. For all other strings, calculate their length.

## 示例

```
["alic3","bob","3","4","00000"]
["1","01","001","0001"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumValue(vector<string>& strs) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumValue(String[] strs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
```

### C

```c
int maximumValue(char** strs, int strsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumValue(string[] strs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} strs
 * @return {number}
 */
var maximumValue = function(strs) {
    
};
```

### TypeScript

```typescript
function maximumValue(strs: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $strs
     * @return Integer
     */
    function maximumValue($strs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumValue(_ strs: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumValue(strs: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumValue(List<String> strs) {
    
  }
}
```

### Go

```golang
func maximumValue(strs []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} strs
# @return {Integer}
def maximum_value(strs)
    
end
```

### Scala

```scala
object Solution {
    def maximumValue(strs: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_value(strs: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-value strs)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_value(Strs :: [unicode:unicode_binary()]) -> integer().
maximum_value(Strs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_value(strs :: [String.t]) :: integer
  def maximum_value(strs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumValue(strs: Array<String>): Int64 {

    }
}
```

