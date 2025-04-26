# 372. 超级次方

## 题目描述

<p>你的任务是计算 <code>a<sup>b</sup></code> 对 <code>1337</code> 取模，<code>a</code> 是一个正整数，<code>b</code> 是一个非常大的正整数且会以数组形式给出。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>a = 2, b = [3]
<strong>输出：</strong>8
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>a = 2, b = [1,0]
<strong>输出：</strong>1024
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>a = 1, b = [4,3,3,8,5,2]
<strong>输出：</strong>1
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>a = 2147483647, b = [2,0,0]
<strong>输出：</strong>1198
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= a <= 2<sup>31</sup> - 1</code></li>
	<li><code>1 <= b.length <= 2000</code></li>
	<li><code>0 <= b[i] <= 9</code></li>
	<li><code>b</code> 不含前导 0</li>
</ul>


## 难度

Medium

## 标签

- 数学
- 分治

## 示例

```
2
[3]
2
[1,0]
1
[4,3,3,8,5,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int superPow(int a, vector<int>& b) {
        
    }
};
```

### Java

```java
class Solution {
    public int superPow(int a, int[] b) {
        
    }
}
```

### Python

```python
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
```

### C

```c
int superPow(int a, int* b, int bSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SuperPow(int a, int[] b) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} a
 * @param {number[]} b
 * @return {number}
 */
var superPow = function(a, b) {
    
};
```

### TypeScript

```typescript
function superPow(a: number, b: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer[] $b
     * @return Integer
     */
    function superPow($a, $b) {
        
    }
}
```

### Swift

```swift
class Solution {
    func superPow(_ a: Int, _ b: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun superPow(a: Int, b: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int superPow(int a, List<int> b) {
    
  }
}
```

### Go

```golang
func superPow(a int, b []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} a
# @param {Integer[]} b
# @return {Integer}
def super_pow(a, b)
    
end
```

### Scala

```scala
object Solution {
    def superPow(a: Int, b: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn super_pow(a: i32, b: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (super-pow a b)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec super_pow(A :: integer(), B :: [integer()]) -> integer().
super_pow(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec super_pow(a :: integer, b :: [integer]) :: integer
  def super_pow(a, b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func superPow(a: Int64, b: Array<Int64>): Int64 {

    }
}
```

