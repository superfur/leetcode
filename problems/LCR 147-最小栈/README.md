# LCR 147. 最小栈

## 题目描述

<p>请你设计一个 <strong>最小栈</strong> 。它提供 <code>push</code> ，<code>pop</code> ，<code>top</code> 操作，并能在常数时间内检索到最小元素的栈。</p>

<p>&nbsp;</p>

<p>实现 <code>MinStack</code> 类:</p>

<ul>
	<li><code>MinStack()</code> 初始化堆栈对象。</li>
	<li><code>void push(int val)</code> 将元素val推入堆栈。</li>
	<li><code>void pop()</code> 删除堆栈顶部的元素。</li>
	<li><code>int top()</code> 获取堆栈顶部的元素。</li>
	<li><code>int getMin()</code> 获取堆栈中的最小元素。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

<strong>输出：</strong>
[null,null,null,null,-3,null,0,-2]

<strong>解释：</strong>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(2);
minStack.push(-3);
minStack.getMin(); &nbsp; --&gt; 返回 -3.
minStack.pop();
minStack.top(); &nbsp; &nbsp; &nbsp;--&gt; 返回 0.
minStack.getMin(); &nbsp; --&gt; 返回 -2.
</pre>

<p>&nbsp;</p>

<p><strong>&nbsp;<br />
提示：</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>pop</code>、<code>top</code> 和 <code>getMin</code> 操作总是在 <strong>非空栈</strong> 上调用</li>
	<li><code>push</code>、<code>pop</code>、<code>top</code> 和 <code>getMin</code> 最多被调用 <code>3 * 10<sup>4</sup></code> 次</li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 155 题相同：<a href="https://leetcode-cn.com/problems/min-stack/">https://leetcode-cn.com/problems/min-stack/</a></p>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 栈
- 设计

## 示例

```
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
```

## 示例代码

### C++

```cpp
class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        
    }
    
    void pop() {
        
    }
    
    int top() {
        
    }
    
    int getMin() {
        
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

### Java

```java
class MinStack {

    /** initialize your data structure here. */
    public MinStack() {
        
    }
    
    public void push(int x) {
        
    }
    
    public void pop() {
        
    }
    
    public int top() {
        
    }
    
