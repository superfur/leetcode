# 1528. 重新排列字符串

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个 <strong>长度相同</strong> 的整数数组 <code>indices</code> 。</p>

<p>请你重新排列字符串 <code>s</code> ，其中第 <code>i</code> 个字符需要移动到 <code>indices[i]</code> 指示的位置。</p>

<p>返回重新排列后的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/26/q1.jpg" /></p>

<pre>
<strong>输入：</strong>s = "codeleet", <code>indices</code> = [4,5,6,7,0,2,1,3]
<strong>输出：</strong>"leetcode"
<strong>解释：</strong>如图所示，"codeleet" 重新排列后变为 "leetcode" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abc", <code>indices</code> = [0,1,2]
<strong>输出：</strong>"abc"
<strong>解释：</strong>重新排列后，每个字符都还留在原来的位置上。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>s.length == indices.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>s</code> 仅包含小写英文字母</li>
	<li><code>0 &lt;= indices[i] &lt;&nbsp;n</code></li>
	<li><code>indices</code> 的所有的值都是 <strong>唯一</strong> 的</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. You can create an auxiliary string t of length n.
2. Assign t[indexes[i]] to s[i] for each i from 0 to n-1.

## 示例

```
"codeleet"
[4,5,6,7,0,2,1,3]
"abc"
[0,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        
    }
};
```

### Java

```java
class Solution {
    public String restoreString(String s, int[] indices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
```

### C

```c
char* restoreString(char* s, int* indices, int indicesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string RestoreString(string s, int[] indices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
    
};
```

### TypeScript

```typescript
function restoreString(s: string, indices: number[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[] $indices
     * @return String
     */
    function restoreString($s, $indices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func restoreString(_ s: String, _ indices: [Int]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun restoreString(s: String, indices: IntArray): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String restoreString(String s, List<int> indices) {
    
  }
}
```

### Go

```golang
func restoreString(s string, indices []int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer[]} indices
# @return {String}
def restore_string(s, indices)
    
end
```

### Scala

```scala
object Solution {
    def restoreString(s: String, indices: Array[Int]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn restore_string(s: String, indices: Vec<i32>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (restore-string s indices)
  (-> string? (listof exact-integer?) string?)
  )
```

### Erlang

```erlang
-spec restore_string(S :: unicode:unicode_binary(), Indices :: [integer()]) -> unicode:unicode_binary().
restore_string(S, Indices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec restore_string(s :: String.t, indices :: [integer]) :: String.t
  def restore_string(s, indices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func restoreString(s: String, indices: Array<Int64>): String {

    }
}
```

