# 1622. 奇妙序列

## 题目描述

<p>请你实现三个 API <code>append</code>，<code>addAll</code> 和 <code>multAll</code> 来实现奇妙序列。</p>

<p>请实现 <code>Fancy</code> 类 ：</p>

<ul>
	<li><code>Fancy()</code> 初始化一个空序列对象。</li>
	<li><code>void append(val)</code> 将整数 <code>val</code> 添加在序列末尾。</li>
	<li><code>void addAll(inc)</code> 将所有序列中的现有数值都增加 <code>inc</code> 。</li>
	<li><code>void multAll(m)</code> 将序列中的所有现有数值都乘以整数 <code>m</code> 。</li>
	<li><code>int getIndex(idx)</code> 得到下标为 <code>idx</code> 处的数值（下标从 0 开始），并将结果对 <code>10<sup>9</sup> + 7</code> 取余。如果下标大于等于序列的长度，请返回 <code>-1</code> 。</li>
</ul>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
<strong>输出：</strong>
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

<strong>解释：</strong>
Fancy fancy = new Fancy();
fancy.append(2);   // 奇妙序列：[2]
fancy.addAll(3);   // 奇妙序列：[2+3] -> [5]
fancy.append(7);   // 奇妙序列：[5, 7]
fancy.multAll(2);  // 奇妙序列：[5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // 返回 10
fancy.addAll(3);   // 奇妙序列：[10+3, 14+3] -> [13, 17]
fancy.append(10);  // 奇妙序列：[13, 17, 10]
fancy.multAll(2);  // 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // 返回 26
fancy.getIndex(1); // 返回 34
fancy.getIndex(2); // 返回 20
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= val, inc, m <= 100</code></li>
	<li><code>0 <= idx <= 10<sup>5</sup></code></li>
	<li>总共最多会有 <code>10<sup>5</sup></code> 次对 <code>append</code>，<code>addAll</code>，<code>multAll</code> 和 <code>getIndex</code> 的调用。</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 线段树
- 数学

## 提示

1. Use two arrays to save the cumulative multipliers at each time point and cumulative sums adjusted by the current multiplier.
2. The function getIndex(idx) ask to the current value modulo 10^9+7. Use modular inverse and both arrays to calculate this value.

## 示例

```
["Fancy","append","addAll","append","multAll","getIndex","addAll","append","multAll","getIndex","getIndex","getIndex"]
[[],[2],[3],[7],[2],[0],[3],[10],[2],[0],[1],[2]]
```

## 示例代码

### C++

```cpp
class Fancy {
public:
    Fancy() {
        
    }
    
    void append(int val) {
        
    }
    
    void addAll(int inc) {
        
    }
    
    void multAll(int m) {
        
    }
    
    int getIndex(int idx) {
        
    }
};

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy* obj = new Fancy();
 * obj->append(val);
 * obj->addAll(inc);
 * obj->multAll(m);
 * int param_4 = obj->getIndex(idx);
 */
```

### Java

```java
class Fancy {

    public Fancy() {
        
    }
    
    public void append(int val) {
        
    }
    
    public void addAll(int inc) {
        
    }
    
    public void multAll(int m) {
        
    }
    
    public int getIndex(int idx) {
        
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy obj = new Fancy();
 * obj.append(val);
 * obj.addAll(inc);
 * obj.multAll(m);
 * int param_4 = obj.getIndex(idx);
 */
```

### Python

```python
class Fancy(object):

    def __init__(self):
        

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
```

### Python3

```python3
class Fancy:

    def __init__(self):
        

    def append(self, val: int) -> None:
        

    def addAll(self, inc: int) -> None:
        

    def multAll(self, m: int) -> None:
        

    def getIndex(self, idx: int) -> int:
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
```

### C

```c



typedef struct {
    
} Fancy;


Fancy* fancyCreate() {
    
}

void fancyAppend(Fancy* obj, int val) {
    
}

void fancyAddAll(Fancy* obj, int inc) {
    
}

void fancyMultAll(Fancy* obj, int m) {
    
}

int fancyGetIndex(Fancy* obj, int idx) {
    
}

void fancyFree(Fancy* obj) {
    
}

/**
 * Your Fancy struct will be instantiated and called as such:
 * Fancy* obj = fancyCreate();
 * fancyAppend(obj, val);
 
 * fancyAddAll(obj, inc);
 
 * fancyMultAll(obj, m);
 
 * int param_4 = fancyGetIndex(obj, idx);
 
 * fancyFree(obj);
*/
```

