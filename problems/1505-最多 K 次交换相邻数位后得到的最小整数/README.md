# 1505. 最多 K 次交换相邻数位后得到的最小整数

## 题目描述

<p>给你一个字符串&nbsp;<code>num</code> 和一个整数&nbsp;<code>k</code> 。其中，<code>num</code> 表示一个很大的整数，字符串中的每个字符依次对应整数上的各个 <strong>数位</strong> 。</p>

<p>你可以交换这个整数相邻数位的数字 <strong>最多</strong>&nbsp;<code>k</code>&nbsp;次。</p>

<p>请你返回你能得到的最小整数，并以字符串形式返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/06/17/q4_1.jpg" style="height:40px; width:500px" /></p>

<pre>
<strong>输入：</strong>num = &quot;4321&quot;, k = 4
<strong>输出：</strong>&quot;1342&quot;
<strong>解释：</strong>4321 通过 4 次交换相邻数位得到最小整数的步骤如上图所示。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = &quot;100&quot;, k = 1
<strong>输出：</strong>&quot;010&quot;
<strong>解释：</strong>输出可以包含前导 0 ，但输入保证不会有前导 0 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>num = &quot;36789&quot;, k = 1000
<strong>输出：</strong>&quot;36789&quot;
<strong>解释：</strong>不需要做任何交换。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>num = &quot;22&quot;, k = 22
<strong>输出：</strong>&quot;22&quot;
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>num = &quot;9438957234785635408&quot;, k = 23
<strong>输出：</strong>&quot;0345989723478563548&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 30000</code></li>
	<li><code>num</code>&nbsp;只包含&nbsp;<strong>数字</strong>&nbsp;且不含有<strong>&nbsp;前导 0&nbsp;</strong>。</li>
	<li><code>1 &lt;= k &lt;= 10^9</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 树状数组
- 线段树
- 字符串

## 提示

1. We want to make the smaller digits the most significant digits in the number.
2. For each index i, check the smallest digit in a window of size k and append it to the answer. Update the indices of all digits in this range accordingly.

## 示例

```
"4321"
4
"100"
1
"36789"
1000
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string minInteger(string num, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String minInteger(String num, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minInteger(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        
```

### C

```c
char* minInteger(char* num, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string MinInteger(string num, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var minInteger = function(num, k) {
    
};
```

### TypeScript

```typescript
function minInteger(num: string, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @param Integer $k
     * @return String
     */
    function minInteger($num, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minInteger(_ num: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minInteger(num: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String minInteger(String num, int k) {
    
  }
}
```

### Go

```golang
func minInteger(num string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} num
# @param {Integer} k
# @return {String}
def min_integer(num, k)
    
end
```

### Scala

```scala
object Solution {
    def minInteger(num: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_integer(num: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (min-integer num k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec min_integer(Num :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
min_integer(Num, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_integer(num :: String.t, k :: integer) :: String.t
  def min_integer(num, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minInteger(num: String, k: Int64): String {

    }
}
```

