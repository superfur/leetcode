# 面试题 16.09. 运算

## 题目描述

<p>请实现整数数字的乘法、减法和除法运算，运算结果均为整数数字，程序中只允许使用加法运算符和逻辑运算符，允许程序中出现正负常数，不允许使用位运算。</p>
<p>你的实现应该支持如下操作：</p>
<ul>
<li><code>Operations()</code> 构造函数</li>
<li><code>minus(a, b)</code> 减法，返回<code>a - b</code></li>
<li><code>multiply(a, b)</code> 乘法，返回<code>a * b</code></li>
<li><code>divide(a, b)</code> 除法，返回<code>a / b</code></li>
</ul>
<p><strong>示例：</strong></p>
<pre>Operations operations = new Operations();
operations.minus(1, 2); //返回-1
operations.multiply(3, 4); //返回12
operations.divide(5, -2); //返回-2
</pre>
<p><strong>提示：</strong></p>
<ul>
<li>你可以假设函数输入一定是有效的，例如不会出现除法分母为0的情况</li>
<li>单个用例的函数调用次数不会超过1000次</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数学

## 提示

1. 从减法开始，逐步解决。一旦完成了一个函数，你可以用它来实现其他函数。
2. 减法：取负函数（将正整数转换为负数）有用吗？你可以使用加法操作符来实现吗?
3. 当a > b时，a – b > 0。你能得到a – b的符号位吗？
4. 你考虑过如何处理a – b中的整数溢出吗？

## 示例

```
["Operations","minus","minus","multiply","multiply","divide","divide"]
[[],[0,-2147483647],[-1,2147483647],[-1,-2147483647],[-100,21474836],[2147483647,-1],[-2147483648,1]]
```

## 示例代码

### C++

```cpp
class Operations {
public:
    Operations() {
        
    }
    
    int minus(int a, int b) {
        
    }
    
    int multiply(int a, int b) {
        
    }
    
    int divide(int a, int b) {
        
    }
};

/**
 * Your Operations object will be instantiated and called as such:
 * Operations* obj = new Operations();
 * int param_1 = obj->minus(a,b);
 * int param_2 = obj->multiply(a,b);
 * int param_3 = obj->divide(a,b);
 */
```

### Java

```java
class Operations {

    public Operations() {
        
    }
    
    public int minus(int a, int b) {
        
    }
    
    public int multiply(int a, int b) {
        
    }
    
    public int divide(int a, int b) {
        
    }
}

/**
 * Your Operations object will be instantiated and called as such:
 * Operations obj = new Operations();
 * int param_1 = obj.minus(a,b);
 * int param_2 = obj.multiply(a,b);
 * int param_3 = obj.divide(a,b);
 */
```

### Python

```python
class Operations(object):

    def __init__(self):
        

    def minus(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        

    def multiply(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        

    def divide(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        


# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)
```

### Python3

```python3
class Operations:

    def __init__(self):
        

    def minus(self, a: int, b: int) -> int:
        

    def multiply(self, a: int, b: int) -> int:
        

    def divide(self, a: int, b: int) -> int:
        


# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)
```

### C

```c



typedef struct {
    
} Operations;


Operations* operationsCreate() {
    
}

int operationsMinus(Operations* obj, int a, int b) {
    
}

int operationsMultiply(Operations* obj, int a, int b) {
    
}

int operationsDivide(Operations* obj, int a, int b) {
    
}

void operationsFree(Operations* obj) {
    
}

/**
 * Your Operations struct will be instantiated and called as such:
 * Operations* obj = operationsCreate();
 * int param_1 = operationsMinus(obj, a, b);
 
 * int param_2 = operationsMultiply(obj, a, b);
 
 * int param_3 = operationsDivide(obj, a, b);
 
 * operationsFree(obj);
*/
```

### C#

```csharp
public class Operations {

    public Operations() {
        
    }
    
    public int Minus(int a, int b) {
        
    }
    
    public int Multiply(int a, int b) {
        
    }
    
    public int Divide(int a, int b) {
        
    }
}

/**
 * Your Operations object will be instantiated and called as such:
 * Operations obj = new Operations();
 * int param_1 = obj.Minus(a,b);
 * int param_2 = obj.Multiply(a,b);
 * int param_3 = obj.Divide(a,b);
 */
```

