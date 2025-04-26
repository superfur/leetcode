# 1172. 餐盘栈

## 题目描述

<p>我们把无限数量 &infin; 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量&nbsp;<code>capacity</code> 都相同。</p>

<p>实现一个叫「餐盘」的类&nbsp;<code>DinnerPlates</code>：</p>

<ul>
	<li><code>DinnerPlates(int capacity)</code>&nbsp;- 给出栈的最大容量&nbsp;<code>capacity</code>。</li>
	<li><code>void push(int val)</code>&nbsp;- 将给出的正整数&nbsp;<code>val</code>&nbsp;推入&nbsp;<strong>从左往右第一个&nbsp;</strong>没有满的栈。</li>
	<li><code>int pop()</code>&nbsp;- 返回&nbsp;<strong>从右往左第一个&nbsp;</strong>非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回&nbsp;<code>-1</code>。</li>
	<li><code>int popAtStack(int index)</code>&nbsp;- 返回编号&nbsp;<code>index</code>&nbsp;的栈顶部的值，并将其从栈中删除；如果编号&nbsp;<code>index</code>&nbsp;的栈是空的，请返回 <code>-1</code>。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入： </strong>
[&quot;DinnerPlates&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;push&quot;,&quot;popAtStack&quot;,&quot;push&quot;,&quot;push&quot;,&quot;popAtStack&quot;,&quot;popAtStack&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;,&quot;pop&quot;]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
<strong>输出：</strong>
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

<strong>解释：</strong>
DinnerPlates D = DinnerPlates(2);  // 初始化，栈最大容量 capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // 栈的现状为：    2 &nbsp;4
&nbsp;                                   1 &nbsp;3 &nbsp;5
                                    ﹈ ﹈ ﹈
D.popAtStack(0);   // 返回 2。栈的现状为：     &nbsp;4
            &nbsp;                             1 &nbsp;3 &nbsp;5
                                          ﹈ ﹈ ﹈
D.push(20);        // 栈的现状为：  20  4
&nbsp;                                  1 &nbsp;3 &nbsp;5
                                   ﹈ ﹈ ﹈
D.push(21);        // 栈的现状为：  20  4 21
&nbsp;                                  1 &nbsp;3 &nbsp;5
                                   ﹈ ﹈ ﹈
D.popAtStack(0);   // 返回 20。栈的现状为：       4 21
             &nbsp;                              1 &nbsp;3 &nbsp;5
                                            ﹈ ﹈ ﹈
D.popAtStack(2);   // 返回 21。栈的现状为：       4
             &nbsp;                              1 &nbsp;3 &nbsp;5
                                            ﹈ ﹈ ﹈ 
D.pop()            // 返回 5。栈的现状为：        4
             &nbsp;                              1 &nbsp;3 
                                            ﹈ ﹈  
D.pop()            // 返回 4。栈的现状为：    1  3 
                                           ﹈ ﹈   
D.pop()            // 返回 3。栈的现状为：    1 
                                           ﹈   
D.pop()            // 返回 1。现在没有栈。
D.pop()            // 返回 -1。仍然没有栈。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= capacity&nbsp;&lt;= 20000</code></li>
	<li><code>1 &lt;= val&nbsp;&lt;= 20000</code></li>
	<li><code>0 &lt;= index&nbsp;&lt;= 100000</code></li>
	<li>最多会对&nbsp;<code>push</code>，<code>pop</code>，和&nbsp;<code>popAtStack</code>&nbsp;进行 <code>200000</code> 次调用。</li>
</ul>


## 难度

Hard

## 标签

- 栈
- 设计
- 哈希表
- 堆（优先队列）

## 提示

1. Use a data structure to save the plate status. You may need to operate the exact index. Maintain the leftmost vacant stack and the rightmost non-empty stack.
2. Use a list of stack to store the plate status. Use heap to maintain the leftmost and rightmost valid stack.

## 示例

```
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
```

## 示例代码

### C++

```cpp
class DinnerPlates {
public:
    DinnerPlates(int capacity) {
        
    }
    
    void push(int val) {
        
    }
    
    int pop() {
        
    }
    
    int popAtStack(int index) {
        
    }
};

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * DinnerPlates* obj = new DinnerPlates(capacity);
 * obj->push(val);
 * int param_2 = obj->pop();
 * int param_3 = obj->popAtStack(index);
 */
```

### Java

