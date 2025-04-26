# 3242. 设计相邻元素求和服务

## 题目描述

<p>给你一个 <code>n x n</code> 的二维数组 <code>grid</code>，它包含范围 <code>[0, n<sup>2</sup> - 1]</code> 内的<strong>不重复</strong>元素。</p>

<p>实现 <code>neighborSum</code> 类：</p>

<ul>
	<li><code>neighborSum(int [][]grid)</code> 初始化对象。</li>
	<li><code>int adjacentSum(int value)</code> 返回在 <code>grid</code> 中与 <code>value</code> 相邻的元素之<strong>和</strong>，相邻指的是与 <code>value</code> 在上、左、右或下的元素。</li>
	<li><code>int diagonalSum(int value)</code> 返回在 <code>grid</code> 中与 <code>value</code> 对角线相邻的元素之<strong>和</strong>，对角线相邻指的是与 <code>value</code> 在左上、右上、左下或右下的元素。</li>
</ul>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/24/design.png" style="width: 400px; height: 248px;" /></p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong></p>

<p>["neighborSum", "adjacentSum", "adjacentSum", "diagonalSum", "diagonalSum"]</p>

<p>[[[[0, 1, 2], [3, 4, 5], [6, 7, 8]]], [1], [4], [4], [8]]</p>

<p><strong>输出：</strong> [null, 6, 16, 16, 4]</p>

<p><strong>解释：</strong></p>

<p><strong class="example"><img alt="" src="https://assets.leetcode.com/uploads/2024/06/24/designexample0.png" style="width: 250px; height: 249px;" /></strong></p>

<ul>
	<li>1 的相邻元素是 0、2 和 4。</li>
	<li>4 的相邻元素是 1、3、5 和 7。</li>
	<li>4 的对角线相邻元素是 0、2、6 和 8。</li>
	<li>8 的对角线相邻元素是 4。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong></p>

<p>["neighborSum", "adjacentSum", "diagonalSum"]</p>

<p>[[[[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]]], [15], [9]]</p>

<p><strong>输出：</strong> [null, 23, 45]</p>

<p><strong>解释：</strong></p>

<p><strong class="example"><img alt="" src="https://assets.leetcode.com/uploads/2024/06/24/designexample2.png" style="width: 300px; height: 300px;" /></strong></p>

<ul>
	<li>15 的相邻元素是 0、10、7 和 6。</li>
	<li>9 的对角线相邻元素是 4、12、14 和 15。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n == grid.length == grid[0].length &lt;= 10</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= n<sup>2</sup> - 1</code></li>
	<li>所有 <code>grid[i][j]</code> 值均不重复。</li>
	<li><code>adjacentSum</code> 和 <code>diagonalSum</code> 中的 <code>value</code> 均在范围 <code>[0, n<sup>2</sup> - 1]</code> 内。</li>
	<li>最多会调用 <code>adjacentSum</code> 和 <code>diagonalSum</code> 总共 <code>2 * n<sup>2</sup></code> 次。</li>
</ul>


## 难度

Easy

## 标签

- 设计
- 数组
- 哈希表
- 矩阵
- 模拟

## 提示

1. Find the cell <code>(i, j)</code> in which the element is present.
2. You can store the coordinates for each value.

## 示例

```
["NeighborSum","adjacentSum","adjacentSum","diagonalSum","diagonalSum"]
[[[[0,1,2],[3,4,5],[6,7,8]]],[1],[4],[4],[8]]
["NeighborSum","adjacentSum","diagonalSum"]
[[[[1,2,0,3],[4,7,15,6],[8,9,10,11],[12,13,14,5]]],[15],[9]]
```

## 示例代码

### C++

```cpp
class NeighborSum {
public:
    NeighborSum(vector<vector<int>>& grid) {
        
    }
    
    int adjacentSum(int value) {
        
    }
    
    int diagonalSum(int value) {
        
    }
};

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum* obj = new NeighborSum(grid);
 * int param_1 = obj->adjacentSum(value);
 * int param_2 = obj->diagonalSum(value);
 */
```

### Java