### JavaScript

```javascript

var Operations = function() {
    
};

/** 
 * @param {number} a 
 * @param {number} b
 * @return {number}
 */
Operations.prototype.minus = function(a, b) {
    
};

/** 
 * @param {number} a 
 * @param {number} b
 * @return {number}
 */
Operations.prototype.multiply = function(a, b) {
    
};

/** 
 * @param {number} a 
 * @param {number} b
 * @return {number}
 */
Operations.prototype.divide = function(a, b) {
    
};

/** 
 * Your Operations object will be instantiated and called as such:
 * var obj = new Operations()
 * var param_1 = obj.minus(a,b)
 * var param_2 = obj.multiply(a,b)
 * var param_3 = obj.divide(a,b)
 */
```

### TypeScript

```typescript
class Operations {
    constructor() {
        
    }

    minus(a: number, b: number): number {
        
    }

    multiply(a: number, b: number): number {
        
    }

    divide(a: number, b: number): number {
        
    }
}

/**
 * Your Operations object will be instantiated and called as such:
 * var obj = new Operations()
 * var param_1 = obj.minus(a,b)
 * var param_2 = obj.multiply(a,b)
 * var param_3 = obj.divide(a,b)
 */
```

### PHP

```php
class Operations {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $a
     * @param Integer $b
     * @return Integer
     */
    function minus($a, $b) {
        
    }
  
    /**
     * @param Integer $a
     * @param Integer $b
     * @return Integer
     */
    function multiply($a, $b) {
        
    }
  
    /**
     * @param Integer $a
     * @param Integer $b
     * @return Integer
     */
    function divide($a, $b) {
        
    }
}

/**
 * Your Operations object will be instantiated and called as such:
 * $obj = Operations();
 * $ret_1 = $obj->minus($a, $b);
 * $ret_2 = $obj->multiply($a, $b);
 * $ret_3 = $obj->divide($a, $b);
 */
```

### Swift

```swift

class Operations {

    init() {
        
    }
    
    func minus(_ a: Int, _ b: Int) -> Int {
        
    }
    
    func multiply(_ a: Int, _ b: Int) -> Int {
        
    }
    
    func divide(_ a: Int, _ b: Int) -> Int {
        
    }
}

/**
 * Your Operations object will be instantiated and called as such:
 * let obj = Operations()
 * let ret_1: Int = obj.minus(a, b)
 * let ret_2: Int = obj.multiply(a, b)
 * let ret_3: Int = obj.divide(a, b)
 */
```

### Kotlin

```kotlin
class Operations() {

    fun minus(a: Int, b: Int): Int {
        
    }

    fun multiply(a: Int, b: Int): Int {
        
    }

    fun divide(a: Int, b: Int): Int {
        
    }

}

/**
 * Your Operations object will be instantiated and called as such:
 * var obj = Operations()
 * var param_1 = obj.minus(a,b)
 * var param_2 = obj.multiply(a,b)
 * var param_3 = obj.divide(a,b)
 */
```

### Dart

```dart
class Operations {

  Operations() {
    
  }
  
  int minus(int a, int b) {
    
  }
  
  int multiply(int a, int b) {
    
  }
  
  int divide(int a, int b) {
    
  }
}

/**
 * Your Operations object will be instantiated and called as such:
 * Operations obj = Operations();
 * int param1 = obj.minus(a,b);
 * int param2 = obj.multiply(a,b);
 * int param3 = obj.divide(a,b);
 */
```

### Go

```golang
type Operations struct {
    
}


func Constructor() Operations {
    
}


func (this *Operations) Minus(a int, b int) int {
    
}


func (this *Operations) Multiply(a int, b int) int {
    
}


func (this *Operations) Divide(a int, b int) int {
    
}


/**
 * Your Operations object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Minus(a,b);
 * param_2 := obj.Multiply(a,b);
 * param_3 := obj.Divide(a,b);
 */
```

### Ruby

