# 1146. 快照数组

## 题目描述

<p>实现支持下列接口的「快照数组」-&nbsp;SnapshotArray：</p>

<ul>
	<li><code>SnapshotArray(int length)</code>&nbsp;- 初始化一个与指定长度相等的 类数组 的数据结构。<strong>初始时，每个元素都等于</strong><strong>&nbsp;0</strong>。</li>
	<li><code>void set(index, val)</code>&nbsp;- 会将指定索引&nbsp;<code>index</code>&nbsp;处的元素设置为&nbsp;<code>val</code>。</li>
	<li><code>int snap()</code>&nbsp;- 获取该数组的快照，并返回快照的编号&nbsp;<code>snap_id</code>（快照号是调用&nbsp;<code>snap()</code>&nbsp;的总次数减去&nbsp;<code>1</code>）。</li>
	<li><code>int get(index, snap_id)</code>&nbsp;- 根据指定的&nbsp;<code>snap_id</code>&nbsp;选择快照，并返回该快照指定索引 <code>index</code>&nbsp;的值。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[&quot;SnapshotArray&quot;,&quot;set&quot;,&quot;snap&quot;,&quot;set&quot;,&quot;get&quot;]
     [[3],[0,5],[],[0,6],[0,0]]
<strong>输出：</strong>[null,null,0,null,5]
<strong>解释：
</strong>SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
snapshotArr.set(0,5);  // 令 array[0] = 5
snapshotArr.snap();  // 获取快照，返回 snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= length&nbsp;&lt;= 50000</code></li>
	<li>题目最多进行<code>50000</code> 次<code>set</code>，<code>snap</code>，和&nbsp;<code>get</code>的调用 。</li>
	<li><code>0 &lt;= index&nbsp;&lt;&nbsp;length</code></li>
	<li><code>0 &lt;=&nbsp;snap_id &lt;&nbsp;</code>我们调用&nbsp;<code>snap()</code>&nbsp;的总次数</li>
	<li><code>0 &lt;=&nbsp;val &lt;= 10^9</code></li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 哈希表
- 二分查找

## 提示

1. Use a list of lists, adding both the element and the snap_id to each index.

## 示例

```
["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
```

## 示例代码

### C++

```cpp
class SnapshotArray {
public:
    SnapshotArray(int length) {
        
    }
    
    void set(int index, int val) {
        
    }
    
    int snap() {
        
    }
    
    int get(int index, int snap_id) {
        
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */
```

### Java

```java
class SnapshotArray {

    public SnapshotArray(int length) {
        
    }
    
    public void set(int index, int val) {
        
    }
    
    public int snap() {
        
    }
    
    public int get(int index, int snap_id) {
        
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.set(index,val);
 * int param_2 = obj.snap();
 * int param_3 = obj.get(index,snap_id);
 */
```

### Python

```python
class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def snap(self):
        """
        :rtype: int
        """
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
```

### Python3

```python3
class SnapshotArray:

    def __init__(self, length: int):
        

    def set(self, index: int, val: int) -> None:
        

    def snap(self) -> int:
        

    def get(self, index: int, snap_id: int) -> int:
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
```

### C

```c



typedef struct {
    
} SnapshotArray;


SnapshotArray* snapshotArrayCreate(int length) {
    
}

void snapshotArraySet(SnapshotArray* obj, int index, int val) {
    
}

int snapshotArraySnap(SnapshotArray* obj) {
    
}

int snapshotArrayGet(SnapshotArray* obj, int index, int snap_id) {
    
}

void snapshotArrayFree(SnapshotArray* obj) {
    
}

/**
 * Your SnapshotArray struct will be instantiated and called as such:
 * SnapshotArray* obj = snapshotArrayCreate(length);
 * snapshotArraySet(obj, index, val);
 
 * int param_2 = snapshotArraySnap(obj);
 
 * int param_3 = snapshotArrayGet(obj, index, snap_id);
 
 * snapshotArrayFree(obj);
*/
```

### C#

