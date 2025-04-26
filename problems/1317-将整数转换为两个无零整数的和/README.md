# 1317. 将整数转换为两个无零整数的和

## 题目描述

<p>「无零整数」是十进制表示中 <strong>不含任何 0</strong>&nbsp;的正整数。</p>

<p>给你一个整数&nbsp;<code>n</code>，请你返回一个 <strong>由两个整数组成的列表</strong> <code>[a, b]</code>，满足：</p>

<ul>
	<li><code>a</code> 和 <code>b</code>&nbsp;都是无零整数</li>
	<li><code>a + b = n</code></li>
</ul>

<p>题目数据保证至少有一个有效的解决方案。</p>

<p>如果存在多个有效解决方案，你可以返回其中任意一个。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>[1,1]
<strong>解释：</strong>a = 1, b = 1。a + b = n 并且 a 和 b 的十进制表示形式都不包含任何 0。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 11
<strong>输出：</strong>[2,9]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 10000
<strong>输出：</strong>[1,9999]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>n = 69
<strong>输出：</strong>[1,68]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>n = 1010
<strong>输出：</strong>[11,999]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. Loop through all elements from 1 to n.
2. Choose A = i and B = n - i then check if A and B are both No-Zero integers.

## 示例

```
2
11
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] getNoZeroIntegers(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getNoZeroIntegers(int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] GetNoZeroIntegers(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var getNoZeroIntegers = function(n) {
    
};
```

### TypeScript

```typescript
function getNoZeroIntegers(n: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function getNoZeroIntegers($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getNoZeroIntegers(_ n: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getNoZeroIntegers(n: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getNoZeroIntegers(int n) {
    
  }
}
```

### Go

```golang
func getNoZeroIntegers(n int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer[]}
def get_no_zero_integers(n)
    
end
```

### Scala

```scala
object Solution {
    def getNoZeroIntegers(n: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_no_zero_integers(n: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-no-zero-integers n)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_no_zero_integers(N :: integer()) -> [integer()].
get_no_zero_integers(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_no_zero_integers(n :: integer) :: [integer]
  def get_no_zero_integers(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getNoZeroIntegers(n: Int64): Array<Int64> {

    }
}
```