```ruby
class Operations
    def initialize()
        
    end


=begin
    :type a: Integer
    :type b: Integer
    :rtype: Integer
=end
    def minus(a, b)
        
    end


=begin
    :type a: Integer
    :type b: Integer
    :rtype: Integer
=end
    def multiply(a, b)
        
    end


=begin
    :type a: Integer
    :type b: Integer
    :rtype: Integer
=end
    def divide(a, b)
        
    end


end

# Your Operations object will be instantiated and called as such:
# obj = Operations.new()
# param_1 = obj.minus(a, b)
# param_2 = obj.multiply(a, b)
# param_3 = obj.divide(a, b)
```

### Scala

```scala
class Operations() {

    def minus(a: Int, b: Int): Int = {
        
    }

    def multiply(a: Int, b: Int): Int = {
        
    }

    def divide(a: Int, b: Int): Int = {
        
    }

}

/**
 * Your Operations object will be instantiated and called as such:
 * val obj = new Operations()
 * val param_1 = obj.minus(a,b)
 * val param_2 = obj.multiply(a,b)
 * val param_3 = obj.divide(a,b)
 */
```

### Rust

```rust
struct Operations {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Operations {

    fn new() -> Self {
        
    }
    
    fn minus(&self, a: i32, b: i32) -> i32 {
        
    }
    
    fn multiply(&self, a: i32, b: i32) -> i32 {
        
    }
    
    fn divide(&self, a: i32, b: i32) -> i32 {
        
    }
}

/**
 * Your Operations object will be instantiated and called as such:
 * let obj = Operations::new();
 * let ret_1: i32 = obj.minus(a, b);
 * let ret_2: i32 = obj.multiply(a, b);
 * let ret_3: i32 = obj.divide(a, b);
 */
```

### Racket

```racket
(define operations%
  (class object%
    (super-new)
    
    (init-field)
    
    ; minus : exact-integer? exact-integer? -> exact-integer?
    (define/public (minus a b)
      )
    ; multiply : exact-integer? exact-integer? -> exact-integer?
    (define/public (multiply a b)
      )
    ; divide : exact-integer? exact-integer? -> exact-integer?
    (define/public (divide a b)
      )))

;; Your operations% object will be instantiated and called as such:
;; (define obj (new operations%))
;; (define param_1 (send obj minus a b))
;; (define param_2 (send obj multiply a b))
;; (define param_3 (send obj divide a b))
```

### Erlang

```erlang
-spec operations_init_() -> any().
operations_init_() ->
  .

-spec operations_minus(A :: integer(), B :: integer()) -> integer().
operations_minus(A, B) ->
  .

-spec operations_multiply(A :: integer(), B :: integer()) -> integer().
operations_multiply(A, B) ->
  .

-spec operations_divide(A :: integer(), B :: integer()) -> integer().
operations_divide(A, B) ->
  .


%% Your functions will be called as such:
%% operations_init_(),
%% Param_1 = operations_minus(A, B),
%% Param_2 = operations_multiply(A, B),
%% Param_3 = operations_divide(A, B),

%% operations_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Operations do
  @spec init_() :: any
  def init_() do
    
  end

  @spec minus(a :: integer, b :: integer) :: integer
  def minus(a, b) do
    
  end

  @spec multiply(a :: integer, b :: integer) :: integer
  def multiply(a, b) do
    
  end

  @spec divide(a :: integer, b :: integer) :: integer
  def divide(a, b) do
    
  end
end

# Your functions will be called as such:
# Operations.init_()
# param_1 = Operations.minus(a, b)
# param_2 = Operations.multiply(a, b)
# param_3 = Operations.divide(a, b)

# Operations.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Operations {
    init() {

    }
    
    func minus(a: Int64, b: Int64): Int64 {

    }
    
    func multiply(a: Int64, b: Int64): Int64 {

    }
    
    func divide(a: Int64, b: Int64): Int64 {

    }
}

/**
 * Your Operations object will be instantiated and called as such:
 * let obj: Operations = Operations()
 * let param_1 = obj.minus(a,b)
 * let param_2 = obj.multiply(a,b)
 * let param_3 = obj.divide(a,b)
 */
```

