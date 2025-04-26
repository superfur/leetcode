# 793. 阶乘函数后 K 个零

## 题目描述

<p>&nbsp;<code>f(x)</code>&nbsp;是&nbsp;<code>x!</code>&nbsp;末尾是 0 的数量。回想一下&nbsp;<code>x! = 1 * 2 * 3 * ... * x</code>，且 <code>0! = 1</code>&nbsp;。</p>

<ul>
	<li>例如，&nbsp;<code>f(3) = 0</code>&nbsp;，因为 <code>3! = 6</code> 的末尾没有 0 ；而 <code>f(11) = 2</code>&nbsp;，因为 <code>11!= 39916800</code> 末端有 2 个 0 。</li>
</ul>

<p>给定&nbsp;<code>k</code>，找出返回能满足 <code>f(x) = k</code>&nbsp;的非负整数 <code>x</code>&nbsp;的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong><strong> </strong></p>

<pre>
<strong>输入：</strong>k = 0<strong>
输出：</strong>5<strong>
解释：</strong>0!, 1!, 2!, 3!, 和 4!&nbsp;均符合 k = 0 的条件。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>k = 5
<strong>输出：</strong>0
<strong>解释：</strong>没有匹配到这样的 x!，符合 k = 5 的条件。</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> k = 3
<strong>输出:</strong> 5
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>0 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 二分查找

## 示例

```
0
5
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int preimageSizeFZF(int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int preimageSizeFZF(int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def preimageSizeFZF(self, k):
        """
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        
```

### C

```c
int preimageSizeFZF(int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int PreimageSizeFZF(int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @return {number}
 */
var preimageSizeFZF = function(k) {
    
};
```

### TypeScript

```typescript
function preimageSizeFZF(k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @return Integer
     */
    function preimageSizeFZF($k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func preimageSizeFZF(_ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun preimageSizeFZF(k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int preimageSizeFZF(int k) {
    
  }
}
```

### Go

```golang
func preimageSizeFZF(k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @return {Integer}
def preimage_size_fzf(k)
    
end
```

### Scala

```scala
object Solution {
    def preimageSizeFZF(k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn preimage_size_fzf(k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (preimage-size-fzf k)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec preimage_size_fzf(K :: integer()) -> integer().
preimage_size_fzf(K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec preimage_size_fzf(k :: integer) :: integer
  def preimage_size_fzf(k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func preimageSizeFZF(k: Int64): Int64 {

    }
}
```

