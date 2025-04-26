# 3091. 执行操作使数据元素之和大于等于 K

## 题目描述

<p>给你一个<strong>正整数</strong> <code>k</code> 。最初，你有一个数组 <code>nums = [1]</code> 。</p>

<p>你可以对数组执行以下 <strong>任意 </strong>操作 <strong>任意 </strong>次数（<strong>可能为零</strong>）：</p>

<ul>
	<li>选择数组中的任何一个元素，然后将它的值<strong> 增加</strong> <code>1</code> 。</li>
	<li>复制数组中的任何一个元素，然后将它附加到数组的末尾。</li>
</ul>

<p>返回使得最终数组元素之<strong> 和 </strong>大于或等于 <code>k</code> 所需的 <strong>最少 </strong>操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">k = 11</span></p>

<p><strong>输出：</strong><span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p>可以对数组 <code>nums = [1]</code> 执行以下操作：</p>

<ul>
	<li>将元素的值增加 <code>1</code> 三次。结果数组为 <code>nums = [4]</code> 。</li>
	<li>复制元素两次。结果数组为 <code>nums = [4,4,4]</code> 。</li>
</ul>

<p>最终数组的和为 <code>4 + 4 + 4 = 12</code> ，大于等于 <code>k = 11</code> 。<br />
执行的总操作次数为 <code>3 + 2 = 5</code> 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">k = 1</span></p>

<p><strong>输出：</strong><span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>原始数组的和已经大于等于 <code>1</code> ，因此不需要执行操作。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学
- 枚举

## 提示

1. It is optimal to make all the increase operations first and all the duplicate operations last.
2. Iterate over all possible number of increase operations that can be done and find the corresponding number of duplicate operations.

## 示例

```
11
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, k):
        """
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, k: int) -> int:
        
```

### C

```c
int minOperations(int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @return {number}
 */
var minOperations = function(k) {
    
};
```

### TypeScript

```typescript
function minOperations(k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @return Integer
     */
    function minOperations($k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(int k) {
    
  }
}
```

### Go

```golang
func minOperations(k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @return {Integer}
def min_operations(k)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations k)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(K :: integer()) -> integer().
min_operations(K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(k :: integer) :: integer
  def min_operations(k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(k: Int64): Int64 {

    }
}
```