```csharp
public class SnapshotArray {

    public SnapshotArray(int length) {
        
    }
    
    public void Set(int index, int val) {
        
    }
    
    public int Snap() {
        
    }
    
    public int Get(int index, int snap_id) {
        
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = new SnapshotArray(length);
 * obj.Set(index,val);
 * int param_2 = obj.Snap();
 * int param_3 = obj.Get(index,snap_id);
 */
```

### JavaScript

```javascript
/**
 * @param {number} length
 */
var SnapshotArray = function(length) {
    
};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
SnapshotArray.prototype.set = function(index, val) {
    
};

/**
 * @return {number}
 */
SnapshotArray.prototype.snap = function() {
    
};

/** 
 * @param {number} index 
 * @param {number} snap_id
 * @return {number}
 */
SnapshotArray.prototype.get = function(index, snap_id) {
    
};

/** 
 * Your SnapshotArray object will be instantiated and called as such:
 * var obj = new SnapshotArray(length)
 * obj.set(index,val)
 * var param_2 = obj.snap()
 * var param_3 = obj.get(index,snap_id)
 */
```

### TypeScript

```typescript
class SnapshotArray {
    constructor(length: number) {
        
    }

    set(index: number, val: number): void {
        
    }

    snap(): number {
        
    }

    get(index: number, snap_id: number): number {
        
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * var obj = new SnapshotArray(length)
 * obj.set(index,val)
 * var param_2 = obj.snap()
 * var param_3 = obj.get(index,snap_id)
 */
```

### PHP

```php
class SnapshotArray {
    /**
     * @param Integer $length
     */
    function __construct($length) {
        
    }
  
    /**
     * @param Integer $index
     * @param Integer $val
     * @return NULL
     */
    function set($index, $val) {
        
    }
  
    /**
     * @return Integer
     */
    function snap() {
        
    }
  
    /**
     * @param Integer $index
     * @param Integer $snap_id
     * @return Integer
     */
    function get($index, $snap_id) {
        
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * $obj = SnapshotArray($length);
 * $obj->set($index, $val);
 * $ret_2 = $obj->snap();
 * $ret_3 = $obj->get($index, $snap_id);
 */
```

### Swift

```swift

class SnapshotArray {

    init(_ length: Int) {
        
    }
    
    func set(_ index: Int, _ val: Int) {
        
    }
    
    func snap() -> Int {
        
    }
    
    func get(_ index: Int, _ snap_id: Int) -> Int {
        
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj = SnapshotArray(length)
 * obj.set(index, val)
 * let ret_2: Int = obj.snap()
 * let ret_3: Int = obj.get(index, snap_id)
 */
```

### Kotlin

```kotlin
class SnapshotArray(length: Int) {

    fun set(index: Int, `val`: Int) {
        
    }

    fun snap(): Int {
        
    }

    fun get(index: Int, snap_id: Int): Int {
        
    }

}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * var obj = SnapshotArray(length)
 * obj.set(index,`val`)
 * var param_2 = obj.snap()
 * var param_3 = obj.get(index,snap_id)
 */
```

### Dart

```dart
class SnapshotArray {

  SnapshotArray(int length) {
    
  }
  
  void set(int index, int val) {
    
  }
  
  int snap() {
    
  }
  
  int get(int index, int snap_id) {
    
  }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray obj = SnapshotArray(length);
 * obj.set(index,val);
 * int param2 = obj.snap();
 * int param3 = obj.get(index,snap_id);
 */
```

### Go

```golang
type SnapshotArray struct {
    
}


func Constructor(length int) SnapshotArray {
    
}


func (this *SnapshotArray) Set(index int, val int)  {
    
}


func (this *SnapshotArray) Snap() int {
    
}


func (this *SnapshotArray) Get(index int, snap_id int) int {
    
}


/**
 * Your SnapshotArray object will be instantiated and called as such:
 * obj := Constructor(length);
 * obj.Set(index,val);
 * param_2 := obj.Snap();
 * param_3 := obj.Get(index,snap_id);
 */
```

### Ruby

