# 295. 数据流的中位数

## 题目描述

<p><strong>中位数</strong>是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。</p>

<ul>
	<li>例如 <code>arr = [2,3,4]</code>&nbsp;的中位数是 <code>3</code>&nbsp;。</li>
	<li>例如&nbsp;<code>arr = [2,3]</code> 的中位数是 <code>(2 + 3) / 2 = 2.5</code> 。</li>
</ul>

<p>实现 MedianFinder 类:</p>

<ul>
	<li>
	<p><code>MedianFinder() </code>初始化 <code>MedianFinder</code>&nbsp;对象。</p>
	</li>
	<li>
	<p><code>void addNum(int num)</code> 将数据流中的整数 <code>num</code> 添加到数据结构中。</p>
	</li>
	<li>
	<p><code>double findMedian()</code> 返回到目前为止所有元素的中位数。与实际答案相差&nbsp;<code>10<sup>-5</sup></code>&nbsp;以内的答案将被接受。</p>
	</li>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入</strong>
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
<strong>输出</strong>
[null, null, null, 1.5, null, 2.0]

<strong>解释</strong>
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= num &lt;= 10<sup>5</sup></code></li>
	<li>在调用 <code>findMedian</code>&nbsp;之前，数据结构中至少有一个元素</li>
	<li>最多&nbsp;<code>5 * 10<sup>4</sup></code>&nbsp;次调用&nbsp;<code>addNum</code>&nbsp;和&nbsp;<code>findMedian</code></li>
</ul>


## 难度

Hard

## 标签

- 设计
- 双指针
- 数据流
- 排序
- 堆（优先队列）

## 示例

```
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
```

## 示例代码

### C++

```cpp
class MedianFinder {
public:
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        
    }
    
    double findMedian() {
        
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
```

### Java

```java
class MedianFinder {

    public MedianFinder() {
        
    }
    
    public void addNum(int num) {
        
    }
    
    public double findMedian() {
        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
```

### Python

```python
class MedianFinder(object):

    def __init__(self):
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        

    def findMedian(self):
        """
        :rtype: float
        """
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

### Python3

```python3
class MedianFinder:

    def __init__(self):
        

    def addNum(self, num: int) -> None:
        

    def findMedian(self) -> float:
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

### C

```c



typedef struct {
    
} MedianFinder;


MedianFinder* medianFinderCreate() {
    
}

void medianFinderAddNum(MedianFinder* obj, int num) {
    
}

double medianFinderFindMedian(MedianFinder* obj) {
    
}

void medianFinderFree(MedianFinder* obj) {
    
}

/**
 * Your MedianFinder struct will be instantiated and called as such:
 * MedianFinder* obj = medianFinderCreate();
 * medianFinderAddNum(obj, num);
 
 * double param_2 = medianFinderFindMedian(obj);
 
 * medianFinderFree(obj);
*/
```

### C#

```csharp
public class MedianFinder {

    public MedianFinder() {
        
    }
    
    public void AddNum(int num) {
        
    }
    
    public double FindMedian() {
        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.AddNum(num);
 * double param_2 = obj.FindMedian();
 */
```

### JavaScript

```javascript

var MedianFinder = function() {
    
};

/** 
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function(num) {
    
};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function() {
    
};

/** 
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
```

### TypeScript

```typescript
class MedianFinder {
    constructor() {
        
    }

    addNum(num: number): void {
        
    }

    findMedian(): number {
        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
```

### PHP

```php
class MedianFinder {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $num
     * @return NULL
     */
    function addNum($num) {
        
    }
  
    /**
     * @return Float
     */
    function findMedian() {
        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * $obj = MedianFinder();
 * $obj->addNum($num);
 * $ret_2 = $obj->findMedian();
 */
```

### Swift

```swift

class MedianFinder {

    init() {
        
    }
    
    func addNum(_ num: Int) {
        
    }
    
    func findMedian() -> Double {
        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder()
 * obj.addNum(num)
 * let ret_2: Double = obj.findMedian()
 */
```

### Kotlin

```kotlin
class MedianFinder() {

    fun addNum(num: Int) {
        
    }

    fun findMedian(): Double {
        
    }

}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
```

### Dart

```dart
class MedianFinder {

  MedianFinder() {
    
  }
  
  void addNum(int num) {
    
  }
  
  double findMedian() {
    
  }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = MedianFinder();
 * obj.addNum(num);
 * double param2 = obj.findMedian();
 */
```

### Go

```golang
type MedianFinder struct {
    
}


func Constructor() MedianFinder {
    
}


func (this *MedianFinder) AddNum(num int)  {
    
}


func (this *MedianFinder) FindMedian() float64 {
    
}


/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */
```

### Ruby

```ruby
class MedianFinder
    def initialize()
        
    end


=begin
    :type num: Integer
    :rtype: Void
=end
    def add_num(num)
        
    end


=begin
    :rtype: Float
=end
    def find_median()
        
    end


end

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder.new()
# obj.add_num(num)
# param_2 = obj.find_median()
```

### Scala

```scala
class MedianFinder() {

    def addNum(num: Int): Unit = {
        
    }

    def findMedian(): Double = {
        
    }

}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * val obj = new MedianFinder()
 * obj.addNum(num)
 * val param_2 = obj.findMedian()
 */
```

### Rust

```rust
struct MedianFinder {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {

    fn new() -> Self {
        
    }
    
    fn add_num(&self, num: i32) {
        
    }
    
    fn find_median(&self) -> f64 {
        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */
```

### Racket

```racket
(define median-finder%
  (class object%
    (super-new)
    
    (init-field)
    
    ; add-num : exact-integer? -> void?
    (define/public (add-num num)
      )
    ; find-median : -> flonum?
    (define/public (find-median)
      )))

;; Your median-finder% object will be instantiated and called as such:
;; (define obj (new median-finder%))
;; (send obj add-num num)
;; (define param_2 (send obj find-median))
```

### Erlang

```erlang
-spec median_finder_init_() -> any().
median_finder_init_() ->
  .

-spec median_finder_add_num(Num :: integer()) -> any().
median_finder_add_num(Num) ->
  .

-spec median_finder_find_median() -> float().
median_finder_find_median() ->
  .


%% Your functions will be called as such:
%% median_finder_init_(),
%% median_finder_add_num(Num),
%% Param_2 = median_finder_find_median(),

%% median_finder_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MedianFinder do
  @spec init_() :: any
  def init_() do
    
  end

  @spec add_num(num :: integer) :: any
  def add_num(num) do
    
  end

  @spec find_median() :: float
  def find_median() do
    
  end
end

# Your functions will be called as such:
# MedianFinder.init_()
# MedianFinder.add_num(num)
# param_2 = MedianFinder.find_median()

# MedianFinder.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MedianFinder {
    init() {

    }
    
    func addNum(num: Int64): Unit {

    }
    
    func findMedian(): Float64 {

    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj: MedianFinder = MedianFinder()
 * obj.addNum(num)
 * let param_2 = obj.findMedian()
 */
```