```java
class NeighborSum {

    public NeighborSum(int[][] grid) {
        
    }
    
    public int adjacentSum(int value) {
        
    }
    
    public int diagonalSum(int value) {
        
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum obj = new NeighborSum(grid);
 * int param_1 = obj.adjacentSum(value);
 * int param_2 = obj.diagonalSum(value);
 */
```

### Python

```python
class NeighborSum(object):

    def __init__(self, grid):
        """
        :type grid: List[List[int]]
        """
        

    def adjacentSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        

    def diagonalSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
```

### Python3

```python3
class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        

    def adjacentSum(self, value: int) -> int:
        

    def diagonalSum(self, value: int) -> int:
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
```

### C

```c



typedef struct {
    
} NeighborSum;


NeighborSum* neighborSumCreate(int** grid, int gridSize, int* gridColSize) {
    
}

int neighborSumAdjacentSum(NeighborSum* obj, int value) {
    
}

int neighborSumDiagonalSum(NeighborSum* obj, int value) {
    
}

void neighborSumFree(NeighborSum* obj) {
    
}

/**
 * Your NeighborSum struct will be instantiated and called as such:
 * NeighborSum* obj = neighborSumCreate(grid, gridSize, gridColSize);
 * int param_1 = neighborSumAdjacentSum(obj, value);
 
 * int param_2 = neighborSumDiagonalSum(obj, value);
 
 * neighborSumFree(obj);
*/
```

### C#

```csharp
public class NeighborSum {

    public NeighborSum(int[][] grid) {
        
    }
    
    public int AdjacentSum(int value) {
        
    }
    
    public int DiagonalSum(int value) {
        
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum obj = new NeighborSum(grid);
 * int param_1 = obj.AdjacentSum(value);
 * int param_2 = obj.DiagonalSum(value);
 */
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 */
var NeighborSum = function(grid) {
    
};

/** 
 * @param {number} value
 * @return {number}
 */
NeighborSum.prototype.adjacentSum = function(value) {
    
};

/** 
 * @param {number} value
 * @return {number}
 */
NeighborSum.prototype.diagonalSum = function(value) {
    
};

/** 
 * Your NeighborSum object will be instantiated and called as such:
 * var obj = new NeighborSum(grid)
 * var param_1 = obj.adjacentSum(value)
 * var param_2 = obj.diagonalSum(value)
 */
```

### TypeScript

```typescript
class NeighborSum {
    constructor(grid: number[][]) {
        
    }

    adjacentSum(value: number): number {
        
    }

    diagonalSum(value: number): number {
        
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * var obj = new NeighborSum(grid)
 * var param_1 = obj.adjacentSum(value)
 * var param_2 = obj.diagonalSum(value)
 */
```

### PHP

```php
class NeighborSum {
    /**
     * @param Integer[][] $grid
     */
    function __construct($grid) {
        
    }
  
    /**
     * @param Integer $value
     * @return Integer
     */
    function adjacentSum($value) {
        
    }
  
    /**
     * @param Integer $value
     * @return Integer
     */
    function diagonalSum($value) {
        
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * $obj = NeighborSum($grid);
 * $ret_1 = $obj->adjacentSum($value);
 * $ret_2 = $obj->diagonalSum($value);
 */
```

### Swift

```swift

class NeighborSum {

    init(_ grid: [[Int]]) {
        
    }
    
    func adjacentSum(_ value: Int) -> Int {
        
    }
    
    func diagonalSum(_ value: Int) -> Int {
        
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * let obj = NeighborSum(grid)
 * let ret_1: Int = obj.adjacentSum(value)
 * let ret_2: Int = obj.diagonalSum(value)
 */
```

### Kotlin

```kotlin
class NeighborSum(grid: Array<IntArray>) {

    fun adjacentSum(value: Int): Int {
        
    }

    fun diagonalSum(value: Int): Int {
        
    }

}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * var obj = NeighborSum(grid)
 * var param_1 = obj.adjacentSum(value)
 * var param_2 = obj.diagonalSum(value)
 */
```

### Dart

```dart
class NeighborSum {

  NeighborSum(List<List<int>> grid) {
    
  }
  
  int adjacentSum(int value) {
    
  }
  
  int diagonalSum(int value) {
    
  }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * NeighborSum obj = NeighborSum(grid);
 * int param1 = obj.adjacentSum(value);
 * int param2 = obj.diagonalSum(value);
 */
```

