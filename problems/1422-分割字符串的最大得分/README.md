# 1422. 分割字符串的最大得分

## 题目描述

<p>给你一个由若干 0 和 1 组成的字符串 <code>s</code> ，请你计算并返回将该字符串分割成两个 <strong>非空</strong> 子字符串（即&nbsp;<strong>左</strong> 子字符串和 <strong>右</strong> 子字符串）所能获得的最大得分。</p>

<p>「分割字符串的得分」为 <strong>左</strong> 子字符串中 <strong>0</strong> 的数量加上 <strong>右</strong> 子字符串中 <strong>1</strong> 的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;011101&quot;
<strong>输出：</strong>5 
<strong>解释：</strong>
将字符串 s 划分为两个非空子字符串的可行方案有：
左子字符串 = &quot;0&quot; 且 右子字符串 = &quot;11101&quot;，得分 = 1 + 4 = 5 
左子字符串 = &quot;01&quot; 且 右子字符串 = &quot;1101&quot;，得分 = 1 + 3 = 4 
左子字符串 = &quot;011&quot; 且 右子字符串 = &quot;101&quot;，得分 = 1 + 2 = 3 
左子字符串 = &quot;0111&quot; 且 右子字符串 = &quot;01&quot;，得分 = 1 + 1 = 2 
左子字符串 = &quot;01110&quot; 且 右子字符串 = &quot;1&quot;，得分 = 2 + 1 = 3
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;00111&quot;
<strong>输出：</strong>5
<strong>解释：</strong>当 左子字符串 = &quot;00&quot; 且 右子字符串 = &quot;111&quot; 时，我们得到最大得分 = 2 + 3 = 5
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;1111&quot;
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 500</code></li>
	<li>字符串 <code>s</code> 仅由字符 <code>&#39;0&#39;</code> 和 <code>&#39;1&#39;</code> 组成。</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 前缀和

## 提示

1. Precompute a prefix sum of ones ('1').
2. Iterate from left to right counting the number of zeros ('0'), then use the precomputed prefix sum for counting ones ('1'). Update the answer.

## 示例

```
"011101"
"00111"
"1111"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxScore(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxScore(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxScore(self, s: str) -> int:
        
```

### C

```c
int maxScore(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxScore(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxScore = function(s) {
    
};
```

### TypeScript

```typescript
function maxScore(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maxScore($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxScore(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxScore(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxScore(String s) {
    
  }
}
```

### Go

```golang
func maxScore(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def max_score(s)
    
end
```

### Scala

```scala
object Solution {
    def maxScore(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_score(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-score s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_score(S :: unicode:unicode_binary()) -> integer().
max_score(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_score(s :: String.t) :: integer
  def max_score(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxScore(s: String): Int64 {

    }
}
```

