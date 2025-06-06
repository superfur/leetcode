# 1670. 设计前中后队列

## 题目描述

<p>请你设计一个队列，支持在前，中，后三个位置的 <code>push</code> 和 <code>pop</code> 操作。</p>

<p>请你完成 <code>FrontMiddleBack</code> 类：</p>

<ul>
	<li><code>FrontMiddleBack()</code> 初始化队列。</li>
	<li><code>void pushFront(int val)</code> 将 <code>val</code> 添加到队列的 <strong>最前面</strong> 。</li>
	<li><code>void pushMiddle(int val)</code> 将 <code>val</code> 添加到队列的 <strong>正中间</strong> 。</li>
	<li><code>void pushBack(int val)</code> 将 <code>val</code> 添加到队里的 <strong>最后面</strong> 。</li>
	<li><code>int popFront()</code> 将 <strong>最前面</strong> 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 <code>-1</code> 。</li>
	<li><code>int popMiddle()</code> 将 <b>正中间</b> 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 <code>-1</code> 。</li>
	<li><code>int popBack()</code> 将 <strong>最后面</strong> 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 <code>-1</code> 。</li>
</ul>

<p>请注意当有 <strong>两个</strong> 中间位置的时候，选择靠前面的位置进行操作。比方说：</p>

<ul>
	<li>将 <code>6</code> 添加到 <code>[1, 2, 3, 4, 5]</code> 的中间位置，结果数组为 <code>[1, 2, <strong>6</strong>, 3, 4, 5]</code> 。</li>
	<li>从 <code>[1, 2, <strong>3</strong>, 4, 5, 6]</code> 的中间位置弹出元素，返回 <code>3</code> ，数组变为 <code>[1, 2, 4, 5, 6]</code> 。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
<strong>输出：</strong>
[null, null, null, null, null, 1, 3, 4, 2, -1]

<strong>解释：</strong>
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [<strong>1</strong>]
q.pushBack(2);    // [1, <strong>2</strong>]
q.pushMiddle(3);  // [1, <strong>3</strong>, 2]
q.pushMiddle(4);  // [1, <strong>4</strong>, 3, 2]
q.popFront();     // 返回 1 -> [4, 3, 2]
q.popMiddle();    // 返回 3 -> [4, 2]
q.popMiddle();    // 返回 4 -> [2]
q.popBack();      // 返回 2 -> []
q.popFront();     // 返回 -1 -> [] （队列为空）
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= val <= 10<sup>9</sup></code></li>
	<li>最多调用 <code>1000</code> 次 <code>pushFront</code>， <code>pushMiddle</code>， <code>pushBack</code>， <code>popFront</code>， <code>popMiddle</code> 和 <code>popBack</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 队列
- 数组
- 链表
- 数据流

## 提示

1. The constraints are low enough for a brute force, single array approach.
2. For an O(1) per method approach, use 2 double-ended queues: one for the first half and one for the second half.

## 示例

```
["FrontMiddleBackQueue","pushFront","pushBack","pushMiddle","pushMiddle","popFront","popMiddle","popMiddle","popBack","popFront"]
[[],[1],[2],[3],[4],[],[],[],[],[]]
```

## 示例代码

### C++

```cpp
class FrontMiddleBackQueue {
public:
    FrontMiddleBackQueue() {
        
    }
    
    void pushFront(int val) {
        
    }
    
    void pushMiddle(int val) {
        
    }
    
    void pushBack(int val) {
        
    }
    
    int popFront() {
        
    }
    
    int popMiddle() {
        
    }
    
    int popBack() {
        
    }
};

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue* obj = new FrontMiddleBackQueue();
 * obj->pushFront(val);
 * obj->pushMiddle(val);
 * obj->pushBack(val);
 * int param_4 = obj->popFront();
 * int param_5 = obj->popMiddle();
 * int param_6 = obj->popBack();
 */
```

### Java

