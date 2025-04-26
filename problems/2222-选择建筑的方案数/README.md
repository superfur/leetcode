# 2222. 选择建筑的方案数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的二进制字符串&nbsp;<code>s</code>&nbsp;，它表示一条街沿途的建筑类型，其中：</p>

<ul>
	<li><code>s[i] = '0'</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;栋建筑是一栋办公楼，</li>
	<li><code>s[i] = '1'</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;栋建筑是一间餐厅。</li>
</ul>

<p>作为市政厅的官员，你需要随机<strong>&nbsp;选择</strong>&nbsp;3 栋建筑。然而，为了确保多样性，选出来的 3 栋建筑 <strong>相邻</strong>&nbsp;的两栋不能是同一类型。</p>

<ul>
	<li>比方说，给你&nbsp;<code>s = "0<em><strong>0</strong></em>1<em><strong>1</strong></em>0<em><strong>1</strong></em>"</code>&nbsp;，我们不能选择第&nbsp;<code>1</code>&nbsp;，<code>3</code>&nbsp;和&nbsp;<code>5</code>&nbsp;栋建筑，因为得到的子序列是&nbsp;<code>"0<em><strong>11</strong></em>"</code>&nbsp;，有相邻两栋建筑是同一类型，所以 <strong>不合</strong>&nbsp;题意。</li>
</ul>

<p>请你返回可以选择 3 栋建筑的 <strong>有效方案数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "001101"
<b>输出：</b>6
<b>解释：</b>
以下下标集合是合法的：
- [0,2,4] ，从 "<em><strong>0</strong></em>0<em><strong>1</strong></em>1<em><strong>0</strong></em>1" 得到 "010"
- [0,3,4] ，从 "<em><strong>0</strong></em>01<em><strong>10</strong></em>1" 得到 "010"
- [1,2,4] ，从 "0<em><strong>01</strong></em>1<em><strong>0</strong></em>1" 得到 "010"
- [1,3,4] ，从 "0<em><strong>0</strong></em>1<em><strong>10</strong></em>1" 得到 "010"
- [2,4,5] ，从 "00<em><strong>1</strong></em>1<em><strong>01</strong></em>" 得到 "101"
- [3,4,5] ，从 "001<em><strong>101</strong></em>" 得到 "101"
没有别的合法选择，所以总共有 6 种方法。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "11100"
<b>输出：</b>0
<b>解释：</b>没有任何符合题意的选择。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code>&nbsp;要么是&nbsp;<code>'0'</code>&nbsp;，要么是&nbsp;<code>'1'</code>&nbsp;。</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 动态规划
- 前缀和

## 提示

1. There are only 2 valid patterns: ‘101’ and ‘010’. Think about how we can construct these 2 patterns from smaller patterns.
2. Count the number of subsequences of the form ‘01’ or ‘10’ first. Let n01[i] be the number of ‘01’ subsequences that exist in the prefix of s up to the ith building. How can you compute n01[i]?
3. Let n0[i] and n1[i] be the number of ‘0’s and ‘1’s that exists in the prefix of s up to i respectively. Then n01[i] = n01[i – 1] if s[i] == ‘0’, otherwise n01[i] = n01[i – 1] + n0[i – 1].
4. The same logic applies to building the n10 array and subsequently the n101 and n010 arrays for the number of ‘101’ and ‘010‘ subsequences.

## 示例

```
"001101"
"11100"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long numberOfWays(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public long numberOfWays(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfWays(self, s: str) -> int:
        
```

### C

```c
long long numberOfWays(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public long NumberOfWays(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numberOfWays = function(s) {
    
};
```

### TypeScript

```typescript
function numberOfWays(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numberOfWays($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfWays(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfWays(s: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfWays(String s) {
    
  }
}
```

### Go

```golang
func numberOfWays(s string) int64 {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def number_of_ways(s)
    
end
```

### Scala

```scala
object Solution {
    def numberOfWays(s: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_ways(s: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-ways s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_ways(S :: unicode:unicode_binary()) -> integer().
number_of_ways(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_ways(s :: String.t) :: integer
  def number_of_ways(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfWays(s: String): Int64 {

    }
}
```