### C#

```csharp
public class Fancy {

    public Fancy() {
        
    }
    
    public void Append(int val) {
        
    }
    
    public void AddAll(int inc) {
        
    }
    
    public void MultAll(int m) {
        
    }
    
    public int GetIndex(int idx) {
        
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy obj = new Fancy();
 * obj.Append(val);
 * obj.AddAll(inc);
 * obj.MultAll(m);
 * int param_4 = obj.GetIndex(idx);
 */
```

### JavaScript

```javascript

var Fancy = function() {
    
};

/** 
 * @param {number} val
 * @return {void}
 */
Fancy.prototype.append = function(val) {
    
};

/** 
 * @param {number} inc
 * @return {void}
 */
Fancy.prototype.addAll = function(inc) {
    
};

/** 
 * @param {number} m
 * @return {void}
 */
Fancy.prototype.multAll = function(m) {
    
};

/** 
 * @param {number} idx
 * @return {number}
 */
Fancy.prototype.getIndex = function(idx) {
    
};

/** 
 * Your Fancy object will be instantiated and called as such:
 * var obj = new Fancy()
 * obj.append(val)
 * obj.addAll(inc)
 * obj.multAll(m)
 * var param_4 = obj.getIndex(idx)
 */
```

### TypeScript

```typescript
class Fancy {
    constructor() {
        
    }

    append(val: number): void {
        
    }

    addAll(inc: number): void {
        
    }

    multAll(m: number): void {
        
    }

    getIndex(idx: number): number {
        
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * var obj = new Fancy()
 * obj.append(val)
 * obj.addAll(inc)
 * obj.multAll(m)
 * var param_4 = obj.getIndex(idx)
 */
```

### PHP

```php
class Fancy {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $val
     * @return NULL
     */
    function append($val) {
        
    }
  
    /**
     * @param Integer $inc
     * @return NULL
     */
    function addAll($inc) {
        
    }
  
    /**
     * @param Integer $m
     * @return NULL
     */
    function multAll($m) {
        
    }
  
    /**
     * @param Integer $idx
     * @return Integer
     */
    function getIndex($idx) {
        
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * $obj = Fancy();
 * $obj->append($val);
 * $obj->addAll($inc);
 * $obj->multAll($m);
 * $ret_4 = $obj->getIndex($idx);
 */
```

### Swift

```swift

class Fancy {

    init() {
        
    }
    
    func append(_ val: Int) {
        
    }
    
    func addAll(_ inc: Int) {
        
    }
    
    func multAll(_ m: Int) {
        
    }
    
    func getIndex(_ idx: Int) -> Int {
        
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * let obj = Fancy()
 * obj.append(val)
 * obj.addAll(inc)
 * obj.multAll(m)
 * let ret_4: Int = obj.getIndex(idx)
 */
```

### Kotlin

```kotlin
class Fancy() {

    fun append(`val`: Int) {
        
    }

    fun addAll(inc: Int) {
        
    }

    fun multAll(m: Int) {
        
    }

    fun getIndex(idx: Int): Int {
        
    }

}

/**
 * Your Fancy object will be instantiated and called as such:
 * var obj = Fancy()
 * obj.append(`val`)
 * obj.addAll(inc)
 * obj.multAll(m)
 * var param_4 = obj.getIndex(idx)
 */
```

### Dart

```dart
class Fancy {

  Fancy() {
    
  }
  
  void append(int val) {
    
  }
  
  void addAll(int inc) {
    
  }
  
  void multAll(int m) {
    
  }
  
  int getIndex(int idx) {
    
  }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy obj = Fancy();
 * obj.append(val);
 * obj.addAll(inc);
 * obj.multAll(m);
 * int param4 = obj.getIndex(idx);
 */
```

### Go

```golang
type Fancy struct {
    
}


func Constructor() Fancy {
    
}


func (this *Fancy) Append(val int)  {
    
}


func (this *Fancy) AddAll(inc int)  {
    
}


func (this *Fancy) MultAll(m int)  {
    
}


func (this *Fancy) GetIndex(idx int) int {
    
}


/**
 * Your Fancy object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Append(val);
 * obj.AddAll(inc);
 * obj.MultAll(m);
 * param_4 := obj.GetIndex(idx);
 */
```

