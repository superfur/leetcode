# 面试题 03.03. 堆盘子

## 题目描述

<p>堆盘子。设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，我们就会另外堆一堆盘子。请实现数据结构<code>SetOfStacks</code>，模拟这种行为。<code>SetOfStacks</code>应该由多个栈组成，并且在前一个栈填满时新建一个栈。此外，<code>SetOfStacks.push()</code>和<code>SetOfStacks.pop()</code>应该与普通栈的操作方法相同（也就是说，pop()返回的值，应该跟只有一个栈时的情况一样）。 进阶：实现一个<code>popAt(int index)</code>方法，根据指定的子栈，执行pop操作。</p>

<p>当某个栈为空时，应当删除该栈。当栈中没有元素或不存在该栈时，<code>pop</code>，<code>popAt</code>&nbsp;应返回 -1.</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：
["StackOfPlates", "push", "push", "popAt", "pop", "pop"]
[[1], [1], [2], [1], [], []]
<strong> 输出</strong>：
[null, null, null, 2, 1, -1]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：
["StackOfPlates", "push", "push", "push", "popAt", "popAt", "popAt"]
[[2], [1], [2], [3], [0], [0], [0]]
<strong> 输出</strong>：
[null, null, null, null, 2, 1, 3]
</pre>


## 难度

Medium

## 标签

- 栈
- 设计
- 链表

## 提示

1. 你需要追踪每个子栈的大小。当一个栈已满时，你可能需要创建一个新栈。
2. 在一个特定的子栈中弹出一个元素意味着一些栈没有满。这是个问题吗？没有正确的答案，但你应该考虑如何处理这个问题。

## 示例

```
["StackOfPlates", "push", "push", "popAt", "pop", "pop"]
[[1], [1], [2], [1], [], []]
["StackOfPlates", "push", "push", "push", "popAt", "popAt", "popAt"]
[[2], [1], [2], [3], [0], [0], [0]]
```

## 示例代码

### C++

```cpp
class StackOfPlates {
public:
    StackOfPlates(int cap) {
        
    }
    
    void push(int val) {
        
    }
    
    int pop() {
        
    }
    
    int popAt(int index) {
        
    }
};

/**
 * Your StackOfPlates object will be instantiated and called as such:
 * StackOfPlates* obj = new StackOfPlates(cap);
 * obj->push(val);
 * int param_2 = obj->pop();
 * int param_3 = obj->popAt(index);
 */
```

### Java

```java
class StackOfPlates {

    public StackOfPlates(int cap) {
        
    }
    
    public void push(int val) {
        
    }
    
    public int pop() {
        
    }
    
    public int popAt(int index) {
        
    }
}

/**
 * Your StackOfPlates object will be instantiated and called as such:
 * StackOfPlates obj = new StackOfPlates(cap);
 * obj.push(val);
 * int param_2 = obj.pop();
 * int param_3 = obj.popAt(index);
 */
```

### Python

```python
class StackOfPlates(object):

    def __init__(self, cap):
        """
        :type cap: int
        """
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        """
        :rtype: int
        """
        

    def popAt(self, index):
        """
        :type index: int
        :rtype: int
        """
        


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)
```

### Python3

```python3
class StackOfPlates:

    def __init__(self, cap: int):
        

    def push(self, val: int) -> None:
        

    def pop(self) -> int:
        

    def popAt(self, index: int) -> int:
        


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)
```

### C

```c



typedef struct {
    
} StackOfPlates;


StackOfPlates* stackOfPlatesCreate(int cap) {
    
}

void stackOfPlatesPush(StackOfPlates* obj, int val) {
    
}

int stackOfPlatesPop(StackOfPlates* obj) {
    
}

int stackOfPlatesPopAt(StackOfPlates* obj, int index) {
    
}

void stackOfPlatesFree(StackOfPlates* obj) {
    
}

/**
 * Your StackOfPlates struct will be instantiated and called as such:
 * StackOfPlates* obj = stackOfPlatesCreate(cap);
 * stackOfPlatesPush(obj, val);
 
 * int param_2 = stackOfPlatesPop(obj);
 
 * int param_3 = stackOfPlatesPopAt(obj, index);
 
 * stackOfPlatesFree(obj);
*/
```

