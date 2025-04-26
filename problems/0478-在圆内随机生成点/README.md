# 478. 在圆内随机生成点

## 题目描述

<p>给定圆的半径和圆心的位置，实现函数 <code>randPoint</code> ，在圆中产生均匀随机点。</p>

<p>实现&nbsp;<code>Solution</code>&nbsp;类:</p>

<ul>
	<li><code>Solution(double radius, double x_center, double y_center)</code>&nbsp;用圆的半径&nbsp;<code>radius</code>&nbsp;和圆心的位置<code> (x_center, y_center)</code> 初始化对象</li>
	<li><code>randPoint()</code>&nbsp;返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 <code>[x, y]</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: 
</strong>["Solution","randPoint","randPoint","randPoint"]
[[1.0, 0.0, 0.0], [], [], []]
<strong>输出: </strong>[null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
<strong>解释:</strong>
Solution solution = new Solution(1.0, 0.0, 0.0);
solution.randPoint ();//返回[-0.02493，-0.38077]
solution.randPoint ();//返回[0.82314,0.38945]
solution.randPoint ();//返回[0.36572,0.17248]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;&nbsp;radius &lt;= 10<sup>8</sup></code></li>
	<li><code>-10<sup>7</sup>&nbsp;&lt;= x_center, y_center &lt;= 10<sup>7</sup></code></li>
	<li><code>randPoint</code> 最多被调用&nbsp;<code>3 * 10<sup>4</sup></code>&nbsp;次</li>
</ul>


## 难度

Medium

## 标签

- 几何
- 数学
- 拒绝采样
- 随机化

## 示例

```
["Solution","randPoint","randPoint","randPoint"]
[[1.0,0.0,0.0],[],[],[]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    Solution(double radius, double x_center, double y_center) {
        
    }
    
    vector<double> randPoint() {
        
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj->randPoint();
 */
```

### Java

```java
class Solution {

    public Solution(double radius, double x_center, double y_center) {
        
    }
    
    public double[] randPoint() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(radius, x_center, y_center);
 * double[] param_1 = obj.randPoint();
 */
```

### Python

```python
class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        

    def randPoint(self):
        """
        :rtype: List[float]
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
```

### Python3

```python3
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        

    def randPoint(self) -> List[float]:
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
```

### C

```c



typedef struct {
    
} Solution;


Solution* solutionCreate(double radius, double x_center, double y_center) {
    
}

double* solutionRandPoint(Solution* obj, int* retSize) {
    
}

void solutionFree(Solution* obj) {
    
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(radius, x_center, y_center);
 * double* param_1 = solutionRandPoint(obj, retSize);
 
 * solutionFree(obj);
*/
```

### C#

```csharp
public class Solution {

    public Solution(double radius, double x_center, double y_center) {
        
    }
    
    public double[] RandPoint() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(radius, x_center, y_center);
 * double[] param_1 = obj.RandPoint();
 */
```

### JavaScript

```javascript
/**
 * @param {number} radius
 * @param {number} x_center
 * @param {number} y_center
 */
var Solution = function(radius, x_center, y_center) {
    
};

/**
 * @return {number[]}
 */
Solution.prototype.randPoint = function() {
    
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(radius, x_center, y_center)
 * var param_1 = obj.randPoint()
 */
```

### TypeScript

```typescript
class Solution {
    constructor(radius: number, x_center: number, y_center: number) {
        
    }

    randPoint(): number[] {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(radius, x_center, y_center)
 * var param_1 = obj.randPoint()
 */
```

### PHP

```php
class Solution {
    /**
     * @param Float $radius
     * @param Float $x_center
     * @param Float $y_center
     */
    function __construct($radius, $x_center, $y_center) {
        
    }
  
    /**
     * @return Float[]
     */
    function randPoint() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = Solution($radius, $x_center, $y_center);
 * $ret_1 = $obj->randPoint();
 */
```

### Swift

```swift

class Solution {

    init(_ radius: Double, _ x_center: Double, _ y_center: Double) {
        
    }
    
    func randPoint() -> [Double] {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution(radius, x_center, y_center)
 * let ret_1: [Double] = obj.randPoint()
 */
```

### Kotlin

```kotlin
class Solution(radius: Double, x_center: Double, y_center: Double) {

    fun randPoint(): DoubleArray {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(radius, x_center, y_center)
 * var param_1 = obj.randPoint()
 */
```

### Dart

```dart
class Solution {

  Solution(double radius, double x_center, double y_center) {
    
  }
  
  List<double> randPoint() {
    
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(radius, x_center, y_center);
 * List<double> param1 = obj.randPoint();
 */
```

### Go

```golang
type Solution struct {
    
}


func Constructor(radius float64, x_center float64, y_center float64) Solution {
    
}


func (this *Solution) RandPoint() []float64 {
    
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(radius, x_center, y_center);
 * param_1 := obj.RandPoint();
 */
```

### Ruby

```ruby
class Solution

=begin
    :type radius: Float
    :type x_center: Float
    :type y_center: Float
=end
    def initialize(radius, x_center, y_center)
        
    end


=begin
    :rtype: Float[]
=end
    def rand_point()
        
    end


end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(radius, x_center, y_center)
# param_1 = obj.rand_point()
```

### Scala

```scala
class Solution(_radius: Double, _x_center: Double, _y_center: Double) {

    def randPoint(): Array[Double] = {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(radius, x_center, y_center)
 * val param_1 = obj.randPoint()
 */
```

### Rust

```rust
struct Solution {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(radius: f64, x_center: f64, y_center: f64) -> Self {
        
    }
    
    fn rand_point(&self) -> Vec<f64> {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(radius, x_center, y_center);
 * let ret_1: Vec<f64> = obj.rand_point();
 */
```

### Racket

```racket
(define solution%
  (class object%
    (super-new)
    
    ; radius : flonum?
    ; x_center : flonum?
    ; y_center : flonum?
    (init-field
      radius
      x_center
      y_center)
    
    ; rand-point : -> (listof flonum?)
    (define/public (rand-point)
      )))

;; Your solution% object will be instantiated and called as such:
;; (define obj (new solution% [radius radius] [x_center x_center] [y_center y_center]))
;; (define param_1 (send obj rand-point))
```

### Erlang

```erlang
-spec solution_init_(Radius :: float(), X_center :: float(), Y_center :: float()) -> any().
solution_init_(Radius, X_center, Y_center) ->
  .

-spec solution_rand_point() -> [float()].
solution_rand_point() ->
  .


%% Your functions will be called as such:
%% solution_init_(Radius, X_center, Y_center),
%% Param_1 = solution_rand_point(),

%% solution_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Solution do
  @spec init_(radius :: float, x_center :: float, y_center :: float) :: any
  def init_(radius, x_center, y_center) do
    
  end

  @spec rand_point() :: [float]
  def rand_point() do
    
  end
end

# Your functions will be called as such:
# Solution.init_(radius, x_center, y_center)
# param_1 = Solution.rand_point()

# Solution.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Solution {
    init(radius: Float64, x_center: Float64, y_center: Float64) {

    }
    
    func randPoint(): Array<Float64> {

    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj: Solution = Solution(radius, x_center, y_center)
 * let param_1 = obj.randPoint()
 */
```

