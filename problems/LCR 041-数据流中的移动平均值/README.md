# LCR 041. 数据流中的移动平均值

## 题目描述

<p>给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算滑动窗口里所有数字的平均值。</p>

<p>实现 <code>MovingAverage</code> 类：</p>

<ul>
	<li><code>MovingAverage(int size)</code> 用窗口大小 <code>size</code> 初始化对象。</li>
	<li><code>double next(int val)</code>&nbsp;成员函数 <code>next</code>&nbsp;每次调用的时候都会往滑动窗口增加一个整数，请计算并返回数据流中最后 <code>size</code> 个值的移动平均值，即滑动窗口里所有数字的平均值。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
inputs = [&quot;MovingAverage&quot;, &quot;next&quot;, &quot;next&quot;, &quot;next&quot;, &quot;next&quot;]
inputs = [[3], [1], [10], [3], [5]]
<strong>输出：</strong>
[null, 1.0, 5.5, 4.66667, 6.0]

<strong>解释：</strong>
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // 返回 1.0 = 1 / 1
movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= size &lt;= 1000</code></li>
	<li><code>-10<sup>5</sup> &lt;= val &lt;= 10<sup>5</sup></code></li>
	<li>最多调用 <code>next</code> 方法 <code>10<sup>4</sup></code> 次</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 346&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/moving-average-from-data-stream/">https://leetcode-cn.com/problems/moving-average-from-data-stream/</a></p>


## 难度

Easy

## 标签

- 设计
- 队列
- 数组
- 数据流

## 示例

```
["MovingAverage","next","next","next","next"]
[[3],[1],[10],[3],[5]]
```

## 示例代码

### C++

```cpp
class MovingAverage {
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) {

    }
    
    double next(int val) {

    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */
```

### Java

```java
class MovingAverage {

    /** Initialize your data structure here. */
    public MovingAverage(int size) {

    }
    
    public double next(int val) {

    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
```

### Python

```python
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```

### Python3

```python3
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """


    def next(self, val: int) -> float:



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```

### C

```c



typedef struct {

} MovingAverage;

/** Initialize your data structure here. */

MovingAverage* movingAverageCreate(int size) {

}

double movingAverageNext(MovingAverage* obj, int val) {

}

void movingAverageFree(MovingAverage* obj) {

}

/**
 * Your MovingAverage struct will be instantiated and called as such:
 * MovingAverage* obj = movingAverageCreate(size);
 * double param_1 = movingAverageNext(obj, val);
 
 * movingAverageFree(obj);
*/
```

### C#

```csharp
public class MovingAverage {

    /** Initialize your data structure here. */
    public MovingAverage(int size) {

    }
    
    public double Next(int val) {

    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.Next(val);
 */
```

### JavaScript

```javascript
/**
 * Initialize your data structure here.
 * @param {number} size
 */
var MovingAverage = function(size) {

};

/** 
 * @param {number} val
 * @return {number}
 */
MovingAverage.prototype.next = function(val) {

};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */
```

### TypeScript

```typescript
class MovingAverage {
    constructor(size: number) {

    }

    next(val: number): number {

    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */
```

### PHP

```php
class MovingAverage {
    /**
     * Initialize your data structure here.
     * @param Integer $size
     */
    function __construct($size) {

    }

    /**
     * @param Integer $val
     * @return Float
     */
    function next($val) {

    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * $obj = MovingAverage($size);
 * $ret_1 = $obj->next($val);
 */
```

### Swift

```swift

class MovingAverage {

    /** Initialize your data structure here. */
    init(_ size: Int) {

    }
    
    func next(_ val: Int) -> Double {

    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * let obj = MovingAverage(size)
 * let ret_1: Double = obj.next(val)
 */
```

### Kotlin

```kotlin
class MovingAverage(size: Int) {

    /** Initialize your data structure here. */


    fun next(`val`: Int): Double {

    }

}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = MovingAverage(size)
 * var param_1 = obj.next(`val`)
 */
```

### Go

```golang
type MovingAverage struct {

}


/** Initialize your data structure here. */
func Constructor(size int) MovingAverage {

}


func (this *MovingAverage) Next(val int) float64 {

}


/**
 * Your MovingAverage object will be instantiated and called as such:
 * obj := Constructor(size);
 * param_1 := obj.Next(val);
 */
```

### Ruby

```ruby
class MovingAverage

=begin
    Initialize your data structure here.
    :type size: Integer
=end
    def initialize(size)

    end


=begin
    :type val: Integer
    :rtype: Float
=end
    def next(val)

    end


end

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage.new(size)
# param_1 = obj.next(val)
```

### Scala

```scala
class MovingAverage(_size: Int) {

    /** Initialize your data structure here. */


    def next(`val`: Int): Double = {

    }

}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(`val`)
 */
```

### Rust

```rust
struct MovingAverage {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MovingAverage {

    /** Initialize your data structure here. */
    fn new(size: i32) -> Self {

    }
    
    fn next(&self, val: i32) -> f64 {

    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * let obj = MovingAverage::new(size);
 * let ret_1: f64 = obj.next(val);
 */
```

### Racket

```racket
(define moving-average%
  (class object%
    (super-new)

    ; size : exact-integer?
    (init-field
      size)
    
    ; next : exact-integer? -> flonum?
    (define/public (next val)

      )))

;; Your moving-average% object will be instantiated and called as such:
;; (define obj (new moving-average% [size size]))
;; (define param_1 (send obj next val))
```

### Erlang

```erlang
-spec moving_average_init_(Size :: integer()) -> any().
moving_average_init_(Size) ->
  .

-spec moving_average_next(Val :: integer()) -> float().
moving_average_next(Val) ->
  .


%% Your functions will be called as such:
%% moving_average_init_(Size),
%% Param_1 = moving_average_next(Val),

%% moving_average_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MovingAverage do
  @spec init_(size :: integer) :: any
  def init_(size) do

  end

  @spec next(val :: integer) :: float
  def next(val) do

  end
end

# Your functions will be called as such:
# MovingAverage.init_(size)
# param_1 = MovingAverage.next(val)

# MovingAverage.init_ will be called before every test case, in which you can do some necessary initializations.
```

