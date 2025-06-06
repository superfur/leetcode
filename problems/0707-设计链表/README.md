# 707. 设计链表

## 题目描述

<p>你可以选择使用单链表或者双链表，设计并实现自己的链表。</p>

<p>单链表中的节点应该具备两个属性：<code>val</code> 和 <code>next</code> 。<code>val</code> 是当前节点的值，<code>next</code> 是指向下一个节点的指针/引用。</p>

<p>如果是双向链表，则还需要属性&nbsp;<code>prev</code>&nbsp;以指示链表中的上一个节点。假设链表中的所有节点下标从 <strong>0</strong> 开始。</p>

<p>实现 <code>MyLinkedList</code> 类：</p>

<ul>
	<li><code>MyLinkedList()</code> 初始化 <code>MyLinkedList</code> 对象。</li>
	<li><code>int get(int index)</code> 获取链表中下标为 <code>index</code> 的节点的值。如果下标无效，则返回 <code>-1</code> 。</li>
	<li><code>void addAtHead(int val)</code> 将一个值为 <code>val</code> 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。</li>
	<li><code>void addAtTail(int val)</code> 将一个值为 <code>val</code> 的节点追加到链表中作为链表的最后一个元素。</li>
	<li><code>void addAtIndex(int index, int val)</code> 将一个值为 <code>val</code> 的节点插入到链表中下标为 <code>index</code> 的节点之前。如果 <code>index</code> 等于链表的长度，那么该节点会被追加到链表的末尾。如果 <code>index</code> 比长度更大，该节点将 <strong>不会插入</strong> 到链表中。</li>
	<li><code>void deleteAtIndex(int index)</code> 如果下标有效，则删除链表中下标为 <code>index</code> 的节点。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例：</strong></p>

<pre>
<strong>输入</strong>
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
<strong>输出</strong>
[null, null, null, null, 2, null, 3]

<strong>解释</strong>
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // 链表变为 1-&gt;2-&gt;3
myLinkedList.get(1);              // 返回 2
myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1-&gt;3
myLinkedList.get(1);              // 返回 3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= index, val &lt;= 1000</code></li>
	<li>请不要使用内置的 LinkedList 库。</li>
	<li>调用 <code>get</code>、<code>addAtHead</code>、<code>addAtTail</code>、<code>addAtIndex</code> 和 <code>deleteAtIndex</code> 的次数不超过 <code>2000</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 链表

## 示例

```
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
```

## 示例代码

### C++

```cpp
class MyLinkedList {
public:
    MyLinkedList() {
        
    }
    
    int get(int index) {
        
    }
    
    void addAtHead(int val) {
        
    }
    
    void addAtTail(int val) {
        
    }
    
    void addAtIndex(int index, int val) {
        
    }
    
    void deleteAtIndex(int index) {
        
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
```

### Java

```java
class MyLinkedList {

    public MyLinkedList() {
        
    }
    
    public int get(int index) {
        
    }
    
    public void addAtHead(int val) {
        
    }
    
    public void addAtTail(int val) {
        
    }
    
    public void addAtIndex(int index, int val) {
        
    }
    
    public void deleteAtIndex(int index) {
        
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
```

### Python

```python
class MyLinkedList(object):

    def __init__(self):
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```

### Python3

```python3
class MyLinkedList:

    def __init__(self):
        

    def get(self, index: int) -> int:
        

    def addAtHead(self, val: int) -> None:
        

    def addAtTail(self, val: int) -> None:
        

    def addAtIndex(self, index: int, val: int) -> None:
        

    def deleteAtIndex(self, index: int) -> None:
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```

### C

```c



typedef struct {
    
} MyLinkedList;


MyLinkedList* myLinkedListCreate() {
    
}

int myLinkedListGet(MyLinkedList* obj, int index) {
    
}

void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    
}

void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    
}

void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    
}

void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    
}

void myLinkedListFree(MyLinkedList* obj) {
    
}

/**
 * Your MyLinkedList struct will be instantiated and called as such:
 * MyLinkedList* obj = myLinkedListCreate();
 * int param_1 = myLinkedListGet(obj, index);
 
 * myLinkedListAddAtHead(obj, val);
 
 * myLinkedListAddAtTail(obj, val);
 
 * myLinkedListAddAtIndex(obj, index, val);
 
 * myLinkedListDeleteAtIndex(obj, index);
 
 * myLinkedListFree(obj);
*/
```

### C#

