# 2166. 设计位集

## 题目描述

<p><strong>位集 Bitset</strong> 是一种能以紧凑形式存储位的数据结构。</p>

<p>请你实现 <code>Bitset</code> 类。</p>

<ul>
	<li><code>Bitset(int size)</code> 用 <code>size</code> 个位初始化 Bitset ，所有位都是 <code>0</code> 。</li>
	<li><code>void fix(int idx)</code> 将下标为 <code>idx</code> 的位上的值更新为 <code>1</code> 。如果值已经是 <code>1</code> ，则不会发生任何改变。</li>
	<li><code>void unfix(int idx)</code> 将下标为 <code>idx</code> 的位上的值更新为 <code>0</code> 。如果值已经是 <code>0</code> ，则不会发生任何改变。</li>
	<li><code>void flip()</code> 翻转 Bitset 中每一位上的值。换句话说，所有值为 <code>0</code> 的位将会变成 <code>1</code> ，反之亦然。</li>
	<li><code>boolean all()</code> 检查&nbsp;Bitset 中 <strong>每一位</strong> 的值是否都是 <code>1</code> 。如果满足此条件，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
	<li><code>boolean one()</code> 检查&nbsp;Bitset 中 是否&nbsp;<strong>至少一位</strong> 的值是 <code>1</code> 。如果满足此条件，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
	<li><code>int count()</code> 返回 Bitset 中值为 1 的位的 <strong>总数</strong> 。</li>
	<li><code>String toString()</code> 返回 Bitset 的当前组成情况。注意，在结果字符串中，第 <code>i</code> 个下标处的字符应该与 Bitset 中的第 <code>i</code> 位一致。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
[[5], [3], [1], [], [], [0], [], [], [0], [], []]
<strong>输出</strong>
[null, null, null, null, false, null, null, true, null, 2, "01010"]

<strong>解释</strong>
Bitset bs = new Bitset(5); // bitset = "00000".
bs.fix(3);     // 将 idx = 3 处的值更新为 1 ，此时 bitset = "00010" 。
bs.fix(1);     // 将 idx = 1 处的值更新为 1 ，此时 bitset = "01010" 。
bs.flip();     // 翻转每一位上的值，此时 bitset = "10101" 。
bs.all();      // 返回 False ，bitset 中的值不全为 1 。
bs.unfix(0);   // 将 idx = 0 处的值更新为 0 ，此时 bitset = "00101" 。
bs.flip();     // 翻转每一位上的值，此时 bitset = "11010" 。
bs.one();      // 返回 True ，至少存在一位的值为 1 。
bs.unfix(0);   // 将 idx = 0 处的值更新为 0 ，此时 bitset = "01010" 。
bs.count();    // 返回 2 ，当前有 2 位的值为 1 。
bs.toString(); // 返回 "01010" ，即 bitset 的当前组成情况。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= size &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= idx &lt;= size - 1</code></li>
	<li>至多调用&nbsp;<code>fix</code>、<code>unfix</code>、<code>flip</code>、<code>all</code>、<code>one</code>、<code>count</code> 和 <code>toString</code> 方法 <strong>总共</strong> <code>10<sup>5</sup></code> 次</li>
	<li>至少调用 <code>all</code>、<code>one</code>、<code>count</code> 或 <code>toString</code> 方法一次</li>
	<li>至多调用&nbsp;<code>toString</code> 方法 <code>5</code> 次</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 哈希表
- 字符串

## 提示

1. Note that flipping a bit twice does nothing.
2. In order to determine the value of a bit, consider how you can efficiently count the number of flips made on the bit since its latest update.

## 示例

```
["Bitset","fix","fix","flip","all","unfix","flip","one","unfix","count","toString"]
[[5],[3],[1],[],[],[0],[],[],[0],[],[]]
```

## 示例代码

### C++

```cpp
class Bitset {
public:
    Bitset(int size) {
        
    }
    
    void fix(int idx) {
        
    }
    
    void unfix(int idx) {
        
    }
    
    void flip() {
        
    }
    
    bool all() {
        
    }
    
    bool one() {
        
    }
    
    int count() {
        
    }
    
    string toString() {
        
    }
};

/**
 * Your Bitset object will be instantiated and called as such:
 * Bitset* obj = new Bitset(size);
 * obj->fix(idx);
 * obj->unfix(idx);
 * obj->flip();
 * bool param_4 = obj->all();
 * bool param_5 = obj->one();
 * int param_6 = obj->count();
 * string param_7 = obj->toString();
 */
```

### Java

