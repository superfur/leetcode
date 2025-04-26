# 面试题 03.04. 化栈为队

## 题目描述

<p>实现一个MyQueue类，该类用两个栈来实现一个队列。</p><br><p><strong>示例：</strong><pre>MyQueue queue = new MyQueue();<br><br>queue.push(1);<br>queue.push(2);<br>queue.peek();  // 返回 1<br>queue.pop();   // 返回 1<br>queue.empty(); // 返回 false</pre></p><br><p><strong>说明：</strong><br><ul><li>你只能使用标准的栈操作 -- 也就是只有 <code>push to top</code>, <code>peek/pop from top</code>, <code>size</code> 和 <code>is empty</code> 操作是合法的。</li><li>你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。</li><li>假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。</li></ul></p>

## 难度

Easy

## 标签

- 栈
- 设计
- 队列

## 提示

1. 队列和栈的主要区别是元素的顺序。队列删除最旧的项，栈删除最新的项。如果你只访问最新的项，那么如何从栈中删除最旧的项？
2. 我们可以通过不断地删除最新的项（将这些项插入临时栈中）来删除栈中最老的项，直到得到一个元素为止。然后，在检索到最新项后，将所有元素返回。与此有关的问题是，每次在一行中做几个弹出操作（pop）将需要O(n)的时间。我们可以优化在一行中连续弹出这一场景吗？

## 示例

```
["MyQueue","push","push","peek","pop","empty"]
[[],[1],[2],[],[],[]]
```

## 示例代码

### C++

```cpp
class MyQueue {
public:
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        
    }
    
    /** Get the front element. */
    int peek() {
        
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
```

### Java

```java
class MyQueue {

    /** Initialize your data structure here. */
    public MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        
    }
    
    /** Get the front element. */
    public int peek() {
        
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
```

### Python

```python
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

### Python3

```python3
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

### C

```c



typedef struct {
    
} MyQueue;

/** Initialize your data structure here. */

MyQueue* myQueueCreate() {
    
}

/** Push element x to the back of queue. */
void myQueuePush(MyQueue* obj, int x) {
    
}

/** Removes the element from in front of queue and returns that element. */
int myQueuePop(MyQueue* obj) {
    
}

/** Get the front element. */
int myQueuePeek(MyQueue* obj) {
    
}

/** Returns whether the queue is empty. */
bool myQueueEmpty(MyQueue* obj) {
    
}

void myQueueFree(MyQueue* obj) {
    
}

/**
 * Your MyQueue struct will be instantiated and called as such:
 * MyQueue* obj = myQueueCreate();
 * myQueuePush(obj, x);
 
 * int param_2 = myQueuePop(obj);
 
 * int param_3 = myQueuePeek(obj);
 
 * bool param_4 = myQueueEmpty(obj);
 
 * myQueueFree(obj);
*/
```

### C#

```csharp
public class MyQueue {

    /** Initialize your data structure here. */
    public MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    public void Push(int x) {
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int Pop() {
        
    }
    
    /** Get the front element. */
    public int Peek() {
        
    }
    
    /** Returns whether the queue is empty. */
    public bool Empty() {
        
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Peek();
 * bool param_4 = obj.Empty();
 */
```

### JavaScript

```javascript
/**
 * Initialize your data structure here.
 */
var MyQueue = function() {
    
};

/**
 * Push element x to the back of queue. 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    
};

/**
 * Removes the element from in front of queue and returns that element.
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    
};

/**
 * Get the front element.
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    
};

/**
 * Returns whether the queue is empty.
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
```

### TypeScript

```typescript
class MyQueue {
    constructor() {
        
    }

    push(x: number): void {
        
    }

    pop(): number {
        
    }

    peek(): number {
        
    }

    empty(): boolean {
        
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
```

### PHP

```php
class MyQueue {
    /**
     * Initialize your data structure here.
     */
    function __construct() {
        
    }
  
    /**
     * Push element x to the back of queue.
     * @param Integer $x
     * @return NULL
     */
    function push($x) {
        
    }
  
    /**
     * Removes the element from in front of queue and returns that element.
     * @return Integer
     */
    function pop() {
        
    }
  
    /**
     * Get the front element.
     * @return Integer
     */
    function peek() {
        
    }
  
    /**
     * Returns whether the queue is empty.
     * @return Boolean
     */
    function empty() {
        
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * $obj = MyQueue();
 * $obj->push($x);
 * $ret_2 = $obj->pop();
 * $ret_3 = $obj->peek();
 * $ret_4 = $obj->empty();
 */
```

### Swift

```swift

class MyQueue {

    /** Initialize your data structure here. */
    init() {
        
    }
    
    /** Push element x to the back of queue. */
    func push(_ x: Int) {
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    func pop() -> Int {
        
    }
    
    /** Get the front element. */
    func peek() -> Int {
        
    }
    
    /** Returns whether the queue is empty. */
    func empty() -> Bool {
        
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue()
 * obj.push(x)
 * let ret_2: Int = obj.pop()
 * let ret_3: Int = obj.peek()
 * let ret_4: Bool = obj.empty()
 */
```

### Kotlin

```kotlin
class MyQueue() {

    /** Initialize your data structure here. */
    

    /** Push element x to the back of queue. */
    fun push(x: Int) {
        
    }

    /** Removes the element from in front of queue and returns that element. */
    fun pop(): Int {
        
    }

    /** Get the front element. */
    fun peek(): Int {
        
    }

    /** Returns whether the queue is empty. */
    fun empty(): Boolean {
        
    }

}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
```

