# 1663. 具有给定数值的最小字符串

## 题目描述

<p><strong>小写字符 </strong>的 <strong>数值</strong> 是它在字母表中的位置（从 <code>1</code> 开始），因此 <code>a</code> 的数值为 <code>1</code> ，<code>b</code> 的数值为 <code>2</code> ，<code>c</code> 的数值为 <code>3</code> ，以此类推。</p>

<p>字符串由若干小写字符组成，<strong>字符串的数值</strong> 为各字符的数值之和。例如，字符串 <code>"abe"</code> 的数值等于 <code>1 + 2 + 5 = 8</code> 。</p>

<p>给你两个整数 <code>n</code> 和 <code>k</code> 。返回 <strong>长度</strong> 等于 <code>n</code> 且 <strong>数值</strong> 等于 <code>k</code> 的 <strong>字典序最小</strong> 的字符串。</p>

<p>注意，如果字符串 <code>x</code> 在字典排序中位于 <code>y</code> 之前，就认为 <code>x</code> 字典序比 <code>y</code> 小，有以下两种情况：</p>

<ul>
	<li><code>x</code> 是 <code>y</code> 的一个前缀；</li>
	<li>如果 <code>i</code> 是 <code>x[i] != y[i]</code> 的第一个位置，且 <code>x[i]</code> 在字母表中的位置比 <code>y[i]</code> 靠前。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, k = 27
<strong>输出：</strong>"aay"
<strong>解释：</strong>字符串的数值为 1 + 1 + 25 = 27，它是数值满足要求且长度等于 3 字典序最小的字符串。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 5, k = 73
<strong>输出：</strong>"aaszz"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>n <= k <= 26 * n</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串

## 提示

1. Think greedily.
2. If you build the string from the end to the beginning, it will always be optimal to put the highest possible character at the current index.

## 示例

```
3
27
5
73
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string getSmallestString(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String getSmallestString(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
```

### C

```c
char* getSmallestString(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string GetSmallestString(int n, int k) {
        
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
var getSmallestString = function(n, k) {
    
};
```

### TypeScript

```typescript
function getSmallestString(n: number, k: number): string {
    
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
    function getSmallestString($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getSmallestString(_ n: Int, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getSmallestString(n: Int, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String getSmallestString(int n, int k) {
    
  }
}
```

### Go

```golang
func getSmallestString(n int, k int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {String}
def get_smallest_string(n, k)
    
end
```

### Scala

```scala
object Solution {
    def getSmallestString(n: Int, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_smallest_string(n: i32, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (get-smallest-string n k)
  (-> exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec get_smallest_string(N :: integer(), K :: integer()) -> unicode:unicode_binary().
get_smallest_string(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_smallest_string(n :: integer, k :: integer) :: String.t
  def get_smallest_string(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getSmallestString(n: Int64, k: Int64): String {

    }
}
```

