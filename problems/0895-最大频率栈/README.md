# 895. 最大频率栈

## 题目描述

<p>设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出<strong>出现频率</strong>最高的元素。</p>

<p>实现 <code>FreqStack</code>&nbsp;类:</p>

<ul>
	<li><meta charset="UTF-8" /><code>FreqStack()</code>&nbsp;构造一个空的堆栈。</li>
	<li><meta charset="UTF-8" /><code>void push(int val)</code>&nbsp;将一个整数&nbsp;<code>val</code>&nbsp;压入栈顶。</li>
	<li><meta charset="UTF-8" /><code>int pop()</code>&nbsp;删除并返回堆栈中出现频率最高的元素。
	<ul>
		<li>如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
<strong>输出：</strong>[null,null,null,null,null,null,null,5,7,5,4]
<strong>解释：</strong>
FreqStack = new FreqStack();
freqStack.push (5);//堆栈为 [5]
freqStack.push (7);//堆栈是 [5,7]
freqStack.push (5);//堆栈是 [5,7,5]
freqStack.push (7);//堆栈是 [5,7,5,7]
freqStack.push (4);//堆栈是 [5,7,5,7,4]
freqStack.push (5);//堆栈是 [5,7,5,7,4,5]
freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
freqStack.pop ();//返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
freqStack.pop ();//返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= val &lt;= 10<sup>9</sup></code></li>
	<li><code>push</code>&nbsp;和 <code>pop</code>&nbsp;的操作数不大于 <code>2 * 10<sup>4</sup></code>。</li>
	<li>输入保证在调用&nbsp;<code>pop</code>&nbsp;之前堆栈中至少有一个元素。</li>
</ul>


## 难度

Hard

## 标签

- 栈
- 设计
- 哈希表
- 有序集合

## 示例

```
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
```

## 示例代码

### C++

```cpp
class FreqStack {
public:
    FreqStack() {
        
    }
    
    void push(int val) {
        
    }
    
    int pop() {
        
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */
```

### Java

```java
class FreqStack {

    public FreqStack() {
        
    }
    
    public void push(int val) {
        
    }
    
    public int pop() {
        
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */
```

### Python

```python
class FreqStack(object):

    def __init__(self):
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        """
        :rtype: int
        """
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
```

### Python3

```python3
class FreqStack:

    def __init__(self):
        

    def push(self, val: int) -> None:
        

    def pop(self) -> int:
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
```

### C

```c



typedef struct {
    
} FreqStack;


FreqStack* freqStackCreate() {
    
}

void freqStackPush(FreqStack* obj, int val) {
    
}

int freqStackPop(FreqStack* obj) {
    
}

void freqStackFree(FreqStack* obj) {
    
}

/**
 * Your FreqStack struct will be instantiated and called as such:
 * FreqStack* obj = freqStackCreate();
 * freqStackPush(obj, val);
 
 * int param_2 = freqStackPop(obj);
 
 * freqStackFree(obj);
*/
```

### C#

```csharp
public class FreqStack {

    public FreqStack() {
        
    }
    
    public void Push(int val) {
        
    }
    
    public int Pop() {
        
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.Push(val);
 * int param_2 = obj.Pop();
 */
```

### JavaScript

```javascript

var FreqStack = function() {
    
};

/** 
 * @param {number} val
 * @return {void}
 */
FreqStack.prototype.push = function(val) {
    
};

/**
 * @return {number}
 */
FreqStack.prototype.pop = function() {
    
};

/** 
 * Your FreqStack object will be instantiated and called as such:
 * var obj = new FreqStack()
 * obj.push(val)
 * var param_2 = obj.pop()
 */
```

### TypeScript

```typescript
class FreqStack {
    constructor() {
        
    }

    push(val: number): void {
        
    }

    pop(): number {
        
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * var obj = new FreqStack()
 * obj.push(val)
 * var param_2 = obj.pop()
 */
```

### PHP

```php
class FreqStack {
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
     * @return Integer
     */
    function pop() {
        
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * $obj = FreqStack();
 * $obj->push($val);
 * $ret_2 = $obj->pop();
 */
```

### Swift

```swift

class FreqStack {

    init() {
        
    }
    
    func push(_ val: Int) {
        
    }
    
    func pop() -> Int {
        
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * let obj = FreqStack()
 * obj.push(val)
 * let ret_2: Int = obj.pop()
 */
```

### Kotlin

```kotlin
class FreqStack() {

    fun push(`val`: Int) {
        
    }

    fun pop(): Int {
        
    }

}

/**
 * Your FreqStack object will be instantiated and called as such:
 * var obj = FreqStack()
 * obj.push(`val`)
 * var param_2 = obj.pop()
 */
```

### Dart

```dart
class FreqStack {

  FreqStack() {
    
  }
  
  void push(int val) {
    
  }
  
  int pop() {
    
  }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = FreqStack();
 * obj.push(val);
 * int param2 = obj.pop();
 */
```

### Go

```golang
type FreqStack struct {
    
}


func Constructor() FreqStack {
    
}


func (this *FreqStack) Push(val int)  {
    
}


func (this *FreqStack) Pop() int {
    
}


/**
 * Your FreqStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * param_2 := obj.Pop();
 */
```

### Ruby

```ruby
class FreqStack
    def initialize()
        
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


end

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack.new()
# obj.push(val)
# param_2 = obj.pop()
```

### Scala

```scala
class FreqStack() {

    def push(`val`: Int): Unit = {
        
    }

    def pop(): Int = {
        
    }

}

/**
 * Your FreqStack object will be instantiated and called as such:
 * val obj = new FreqStack()
 * obj.push(`val`)
 * val param_2 = obj.pop()
 */
```

### Rust

```rust
struct FreqStack {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FreqStack {

    fn new() -> Self {
        
    }
    
    fn push(&self, val: i32) {
        
    }
    
    fn pop(&self) -> i32 {
        
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * let obj = FreqStack::new();
 * obj.push(val);
 * let ret_2: i32 = obj.pop();
 */
```

### Racket

```racket
(define freq-stack%
  (class object%
    (super-new)
    
    (init-field)
    
    ; push : exact-integer? -> void?
    (define/public (push val)
      )
    ; pop : -> exact-integer?
    (define/public (pop)
      )))

;; Your freq-stack% object will be instantiated and called as such:
;; (define obj (new freq-stack%))
;; (send obj push val)
;; (define param_2 (send obj pop))
```

### Erlang

```erlang
-spec freq_stack_init_() -> any().
freq_stack_init_() ->
  .

-spec freq_stack_push(Val :: integer()) -> any().
freq_stack_push(Val) ->
  .

-spec freq_stack_pop() -> integer().
freq_stack_pop() ->
  .


%% Your functions will be called as such:
%% freq_stack_init_(),
%% freq_stack_push(Val),
%% Param_2 = freq_stack_pop(),

%% freq_stack_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule FreqStack do
  @spec init_() :: any
  def init_() do
    
  end

  @spec push(val :: integer) :: any
  def push(val) do
    
  end

  @spec pop() :: integer
  def pop() do
    
  end
end

# Your functions will be called as such:
# FreqStack.init_()
# FreqStack.push(val)
# param_2 = FreqStack.pop()

# FreqStack.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class FreqStack {
    init() {

    }
    
    func push(val: Int64): Unit {

    }
    
    func pop(): Int64 {

    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * let obj: FreqStack = FreqStack()
 * obj.push(val)
 * let param_2 = obj.pop()
 */
```