```java
class Bitset {

    public Bitset(int size) {
        
    }
    
    public void fix(int idx) {
        
    }
    
    public void unfix(int idx) {
        
    }
    
    public void flip() {
        
    }
    
    public boolean all() {
        
    }
    
    public boolean one() {
        
    }
    
    public int count() {
        
    }
    
    public String toString() {
        
    }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * Bitset obj = new Bitset(size);
 * obj.fix(idx);
 * obj.unfix(idx);
 * obj.flip();
 * boolean param_4 = obj.all();
 * boolean param_5 = obj.one();
 * int param_6 = obj.count();
 * String param_7 = obj.toString();
 */
```

### Python

```python
class Bitset(object):

    def __init__(self, size):
        """
        :type size: int
        """
        

    def fix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        

    def unfix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        

    def flip(self):
        """
        :rtype: None
        """
        

    def all(self):
        """
        :rtype: bool
        """
        

    def one(self):
        """
        :rtype: bool
        """
        

    def count(self):
        """
        :rtype: int
        """
        

    def toString(self):
        """
        :rtype: str
        """
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
```

### Python3

```python3
class Bitset:

    def __init__(self, size: int):
        

    def fix(self, idx: int) -> None:
        

    def unfix(self, idx: int) -> None:
        

    def flip(self) -> None:
        

    def all(self) -> bool:
        

    def one(self) -> bool:
        

    def count(self) -> int:
        

    def toString(self) -> str:
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
```

### C

```c



typedef struct {
    
} Bitset;


Bitset* bitsetCreate(int size) {
    
}

void bitsetFix(Bitset* obj, int idx) {
    
}

void bitsetUnfix(Bitset* obj, int idx) {
    
}

void bitsetFlip(Bitset* obj) {
    
}

bool bitsetAll(Bitset* obj) {
    
}

bool bitsetOne(Bitset* obj) {
    
}

int bitsetCount(Bitset* obj) {
    
}

char* bitsetToString(Bitset* obj) {
    
}

void bitsetFree(Bitset* obj) {
    
}

/**
 * Your Bitset struct will be instantiated and called as such:
 * Bitset* obj = bitsetCreate(size);
 * bitsetFix(obj, idx);
 
 * bitsetUnfix(obj, idx);
 
 * bitsetFlip(obj);
 
 * bool param_4 = bitsetAll(obj);
 
 * bool param_5 = bitsetOne(obj);
 
 * int param_6 = bitsetCount(obj);
 
 * char* param_7 = bitsetToString(obj);
 
 * bitsetFree(obj);
*/
```

### C#

```csharp
public class Bitset {

    public Bitset(int size) {
        
    }
    
    public void Fix(int idx) {
        
    }
    
    public void Unfix(int idx) {
        
    }
    
    public void Flip() {
        
    }
    
    public bool All() {
        
    }
    
    public bool One() {
        
    }
    
    public int Count() {
        
    }
    
    public string ToString() {
        
    }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * Bitset obj = new Bitset(size);
 * obj.Fix(idx);
 * obj.Unfix(idx);
 * obj.Flip();
 * bool param_4 = obj.All();
 * bool param_5 = obj.One();
 * int param_6 = obj.Count();
 * string param_7 = obj.ToString();
 */
```

### JavaScript

```javascript
/**
 * @param {number} size
 */
var Bitset = function(size) {
    
};

/** 
 * @param {number} idx
 * @return {void}
 */
Bitset.prototype.fix = function(idx) {
    
};

/** 
 * @param {number} idx
 * @return {void}
 */
Bitset.prototype.unfix = function(idx) {
    
};

/**
 * @return {void}
 */
Bitset.prototype.flip = function() {
    
};

/**
 * @return {boolean}
 */
Bitset.prototype.all = function() {
    
};

/**
 * @return {boolean}
 */
Bitset.prototype.one = function() {
    
};

/**
 * @return {number}
 */
Bitset.prototype.count = function() {
    
};

/**
 * @return {string}
 */
Bitset.prototype.toString = function() {
    
};

/** 
 * Your Bitset object will be instantiated and called as such:
 * var obj = new Bitset(size)
 * obj.fix(idx)
 * obj.unfix(idx)
 * obj.flip()
 * var param_4 = obj.all()
 * var param_5 = obj.one()
 * var param_6 = obj.count()
 * var param_7 = obj.toString()
 */
```

### TypeScript

```typescript
class Bitset {
    constructor(size: number) {
        
    }

    fix(idx: number): void {
        
    }

    unfix(idx: number): void {
        
    }

    flip(): void {
        
    }

    all(): boolean {
        
    }

    one(): boolean {
        
    }

    count(): number {
        
    }

    toString(): string {
        
    }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * var obj = new Bitset(size)
 * obj.fix(idx)
 * obj.unfix(idx)
 * obj.flip()
 * var param_4 = obj.all()
 * var param_5 = obj.one()
 * var param_6 = obj.count()
 * var param_7 = obj.toString()
 */
```

### PHP

