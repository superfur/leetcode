# 593. 有效的正方形

## 题目描述

<p>给定2D空间中四个点的坐标&nbsp;<code>p1</code>,&nbsp;<code>p2</code>,&nbsp;<code>p3</code>&nbsp;和&nbsp;<code>p4</code>，如果这四个点构成一个正方形，则返回 <code>true</code> 。</p>

<p>点的坐标&nbsp;<code>p<sub>i</sub></code> 表示为 <code>[xi, yi]</code> 。 <code>输入没有任何顺序</code> 。</p>

<p>一个 <strong>有效的正方形</strong> 有四条等边和四个等角(90度角)。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
<strong>输出:</strong> true
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入：</strong>p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
<b>输出：</b>false
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<b>输入：</b>p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
<b>输出：</b>true
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>p1.length == p2.length == p3.length == p4.length == 2</code></li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= x<sub>i</sub>, y<sub>i</sub>&nbsp;&lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 几何
- 数学

## 示例

```
[0,0]
[1,1]
[1,0]
[0,1]
[0,0]
[1,1]
[1,0]
[0,12]
[1,0]
[-1,0]
[0,1]
[0,-1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
```

### C

```c
bool validSquare(int* p1, int p1Size, int* p2, int p2Size, int* p3, int p3Size, int* p4, int p4Size) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ValidSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} p1
 * @param {number[]} p2
 * @param {number[]} p3
 * @param {number[]} p4
 * @return {boolean}
 */
var validSquare = function(p1, p2, p3, p4) {
    
};
```

### TypeScript

```typescript
function validSquare(p1: number[], p2: number[], p3: number[], p4: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $p1
     * @param Integer[] $p2
     * @param Integer[] $p3
     * @param Integer[] $p4
     * @return Boolean
     */
    function validSquare($p1, $p2, $p3, $p4) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validSquare(_ p1: [Int], _ p2: [Int], _ p3: [Int], _ p4: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validSquare(p1: IntArray, p2: IntArray, p3: IntArray, p4: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool validSquare(List<int> p1, List<int> p2, List<int> p3, List<int> p4) {
    
  }
}
```

### Go

```golang
func validSquare(p1 []int, p2 []int, p3 []int, p4 []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} p1
# @param {Integer[]} p2
# @param {Integer[]} p3
# @param {Integer[]} p4
# @return {Boolean}
def valid_square(p1, p2, p3, p4)
    
end
```

### Scala

```scala
object Solution {
    def validSquare(p1: Array[Int], p2: Array[Int], p3: Array[Int], p4: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn valid_square(p1: Vec<i32>, p2: Vec<i32>, p3: Vec<i32>, p4: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (valid-square p1 p2 p3 p4)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec valid_square(P1 :: [integer()], P2 :: [integer()], P3 :: [integer()], P4 :: [integer()]) -> boolean().
valid_square(P1, P2, P3, P4) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec valid_square(p1 :: [integer], p2 :: [integer], p3 :: [integer], p4 :: [integer]) :: boolean
  def valid_square(p1, p2, p3, p4) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validSquare(p1: Array<Int64>, p2: Array<Int64>, p3: Array<Int64>, p4: Array<Int64>): Bool {

    }
}
```

