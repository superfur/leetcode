# 2034. 股票价格波动

## 题目描述

<p>给你一支股票价格的数据流。数据流中每一条记录包含一个 <strong>时间戳</strong>&nbsp;和该时间点股票对应的 <strong>价格</strong>&nbsp;。</p>

<p>不巧的是，由于股票市场内在的波动性，股票价格记录可能不是按时间顺序到来的。某些情况下，有的记录可能是错的。如果两个有相同时间戳的记录出现在数据流中，前一条记录视为错误记录，后出现的记录 <b>更正</b>&nbsp;前一条错误的记录。</p>

<p>请你设计一个算法，实现：</p>

<ul>
	<li><strong>更新 </strong>股票在某一时间戳的股票价格，如果有之前同一时间戳的价格，这一操作将&nbsp;<strong>更正</strong>&nbsp;之前的错误价格。</li>
	<li>找到当前记录里 <b>最新股票价格</b>&nbsp;。<strong>最新股票价格</strong>&nbsp;定义为时间戳最晚的股票价格。</li>
	<li>找到当前记录里股票的 <strong>最高价格</strong>&nbsp;。</li>
	<li>找到当前记录里股票的 <strong>最低价格</strong>&nbsp;。</li>
</ul>

<p>请你实现&nbsp;<code>StockPrice</code>&nbsp;类：</p>

<ul>
	<li><code>StockPrice()</code>&nbsp;初始化对象，当前无股票价格记录。</li>
	<li><code>void update(int timestamp, int price)</code>&nbsp;在时间点 <code>timestamp</code>&nbsp;更新股票价格为 <code>price</code>&nbsp;。</li>
	<li><code>int current()</code>&nbsp;返回股票 <strong>最新价格</strong>&nbsp;。</li>
	<li><code>int maximum()</code>&nbsp;返回股票 <strong>最高价格</strong>&nbsp;。</li>
	<li><code>int minimum()</code>&nbsp;返回股票 <strong>最低价格</strong>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
<strong>输出：</strong>
[null, null, null, 5, 10, null, 5, null, 2]

<strong>解释：</strong>
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // 时间戳为 [1] ，对应的股票价格为 [10] 。
stockPrice.update(2, 5);  // 时间戳为 [1,2] ，对应的股票价格为 [10,5] 。
stockPrice.current();     // 返回 5 ，最新时间戳为 2 ，对应价格为 5 。
stockPrice.maximum();     // 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。
stockPrice.update(1, 3);  // 之前时间戳为 1 的价格错误，价格更新为 3 。
                          // 时间戳为 [1,2] ，对应股票价格为 [3,5] 。
stockPrice.maximum();     // 返回 5 ，更正后最高价格为 5 。
stockPrice.update(4, 2);  // 时间戳为 [1,2,4] ，对应价格为 [3,5,2] 。
stockPrice.minimum();     // 返回 2 ，最低价格时间戳为 4 ，价格为 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= timestamp, price &lt;= 10<sup>9</sup></code></li>
	<li><code>update</code>，<code>current</code>，<code>maximum</code>&nbsp;和&nbsp;<code>minimum</code>&nbsp;<strong>总</strong> 调用次数不超过&nbsp;<code>10<sup>5</sup></code>&nbsp;。</li>
	<li><code>current</code>，<code>maximum</code>&nbsp;和&nbsp;<code>minimum</code>&nbsp;被调用时，<code>update</code>&nbsp;操作 <strong>至少</strong>&nbsp;已经被调用过 <strong>一次</strong>&nbsp;。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 哈希表
- 数据流
- 有序集合
- 堆（优先队列）

## 提示

1. How would you solve the problem for offline queries (all queries given at once)?
2. Think about which data structure can help insert and delete the most optimal way.

## 示例

```
["StockPrice","update","update","current","maximum","update","maximum","update","minimum"]
[[],[1,10],[2,5],[],[],[1,3],[],[4,2],[]]
```

## 示例代码

### C++

```cpp
class StockPrice {
public:
    StockPrice() {
        
    }
    
    void update(int timestamp, int price) {
        
    }
    
    int current() {
        
    }
    
    int maximum() {
        
    }
    
    int minimum() {
        
    }
};

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice* obj = new StockPrice();
 * obj->update(timestamp,price);
 * int param_2 = obj->current();
 * int param_3 = obj->maximum();
 * int param_4 = obj->minimum();
 */
```

### Java

```java
class StockPrice {

    public StockPrice() {
        
    }
    
    public void update(int timestamp, int price) {
        
    }
    
    public int current() {
        
    }
    
    public int maximum() {
        
    }
    
    public int minimum() {
        
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = new StockPrice();
 * obj.update(timestamp,price);
 * int param_2 = obj.current();
 * int param_3 = obj.maximum();
 * int param_4 = obj.minimum();
 */
```

