# 1352. 最后 K 个数的乘积

## 题目描述

<p>设计一个算法，该算法接受一个整数流并检索该流中最后 <code>k</code> 个整数的乘积。</p>

<p>实现&nbsp;<code>ProductOfNumbers</code>&nbsp;类：</p>

<ul>
	<li><code>ProductOfNumbers()</code>&nbsp;用一个空的流初始化对象。</li>
	<li><code>void add(int num)</code>&nbsp;将数字&nbsp;<code>num</code>&nbsp;添加到当前数字列表的最后面。</li>
	<li><code>int getProduct(int k)</code>&nbsp;返回当前数字列表中，最后&nbsp;<code>k</code>&nbsp;个数字的乘积。你可以假设当前列表中始终 <strong>至少</strong> 包含 <code>k</code> 个数字。</li>
</ul>

<p>题目数据保证：任何时候，任一连续数字序列的乘积都在 32 位整数范围内，不会溢出。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

<strong>输出：</strong>
[null,null,null,null,null,null,20,40,0,null,32]

<strong>解释：</strong>
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // 返回 20 。最后 2 个数字的乘积是 5 * 4 = 20
productOfNumbers.getProduct(3); // 返回 40 。最后 3 个数字的乘积是 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // 返回  0 。最后 4 个数字的乘积是 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // 返回 32 。最后 2 个数字的乘积是 4 * 8 = 32 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= num&nbsp;&lt;=&nbsp;100</code></li>
	<li><code>1 &lt;= k &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>add</code> 和 <code>getProduct</code>&nbsp;最多被调用&nbsp;<code>4 * 10<sup>4</sup></code> 次。</li>
	<li>在任何时间点流的乘积都在 32 位整数范围内。</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>您能否 <strong>同时</strong> 将 <code>GetProduct</code> 和 <code>Add</code> 的实现改为 <code>O(1)</code> 时间复杂度，而不是 <code>O(k)</code> 时间复杂度？</p>


## 难度

Medium

## 标签

- 设计
- 数组
- 数学
- 数据流
- 前缀和

## 提示

1. Keep all prefix products of numbers in an array, then calculate the product of last K elements in O(1) complexity.
2. When a zero number is added, clean the array of prefix products.

## 示例

```
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
```

## 示例代码

### C++

```cpp
class ProductOfNumbers {
public:
    ProductOfNumbers() {
        
    }
    
    void add(int num) {
        
    }
    
    int getProduct(int k) {
        
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */
```

### Java

```java
class ProductOfNumbers {

    public ProductOfNumbers() {
        
    }
    
    public void add(int num) {
        
    }
    
    public int getProduct(int k) {
        
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */
```

### Python

```python
class ProductOfNumbers(object):

    def __init__(self):
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
```

### Python3

```python3
class ProductOfNumbers:

    def __init__(self):
        

    def add(self, num: int) -> None:
        

    def getProduct(self, k: int) -> int:
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
```

### C

```c



typedef struct {
    
} ProductOfNumbers;


ProductOfNumbers* productOfNumbersCreate() {
    
}

void productOfNumbersAdd(ProductOfNumbers* obj, int num) {
    
}

int productOfNumbersGetProduct(ProductOfNumbers* obj, int k) {
    
}

void productOfNumbersFree(ProductOfNumbers* obj) {
    
}

/**
 * Your ProductOfNumbers struct will be instantiated and called as such:
 * ProductOfNumbers* obj = productOfNumbersCreate();
 * productOfNumbersAdd(obj, num);
 
 * int param_2 = productOfNumbersGetProduct(obj, k);
 
 * productOfNumbersFree(obj);
*/
```

### C#

```csharp
public class ProductOfNumbers {

    public ProductOfNumbers() {
        
    }
    
    public void Add(int num) {
        
    }
    
    public int GetProduct(int k) {
        
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.Add(num);
 * int param_2 = obj.GetProduct(k);
 */
```

### JavaScript

```javascript

var ProductOfNumbers = function() {
    
};

/** 
 * @param {number} num
 * @return {void}
 */
ProductOfNumbers.prototype.add = function(num) {
    
};

/** 
 * @param {number} k
 * @return {number}
 */
ProductOfNumbers.prototype.getProduct = function(k) {
    
};

/** 
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = new ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */
```

### TypeScript

```typescript
class ProductOfNumbers {
    constructor() {
        
    }

    add(num: number): void {
        
    }

    getProduct(k: number): number {
        
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = new ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */
```

