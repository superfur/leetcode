# 119. 杨辉三角 II

## 题目描述

<p>给定一个非负索引 <code>rowIndex</code>，返回「杨辉三角」的第 <code>rowIndex</code><em> </em>行。</p>

<p><small>在「杨辉三角」中，每个数是它左上方和右上方的数的和。</small></p>

<p><img alt="" src="https://pic.leetcode-cn.com/1626927345-DZmfxB-PascalTriangleAnimated2.gif" /></p>

<p> </p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> rowIndex = 3
<strong>输出:</strong> [1,3,3,1]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> rowIndex = 0
<strong>输出:</strong> [1]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> rowIndex = 1
<strong>输出:</strong> [1,1]
</pre>

<p> </p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>0 <= rowIndex <= 33</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong></p>

<p>你可以优化你的算法到 <code><em>O</em>(<i>rowIndex</i>)</code> 空间复杂度吗？</p>


## 难度

Easy

## 标签

- 数组
- 动态规划

## 示例

```
3
0
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> getRow(int rowIndex) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getRow(int rowIndex, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> GetRow(int rowIndex) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    
};
```

### TypeScript

```typescript
function getRow(rowIndex: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $rowIndex
     * @return Integer[]
     */
    function getRow($rowIndex) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getRow(_ rowIndex: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getRow(rowIndex: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getRow(int rowIndex) {
    
  }
}
```

### Go

```golang
func getRow(rowIndex int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} row_index
# @return {Integer[]}
def get_row(row_index)
    
end
```

### Scala

```scala
object Solution {
    def getRow(rowIndex: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-row rowIndex)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_row(RowIndex :: integer()) -> [integer()].
get_row(RowIndex) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_row(row_index :: integer) :: [integer]
  def get_row(row_index) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getRow(rowIndex: Int64): ArrayList<Int64> {

    }
}
```