### Dart

```dart
class MyQueue {

  /** Initialize your data structure here. */
  MyQueue() {
    
  }
  
  /** Push element x to the back of queue. */
  void push(int x) {
    
  }
  
  /** Removes the element from in front of queue and returns that element. */
  int pop() {
    
  }
  
  /** Get the front element. */
  int peek() {
    
  }
  
  /** Returns whether the queue is empty. */
  bool empty() {
    
  }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = MyQueue();
 * obj.push(x);
 * int param2 = obj.pop();
 * int param3 = obj.peek();
 * bool param4 = obj.empty();
 */
```

### Go

```golang
type MyQueue struct {
    
}


/** Initialize your data structure here. */
func Constructor() MyQueue {
    
}


/** Push element x to the back of queue. */
func (this *MyQueue) Push(x int)  {
    
}


/** Removes the element from in front of queue and returns that element. */
func (this *MyQueue) Pop() int {
    
}


/** Get the front element. */
func (this *MyQueue) Peek() int {
    
}


/** Returns whether the queue is empty. */
func (this *MyQueue) Empty() bool {
    
}


/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
```

### Ruby

```ruby
class MyQueue

=begin
    Initialize your data structure here.
=end
    def initialize()
        
    end


=begin
    Push element x to the back of queue.
    :type x: Integer
    :rtype: Void
=end
    def push(x)
        
    end


=begin
    Removes the element from in front of queue and returns that element.
    :rtype: Integer
=end
    def pop()
        
    end


=begin
    Get the front element.
    :rtype: Integer
=end
    def peek()
        
    end


=begin
    Returns whether the queue is empty.
    :rtype: Boolean
=end
    def empty()
        
    end


end

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue.new()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

### Scala

```scala
class MyQueue() {

    /** Initialize your data structure here. */
    

    /** Push element x to the back of queue. */
    def push(x: Int): Unit = {
        
    }

    /** Removes the element from in front of queue and returns that element. */
    def pop(): Int = {
        
    }

    /** Get the front element. */
    def peek(): Int = {
        
    }

    /** Returns whether the queue is empty. */
    def empty(): Boolean = {
        
    }

}

/**
 * Your MyQueue object will be instantiated and called as such:
 * val obj = new MyQueue()
 * obj.push(x)
 * val param_2 = obj.pop()
 * val param_3 = obj.peek()
 * val param_4 = obj.empty()
 */
```

### Rust

```rust
struct MyQueue {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {

    /** Initialize your data structure here. */
    fn new() -> Self {
        
    }
    
    /** Push element x to the back of queue. */
    fn push(&self, x: i32) {
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    fn pop(&self) -> i32 {
        
    }
    
    /** Get the front element. */
    fn peek(&self) -> i32 {
        
    }
    
    /** Returns whether the queue is empty. */
    fn empty(&self) -> bool {
        
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */
```

### Racket

```racket
(define my-queue%
  (class object%
    (super-new)
    
    (init-field)
    
    ; push : exact-integer? -> void?
    (define/public (push x)
      )
    ; pop : -> exact-integer?
    (define/public (pop)
      )
    ; peek : -> exact-integer?
    (define/public (peek)
      )
    ; empty : -> boolean?
    (define/public (empty)
      )))

;; Your my-queue% object will be instantiated and called as such:
;; (define obj (new my-queue%))
;; (send obj push x)
;; (define param_2 (send obj pop))
;; (define param_3 (send obj peek))
;; (define param_4 (send obj empty))
```

### Erlang

```erlang
-spec my_queue_init_() -> any().
my_queue_init_() ->
  .

-spec my_queue_push(X :: integer()) -> any().
my_queue_push(X) ->
  .

-spec my_queue_pop() -> integer().
my_queue_pop() ->
  .

-spec my_queue_peek() -> integer().
my_queue_peek() ->
  .

-spec my_queue_empty() -> boolean().
my_queue_empty() ->
  .


%% Your functions will be called as such:
%% my_queue_init_(),
%% my_queue_push(X),
%% Param_2 = my_queue_pop(),
%% Param_3 = my_queue_peek(),
%% Param_4 = my_queue_empty(),

%% my_queue_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MyQueue do
  @spec init_() :: any
  def init_() do
    
  end

  @spec push(x :: integer) :: any
  def push(x) do
    
  end

  @spec pop() :: integer
  def pop() do
    
  end

  @spec peek() :: integer
  def peek() do
    
  end

  @spec empty() :: boolean
  def empty() do
    
  end
end

# Your functions will be called as such:
# MyQueue.init_()
# MyQueue.push(x)
# param_2 = MyQueue.pop()
# param_3 = MyQueue.peek()
# param_4 = MyQueue.empty()

# MyQueue.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MyQueue {
    /** Initialize your data structure here. */
    init() {

    }
    
    /** Push element x to the back of queue. */
    func push(x: Int64): Unit {

    }
    
    /** Removes the element from in front of queue and returns that element. */
    func pop(): Int64 {

    }
    
    /** Get the front element. */
    func peek(): Int64 {

    }
    
    /** Returns whether the queue is empty. */
    func empty(): Bool {

    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj: MyQueue = MyQueue()
 * obj.push(x)
 * let param_2 = obj.pop()
 * let param_3 = obj.peek()
 * let param_4 = obj.empty()
 */
```

