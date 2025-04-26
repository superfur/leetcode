# 1415. 长度为 n 的开心字符串中字典序第 k 小的字符串

## 题目描述

<p>一个 「开心字符串」定义为：</p>

<ul>
	<li>仅包含小写字母&nbsp;<code>[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]</code>.</li>
	<li>对所有在&nbsp;<code>1</code>&nbsp;到&nbsp;<code>s.length - 1</code>&nbsp;之间的&nbsp;<code>i</code>&nbsp;，满足&nbsp;<code>s[i] != s[i + 1]</code>&nbsp;（字符串的下标从 1 开始）。</li>
</ul>

<p>比方说，字符串&nbsp;<strong>&quot;abc&quot;</strong>，<strong>&quot;ac&quot;，&quot;b&quot;</strong> 和&nbsp;<strong>&quot;abcbabcbcb&quot;</strong>&nbsp;都是开心字符串，但是&nbsp;<strong>&quot;aa&quot;</strong>，<strong>&quot;baa&quot;</strong>&nbsp;和&nbsp;<strong>&quot;ababbc&quot;</strong>&nbsp;都不是开心字符串。</p>

<p>给你两个整数 <code>n</code>&nbsp;和 <code>k</code>&nbsp;，你需要将长度为 <code>n</code>&nbsp;的所有开心字符串按字典序排序。</p>

<p>请你返回排序后的第 k 个开心字符串，如果长度为 <code>n</code>&nbsp;的开心字符串少于 <code>k</code>&nbsp;个，那么请你返回 <strong>空字符串</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 1, k = 3
<strong>输出：</strong>&quot;c&quot;
<strong>解释：</strong>列表 [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 &quot;c&quot; 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 1, k = 4
<strong>输出：</strong>&quot;&quot;
<strong>解释：</strong>长度为 1 的开心字符串只有 3 个。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 3, k = 9
<strong>输出：</strong>&quot;cab&quot;
<strong>解释：</strong>长度为 3 的开心字符串总共有 12 个 [&quot;aba&quot;, &quot;abc&quot;, &quot;aca&quot;, &quot;acb&quot;, &quot;bab&quot;, &quot;bac&quot;, &quot;bca&quot;, &quot;bcb&quot;, &quot;cab&quot;, &quot;cac&quot;, &quot;cba&quot;, &quot;cbc&quot;] 。第 9 个字符串为 &quot;cab&quot;
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>n = 2, k = 7
<strong>输出：</strong>&quot;&quot;
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>n = 10, k = 100
<strong>输出：</strong>&quot;abacbabacb&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 字符串
- 回溯

## 提示

1. Generate recursively all the happy strings of length n.
2. Sort them in lexicographical order and return the kth string if it exists.

## 示例

```
1
3
1
4
3
9
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string getHappyString(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String getHappyString(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
```

### C

```c
char* getHappyString(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string GetHappyString(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getHappyString = function(n, k) {
    
};
```

### TypeScript

```typescript
function getHappyString(n: number, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function getHappyString($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getHappyString(_ n: Int, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getHappyString(n: Int, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String getHappyString(int n, int k) {
    
  }
}
```

### Go

```golang
func getHappyString(n int, k int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {String}
def get_happy_string(n, k)
    
end
```

### Scala

```scala
object Solution {
    def getHappyString(n: Int, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_happy_string(n: i32, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (get-happy-string n k)
  (-> exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec get_happy_string(N :: integer(), K :: integer()) -> unicode:unicode_binary().
get_happy_string(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_happy_string(n :: integer, k :: integer) :: String.t
  def get_happy_string(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getHappyString(n: Int64, k: Int64): String {

    }
}
```