    public int getMin() {
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
```

### Python

```python
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        """
        :rtype: None
        """
        

    def top(self):
        """
        :rtype: int
        """
        

    def getMin(self):
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

### Python3

```python3
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        

    def pop(self) -> None:
        

    def top(self) -> int:
        

    def getMin(self) -> int:
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

### C

```c



typedef struct {
    
} MinStack;

/** initialize your data structure here. */

MinStack* minStackCreate() {
    
}

void minStackPush(MinStack* obj, int x) {
    
}

void minStackPop(MinStack* obj) {
    
}

int minStackTop(MinStack* obj) {
    
}

int minStackGetMin(MinStack* obj) {
    
}

void minStackFree(MinStack* obj) {
    
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, x);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/
```

### C#

```csharp
public class MinStack {

    /** initialize your data structure here. */
    public MinStack() {
        
    }
    
    public void Push(int x) {
        
    }
    
    public void Pop() {
        
    }
    
    public int Top() {
        
    }
    
    public int GetMin() {
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(x);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */
```

### JavaScript

```javascript
/**
 * initialize your data structure here.
 */
var MinStack = function() {
    
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
```

### TypeScript

```typescript
class MinStack {
    constructor() {
        
    }

    push(x: number): void {
        
    }

    pop(): void {
        
    }

    top(): number {
        
    }

    getMin(): number {
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
```

### PHP

```php
class MinStack {
    /**
     * initialize your data structure here.
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $x
     * @return NULL
     */
    function push($x) {
        
    }
  
    /**
     * @return NULL
     */
    function pop() {
        
    }
  
    /**
     * @return Integer
     */
    function top() {
        
    }
  
    /**
     * @return Integer
     */
    function getMin() {
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * $obj = MinStack();
 * $obj->push($x);
 * $obj->pop();
 * $ret_3 = $obj->top();
 * $ret_4 = $obj->getMin();
 */
```

### Swift

```swift

class MinStack {

    /** initialize your data structure here. */
    init() {
        
    }
    
    func push(_ x: Int) {
        
    }
    
    func pop() {
        
    }
    
    func top() -> Int {
        
    }
    
    func getMin() -> Int {
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack()
 * obj.push(x)
 * obj.pop()
 * let ret_3: Int = obj.top()
 * let ret_4: Int = obj.getMin()
 */
```

### Kotlin

```kotlin
class MinStack() {

    /** initialize your data structure here. */
    

    fun push(x: Int) {
        
    }

    fun pop() {
        
    }

    fun top(): Int {
        
    }

    fun getMin(): Int {
        
    }

}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
```

### Dart

```dart
class MinStack {

  /** initialize your data structure here. */
  MinStack() {
    
  }
  
  void push(int x) {
    
  }
  
  void pop() {
    
  }
  
  int top() {
    
  }
  
  int getMin() {
    
  }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = MinStack();
 * obj.push(x);
 * obj.pop();
 * int param3 = obj.top();
 * int param4 = obj.getMin();
 */
```

### Go

```golang
type MinStack struct {
    
}


/** initialize your data structure here. */
func Constructor() MinStack {
    
}


func (this *MinStack) Push(x int)  {
    
}


func (this *MinStack) Pop()  {
    
}


func (this *MinStack) Top() int {
    
}


func (this *MinStack) GetMin() int {
    
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
```

### Ruby

```ruby
class MinStack

=begin
    initialize your data structure here.
=end
    def initialize()
        
    end


=begin
    :type x: Integer
    :rtype: Void
=end
    def push(x)
        
    end


=begin
    :rtype: Void
=end
    def pop()
        
    end


=begin
    :rtype: Integer
=end
    def top()
        
    end


=begin
    :rtype: Integer
=end
    def get_min()
        
    end


end

# Your MinStack object will be instantiated and called as such:
# obj = MinStack.new()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.get_min()
```

### Scala

```scala
class MinStack() {

    /** initialize your data structure here. */
    

    def push(x: Int): Unit = {
        
    }

    def pop(): Unit = {
        
    }

    def top(): Int = {
        
    }

    def getMin(): Int = {
        
    }

}

/**
 * Your MinStack object will be instantiated and called as such:
 * val obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * val param_3 = obj.top()
 * val param_4 = obj.getMin()
 */
```

### Rust

```rust
struct MinStack {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    /** initialize your data structure here. */
    fn new() -> Self {
        
    }
    
    fn push(&self, x: i32) {
        
    }
    
    fn pop(&self) {
        
    }
    
    fn top(&self) -> i32 {
        
    }
    
    fn get_min(&self) -> i32 {
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(x);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */
```

### Racket

```racket
(define min-stack%
  (class object%
    (super-new)
    
    (init-field)
    
    ; push : exact-integer? -> void?
    (define/public (push x)
      )
    ; pop : -> void?
    (define/public (pop)
      )
    ; top : -> exact-integer?
    (define/public (top)
      )
    ; get-min : -> exact-integer?
    (define/public (get-min)
      )))

;; Your min-stack% object will be instantiated and called as such:
;; (define obj (new min-stack%))
;; (send obj push x)
;; (send obj pop)
;; (define param_3 (send obj top))
;; (define param_4 (send obj get-min))
```

### Erlang

```erlang
-spec min_stack_init_() -> any().
min_stack_init_() ->
  .

-spec min_stack_push(X :: integer()) -> any().
min_stack_push(X) ->
  .

-spec min_stack_pop() -> any().
min_stack_pop() ->
  .

-spec min_stack_top() -> integer().
min_stack_top() ->
  .

-spec min_stack_get_min() -> integer().
min_stack_get_min() ->
  .


%% Your functions will be called as such:
%% min_stack_init_(),
%% min_stack_push(X),
%% min_stack_pop(),
%% Param_3 = min_stack_top(),
%% Param_4 = min_stack_get_min(),

%% min_stack_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MinStack do
  @spec init_() :: any
  def init_() do
    
  end

  @spec push(x :: integer) :: any
  def push(x) do
    
  end

  @spec pop() :: any
  def pop() do
    
  end

  @spec top() :: integer
  def top() do
    
  end

  @spec get_min() :: integer
  def get_min() do
    
  end
end

# Your functions will be called as such:
# MinStack.init_()
# MinStack.push(x)
# MinStack.pop()
# param_3 = MinStack.top()
# param_4 = MinStack.get_min()

# MinStack.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MinStack {
    /** initialize your data structure here. */
    init() {

    }
    
    func push(x: Int64): Unit {

    }
    
    func pop(): Unit {

    }
    
    func top(): Int64 {

    }
    
    func getMin(): Int64 {

    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj: MinStack = MinStack()
 * obj.push(x)
 * obj.pop()
 * let param_3 = obj.top()
 * let param_4 = obj.getMin()
 */
```

