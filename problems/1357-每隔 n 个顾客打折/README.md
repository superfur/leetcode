# 1357. 每隔 n 个顾客打折

## 题目描述

<p>超市里正在举行打折活动，每隔&nbsp;<code>n</code>&nbsp;个顾客会得到 <code>discount</code>&nbsp;的折扣。</p>

<p>超市里有一些商品，第&nbsp;<code>i</code>&nbsp;种商品为&nbsp;<code>products[i]</code>&nbsp;且每件单品的价格为&nbsp;<code>prices[i]</code>&nbsp;。</p>

<p>结账系统会统计顾客的数目，每隔&nbsp;<code>n</code>&nbsp;个顾客结账时，该顾客的账单都会打折，折扣为&nbsp;<code>discount</code>&nbsp;（也就是如果原本账单为&nbsp;<code>x</code>&nbsp;，那么实际金额会变成&nbsp;<code>x - (discount * x) / 100</code>&nbsp;），然后系统会重新开始计数。</p>

<p>顾客会购买一些商品，&nbsp;<code>product[i]</code>&nbsp;是顾客购买的第&nbsp;<code>i</code>&nbsp;种商品，&nbsp;<code>amount[i]</code>&nbsp;是对应的购买该种商品的数目。</p>

<p>请你实现&nbsp;<code>Cashier</code>&nbsp;类：</p>

<ul>
	<li><code>Cashier(int n, int discount, int[] products, int[] prices)</code>&nbsp;初始化实例对象，参数分别为打折频率&nbsp;<code>n</code>&nbsp;，折扣大小 <code>discount</code>&nbsp;，超市里的商品列表 <code>products</code>&nbsp;和它们的价格 <code>prices</code>&nbsp;。</li>
	<li><code>double&nbsp;getBill(int[] product, int[] amount)</code>&nbsp;返回账单的实际金额（如果有打折，请返回打折后的结果）。返回结果与标准答案误差在&nbsp;<code>10^-5</code>&nbsp;以内都视为正确结果。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入</strong>
