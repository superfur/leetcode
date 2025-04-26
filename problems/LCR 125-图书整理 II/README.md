# LCR 125. 图书整理 II

## 题目描述

<p>读者来到图书馆排队借还书，图书管理员使用两个书车来完成整理借还书的任务。书车中的书从下往上叠加存放，图书管理员每次只能拿取书车顶部的书。排队的读者会有两种操作：</p>

<ul>
	<li><code>push(bookID)</code>：把借阅的书籍还到图书馆。</li>
	<li><code>pop()</code>：从图书馆中借出书籍。</li>
</ul>

<p>为了保持图书的顺序，图书管理员每次取出供读者借阅的书籍是 <strong>最早</strong> 归还到图书馆的书籍。你需要返回 <strong>每次读者借出书的值</strong> 。</p>

<p>如果没有归还的书可以取出，返回&nbsp;<code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["BookQueue", "push", "push", "pop"]
[[], [1], [2], []]
<strong>输出：</strong>[null,null,null,1]
<strong>解释：
</strong>MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.pop(); // return 1, queue is [2]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= bookID &lt;= 10000</code></li>
	<li>最多会对 <code>push</code>、<code>pop</code> 进行 <code>10000</code> 次调用</li>
</ul>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 栈
- 设计
- 队列

## 示例

```
["CQueue","appendTail","deleteHead","deleteHead","deleteHead"]
[[],[3],[],[],[]]
```

## 示例代码

### C++

```cpp
class CQueue {
public:
    CQueue() {
        
    }
    
    void appendTail(int value) {
        
    }
    
    int deleteHead() {
        
    }
};

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue* obj = new CQueue();
 * obj->appendTail(value);
 * int param_2 = obj->deleteHead();
 */
```

### Java

```java
class CQueue {

    public CQueue() {
        
    }
    
    public void appendTail(int value) {
        
    }
    
    public int deleteHead() {
        
    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue obj = new CQueue();
 * obj.appendTail(value);
 * int param_2 = obj.deleteHead();
 */
```

### Python

```python
class CQueue(object):

    def __init__(self):
        

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        

    def deleteHead(self):
        """
        :rtype: int
        """
        


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

### Python3

```python3
class CQueue:

    def __init__(self):
        

    def appendTail(self, value: int) -> None:
        

    def deleteHead(self) -> int:
        


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

### C

```c



typedef struct {
    
} CQueue;


CQueue* cQueueCreate() {
    
}

void cQueueAppendTail(CQueue* obj, int value) {
    
}

int cQueueDeleteHead(CQueue* obj) {
    
}

void cQueueFree(CQueue* obj) {
    
}

/**
 * Your CQueue struct will be instantiated and called as such:
 * CQueue* obj = cQueueCreate();
 * cQueueAppendTail(obj, value);
 
 * int param_2 = cQueueDeleteHead(obj);
 
 * cQueueFree(obj);
*/
```

### C#

```csharp
public class CQueue {

    public CQueue() {
        
    }
    
    public void AppendTail(int value) {
        
    }
    
    public int DeleteHead() {
        
    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue obj = new CQueue();
 * obj.AppendTail(value);
 * int param_2 = obj.DeleteHead();
 */
```

### JavaScript

```javascript

var CQueue = function() {
    
};

/** 
 * @param {number} value
 * @return {void}
 */
CQueue.prototype.appendTail = function(value) {
    
};

/**
 * @return {number}
 */
CQueue.prototype.deleteHead = function() {
    
};

/** 
 * Your CQueue object will be instantiated and called as such:
 * var obj = new CQueue()
 * obj.appendTail(value)
 * var param_2 = obj.deleteHead()
 */
```

### TypeScript

```typescript
class CQueue {
    constructor() {
        
    }

    appendTail(value: number): void {
        
    }

    deleteHead(): number {
        
    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * var obj = new CQueue()
 * obj.appendTail(value)
 * var param_2 = obj.deleteHead()
 */
```

### PHP

```php
class CQueue {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $value
     * @return NULL
     */
    function appendTail($value) {
        
    }
  
    /**
     * @return Integer
     */
    function deleteHead() {
        
    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * $obj = CQueue();
 * $obj->appendTail($value);
 * $ret_2 = $obj->deleteHead();
 */
```