```java
class DinnerPlates {

    public DinnerPlates(int capacity) {
        
    }
    
    public void push(int val) {
        
    }
    
    public int pop() {
        
    }
    
    public int popAtStack(int index) {
        
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * DinnerPlates obj = new DinnerPlates(capacity);
 * obj.push(val);
 * int param_2 = obj.pop();
 * int param_3 = obj.popAtStack(index);
 */
```

### Python

```python
class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
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
        

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
```

### Python3

```python3
class DinnerPlates:

    def __init__(self, capacity: int):
        

    def push(self, val: int) -> None:
        

    def pop(self) -> int:
        

    def popAtStack(self, index: int) -> int:
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
```

### C

```c



typedef struct {
    
} DinnerPlates;


DinnerPlates* dinnerPlatesCreate(int capacity) {
    
}

void dinnerPlatesPush(DinnerPlates* obj, int val) {
    
}

int dinnerPlatesPop(DinnerPlates* obj) {
    
}

int dinnerPlatesPopAtStack(DinnerPlates* obj, int index) {
    
}

void dinnerPlatesFree(DinnerPlates* obj) {
    
}

/**
 * Your DinnerPlates struct will be instantiated and called as such:
 * DinnerPlates* obj = dinnerPlatesCreate(capacity);
 * dinnerPlatesPush(obj, val);
 
 * int param_2 = dinnerPlatesPop(obj);
 
 * int param_3 = dinnerPlatesPopAtStack(obj, index);
 
 * dinnerPlatesFree(obj);
*/
```

### C#

```csharp
public class DinnerPlates {

    public DinnerPlates(int capacity) {
        
    }
    
    public void Push(int val) {
        
    }
    
    public int Pop() {
        
    }
    
    public int PopAtStack(int index) {
        
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * DinnerPlates obj = new DinnerPlates(capacity);
 * obj.Push(val);
 * int param_2 = obj.Pop();
 * int param_3 = obj.PopAtStack(index);
 */
```

### JavaScript

```javascript
/**
 * @param {number} capacity
 */
var DinnerPlates = function(capacity) {
    
};

/** 
 * @param {number} val
 * @return {void}
 */
DinnerPlates.prototype.push = function(val) {
    
};

/**
 * @return {number}
 */
DinnerPlates.prototype.pop = function() {
    
};

/** 
 * @param {number} index
 * @return {number}
 */
DinnerPlates.prototype.popAtStack = function(index) {
    
};

/** 
 * Your DinnerPlates object will be instantiated and called as such:
 * var obj = new DinnerPlates(capacity)
 * obj.push(val)
 * var param_2 = obj.pop()
 * var param_3 = obj.popAtStack(index)
 */
```

### TypeScript

```typescript
class DinnerPlates {
    constructor(capacity: number) {
        
    }

    push(val: number): void {
        
    }

    pop(): number {
        
    }

    popAtStack(index: number): number {
        
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * var obj = new DinnerPlates(capacity)
 * obj.push(val)
 * var param_2 = obj.pop()
 * var param_3 = obj.popAtStack(index)
 */
```

### PHP

```php
class DinnerPlates {
    /**
     * @param Integer $capacity
     */
    function __construct($capacity) {
        
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
    function popAtStack($index) {
        
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * $obj = DinnerPlates($capacity);
 * $obj->push($val);
 * $ret_2 = $obj->pop();
 * $ret_3 = $obj->popAtStack($index);
 */
```

### Swift

```swift

class DinnerPlates {

    init(_ capacity: Int) {
        
    }
    
    func push(_ val: Int) {
        
    }
    
    func pop() -> Int {
        
    }
    
    func popAtStack(_ index: Int) -> Int {
        
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * let obj = DinnerPlates(capacity)
 * obj.push(val)
 * let ret_2: Int = obj.pop()
 * let ret_3: Int = obj.popAtStack(index)
 */
```

### Kotlin

```kotlin
class DinnerPlates(capacity: Int) {

    fun push(`val`: Int) {
        
    }

    fun pop(): Int {
        
    }

    fun popAtStack(index: Int): Int {
        
    }

}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * var obj = DinnerPlates(capacity)
 * obj.push(`val`)
 * var param_2 = obj.pop()
 * var param_3 = obj.popAtStack(index)
 */
```

### Dart

