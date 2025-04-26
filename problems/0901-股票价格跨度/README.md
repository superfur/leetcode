# 901. 股票价格跨度

## 题目描述

<p>设计一个算法收集某些股票的每日报价，并返回该股票当日价格的 <strong>跨度</strong> 。</p>

<p>当日股票价格的 <strong>跨度</strong> 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。</p>

<ul>
	<li>
	<p>例如，如果未来 7 天股票的价格是 <code>[100,80,60,70,60,75,85]</code>，那么股票跨度将是 <code>[1,1,1,2,1,4,6]</code> 。</p>
	</li>
</ul>

<p>实现 <code>StockSpanner</code> 类：</p>

<ul>
	<li><code>StockSpanner()</code> 初始化类对象。</li>
	<li><code>int next(int price)</code> 给出今天的股价 <code>price</code> ，返回该股票当日价格的 <strong>跨度</strong> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例：</strong></p>

<pre>
<strong>输入</strong>：
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
<strong>输出</strong>：
[null, 1, 1, 1, 2, 1, 4, 6]

<strong>解释：</strong>
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // 返回 1
stockSpanner.next(80);  // 返回 1
stockSpanner.next(60);  // 返回 1
stockSpanner.next(70);  // 返回 2
stockSpanner.next(60);  // 返回 1
stockSpanner.next(75);  // 返回 4 ，因为截至今天的最后 4 个股价 (包括今天的股价 75) 都小于或等于今天的股价。
stockSpanner.next(85);  // 返回 6
</pre>
&nbsp;

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= price &lt;= 10<sup>5</sup></code></li>
	<li>最多调用 <code>next</code> 方法 <code>10<sup>4</sup></code> 次</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 设计
- 数据流
- 单调栈

## 示例

```
["StockSpanner","next","next","next","next","next","next","next"]
[[],[100],[80],[60],[70],[60],[75],[85]]
```

## 示例代码

### C++

```cpp
class StockSpanner {
public:
    StockSpanner() {
        
    }
    
    int next(int price) {
        
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
```

### Java

```java
class StockSpanner {

    public StockSpanner() {
        
    }
    
    public int next(int price) {
        
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */
```

### Python

```python
class StockSpanner(object):

    def __init__(self):
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
```

### Python3

```python3
class StockSpanner:

    def __init__(self):
        

    def next(self, price: int) -> int:
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
```

### C

```c



typedef struct {
    
} StockSpanner;


StockSpanner* stockSpannerCreate() {
    
}

int stockSpannerNext(StockSpanner* obj, int price) {
    
}

void stockSpannerFree(StockSpanner* obj) {
    
}

/**
 * Your StockSpanner struct will be instantiated and called as such:
 * StockSpanner* obj = stockSpannerCreate();
 * int param_1 = stockSpannerNext(obj, price);
 
 * stockSpannerFree(obj);
*/
```

### C#

```csharp
public class StockSpanner {

    public StockSpanner() {
        
    }
    
    public int Next(int price) {
        
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.Next(price);
 */
```

### JavaScript

```javascript

var StockSpanner = function() {
    
};

/** 
 * @param {number} price
 * @return {number}
 */
StockSpanner.prototype.next = function(price) {
    
};

/** 
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */
```

### TypeScript

```typescript
class StockSpanner {
    constructor() {
        
    }

    next(price: number): number {
        
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */
```

### PHP

```php
class StockSpanner {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $price
     * @return Integer
     */
    function next($price) {
        
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * $obj = StockSpanner();
 * $ret_1 = $obj->next($price);
 */
```

### Swift

```swift

class StockSpanner {

    init() {
        
    }
    
    func next(_ price: Int) -> Int {
        
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * let obj = StockSpanner()
 * let ret_1: Int = obj.next(price)
 */
```

### Kotlin

```kotlin
class StockSpanner() {

    fun next(price: Int): Int {
        
    }

}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = StockSpanner()
 * var param_1 = obj.next(price)
 */
```

### Dart

```dart
class StockSpanner {

  StockSpanner() {
    
  }
  
  int next(int price) {
    
  }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = StockSpanner();
 * int param1 = obj.next(price);
 */
```

### Go

```golang
type StockSpanner struct {
    
}


func Constructor() StockSpanner {
    
}


func (this *StockSpanner) Next(price int) int {
    
}


/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */
```

### Ruby

```ruby
class StockSpanner
    def initialize()
        
    end


=begin
    :type price: Integer
    :rtype: Integer
=end
    def next(price)
        
    end


end

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner.new()
# param_1 = obj.next(price)
```

### Scala

```scala
class StockSpanner() {

    def next(price: Int): Int = {
        
    }

}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * val obj = new StockSpanner()
 * val param_1 = obj.next(price)
 */
```

### Rust

```rust
struct StockSpanner {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StockSpanner {

    fn new() -> Self {
        
    }
    
    fn next(&self, price: i32) -> i32 {
        
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * let obj = StockSpanner::new();
 * let ret_1: i32 = obj.next(price);
 */
```

### Racket

```racket
(define stock-spanner%
  (class object%
    (super-new)
    
    (init-field)
    
    ; next : exact-integer? -> exact-integer?
    (define/public (next price)
      )))

;; Your stock-spanner% object will be instantiated and called as such:
;; (define obj (new stock-spanner%))
;; (define param_1 (send obj next price))
```

### Erlang

```erlang
-spec stock_spanner_init_() -> any().
stock_spanner_init_() ->
  .

-spec stock_spanner_next(Price :: integer()) -> integer().
stock_spanner_next(Price) ->
  .


%% Your functions will be called as such:
%% stock_spanner_init_(),
%% Param_1 = stock_spanner_next(Price),

%% stock_spanner_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule StockSpanner do
  @spec init_() :: any
  def init_() do
    
  end

  @spec next(price :: integer) :: integer
  def next(price) do
    
  end
end

# Your functions will be called as such:
# StockSpanner.init_()
# param_1 = StockSpanner.next(price)

# StockSpanner.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class StockSpanner {
    init() {

    }
    
    func next(price: Int64): Int64 {

    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * let obj: StockSpanner = StockSpanner()
 * let param_1 = obj.next(price)
 */
```

