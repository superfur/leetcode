# 2834. 找出美丽数组的最小和

## 题目描述

<p>给你两个正整数：<code>n</code> 和 <code>target</code> 。</p>

<p>如果数组 <code>nums</code> 满足下述条件，则称其为 <strong>美丽数组</strong> 。</p>

<ul>
	<li><code>nums.length == n</code>.</li>
	<li><code>nums</code> 由两两互不相同的正整数组成。</li>
	<li>在范围 <code>[0, n-1]</code> 内，<strong>不存在 </strong>两个 <strong>不同</strong> 下标 <code>i</code> 和 <code>j</code> ，使得 <code>nums[i] + nums[j] == target</code> 。</li>
</ul>

<p>返回符合条件的美丽数组所可能具备的 <strong>最小</strong> 和，并对结果进行取模 <code>10<sup>9</sup>&nbsp;+ 7</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2, target = 3
<strong>输出：</strong>4
<strong>解释：</strong>nums = [1,3] 是美丽数组。
- nums 的长度为 n = 2 。
- nums 由两两互不相同的正整数组成。
- 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。
可以证明 4 是符合条件的美丽数组所可能具备的最小和。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3, target = 3
<strong>输出：</strong>8
<strong>解释：</strong>
nums = [1,3,4] 是美丽数组。 
- nums 的长度为 n = 3 。 
- nums 由两两互不相同的正整数组成。 
- 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。
可以证明 8 是符合条件的美丽数组所可能具备的最小和。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 1, target = 1
<strong>输出：</strong>1
<strong>解释：</strong>nums = [1] 是美丽数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学

## 提示

1. <div class="_1l1MA">Greedily try to add the smallest possible number in the array <code>nums</code>, such that <code>nums</code> contains distinct positive integers, and there are no two indices <code>i</code> and <code>j</code> with <code>nums[i] + nums[j] == target</code>.</div>

## 示例

```
2
3
3
3
1
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumPossibleSum(int n, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumPossibleSum(int n, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumPossibleSum(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        
```

### C

```c
int minimumPossibleSum(int n, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumPossibleSum(int n, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} target
 * @return {number}
 */
var minimumPossibleSum = function(n, target) {
    
};
```

### TypeScript

```typescript
function minimumPossibleSum(n: number, target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $target
     * @return Integer
     */
    function minimumPossibleSum($n, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumPossibleSum(_ n: Int, _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumPossibleSum(n: Int, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumPossibleSum(int n, int target) {
    
  }
}
```

### Go

```golang
func minimumPossibleSum(n int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} target
# @return {Integer}
def minimum_possible_sum(n, target)
    
end
```

### Scala

```scala
object Solution {
    def minimumPossibleSum(n: Int, target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_possible_sum(n: i32, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-possible-sum n target)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_possible_sum(N :: integer(), Target :: integer()) -> integer().
minimum_possible_sum(N, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_possible_sum(n :: integer, target :: integer) :: integer
  def minimum_possible_sum(n, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumPossibleSum(n: Int64, target: Int64): Int64 {

    }
}
```