### Swift

```swift

class CQueue {

    init() {
        
    }
    
    func appendTail(_ value: Int) {
        
    }
    
    func deleteHead() -> Int {
        
    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * let obj = CQueue()
 * obj.appendTail(value)
 * let ret_2: Int = obj.deleteHead()
 */
```

### Kotlin

```kotlin
class CQueue() {

    fun appendTail(value: Int) {
        
    }

    fun deleteHead(): Int {
        
    }

}

/**
 * Your CQueue object will be instantiated and called as such:
 * var obj = CQueue()
 * obj.appendTail(value)
 * var param_2 = obj.deleteHead()
 */
```

### Dart

```dart
class CQueue {

  CQueue() {
    
  }
  
  void appendTail(int value) {
    
  }
  
  int deleteHead() {
    
  }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * CQueue obj = CQueue();
 * obj.appendTail(value);
 * int param2 = obj.deleteHead();
 */
```

### Go

```golang
type CQueue struct {
    
}


func Constructor() CQueue {
    
}


func (this *CQueue) AppendTail(value int)  {
    
}


func (this *CQueue) DeleteHead() int {
    
}


/**
 * Your CQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AppendTail(value);
 * param_2 := obj.DeleteHead();
 */
```

### Ruby

```ruby
class CQueue
    def initialize()
        
    end


=begin
    :type value: Integer
    :rtype: Void
=end
    def append_tail(value)
        
    end


=begin
    :rtype: Integer
=end
    def delete_head()
        
    end


end

# Your CQueue object will be instantiated and called as such:
# obj = CQueue.new()
# obj.append_tail(value)
# param_2 = obj.delete_head()
```

### Scala

```scala
class CQueue() {

    def appendTail(value: Int): Unit = {
        
    }

    def deleteHead(): Int = {
        
    }

}

/**
 * Your CQueue object will be instantiated and called as such:
 * val obj = new CQueue()
 * obj.appendTail(value)
 * val param_2 = obj.deleteHead()
 */
```

### Rust

```rust
struct CQueue {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl CQueue {

    fn new() -> Self {
        
    }
    
    fn append_tail(&self, value: i32) {
        
    }
    
    fn delete_head(&self) -> i32 {
        
    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * let obj = CQueue::new();
 * obj.append_tail(value);
 * let ret_2: i32 = obj.delete_head();
 */
```

### Racket

```racket
(define c-queue%
  (class object%
    (super-new)
    
    (init-field)
    
    ; append-tail : exact-integer? -> void?
    (define/public (append-tail value)
      )
    ; delete-head : -> exact-integer?
    (define/public (delete-head)
      )))

;; Your c-queue% object will be instantiated and called as such:
;; (define obj (new c-queue%))
;; (send obj append-tail value)
;; (define param_2 (send obj delete-head))
```

### Erlang

```erlang
-spec c_queue_init_() -> any().
c_queue_init_() ->
  .

-spec c_queue_append_tail(Value :: integer()) -> any().
c_queue_append_tail(Value) ->
  .

-spec c_queue_delete_head() -> integer().
c_queue_delete_head() ->
  .


%% Your functions will be called as such:
%% c_queue_init_(),
%% c_queue_append_tail(Value),
%% Param_2 = c_queue_delete_head(),

%% c_queue_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule CQueue do
  @spec init_() :: any
  def init_() do
    
  end

  @spec append_tail(value :: integer) :: any
  def append_tail(value) do
    
  end

  @spec delete_head() :: integer
  def delete_head() do
    
  end
end

# Your functions will be called as such:
# CQueue.init_()
# CQueue.append_tail(value)
# param_2 = CQueue.delete_head()

# CQueue.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class CQueue {
    init() {

    }
    
    func appendTail(value: Int64): Unit {

    }
    
    func deleteHead(): Int64 {

    }
}

/**
 * Your CQueue object will be instantiated and called as such:
 * let obj: CQueue = CQueue()
 * obj.appendTail(value)
 * let param_2 = obj.deleteHead()
 */
```

