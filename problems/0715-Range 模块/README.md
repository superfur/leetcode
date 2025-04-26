# 715. Range 模块

## 题目描述

<p>Range模块是跟踪数字范围的模块。设计一个数据结构来跟踪表示为 <strong>半开区间</strong> 的范围并查询它们。</p>

<p><strong>半开区间</strong>&nbsp;<code>[left, right)</code>&nbsp;表示所有&nbsp;<code>left &lt;= x &lt; right</code>&nbsp;的实数 <code>x</code> 。</p>

<p>实现 <code>RangeModule</code> 类:</p>

<ul>
	<li><code>RangeModule()</code>&nbsp;初始化数据结构的对象。</li>
	<li><code>void addRange(int left, int right)</code> 添加 <strong>半开区间</strong>&nbsp;<code>[left, right)</code>，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间&nbsp;<code>[left, right)</code>&nbsp;中尚未跟踪的任何数字到该区间中。</li>
	<li><code>boolean queryRange(int left, int right)</code>&nbsp;只有在当前正在跟踪区间&nbsp;<code>[left, right)</code>&nbsp;中的每一个实数时，才返回 <code>true</code>&nbsp;，否则返回 <code>false</code> 。</li>
	<li><code>void removeRange(int left, int right)</code>&nbsp;停止跟踪 <strong>半开区间</strong>&nbsp;<code>[left, right)</code>&nbsp;中当前正在跟踪的每个实数。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入</strong>
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
<strong>输出</strong>
[null, null, null, true, false, true]

<strong>解释</strong>
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); 返回 true （区间 [10, 14) 中的每个数都正在被跟踪）
rangeModule.queryRange(13, 15); 返回 false（未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
rangeModule.queryRange(16, 17); 返回 true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= left &lt; right &lt;= 10<sup>9</sup></code></li>
	<li>在单个测试用例中，对&nbsp;<code>addRange</code>&nbsp;、&nbsp; <code>queryRange</code>&nbsp;和 <code>removeRange</code> 的调用总数不超过&nbsp;<code>10<sup>4</sup></code>&nbsp;次</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 线段树
- 有序集合

## 提示

1. Maintain a sorted set of disjoint intervals.  addRange and removeRange can be performed with time complexity linear to the size of this set; queryRange can be performed with time complexity logarithmic to the size of this set.

## 示例

```
["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]
[[],[10,20],[14,16],[10,14],[13,15],[16,17]]
```

## 示例代码

### C++

```cpp
class RangeModule {
public:
    RangeModule() {
        
    }
    
    void addRange(int left, int right) {
        
    }
    
    bool queryRange(int left, int right) {
        
    }
    
    void removeRange(int left, int right) {
        
    }
};

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule* obj = new RangeModule();
 * obj->addRange(left,right);
 * bool param_2 = obj->queryRange(left,right);
 * obj->removeRange(left,right);
 */
```

### Java

```java
class RangeModule {

    public RangeModule() {
        
    }
    
    public void addRange(int left, int right) {
        
    }
    
    public boolean queryRange(int left, int right) {
        
    }
    
    public void removeRange(int left, int right) {
        
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = new RangeModule();
 * obj.addRange(left,right);
 * boolean param_2 = obj.queryRange(left,right);
 * obj.removeRange(left,right);
 */
```

### Python

```python
class RangeModule(object):

    def __init__(self):
        

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
```

### Python3

```python3
class RangeModule:

    def __init__(self):
        

    def addRange(self, left: int, right: int) -> None:
        

    def queryRange(self, left: int, right: int) -> bool:
        

    def removeRange(self, left: int, right: int) -> None:
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
```

### C

```c



typedef struct {
    
} RangeModule;


RangeModule* rangeModuleCreate() {
    
}

void rangeModuleAddRange(RangeModule* obj, int left, int right) {
    
}

bool rangeModuleQueryRange(RangeModule* obj, int left, int right) {
    
}

void rangeModuleRemoveRange(RangeModule* obj, int left, int right) {
    
}

void rangeModuleFree(RangeModule* obj) {
    
}

/**
 * Your RangeModule struct will be instantiated and called as such:
 * RangeModule* obj = rangeModuleCreate();
 * rangeModuleAddRange(obj, left, right);
 
 * bool param_2 = rangeModuleQueryRange(obj, left, right);
 
 * rangeModuleRemoveRange(obj, left, right);
 
 * rangeModuleFree(obj);
*/
```

