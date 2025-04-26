# 1399. 统计最大组的数目

## 题目描述

<p>给你一个整数 <code>n</code>&nbsp;。请你先求出从 <code>1</code>&nbsp;到 <code>n</code> 的每个整数 10 进制表示下的数位和（每一位上的数字相加），然后把数位和相等的数字放到同一个组中。</p>

<p>请你统计每个组中的数字数目，并返回数字数目并列最多的组有多少个。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 13
<strong>输出：</strong>4
<strong>解释：</strong>总共有 9 个组，将 1 到 13 按数位求和后这些组分别是：
[1,10]，[2,11]，[3,12]，[4,13]，[5]，[6]，[7]，[8]，[9]。总共有 4 个组拥有的数字并列最多。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>2
<strong>解释：</strong>总共有 2 个大小为 1 的组 [1]，[2]。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 15
<strong>输出：</strong>6
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>n = 24
<strong>输出：</strong>5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^4</code></li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 数学

## 提示

1. Count the digit sum for each integer in the range and find out the largest groups.

## 示例

```
13
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countLargestGroup(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int countLargestGroup(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countLargestGroup(self, n: int) -> int:
        
```

### C

```c
int countLargestGroup(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountLargestGroup(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function(n) {
    
};
```

### TypeScript

```typescript
function countLargestGroup(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countLargestGroup($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countLargestGroup(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countLargestGroup(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countLargestGroup(int n) {
    
  }
}
```

### Go

```golang
func countLargestGroup(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def count_largest_group(n)
    
end
```

### Scala

```scala
object Solution {
    def countLargestGroup(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_largest_group(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-largest-group n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_largest_group(N :: integer()) -> integer().
count_largest_group(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_largest_group(n :: integer) :: integer
  def count_largest_group(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countLargestGroup(n: Int64): Int64 {

    }
}
```

