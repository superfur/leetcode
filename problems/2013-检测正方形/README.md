# 2013. 检测正方形

## 题目描述

<p>给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法：</p>

<ul>
	<li><strong>添加</strong> 一个在数据流中的新点到某个数据结构中<strong>。</strong>可以添加 <strong>重复</strong> 的点，并会视作不同的点进行处理。</li>
	<li>给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 <strong>面积为正</strong> 的 <strong>轴对齐正方形</strong> ，<strong>统计</strong> 满足该要求的方案数目<strong>。</strong></li>
</ul>

<p><strong>轴对齐正方形</strong> 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。</p>

<p>实现 <code>DetectSquares</code> 类：</p>

<ul>
	<li><code>DetectSquares()</code> 使用空数据结构初始化对象</li>
	<li><code>void add(int[] point)</code> 向数据结构添加一个新的点 <code>point = [x, y]</code></li>
	<li><code>int count(int[] point)</code> 统计按上述方式与点 <code>point = [x, y]</code> 共同构造 <strong>轴对齐正方形</strong> 的方案数。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/01/image.png" style="width: 869px; height: 504px;" />
<pre>
<strong>输入：</strong>
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
<strong>输出：</strong>
[null, null, null, null, 1, 0, null, 2]

<strong>解释：</strong>
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // 返回 1 。你可以选择：
                               //   - 第一个，第二个，和第三个点
detectSquares.count([14, 8]);  // 返回 0 。查询点无法与数据结构中的这些点构成正方形。
detectSquares.add([11, 2]);    // 允许添加重复的点。
detectSquares.count([11, 10]); // 返回 2 。你可以选择：
                               //   - 第一个，第二个，和第三个点
                               //   - 第一个，第三个，和第四个点
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>point.length == 2</code></li>
	<li><code>0 &lt;= x, y &lt;= 1000</code></li>
	<li>调用&nbsp;<code>add</code> 和 <code>count</code> 的 <strong>总次数</strong> 最多为 <code>5000</code></li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 哈希表
- 计数

## 提示

1. Maintain the frequency of all the points in a hash map.
2. Traverse the hash map and if any point has the same y-coordinate as the query point, consider this point and the query point to form one of the horizontal lines of the square.

## 示例

```
["DetectSquares","add","add","add","count","count","add","count"]
[[],[[3,10]],[[11,2]],[[3,2]],[[11,10]],[[14,8]],[[11,2]],[[11,10]]]
```

## 示例代码

### C++

```cpp
class DetectSquares {
public:
    DetectSquares() {
        
    }
    
    void add(vector<int> point) {
        
    }
    
    int count(vector<int> point) {
        
    }
};

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares* obj = new DetectSquares();
 * obj->add(point);
 * int param_2 = obj->count(point);
 */
```

### Java

```java
class DetectSquares {

    public DetectSquares() {
        
    }
    
    public void add(int[] point) {
        
    }
    
    public int count(int[] point) {
        
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares obj = new DetectSquares();
 * obj.add(point);
 * int param_2 = obj.count(point);
 */
```

### Python

```python
class DetectSquares(object):

    def __init__(self):
        

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
```

### Python3

```python3
class DetectSquares:

    def __init__(self):
        

    def add(self, point: List[int]) -> None:
        

    def count(self, point: List[int]) -> int:
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
```

### C

```c



typedef struct {
    
} DetectSquares;


DetectSquares* detectSquaresCreate() {
    
}

void detectSquaresAdd(DetectSquares* obj, int* point, int pointSize) {
    
}

int detectSquaresCount(DetectSquares* obj, int* point, int pointSize) {
    
}

void detectSquaresFree(DetectSquares* obj) {
    
}

/**
 * Your DetectSquares struct will be instantiated and called as such:
 * DetectSquares* obj = detectSquaresCreate();
 * detectSquaresAdd(obj, point, pointSize);
 
 * int param_2 = detectSquaresCount(obj, point, pointSize);
 
 * detectSquaresFree(obj);
*/
```

### C#

```csharp
public class DetectSquares {

    public DetectSquares() {
        
    }
    
    public void Add(int[] point) {
        
    }
    
    public int Count(int[] point) {
        
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares obj = new DetectSquares();
 * obj.Add(point);
 * int param_2 = obj.Count(point);
 */
```

### JavaScript

```javascript

var DetectSquares = function() {
    
};

/** 
 * @param {number[]} point
 * @return {void}
 */
DetectSquares.prototype.add = function(point) {
    
};

/** 
 * @param {number[]} point
 * @return {number}
 */
DetectSquares.prototype.count = function(point) {
    
};

/** 
 * Your DetectSquares object will be instantiated and called as such:
 * var obj = new DetectSquares()
 * obj.add(point)
 * var param_2 = obj.count(point)
 */
```