```php
class Bitset {
    /**
     * @param Integer $size
     */
    function __construct($size) {
        
    }
  
    /**
     * @param Integer $idx
     * @return NULL
     */
    function fix($idx) {
        
    }
  
    /**
     * @param Integer $idx
     * @return NULL
     */
    function unfix($idx) {
        
    }
  
    /**
     * @return NULL
     */
    function flip() {
        
    }
  
    /**
     * @return Boolean
     */
    function all() {
        
    }
  
    /**
     * @return Boolean
     */
    function one() {
        
    }
  
    /**
     * @return Integer
     */
    function count() {
        
    }
  
    /**
     * @return String
     */
    function toString() {
        
    }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * $obj = Bitset($size);
 * $obj->fix($idx);
 * $obj->unfix($idx);
 * $obj->flip();
 * $ret_4 = $obj->all();
 * $ret_5 = $obj->one();
 * $ret_6 = $obj->count();
 * $ret_7 = $obj->toString();
 */
```

### Swift

```swift

class Bitset {

    init(_ size: Int) {
        
    }
    
    func fix(_ idx: Int) {
        
    }
    
    func unfix(_ idx: Int) {
        
    }
    
    func flip() {
        
    }
    
    func all() -> Bool {
        
    }
    
    func one() -> Bool {
        
    }
    
    func count() -> Int {
        
    }
    
    func toString() -> String {
        
    }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * let obj = Bitset(size)
 * obj.fix(idx)
 * obj.unfix(idx)
 * obj.flip()
 * let ret_4: Bool = obj.all()
 * let ret_5: Bool = obj.one()
 * let ret_6: Int = obj.count()
 * let ret_7: String = obj.toString()
 */
```

### Kotlin

```kotlin
class Bitset(size: Int) {

    fun fix(idx: Int) {
        
    }

    fun unfix(idx: Int) {
        
    }

    fun flip() {
        
    }

    fun all(): Boolean {
        
    }

    fun one(): Boolean {
        
    }

    fun count(): Int {
        
    }

    fun toString(): String {
        
    }

}

/**
 * Your Bitset object will be instantiated and called as such:
 * var obj = Bitset(size)
 * obj.fix(idx)
 * obj.unfix(idx)
 * obj.flip()
 * var param_4 = obj.all()
 * var param_5 = obj.one()
 * var param_6 = obj.count()
 * var param_7 = obj.toString()
 */
```

### Dart

```dart
class Bitset {

  Bitset(int size) {
    
  }
  
  void fix(int idx) {
    
  }
  
  void unfix(int idx) {
    
  }
  
  void flip() {
    
  }
  
  bool all() {
    
  }
  
  bool one() {
    
  }
  
  int count() {
    
  }
  
  String toString() {
    
  }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * Bitset obj = Bitset(size);
 * obj.fix(idx);
 * obj.unfix(idx);
 * obj.flip();
 * bool param4 = obj.all();
 * bool param5 = obj.one();
 * int param6 = obj.count();
 * String param7 = obj.toString();
 */
```

### Go

```golang
type Bitset struct {
    
}


func Constructor(size int) Bitset {
    
}


func (this *Bitset) Fix(idx int)  {
    
}


func (this *Bitset) Unfix(idx int)  {
    
}


func (this *Bitset) Flip()  {
    
}


func (this *Bitset) All() bool {
    
}


func (this *Bitset) One() bool {
    
}


func (this *Bitset) Count() int {
    
}


func (this *Bitset) ToString() string {
    
}


/**
 * Your Bitset object will be instantiated and called as such:
 * obj := Constructor(size);
 * obj.Fix(idx);
 * obj.Unfix(idx);
 * obj.Flip();
 * param_4 := obj.All();
 * param_5 := obj.One();
 * param_6 := obj.Count();
 * param_7 := obj.ToString();
 */
```

### Ruby

```ruby
class Bitset

=begin
    :type size: Integer
=end
    def initialize(size)
        
    end


=begin
    :type idx: Integer
    :rtype: Void
=end
    def fix(idx)
        
    end


=begin
    :type idx: Integer
    :rtype: Void
=end
    def unfix(idx)
        
    end


=begin
    :rtype: Void
=end
    def flip()
        
    end


=begin
    :rtype: Boolean
=end
    def all()
        
    end


=begin
    :rtype: Boolean
=end
    def one()
        
    end


=begin
    :rtype: Integer
=end
    def count()
        
    end


=begin
    :rtype: String
=end
    def to_string()
        
    end


end

# Your Bitset object will be instantiated and called as such:
# obj = Bitset.new(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.to_string()
```

### Scala

