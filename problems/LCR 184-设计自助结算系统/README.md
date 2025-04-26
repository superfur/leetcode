# LCR 184. 设计自助结算系统

## 题目描述

<p>请设计一个自助结账系统，该系统需要通过一个队列来模拟顾客通过购物车的结算过程，需要实现的功能有：</p>

<ul>
	<li><code>get_max()</code>：获取结算商品中的最高价格，如果队列为空，则返回 -1</li>
	<li><code>add(value)</code>：将价格为 <code>value</code> 的商品加入待结算商品队列的尾部</li>
	<li><code>remove()</code>：移除第一个待结算的商品价格，如果队列为空，则返回 -1</li>
</ul>

<p>注意，为保证该系统运转高效性，以上函数的均摊时间复杂度均为 O(1)</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
输入: 
["Checkout","add","add","get_max","remove","get_max"]
[[],[4],[7],[],[],[]]

输出: [null,null,null,7,4,7]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
输入: 
["Checkout","remove","get_max"]
[[],[],[]]

输出: [null,-1,-1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= get_max, add, remove 的总操作数&nbsp;&lt;= 10000</code></li>
	<li><code>1 &lt;= value &lt;= 10^5</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 设计
- 队列
- 单调队列

## 示例

```
["Checkout","add","add","get_max","remove","get_max"]
[[],[4],[7],[],[],[]]
["Checkout","remove","get_max"]
[[],[],[]]
```

## 示例代码

### C++

```cpp
class Checkout {
public:
    Checkout() {
        
    }
    
    int get_max() {
        
    }
    
    void add(int value) {
        
    }
    
    int remove() {
        
    }
};

/**
 * Your Checkout object will be instantiated and called as such:
 * Checkout* obj = new Checkout();
 * int param_1 = obj->get_max();
 * obj->add(value);
 * int param_3 = obj->remove();
 */
```

### Java

```java
class Checkout {

    public Checkout() {
        
    }
    
    public int get_max() {
        
    }
    
    public void add(int value) {
        
    }
    
    public int remove() {
        
    }
}

/**
 * Your Checkout object will be instantiated and called as such:
 * Checkout obj = new Checkout();
 * int param_1 = obj.get_max();
 * obj.add(value);
 * int param_3 = obj.remove();
 */
```

### Python

```python
class Checkout(object):

    def __init__(self):
        

    def get_max(self):
        """
        :rtype: int
        """
        

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        

    def remove(self):
        """
        :rtype: int
        """
        


# Your Checkout object will be instantiated and called as such:
# obj = Checkout()
# param_1 = obj.get_max()
# obj.add(value)
# param_3 = obj.remove()
```

### Python3

```python3
class Checkout:

    def __init__(self):
        

    def get_max(self) -> int:
        

    def add(self, value: int) -> None:
        

    def remove(self) -> int:
        


# Your Checkout object will be instantiated and called as such:
# obj = Checkout()
# param_1 = obj.get_max()
# obj.add(value)
# param_3 = obj.remove()
```

### C

```c



typedef struct {
    
} Checkout;


Checkout* checkoutCreate() {
    
}

int checkoutGet_max(Checkout* obj) {
    
}

void checkoutAdd(Checkout* obj, int value) {
    
}

int checkoutRemove(Checkout* obj) {
    
}

void checkoutFree(Checkout* obj) {
    
}

/**
 * Your Checkout struct will be instantiated and called as such:
 * Checkout* obj = checkoutCreate();
 * int param_1 = checkoutGet_max(obj);
 
 * checkoutAdd(obj, value);
 
 * int param_3 = checkoutRemove(obj);
 
 * checkoutFree(obj);
*/
```

### C#

```csharp
public class Checkout {

    public Checkout() {
        
    }
    
    public int Get_max() {
        
    }
    
    public void Add(int value) {
        
    }
    
    public int Remove() {
        
    }
}

/**
 * Your Checkout object will be instantiated and called as such:
 * Checkout obj = new Checkout();
 * int param_1 = obj.Get_max();
 * obj.Add(value);
 * int param_3 = obj.Remove();
 */
```

### JavaScript

```javascript

var Checkout = function() {
    
};

/**
 * @return {number}
 */
Checkout.prototype.get_max = function() {
    
};

/** 
 * @param {number} value
 * @return {void}
 */
Checkout.prototype.add = function(value) {
    
};

/**
 * @return {number}
 */
Checkout.prototype.remove = function() {
    
};

/** 
 * Your Checkout object will be instantiated and called as such:
 * var obj = new Checkout()
 * var param_1 = obj.get_max()
 * obj.add(value)
 * var param_3 = obj.remove()
 */
```

### TypeScript

```typescript
class Checkout {
    constructor() {
        
    }

    get_max(): number {
        
    }

    add(value: number): void {
        
    }

    remove(): number {
        
    }
}

/**
 * Your Checkout object will be instantiated and called as such:
 * var obj = new Checkout()
 * var param_1 = obj.get_max()
 * obj.add(value)
 * var param_3 = obj.remove()
 */
```

### PHP

```php
class Checkout {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @return Integer
     */
    function get_max() {
        
    }
  
    /**
     * @param Integer $value
     * @return NULL
     */
    function add($value) {
        
    }
  
    /**
     * @return Integer
     */
    function remove() {
        
    }
}

/**
 * Your Checkout object will be instantiated and called as such:
 * $obj = Checkout();
 * $ret_1 = $obj->get_max();
 * $obj->add($value);
 * $ret_3 = $obj->remove();
 */
```

### Swift

```swift

class Checkout {

    init() {
        
    }
    
    func get_max() -> Int {
        
    }
    
    func add(_ value: Int) {
        
    }
    
    func remove() -> Int {
        
    }
}

/**
 * Your Checkout object will be instantiated and called as such:
 * let obj = Checkout()
 * let ret_1: Int = obj.get_max()
 * obj.add(value)
 * let ret_3: Int = obj.remove()
 */
```

### Kotlin

```kotlin
class Checkout() {

    fun get_max(): Int {
        
    }

    fun add(value: Int) {
        
    }

    fun remove(): Int {
        
    }

}

/**
 * Your Checkout object will be instantiated and called as such:
 * var obj = Checkout()
 * var param_1 = obj.get_max()
 * obj.add(value)
 * var param_3 = obj.remove()
 */
```

### Dart

```dart
class Checkout {

  Checkout() {
    
  }
  
  int get_max() {
    
  }
  
  void add(int value) {
    
  }
  
  int remove() {
    
  }
}

/**
 * Your Checkout object will be instantiated and called as such:
 * Checkout obj = Checkout();
 * int param1 = obj.get_max();
 * obj.add(value);
 * int param3 = obj.remove();
 */
```

### Go

```golang
type Checkout struct {
    
}


func Constructor() Checkout {
    
}


func (this *Checkout) Get_max() int {
    
}


func (this *Checkout) Add(value int)  {
    
}


func (this *Checkout) Remove() int {
    
}


/**
 * Your Checkout object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get_max();
 * obj.Add(value);
 * param_3 := obj.Remove();
 */
```

### Ruby

```ruby
class Checkout
    def initialize()
        
    end


=begin
    :rtype: Integer
=end
    def get_max()
        
    end


=begin
    :type value: Integer
    :rtype: Void
=end
    def add(value)
        
    end


=begin
    :rtype: Integer
=end
    def remove()
        
    end


end

# Your Checkout object will be instantiated and called as such:
# obj = Checkout.new()
# param_1 = obj.get_max()
# obj.add(value)
# param_3 = obj.remove()
```

### Scala

```scala
class Checkout() {

    def get_max(): Int = {
        
    }

    def add(value: Int): Unit = {
        
    }

    def remove(): Int = {
        
    }

}

/**
 * Your Checkout object will be instantiated and called as such:
 * val obj = new Checkout()
 * val param_1 = obj.get_max()
 * obj.add(value)
 * val param_3 = obj.remove()
 */
```

### Rust

```rust
struct Checkout {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Checkout {

    fn new() -> Self {
        
    }
    
    fn get_max(&self) -> i32 {
        
    }
    
    fn add(&self, value: i32) {
        
    }
    
    fn remove(&self) -> i32 {
        
    }
}

/**
 * Your Checkout object will be instantiated and called as such:
 * let obj = Checkout::new();
 * let ret_1: i32 = obj.get_max();
 * obj.add(value);
 * let ret_3: i32 = obj.remove();
 */
```

### Racket

```racket
(define checkout%
  (class object%
    (super-new)
    
    (init-field)
    
    ; get_max : -> exact-integer?
    (define/public (get_max)
      )
    ; add : exact-integer? -> void?
    (define/public (add value)
      )
    ; remove : -> exact-integer?
    (define/public (remove)
      )))

;; Your checkout% object will be instantiated and called as such:
;; (define obj (new checkout%))
;; (define param_1 (send obj get_max))
;; (send obj add value)
;; (define param_3 (send obj remove))
```

### Erlang

```erlang
-spec checkout_init_() -> any().
checkout_init_() ->
  .

-spec checkout_get_max() -> integer().
checkout_get_max() ->
  .

-spec checkout_add(Value :: integer()) -> any().
checkout_add(Value) ->
  .

-spec checkout_remove() -> integer().
checkout_remove() ->
  .


%% Your functions will be called as such:
%% checkout_init_(),
%% Param_1 = checkout_get_max(),
%% checkout_add(Value),
%% Param_3 = checkout_remove(),

%% checkout_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Checkout do
  @spec init_() :: any
  def init_() do
    
  end

  @spec get_max() :: integer
  def get_max() do
    
  end

  @spec add(value :: integer) :: any
  def add(value) do
    
  end

  @spec remove() :: integer
  def remove() do
    
  end
end

# Your functions will be called as such:
# Checkout.init_()
# param_1 = Checkout.get_max()
# Checkout.add(value)
# param_3 = Checkout.remove()

# Checkout.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Checkout {
    init() {

    }
    
    func get_max(): Int64 {

    }
    
    func add(value: Int64): Unit {

    }
    
    func remove(): Int64 {

    }
}

/**
 * Your Checkout object will be instantiated and called as such:
 * let obj: Checkout = Checkout()
 * let param_1 = obj.get_max()
 * obj.add(value)
 * let param_3 = obj.remove()
 */
```