### Python

```python
class StockPrice(object):

    def __init__(self):
        

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        

    def current(self):
        """
        :rtype: int
        """
        

    def maximum(self):
        """
        :rtype: int
        """
        

    def minimum(self):
        """
        :rtype: int
        """
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
```

### Python3

```python3
class StockPrice:

    def __init__(self):
        

    def update(self, timestamp: int, price: int) -> None:
        

    def current(self) -> int:
        

    def maximum(self) -> int:
        

    def minimum(self) -> int:
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
```

### C

```c



typedef struct {
    
} StockPrice;


StockPrice* stockPriceCreate() {
    
}

void stockPriceUpdate(StockPrice* obj, int timestamp, int price) {
    
}

int stockPriceCurrent(StockPrice* obj) {
    
}

int stockPriceMaximum(StockPrice* obj) {
    
}

int stockPriceMinimum(StockPrice* obj) {
    
}

void stockPriceFree(StockPrice* obj) {
    
}

/**
 * Your StockPrice struct will be instantiated and called as such:
 * StockPrice* obj = stockPriceCreate();
 * stockPriceUpdate(obj, timestamp, price);
 
 * int param_2 = stockPriceCurrent(obj);
 
 * int param_3 = stockPriceMaximum(obj);
 
 * int param_4 = stockPriceMinimum(obj);
 
 * stockPriceFree(obj);
*/
```

### C#

```csharp
public class StockPrice {

    public StockPrice() {
        
    }
    
    public void Update(int timestamp, int price) {
        
    }
    
    public int Current() {
        
    }
    
    public int Maximum() {
        
    }
    
    public int Minimum() {
        
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = new StockPrice();
 * obj.Update(timestamp,price);
 * int param_2 = obj.Current();
 * int param_3 = obj.Maximum();
 * int param_4 = obj.Minimum();
 */
```

### JavaScript

```javascript

var StockPrice = function() {
    
};

/** 
 * @param {number} timestamp 
 * @param {number} price
 * @return {void}
 */
StockPrice.prototype.update = function(timestamp, price) {
    
};

/**
 * @return {number}
 */
StockPrice.prototype.current = function() {
    
};

/**
 * @return {number}
 */
StockPrice.prototype.maximum = function() {
    
};

/**
 * @return {number}
 */
StockPrice.prototype.minimum = function() {
    
};

/** 
 * Your StockPrice object will be instantiated and called as such:
 * var obj = new StockPrice()
 * obj.update(timestamp,price)
 * var param_2 = obj.current()
 * var param_3 = obj.maximum()
 * var param_4 = obj.minimum()
 */
```

### TypeScript

```typescript
class StockPrice {
    constructor() {
        
    }

    update(timestamp: number, price: number): void {
        
    }

    current(): number {
        
    }

    maximum(): number {
        
    }

    minimum(): number {
        
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * var obj = new StockPrice()
 * obj.update(timestamp,price)
 * var param_2 = obj.current()
 * var param_3 = obj.maximum()
 * var param_4 = obj.minimum()
 */
```

### PHP

```php
class StockPrice {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $timestamp
     * @param Integer $price
     * @return NULL
     */
    function update($timestamp, $price) {
        
    }
  
    /**
     * @return Integer
     */
    function current() {
        
    }
  
    /**
     * @return Integer
     */
    function maximum() {
        
    }
  
    /**
     * @return Integer
     */
    function minimum() {
        
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * $obj = StockPrice();
 * $obj->update($timestamp, $price);
 * $ret_2 = $obj->current();
 * $ret_3 = $obj->maximum();
 * $ret_4 = $obj->minimum();
 */
```

### Swift

```swift

class StockPrice {

    init() {
        
    }
    
    func update(_ timestamp: Int, _ price: Int) {
        
    }
    
    func current() -> Int {
        
    }
    
    func maximum() -> Int {
        
    }
    
    func minimum() -> Int {
        
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * let obj = StockPrice()
 * obj.update(timestamp, price)
 * let ret_2: Int = obj.current()
 * let ret_3: Int = obj.maximum()
 * let ret_4: Int = obj.minimum()
 */
```

### Kotlin

```kotlin
class StockPrice() {

    fun update(timestamp: Int, price: Int) {
        
    }

    fun current(): Int {
        
    }

    fun maximum(): Int {
        
    }

    fun minimum(): Int {
        
    }

}

/**
 * Your StockPrice object will be instantiated and called as such:
 * var obj = StockPrice()
 * obj.update(timestamp,price)
 * var param_2 = obj.current()
 * var param_3 = obj.maximum()
 * var param_4 = obj.minimum()
 */
```

### Dart