### C#

```csharp
public class RangeModule {

    public RangeModule() {
        
    }
    
    public void AddRange(int left, int right) {
        
    }
    
    public bool QueryRange(int left, int right) {
        
    }
    
    public void RemoveRange(int left, int right) {
        
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = new RangeModule();
 * obj.AddRange(left,right);
 * bool param_2 = obj.QueryRange(left,right);
 * obj.RemoveRange(left,right);
 */
```

### JavaScript

```javascript

var RangeModule = function() {
    
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {void}
 */
RangeModule.prototype.addRange = function(left, right) {
    
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {boolean}
 */
RangeModule.prototype.queryRange = function(left, right) {
    
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {void}
 */
RangeModule.prototype.removeRange = function(left, right) {
    
};

/** 
 * Your RangeModule object will be instantiated and called as such:
 * var obj = new RangeModule()
 * obj.addRange(left,right)
 * var param_2 = obj.queryRange(left,right)
 * obj.removeRange(left,right)
 */
```

### TypeScript

```typescript
class RangeModule {
    constructor() {
        
    }

    addRange(left: number, right: number): void {
        
    }

    queryRange(left: number, right: number): boolean {
        
    }

    removeRange(left: number, right: number): void {
        
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * var obj = new RangeModule()
 * obj.addRange(left,right)
 * var param_2 = obj.queryRange(left,right)
 * obj.removeRange(left,right)
 */
```

### PHP

```php
class RangeModule {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $left
     * @param Integer $right
     * @return NULL
     */
    function addRange($left, $right) {
        
    }
  
    /**
     * @param Integer $left
     * @param Integer $right
     * @return Boolean
     */
    function queryRange($left, $right) {
        
    }
  
    /**
     * @param Integer $left
     * @param Integer $right
     * @return NULL
     */
    function removeRange($left, $right) {
        
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * $obj = RangeModule();
 * $obj->addRange($left, $right);
 * $ret_2 = $obj->queryRange($left, $right);
 * $obj->removeRange($left, $right);
 */
```

### Swift

```swift

class RangeModule {

    init() {
        
    }
    
    func addRange(_ left: Int, _ right: Int) {
        
    }
    
    func queryRange(_ left: Int, _ right: Int) -> Bool {
        
    }
    
    func removeRange(_ left: Int, _ right: Int) {
        
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * let obj = RangeModule()
 * obj.addRange(left, right)
 * let ret_2: Bool = obj.queryRange(left, right)
 * obj.removeRange(left, right)
 */
```

### Kotlin

```kotlin
class RangeModule() {

    fun addRange(left: Int, right: Int) {
        
    }

    fun queryRange(left: Int, right: Int): Boolean {
        
    }

    fun removeRange(left: Int, right: Int) {
        
    }

}

/**
 * Your RangeModule object will be instantiated and called as such:
 * var obj = RangeModule()
 * obj.addRange(left,right)
 * var param_2 = obj.queryRange(left,right)
 * obj.removeRange(left,right)
 */
```

### Dart

```dart
class RangeModule {

  RangeModule() {
    
  }
  
  void addRange(int left, int right) {
    
  }
  
  bool queryRange(int left, int right) {
    
  }
  
  void removeRange(int left, int right) {
    
  }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = RangeModule();
 * obj.addRange(left,right);
 * bool param2 = obj.queryRange(left,right);
 * obj.removeRange(left,right);
 */
```

### Go

```golang
type RangeModule struct {
    
}


func Constructor() RangeModule {
    
}


func (this *RangeModule) AddRange(left int, right int)  {
    
}


func (this *RangeModule) QueryRange(left int, right int) bool {
    
}


func (this *RangeModule) RemoveRange(left int, right int)  {
    
}


/**
 * Your RangeModule object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddRange(left,right);
 * param_2 := obj.QueryRange(left,right);
 * obj.RemoveRange(left,right);
 */
```