### TypeScript

```typescript
class DetectSquares {
    constructor() {
        
    }

    add(point: number[]): void {
        
    }

    count(point: number[]): number {
        
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * var obj = new DetectSquares()
 * obj.add(point)
 * var param_2 = obj.count(point)
 */
```

### PHP

```php
class DetectSquares {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer[] $point
     * @return NULL
     */
    function add($point) {
        
    }
  
    /**
     * @param Integer[] $point
     * @return Integer
     */
    function count($point) {
        
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * $obj = DetectSquares();
 * $obj->add($point);
 * $ret_2 = $obj->count($point);
 */
```

### Swift

```swift

class DetectSquares {

    init() {
        
    }
    
    func add(_ point: [Int]) {
        
    }
    
    func count(_ point: [Int]) -> Int {
        
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * let obj = DetectSquares()
 * obj.add(point)
 * let ret_2: Int = obj.count(point)
 */
```

### Kotlin

```kotlin
class DetectSquares() {

    fun add(point: IntArray) {
        
    }

    fun count(point: IntArray): Int {
        
    }

}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * var obj = DetectSquares()
 * obj.add(point)
 * var param_2 = obj.count(point)
 */
```

### Dart

```dart
class DetectSquares {

  DetectSquares() {
    
  }
  
  void add(List<int> point) {
    
  }
  
  int count(List<int> point) {
    
  }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares obj = DetectSquares();
 * obj.add(point);
 * int param2 = obj.count(point);
 */
```

### Go

```golang
type DetectSquares struct {
    
}


func Constructor() DetectSquares {
    
}


func (this *DetectSquares) Add(point []int)  {
    
}


func (this *DetectSquares) Count(point []int) int {
    
}


/**
 * Your DetectSquares object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(point);
 * param_2 := obj.Count(point);
 */
```

### Ruby

```ruby
class DetectSquares
    def initialize()
        
    end


=begin
    :type point: Integer[]
    :rtype: Void
=end
    def add(point)
        
    end


=begin
    :type point: Integer[]
    :rtype: Integer
=end
    def count(point)
        
    end


end

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares.new()
# obj.add(point)
# param_2 = obj.count(point)
```

### Scala

```scala
class DetectSquares() {

    def add(point: Array[Int]): Unit = {
        
    }

    def count(point: Array[Int]): Int = {
        
    }

}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * val obj = new DetectSquares()
 * obj.add(point)
 * val param_2 = obj.count(point)
 */
```

### Rust

```rust
struct DetectSquares {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl DetectSquares {

    fn new() -> Self {
        
    }
    
    fn add(&self, point: Vec<i32>) {
        
    }
    
    fn count(&self, point: Vec<i32>) -> i32 {
        
    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * let obj = DetectSquares::new();
 * obj.add(point);
 * let ret_2: i32 = obj.count(point);
 */
```

### Racket

```racket
(define detect-squares%
  (class object%
    (super-new)
    
    (init-field)
    
    ; add : (listof exact-integer?) -> void?
    (define/public (add point)
      )
    ; count : (listof exact-integer?) -> exact-integer?
    (define/public (count point)
      )))

;; Your detect-squares% object will be instantiated and called as such:
;; (define obj (new detect-squares%))
;; (send obj add point)
;; (define param_2 (send obj count point))
```

### Erlang

```erlang
-spec detect_squares_init_() -> any().
detect_squares_init_() ->
  .

-spec detect_squares_add(Point :: [integer()]) -> any().
detect_squares_add(Point) ->
  .

-spec detect_squares_count(Point :: [integer()]) -> integer().
detect_squares_count(Point) ->
  .


%% Your functions will be called as such:
%% detect_squares_init_(),
%% detect_squares_add(Point),
%% Param_2 = detect_squares_count(Point),

%% detect_squares_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule DetectSquares do
  @spec init_() :: any
  def init_() do
    
  end

  @spec add(point :: [integer]) :: any
  def add(point) do
    
  end

  @spec count(point :: [integer]) :: integer
  def count(point) do
    
  end
end

# Your functions will be called as such:
# DetectSquares.init_()
# DetectSquares.add(point)
# param_2 = DetectSquares.count(point)

# DetectSquares.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class DetectSquares {
    init() {

    }
    
    func add(point: Array<Int64>): Unit {

    }
    
    func count(point: Array<Int64>): Int64 {

    }
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * let obj: DetectSquares = DetectSquares()
 * obj.add(point)
 * let param_2 = obj.count(point)
 */
```

