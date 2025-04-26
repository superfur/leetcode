# 225. 用队列实现栈

## 题目描述

<p>请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（<code>push</code>、<code>top</code>、<code>pop</code> 和 <code>empty</code>）。</p>

<p>实现 <code>MyStack</code> 类：</p>

<ul>
	<li><code>void push(int x)</code> 将元素 x 压入栈顶。</li>
	<li><code>int pop()</code> 移除并返回栈顶元素。</li>
	<li><code>int top()</code> 返回栈顶元素。</li>
	<li><code>boolean empty()</code> 如果栈是空的，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong></p>

<ul>
	<li>你只能使用队列的标准操作 —— 也就是&nbsp;<code>push to back</code>、<code>peek/pop from front</code>、<code>size</code> 和&nbsp;<code>is empty</code>&nbsp;这些操作。</li>
	<li>你所使用的语言也许不支持队列。&nbsp;你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列&nbsp;, 只要是标准的队列操作即可。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>输出：</strong>
[null, null, null, 2, 2, false]

<strong>解释：</strong>
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
	<li>最多调用<code>100</code> 次 <code>push</code>、<code>pop</code>、<code>top</code> 和 <code>empty</code></li>
	<li>每次调用 <code>pop</code> 和 <code>top</code> 都保证栈不为空</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能否仅用一个队列来实现栈。</p>


## 难度

Easy

## 标签

- 栈
- 设计
- 队列

## 示例

```
["MyStack","push","push","top","pop","empty"]
[[],[1],[2],[],[],[]]
```

## 示例代码

### C++

```cpp
class MyStack {
public:
    MyStack() {
        
    }
    
    void push(int x) {
        
    }
    
    int pop() {
        
    }
    
    int top() {
        
    }
    
    bool empty() {
        
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
```

### Java

```java
class MyStack {

    public MyStack() {
        
    }
    
    public void push(int x) {
        
    }
    
    public int pop() {
        
    }
    
    public int top() {
        
    }
    
    public boolean empty() {
        
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
```

### Python

```python
class MyStack(object):

    def __init__(self):
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        """
        :rtype: int
        """
        

    def top(self):
        """
        :rtype: int
        """
        

    def empty(self):
        """
        :rtype: bool
        """
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

### Python3

```python3
class MyStack:

    def __init__(self):
        

    def push(self, x: int) -> None:
        

    def pop(self) -> int:
        

    def top(self) -> int:
        

    def empty(self) -> bool:
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

### C

```c



typedef struct {
    
} MyStack;


MyStack* myStackCreate() {
    
}

void myStackPush(MyStack* obj, int x) {
    
}

int myStackPop(MyStack* obj) {
    
}

int myStackTop(MyStack* obj) {
    
}

bool myStackEmpty(MyStack* obj) {
    
}

void myStackFree(MyStack* obj) {
    
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 
 * int param_2 = myStackPop(obj);
 
 * int param_3 = myStackTop(obj);
 
 * bool param_4 = myStackEmpty(obj);
 
 * myStackFree(obj);
*/
```

### C#

```csharp
public class MyStack {

    public MyStack() {
        
    }
    
    public void Push(int x) {
        
    }
    
    public int Pop() {
        
    }
    
    public int Top() {
        
    }
    
    public bool Empty() {
        
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Top();
 * bool param_4 = obj.Empty();
 */
```

### JavaScript

```javascript

var MyStack = function() {
    
};

/** 
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
    
};

/**
 * @return {number}
 */
MyStack.prototype.pop = function() {
    
};

/**
 * @return {number}
 */
MyStack.prototype.top = function() {
    
};

/**
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
    
};

/** 
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
```

### TypeScript

```typescript
class MyStack {
    constructor() {
        
    }

    push(x: number): void {
        
    }

    pop(): number {
        
    }

    top(): number {
        
    }

    empty(): boolean {
        
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
```

### PHP

```php
class MyStack {
    /**
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
     * @return Integer
     */
    function pop() {
        
    }
  
    /**
     * @return Integer
     */
    function top() {
        
    }
  
    /**
     * @return Boolean
     */
    function empty() {
        
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * $obj = MyStack();
 * $obj->push($x);
 * $ret_2 = $obj->pop();
 * $ret_3 = $obj->top();
 * $ret_4 = $obj->empty();
 */
```

### Swift

