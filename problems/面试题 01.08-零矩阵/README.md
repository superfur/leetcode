# 面试题 01.08. 零矩阵

## 题目描述

<p>编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
<strong>输出：</strong>
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
<strong>输出：</strong>
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
</pre>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 矩阵

## 提示

1. 如果你在找到0时清除了行和列，则可能会清理整个矩阵。在对矩阵进行任何更改之前，首先尝试找到所有的0。
2. 你能只用额外的O(N)空间而不是O(N2)吗？在为0的单元格列表中你真正需要的是什么信息？
3. 你可能需要一些数据存储来维护一个需要清零的行与列的列表。通过使用矩阵本身来存储数据，你是否可以把额外的空间占用减小到O(1)？

## 示例

```
[[1,1,1],[1,0,1],[1,1,1]]
[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public void setZeroes(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
```

### Python3

```python3
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
```

### C

```c
void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public void SetZeroes(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    
};
```

### TypeScript

```typescript
/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return NULL
     */
    function setZeroes(&$matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func setZeroes(_ matrix: inout [[Int]]) {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun setZeroes(matrix: Array<IntArray>): Unit {
        
    }
}
```

### Dart

```dart
class Solution {
  void setZeroes(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func setZeroes(matrix [][]int)  {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Void} Do not return anything, modify matrix in-place instead.
def set_zeroes(matrix)
    
end
```

### Scala

```scala
object Solution {
    def setZeroes(matrix: Array[Array[Int]]): Unit = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        
    }
}
```

### Cangjie

```cangjie
class Solution {
    func setZeroes(matrix: Array<Array<Int64>>): Unit {

    }
}
```

