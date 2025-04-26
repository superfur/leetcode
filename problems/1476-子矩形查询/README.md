# 1476. 子矩形查询

## 题目描述

<p>请你实现一个类&nbsp;<code>SubrectangleQueries</code>&nbsp;，它的构造函数的参数是一个 <code>rows x cols</code>&nbsp;的矩形（这里用整数矩阵表示），并支持以下两种操作：</p>

<p>1.<code>&nbsp;updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)</code></p>

<ul>
	<li>用&nbsp;<code>newValue</code>&nbsp;更新以&nbsp;<code>(row1,col1)</code>&nbsp;为左上角且以&nbsp;<code>(row2,col2)</code>&nbsp;为右下角的子矩形。</li>
</ul>

<p>2.<code>&nbsp;getValue(int row, int col)</code></p>

<ul>
	<li>返回矩形中坐标 <code>(row,col)</code> 的当前值。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>
[&quot;SubrectangleQueries&quot;,&quot;getValue&quot;,&quot;updateSubrectangle&quot;,&quot;getValue&quot;,&quot;getValue&quot;,&quot;updateSubrectangle&quot;,&quot;getValue&quot;,&quot;getValue&quot;]
[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
<strong>输出：</strong>
[null,1,null,5,5,null,10,5]
<strong>解释：</strong>
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]);  
// 初始的 (4x3) 矩形如下：
// 1 2 1
// 4 3 4
// 3 2 1
// 1 1 1
subrectangleQueries.getValue(0, 2); // 返回 1
subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
// 此次更新后矩形变为：
// 5 5 5
// 5 5 5
// 5 5 5
// 5 5 5 
subrectangleQueries.getValue(0, 2); // 返回 5
subrectangleQueries.getValue(3, 1); // 返回 5
subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
// 此次更新后矩形变为：
// 5   5   5
// 5   5   5
// 5   5   5
// 10  10  10 
subrectangleQueries.getValue(3, 1); // 返回 10
subrectangleQueries.getValue(0, 2); // 返回 5
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>
[&quot;SubrectangleQueries&quot;,&quot;getValue&quot;,&quot;updateSubrectangle&quot;,&quot;getValue&quot;,&quot;getValue&quot;,&quot;updateSubrectangle&quot;,&quot;getValue&quot;]
[[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
<strong>输出：</strong>
[null,1,null,100,100,null,20]
<strong>解释：</strong>
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]]);
subrectangleQueries.getValue(0, 0); // 返回 1
subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100);
subrectangleQueries.getValue(0, 0); // 返回 100
subrectangleQueries.getValue(2, 2); // 返回 100
subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20);
subrectangleQueries.getValue(2, 2); // 返回 20
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>最多有&nbsp;<code>500</code>&nbsp;次<code>updateSubrectangle</code> 和&nbsp;<code>getValue</code>&nbsp;操作。</li>
	<li><code>1 &lt;= rows, cols &lt;= 100</code></li>
	<li><code>rows ==&nbsp;rectangle.length</code></li>
	<li><code>cols == rectangle[i].length</code></li>
	<li><code>0 &lt;= row1 &lt;= row2 &lt; rows</code></li>
	<li><code>0 &lt;= col1 &lt;= col2 &lt; cols</code></li>
	<li><code>1 &lt;= newValue, rectangle[i][j] &lt;= 10^9</code></li>
	<li><code>0 &lt;= row &lt; rows</code></li>
	<li><code>0 &lt;= col &lt; cols</code></li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 矩阵

## 提示

1. Use brute force to update a rectangle and, response to the queries in O(1).

## 示例

```
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
[[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
```

## 示例代码

### C++

```cpp
class SubrectangleQueries {
public:
    SubrectangleQueries(vector<vector<int>>& rectangle) {
        
    }
    
    void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        
    }
    
    int getValue(int row, int col) {
        
    }
};

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries* obj = new SubrectangleQueries(rectangle);
 * obj->updateSubrectangle(row1,col1,row2,col2,newValue);
 * int param_2 = obj->getValue(row,col);
 */
```

### Java

```java
class SubrectangleQueries {

    public SubrectangleQueries(int[][] rectangle) {
        
    }
    
    public void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        
    }
    
    public int getValue(int row, int col) {
        
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries obj = new SubrectangleQueries(rectangle);
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue);
 * int param_2 = obj.getValue(row,col);
 */
```

### Python

```python
class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
```

### Python3

```python3
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        

    def getValue(self, row: int, col: int) -> int:
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
```

### C