```java
class FrontMiddleBackQueue {

    public FrontMiddleBackQueue() {
        
    }
    
    public void pushFront(int val) {
        
    }
    
    public void pushMiddle(int val) {
        
    }
    
    public void pushBack(int val) {
        
    }
    
    public int popFront() {
        
    }
    
    public int popMiddle() {
        
    }
    
    public int popBack() {
        
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue obj = new FrontMiddleBackQueue();
 * obj.pushFront(val);
 * obj.pushMiddle(val);
 * obj.pushBack(val);
 * int param_4 = obj.popFront();
 * int param_5 = obj.popMiddle();
 * int param_6 = obj.popBack();
 */
```

### Python

```python
class FrontMiddleBackQueue(object):

    def __init__(self):
        

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def popFront(self):
        """
        :rtype: int
        """
        

    def popMiddle(self):
        """
        :rtype: int
        """
        

    def popBack(self):
        """
        :rtype: int
        """
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
```

### Python3

```python3
class FrontMiddleBackQueue:

    def __init__(self):
        

    def pushFront(self, val: int) -> None:
        

    def pushMiddle(self, val: int) -> None:
        

    def pushBack(self, val: int) -> None:
        

    def popFront(self) -> int:
        

    def popMiddle(self) -> int:
        

    def popBack(self) -> int:
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
```

### C

```c



typedef struct {
    
} FrontMiddleBackQueue;


FrontMiddleBackQueue* frontMiddleBackQueueCreate() {
    
}

void frontMiddleBackQueuePushFront(FrontMiddleBackQueue* obj, int val) {
    
}

void frontMiddleBackQueuePushMiddle(FrontMiddleBackQueue* obj, int val) {
    
}

void frontMiddleBackQueuePushBack(FrontMiddleBackQueue* obj, int val) {
    
}

int frontMiddleBackQueuePopFront(FrontMiddleBackQueue* obj) {
    
}

int frontMiddleBackQueuePopMiddle(FrontMiddleBackQueue* obj) {
    
}

int frontMiddleBackQueuePopBack(FrontMiddleBackQueue* obj) {
    
}

void frontMiddleBackQueueFree(FrontMiddleBackQueue* obj) {
    
}

/**
 * Your FrontMiddleBackQueue struct will be instantiated and called as such:
 * FrontMiddleBackQueue* obj = frontMiddleBackQueueCreate();
 * frontMiddleBackQueuePushFront(obj, val);
 
 * frontMiddleBackQueuePushMiddle(obj, val);
 
 * frontMiddleBackQueuePushBack(obj, val);
 
 * int param_4 = frontMiddleBackQueuePopFront(obj);
 
 * int param_5 = frontMiddleBackQueuePopMiddle(obj);
 
 * int param_6 = frontMiddleBackQueuePopBack(obj);
 
 * frontMiddleBackQueueFree(obj);
*/
```

### C#

```csharp
public class FrontMiddleBackQueue {

    public FrontMiddleBackQueue() {
        
    }
    
    public void PushFront(int val) {
        
    }
    
    public void PushMiddle(int val) {
        
    }
    
    public void PushBack(int val) {
        
    }
    
    public int PopFront() {
        
    }
    
    public int PopMiddle() {
        
    }
    
    public int PopBack() {
        
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue obj = new FrontMiddleBackQueue();
 * obj.PushFront(val);
 * obj.PushMiddle(val);
 * obj.PushBack(val);
 * int param_4 = obj.PopFront();
 * int param_5 = obj.PopMiddle();
 * int param_6 = obj.PopBack();
 */
```

### JavaScript

