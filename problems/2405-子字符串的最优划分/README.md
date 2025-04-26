# 2405. 子字符串的最优划分

## 题目描述

<p>给你一个字符串 <code>s</code> ，请你将该字符串划分成一个或多个 <strong>子字符串</strong> ，并满足每个子字符串中的字符都是 <strong>唯一</strong> 的。也就是说，在单个子字符串中，字母的出现次数都不超过 <strong>一次</strong> 。</p>

<p>满足题目要求的情况下，返回 <strong>最少</strong> 需要划分多少个子字符串<em>。</em></p>

<p>注意，划分后，原字符串中的每个字符都应该恰好属于一个子字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abacaba"
<strong>输出：</strong>4
<strong>解释：</strong>
两种可行的划分方法分别是 ("a","ba","cab","a") 和 ("ab","a","ca","ba") 。
可以证明最少需要划分 4 个子字符串。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "ssssss"
<strong>输出：</strong>6
<strong>解释：
</strong>只存在一种可行的划分方法 ("s","s","s","s","s","s") 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 哈希表
- 字符串

## 提示

1. Try to come up with a greedy approach.
2. From left to right, extend every substring in the partition as much as possible.

## 示例

```
"abacaba"
"ssssss"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int partitionString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int partitionString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def partitionString(self, s: str) -> int:
        
```

### C

```c
int partitionString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int PartitionString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var partitionString = function(s) {
    
};
```

### TypeScript

```typescript
function partitionString(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function partitionString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func partitionString(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun partitionString(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int partitionString(String s) {
    
  }
}
```

### Go

```golang
func partitionString(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def partition_string(s)
    
end
```

### Scala

```scala
object Solution {
    def partitionString(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn partition_string(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (partition-string s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec partition_string(S :: unicode:unicode_binary()) -> integer().
partition_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec partition_string(s :: String.t) :: integer
  def partition_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func partitionString(s: String): Int64 {

    }
}
```

