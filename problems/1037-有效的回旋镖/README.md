# 1037. 有效的回旋镖

## 题目描述

<p>给定一个数组<meta charset="UTF-8" />&nbsp;<code>points</code>&nbsp;，其中<meta charset="UTF-8" />&nbsp;<code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;表示 <strong>X-Y</strong> 平面上的一个点，<em>如果这些点构成一个&nbsp;</em><strong>回旋镖</strong>&nbsp;则返回&nbsp;<code>true</code>&nbsp;。</p>

<p><strong>回旋镖</strong>&nbsp;定义为一组三个点，这些点&nbsp;<strong>各不相同</strong>&nbsp;且&nbsp;<strong>不在一条直线上</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>points = [[1,1],[2,3],[3,2]]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>points = [[1,1],[2,2],[3,3]]
<strong>输出：</strong>false</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>
<meta charset="UTF-8" />

<ul>
	<li><code>points.length == 3</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub>&nbsp;&lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 几何
- 数组
- 数学

## 提示

1. 3 points form a boomerang if and only if the triangle formed from them has non-zero area.

## 示例

```
[[1,1],[2,3],[3,2]]
[[1,1],[2,2],[3,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isBoomerang(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isBoomerang(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
```

### C

```c
bool isBoomerang(int** points, int pointsSize, int* pointsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsBoomerang(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {boolean}
 */
var isBoomerang = function(points) {
    
};
```

### TypeScript

```typescript
function isBoomerang(points: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Boolean
     */
    function isBoomerang($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isBoomerang(_ points: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isBoomerang(points: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isBoomerang(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func isBoomerang(points [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Boolean}
def is_boomerang(points)
    
end
```

### Scala

```scala
object Solution {
    def isBoomerang(points: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_boomerang(points: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-boomerang points)
  (-> (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec is_boomerang(Points :: [[integer()]]) -> boolean().
is_boomerang(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_boomerang(points :: [[integer]]) :: boolean
  def is_boomerang(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isBoomerang(points: Array<Array<Int64>>): Bool {

    }
}
```