```scala
class Bitset(_size: Int) {

    def fix(idx: Int): Unit = {
        
    }

    def unfix(idx: Int): Unit = {
        
    }

    def flip(): Unit = {
        
    }

    def all(): Boolean = {
        
    }

    def one(): Boolean = {
        
    }

    def count(): Int = {
        
    }

    def toString(): String = {
        
    }

}

/**
 * Your Bitset object will be instantiated and called as such:
 * val obj = new Bitset(size)
 * obj.fix(idx)
 * obj.unfix(idx)
 * obj.flip()
 * val param_4 = obj.all()
 * val param_5 = obj.one()
 * val param_6 = obj.count()
 * val param_7 = obj.toString()
 */
```

### Rust

```rust
struct Bitset {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Bitset {

    fn new(size: i32) -> Self {
        
    }
    
    fn fix(&self, idx: i32) {
        
    }
    
    fn unfix(&self, idx: i32) {
        
    }
    
    fn flip(&self) {
        
    }
    
    fn all(&self) -> bool {
        
    }
    
    fn one(&self) -> bool {
        
    }
    
    fn count(&self) -> i32 {
        
    }
    
    fn to_string(&self) -> String {
        
    }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * let obj = Bitset::new(size);
 * obj.fix(idx);
 * obj.unfix(idx);
 * obj.flip();
 * let ret_4: bool = obj.all();
 * let ret_5: bool = obj.one();
 * let ret_6: i32 = obj.count();
 * let ret_7: String = obj.to_string();
 */
```

### Racket

```racket
(define bitset%
  (class object%
    (super-new)
    
    ; size : exact-integer?
    (init-field
      size)
    
    ; fix : exact-integer? -> void?
    (define/public (fix idx)
      )
    ; unfix : exact-integer? -> void?
    (define/public (unfix idx)
      )
    ; flip : -> void?
    (define/public (flip)
      )
    ; all : -> boolean?
    (define/public (all)
      )
    ; one : -> boolean?
    (define/public (one)
      )
    ; count : -> exact-integer?
    (define/public (count)
      )
    ; to-string : -> string?
    (define/public (to-string)
      )))

;; Your bitset% object will be instantiated and called as such:
;; (define obj (new bitset% [size size]))
;; (send obj fix idx)
;; (send obj unfix idx)
;; (send obj flip)
;; (define param_4 (send obj all))
;; (define param_5 (send obj one))
;; (define param_6 (send obj count))
;; (define param_7 (send obj to-string))
```

### Erlang

```erlang
-spec bitset_init_(Size :: integer()) -> any().
bitset_init_(Size) ->
  .

-spec bitset_fix(Idx :: integer()) -> any().
bitset_fix(Idx) ->
  .

-spec bitset_unfix(Idx :: integer()) -> any().
bitset_unfix(Idx) ->
  .

-spec bitset_flip() -> any().
bitset_flip() ->
  .

-spec bitset_all() -> boolean().
bitset_all() ->
  .

-spec bitset_one() -> boolean().
bitset_one() ->
  .

-spec bitset_count() -> integer().
bitset_count() ->
  .

-spec bitset_to_string() -> unicode:unicode_binary().
bitset_to_string() ->
  .


%% Your functions will be called as such:
%% bitset_init_(Size),
%% bitset_fix(Idx),
%% bitset_unfix(Idx),
%% bitset_flip(),
%% Param_4 = bitset_all(),
%% Param_5 = bitset_one(),
%% Param_6 = bitset_count(),
%% Param_7 = bitset_to_string(),

%% bitset_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Bitset do
  @spec init_(size :: integer) :: any
  def init_(size) do
    
  end

  @spec fix(idx :: integer) :: any
  def fix(idx) do
    
  end

  @spec unfix(idx :: integer) :: any
  def unfix(idx) do
    
  end

  @spec flip() :: any
  def flip() do
    
  end

  @spec all() :: boolean
  def all() do
    
  end

  @spec one() :: boolean
  def one() do
    
  end

  @spec count() :: integer
  def count() do
    
  end

  @spec to_string() :: String.t
  def to_string() do
    
  end
end

# Your functions will be called as such:
# Bitset.init_(size)
# Bitset.fix(idx)
# Bitset.unfix(idx)
# Bitset.flip()
# param_4 = Bitset.all()
# param_5 = Bitset.one()
# param_6 = Bitset.count()
# param_7 = Bitset.to_string()

# Bitset.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Bitset {
    init(size: Int64) {

    }
    
    func fix(idx: Int64): Unit {

    }
    
    func unfix(idx: Int64): Unit {

    }
    
    func flip(): Unit {

    }
    
    func all(): Bool {

    }
    
    func one(): Bool {

    }
    
    func count(): Int64 {

    }
    
    func toString(): String {

    }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * let obj: Bitset = Bitset(size)
 * obj.fix(idx)
 * obj.unfix(idx)
 * obj.flip()
 * let param_4 = obj.all()
 * let param_5 = obj.one()
 * let param_6 = obj.count()
 * let param_7 = obj.toString()
 */
```

