# 1206. 设计跳表

## 题目描述

<p>不使用任何库函数，设计一个 <strong>跳表</strong> 。</p>

<p><strong>跳表</strong> 是在 <code>O(log(n))</code> 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。</p>

<p>例如，一个跳表包含 <code>[30, 40, 50, 60, 70, 90]</code> ，然后增加 <code>80</code>、<code>45</code> 到跳表中，以下图的方式操作：</p>

<p><img alt="" src="https://pic.leetcode.cn/1702370216-mKQcTt-1506_skiplist.gif" style="width: 500px; height: 173px;" /></p>

<p>跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 <code>O(n)</code>。跳表的每一个操作的平均时间复杂度是 <code>O(log(n))</code>，空间复杂度是 <code>O(n)</code>。</p>

<p>了解更多 :&nbsp;<a href="https://oi-wiki.org/ds/skiplist/" target="_blank">https://oi-wiki.org/ds/skiplist/</a></p>

<p>在本题中，你的设计应该要包含这些函数：</p>

<ul>
	<li><code>bool search(int target)</code> : 返回target是否存在于跳表中。</li>
	<li><code>void add(int num)</code>:&nbsp;插入一个元素到跳表。</li>
	<li><code>bool erase(int num)</code>: 在跳表中删除一个值，如果&nbsp;<code>num</code>&nbsp;不存在，直接返回false. 如果存在多个&nbsp;<code>num</code>&nbsp;，删除其中任意一个即可。</li>
</ul>