```ruby
class SnapshotArray

=begin
    :type length: Integer
=end
    def initialize(length)
        
    end


=begin
    :type index: Integer
    :type val: Integer
    :rtype: Void
=end
    def set(index, val)
        
    end


=begin
    :rtype: Integer
=end
    def snap()
        
    end


=begin
    :type index: Integer
    :type snap_id: Integer
    :rtype: Integer
=end
    def get(index, snap_id)
        
    end


end

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray.new(length)
# obj.set(index, val)
# param_2 = obj.snap()
# param_3 = obj.get(index, snap_id)
```

### Scala

```scala
class SnapshotArray(_length: Int) {

    def set(index: Int, `val`: Int): Unit = {
        
    }

    def snap(): Int = {
        
    }

    def get(index: Int, snap_id: Int): Int = {
        
    }

}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * val obj = new SnapshotArray(length)
 * obj.set(index,`val`)
 * val param_2 = obj.snap()
 * val param_3 = obj.get(index,snap_id)
 */
```

### Rust

```rust
struct SnapshotArray {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SnapshotArray {

    fn new(length: i32) -> Self {
        
    }
    
    fn set(&self, index: i32, val: i32) {
        
    }
    
    fn snap(&self) -> i32 {
        
    }
    
    fn get(&self, index: i32, snap_id: i32) -> i32 {
        
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj = SnapshotArray::new(length);
 * obj.set(index, val);
 * let ret_2: i32 = obj.snap();
 * let ret_3: i32 = obj.get(index, snap_id);
 */
```

### Racket

```racket
(define snapshot-array%
  (class object%
    (super-new)
    
    ; length : exact-integer?
    (init-field
      length)
    
    ; set : exact-integer? exact-integer? -> void?
    (define/public (set index val)
      )
    ; snap : -> exact-integer?
    (define/public (snap)
      )
    ; get : exact-integer? exact-integer? -> exact-integer?
    (define/public (get index snap_id)
      )))

;; Your snapshot-array% object will be instantiated and called as such:
;; (define obj (new snapshot-array% [length length]))
;; (send obj set index val)
;; (define param_2 (send obj snap))
;; (define param_3 (send obj get index snap_id))
```

### Erlang

```erlang
-spec snapshot_array_init_(Length :: integer()) -> any().
snapshot_array_init_(Length) ->
  .

-spec snapshot_array_set(Index :: integer(), Val :: integer()) -> any().
snapshot_array_set(Index, Val) ->
  .

-spec snapshot_array_snap() -> integer().
snapshot_array_snap() ->
  .

-spec snapshot_array_get(Index :: integer(), Snap_id :: integer()) -> integer().
snapshot_array_get(Index, Snap_id) ->
  .


%% Your functions will be called as such:
%% snapshot_array_init_(Length),
%% snapshot_array_set(Index, Val),
%% Param_2 = snapshot_array_snap(),
%% Param_3 = snapshot_array_get(Index, Snap_id),

%% snapshot_array_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule SnapshotArray do
  @spec init_(length :: integer) :: any
  def init_(length) do
    
  end

  @spec set(index :: integer, val :: integer) :: any
  def set(index, val) do
    
  end

  @spec snap() :: integer
  def snap() do
    
  end

  @spec get(index :: integer, snap_id :: integer) :: integer
  def get(index, snap_id) do
    
  end
end

# Your functions will be called as such:
# SnapshotArray.init_(length)
# SnapshotArray.set(index, val)
# param_2 = SnapshotArray.snap()
# param_3 = SnapshotArray.get(index, snap_id)

# SnapshotArray.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class SnapshotArray {
    init(length: Int64) {

    }
    
    func set(index: Int64, val: Int64): Unit {

    }
    
    func snap(): Int64 {

    }
    
    func get(index: Int64, snap_id: Int64): Int64 {

    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj: SnapshotArray = SnapshotArray(length)
 * obj.set(index,val)
 * let param_2 = obj.snap()
 * let param_3 = obj.get(index,snap_id)
 */
```