### Ruby

```ruby
class Fancy
    def initialize()
        
    end


=begin
    :type val: Integer
    :rtype: Void
=end
    def append(val)
        
    end


=begin
    :type inc: Integer
    :rtype: Void
=end
    def add_all(inc)
        
    end


=begin
    :type m: Integer
    :rtype: Void
=end
    def mult_all(m)
        
    end


=begin
    :type idx: Integer
    :rtype: Integer
=end
    def get_index(idx)
        
    end


end

# Your Fancy object will be instantiated and called as such:
# obj = Fancy.new()
# obj.append(val)
# obj.add_all(inc)
# obj.mult_all(m)
# param_4 = obj.get_index(idx)
```

### Scala

```scala
class Fancy() {

    def append(`val`: Int): Unit = {
        
    }

    def addAll(inc: Int): Unit = {
        
    }

    def multAll(m: Int): Unit = {
        
    }

    def getIndex(idx: Int): Int = {
        
    }

}

/**
 * Your Fancy object will be instantiated and called as such:
 * val obj = new Fancy()
 * obj.append(`val`)
 * obj.addAll(inc)
 * obj.multAll(m)
 * val param_4 = obj.getIndex(idx)
 */
```

### Rust

```rust
struct Fancy {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Fancy {

    fn new() -> Self {
        
    }
    
    fn append(&self, val: i32) {
        
    }
    
    fn add_all(&self, inc: i32) {
        
    }
    
    fn mult_all(&self, m: i32) {
        
    }
    
    fn get_index(&self, idx: i32) -> i32 {
        
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * let obj = Fancy::new();
 * obj.append(val);
 * obj.add_all(inc);
 * obj.mult_all(m);
 * let ret_4: i32 = obj.get_index(idx);
 */
```

### Racket

```racket
(define fancy%
  (class object%
    (super-new)
    
    (init-field)
    
    ; append : exact-integer? -> void?
    (define/public (append val)
      )
    ; add-all : exact-integer? -> void?
    (define/public (add-all inc)
      )
    ; mult-all : exact-integer? -> void?
    (define/public (mult-all m)
      )
    ; get-index : exact-integer? -> exact-integer?
    (define/public (get-index idx)
      )))

;; Your fancy% object will be instantiated and called as such:
;; (define obj (new fancy%))
;; (send obj append val)
;; (send obj add-all inc)
;; (send obj mult-all m)
;; (define param_4 (send obj get-index idx))
```

### Erlang

```erlang
-spec fancy_init_() -> any().
fancy_init_() ->
  .

-spec fancy_append(Val :: integer()) -> any().
fancy_append(Val) ->
  .

-spec fancy_add_all(Inc :: integer()) -> any().
fancy_add_all(Inc) ->
  .

-spec fancy_mult_all(M :: integer()) -> any().
fancy_mult_all(M) ->
  .

-spec fancy_get_index(Idx :: integer()) -> integer().
fancy_get_index(Idx) ->
  .


%% Your functions will be called as such:
%% fancy_init_(),
%% fancy_append(Val),
%% fancy_add_all(Inc),
%% fancy_mult_all(M),
%% Param_4 = fancy_get_index(Idx),

%% fancy_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Fancy do
  @spec init_() :: any
  def init_() do
    
  end

  @spec append(val :: integer) :: any
  def append(val) do
    
  end

  @spec add_all(inc :: integer) :: any
  def add_all(inc) do
    
  end

  @spec mult_all(m :: integer) :: any
  def mult_all(m) do
    
  end

  @spec get_index(idx :: integer) :: integer
  def get_index(idx) do
    
  end
end

# Your functions will be called as such:
# Fancy.init_()
# Fancy.append(val)
# Fancy.add_all(inc)
# Fancy.mult_all(m)
# param_4 = Fancy.get_index(idx)

# Fancy.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Fancy {
    init() {

    }
    
    func append(val: Int64): Unit {

    }
    
    func addAll(inc: Int64): Unit {

    }
    
    func multAll(m: Int64): Unit {

    }
    
    func getIndex(idx: Int64): Int64 {

    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * let obj: Fancy = Fancy()
 * obj.append(val)
 * obj.addAll(inc)
 * obj.multAll(m)
 * let param_4 = obj.getIndex(idx)
 */
```