<p>注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<b>输入</b>
["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
<strong>输出</strong>
[null, null, null, null, false, null, true, false, true, false]

<strong>解释</strong>
Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // 返回 false
skiplist.add(4);
skiplist.search(1);   // 返回 true
skiplist.erase(0);    // 返回 false，0 不在跳表中
skiplist.erase(1);    // 返回 true
skiplist.search(1);   // 返回 false，1 已被擦除
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>0 &lt;= num, target &lt;= 2 * 10<sup>4</sup></code></li>
	<li>调用<code>search</code>, <code>add</code>, &nbsp;<code>erase</code>操作次数不大于&nbsp;<code>5 * 10<sup>4</sup></code>&nbsp;</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 链表

## 示例

```
["Skiplist","add","add","add","search","add","search","erase","erase","search"]
[[],[1],[2],[3],[0],[4],[1],[0],[1],[1]]
```

## 示例代码

### C++

```cpp
class Skiplist {
public:
    Skiplist() {
        
    }
    
    bool search(int target) {
        
    }
    
    void add(int num) {
        
    }
    
    bool erase(int num) {
        
    }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
 */
```

### Java

```java
class Skiplist {

    public Skiplist() {
        
    }
    
    public boolean search(int target) {
        
    }
    
    public void add(int num) {
        
    }
    
    public boolean erase(int num) {
        
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist obj = new Skiplist();
 * boolean param_1 = obj.search(target);
 * obj.add(num);
 * boolean param_3 = obj.erase(num);
 */
```

### Python

```python
class Skiplist(object):

    def __init__(self):
        

    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        

    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
```

### Python3

```python3
class Skiplist:

    def __init__(self):
        

    def search(self, target: int) -> bool:
        

    def add(self, num: int) -> None:
        

    def erase(self, num: int) -> bool:
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
```

### C

```c



typedef struct {
    
} Skiplist;


Skiplist* skiplistCreate() {
    
}

bool skiplistSearch(Skiplist* obj, int target) {
    
}

void skiplistAdd(Skiplist* obj, int num) {
    
}

bool skiplistErase(Skiplist* obj, int num) {
    
}

void skiplistFree(Skiplist* obj) {
    
}

/**
 * Your Skiplist struct will be instantiated and called as such:
 * Skiplist* obj = skiplistCreate();
 * bool param_1 = skiplistSearch(obj, target);
 
 * skiplistAdd(obj, num);
 
 * bool param_3 = skiplistErase(obj, num);
 
 * skiplistFree(obj);
*/
```

### C#

```csharp
public class Skiplist {

    public Skiplist() {
        
    }
    
    public bool Search(int target) {
        
    }
    
    public void Add(int num) {
        
    }
    
    public bool Erase(int num) {
        
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist obj = new Skiplist();
 * bool param_1 = obj.Search(target);
 * obj.Add(num);
 * bool param_3 = obj.Erase(num);
 */
```

### JavaScript

```javascript

var Skiplist = function() {
    
};

/** 
 * @param {number} target
 * @return {boolean}
 */
Skiplist.prototype.search = function(target) {
    
};

/** 
 * @param {number} num
 * @return {void}
 */
Skiplist.prototype.add = function(num) {
    
};

/** 
 * @param {number} num
 * @return {boolean}
 */
Skiplist.prototype.erase = function(num) {
    
};

/** 
 * Your Skiplist object will be instantiated and called as such:
 * var obj = new Skiplist()
 * var param_1 = obj.search(target)
 * obj.add(num)
 * var param_3 = obj.erase(num)
 */
```

### TypeScript

```typescript
class Skiplist {
    constructor() {
        
    }

    search(target: number): boolean {
        
    }

    add(num: number): void {
        
    }

    erase(num: number): boolean {
        
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * var obj = new Skiplist()
 * var param_1 = obj.search(target)
 * obj.add(num)
 * var param_3 = obj.erase(num)
 */
```

### PHP

```php
class Skiplist {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $target
     * @return Boolean
     */
    function search($target) {
        
    }
  
    /**
     * @param Integer $num
     * @return NULL
     */
    function add($num) {
        
    }
  
    /**
     * @param Integer $num
     * @return Boolean
     */
    function erase($num) {
        
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * $obj = Skiplist();
 * $ret_1 = $obj->search($target);
 * $obj->add($num);
 * $ret_3 = $obj->erase($num);
 */
```

### Swift

```swift

class Skiplist {

    init() {
        
    }
    
    func search(_ target: Int) -> Bool {
        
    }
    
    func add(_ num: Int) {
        
    }
    
    func erase(_ num: Int) -> Bool {
        
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * let obj = Skiplist()
 * let ret_1: Bool = obj.search(target)
 * obj.add(num)
 * let ret_3: Bool = obj.erase(num)
 */
```

### Kotlin

```kotlin
class Skiplist() {

    fun search(target: Int): Boolean {
        
    }

    fun add(num: Int) {
        
    }

    fun erase(num: Int): Boolean {
        
    }

}

/**
 * Your Skiplist object will be instantiated and called as such:
 * var obj = Skiplist()
 * var param_1 = obj.search(target)
 * obj.add(num)
 * var param_3 = obj.erase(num)
 */
```

### Dart

```dart
class Skiplist {

  Skiplist() {
    
  }
  
  bool search(int target) {
    
  }
  
  void add(int num) {
    
  }
  
  bool erase(int num) {
    
  }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist obj = Skiplist();
 * bool param1 = obj.search(target);
 * obj.add(num);
 * bool param3 = obj.erase(num);
 */
```

### Go

```golang
type Skiplist struct {
    
}


func Constructor() Skiplist {
    
}


func (this *Skiplist) Search(target int) bool {
    
}


func (this *Skiplist) Add(num int)  {
    
}


func (this *Skiplist) Erase(num int) bool {
    
}


/**
 * Your Skiplist object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Search(target);
 * obj.Add(num);
 * param_3 := obj.Erase(num);
 */
```

### Ruby

```ruby
class Skiplist
    def initialize()
        
    end


=begin
    :type target: Integer
    :rtype: Boolean
=end
    def search(target)
        
    end


=begin
    :type num: Integer
    :rtype: Void
=end
    def add(num)
        
    end


=begin
    :type num: Integer
    :rtype: Boolean
=end
    def erase(num)
        
    end


end

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist.new()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
```

### Scala

```scala
class Skiplist() {

    def search(target: Int): Boolean = {
        
    }

    def add(num: Int): Unit = {
        
    }

    def erase(num: Int): Boolean = {
        
    }

}

/**
 * Your Skiplist object will be instantiated and called as such:
 * val obj = new Skiplist()
 * val param_1 = obj.search(target)
 * obj.add(num)
 * val param_3 = obj.erase(num)
 */
```

### Rust

```rust
struct Skiplist {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Skiplist {

    fn new() -> Self {
        
    }
    
    fn search(&self, target: i32) -> bool {
        
    }
    
    fn add(&self, num: i32) {
        
    }
    
    fn erase(&self, num: i32) -> bool {
        
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * let obj = Skiplist::new();
 * let ret_1: bool = obj.search(target);
 * obj.add(num);
 * let ret_3: bool = obj.erase(num);
 */
```

### Racket

```racket
(define skiplist%
  (class object%
    (super-new)
    
    (init-field)
    
    ; search : exact-integer? -> boolean?
    (define/public (search target)
      )
    ; add : exact-integer? -> void?
    (define/public (add num)
      )
    ; erase : exact-integer? -> boolean?
    (define/public (erase num)
      )))

;; Your skiplist% object will be instantiated and called as such:
;; (define obj (new skiplist%))
;; (define param_1 (send obj search target))
;; (send obj add num)
;; (define param_3 (send obj erase num))
```

### Erlang

```erlang
-spec skiplist_init_() -> any().
skiplist_init_() ->
  .

-spec skiplist_search(Target :: integer()) -> boolean().
skiplist_search(Target) ->
  .

-spec skiplist_add(Num :: integer()) -> any().
skiplist_add(Num) ->
  .

-spec skiplist_erase(Num :: integer()) -> boolean().
skiplist_erase(Num) ->
  .


%% Your functions will be called as such:
%% skiplist_init_(),
%% Param_1 = skiplist_search(Target),
%% skiplist_add(Num),
%% Param_3 = skiplist_erase(Num),

%% skiplist_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Skiplist do
  @spec init_() :: any
  def init_() do
    
  end

  @spec search(target :: integer) :: boolean
  def search(target) do
    
  end

  @spec add(num :: integer) :: any
  def add(num) do
    
  end

  @spec erase(num :: integer) :: boolean
  def erase(num) do
    
  end
end

# Your functions will be called as such:
# Skiplist.init_()
# param_1 = Skiplist.search(target)
# Skiplist.add(num)
# param_3 = Skiplist.erase(num)

# Skiplist.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Skiplist {
    init() {

    }
    
    func search(target: Int64): Bool {

    }
    
    func add(num: Int64): Unit {

    }
    
    func erase(num: Int64): Bool {

    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * let obj: Skiplist = Skiplist()
 * let param_1 = obj.search(target)
 * obj.add(num)
 * let param_3 = obj.erase(num)
 */
```

