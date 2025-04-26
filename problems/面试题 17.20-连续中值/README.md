# 面试题 17.20. 连续中值

## 题目描述

<p>随机产生数字并传递给一个方法。你能否完成这个方法，在每次产生新值时，寻找当前所有值的中间值（中位数）并保存。</p>

<p>中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。</p>

<p>例如，</p>

<p>[2,3,4]&nbsp;的中位数是 3</p>

<p>[2,3] 的中位数是 (2 + 3) / 2 = 2.5</p>

<p>设计一个支持以下两种操作的数据结构：</p>

<ul>
	<li>void addNum(int num) - 从数据流中添加一个整数到数据结构中。</li>
	<li>double findMedian() - 返回目前所有元素的中位数。</li>
</ul>

<p><strong>示例：</strong></p>

<pre>addNum(1)
addNum(2)
findMedian() -&gt; 1.5
addNum(3) 
findMedian() -&gt; 2
</pre>


## 难度

Hard

## 标签

- 设计
- 双指针
- 数据流
- 排序
- 堆（优先队列）

## 提示

1. 回想一下，中位数是指比一半数字更大、一半数字更小的数字。
2. 注意，必须存储见过的所有元素。即使是前100个元素中最小的元素也可以成为中间值。你不能抛弃较大或较小的元素。
3. 另一种思考方法是：你能维护元素的下半部分和上半部分吗?
4. 如果使用堆呢？或是两个堆？

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
    /** initialize your data structure here. */
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

    /** initialize your data structure here. */
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
        """
        initialize your data structure here.
        """
        

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
        """
        initialize your data structure here.
        """
        

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

/** initialize your data structure here. */

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

    /** initialize your data structure here. */
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
/**
 * initialize your data structure here.
 */
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
     * initialize your data structure here.
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

    /** initialize your data structure here. */
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

    /** initialize your data structure here. */
    

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

  /** initialize your data structure here. */
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


/** initialize your data structure here. */
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

=begin
    initialize your data structure here.
=end
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

    /** initialize your data structure here. */
    

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

    /** initialize your data structure here. */
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
    /** initialize your data structure here. */
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

