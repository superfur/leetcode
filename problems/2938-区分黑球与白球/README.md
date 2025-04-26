# 2938. 区分黑球与白球

## 题目描述

<p>桌子上有 <code>n</code> 个球，每个球的颜色不是黑色，就是白色。</p>

<p>给你一个长度为 <code>n</code> 、下标从 <strong>0</strong> 开始的二进制字符串 <code>s</code>，其中 <code>1</code> 和 <code>0</code> 分别代表黑色和白色的球。</p>

<p>在每一步中，你可以选择两个相邻的球并交换它们。</p>

<p>返回「将所有黑色球都移到右侧，所有白色球都移到左侧所需的 <strong>最小步数</strong>」。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "101"
<strong>输出：</strong>1
<strong>解释：</strong>我们可以按以下方式将所有黑色球移到右侧：
- 交换 s[0] 和 s[1]，s = "011"。
最开始，1 没有都在右侧，需要至少 1 步将其移到右侧。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "100"
<strong>输出：</strong>2
<strong>解释：</strong>我们可以按以下方式将所有黑色球移到右侧：
- 交换 s[0] 和 s[1]，s = "010"。
- 交换 s[1] 和 s[2]，s = "001"。
可以证明所需的最小步数为 2 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "0111"
<strong>输出：</strong>0
<strong>解释：</strong>所有黑色球都已经在右侧。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 不是 <code>'0'</code>，就是 <code>'1'</code>。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 双指针
- 字符串

## 提示

1. Every <code>1</code> in the string <code>s</code> should be swapped with every <code>0</code> on its right side.
2. Iterate right to left and count the number of <code>0</code> that have already occurred, whenever you iterate on <code>1</code> add that counter to the answer.

## 示例

```
"101"
"100"
"0111"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumSteps(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumSteps(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumSteps(self, s: str) -> int:
        
```

### C

```c
long long minimumSteps(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumSteps(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumSteps = function(s) {
    
};
```

### TypeScript

```typescript
function minimumSteps(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumSteps($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumSteps(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumSteps(s: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumSteps(String s) {
    
  }
}
```

### Go

```golang
func minimumSteps(s string) int64 {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def minimum_steps(s)
    
end
```

### Scala

```scala
object Solution {
    def minimumSteps(s: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_steps(s: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-steps s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_steps(S :: unicode:unicode_binary()) -> integer().
minimum_steps(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_steps(s :: String.t) :: integer
  def minimum_steps(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumSteps(s: String): Int64 {

    }
}
```