```c



typedef struct {
    
} SubrectangleQueries;


SubrectangleQueries* subrectangleQueriesCreate(int** rectangle, int rectangleSize, int* rectangleColSize) {
    
}

void subrectangleQueriesUpdateSubrectangle(SubrectangleQueries* obj, int row1, int col1, int row2, int col2, int newValue) {
    
}

int subrectangleQueriesGetValue(SubrectangleQueries* obj, int row, int col) {
    
}

void subrectangleQueriesFree(SubrectangleQueries* obj) {
    
}

/**
 * Your SubrectangleQueries struct will be instantiated and called as such:
 * SubrectangleQueries* obj = subrectangleQueriesCreate(rectangle, rectangleSize, rectangleColSize);
 * subrectangleQueriesUpdateSubrectangle(obj, row1, col1, row2, col2, newValue);
 
 * int param_2 = subrectangleQueriesGetValue(obj, row, col);
 
 * subrectangleQueriesFree(obj);
*/
```

### C#

```csharp
public class SubrectangleQueries {

    public SubrectangleQueries(int[][] rectangle) {
        
    }
    
    public void UpdateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        
    }
    
    public int GetValue(int row, int col) {
        
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries obj = new SubrectangleQueries(rectangle);
 * obj.UpdateSubrectangle(row1,col1,row2,col2,newValue);
 * int param_2 = obj.GetValue(row,col);
 */
```

### JavaScript

```javascript
/**
 * @param {number[][]} rectangle
 */
var SubrectangleQueries = function(rectangle) {
    
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2 
 * @param {number} newValue
 * @return {void}
 */
SubrectangleQueries.prototype.updateSubrectangle = function(row1, col1, row2, col2, newValue) {
    
};

/** 
 * @param {number} row 
 * @param {number} col
 * @return {number}
 */
SubrectangleQueries.prototype.getValue = function(row, col) {
    
};

/** 
 * Your SubrectangleQueries object will be instantiated and called as such:
 * var obj = new SubrectangleQueries(rectangle)
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue)
 * var param_2 = obj.getValue(row,col)
 */
```

### TypeScript

```typescript
class SubrectangleQueries {
    constructor(rectangle: number[][]) {
        
    }

    updateSubrectangle(row1: number, col1: number, row2: number, col2: number, newValue: number): void {
        
    }

    getValue(row: number, col: number): number {
        
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * var obj = new SubrectangleQueries(rectangle)
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue)
 * var param_2 = obj.getValue(row,col)
 */
```

### PHP

```php
class SubrectangleQueries {
    /**
     * @param Integer[][] $rectangle
     */
    function __construct($rectangle) {
        
    }
  
    /**
     * @param Integer $row1
     * @param Integer $col1
     * @param Integer $row2
     * @param Integer $col2
     * @param Integer $newValue
     * @return NULL
     */
    function updateSubrectangle($row1, $col1, $row2, $col2, $newValue) {
        
    }
  
    /**
     * @param Integer $row
     * @param Integer $col
     * @return Integer
     */
    function getValue($row, $col) {
        
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * $obj = SubrectangleQueries($rectangle);
 * $obj->updateSubrectangle($row1, $col1, $row2, $col2, $newValue);
 * $ret_2 = $obj->getValue($row, $col);
 */
```

### Swift

```swift

class SubrectangleQueries {

    init(_ rectangle: [[Int]]) {
        
    }
    
    func updateSubrectangle(_ row1: Int, _ col1: Int, _ row2: Int, _ col2: Int, _ newValue: Int) {
        
    }
    
    func getValue(_ row: Int, _ col: Int) -> Int {
        
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * let obj = SubrectangleQueries(rectangle)
 * obj.updateSubrectangle(row1, col1, row2, col2, newValue)
 * let ret_2: Int = obj.getValue(row, col)
 */
```

### Kotlin

```kotlin
class SubrectangleQueries(rectangle: Array<IntArray>) {

    fun updateSubrectangle(row1: Int, col1: Int, row2: Int, col2: Int, newValue: Int) {
        
    }

    fun getValue(row: Int, col: Int): Int {
        
    }

}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * var obj = SubrectangleQueries(rectangle)
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue)
 * var param_2 = obj.getValue(row,col)
 */
```

### Dart

```dart
class SubrectangleQueries {

  SubrectangleQueries(List<List<int>> rectangle) {
    
  }
  
  void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
    
  }
  
  int getValue(int row, int col) {
    
  }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries obj = SubrectangleQueries(rectangle);
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue);
 * int param2 = obj.getValue(row,col);
 */
```

### Go

```golang
type SubrectangleQueries struct {
    
}


func Constructor(rectangle [][]int) SubrectangleQueries {
    
}


func (this *SubrectangleQueries) UpdateSubrectangle(row1 int, col1 int, row2 int, col2 int, newValue int)  {
    
}


func (this *SubrectangleQueries) GetValue(row int, col int) int {
    
}


/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * obj := Constructor(rectangle);
 * obj.UpdateSubrectangle(row1,col1,row2,col2,newValue);
 * param_2 := obj.GetValue(row,col);
 */
```