### Go

```golang
type NeighborSum struct {
    
}


func Constructor(grid [][]int) NeighborSum {
    
}


func (this *NeighborSum) AdjacentSum(value int) int {
    
}


func (this *NeighborSum) DiagonalSum(value int) int {
    
}


/**
 * Your NeighborSum object will be instantiated and called as such:
 * obj := Constructor(grid);
 * param_1 := obj.AdjacentSum(value);
 * param_2 := obj.DiagonalSum(value);
 */
```

### Ruby

```ruby
class NeighborSum

=begin
    :type grid: Integer[][]
=end
    def initialize(grid)
        
    end


=begin
    :type value: Integer
    :rtype: Integer
=end
    def adjacent_sum(value)
        
    end


=begin
    :type value: Integer
    :rtype: Integer
=end
    def diagonal_sum(value)
        
    end


end

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum.new(grid)
# param_1 = obj.adjacent_sum(value)
# param_2 = obj.diagonal_sum(value)
```

### Scala

```scala
class NeighborSum(_grid: Array[Array[Int]]) {

    def adjacentSum(value: Int): Int = {
        
    }

    def diagonalSum(value: Int): Int = {
        
    }

}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * val obj = new NeighborSum(grid)
 * val param_1 = obj.adjacentSum(value)
 * val param_2 = obj.diagonalSum(value)
 */
```

### Rust

```rust
struct NeighborSum {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NeighborSum {

    fn new(grid: Vec<Vec<i32>>) -> Self {
        
    }
    
    fn adjacent_sum(&self, value: i32) -> i32 {
        
    }
    
    fn diagonal_sum(&self, value: i32) -> i32 {
        
    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * let obj = NeighborSum::new(grid);
 * let ret_1: i32 = obj.adjacent_sum(value);
 * let ret_2: i32 = obj.diagonal_sum(value);
 */
```

### Racket

```racket
(define neighbor-sum%
  (class object%
    (super-new)
    
    ; grid : (listof (listof exact-integer?))
    (init-field
      grid)
    
    ; adjacent-sum : exact-integer? -> exact-integer?
    (define/public (adjacent-sum value)
      )
    ; diagonal-sum : exact-integer? -> exact-integer?
    (define/public (diagonal-sum value)
      )))

;; Your neighbor-sum% object will be instantiated and called as such:
;; (define obj (new neighbor-sum% [grid grid]))
;; (define param_1 (send obj adjacent-sum value))
;; (define param_2 (send obj diagonal-sum value))
```

### Erlang

```erlang
-spec neighbor_sum_init_(Grid :: [[integer()]]) -> any().
neighbor_sum_init_(Grid) ->
  .

-spec neighbor_sum_adjacent_sum(Value :: integer()) -> integer().
neighbor_sum_adjacent_sum(Value) ->
  .

-spec neighbor_sum_diagonal_sum(Value :: integer()) -> integer().
neighbor_sum_diagonal_sum(Value) ->
  .


%% Your functions will be called as such:
%% neighbor_sum_init_(Grid),
%% Param_1 = neighbor_sum_adjacent_sum(Value),
%% Param_2 = neighbor_sum_diagonal_sum(Value),

%% neighbor_sum_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule NeighborSum do
  @spec init_(grid :: [[integer]]) :: any
  def init_(grid) do
    
  end

  @spec adjacent_sum(value :: integer) :: integer
  def adjacent_sum(value) do
    
  end

  @spec diagonal_sum(value :: integer) :: integer
  def diagonal_sum(value) do
    
  end
end

# Your functions will be called as such:
# NeighborSum.init_(grid)
# param_1 = NeighborSum.adjacent_sum(value)
# param_2 = NeighborSum.diagonal_sum(value)

# NeighborSum.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class NeighborSum {
    init(grid: Array<Array<Int64>>) {

    }
    
    func adjacentSum(value: Int64): Int64 {

    }
    
    func diagonalSum(value: Int64): Int64 {

    }
}

/**
 * Your NeighborSum object will be instantiated and called as such:
 * let obj: NeighborSum = NeighborSum(grid)
 * let param_1 = obj.adjacentSum(value)
 * let param_2 = obj.diagonalSum(value)
 */
```