### C#

```csharp
public class StackOfPlates {

    public StackOfPlates(int cap) {
        
    }
    
    public void Push(int val) {
        
    }
    
    public int Pop() {
        
    }
    
    public int PopAt(int index) {
        
    }
}

/**
 * Your StackOfPlates object will be instantiated and called as such:
 * StackOfPlates obj = new StackOfPlates(cap);
 * obj.Push(val);
 * int param_2 = obj.Pop();
 * int param_3 = obj.PopAt(index);
 */
```

### JavaScript

```javascript
/**
 * @param {number} cap
 */
var StackOfPlates = function(cap) {
    
};

/** 
 * @param {number} val
 * @return {void}
 */
StackOfPlates.prototype.push = function(val) {
    
};

/**
 * @return {number}
 */
StackOfPlates.prototype.pop = function() {
    
};

/** 
 * @param {number} index
 * @return {number}
 */
StackOfPlates.prototype.popAt = function(index) {
    
};

/** 
 * Your StackOfPlates object will be instantiated and called as such:
 * var obj = new StackOfPlates(cap)
 * obj.push(val)
 * var param_2 = obj.pop()
 * var param_3 = obj.popAt(index)
 */
```

### TypeScript

```typescript
class StackOfPlates {
    constructor(cap: number) {
        
    }

    push(val: number): void {
        
    }

    pop(): number {
        
    }

    popAt(index: number): number {
        
    }
}

/**
 * Your StackOfPlates object will be instantiated and called as such:
 * var obj = new StackOfPlates(cap)
 * obj.push(val)
 * var param_2 = obj.pop()
 * var param_3 = obj.popAt(index)
 */
```

### PHP

```php
class StackOfPlates {
    /**
     * @param Integer $cap
     */
    function __construct($cap) {
        
    }
  
    /**
     * @param Integer $val
     * @return NULL
     */
    function push($val) {
        
    }
  
    /**
     * @return Integer
     */
    function pop() {
        
    }
  
    /**
     * @param Integer $index
     * @return Integer
     */
    function popAt($index) {
        
    }
}

/**
 * Your StackOfPlates object will be instantiated and called as such:
 * $obj = StackOfPlates($cap);
 * $obj->push($val);
 * $ret_2 = $obj->pop();
 * $ret_3 = $obj->popAt($index);
 */
```

### Swift

```swift

class StackOfPlates {

    init(_ cap: Int) {
        
    }
    
    func push(_ val: Int) {
        
    }
    
    func pop() -> Int {
        
    }
    
    func popAt(_ index: Int) -> Int {
        
    }
}

/**
 * Your StackOfPlates object will be instantiated and called as such:
 * let obj = StackOfPlates(cap)
 * obj.push(val)
 * let ret_2: Int = obj.pop()
 * let ret_3: Int = obj.popAt(index)
 */
```

### Kotlin

```kotlin
class StackOfPlates(cap: Int) {

    fun push(`val`: Int) {
        
    }

    fun pop(): Int {
        
    }

    fun popAt(index: Int): Int {
        
    }

}

/**
 * Your StackOfPlates object will be instantiated and called as such:
 * var obj = StackOfPlates(cap)
 * obj.push(`val`)
 * var param_2 = obj.pop()
 * var param_3 = obj.popAt(index)
 */
```

### Dart

```dart
class StackOfPlates {

  StackOfPlates(int cap) {
    
  }
  
  void push(int val) {
    
  }
  
  int pop() {
    
  }
  
  int popAt(int index) {
    
  }
}

/**
 * Your StackOfPlates object will be instantiated and called as such:
 * StackOfPlates obj = StackOfPlates(cap);
 * obj.push(val);
 * int param2 = obj.pop();
 * int param3 = obj.popAt(index);
 */
```

### Go