### PHP

```php
class ProductOfNumbers {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $num
     * @return NULL
     */
    function add($num) {
        
    }
  
    /**
     * @param Integer $k
     * @return Integer
     */
    function getProduct($k) {
        
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * $obj = ProductOfNumbers();
 * $obj->add($num);
 * $ret_2 = $obj->getProduct($k);
 */
```

### Swift

```swift

class ProductOfNumbers {

    init() {
        
    }
    
    func add(_ num: Int) {
        
    }
    
    func getProduct(_ k: Int) -> Int {
        
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * let obj = ProductOfNumbers()
 * obj.add(num)
 * let ret_2: Int = obj.getProduct(k)
 */
```

### Kotlin

```kotlin
class ProductOfNumbers() {

    fun add(num: Int) {
        
    }

    fun getProduct(k: Int): Int {
        
    }

}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */
```

### Dart

```dart
class ProductOfNumbers {

  ProductOfNumbers() {
    
  }
  
  void add(int num) {
    
  }
  
  int getProduct(int k) {
    
  }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = ProductOfNumbers();
 * obj.add(num);
 * int param2 = obj.getProduct(k);
 */
```

### Go

```golang
type ProductOfNumbers struct {
    
}


func Constructor() ProductOfNumbers {
    
}


func (this *ProductOfNumbers) Add(num int)  {
    
}


func (this *ProductOfNumbers) GetProduct(k int) int {
    
}


/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(num);
 * param_2 := obj.GetProduct(k);
 */
```

### Ruby

```ruby
class ProductOfNumbers
    def initialize()
        
    end


=begin
    :type num: Integer
    :rtype: Void
=end
    def add(num)
        
    end


=begin
    :type k: Integer
    :rtype: Integer
=end
    def get_product(k)
        
    end


end

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers.new()
# obj.add(num)
# param_2 = obj.get_product(k)
```

### Scala

```scala
class ProductOfNumbers() {

    def add(num: Int): Unit = {
        
    }

    def getProduct(k: Int): Int = {
        
    }

}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * val obj = new ProductOfNumbers()
 * obj.add(num)
 * val param_2 = obj.getProduct(k)
 */
```

### Rust

```rust
struct ProductOfNumbers {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ProductOfNumbers {

    fn new() -> Self {
        
    }
    
    fn add(&self, num: i32) {
        
    }
    
    fn get_product(&self, k: i32) -> i32 {
        
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * let obj = ProductOfNumbers::new();
 * obj.add(num);
 * let ret_2: i32 = obj.get_product(k);
 */
```

### Racket

```racket
(define product-of-numbers%
  (class object%
    (super-new)
    
    (init-field)
    
    ; add : exact-integer? -> void?
    (define/public (add num)
      )
    ; get-product : exact-integer? -> exact-integer?
    (define/public (get-product k)
      )))

;; Your product-of-numbers% object will be instantiated and called as such:
;; (define obj (new product-of-numbers%))
;; (send obj add num)
;; (define param_2 (send obj get-product k))
```

### Erlang

```erlang
-spec product_of_numbers_init_() -> any().
product_of_numbers_init_() ->
  .

-spec product_of_numbers_add(Num :: integer()) -> any().
product_of_numbers_add(Num) ->
  .

-spec product_of_numbers_get_product(K :: integer()) -> integer().
product_of_numbers_get_product(K) ->
  .


%% Your functions will be called as such:
%% product_of_numbers_init_(),
%% product_of_numbers_add(Num),
%% Param_2 = product_of_numbers_get_product(K),

%% product_of_numbers_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule ProductOfNumbers do
  @spec init_() :: any
  def init_() do
    
  end

  @spec add(num :: integer) :: any
  def add(num) do
    
  end

  @spec get_product(k :: integer) :: integer
  def get_product(k) do
    
  end
end

# Your functions will be called as such:
# ProductOfNumbers.init_()
# ProductOfNumbers.add(num)
# param_2 = ProductOfNumbers.get_product(k)

# ProductOfNumbers.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class ProductOfNumbers {
    init() {

    }
    
    func add(num: Int64): Unit {

    }
    
    func getProduct(k: Int64): Int64 {

    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * let obj: ProductOfNumbers = ProductOfNumbers()
 * obj.add(num)
 * let param_2 = obj.getProduct(k)
 */
```

