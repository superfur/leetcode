# LCR 013. 二维区域和检索 - 矩阵不可变

## 题目描述

<p><big><small>给定一个二维矩阵 <code>matrix</code>，</small></big>以下类型的多个请求：</p>

<ul>
	<li><big><small>计算其子矩形范围内元素的总和，该子矩阵的左上角为 <code>(row1,&nbsp;col1)</code> ，右下角为 <code>(row2,&nbsp;col2)</code> 。</small></big></li>
</ul>

<p>实现 <code>NumMatrix</code> 类：</p>

<ul>
	<li><code>NumMatrix(int[][] matrix)</code>&nbsp;给定整数矩阵 <code>matrix</code> 进行初始化</li>
	<li><code>int sumRegion(int row1, int col1, int row2, int col2)</code>&nbsp;返回<big><small>左上角</small></big><big><small> <code>(row1,&nbsp;col1)</code>&nbsp;、右下角&nbsp;<code>(row2,&nbsp;col2)</code></small></big>&nbsp;的子矩阵的元素总和。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://pic.leetcode-cn.com/1626332422-wUpUHT-image.png" style="width: 200px;" /></p>

<pre>
<strong>输入:</strong> 
[&quot;NumMatrix&quot;,&quot;sumRegion&quot;,&quot;sumRegion&quot;,&quot;sumRegion&quot;]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
<strong>输出:</strong> 
[null, 8, 11, 12]

<strong>解释:</strong>
NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m,&nbsp;n &lt;=&nbsp;200</code><meta charset="UTF-8" /></li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= matrix[i][j] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= row1 &lt;= row2 &lt; m</code></li>
	<li><code>0 &lt;= col1 &lt;= col2 &lt; n</code></li>
	<li><meta charset="UTF-8" />最多调用 <code>10<sup>4</sup></code> 次&nbsp;<code>sumRegion</code> 方法</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 304&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/range-sum-query-2d-immutable/">https://leetcode-cn.com/problems/range-sum-query-2d-immutable/</a></p>


## 难度

Medium

## 标签

- 设计
- 数组
- 矩阵
- 前缀和

## 示例

```
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
```

## 示例代码

### C++

```cpp
class NumMatrix {
public:
    NumMatrix(vector<vector<int>>& matrix) {
        
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
```

### Java

```java
class NumMatrix {

    public NumMatrix(int[][] matrix) {
        
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
```

### Python

```python
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```

### Python3

```python3
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```

### C

```c



typedef struct {
    
} NumMatrix;


NumMatrix* numMatrixCreate(int** matrix, int matrixSize, int* matrixColSize) {
    
}

int numMatrixSumRegion(NumMatrix* obj, int row1, int col1, int row2, int col2) {
    
}

void numMatrixFree(NumMatrix* obj) {
    
}

/**
 * Your NumMatrix struct will be instantiated and called as such:
 * NumMatrix* obj = numMatrixCreate(matrix, matrixSize, matrixColSize);
 * int param_1 = numMatrixSumRegion(obj, row1, col1, row2, col2);
 
 * numMatrixFree(obj);
*/
```

### C#

```csharp
public class NumMatrix {

    public NumMatrix(int[][] matrix) {
        
    }
    
    public int SumRegion(int row1, int col1, int row2, int col2) {
        
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.SumRegion(row1,col1,row2,col2);
 */
```

### JavaScript

```javascript
/**
 * @param {number[][]} matrix
 */
var NumMatrix = function(matrix) {
    
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
    
};

/** 
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
```

### TypeScript

```typescript
class NumMatrix {
    constructor(matrix: number[][]) {
        
    }

    sumRegion(row1: number, col1: number, row2: number, col2: number): number {
        
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
```

### PHP

```php
class NumMatrix {
    /**
     * @param Integer[][] $matrix
     */
    function __construct($matrix) {
        
    }
  
    /**
     * @param Integer $row1
     * @param Integer $col1
     * @param Integer $row2
     * @param Integer $col2
     * @return Integer
     */
    function sumRegion($row1, $col1, $row2, $col2) {
        
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * $obj = NumMatrix($matrix);
 * $ret_1 = $obj->sumRegion($row1, $col1, $row2, $col2);
 */
```

