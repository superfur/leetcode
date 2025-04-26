# 3389. 使字符频率相等的最少操作次数

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>&nbsp;。</p>

<p>如果字符串 <code>t</code>&nbsp;中的字符出现次数相等，那么我们称&nbsp;<code>t</code>&nbsp;为 <strong>好的</strong>&nbsp;。</p>

<p>你可以执行以下操作 <strong>任意次</strong>&nbsp;：</p>

<ul>
	<li>从&nbsp;<code>s</code>&nbsp;中删除一个字符。</li>
	<li>往&nbsp;<code>s</code>&nbsp;中添加一个字符。</li>
	<li>将&nbsp;<code>s</code>&nbsp;中一个字母变成字母表中下一个字母。</li>
</ul>

<p><b>注意</b>&nbsp;，第三个操作不能将&nbsp;<code>'z'</code>&nbsp;变为&nbsp;<code>'a'</code>&nbsp;。</p>

<p>请你返回将 <code>s</code>&nbsp;变 <strong>好</strong>&nbsp;的 <strong>最少</strong>&nbsp;操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "acab"</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><b>解释：</b></p>

<p>删掉一个字符&nbsp;<code>'a'</code>&nbsp;，<code>s</code>&nbsp;变为好的。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "wddw"</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<p><code>s</code>&nbsp;一开始就是好的，所以不需要执行任何操作。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>s = "aaabc"</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>通过以下操作，将&nbsp;<code>s</code>&nbsp;变好：</p>

<ul>
	<li>将一个&nbsp;<code>'a'</code>&nbsp;变为&nbsp;<code>'b'</code>&nbsp;。</li>
	<li>往 <code>s</code>&nbsp;中插入一个&nbsp;<code>'c'</code>&nbsp;。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2&nbsp;* 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 哈希表
- 字符串
- 动态规划
- 计数
- 枚举

## 提示

1. The order of the letters in the string is irrelevant.
2. Compute an occurrence array <code>occ</code> where <code>occ[x]</code> is the number of occurrences of the <code>x<supth</sup></code> character of the alphabet. How do the described operations change <code>occ</code>?
3. We have three types of operations: increase any <code>occ[x]</code> by 1, decrease any <code>occ[x]</code> by 1, or decrease any <code>occ[x]</code> by 1 and simultaneously increase <code>occ[x + 1]</code> by 1 at the same time. To make <code>s</code> good, we need to make <code>occ</code> good. <code>occ</code> is good if and only if every <code>occ[x]</code> equals either 0 or some constant <code>c</code>.
4. If you know the value of <code>c</code>, how can you calculate the minimum operations required to make <code>occ</code> good?
5. Observation 1: It is never optimal to apply the third type of operation (simultaneous decrease and increase) on two continuous elements <code>occ[x]</code> and <code>occ[x + 1]</code>. Instead, we can decrease <code>occ[x]</code> by 1 then increase <code>occ[x + 2]</code> by 1 to achieve the same effect.
6. Observation 2: It is never optimal to increase an element of <code>occ</code> then decrease it, or vice versa.
7. Use dynamic programming where <code>dp[i]</code> is the minimum number of operations required to make <code>occ[0..i]</code> good. You will need to use the above observations to come up with the transitions.

## 示例

```
"acab"
"wddw"
"aaabbc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int makeStringGood(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int makeStringGood(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeStringGood(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def makeStringGood(self, s: str) -> int:
        
```

### C

```c
int makeStringGood(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MakeStringGood(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var makeStringGood = function(s) {
    
};
```

### TypeScript

```typescript
function makeStringGood(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function makeStringGood($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeStringGood(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeStringGood(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int makeStringGood(String s) {
    
  }
}
```

### Go

```golang
func makeStringGood(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def make_string_good(s)
    
end
```

### Scala

```scala
object Solution {
    def makeStringGood(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_string_good(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (make-string-good s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec make_string_good(S :: unicode:unicode_binary()) -> integer().
make_string_good(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_string_good(s :: String.t) :: integer
  def make_string_good(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeStringGood(s: String): Int64 {

    }
}
```