```javascript

var FrontMiddleBackQueue = function() {
    
};

/** 
 * @param {number} val
 * @return {void}
 */
FrontMiddleBackQueue.prototype.pushFront = function(val) {
    
};

/** 
 * @param {number} val
 * @return {void}
 */
FrontMiddleBackQueue.prototype.pushMiddle = function(val) {
    
};

/** 
 * @param {number} val
 * @return {void}
 */
FrontMiddleBackQueue.prototype.pushBack = function(val) {
    
};

/**
 * @return {number}
 */
FrontMiddleBackQueue.prototype.popFront = function() {
    
};

/**
 * @return {number}
 */
FrontMiddleBackQueue.prototype.popMiddle = function() {
    
};

/**
 * @return {number}
 */
FrontMiddleBackQueue.prototype.popBack = function() {
    
};

/** 
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * var obj = new FrontMiddleBackQueue()
 * obj.pushFront(val)
 * obj.pushMiddle(val)
 * obj.pushBack(val)
 * var param_4 = obj.popFront()
 * var param_5 = obj.popMiddle()
 * var param_6 = obj.popBack()
 */
```

### TypeScript

```typescript
class FrontMiddleBackQueue {
    constructor() {
        
    }

    pushFront(val: number): void {
        
    }

    pushMiddle(val: number): void {
        
    }

    pushBack(val: number): void {
        
    }

    popFront(): number {
        
    }

    popMiddle(): number {
        
    }

    popBack(): number {
        
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * var obj = new FrontMiddleBackQueue()
 * obj.pushFront(val)
 * obj.pushMiddle(val)
 * obj.pushBack(val)
 * var param_4 = obj.popFront()
 * var param_5 = obj.popMiddle()
 * var param_6 = obj.popBack()
 */
```

### PHP

```php
class FrontMiddleBackQueue {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $val
     * @return NULL
     */
    function pushFront($val) {
        
    }
  
    /**
     * @param Integer $val
     * @return NULL
     */
    function pushMiddle($val) {
        
    }
  
    /**
     * @param Integer $val
     * @return NULL
     */
    function pushBack($val) {
        
    }
  
    /**
     * @return Integer
     */
    function popFront() {
        
    }
  
    /**
     * @return Integer
     */
    function popMiddle() {
        
    }
  
    /**
     * @return Integer
     */
    function popBack() {
        
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * $obj = FrontMiddleBackQueue();
 * $obj->pushFront($val);
 * $obj->pushMiddle($val);
 * $obj->pushBack($val);
 * $ret_4 = $obj->popFront();
 * $ret_5 = $obj->popMiddle();
 * $ret_6 = $obj->popBack();
 */
```

### Swift

```swift

class FrontMiddleBackQueue {

    init() {
        
    }
    
    func pushFront(_ val: Int) {
        
    }
    
    func pushMiddle(_ val: Int) {
        
    }
    
    func pushBack(_ val: Int) {
        
    }
    
    func popFront() -> Int {
        
    }
    
    func popMiddle() -> Int {
        
    }
    
    func popBack() -> Int {
        
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * let obj = FrontMiddleBackQueue()
 * obj.pushFront(val)
 * obj.pushMiddle(val)
 * obj.pushBack(val)
 * let ret_4: Int = obj.popFront()
 * let ret_5: Int = obj.popMiddle()
 * let ret_6: Int = obj.popBack()
 */
```

### Kotlin

```kotlin
class FrontMiddleBackQueue() {

    fun pushFront(`val`: Int) {
        
    }

    fun pushMiddle(`val`: Int) {
        
    }

    fun pushBack(`val`: Int) {
        
    }

    fun popFront(): Int {
        
    }

    fun popMiddle(): Int {
        
    }

    fun popBack(): Int {
        
    }

}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * var obj = FrontMiddleBackQueue()
 * obj.pushFront(`val`)
 * obj.pushMiddle(`val`)
 * obj.pushBack(`val`)
 * var param_4 = obj.popFront()
 * var param_5 = obj.popMiddle()
 * var param_6 = obj.popBack()
 */
```

### Dart