[&quot;Cashier&quot;,&quot;getBill&quot;,&quot;getBill&quot;,&quot;getBill&quot;,&quot;getBill&quot;,&quot;getBill&quot;,&quot;getBill&quot;,&quot;getBill&quot;]
[[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]
<strong>输出</strong>
[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]
<strong>解释</strong>
Cashier cashier = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
cashier.getBill([1,2],[1,2]);                        // 返回 500.0, 账单金额为 = 1 * 100 + 2 * 200 = 500.
cashier.getBill([3,7],[10,10]);                      // 返回 4000.0
cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]);    // 返回 800.0 ，账单原本为 1600.0 ，但由于该顾客是第三位顾客，他将得到 50% 的折扣，所以实际金额为 1600 - 1600 * (50 / 100) = 800 。
cashier.getBill([4],[10]);                           // 返回 4000.0
cashier.getBill([7,3],[10,10]);                      // 返回 4000.0
cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]); // 返回 7350.0 ，账单原本为 14700.0 ，但由于系统计数再次达到三，该顾客将得到 50% 的折扣，实际金额为 7350.0 。
cashier.getBill([2,3,5],[5,3,2]);                    // 返回 2500.0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^4</code></li>
	<li><code>0 &lt;= discount &lt;= 100</code></li>
	<li><code>1 &lt;= products.length &lt;= 200</code></li>
	<li><code>1 &lt;= products[i] &lt;= 200</code></li>
	<li><code>products</code>&nbsp;列表中&nbsp;<strong>不会</strong>&nbsp;有重复的元素。</li>
	<li><code>prices.length == products.length</code></li>
	<li><code>1 &lt;= prices[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= product.length &lt;= products.length</code></li>
	<li><code>product[i]</code>&nbsp;在&nbsp;<code>products</code>&nbsp;出现过。</li>
	<li><code>amount.length == product.length</code></li>
	<li><code>1 &lt;= amount[i] &lt;= 1000</code></li>
	<li>最多有&nbsp;<code>1000</code> 次对&nbsp;<code>getBill</code>&nbsp;函数的调用。</li>
	<li>返回结果与标准答案误差在&nbsp;<code>10^-5</code>&nbsp;以内都视为正确结果。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 哈希表

## 提示

1. Keep track of the count of the customers.
2. Check if the count of the customers is divisible by n then apply the discount formula.

## 示例

```
["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
[[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]
```

## 示例代码

### C++

```cpp
class Cashier {
public:
    Cashier(int n, int discount, vector<int>& products, vector<int>& prices) {
        
    }
    
    double getBill(vector<int> product, vector<int> amount) {
        
    }
};

/**
 * Your Cashier object will be instantiated and called as such:
 * Cashier* obj = new Cashier(n, discount, products, prices);
 * double param_1 = obj->getBill(product,amount);
 */
```

### Java

```java
class Cashier {

    public Cashier(int n, int discount, int[] products, int[] prices) {
        
    }
    
    public double getBill(int[] product, int[] amount) {
        
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * Cashier obj = new Cashier(n, discount, products, prices);
 * double param_1 = obj.getBill(product,amount);
 */
```

### Python

```python
class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
```

### Python3

```python3
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
```

### C

```c



typedef struct {
    
} Cashier;


Cashier* cashierCreate(int n, int discount, int* products, int productsSize, int* prices, int pricesSize) {
    
}

double cashierGetBill(Cashier* obj, int* product, int productSize, int* amount, int amountSize) {
    
}

void cashierFree(Cashier* obj) {
    
}

/**
 * Your Cashier struct will be instantiated and called as such:
 * Cashier* obj = cashierCreate(n, discount, products, productsSize, prices, pricesSize);
 * double param_1 = cashierGetBill(obj, product, productSize, amount, amountSize);
 
 * cashierFree(obj);
*/
```

### C#

```csharp
public class Cashier {

    public Cashier(int n, int discount, int[] products, int[] prices) {
        
    }
    
    public double GetBill(int[] product, int[] amount) {
        
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * Cashier obj = new Cashier(n, discount, products, prices);
 * double param_1 = obj.GetBill(product,amount);
 */
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} discount
 * @param {number[]} products
 * @param {number[]} prices
 */
var Cashier = function(n, discount, products, prices) {
    
};

/** 
 * @param {number[]} product 
 * @param {number[]} amount
 * @return {number}
 */
Cashier.prototype.getBill = function(product, amount) {
    
};

/** 
 * Your Cashier object will be instantiated and called as such:
 * var obj = new Cashier(n, discount, products, prices)
 * var param_1 = obj.getBill(product,amount)
 */
```

### TypeScript

```typescript
class Cashier {
    constructor(n: number, discount: number, products: number[], prices: number[]) {
        
    }

    getBill(product: number[], amount: number[]): number {
        
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * var obj = new Cashier(n, discount, products, prices)
 * var param_1 = obj.getBill(product,amount)
 */
```

### PHP

```php
class Cashier {
    /**
     * @param Integer $n
     * @param Integer $discount
     * @param Integer[] $products
     * @param Integer[] $prices
     */
    function __construct($n, $discount, $products, $prices) {
        
    }
  
    /**
     * @param Integer[] $product
     * @param Integer[] $amount
     * @return Float
     */
    function getBill($product, $amount) {
        
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * $obj = Cashier($n, $discount, $products, $prices);
 * $ret_1 = $obj->getBill($product, $amount);
 */
```

### Swift

```swift

class Cashier {

    init(_ n: Int, _ discount: Int, _ products: [Int], _ prices: [Int]) {
        
    }
    
    func getBill(_ product: [Int], _ amount: [Int]) -> Double {
        
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * let obj = Cashier(n, discount, products, prices)
 * let ret_1: Double = obj.getBill(product, amount)
 */
```

### Kotlin

```kotlin
class Cashier(n: Int, discount: Int, products: IntArray, prices: IntArray) {

    fun getBill(product: IntArray, amount: IntArray): Double {
        
    }

}

/**
 * Your Cashier object will be instantiated and called as such:
 * var obj = Cashier(n, discount, products, prices)
 * var param_1 = obj.getBill(product,amount)
 */
```

### Dart

```dart
class Cashier {

  Cashier(int n, int discount, List<int> products, List<int> prices) {
    
  }
  
  double getBill(List<int> product, List<int> amount) {
    
  }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * Cashier obj = Cashier(n, discount, products, prices);
 * double param1 = obj.getBill(product,amount);
 */
```

### Go

```golang
type Cashier struct {
    
}


func Constructor(n int, discount int, products []int, prices []int) Cashier {
    
}


func (this *Cashier) GetBill(product []int, amount []int) float64 {
    
}


/**
 * Your Cashier object will be instantiated and called as such:
 * obj := Constructor(n, discount, products, prices);
 * param_1 := obj.GetBill(product,amount);
 */
```

### Ruby

```ruby
class Cashier

=begin
    :type n: Integer
    :type discount: Integer
    :type products: Integer[]
    :type prices: Integer[]
=end
    def initialize(n, discount, products, prices)
        
    end


=begin
    :type product: Integer[]
    :type amount: Integer[]
    :rtype: Float
=end
    def get_bill(product, amount)
        
    end


end

# Your Cashier object will be instantiated and called as such:
# obj = Cashier.new(n, discount, products, prices)
# param_1 = obj.get_bill(product, amount)
```

### Scala

```scala
class Cashier(_n: Int, _discount: Int, _products: Array[Int], _prices: Array[Int]) {

    def getBill(product: Array[Int], amount: Array[Int]): Double = {
        
    }

}

/**
 * Your Cashier object will be instantiated and called as such:
 * val obj = new Cashier(n, discount, products, prices)
 * val param_1 = obj.getBill(product,amount)
 */
```

### Rust

```rust
struct Cashier {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Cashier {

    fn new(n: i32, discount: i32, products: Vec<i32>, prices: Vec<i32>) -> Self {
        
    }
    
    fn get_bill(&self, product: Vec<i32>, amount: Vec<i32>) -> f64 {
        
    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * let obj = Cashier::new(n, discount, products, prices);
 * let ret_1: f64 = obj.get_bill(product, amount);
 */
```

### Racket

```racket
(define cashier%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    ; discount : exact-integer?
    ; products : (listof exact-integer?)
    ; prices : (listof exact-integer?)
    (init-field
      n
      discount
      products
      prices)
    
    ; get-bill : (listof exact-integer?) (listof exact-integer?) -> flonum?
    (define/public (get-bill product amount)
      )))

;; Your cashier% object will be instantiated and called as such:
;; (define obj (new cashier% [n n] [discount discount] [products products] [prices prices]))
;; (define param_1 (send obj get-bill product amount))
```

### Erlang

```erlang
-spec cashier_init_(N :: integer(), Discount :: integer(), Products :: [integer()], Prices :: [integer()]) -> any().
cashier_init_(N, Discount, Products, Prices) ->
  .

-spec cashier_get_bill(Product :: [integer()], Amount :: [integer()]) -> float().
cashier_get_bill(Product, Amount) ->
  .


%% Your functions will be called as such:
%% cashier_init_(N, Discount, Products, Prices),
%% Param_1 = cashier_get_bill(Product, Amount),

%% cashier_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Cashier do
  @spec init_(n :: integer, discount :: integer, products :: [integer], prices :: [integer]) :: any
  def init_(n, discount, products, prices) do
    
  end

  @spec get_bill(product :: [integer], amount :: [integer]) :: float
  def get_bill(product, amount) do
    
  end
end

# Your functions will be called as such:
# Cashier.init_(n, discount, products, prices)
# param_1 = Cashier.get_bill(product, amount)

# Cashier.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Cashier {
    init(n: Int64, discount: Int64, products: Array<Int64>, prices: Array<Int64>) {

    }
    
    func getBill(product: Array<Int64>, amount: Array<Int64>): Float64 {

    }
}

/**
 * Your Cashier object will be instantiated and called as such:
 * let obj: Cashier = Cashier(n, discount, products, prices)
 * let param_1 = obj.getBill(product,amount)
 */
```

