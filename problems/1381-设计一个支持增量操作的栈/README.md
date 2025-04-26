# 1381. 设计一个支持增量操作的栈

## 题目描述

<p>请你设计一个支持对其元素进行增量操作的栈。</p>

<p>实现自定义栈类 <code>CustomStack</code> ：</p>

<ul>
	<li><code>CustomStack(int maxSize)</code>：用 <code>maxSize</code> 初始化对象，<code>maxSize</code> 是栈中最多能容纳的元素数量。</li>
	<li><code>void push(int x)</code>：如果栈还未增长到 <code>maxSize</code> ，就将 <code>x</code> 添加到栈顶。</li>
	<li><code>int pop()</code>：弹出栈顶元素，并返回栈顶的值，或栈为空时返回 <strong>-1</strong> 。</li>
	<li><code>void inc(int k, int val)</code>：栈底的 <code>k</code> 个元素的值都增加 <code>val</code> 。如果栈中元素总数小于 <code>k</code> ，则栈中的所有元素都增加 <code>val</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
<strong>输出：</strong>
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
<strong>解释：</strong>
CustomStack stk = new CustomStack(3); // 栈是空的 []
stk.push(1);                          // 栈变为 [1]
stk.push(2);                          // 栈变为 [1, 2]
stk.pop();                            // 返回 2 --&gt; 返回栈顶值 2，栈变为 [1]
stk.push(2);                          // 栈变为 [1, 2]
stk.push(3);                          // 栈变为 [1, 2, 3]
stk.push(4);                          // 栈仍然是 [1, 2, 3]，不能添加其他元素使栈大小变为 4
stk.increment(5, 100);                // 栈变为 [101, 102, 103]
stk.increment(2, 100);                // 栈变为 [201, 202, 103]
stk.pop();                            // 返回 103 --&gt; 返回栈顶值 103，栈变为 [201, 202]
stk.pop();                            // 返回 202 --&gt; 返回栈顶值 202，栈变为 [201]
stk.pop();                            // 返回 201 --&gt; 返回栈顶值 201，栈变为 []
stk.pop();                            // 返回 -1 --&gt; 栈为空，返回 -1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= maxSize, x, k &lt;= 1000</code></li>
	<li><code>0 &lt;= val &lt;= 100</code></li>
	<li>每种方法 <code>increment</code>，<code>push</code> 以及 <code>pop</code> 分别最多调用 <code>1000</code> 次</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 设计
- 数组

## 提示

1. Use an array to represent the stack. Push will add new integer to the array. Pop removes the last element in the array and increment will add val to the first k elements of the array.
2. This solution run in O(1) per push and pop and O(k) per increment.

## 示例

```
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
```

## 示例代码

### C++

```cpp
class CustomStack {
public:
    CustomStack(int maxSize) {
        
    }
    
    void push(int x) {
        
    }
    
    int pop() {
        
    }
    
    void increment(int k, int val) {
        
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
```

### Java

```java
class CustomStack {

    public CustomStack(int maxSize) {
        
    }
    
    public void push(int x) {
        
    }
    
    public int pop() {
        
    }
    
    public void increment(int k, int val) {
        
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */
```

### Python

```python
class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        """
        :rtype: int
        """
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
```

### Python3

```python3
class CustomStack:

    def __init__(self, maxSize: int):
        

    def push(self, x: int) -> None:
        

    def pop(self) -> int:
        

    def increment(self, k: int, val: int) -> None:
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
```

### C

```c



typedef struct {
    
} CustomStack;


CustomStack* customStackCreate(int maxSize) {
    
}

void customStackPush(CustomStack* obj, int x) {
    
}

int customStackPop(CustomStack* obj) {
    
}

void customStackIncrement(CustomStack* obj, int k, int val) {
    
}

void customStackFree(CustomStack* obj) {
    
}

/**
 * Your CustomStack struct will be instantiated and called as such:
 * CustomStack* obj = customStackCreate(maxSize);
 * customStackPush(obj, x);
 
 * int param_2 = customStackPop(obj);
 
 * customStackIncrement(obj, k, val);
 
 * customStackFree(obj);
*/
```

### C#

```csharp
public class CustomStack {

    public CustomStack(int maxSize) {
        
    }
    
    public void Push(int x) {
        
    }
    
    public int Pop() {
        
    }
    
    public void Increment(int k, int val) {
        
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * obj.Increment(k,val);
 */
```

### JavaScript

```javascript
/**
 * @param {number} maxSize
 */
var CustomStack = function(maxSize) {
    
};

/** 
 * @param {number} x
 * @return {void}
 */
CustomStack.prototype.push = function(x) {
    
};

/**
 * @return {number}
 */
CustomStack.prototype.pop = function() {
    
};

/** 
 * @param {number} k 
 * @param {number} val
 * @return {void}
 */
CustomStack.prototype.increment = function(k, val) {
    
};

/** 
 * Your CustomStack object will be instantiated and called as such:
 * var obj = new CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,val)
 */
```

### TypeScript

```typescript
class CustomStack {
    constructor(maxSize: number) {
        
    }

    push(x: number): void {
        
    }

    pop(): number {
        
    }

    increment(k: number, val: number): void {
        
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * var obj = new CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,val)
 */
```

### PHP