```swift

class MyStack {

    init() {
        
    }
    
    func push(_ x: Int) {
        
    }
    
    func pop() -> Int {
        
    }
    
    func top() -> Int {
        
    }
    
    func empty() -> Bool {
        
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * let obj = MyStack()
 * obj.push(x)
 * let ret_2: Int = obj.pop()
 * let ret_3: Int = obj.top()
 * let ret_4: Bool = obj.empty()
 */
```

### Kotlin

```kotlin
class MyStack() {

    fun push(x: Int) {
        
    }

    fun pop(): Int {
        
    }

    fun top(): Int {
        
    }

    fun empty(): Boolean {
        
    }

}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
```

### Dart

```dart
class MyStack {

  MyStack() {
    
  }
  
  void push(int x) {
    
  }
  
  int pop() {
    
  }
  
  int top() {
    
  }
  
  bool empty() {
    
  }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = MyStack();
 * obj.push(x);
 * int param2 = obj.pop();
 * int param3 = obj.top();
 * bool param4 = obj.empty();
 */
```

### Go

```golang
type MyStack struct {
    
}


func Constructor() MyStack {
    
}


func (this *MyStack) Push(x int)  {
    
}


func (this *MyStack) Pop() int {
    
}


func (this *MyStack) Top() int {
    
}


func (this *MyStack) Empty() bool {
    
}


/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
```

### Ruby

```ruby
class MyStack
    def initialize()
        
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
    :rtype: Integer
=end
    def top()
        
    end


=begin
    :rtype: Boolean
=end
    def empty()
        
    end


end

# Your MyStack object will be instantiated and called as such:
# obj = MyStack.new()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

### Scala

```scala
class MyStack() {

    def push(x: Int): Unit = {
        
    }

    def pop(): Int = {
        
    }

    def top(): Int = {
        
    }

    def empty(): Boolean = {
        
    }

}

/**
 * Your MyStack object will be instantiated and called as such:
 * val obj = new MyStack()
 * obj.push(x)
 * val param_2 = obj.pop()
 * val param_3 = obj.top()
 * val param_4 = obj.empty()
 */
```

### Rust

```rust
struct MyStack {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyStack {

    fn new() -> Self {
        
    }
    
    fn push(&self, x: i32) {
        
    }
    
    fn pop(&self) -> i32 {
        
    }
    
    fn top(&self) -> i32 {
        
    }
    
    fn empty(&self) -> bool {
        
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * let obj = MyStack::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: bool = obj.empty();
 */
```

### Racket

```racket
(define my-stack%
  (class object%
    (super-new)
    
    (init-field)
    
    ; push : exact-integer? -> void?
    (define/public (push x)
      )
    ; pop : -> exact-integer?
    (define/public (pop)
      )
    ; top : -> exact-integer?
    (define/public (top)
      )
    ; empty : -> boolean?
    (define/public (empty)
      )))

;; Your my-stack% object will be instantiated and called as such:
;; (define obj (new my-stack%))
;; (send obj push x)
;; (define param_2 (send obj pop))
;; (define param_3 (send obj top))
;; (define param_4 (send obj empty))
```

### Erlang

```erlang
-spec my_stack_init_() -> any().
my_stack_init_() ->
  .

-spec my_stack_push(X :: integer()) -> any().
my_stack_push(X) ->
  .

-spec my_stack_pop() -> integer().
my_stack_pop() ->
  .

-spec my_stack_top() -> integer().
my_stack_top() ->
  .

-spec my_stack_empty() -> boolean().
my_stack_empty() ->
  .


%% Your functions will be called as such:
%% my_stack_init_(),
%% my_stack_push(X),
%% Param_2 = my_stack_pop(),
%% Param_3 = my_stack_top(),
%% Param_4 = my_stack_empty(),

%% my_stack_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MyStack do
  @spec init_() :: any
  def init_() do
    
  end

  @spec push(x :: integer) :: any
  def push(x) do
    
  end

  @spec pop() :: integer
  def pop() do
    
  end

  @spec top() :: integer
  def top() do
    
  end

  @spec empty() :: boolean
  def empty() do
    
  end
end

# Your functions will be called as such:
# MyStack.init_()
# MyStack.push(x)
# param_2 = MyStack.pop()
# param_3 = MyStack.top()
# param_4 = MyStack.empty()

# MyStack.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MyStack {
    init() {

    }
    
    func push(x: Int64): Unit {

    }
    
    func pop(): Int64 {

    }
    
    func top(): Int64 {

    }
    
    func empty(): Bool {

    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * let obj: MyStack = MyStack()
 * obj.push(x)
 * let param_2 = obj.pop()
 * let param_3 = obj.top()
 * let param_4 = obj.empty()
 */
```