### Ruby

```ruby
class SubrectangleQueries

=begin
    :type rectangle: Integer[][]
=end
    def initialize(rectangle)
        
    end


=begin
    :type row1: Integer
    :type col1: Integer
    :type row2: Integer
    :type col2: Integer
    :type new_value: Integer
    :rtype: Void
=end
    def update_subrectangle(row1, col1, row2, col2, new_value)
        
    end


=begin
    :type row: Integer
    :type col: Integer
    :rtype: Integer
=end
    def get_value(row, col)
        
    end


end

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries.new(rectangle)
# obj.update_subrectangle(row1, col1, row2, col2, new_value)
# param_2 = obj.get_value(row, col)
```

### Scala

```scala
class SubrectangleQueries(_rectangle: Array[Array[Int]]) {

    def updateSubrectangle(row1: Int, col1: Int, row2: Int, col2: Int, newValue: Int): Unit = {
        
    }

    def getValue(row: Int, col: Int): Int = {
        
    }

}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * val obj = new SubrectangleQueries(rectangle)
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue)
 * val param_2 = obj.getValue(row,col)
 */
```

### Rust

```rust
struct SubrectangleQueries {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SubrectangleQueries {

    fn new(rectangle: Vec<Vec<i32>>) -> Self {
        
    }
    
    fn update_subrectangle(&self, row1: i32, col1: i32, row2: i32, col2: i32, new_value: i32) {
        
    }
    
    fn get_value(&self, row: i32, col: i32) -> i32 {
        
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * let obj = SubrectangleQueries::new(rectangle);
 * obj.update_subrectangle(row1, col1, row2, col2, newValue);
 * let ret_2: i32 = obj.get_value(row, col);
 */
```

### Racket

```racket
(define subrectangle-queries%
  (class object%
    (super-new)
    
    ; rectangle : (listof (listof exact-integer?))
    (init-field
      rectangle)
    
    ; update-subrectangle : exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? -> void?
    (define/public (update-subrectangle row1 col1 row2 col2 new-value)
      )
    ; get-value : exact-integer? exact-integer? -> exact-integer?
    (define/public (get-value row col)
      )))

;; Your subrectangle-queries% object will be instantiated and called as such:
;; (define obj (new subrectangle-queries% [rectangle rectangle]))
;; (send obj update-subrectangle row1 col1 row2 col2 new-value)
;; (define param_2 (send obj get-value row col))
```

### Erlang

```erlang
-spec subrectangle_queries_init_(Rectangle :: [[integer()]]) -> any().
subrectangle_queries_init_(Rectangle) ->
  .

-spec subrectangle_queries_update_subrectangle(Row1 :: integer(), Col1 :: integer(), Row2 :: integer(), Col2 :: integer(), NewValue :: integer()) -> any().
subrectangle_queries_update_subrectangle(Row1, Col1, Row2, Col2, NewValue) ->
  .

-spec subrectangle_queries_get_value(Row :: integer(), Col :: integer()) -> integer().
subrectangle_queries_get_value(Row, Col) ->
  .


%% Your functions will be called as such:
%% subrectangle_queries_init_(Rectangle),
%% subrectangle_queries_update_subrectangle(Row1, Col1, Row2, Col2, NewValue),
%% Param_2 = subrectangle_queries_get_value(Row, Col),

%% subrectangle_queries_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule SubrectangleQueries do
  @spec init_(rectangle :: [[integer]]) :: any
  def init_(rectangle) do
    
  end

  @spec update_subrectangle(row1 :: integer, col1 :: integer, row2 :: integer, col2 :: integer, new_value :: integer) :: any
  def update_subrectangle(row1, col1, row2, col2, new_value) do
    
  end

  @spec get_value(row :: integer, col :: integer) :: integer
  def get_value(row, col) do
    
  end
end

# Your functions will be called as such:
# SubrectangleQueries.init_(rectangle)
# SubrectangleQueries.update_subrectangle(row1, col1, row2, col2, new_value)
# param_2 = SubrectangleQueries.get_value(row, col)

# SubrectangleQueries.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class SubrectangleQueries {
    init(rectangle: Array<Array<Int64>>) {

    }
    
    func updateSubrectangle(row1: Int64, col1: Int64, row2: Int64, col2: Int64, newValue: Int64): Unit {

    }
    
    func getValue(row: Int64, col: Int64): Int64 {

    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * let obj: SubrectangleQueries = SubrectangleQueries(rectangle)
 * obj.updateSubrectangle(row1,col1,row2,col2,newValue)
 * let param_2 = obj.getValue(row,col)
 */
```

