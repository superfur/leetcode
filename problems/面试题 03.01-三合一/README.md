# 面试题 03.01. 三合一

## 题目描述

<p>三合一。描述如何只用一个数组来实现三个栈。</p>

<p>你应该实现<code>push(stackNum, value)</code>、<code>pop(stackNum)</code>、<code>isEmpty(stackNum)</code>、<code>peek(stackNum)</code>方法。<code>stackNum</code>表示栈下标，<code>value</code>表示压入的值。</p>

<p>构造函数会传入一个<code>stackSize</code>参数，代表每个栈的大小。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：
["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
<strong> 输出</strong>：
[null, null, null, 1, -1, -1, true]
<strong>说明</strong>：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：
["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
[[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
<strong> 输出</strong>：
[null, null, null, null, 2, 1, -1, -1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= stackNum &lt;= 2</code></li>
</ul>


## 难度

Easy

## 标签

- 栈
- 设计
- 数组

## 提示

1. 栈只是一个数据结构，其中最近添加的元素首先被删除。你能用一个数组来模拟单个栈吗？请记住，有很多可能的解法且每个解法都有其利弊。
2. 我们可以通过将数组的前三分之一分配到第一个栈、第二个三分之一分配到第二个栈、最后的第三个三分之一分配到第三个栈，来模拟数组中的三个栈。然而，实际上某个栈可能比其他的大得多。能更灵活地分配吗？
3. 如果你想考虑灵活划分，可以移动栈。你能保证使用所有可用的容量吗？
4. 试着把数组看作是循环的，这样数组的结尾就“环绕”到了数组的开始部分。

## 示例

```
["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
[[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
```

## 示例代码

### C++

```cpp
class TripleInOne {
public:
    TripleInOne(int stackSize) {
        
    }
    
    void push(int stackNum, int value) {
        
    }
    
    int pop(int stackNum) {
        
    }
    
    int peek(int stackNum) {
        
    }
    
    bool isEmpty(int stackNum) {
        
    }
};

/**
 * Your TripleInOne object will be instantiated and called as such:
 * TripleInOne* obj = new TripleInOne(stackSize);
 * obj->push(stackNum,value);
 * int param_2 = obj->pop(stackNum);
 * int param_3 = obj->peek(stackNum);
 * bool param_4 = obj->isEmpty(stackNum);
 */
```

### Java

```java
class TripleInOne {

    public TripleInOne(int stackSize) {
        
    }
    
    public void push(int stackNum, int value) {
        
    }
    
    public int pop(int stackNum) {
        
    }
    
    public int peek(int stackNum) {
        
    }
    
    public boolean isEmpty(int stackNum) {
        
    }
}

/**
 * Your TripleInOne object will be instantiated and called as such:
 * TripleInOne obj = new TripleInOne(stackSize);
 * obj.push(stackNum,value);
 * int param_2 = obj.pop(stackNum);
 * int param_3 = obj.peek(stackNum);
 * boolean param_4 = obj.isEmpty(stackNum);
 */
```

### Python

```python
class TripleInOne(object):

    def __init__(self, stackSize):
        """
        :type stackSize: int
        """
        

    def push(self, stackNum, value):
        """
        :type stackNum: int
        :type value: int
        :rtype: None
        """
        

    def pop(self, stackNum):
        """
        :type stackNum: int
        :rtype: int
        """
        

    def peek(self, stackNum):
        """
        :type stackNum: int
        :rtype: int
        """
        

    def isEmpty(self, stackNum):
        """
        :type stackNum: int
        :rtype: bool
        """
        


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
```

### Python3

```python3
class TripleInOne:

    def __init__(self, stackSize: int):
        

    def push(self, stackNum: int, value: int) -> None:
        

    def pop(self, stackNum: int) -> int:
        

    def peek(self, stackNum: int) -> int:
        

    def isEmpty(self, stackNum: int) -> bool:
        


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
```

### C

```c



typedef struct {
    
} TripleInOne;


TripleInOne* tripleInOneCreate(int stackSize) {
    
}

void tripleInOnePush(TripleInOne* obj, int stackNum, int value) {
    
}

int tripleInOnePop(TripleInOne* obj, int stackNum) {
    
}

int tripleInOnePeek(TripleInOne* obj, int stackNum) {
    
}

bool tripleInOneIsEmpty(TripleInOne* obj, int stackNum) {
    
}

void tripleInOneFree(TripleInOne* obj) {
    
}

/**
 * Your TripleInOne struct will be instantiated and called as such:
 * TripleInOne* obj = tripleInOneCreate(stackSize);
 * tripleInOnePush(obj, stackNum, value);
 
 * int param_2 = tripleInOnePop(obj, stackNum);
 
 * int param_3 = tripleInOnePeek(obj, stackNum);
 
 * bool param_4 = tripleInOneIsEmpty(obj, stackNum);
 
 * tripleInOneFree(obj);
*/
```

### C#

```csharp
public class TripleInOne {

    public TripleInOne(int stackSize) {
        
    }
    
    public void Push(int stackNum, int value) {
        
    }
    
    public int Pop(int stackNum) {
        
    }
    
    public int Peek(int stackNum) {
        
    }
    
    public bool IsEmpty(int stackNum) {
        
    }
}

/**
 * Your TripleInOne object will be instantiated and called as such:
 * TripleInOne obj = new TripleInOne(stackSize);
 * obj.Push(stackNum,value);
 * int param_2 = obj.Pop(stackNum);
 * int param_3 = obj.Peek(stackNum);
 * bool param_4 = obj.IsEmpty(stackNum);
 */
```

### JavaScript

```javascript
/**
 * @param {number} stackSize
 */
var TripleInOne = function(stackSize) {
    
};

/** 
 * @param {number} stackNum 
 * @param {number} value
 * @return {void}
 */
TripleInOne.prototype.push = function(stackNum, value) {
    
};

/** 
 * @param {number} stackNum
 * @return {number}
 */
TripleInOne.prototype.pop = function(stackNum) {
    
};

/** 
 * @param {number} stackNum
 * @return {number}
 */
TripleInOne.prototype.peek = function(stackNum) {
    
};

/** 
 * @param {number} stackNum
 * @return {boolean}
 */
TripleInOne.prototype.isEmpty = function(stackNum) {
    
};

/** 
 * Your TripleInOne object will be instantiated and called as such:
 * var obj = new TripleInOne(stackSize)
 * obj.push(stackNum,value)
 * var param_2 = obj.pop(stackNum)
 * var param_3 = obj.peek(stackNum)
 * var param_4 = obj.isEmpty(stackNum)
 */
```

### TypeScript

```typescript
class TripleInOne {
    constructor(stackSize: number) {
        
    }

    push(stackNum: number, value: number): void {
        
    }

    pop(stackNum: number): number {
        
    }

    peek(stackNum: number): number {
        
    }

    isEmpty(stackNum: number): boolean {
        
    }
}

/**
 * Your TripleInOne object will be instantiated and called as such:
 * var obj = new TripleInOne(stackSize)
 * obj.push(stackNum,value)
 * var param_2 = obj.pop(stackNum)
 * var param_3 = obj.peek(stackNum)
 * var param_4 = obj.isEmpty(stackNum)
 */
```

### PHP

```php
class TripleInOne {
    /**
     * @param Integer $stackSize
     */
    function __construct($stackSize) {
        
    }
  
    /**
     * @param Integer $stackNum
     * @param Integer $value
     * @return NULL
     */
    function push($stackNum, $value) {
        
    }
  
    /**
     * @param Integer $stackNum
     * @return Integer
     */
    function pop($stackNum) {
        
    }
  
    /**
     * @param Integer $stackNum
     * @return Integer
     */
    function peek($stackNum) {
        
    }
  
    /**
     * @param Integer $stackNum
     * @return Boolean
     */
    function isEmpty($stackNum) {
        
    }
}

/**
 * Your TripleInOne object will be instantiated and called as such:
 * $obj = TripleInOne($stackSize);
 * $obj->push($stackNum, $value);
 * $ret_2 = $obj->pop($stackNum);
 * $ret_3 = $obj->peek($stackNum);
 * $ret_4 = $obj->isEmpty($stackNum);
 */
```

### Swift

```swift

class TripleInOne {

    init(_ stackSize: Int) {
        
    }
    
    func push(_ stackNum: Int, _ value: Int) {
        
    }
    
    func pop(_ stackNum: Int) -> Int {
        
    }
    
    func peek(_ stackNum: Int) -> Int {
        
    }
    
    func isEmpty(_ stackNum: Int) -> Bool {
        
    }
}

/**
 * Your TripleInOne object will be instantiated and called as such:
 * let obj = TripleInOne(stackSize)
 * obj.push(stackNum, value)
 * let ret_2: Int = obj.pop(stackNum)
 * let ret_3: Int = obj.peek(stackNum)
 * let ret_4: Bool = obj.isEmpty(stackNum)
 */
```

### Kotlin

```kotlin
class TripleInOne(stackSize: Int) {

    fun push(stackNum: Int, value: Int) {
        
    }

    fun pop(stackNum: Int): Int {
        
    }

    fun peek(stackNum: Int): Int {
        
    }

    fun isEmpty(stackNum: Int): Boolean {
        
    }

}

/**
 * Your TripleInOne object will be instantiated and called as such:
 * var obj = TripleInOne(stackSize)
 * obj.push(stackNum,value)
 * var param_2 = obj.pop(stackNum)
 * var param_3 = obj.peek(stackNum)
 * var param_4 = obj.isEmpty(stackNum)
 */
```

### Dart

```dart
class TripleInOne {

  TripleInOne(int stackSize) {
    
  }
  
  void push(int stackNum, int value) {
    
  }
  
  int pop(int stackNum) {
    
  }
  
  int peek(int stackNum) {
    
  }
  
  bool isEmpty(int stackNum) {
    
  }
}

/**
 * Your TripleInOne object will be instantiated and called as such:
 * TripleInOne obj = TripleInOne(stackSize);
 * obj.push(stackNum,value);
 * int param2 = obj.pop(stackNum);
 * int param3 = obj.peek(stackNum);
 * bool param4 = obj.isEmpty(stackNum);
 */
```

### Go

```golang
type TripleInOne struct {
    
}


func Constructor(stackSize int) TripleInOne {
    
}


func (this *TripleInOne) Push(stackNum int, value int)  {
    
}


func (this *TripleInOne) Pop(stackNum int) int {
    
}


func (this *TripleInOne) Peek(stackNum int) int {
    
}


func (this *TripleInOne) IsEmpty(stackNum int) bool {
    
}


/**
 * Your TripleInOne object will be instantiated and called as such:
 * obj := Constructor(stackSize);
 * obj.Push(stackNum,value);
 * param_2 := obj.Pop(stackNum);
 * param_3 := obj.Peek(stackNum);
 * param_4 := obj.IsEmpty(stackNum);
 */
```

### Ruby

```ruby
class TripleInOne

=begin
    :type stack_size: Integer
=end
    def initialize(stack_size)
        
    end


=begin
    :type stack_num: Integer
    :type value: Integer
    :rtype: Void
=end
    def push(stack_num, value)
        
    end


=begin
    :type stack_num: Integer
    :rtype: Integer
=end
    def pop(stack_num)
        
    end


=begin
    :type stack_num: Integer
    :rtype: Integer
=end
    def peek(stack_num)
        
    end


=begin
    :type stack_num: Integer
    :rtype: Boolean
=end
    def is_empty(stack_num)
        
    end


end

# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne.new(stack_size)
# obj.push(stack_num, value)
# param_2 = obj.pop(stack_num)
# param_3 = obj.peek(stack_num)
# param_4 = obj.is_empty(stack_num)
```

### Scala

```scala
class TripleInOne(_stackSize: Int) {

    def push(stackNum: Int, value: Int): Unit = {
        
    }

    def pop(stackNum: Int): Int = {
        
    }

    def peek(stackNum: Int): Int = {
        
    }

    def isEmpty(stackNum: Int): Boolean = {
        
    }

}

/**
 * Your TripleInOne object will be instantiated and called as such:
 * val obj = new TripleInOne(stackSize)
 * obj.push(stackNum,value)
 * val param_2 = obj.pop(stackNum)
 * val param_3 = obj.peek(stackNum)
 * val param_4 = obj.isEmpty(stackNum)
 */
```

### Rust

```rust
struct TripleInOne {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TripleInOne {

    fn new(stackSize: i32) -> Self {
        
    }
    
    fn push(&self, stack_num: i32, value: i32) {
        
    }
    
    fn pop(&self, stack_num: i32) -> i32 {
        
    }
    
    fn peek(&self, stack_num: i32) -> i32 {
        
    }
    
    fn is_empty(&self, stack_num: i32) -> bool {
        
    }
}

/**
 * Your TripleInOne object will be instantiated and called as such:
 * let obj = TripleInOne::new(stackSize);
 * obj.push(stackNum, value);
 * let ret_2: i32 = obj.pop(stackNum);
 * let ret_3: i32 = obj.peek(stackNum);
 * let ret_4: bool = obj.is_empty(stackNum);
 */
```

### Racket

```racket
(define triple-in-one%
  (class object%
    (super-new)
    
    ; stack-size : exact-integer?
    (init-field
      stack-size)
    
    ; push : exact-integer? exact-integer? -> void?
    (define/public (push stack-num value)
      )
    ; pop : exact-integer? -> exact-integer?
    (define/public (pop stack-num)
      )
    ; peek : exact-integer? -> exact-integer?
    (define/public (peek stack-num)
      )
    ; is-empty : exact-integer? -> boolean?
    (define/public (is-empty stack-num)
      )))

;; Your triple-in-one% object will be instantiated and called as such:
;; (define obj (new triple-in-one% [stack-size stack-size]))
;; (send obj push stack-num value)
;; (define param_2 (send obj pop stack-num))
;; (define param_3 (send obj peek stack-num))
;; (define param_4 (send obj is-empty stack-num))
```

### Erlang

```erlang
-spec triple_in_one_init_(StackSize :: integer()) -> any().
triple_in_one_init_(StackSize) ->
  .

-spec triple_in_one_push(StackNum :: integer(), Value :: integer()) -> any().
triple_in_one_push(StackNum, Value) ->
  .

-spec triple_in_one_pop(StackNum :: integer()) -> integer().
triple_in_one_pop(StackNum) ->
  .

-spec triple_in_one_peek(StackNum :: integer()) -> integer().
triple_in_one_peek(StackNum) ->
  .

-spec triple_in_one_is_empty(StackNum :: integer()) -> boolean().
triple_in_one_is_empty(StackNum) ->
  .


%% Your functions will be called as such:
%% triple_in_one_init_(StackSize),
%% triple_in_one_push(StackNum, Value),
%% Param_2 = triple_in_one_pop(StackNum),
%% Param_3 = triple_in_one_peek(StackNum),
%% Param_4 = triple_in_one_is_empty(StackNum),

%% triple_in_one_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule TripleInOne do
  @spec init_(stack_size :: integer) :: any
  def init_(stack_size) do
    
  end

  @spec push(stack_num :: integer, value :: integer) :: any
  def push(stack_num, value) do
    
  end

  @spec pop(stack_num :: integer) :: integer
  def pop(stack_num) do
    
  end

  @spec peek(stack_num :: integer) :: integer
  def peek(stack_num) do
    
  end

  @spec is_empty(stack_num :: integer) :: boolean
  def is_empty(stack_num) do
    
  end
end

# Your functions will be called as such:
# TripleInOne.init_(stack_size)
# TripleInOne.push(stack_num, value)
# param_2 = TripleInOne.pop(stack_num)
# param_3 = TripleInOne.peek(stack_num)
# param_4 = TripleInOne.is_empty(stack_num)

# TripleInOne.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class TripleInOne {
    init(stackSize: Int64) {

    }
    
    func push(stackNum: Int64, value: Int64): Unit {

    }
    
    func pop(stackNum: Int64): Int64 {

    }
    
    func peek(stackNum: Int64): Int64 {

    }
    
    func isEmpty(stackNum: Int64): Bool {

    }
}

/**
 * Your TripleInOne object will be instantiated and called as such:
 * let obj: TripleInOne = TripleInOne(stackSize)
 * obj.push(stackNum,value)
 * let param_2 = obj.pop(stackNum)
 * let param_3 = obj.peek(stackNum)
 * let param_4 = obj.isEmpty(stackNum)
 */
```