### Ruby

```ruby
class RangeModule
    def initialize()
        
    end


=begin
    :type left: Integer
    :type right: Integer
    :rtype: Void
=end
    def add_range(left, right)
        
    end


=begin
    :type left: Integer
    :type right: Integer
    :rtype: Boolean
=end
    def query_range(left, right)
        
    end


=begin
    :type left: Integer
    :type right: Integer
    :rtype: Void
=end
    def remove_range(left, right)
        
    end


end

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule.new()
# obj.add_range(left, right)
# param_2 = obj.query_range(left, right)
# obj.remove_range(left, right)
```

### Scala

```scala
class RangeModule() {

    def addRange(left: Int, right: Int): Unit = {
        
    }

    def queryRange(left: Int, right: Int): Boolean = {
        
    }

    def removeRange(left: Int, right: Int): Unit = {
        
    }

}

/**
 * Your RangeModule object will be instantiated and called as such:
 * val obj = new RangeModule()
 * obj.addRange(left,right)
 * val param_2 = obj.queryRange(left,right)
 * obj.removeRange(left,right)
 */
```

### Rust

```rust
struct RangeModule {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RangeModule {

    fn new() -> Self {
        
    }
    
    fn add_range(&self, left: i32, right: i32) {
        
    }
    
    fn query_range(&self, left: i32, right: i32) -> bool {
        
    }
    
    fn remove_range(&self, left: i32, right: i32) {
        
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * let obj = RangeModule::new();
 * obj.add_range(left, right);
 * let ret_2: bool = obj.query_range(left, right);
 * obj.remove_range(left, right);
 */
```

### Racket

```racket
(define range-module%
  (class object%
    (super-new)
    
    (init-field)
    
    ; add-range : exact-integer? exact-integer? -> void?
    (define/public (add-range left right)
      )
    ; query-range : exact-integer? exact-integer? -> boolean?
    (define/public (query-range left right)
      )
    ; remove-range : exact-integer? exact-integer? -> void?
    (define/public (remove-range left right)
      )))

;; Your range-module% object will be instantiated and called as such:
;; (define obj (new range-module%))
;; (send obj add-range left right)
;; (define param_2 (send obj query-range left right))
;; (send obj remove-range left right)
```

### Erlang

```erlang
-spec range_module_init_() -> any().
range_module_init_() ->
  .

-spec range_module_add_range(Left :: integer(), Right :: integer()) -> any().
range_module_add_range(Left, Right) ->
  .

-spec range_module_query_range(Left :: integer(), Right :: integer()) -> boolean().
range_module_query_range(Left, Right) ->
  .

-spec range_module_remove_range(Left :: integer(), Right :: integer()) -> any().
range_module_remove_range(Left, Right) ->
  .


%% Your functions will be called as such:
%% range_module_init_(),
%% range_module_add_range(Left, Right),
%% Param_2 = range_module_query_range(Left, Right),
%% range_module_remove_range(Left, Right),

%% range_module_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule RangeModule do
  @spec init_() :: any
  def init_() do
    
  end

  @spec add_range(left :: integer, right :: integer) :: any
  def add_range(left, right) do
    
  end

  @spec query_range(left :: integer, right :: integer) :: boolean
  def query_range(left, right) do
    
  end

  @spec remove_range(left :: integer, right :: integer) :: any
  def remove_range(left, right) do
    
  end
end

# Your functions will be called as such:
# RangeModule.init_()
# RangeModule.add_range(left, right)
# param_2 = RangeModule.query_range(left, right)
# RangeModule.remove_range(left, right)

# RangeModule.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class RangeModule {
    init() {

    }
    
    func addRange(left: Int64, right: Int64): Unit {

    }
    
    func queryRange(left: Int64, right: Int64): Bool {

    }
    
    func removeRange(left: Int64, right: Int64): Unit {

    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * let obj: RangeModule = RangeModule()
 * obj.addRange(left,right)
 * let param_2 = obj.queryRange(left,right)
 * obj.removeRange(left,right)
 */
```