```dart
class FrontMiddleBackQueue {

  FrontMiddleBackQueue() {
    
  }
  
  void pushFront(int val) {
    
  }
  
  void pushMiddle(int val) {
    
  }
  
  void pushBack(int val) {
    
  }
  
  int popFront() {
    
  }
  
  int popMiddle() {
    
  }
  
  int popBack() {
    
  }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue obj = FrontMiddleBackQueue();
 * obj.pushFront(val);
 * obj.pushMiddle(val);
 * obj.pushBack(val);
 * int param4 = obj.popFront();
 * int param5 = obj.popMiddle();
 * int param6 = obj.popBack();
 */
```

### Go

```golang
type FrontMiddleBackQueue struct {
    
}


func Constructor() FrontMiddleBackQueue {
    
}


func (this *FrontMiddleBackQueue) PushFront(val int)  {
    
}


func (this *FrontMiddleBackQueue) PushMiddle(val int)  {
    
}


func (this *FrontMiddleBackQueue) PushBack(val int)  {
    
}


func (this *FrontMiddleBackQueue) PopFront() int {
    
}


func (this *FrontMiddleBackQueue) PopMiddle() int {
    
}


func (this *FrontMiddleBackQueue) PopBack() int {
    
}


/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.PushFront(val);
 * obj.PushMiddle(val);
 * obj.PushBack(val);
 * param_4 := obj.PopFront();
 * param_5 := obj.PopMiddle();
 * param_6 := obj.PopBack();
 */
```

### Ruby

```ruby
class FrontMiddleBackQueue
    def initialize()
        
    end


=begin
    :type val: Integer
    :rtype: Void
=end
    def push_front(val)
        
    end


=begin
    :type val: Integer
    :rtype: Void
=end
    def push_middle(val)
        
    end


=begin
    :type val: Integer
    :rtype: Void
=end
    def push_back(val)
        
    end


=begin
    :rtype: Integer
=end
    def pop_front()
        
    end


=begin
    :rtype: Integer
=end
    def pop_middle()
        
    end


=begin
    :rtype: Integer
=end
    def pop_back()
        
    end


end

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue.new()
# obj.push_front(val)
# obj.push_middle(val)
# obj.push_back(val)
# param_4 = obj.pop_front()
# param_5 = obj.pop_middle()
# param_6 = obj.pop_back()
```

### Scala

```scala
class FrontMiddleBackQueue() {

    def pushFront(`val`: Int): Unit = {
        
    }

    def pushMiddle(`val`: Int): Unit = {
        
    }

    def pushBack(`val`: Int): Unit = {
        
    }

    def popFront(): Int = {
        
    }

    def popMiddle(): Int = {
        
    }

    def popBack(): Int = {
        
    }

}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * val obj = new FrontMiddleBackQueue()
 * obj.pushFront(`val`)
 * obj.pushMiddle(`val`)
 * obj.pushBack(`val`)
 * val param_4 = obj.popFront()
 * val param_5 = obj.popMiddle()
 * val param_6 = obj.popBack()
 */
```

### Rust

```rust
struct FrontMiddleBackQueue {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FrontMiddleBackQueue {

    fn new() -> Self {
        
    }
    
    fn push_front(&self, val: i32) {
        
    }
    
    fn push_middle(&self, val: i32) {
        
    }
    
    fn push_back(&self, val: i32) {
        
    }
    
    fn pop_front(&self) -> i32 {
        
    }
    
    fn pop_middle(&self) -> i32 {
        
    }
    
    fn pop_back(&self) -> i32 {
        
    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * let obj = FrontMiddleBackQueue::new();
 * obj.push_front(val);
 * obj.push_middle(val);
 * obj.push_back(val);
 * let ret_4: i32 = obj.pop_front();
 * let ret_5: i32 = obj.pop_middle();
 * let ret_6: i32 = obj.pop_back();
 */
```

### Racket