```dart
class DinnerPlates {

  DinnerPlates(int capacity) {
    
  }
  
  void push(int val) {
    
  }
  
  int pop() {
    
  }
  
  int popAtStack(int index) {
    
  }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * DinnerPlates obj = DinnerPlates(capacity);
 * obj.push(val);
 * int param2 = obj.pop();
 * int param3 = obj.popAtStack(index);
 */
```

### Go

```golang
type DinnerPlates struct {
    
}


func Constructor(capacity int) DinnerPlates {
    
}


func (this *DinnerPlates) Push(val int)  {
    
}


func (this *DinnerPlates) Pop() int {
    
}


func (this *DinnerPlates) PopAtStack(index int) int {
    
}


/**
 * Your DinnerPlates object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * obj.Push(val);
 * param_2 := obj.Pop();
 * param_3 := obj.PopAtStack(index);
 */
```

### Ruby

```ruby
class DinnerPlates

=begin
    :type capacity: Integer
=end
    def initialize(capacity)
        
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
    def pop_at_stack(index)
        
    end


end

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates.new(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.pop_at_stack(index)
```

### Scala

```scala
class DinnerPlates(_capacity: Int) {

    def push(`val`: Int): Unit = {
        
    }

    def pop(): Int = {
        
    }

    def popAtStack(index: Int): Int = {
        
    }

}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * val obj = new DinnerPlates(capacity)
 * obj.push(`val`)
 * val param_2 = obj.pop()
 * val param_3 = obj.popAtStack(index)
 */
```

### Rust

```rust
struct DinnerPlates {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl DinnerPlates {

    fn new(capacity: i32) -> Self {
        
    }
    
    fn push(&self, val: i32) {
        
    }
    
    fn pop(&self) -> i32 {
        
    }
    
    fn pop_at_stack(&self, index: i32) -> i32 {
        
    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * let obj = DinnerPlates::new(capacity);
 * obj.push(val);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.pop_at_stack(index);
 */
```

### Racket

```racket
(define dinner-plates%
  (class object%
    (super-new)
    
    ; capacity : exact-integer?
    (init-field
      capacity)
    
    ; push : exact-integer? -> void?
    (define/public (push val)
      )
    ; pop : -> exact-integer?
    (define/public (pop)
      )
    ; pop-at-stack : exact-integer? -> exact-integer?
    (define/public (pop-at-stack index)
      )))

;; Your dinner-plates% object will be instantiated and called as such:
;; (define obj (new dinner-plates% [capacity capacity]))
;; (send obj push val)
;; (define param_2 (send obj pop))
;; (define param_3 (send obj pop-at-stack index))
```

### Erlang

```erlang
-spec dinner_plates_init_(Capacity :: integer()) -> any().
dinner_plates_init_(Capacity) ->
  .

-spec dinner_plates_push(Val :: integer()) -> any().
dinner_plates_push(Val) ->
  .

-spec dinner_plates_pop() -> integer().
dinner_plates_pop() ->
  .

-spec dinner_plates_pop_at_stack(Index :: integer()) -> integer().
dinner_plates_pop_at_stack(Index) ->
  .


%% Your functions will be called as such:
%% dinner_plates_init_(Capacity),
%% dinner_plates_push(Val),
%% Param_2 = dinner_plates_pop(),
%% Param_3 = dinner_plates_pop_at_stack(Index),

%% dinner_plates_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule DinnerPlates do
  @spec init_(capacity :: integer) :: any
  def init_(capacity) do
    
  end

  @spec push(val :: integer) :: any
  def push(val) do
    
  end

  @spec pop() :: integer
  def pop() do
    
  end

  @spec pop_at_stack(index :: integer) :: integer
  def pop_at_stack(index) do
    
  end
end

# Your functions will be called as such:
# DinnerPlates.init_(capacity)
# DinnerPlates.push(val)
# param_2 = DinnerPlates.pop()
# param_3 = DinnerPlates.pop_at_stack(index)

# DinnerPlates.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class DinnerPlates {
    init(capacity: Int64) {

    }
    
    func push(val: Int64): Unit {

    }
    
    func pop(): Int64 {

    }
    
    func popAtStack(index: Int64): Int64 {

    }
}

/**
 * Your DinnerPlates object will be instantiated and called as such:
 * let obj: DinnerPlates = DinnerPlates(capacity)
 * obj.push(val)
 * let param_2 = obj.pop()
 * let param_3 = obj.popAtStack(index)
 */
```

