# 771. 宝石与石头

## 题目描述

<p>&nbsp;给你一个字符串 <code>jewels</code>&nbsp;代表石头中宝石的类型，另有一个字符串 <code>stones</code> 代表你拥有的石头。&nbsp;<code>stones</code>&nbsp;中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。</p>

<p>字母区分大小写，因此 <code>"a"</code> 和 <code>"A"</code> 是不同类型的石头。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>jewels = "aA", stones = "aAAbbbb"
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>jewels = "z", stones = "ZZ"
<strong>输出：</strong>0<strong>
</strong></pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;jewels.length, stones.length &lt;= 50</code></li>
	<li><code>jewels</code> 和 <code>stones</code> 仅由英文字母组成</li>
	<li><code>jewels</code> 中的所有字符都是 <strong>唯一的</strong></li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. For each stone, check if it is a jewel.

## 示例

```
"aA"
"aAAbbbb"
"z"
"ZZ"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        
    }
};
```

### Java

```java
class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
```

### C

```c
int numJewelsInStones(char* jewels, char* stones) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumJewelsInStones(string jewels, string stones) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    
};
```

### TypeScript

```typescript
function numJewelsInStones(jewels: string, stones: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $jewels
     * @param String $stones
     * @return Integer
     */
    function numJewelsInStones($jewels, $stones) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numJewelsInStones(_ jewels: String, _ stones: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numJewelsInStones(jewels: String, stones: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numJewelsInStones(String jewels, String stones) {
    
  }
}
```

### Go

```golang
func numJewelsInStones(jewels string, stones string) int {
    
}
```

### Ruby

```ruby
# @param {String} jewels
# @param {String} stones
# @return {Integer}
def num_jewels_in_stones(jewels, stones)
    
end
```

### Scala

```scala
object Solution {
    def numJewelsInStones(jewels: String, stones: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-jewels-in-stones jewels stones)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_jewels_in_stones(Jewels :: unicode:unicode_binary(), Stones :: unicode:unicode_binary()) -> integer().
num_jewels_in_stones(Jewels, Stones) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_jewels_in_stones(jewels :: String.t, stones :: String.t) :: integer
  def num_jewels_in_stones(jewels, stones) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numJewelsInStones(jewels: String, stones: String): Int64 {

    }
}
```

