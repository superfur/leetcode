# 970. 强整数

## 题目描述

<p>给定三个整数 <code>x</code>&nbsp;、&nbsp;<code>y</code>&nbsp;和<em>&nbsp;</em><code>bound</code><em>&nbsp;</em>，返回 <em>值小于或等于&nbsp;<code>bound</code>&nbsp;的所有&nbsp;<strong>强整数</strong>&nbsp;组成的列表</em>&nbsp;。</p>

<p>如果某一整数可以表示为&nbsp;<code>x<sup>i</sup>&nbsp;+ y<sup>j</sup></code>&nbsp;，其中整数&nbsp;<code>i &gt;= 0</code> 且&nbsp;<code>j &gt;= 0</code>，那么我们认为该整数是一个&nbsp;<strong>强整数</strong>&nbsp;。</p>

<p>你可以按 <strong>任何顺序</strong> 返回答案。在你的回答中，每个值 <strong>最多</strong> 出现一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>x = 2, y = 3, bound = 10
<strong>输出：</strong>[2,3,4,5,7,9,10]
<strong>解释： </strong>
2 = 2<sup>0</sup> + 3<sup>0</sup>
3 = 2<sup>1</sup> + 3<sup>0</sup>
4 = 2<sup>0</sup> + 3<sup>1</sup>
5 = 2<sup>1</sup> + 3<sup>1</sup>
7 = 2<sup>2</sup> + 3<sup>1</sup>
9 = 2<sup>3</sup> + 3<sup>0</sup>
10 = 2<sup>0</sup> + 3<sup>2</sup></pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>x = 3, y = 5, bound = 15
<strong>输出：</strong>[2,4,6,8,10,14]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= x, y &lt;= 100</code></li>
	<li><code>0 &lt;= bound &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 数学
- 枚举

## 示例

```
2
3
10
3
5
15
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> powerfulIntegers(int x, int y, int bound) {
        
    }
}
```

### Python

```python
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* powerfulIntegers(int x, int y, int bound, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> PowerfulIntegers(int x, int y, int bound) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @param {number} bound
 * @return {number[]}
 */
var powerfulIntegers = function(x, y, bound) {
    
};
```

### TypeScript

```typescript
function powerfulIntegers(x: number, y: number, bound: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @param Integer $bound
     * @return Integer[]
     */
    function powerfulIntegers($x, $y, $bound) {
        
    }
}
```

### Swift

```swift
class Solution {
    func powerfulIntegers(_ x: Int, _ y: Int, _ bound: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun powerfulIntegers(x: Int, y: Int, bound: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> powerfulIntegers(int x, int y, int bound) {
    
  }
}
```

### Go

```golang
func powerfulIntegers(x int, y int, bound int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} x
# @param {Integer} y
# @param {Integer} bound
# @return {Integer[]}
def powerful_integers(x, y, bound)
    
end
```

### Scala

```scala
object Solution {
    def powerfulIntegers(x: Int, y: Int, bound: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn powerful_integers(x: i32, y: i32, bound: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (powerful-integers x y bound)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec powerful_integers(X :: integer(), Y :: integer(), Bound :: integer()) -> [integer()].
powerful_integers(X, Y, Bound) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec powerful_integers(x :: integer, y :: integer, bound :: integer) :: [integer]
  def powerful_integers(x, y, bound) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func powerfulIntegers(x: Int64, y: Int64, bound: Int64): ArrayList<Int64> {

    }
}
```

