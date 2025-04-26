# 942. 增减字符串匹配

## 题目描述

<p>由范围 <code>[0,n]</code> 内所有整数组成的 <code>n + 1</code> 个整数的排列序列可以表示为长度为 <code>n</code> 的字符串 <code>s</code> ，其中:</p>

<ul>
	<li>如果&nbsp;<code>perm[i] &lt; perm[i + 1]</code>&nbsp;，那么&nbsp;<code>s[i] == 'I'</code>&nbsp;</li>
	<li>如果&nbsp;<code>perm[i] &gt; perm[i + 1]</code>&nbsp;，那么 <code>s[i] == 'D'</code>&nbsp;</li>
</ul>

<p>给定一个字符串 <code>s</code> ，重构排列&nbsp;<code>perm</code> 并返回它。如果有多个有效排列perm，则返回其中 <strong>任何一个</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "IDID"
<strong>输出：</strong>[0,4,1,3,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "III"
<strong>输出：</strong>[0,1,2,3]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "DDI"
<strong>输出：</strong>[3,2,0,1]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code><font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">s</span></span></font></font></code> 只包含字符&nbsp;<code>"I"</code>&nbsp;或&nbsp;<code>"D"</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 双指针
- 字符串

## 示例

```
"IDID"
"III"
"DDI"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> diStringMatch(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] diStringMatch(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* diStringMatch(char* s, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] DiStringMatch(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number[]}
 */
var diStringMatch = function(s) {
    
};
```

### TypeScript

```typescript
function diStringMatch(s: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer[]
     */
    function diStringMatch($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func diStringMatch(_ s: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun diStringMatch(s: String): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> diStringMatch(String s) {
    
  }
}
```

### Go

```golang
func diStringMatch(s string) []int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer[]}
def di_string_match(s)
    
end
```

### Scala

```scala
object Solution {
    def diStringMatch(s: String): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn di_string_match(s: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (di-string-match s)
  (-> string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec di_string_match(S :: unicode:unicode_binary()) -> [integer()].
di_string_match(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec di_string_match(s :: String.t) :: [integer]
  def di_string_match(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func diStringMatch(s: String): Array<Int64> {

    }
}
```

