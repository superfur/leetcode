# 1304. 和为零的 N 个不同整数

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>，请你返回 <strong>任意&nbsp;</strong>一个由 <code>n</code>&nbsp;个 <strong>各不相同&nbsp;</strong>的整数组成的数组，并且这 <code>n</code> 个数相加和为 <code>0</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 5
<strong>输出：</strong>[-7,-1,1,3,4]
<strong>解释：</strong>这些数组也是正确的 [-5,-1,1,2,3]，[-3,-1,2,-2,4]。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 3
<strong>输出：</strong>[-1,0,1]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 1
<strong>输出：</strong>[0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学

## 提示

1. Return an array where the values are symmetric. (+x , -x).
2. If n is odd, append value 0 in your returned array.

## 示例

```
5
3
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> sumZero(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] sumZero(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def sumZero(self, n: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumZero(int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SumZero(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    
};
```

### TypeScript

```typescript
function sumZero(n: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function sumZero($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumZero(_ n: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumZero(n: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> sumZero(int n) {
    
  }
}
```

### Go

```golang
func sumZero(n int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer[]}
def sum_zero(n)
    
end
```

### Scala

```scala
object Solution {
    def sumZero(n: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_zero(n: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (sum-zero n)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec sum_zero(N :: integer()) -> [integer()].
sum_zero(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_zero(n :: integer) :: [integer]
  def sum_zero(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumZero(n: Int64): Array<Int64> {

    }
}
```

