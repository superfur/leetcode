# 1529. 最少的后缀翻转次数

## 题目描述

<p>给你一个长度为 <code>n</code> 、下标从 <strong>0</strong> 开始的二进制字符串 <code>target</code> 。你自己有另一个长度为 <code>n</code> 的二进制字符串 <code>s</code> ，最初每一位上都是 0 。你想要让 <code>s</code> 和 <code>target</code> 相等。</p>

<p>在一步操作，你可以选择下标 <code>i</code>（<code>0 &lt;= i &lt; n</code>）并翻转在 <strong>闭区间</strong> <code>[i, n - 1]</code> 内的所有位。翻转意味着 <code>'0'</code> 变为 <code>'1'</code> ，而 <code>'1'</code> 变为 <code>'0'</code> 。</p>

<div class="original__bRMd">
<div>
<p>返回使<em> </em><code>s</code><em> </em>与<em> </em><code>target</code> 相等需要的最少翻转次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>target = "10111"
<strong>输出：</strong>3
<strong>解释：</strong>最初，s = "00000" 。
选择下标 i = 2: "00<em><strong>000</strong></em>" -&gt; "00<em><strong>111</strong></em>"
选择下标 i = 0: "<em><strong>00111</strong></em>" -&gt; "<em><strong>11000</strong></em>"
选择下标 i = 1: "1<em><strong>1000</strong></em>" -&gt; "1<em><strong>0111</strong></em>"
要达成目标，需要至少 3 次翻转。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>target = "101"
<strong>输出：</strong>3
<strong>解释：</strong>最初，s = "000" 。
选择下标 i = 0: "<em><strong>000</strong></em>" -&gt; "<em><strong>111</strong></em>"
选择下标 i = 1: "1<em><strong>11</strong></em>" -&gt; "1<em><strong>00</strong></em>"
选择下标 i = 2: "10<em><strong>0</strong></em>" -&gt; "10<em><strong>1</strong></em>"
要达成目标，需要至少 3 次翻转。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>target = "00000"
<strong>输出：</strong>0
<strong>解释：</strong>由于 s 已经等于目标，所以不需要任何操作
</pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == target.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>target[i]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串

## 提示

1. Consider a strategy where the choice of bulb with number i is increasing. In such a strategy, you no longer need to worry about bulbs that have been set to the left.

## 示例

```
"10111"
"101"
"00000"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minFlips(string target) {
        
    }
};
```

### Java

```java
class Solution {
    public int minFlips(String target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minFlips(self, target: str) -> int:
        
```

### C

```c
int minFlips(char* target) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinFlips(string target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} target
 * @return {number}
 */
var minFlips = function(target) {
    
};
```

### TypeScript

```typescript
function minFlips(target: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $target
     * @return Integer
     */
    function minFlips($target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minFlips(_ target: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minFlips(target: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minFlips(String target) {
    
  }
}
```

### Go

```golang
func minFlips(target string) int {
    
}
```

### Ruby

```ruby
# @param {String} target
# @return {Integer}
def min_flips(target)
    
end
```

### Scala

```scala
object Solution {
    def minFlips(target: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_flips(target: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-flips target)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_flips(Target :: unicode:unicode_binary()) -> integer().
min_flips(Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_flips(target :: String.t) :: integer
  def min_flips(target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minFlips(target: String): Int64 {

    }
}
```