```golang
type StackOfPlates struct {
    
}


func Constructor(cap int) StackOfPlates {
    
}


func (this *StackOfPlates) Push(val int)  {
    
}


func (this *StackOfPlates) Pop() int {
    
}


func (this *StackOfPlates) PopAt(index int) int {
    
}


/**
 * Your StackOfPlates object will be instantiated and called as such:
 * obj := Constructor(cap);
 * obj.Push(val);
 * param_2 := obj.Pop();
 * param_3 := obj.PopAt(index);
 */
```

### Ruby

```ruby
class StackOfPlates

=begin
    :type cap: Integer
=end
    def initialize(cap)
        
    end


=begin
    :type val: Integer
    :rtype: Void
=end
    def push(val)
        
    end


=begin
    :rtype: Integer
=end
    def pop()
        
    end


=begin
    :type index: Integer
    :rtype: Integer
=end
    def pop_at(index)
        
    end


end

# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates.new(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.pop_at(index)
```

### Scala

```scala
class StackOfPlates(_cap: Int) {

    def push(`val`: Int): Unit = {
        
    }

    def pop(): Int = {
        
    }

    def popAt(index: Int): Int = {
        
    }

}

/**
 * Your StackOfPlates object will be instantiated and called as such:
 * val obj = new StackOfPlates(cap)
 * obj.push(`val`)
 * val param_2 = obj.pop()
 * val param_3 = obj.popAt(index)
 */
```

### Rust

```rust
struct StackOfPlates {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StackOfPlates {

    fn new(cap: i32) -> Self {
        
    }
    
    fn push(&self, val: i32) {
        
    }
    
    fn pop(&self) -> i32 {
        
    }
    
    fn pop_at(&self, index: i32) -> i32 {
        
    }
}

/**
 * Your StackOfPlates object will be instantiated and called as such:
 * let obj = StackOfPlates::new(cap);
 * obj.push(val);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.pop_at(index);
 */
```

### Racket

```racket
(define stack-of-plates%
  (class object%
    (super-new)
    
    ; cap : exact-integer?
    (init-field
      cap)
    
    ; push : exact-integer? -> void?
    (define/public (push val)
      )
    ; pop : -> exact-integer?
    (define/public (pop)
      )
    ; pop-at : exact-integer? -> exact-integer?
    (define/public (pop-at index)
      )))

;; Your stack-of-plates% object will be instantiated and called as such:
;; (define obj (new stack-of-plates% [cap cap]))
;; (send obj push val)
;; (define param_2 (send obj pop))
;; (define param_3 (send obj pop-at index))
```

### Erlang

```erlang
-spec stack_of_plates_init_(Cap :: integer()) -> any().
stack_of_plates_init_(Cap) ->
  .

-spec stack_of_plates_push(Val :: integer()) -> any().
stack_of_plates_push(Val) ->
  .

-spec stack_of_plates_pop() -> integer().
stack_of_plates_pop() ->
  .

-spec stack_of_plates_pop_at(Index :: integer()) -> integer().
stack_of_plates_pop_at(Index) ->
  .


%% Your functions will be called as such:
%% stack_of_plates_init_(Cap),
%% stack_of_plates_push(Val),
%% Param_2 = stack_of_plates_pop(),
%% Param_3 = stack_of_plates_pop_at(Index),

%% stack_of_plates_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule StackOfPlates do
  @spec init_(cap :: integer) :: any
  def init_(cap) do
    
  end

  @spec push(val :: integer) :: any
  def push(val) do
    
  end

  @spec pop() :: integer
  def pop() do
    
  end

  @spec pop_at(index :: integer) :: integer
  def pop_at(index) do
    
  end
end

# Your functions will be called as such:
# StackOfPlates.init_(cap)
# StackOfPlates.push(val)
# param_2 = StackOfPlates.pop()
# param_3 = StackOfPlates.pop_at(index)

# StackOfPlates.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class StackOfPlates {
    init(cap: Int64) {

    }
    
    func push(val: Int64): Unit {

    }
    
    func pop(): Int64 {

    }
    
    func popAt(index: Int64): Int64 {

    }
}

/**
 * Your StackOfPlates object will be instantiated and called as such:
 * let obj: StackOfPlates = StackOfPlates(cap)
 * obj.push(val)
 * let param_2 = obj.pop()
 * let param_3 = obj.popAt(index)
 */
```