### Swift

```swift

class NumMatrix {

    init(_ matrix: [[Int]]) {
        
    }
    
    func sumRegion(_ row1: Int, _ col1: Int, _ row2: Int, _ col2: Int) -> Int {
        
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * let obj = NumMatrix(matrix)
 * let ret_1: Int = obj.sumRegion(row1, col1, row2, col2)
 */
```

### Kotlin

```kotlin
class NumMatrix(matrix: Array<IntArray>) {

    fun sumRegion(row1: Int, col1: Int, row2: Int, col2: Int): Int {
        
    }

}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
```

### Dart

```dart
class NumMatrix {

  NumMatrix(List<List<int>> matrix) {
    
  }
  
  int sumRegion(int row1, int col1, int row2, int col2) {
    
  }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = NumMatrix(matrix);
 * int param1 = obj.sumRegion(row1,col1,row2,col2);
 */
```

### Go

```golang
type NumMatrix struct {
    
}


func Constructor(matrix [][]int) NumMatrix {
    
}


func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    
}


/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */
```

### Ruby

```ruby
class NumMatrix

=begin
    :type matrix: Integer[][]
=end
    def initialize(matrix)
        
    end


=begin
    :type row1: Integer
    :type col1: Integer
    :type row2: Integer
    :type col2: Integer
    :rtype: Integer
=end
    def sum_region(row1, col1, row2, col2)
        
    end


end

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix.new(matrix)
# param_1 = obj.sum_region(row1, col1, row2, col2)
```

### Scala

```scala
class NumMatrix(_matrix: Array[Array[Int]]) {

    def sumRegion(row1: Int, col1: Int, row2: Int, col2: Int): Int = {
        
    }

}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * val obj = new NumMatrix(matrix)
 * val param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
```

### Rust

```rust
struct NumMatrix {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumMatrix {

    fn new(matrix: Vec<Vec<i32>>) -> Self {
        
    }
    
    fn sum_region(&self, row1: i32, col1: i32, row2: i32, col2: i32) -> i32 {
        
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * let obj = NumMatrix::new(matrix);
 * let ret_1: i32 = obj.sum_region(row1, col1, row2, col2);
 */
```

### Racket

```racket
(define num-matrix%
  (class object%
    (super-new)
    
    ; matrix : (listof (listof exact-integer?))
    (init-field
      matrix)
    
    ; sum-region : exact-integer? exact-integer? exact-integer? exact-integer? -> exact-integer?
    (define/public (sum-region row1 col1 row2 col2)
      )))

;; Your num-matrix% object will be instantiated and called as such:
;; (define obj (new num-matrix% [matrix matrix]))
;; (define param_1 (send obj sum-region row1 col1 row2 col2))
```

### Erlang

```erlang
-spec num_matrix_init_(Matrix :: [[integer()]]) -> any().
num_matrix_init_(Matrix) ->
  .

-spec num_matrix_sum_region(Row1 :: integer(), Col1 :: integer(), Row2 :: integer(), Col2 :: integer()) -> integer().
num_matrix_sum_region(Row1, Col1, Row2, Col2) ->
  .


%% Your functions will be called as such:
%% num_matrix_init_(Matrix),
%% Param_1 = num_matrix_sum_region(Row1, Col1, Row2, Col2),

%% num_matrix_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule NumMatrix do
  @spec init_(matrix :: [[integer]]) :: any
  def init_(matrix) do
    
  end

  @spec sum_region(row1 :: integer, col1 :: integer, row2 :: integer, col2 :: integer) :: integer
  def sum_region(row1, col1, row2, col2) do
    
  end
end

# Your functions will be called as such:
# NumMatrix.init_(matrix)
# param_1 = NumMatrix.sum_region(row1, col1, row2, col2)

# NumMatrix.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class NumMatrix {
    init(matrix: Array<Array<Int64>>) {

    }
    
    func sumRegion(row1: Int64, col1: Int64, row2: Int64, col2: Int64): Int64 {

    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * let obj: NumMatrix = NumMatrix(matrix)
 * let param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
```

