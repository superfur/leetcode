# 1646. 获取生成数组中的最大值

## 题目描述

<p>给你一个整数 <code>n</code> 。按下述规则生成一个长度为 <code>n + 1</code> 的数组 <code>nums</code> ：</p>

<ul>
	<li><code>nums[0] = 0</code></li>
	<li><code>nums[1] = 1</code></li>
	<li>当 <code>2 <= 2 * i <= n</code> 时，<code>nums[2 * i] = nums[i]</code></li>
	<li>当 <code>2 <= 2 * i + 1 <= n</code> 时，<code>nums[2 * i + 1] = nums[i] + nums[i + 1]</code></li>
</ul>

<p>返回生成数组 <code>nums</code> 中的 <strong>最大</strong> 值。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 7
<strong>输出：</strong>3
<strong>解释：</strong>根据规则：
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
因此，nums = [0,1,1,2,1,3,2,3]，最大值 3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>1
<strong>解释：</strong>根据规则，nums[0]、nums[1] 和 nums[2] 之中的最大值是 1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>2
<strong>解释：</strong>根据规则，nums[0]、nums[1]、nums[2] 和 nums[3] 之中的最大值是 2
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= n <= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 模拟

## 提示

1. Try generating the array.
2. Make sure not to fall in the base case of 0.

## 示例

```
7
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getMaximumGenerated(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int getMaximumGenerated(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
```

### C

```c
int getMaximumGenerated(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetMaximumGenerated(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var getMaximumGenerated = function(n) {
    
};
```

### TypeScript

```typescript
function getMaximumGenerated(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function getMaximumGenerated($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getMaximumGenerated(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMaximumGenerated(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getMaximumGenerated(int n) {
    
  }
}
```

### Go

```golang
func getMaximumGenerated(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def get_maximum_generated(n)
    
end
```

### Scala

```scala
object Solution {
    def getMaximumGenerated(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_maximum_generated(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-maximum-generated n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec get_maximum_generated(N :: integer()) -> integer().
get_maximum_generated(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_maximum_generated(n :: integer) :: integer
  def get_maximum_generated(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getMaximumGenerated(n: Int64): Int64 {

    }
}
```