```dart
class StockPrice {

  StockPrice() {
    
  }
  
  void update(int timestamp, int price) {
    
  }
  
  int current() {
    
  }
  
  int maximum() {
    
  }
  
  int minimum() {
    
  }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice obj = StockPrice();
 * obj.update(timestamp,price);
 * int param2 = obj.current();
 * int param3 = obj.maximum();
 * int param4 = obj.minimum();
 */
```

### Go

```golang
type StockPrice struct {
    
}


func Constructor() StockPrice {
    
}


func (this *StockPrice) Update(timestamp int, price int)  {
    
}


func (this *StockPrice) Current() int {
    
}


func (this *StockPrice) Maximum() int {
    
}


func (this *StockPrice) Minimum() int {
    
}


/**
 * Your StockPrice object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Update(timestamp,price);
 * param_2 := obj.Current();
 * param_3 := obj.Maximum();
 * param_4 := obj.Minimum();
 */
```

### Ruby

```ruby
class StockPrice
    def initialize()
        
    end


=begin
    :type timestamp: Integer
    :type price: Integer
    :rtype: Void
=end
    def update(timestamp, price)
        
    end


=begin
    :rtype: Integer
=end
    def current()
        
    end


=begin
    :rtype: Integer
=end
    def maximum()
        
    end


=begin
    :rtype: Integer
=end
    def minimum()
        
    end


end

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice.new()
# obj.update(timestamp, price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
```

### Scala

```scala
class StockPrice() {

    def update(timestamp: Int, price: Int): Unit = {
        
    }

    def current(): Int = {
        
    }

    def maximum(): Int = {
        
    }

    def minimum(): Int = {
        
    }

}

/**
 * Your StockPrice object will be instantiated and called as such:
 * val obj = new StockPrice()
 * obj.update(timestamp,price)
 * val param_2 = obj.current()
 * val param_3 = obj.maximum()
 * val param_4 = obj.minimum()
 */
```

### Rust

```rust
struct StockPrice {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StockPrice {

    fn new() -> Self {
        
    }
    
    fn update(&self, timestamp: i32, price: i32) {
        
    }
    
    fn current(&self) -> i32 {
        
    }
    
    fn maximum(&self) -> i32 {
        
    }
    
    fn minimum(&self) -> i32 {
        
    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * let obj = StockPrice::new();
 * obj.update(timestamp, price);
 * let ret_2: i32 = obj.current();
 * let ret_3: i32 = obj.maximum();
 * let ret_4: i32 = obj.minimum();
 */
```

### Racket

```racket
(define stock-price%
  (class object%
    (super-new)
    
    (init-field)
    
    ; update : exact-integer? exact-integer? -> void?
    (define/public (update timestamp price)
      )
    ; current : -> exact-integer?
    (define/public (current)
      )
    ; maximum : -> exact-integer?
    (define/public (maximum)
      )
    ; minimum : -> exact-integer?
    (define/public (minimum)
      )))

;; Your stock-price% object will be instantiated and called as such:
;; (define obj (new stock-price%))
;; (send obj update timestamp price)
;; (define param_2 (send obj current))
;; (define param_3 (send obj maximum))
;; (define param_4 (send obj minimum))
```

### Erlang

```erlang
-spec stock_price_init_() -> any().
stock_price_init_() ->
  .

-spec stock_price_update(Timestamp :: integer(), Price :: integer()) -> any().
stock_price_update(Timestamp, Price) ->
  .

-spec stock_price_current() -> integer().
stock_price_current() ->
  .

-spec stock_price_maximum() -> integer().
stock_price_maximum() ->
  .

-spec stock_price_minimum() -> integer().
stock_price_minimum() ->
  .


%% Your functions will be called as such:
%% stock_price_init_(),
%% stock_price_update(Timestamp, Price),
%% Param_2 = stock_price_current(),
%% Param_3 = stock_price_maximum(),
%% Param_4 = stock_price_minimum(),

%% stock_price_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule StockPrice do
  @spec init_() :: any
  def init_() do
    
  end

  @spec update(timestamp :: integer, price :: integer) :: any
  def update(timestamp, price) do
    
  end

  @spec current() :: integer
  def current() do
    
  end

  @spec maximum() :: integer
  def maximum() do
    
  end

  @spec minimum() :: integer
  def minimum() do
    
  end
end

# Your functions will be called as such:
# StockPrice.init_()
# StockPrice.update(timestamp, price)
# param_2 = StockPrice.current()
# param_3 = StockPrice.maximum()
# param_4 = StockPrice.minimum()

# StockPrice.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class StockPrice {
    init() {

    }
    
    func update(timestamp: Int64, price: Int64): Unit {

    }
    
    func current(): Int64 {

    }
    
    func maximum(): Int64 {

    }
    
    func minimum(): Int64 {

    }
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * let obj: StockPrice = StockPrice()
 * obj.update(timestamp,price)
 * let param_2 = obj.current()
 * let param_3 = obj.maximum()
 * let param_4 = obj.minimum()
 */
```