```csharp
public class MyLinkedList {

    public MyLinkedList() {
        
    }
    
    public int Get(int index) {
        
    }
    
    public void AddAtHead(int val) {
        
    }
    
    public void AddAtTail(int val) {
        
    }
    
    public void AddAtIndex(int index, int val) {
        
    }
    
    public void DeleteAtIndex(int index) {
        
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */
```

### JavaScript

```javascript

var MyLinkedList = function() {
    
};

/** 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function(index) {
    
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function(val) {
    
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function(val) {
    
};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function(index, val) {
    
};

/** 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function(index) {
    
};

/** 
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */
```

### TypeScript

```typescript
class MyLinkedList {
    constructor() {
        
    }

    get(index: number): number {
        
    }

    addAtHead(val: number): void {
        
    }

    addAtTail(val: number): void {
        
    }

    addAtIndex(index: number, val: number): void {
        
    }

    deleteAtIndex(index: number): void {
        
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */
```

### PHP

```php
class MyLinkedList {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $index
     * @return Integer
     */
    function get($index) {
        
    }
  
    /**
     * @param Integer $val
     * @return NULL
     */
    function addAtHead($val) {
        
    }
  
    /**
     * @param Integer $val
     * @return NULL
     */
    function addAtTail($val) {
        
    }
  
    /**
     * @param Integer $index
     * @param Integer $val
     * @return NULL
     */
    function addAtIndex($index, $val) {
        
    }
  
    /**
     * @param Integer $index
     * @return NULL
     */
    function deleteAtIndex($index) {
        
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * $obj = MyLinkedList();
 * $ret_1 = $obj->get($index);
 * $obj->addAtHead($val);
 * $obj->addAtTail($val);
 * $obj->addAtIndex($index, $val);
 * $obj->deleteAtIndex($index);
 */
```

### Swift

```swift

class MyLinkedList {

    init() {
        
    }
    
    func get(_ index: Int) -> Int {
        
    }
    
    func addAtHead(_ val: Int) {
        
    }
    
    func addAtTail(_ val: Int) {
        
    }
    
    func addAtIndex(_ index: Int, _ val: Int) {
        
    }
    
    func deleteAtIndex(_ index: Int) {
        
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * let obj = MyLinkedList()
 * let ret_1: Int = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index, val)
 * obj.deleteAtIndex(index)
 */
```

### Kotlin

```kotlin
class MyLinkedList() {

    fun get(index: Int): Int {
        
    }

    fun addAtHead(`val`: Int) {
        
    }

    fun addAtTail(`val`: Int) {
        
    }

    fun addAtIndex(index: Int, `val`: Int) {
        
    }

    fun deleteAtIndex(index: Int) {
        
    }

}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(`val`)
 * obj.addAtTail(`val`)
 * obj.addAtIndex(index,`val`)
 * obj.deleteAtIndex(index)
 */
```

### Dart

```dart
class MyLinkedList {

  MyLinkedList() {
    
  }
  
  int get(int index) {
    
  }
  
  void addAtHead(int val) {
    
  }
  
  void addAtTail(int val) {
    
  }
  
  void addAtIndex(int index, int val) {
    
  }
  
  void deleteAtIndex(int index) {
    
  }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = MyLinkedList();
 * int param1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
```

### Go

```golang
type MyLinkedList struct {
    
}


func Constructor() MyLinkedList {
    
}


func (this *MyLinkedList) Get(index int) int {
    
}


func (this *MyLinkedList) AddAtHead(val int)  {
    
}


func (this *MyLinkedList) AddAtTail(val int)  {
    
}


func (this *MyLinkedList) AddAtIndex(index int, val int)  {
    
}


func (this *MyLinkedList) DeleteAtIndex(index int)  {
    
}


/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */
```

### Ruby

```ruby
class MyLinkedList
    def initialize()
        
    end


=begin
    :type index: Integer
    :rtype: Integer
=end
    def get(index)
        
    end


=begin
    :type val: Integer
    :rtype: Void
=end
    def add_at_head(val)
        
    end


=begin
    :type val: Integer
    :rtype: Void
=end
    def add_at_tail(val)
        
    end


=begin
    :type index: Integer
    :type val: Integer
    :rtype: Void
=end
    def add_at_index(index, val)
        
    end


=begin
    :type index: Integer
    :rtype: Void
=end
    def delete_at_index(index)
        
    end


end

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList.new()
# param_1 = obj.get(index)
# obj.add_at_head(val)
# obj.add_at_tail(val)
# obj.add_at_index(index, val)
# obj.delete_at_index(index)
```

### Scala