```racket
(define front-middle-back-queue%
  (class object%
    (super-new)
    
    (init-field)
    
    ; push-front : exact-integer? -> void?
    (define/public (push-front val)
      )
    ; push-middle : exact-integer? -> void?
    (define/public (push-middle val)
      )
    ; push-back : exact-integer? -> void?
    (define/public (push-back val)
      )
    ; pop-front : -> exact-integer?
    (define/public (pop-front)
      )
    ; pop-middle : -> exact-integer?
    (define/public (pop-middle)
      )
    ; pop-back : -> exact-integer?
    (define/public (pop-back)
      )))

;; Your front-middle-back-queue% object will be instantiated and called as such:
;; (define obj (new front-middle-back-queue%))
;; (send obj push-front val)
;; (send obj push-middle val)
;; (send obj push-back val)
;; (define param_4 (send obj pop-front))
;; (define param_5 (send obj pop-middle))
;; (define param_6 (send obj pop-back))
```

### Erlang

```erlang
-spec front_middle_back_queue_init_() -> any().
front_middle_back_queue_init_() ->
  .

-spec front_middle_back_queue_push_front(Val :: integer()) -> any().
front_middle_back_queue_push_front(Val) ->
  .

-spec front_middle_back_queue_push_middle(Val :: integer()) -> any().
front_middle_back_queue_push_middle(Val) ->
  .

-spec front_middle_back_queue_push_back(Val :: integer()) -> any().
front_middle_back_queue_push_back(Val) ->
  .

-spec front_middle_back_queue_pop_front() -> integer().
front_middle_back_queue_pop_front() ->
  .

-spec front_middle_back_queue_pop_middle() -> integer().
front_middle_back_queue_pop_middle() ->
  .

-spec front_middle_back_queue_pop_back() -> integer().
front_middle_back_queue_pop_back() ->
  .


%% Your functions will be called as such:
%% front_middle_back_queue_init_(),
%% front_middle_back_queue_push_front(Val),
%% front_middle_back_queue_push_middle(Val),
%% front_middle_back_queue_push_back(Val),
%% Param_4 = front_middle_back_queue_pop_front(),
%% Param_5 = front_middle_back_queue_pop_middle(),
%% Param_6 = front_middle_back_queue_pop_back(),

%% front_middle_back_queue_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule FrontMiddleBackQueue do
  @spec init_() :: any
  def init_() do
    
  end

  @spec push_front(val :: integer) :: any
  def push_front(val) do
    
  end

  @spec push_middle(val :: integer) :: any
  def push_middle(val) do
    
  end

  @spec push_back(val :: integer) :: any
  def push_back(val) do
    
  end

  @spec pop_front() :: integer
  def pop_front() do
    
  end

  @spec pop_middle() :: integer
  def pop_middle() do
    
  end

  @spec pop_back() :: integer
  def pop_back() do
    
  end
end

# Your functions will be called as such:
# FrontMiddleBackQueue.init_()
# FrontMiddleBackQueue.push_front(val)
# FrontMiddleBackQueue.push_middle(val)
# FrontMiddleBackQueue.push_back(val)
# param_4 = FrontMiddleBackQueue.pop_front()
# param_5 = FrontMiddleBackQueue.pop_middle()
# param_6 = FrontMiddleBackQueue.pop_back()

# FrontMiddleBackQueue.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class FrontMiddleBackQueue {
    init() {

    }
    
    func pushFront(val: Int64): Unit {

    }
    
    func pushMiddle(val: Int64): Unit {

    }
    
    func pushBack(val: Int64): Unit {

    }
    
    func popFront(): Int64 {

    }
    
    func popMiddle(): Int64 {

    }
    
    func popBack(): Int64 {

    }
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * let obj: FrontMiddleBackQueue = FrontMiddleBackQueue()
 * obj.pushFront(val)
 * obj.pushMiddle(val)
 * obj.pushBack(val)
 * let param_4 = obj.popFront()
 * let param_5 = obj.popMiddle()
 * let param_6 = obj.popBack()
 */
```

