# 232. 用栈实现队列

## 题目描述

<p>请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（<code>push</code>、<code>pop</code>、<code>peek</code>、<code>empty</code>）：</p>

<p>实现 <code>MyQueue</code> 类：</p>

<ul>
	<li><code>void push(int x)</code> 将元素 x 推到队列的末尾</li>
	<li><code>int pop()</code> 从队列的开头移除并返回元素</li>
	<li><code>int peek()</code> 返回队列开头的元素</li>
	<li><code>boolean empty()</code> 如果队列为空，返回 <code>true</code> ；否则，返回 <code>false</code></li>
</ul>

<p><strong>说明：</strong></p>

<ul>
	<li>你 <strong>只能</strong> 使用标准的栈操作 —— 也就是只有&nbsp;<code>push to top</code>,&nbsp;<code>peek/pop from top</code>,&nbsp;<code>size</code>, 和&nbsp;<code>is empty</code>&nbsp;操作是合法的。</li>
	<li>你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>输出：</strong>
[null, null, null, 1, 1, false]

<strong>解释：</strong>
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
</pre>

<ul>
</ul>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
	<li>最多调用 <code>100</code> 次 <code>push</code>、<code>pop</code>、<code>peek</code> 和 <code>empty</code></li>
	<li>假设所有操作都是有效的 （例如，一个空的队列不会调用 <code>pop</code> 或者 <code>peek</code> 操作）</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你能否实现每个操作均摊时间复杂度为 <code>O(1)</code> 的队列？换句话说，执行 <code>n</code> 个操作的总时间复杂度为 <code>O(n)</code> ，即使其中一个操作可能花费较长时间。</li>
</ul>


## 难度

Easy

## 标签

- 栈
- 设计
- 队列

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
    MyQueue() {
        
    }
    
    void push(int x) {
        
    }
    
    int pop() {
        
    }
    
    int peek() {
        
    }
    
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

    public MyQueue() {
        
    }
    
    public void push(int x) {
        
    }
    
    public int pop() {
        
    }
    
    public int peek() {
        
    }
    
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
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        """
        :rtype: int
        """
        

    def peek(self):
        """
        :rtype: int
        """
        

    def empty(self):
        """
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
        

    def push(self, x: int) -> None:
        

    def pop(self) -> int:
        

    def peek(self) -> int:
        

    def empty(self) -> bool:
        


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


MyQueue* myQueueCreate() {
    
}

void myQueuePush(MyQueue* obj, int x) {
    
}

int myQueuePop(MyQueue* obj) {
    
}

int myQueuePeek(MyQueue* obj) {
    
}

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

    public MyQueue() {
        
    }
    
    public void Push(int x) {
        
    }
    
    public int Pop() {
        
    }
    
    public int Peek() {
        
    }
    
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

var MyQueue = function() {
    
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    
};

/**
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
    function peek() {
        
    }
  
    /**
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

    init() {
        
    }
    
    func push(_ x: Int) {
        
    }
    
    func pop() -> Int {
        
    }
    
    func peek() -> Int {
        
    }
    
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

    fun push(x: Int) {
        
    }

    fun pop(): Int {
        
    }

    fun peek(): Int {
        
    }

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

  MyQueue() {
    
  }
  
  void push(int x) {
    
  }
  
  int pop() {
    
  }
  
  int peek() {
    
  }
  
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


func Constructor() MyQueue {
    
}


func (this *MyQueue) Push(x int)  {
    
}


func (this *MyQueue) Pop() int {
    
}


func (this *MyQueue) Peek() int {
    
}


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
    def peek()
        
    end


=begin
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

    def push(x: Int): Unit = {
        
    }

    def pop(): Int = {
        
    }

    def peek(): Int = {
        
    }

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

    fn new() -> Self {
        
    }
    
    fn push(&self, x: i32) {
        
    }
    
    fn pop(&self) -> i32 {
        
    }
    
    fn peek(&self) -> i32 {
        
    }
    
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
    init() {

    }
    
    func push(x: Int64): Unit {

    }
    
    func pop(): Int64 {

    }
    
    func peek(): Int64 {

    }
    
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