```scala
class MyLinkedList() {

    def get(index: Int): Int = {
        
    }

    def addAtHead(`val`: Int): Unit = {
        
    }

    def addAtTail(`val`: Int): Unit = {
        
    }

    def addAtIndex(index: Int, `val`: Int): Unit = {
        
    }

    def deleteAtIndex(index: Int): Unit = {
        
    }

}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * val obj = new MyLinkedList()
 * val param_1 = obj.get(index)
 * obj.addAtHead(`val`)
 * obj.addAtTail(`val`)
 * obj.addAtIndex(index,`val`)
 * obj.deleteAtIndex(index)
 */
```

### Rust

```rust
struct MyLinkedList {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyLinkedList {

    fn new() -> Self {
        
    }
    
    fn get(&self, index: i32) -> i32 {
        
    }
    
    fn add_at_head(&self, val: i32) {
        
    }
    
    fn add_at_tail(&self, val: i32) {
        
    }
    
    fn add_at_index(&self, index: i32, val: i32) {
        
    }
    
    fn delete_at_index(&self, index: i32) {
        
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * let obj = MyLinkedList::new();
 * let ret_1: i32 = obj.get(index);
 * obj.add_at_head(val);
 * obj.add_at_tail(val);
 * obj.add_at_index(index, val);
 * obj.delete_at_index(index);
 */
```

### Racket

```racket
(define my-linked-list%
  (class object%
    (super-new)
    
    (init-field)
    
    ; get : exact-integer? -> exact-integer?
    (define/public (get index)
      )
    ; add-at-head : exact-integer? -> void?
    (define/public (add-at-head val)
      )
    ; add-at-tail : exact-integer? -> void?
    (define/public (add-at-tail val)
      )
    ; add-at-index : exact-integer? exact-integer? -> void?
    (define/public (add-at-index index val)
      )
    ; delete-at-index : exact-integer? -> void?
    (define/public (delete-at-index index)
      )))

;; Your my-linked-list% object will be instantiated and called as such:
;; (define obj (new my-linked-list%))
;; (define param_1 (send obj get index))
;; (send obj add-at-head val)
;; (send obj add-at-tail val)
;; (send obj add-at-index index val)
;; (send obj delete-at-index index)
```

### Erlang

```erlang
-spec my_linked_list_init_() -> any().
my_linked_list_init_() ->
  .

-spec my_linked_list_get(Index :: integer()) -> integer().
my_linked_list_get(Index) ->
  .

-spec my_linked_list_add_at_head(Val :: integer()) -> any().
my_linked_list_add_at_head(Val) ->
  .

-spec my_linked_list_add_at_tail(Val :: integer()) -> any().
my_linked_list_add_at_tail(Val) ->
  .

-spec my_linked_list_add_at_index(Index :: integer(), Val :: integer()) -> any().
my_linked_list_add_at_index(Index, Val) ->
  .

-spec my_linked_list_delete_at_index(Index :: integer()) -> any().
my_linked_list_delete_at_index(Index) ->
  .


%% Your functions will be called as such:
%% my_linked_list_init_(),
%% Param_1 = my_linked_list_get(Index),
%% my_linked_list_add_at_head(Val),
%% my_linked_list_add_at_tail(Val),
%% my_linked_list_add_at_index(Index, Val),
%% my_linked_list_delete_at_index(Index),

%% my_linked_list_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MyLinkedList do
  @spec init_() :: any
  def init_() do
    
  end

  @spec get(index :: integer) :: integer
  def get(index) do
    
  end

  @spec add_at_head(val :: integer) :: any
  def add_at_head(val) do
    
  end

  @spec add_at_tail(val :: integer) :: any
  def add_at_tail(val) do
    
  end

  @spec add_at_index(index :: integer, val :: integer) :: any
  def add_at_index(index, val) do
    
  end

  @spec delete_at_index(index :: integer) :: any
  def delete_at_index(index) do
    
  end
end

# Your functions will be called as such:
# MyLinkedList.init_()
# param_1 = MyLinkedList.get(index)
# MyLinkedList.add_at_head(val)
# MyLinkedList.add_at_tail(val)
# MyLinkedList.add_at_index(index, val)
# MyLinkedList.delete_at_index(index)

# MyLinkedList.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MyLinkedList {
    init() {

    }
    
    func get(index: Int64): Int64 {

    }
    
    func addAtHead(val: Int64): Unit {

    }
    
    func addAtTail(val: Int64): Unit {

    }
    
    func addAtIndex(index: Int64, val: Int64): Unit {

    }
    
    func deleteAtIndex(index: Int64): Unit {

    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * let obj: MyLinkedList = MyLinkedList()
 * let param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */
```

