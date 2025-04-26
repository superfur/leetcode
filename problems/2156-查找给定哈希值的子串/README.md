# 2156. 查找给定哈希值的子串

## 题目描述

<p>给定整数 <code>p</code>&nbsp;和 <code>m</code>&nbsp;，一个长度为 <code>k</code>&nbsp;且下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>s</code>&nbsp;的哈希值按照如下函数计算：</p>

<ul>
	<li><code>hash(s, p, m) = (val(s[0]) * p<sup>0</sup> + val(s[1]) * p<sup>1</sup> + ... + val(s[k-1]) * p<sup>k-1</sup>) mod m</code>.</li>
</ul>

<p>其中&nbsp;<code>val(s[i])</code>&nbsp;表示&nbsp;<code>s[i]</code>&nbsp;在字母表中的下标，从&nbsp;<code>val('a') = 1</code> 到&nbsp;<code>val('z') = 26</code>&nbsp;。</p>

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;和整数&nbsp;<code>power</code>，<code>modulo</code>，<code>k</code>&nbsp;和&nbsp;<code>hashValue</code>&nbsp;。请你返回 <code>s</code>&nbsp;中 <strong>第一个</strong> 长度为 <code>k</code>&nbsp;的 <strong>子串</strong>&nbsp;<code>sub</code>&nbsp;，满足<em>&nbsp;</em><code>hash(sub, power, modulo) == hashValue</code>&nbsp;。</p>

<p>测试数据保证一定 <strong>存在</strong>&nbsp;至少一个这样的子串。</p>

<p><strong>子串</strong> 定义为一个字符串中连续非空字符组成的序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0
<strong>输出：</strong>"ee"
<strong>解释：</strong>"ee" 的哈希值为 hash("ee", 7, 20) = (5 * 1 + 5 * 7) mod 20 = 40 mod 20 = 0 。
"ee" 是长度为 2 的第一个哈希值为 0 的子串，所以我们返回 "ee" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32
<b>输出：</b>"fbx"
<b>解释：</b>"fbx" 的哈希值为 hash("fbx", 31, 100) = (6 * 1 + 2 * 31 + 24 * 31<sup>2</sup>) mod 100 = 23132 mod 100 = 32 。
"bxz" 的哈希值为 hash("bxz", 31, 100) = (2 * 1 + 24 * 31 + 26 * 31<sup>2</sup>) mod 100 = 25732 mod 100 = 32 。
"fbx" 是长度为 3 的第一个哈希值为 32 的子串，所以我们返回 "fbx" 。
注意，"bxz" 的哈希值也为 32 ，但是它在字符串中比 "fbx" 更晚出现。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= s.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= power, modulo &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= hashValue &lt; modulo</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
	<li>测试数据保证一定 <strong>存在</strong>&nbsp;满足条件的子串。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 滑动窗口
- 哈希函数
- 滚动哈希

## 提示

1. How can we update the hash value efficiently while iterating instead of recalculating it each time?
2. Use the rolling hash method.

## 示例

```
"leetcode"
7
20
2
0
"fbxzaad"
31
100
3
32
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string subStrHash(string s, int power, int modulo, int k, int hashValue) {
        
    }
};
```

### Java

```java
class Solution {
    public String subStrHash(String s, int power, int modulo, int k, int hashValue) {
        
    }
}
```

### Python

```python
class Solution(object):
    def subStrHash(self, s, power, modulo, k, hashValue):
        """
        :type s: str
        :type power: int
        :type modulo: int
        :type k: int
        :type hashValue: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
```

### C

```c
char* subStrHash(char* s, int power, int modulo, int k, int hashValue) {
    
}
```

### C#

```csharp
public class Solution {
    public string SubStrHash(string s, int power, int modulo, int k, int hashValue) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} power
 * @param {number} modulo
 * @param {number} k
 * @param {number} hashValue
 * @return {string}
 */
var subStrHash = function(s, power, modulo, k, hashValue) {
    
};
```

### TypeScript

```typescript
function subStrHash(s: string, power: number, modulo: number, k: number, hashValue: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $power
     * @param Integer $modulo
     * @param Integer $k
     * @param Integer $hashValue
     * @return String
     */
    function subStrHash($s, $power, $modulo, $k, $hashValue) {
        
    }
}
```

### Swift

```swift
class Solution {
    func subStrHash(_ s: String, _ power: Int, _ modulo: Int, _ k: Int, _ hashValue: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subStrHash(s: String, power: Int, modulo: Int, k: Int, hashValue: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String subStrHash(String s, int power, int modulo, int k, int hashValue) {
    
  }
}
```

### Go

```golang
func subStrHash(s string, power int, modulo int, k int, hashValue int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} power
# @param {Integer} modulo
# @param {Integer} k
# @param {Integer} hash_value
# @return {String}
def sub_str_hash(s, power, modulo, k, hash_value)
    
end
```

### Scala

```scala
object Solution {
    def subStrHash(s: String, power: Int, modulo: Int, k: Int, hashValue: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sub_str_hash(s: String, power: i32, modulo: i32, k: i32, hash_value: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (sub-str-hash s power modulo k hashValue)
  (-> string? exact-integer? exact-integer? exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec sub_str_hash(S :: unicode:unicode_binary(), Power :: integer(), Modulo :: integer(), K :: integer(), HashValue :: integer()) -> unicode:unicode_binary().
sub_str_hash(S, Power, Modulo, K, HashValue) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sub_str_hash(s :: String.t, power :: integer, modulo :: integer, k :: integer, hash_value :: integer) :: String.t
  def sub_str_hash(s, power, modulo, k, hash_value) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func subStrHash(s: String, power: Int64, modulo: Int64, k: Int64, hashValue: Int64): String {

    }
}
```

