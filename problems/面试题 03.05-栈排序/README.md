# 面试题 03.05. 栈排序

## 题目描述

<p>栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：<code>push</code>、<code>pop</code>、<code>peek</code> 和 <code>isEmpty</code>。当栈为空时，<code>peek</code>&nbsp;返回 -1。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：
["SortedStack", "push", "push", "peek", "pop", "peek"]
[[], [1], [2], [], [], []]
<strong> 输出</strong>：
[null,null,null,1,null,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>： 
["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
[[], [], [], [1], [], []]
<strong> 输出</strong>：
[null,null,null,null,null,true]
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li>栈中的元素数目在[0, 5000]范围内。</li>
</ol>


## 难度

Medium

## 标签

- 栈
- 设计
- 单调栈

## 提示

1. 排序数组的一种方法是遍历数组，并将每个元素按排序顺序插入到一个新数组中。你可以用一个栈实现吗？
2. 假设二级栈已排序。你能按顺序插入元素吗？你可能需要一些额外的存储空间。你可以使用什么额外的存储？
3. 保持二级栈的排序顺序，最大的元素在顶部。使用主栈进行额外的存储。

## 示例

```
["SortedStack", "push", "push", "peek", "pop", "peek"]
[[], [1], [2], [], [], []]
["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
[[], [], [], [1], [], []]
```

## 示例代码

### C++

```cpp
class SortedStack {
public:
    SortedStack() {
        
    }
    
    void push(int val) {
        
    }
    
    void pop() {
        
    }
    
    int peek() {
        
    }
    
    bool isEmpty() {
        
    }
};

/**
 * Your SortedStack object will be instantiated and called as such:
 * SortedStack* obj = new SortedStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->isEmpty();
 */
```

### Java

```java
class SortedStack {

    public SortedStack() {
        
    }
    
    public void push(int val) {
        
    }
    
    public void pop() {
        
    }
    
    public int peek() {
        
    }
    
    public boolean isEmpty() {
        
    }
}

/**
 * Your SortedStack object will be instantiated and called as such:
 * SortedStack obj = new SortedStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.isEmpty();
 */
```

### Python

```python
class SortedStack(object):

    def __init__(self):
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        """
        :rtype: None
        """
        

    def peek(self):
        """
        :rtype: int
        """
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
```

### Python3

```python3
class SortedStack:

    def __init__(self):
        

    def push(self, val: int) -> None:
        

    def pop(self) -> None:
        

    def peek(self) -> int:
        

    def isEmpty(self) -> bool:
        


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
```

### C

```c



typedef struct {
    
} SortedStack;


SortedStack* sortedStackCreate() {
    
}

void sortedStackPush(SortedStack* obj, int val) {
    
}

void sortedStackPop(SortedStack* obj) {
    
}

int sortedStackPeek(SortedStack* obj) {
    
}

bool sortedStackIsEmpty(SortedStack* obj) {
    
}

void sortedStackFree(SortedStack* obj) {
    
}

/**
 * Your SortedStack struct will be instantiated and called as such:
 * SortedStack* obj = sortedStackCreate();
 * sortedStackPush(obj, val);
 
 * sortedStackPop(obj);
 
 * int param_3 = sortedStackPeek(obj);
 
 * bool param_4 = sortedStackIsEmpty(obj);
 
 * sortedStackFree(obj);
*/
```

### C#

```csharp
public class SortedStack {

    public SortedStack() {
        
    }
    
    public void Push(int val) {
        
    }
    
    public void Pop() {
        
    }
    
    public int Peek() {
        
    }
    
    public bool IsEmpty() {
        
    }
}

/**
 * Your SortedStack object will be instantiated and called as such:
 * SortedStack obj = new SortedStack();
 * obj.Push(val);
 * obj.Pop();
 * int param_3 = obj.Peek();
 * bool param_4 = obj.IsEmpty();
 */
```

### JavaScript

```javascript

var SortedStack = function() {
    
};

/** 
 * @param {number} val
 * @return {void}
 */
SortedStack.prototype.push = function(val) {
    
};

/**
 * @return {void}
 */
SortedStack.prototype.pop = function() {
    
};

/**
 * @return {number}
 */
SortedStack.prototype.peek = function() {
    
};

/**
 * @return {boolean}
 */
SortedStack.prototype.isEmpty = function() {
    
};

/** 
 * Your SortedStack object will be instantiated and called as such:
 * var obj = new SortedStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.isEmpty()
 */
```

### TypeScript

```typescript
class SortedStack {
    constructor() {
        
    }

    push(val: number): void {
        
    }

    pop(): void {
        
    }

    peek(): number {
        
    }

    isEmpty(): boolean {
        
    }
}

/**
 * Your SortedStack object will be instantiated and called as such:
 * var obj = new SortedStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.isEmpty()
 */
```

### PHP

```php
class SortedStack {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $val
     * @return NULL
     */
    function push($val) {
        
    }
  
    /**
     * @return NULL
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
    function isEmpty() {
        
    }
}

/**
 * Your SortedStack object will be instantiated and called as such:
 * $obj = SortedStack();
 * $obj->push($val);
 * $obj->pop();
 * $ret_3 = $obj->peek();
 * $ret_4 = $obj->isEmpty();
 */
```

### Swift

```swift

class SortedStack {

    init() {
        
    }
    
    func push(_ val: Int) {
        
    }
    
    func pop() {
        
    }
    
    func peek() -> Int {
        
    }
    
    func isEmpty() -> Bool {
        
    }
}

/**
 * Your SortedStack object will be instantiated and called as such:
 * let obj = SortedStack()
 * obj.push(val)
 * obj.pop()
 * let ret_3: Int = obj.peek()
 * let ret_4: Bool = obj.isEmpty()
 */
```

### Kotlin

```kotlin
class SortedStack() {

    fun push(`val`: Int) {
        
    }

    fun pop() {
        
    }

    fun peek(): Int {
        
    }

    fun isEmpty(): Boolean {
        
    }

}

/**
 * Your SortedStack object will be instantiated and called as such:
 * var obj = SortedStack()
 * obj.push(`val`)
 * obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.isEmpty()
 */
```

### Dart

```dart
class SortedStack {

  SortedStack() {
    
  }
  
  void push(int val) {
    
  }
  
  void pop() {
    
  }
  
  int peek() {
    
  }
  
  bool isEmpty() {
    
  }
}

/**
 * Your SortedStack object will be instantiated and called as such:
 * SortedStack obj = SortedStack();
 * obj.push(val);
 * obj.pop();
 * int param3 = obj.peek();
 * bool param4 = obj.isEmpty();
 */
```

### Go

```golang
type SortedStack struct {
    
}


func Constructor() SortedStack {
    
}


func (this *SortedStack) Push(val int)  {
    
}


func (this *SortedStack) Pop()  {
    
}


func (this *SortedStack) Peek() int {
    
}


func (this *SortedStack) IsEmpty() bool {
    
}


/**
 * Your SortedStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.IsEmpty();
 */
```

### Ruby

```ruby
class SortedStack
    def initialize()
        
    end


=begin
    :type val: Integer
    :rtype: Void
=end
    def push(val)
        
    end


=begin
    :rtype: Void
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
    def is_empty()
        
    end


end

# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack.new()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.is_empty()
```

### Scala

```scala
class SortedStack() {

    def push(`val`: Int): Unit = {
        
    }

    def pop(): Unit = {
        
    }

    def peek(): Int = {
        
    }

    def isEmpty(): Boolean = {
        
    }

}

/**
 * Your SortedStack object will be instantiated and called as such:
 * val obj = new SortedStack()
 * obj.push(`val`)
 * obj.pop()
 * val param_3 = obj.peek()
 * val param_4 = obj.isEmpty()
 */
```

### Rust

```rust
struct SortedStack {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SortedStack {

    fn new() -> Self {
        
    }
    
    fn push(&self, val: i32) {
        
    }
    
    fn pop(&self) {
        
    }
    
    fn peek(&self) -> i32 {
        
    }
    
    fn is_empty(&self) -> bool {
        
    }
}

/**
 * Your SortedStack object will be instantiated and called as such:
 * let obj = SortedStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.is_empty();
 */
```

### Racket

```racket
(define sorted-stack%
  (class object%
    (super-new)
    
    (init-field)
    
    ; push : exact-integer? -> void?
    (define/public (push val)
      )
    ; pop : -> void?
    (define/public (pop)
      )
    ; peek : -> exact-integer?
    (define/public (peek)
      )
    ; is-empty : -> boolean?
    (define/public (is-empty)
      )))

;; Your sorted-stack% object will be instantiated and called as such:
;; (define obj (new sorted-stack%))
;; (send obj push val)
;; (send obj pop)
;; (define param_3 (send obj peek))
;; (define param_4 (send obj is-empty))
```

### Erlang

```erlang
-spec sorted_stack_init_() -> any().
sorted_stack_init_() ->
  .

-spec sorted_stack_push(Val :: integer()) -> any().
sorted_stack_push(Val) ->
  .

-spec sorted_stack_pop() -> any().
sorted_stack_pop() ->
  .

-spec sorted_stack_peek() -> integer().
sorted_stack_peek() ->
  .

-spec sorted_stack_is_empty() -> boolean().
sorted_stack_is_empty() ->
  .


%% Your functions will be called as such:
%% sorted_stack_init_(),
%% sorted_stack_push(Val),
%% sorted_stack_pop(),
%% Param_3 = sorted_stack_peek(),
%% Param_4 = sorted_stack_is_empty(),

%% sorted_stack_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule SortedStack do
  @spec init_() :: any
  def init_() do
    
  end

  @spec push(val :: integer) :: any
  def push(val) do
    
  end

  @spec pop() :: any
  def pop() do
    
  end

  @spec peek() :: integer
  def peek() do
    
  end

  @spec is_empty() :: boolean
  def is_empty() do
    
  end
end

# Your functions will be called as such:
# SortedStack.init_()
# SortedStack.push(val)
# SortedStack.pop()
# param_3 = SortedStack.peek()
# param_4 = SortedStack.is_empty()

# SortedStack.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class SortedStack {
    init() {

    }
    
    func push(val: Int64): Unit {

    }
    
    func pop(): Unit {

    }
    
    func peek(): Int64 {

    }
    
    func isEmpty(): Bool {

    }
}

/**
 * Your SortedStack object will be instantiated and called as such:
 * let obj: SortedStack = SortedStack()
 * obj.push(val)
 * obj.pop()
 * let param_3 = obj.peek()
 * let param_4 = obj.isEmpty()
 */
```

