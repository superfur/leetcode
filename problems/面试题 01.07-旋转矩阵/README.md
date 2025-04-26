# 面试题 01.07. 旋转矩阵

## 题目描述

<p>给你一幅由 <code>N × N</code> 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。</p>

<p>不占用额外内存空间能否做到？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
给定 <strong>matrix</strong> = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

<strong>原地</strong>旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
给定 <strong>matrix</strong> =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

<strong>原地</strong>旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
</pre>

<p><strong>注意</strong>：本题与主站 48&nbsp;题相同：<a href="https://leetcode-cn.com/problems/rotate-image/">https://leetcode-cn.com/problems/rotate-image/</a></p>


## 难度

Medium

## 标签

- 数组
- 数学
- 矩阵

## 提示

1. 尝试逐层思考。你能旋转某个特定图层吗？
2. 旋转一个特定的层只意味着在4个数组中交换值。如果要求你在2个数组中交换值，你能做到吗？你能把它扩展到4个数组吗？

## 示例

```
[[1,2,3],[4,5,6],[7,8,9]]
[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        
    }
};
```

### Java

```java
class Solution {
    public void rotate(int[][] matrix) {
        
    }
}
```

### Python

```python
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
```

### Python3

```python3
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
```

### C

```c
void rotate(int** matrix, int matrixSize, int* matrixColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public void Rotate(int[][] matrix) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    
};
```

### TypeScript

```typescript
/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return NULL
     */
    function rotate(&$matrix) {
        
    }
}
```

### Swift

```swift
class Solution {
    func rotate(_ matrix: inout [[Int]]) {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rotate(matrix: Array<IntArray>): Unit {
        
    }
}
```

### Dart

```dart
class Solution {
  void rotate(List<List<int>> matrix) {
    
  }
}
```

### Go

```golang
func rotate(matrix [][]int)  {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} matrix
# @return {Void} Do not return anything, modify matrix in-place instead.
def rotate(matrix)
    
end
```

### Scala

```scala
object Solution {
    def rotate(matrix: Array[Array[Int]]): Unit = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        
    }
}
```

### Cangjie

```cangjie
class Solution {
    func rotate(matrix: Array<Array<Int64>>): Unit {

    }
}
```

