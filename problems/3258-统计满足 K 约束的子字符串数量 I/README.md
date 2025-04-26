# 3258. 统计满足 K 约束的子字符串数量 I

## 题目描述

<p>给你一个 <strong>二进制</strong> 字符串 <code>s</code> 和一个整数 <code>k</code>。</p>

<p>如果一个 <strong>二进制字符串</strong> 满足以下任一条件，则认为该字符串满足 <strong>k 约束</strong>：</p>

<ul>
	<li>字符串中 <code>0</code> 的数量最多为 <code>k</code>。</li>
	<li>字符串中 <code>1</code> 的数量最多为 <code>k</code>。</li>
</ul>

<p>返回一个整数，表示 <code>s</code> 的所有满足 <strong>k 约束 </strong>的<span data-keyword="substring-nonempty">子字符串</span>的数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "10101", k = 1</span></p>

<p><strong>输出：</strong><span class="example-io">12</span></p>

<p><strong>解释：</strong></p>

<p><code>s</code> 的所有子字符串中，除了 <code>"1010"</code>、<code>"10101"</code> 和 <code>"0101"</code> 外，其余子字符串都满足 k 约束。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "1010101", k = 2</span></p>

<p><strong>输出：</strong><span class="example-io">25</span></p>

<p><strong>解释：</strong></p>

<p><code>s</code> 的所有子字符串中，除了长度大于 5 的子字符串外，其余子字符串都满足 k 约束。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "11111", k = 1</span></p>

<p><strong>输出：</strong><span class="example-io">15</span></p>

<p><strong>解释：</strong></p>

<p><code>s</code> 的所有子字符串都满足 k 约束。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
	<li><code>s[i]</code> 是 <code>'0'</code> 或 <code>'1'</code>。</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 滑动窗口

## 提示

1. Using a brute force approach, check each index until a substring satisfying the k-constraint is found, then increment.

## 示例

```
"10101"
1
"1010101"
2
"11111"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countKConstraintSubstrings(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int countKConstraintSubstrings(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        
```

### C

```c
int countKConstraintSubstrings(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountKConstraintSubstrings(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var countKConstraintSubstrings = function(s, k) {
    
};
```

### TypeScript

```typescript
function countKConstraintSubstrings(s: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function countKConstraintSubstrings($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countKConstraintSubstrings(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countKConstraintSubstrings(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countKConstraintSubstrings(String s, int k) {
    
  }
}
```

### Go

```golang
func countKConstraintSubstrings(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def count_k_constraint_substrings(s, k)
    
end
```

### Scala

```scala
object Solution {
    def countKConstraintSubstrings(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_k_constraint_substrings(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-k-constraint-substrings s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_k_constraint_substrings(S :: unicode:unicode_binary(), K :: integer()) -> integer().
count_k_constraint_substrings(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_k_constraint_substrings(s :: String.t, k :: integer) :: integer
  def count_k_constraint_substrings(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countKConstraintSubstrings(s: String, k: Int64): Int64 {

    }
}
```