```php
class CustomStack {
    /**
     * @param Integer $maxSize
     */
    function __construct($maxSize) {
        
    }
  
    /**
     * @param Integer $x
     * @return NULL
     */
    function push($x) {
        
    }
  
    /**
     * @return Integer
     */
    function pop() {
        
    }
  
    /**
     * @param Integer $k
     * @param Integer $val
     * @return NULL
     */
    function increment($k, $val) {
        
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * $obj = CustomStack($maxSize);
 * $obj->push($x);
 * $ret_2 = $obj->pop();
 * $obj->increment($k, $val);
 */
```

### Swift

```swift

class CustomStack {

    init(_ maxSize: Int) {
        
    }
    
    func push(_ x: Int) {
        
    }
    
    func pop() -> Int {
        
    }
    
    func increment(_ k: Int, _ val: Int) {
        
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * let obj = CustomStack(maxSize)
 * obj.push(x)
 * let ret_2: Int = obj.pop()
 * obj.increment(k, val)
 */
```

### Kotlin

```kotlin
class CustomStack(maxSize: Int) {

    fun push(x: Int) {
        
    }

    fun pop(): Int {
        
    }

    fun increment(k: Int, `val`: Int) {
        
    }

}

/**
 * Your CustomStack object will be instantiated and called as such:
 * var obj = CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,`val`)
 */
```

### Dart

```dart
class CustomStack {

  CustomStack(int maxSize) {
    
  }
  
  void push(int x) {
    
  }
  
  int pop() {
    
  }
  
  void increment(int k, int val) {
    
  }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = CustomStack(maxSize);
 * obj.push(x);
 * int param2 = obj.pop();
 * obj.increment(k,val);
 */
```

### Go

```golang
type CustomStack struct {
    
}


func Constructor(maxSize int) CustomStack {
    
}


func (this *CustomStack) Push(x int)  {
    
}


func (this *CustomStack) Pop() int {
    
}


func (this *CustomStack) Increment(k int, val int)  {
    
}


/**
 * Your CustomStack object will be instantiated and called as such:
 * obj := Constructor(maxSize);
 * obj.Push(x);
 * param_2 := obj.Pop();
 * obj.Increment(k,val);
 */
```

### Ruby

```ruby
class CustomStack

=begin
    :type max_size: Integer
=end
    def initialize(max_size)
        
    end


=begin
    :type x: Integer
    :rtype: Void
=end
    def push(x)
        
    end


=begin
    :rtype: Integer
=end
    def pop()
        
    end


=begin
    :type k: Integer
    :type val: Integer
    :rtype: Void
=end
    def increment(k, val)
        
    end


end

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack.new(max_size)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k, val)
```

### Scala

```scala
class CustomStack(_maxSize: Int) {

    def push(x: Int): Unit = {
        
    }

    def pop(): Int = {
        
    }

    def increment(k: Int, `val`: Int): Unit = {
        
    }

}

/**
 * Your CustomStack object will be instantiated and called as such:
 * val obj = new CustomStack(maxSize)
 * obj.push(x)
 * val param_2 = obj.pop()
 * obj.increment(k,`val`)
 */
```

### Rust

```rust
struct CustomStack {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl CustomStack {

    fn new(maxSize: i32) -> Self {
        
    }
    
    fn push(&self, x: i32) {
        
    }
    
    fn pop(&self) -> i32 {
        
    }
    
    fn increment(&self, k: i32, val: i32) {
        
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * let obj = CustomStack::new(maxSize);
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * obj.increment(k, val);
 */
```

### Racket

```racket
(define custom-stack%
  (class object%
    (super-new)
    
    ; max-size : exact-integer?
    (init-field
      max-size)
    
    ; push : exact-integer? -> void?
    (define/public (push x)
      )
    ; pop : -> exact-integer?
    (define/public (pop)
      )
    ; increment : exact-integer? exact-integer? -> void?
    (define/public (increment k val)
      )))

;; Your custom-stack% object will be instantiated and called as such:
;; (define obj (new custom-stack% [max-size max-size]))
;; (send obj push x)
;; (define param_2 (send obj pop))
;; (send obj increment k val)
```

### Erlang

```erlang
-spec custom_stack_init_(MaxSize :: integer()) -> any().
custom_stack_init_(MaxSize) ->
  .

-spec custom_stack_push(X :: integer()) -> any().
custom_stack_push(X) ->
  .

-spec custom_stack_pop() -> integer().
custom_stack_pop() ->
  .

-spec custom_stack_increment(K :: integer(), Val :: integer()) -> any().
custom_stack_increment(K, Val) ->
  .


%% Your functions will be called as such:
%% custom_stack_init_(MaxSize),
%% custom_stack_push(X),
%% Param_2 = custom_stack_pop(),
%% custom_stack_increment(K, Val),

%% custom_stack_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule CustomStack do
  @spec init_(max_size :: integer) :: any
  def init_(max_size) do
    
  end

  @spec push(x :: integer) :: any
  def push(x) do
    
  end

  @spec pop() :: integer
  def pop() do
    
  end

  @spec increment(k :: integer, val :: integer) :: any
  def increment(k, val) do
    
  end
end

# Your functions will be called as such:
# CustomStack.init_(max_size)
# CustomStack.push(x)
# param_2 = CustomStack.pop()
# CustomStack.increment(k, val)

# CustomStack.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class CustomStack {
    init(maxSize: Int64) {

    }
    
    func push(x: Int64): Unit {

    }
    
    func pop(): Int64 {

    }
    
    func increment(k: Int64, val: Int64): Unit {

    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * let obj: CustomStack = CustomStack(maxSize)
 * obj.push(x)
 * let param_2 = obj.pop()
 * obj.increment(k,val)
 */
```

