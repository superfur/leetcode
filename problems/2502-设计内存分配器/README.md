# 2502. 设计内存分配器

## 题目描述

<p>给你一个整数 <code>n</code> ，表示下标从 <strong>0</strong> 开始的内存数组的大小。所有内存单元开始都是空闲的。</p>

<p>请你设计一个具备以下功能的内存分配器：</p>

<ol>
	<li><strong>分配 </strong>一块大小为 <code>size</code> 的连续空闲内存单元并赋 id <code>mID</code> 。</li>
	<li><strong>释放</strong> 给定 id <code>mID</code> 对应的所有内存单元。</li>
</ol>

<p><strong>注意：</strong></p>

<ul>
	<li>多个块可以被分配到同一个 <code>mID</code> 。</li>
	<li>你必须释放 <code>mID</code> 对应的所有内存单元，即便这些内存单元被分配在不同的块中。</li>
</ul>

<p>实现 <code>Allocator</code> 类：</p>

<ul>
	<li><code>Allocator(int n)</code> 使用一个大小为 <code>n</code> 的内存数组初始化 <code>Allocator</code> 对象。</li>
	<li><code>int allocate(int size, int mID)</code> 找出大小为 <code>size</code> 个连续空闲内存单元且位于&nbsp; <strong>最左侧</strong> 的块，分配并赋 id <code>mID</code> 。返回块的第一个下标。如果不存在这样的块，返回 <code>-1</code> 。</li>
	<li><code>int freeMemory(int mID)</code> 释放 id <code>mID</code> 对应的所有内存单元。返回释放的内存单元数目。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["Allocator", "allocate", "allocate", "allocate", "freeMemory", "allocate", "allocate", "allocate", "freeMemory", "allocate", "freeMemory"]
[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]
<strong>输出</strong>
[null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]

<strong>解释</strong>
Allocator loc = new Allocator(10); // 初始化一个大小为 10 的内存数组，所有内存单元都是空闲的。
loc.allocate(1, 1); // 最左侧的块的第一个下标是 0 。内存数组变为 [<strong>1</strong>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>]。返回 0 。
loc.allocate(1, 2); // 最左侧的块的第一个下标是 1 。内存数组变为 [1,<strong>2</strong>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>]。返回 1 。
loc.allocate(1, 3); // 最左侧的块的第一个下标是 2 。内存数组变为 [1,2,<strong>3</strong>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>]。返回 2 。
loc.freeMemory(2); // 释放 mID 为 2 的所有内存单元。内存数组变为 [1,<u> </u>,<strong>3</strong>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>,<u> </u>] 。返回 1 ，因为只有 1 个 mID 为 2 的内存单元。
loc.allocate(3, 4); // 最左侧的块的第一个下标是 3 。内存数组变为 [1,<u> </u>,3,<strong>4</strong>,<strong>4</strong>,<strong>4</strong>,<u> </u>,<u> </u>,<u> </u>,<u> </u>]。返回 3 。
loc.allocate(1, 1); // 最左侧的块的第一个下标是 1 。内存数组变为 [1,<strong>1</strong>,3,4,4,4,<u> </u>,<u> </u>,<u> </u>,<u> </u>]。返回 1 。
loc.allocate(1, 1); // 最左侧的块的第一个下标是 6 。内存数组变为 [1,1,3,4,4,4,<strong>1</strong>,<u> </u>,<u> </u>,<u> </u>]。返回 6 。
loc.freeMemory(1); // 释放 mID 为 1 的所有内存单元。内存数组变为 [<u> </u>,<u> </u>,3,4,4,4,<u><strong> </strong></u>,<u> </u>,<u> </u>,<u> </u>] 。返回 3 ，因为有 3 个 mID 为 1 的内存单元。
loc.allocate(10, 2); // 无法找出长度为 10 个连续空闲内存单元的空闲块，所有返回 -1 。
loc.freeMemory(7); // 释放 mID 为 7 的所有内存单元。内存数组保持原状，因为不存在 mID 为 7 的内存单元。返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, size, mID &lt;= 1000</code></li>
	<li>最多调用 <code>allocate</code> 和 <code>free</code> 方法 <code>1000</code> 次</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 哈希表
- 模拟

## 提示

1. Can you simulate the process?
2. Use brute force to find the leftmost free block and free each occupied memory unit

## 示例

```
["Allocator","allocate","allocate","allocate","freeMemory","allocate","allocate","allocate","freeMemory","allocate","freeMemory"]
[[10],[1,1],[1,2],[1,3],[2],[3,4],[1,1],[1,1],[1],[10,2],[7]]
```

## 示例代码

### C++

```cpp
class Allocator {
public:
    Allocator(int n) {
        
    }
    
    int allocate(int size, int mID) {
        
    }
    
    int freeMemory(int mID) {
        
    }
};

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator* obj = new Allocator(n);
 * int param_1 = obj->allocate(size,mID);
 * int param_2 = obj->freeMemory(mID);
 */
```

### Java

```java
class Allocator {

    public Allocator(int n) {
        
    }
    
    public int allocate(int size, int mID) {
        
    }
    
    public int freeMemory(int mID) {
        
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator obj = new Allocator(n);
 * int param_1 = obj.allocate(size,mID);
 * int param_2 = obj.freeMemory(mID);
 */
```

### Python

```python
class Allocator(object):

    def __init__(self, n):
        """
        :type n: int
        """
        

    def allocate(self, size, mID):
        """
        :type size: int
        :type mID: int
        :rtype: int
        """
        

    def freeMemory(self, mID):
        """
        :type mID: int
        :rtype: int
        """
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
```

### Python3

```python3
class Allocator:

    def __init__(self, n: int):
        

    def allocate(self, size: int, mID: int) -> int:
        

    def freeMemory(self, mID: int) -> int:
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
```

### C

```c



typedef struct {
    
} Allocator;


Allocator* allocatorCreate(int n) {
    
}

int allocatorAllocate(Allocator* obj, int size, int mID) {
    
}

int allocatorFreeMemory(Allocator* obj, int mID) {
    
}

void allocatorFree(Allocator* obj) {
    
}

/**
 * Your Allocator struct will be instantiated and called as such:
 * Allocator* obj = allocatorCreate(n);
 * int param_1 = allocatorAllocate(obj, size, mID);
 
 * int param_2 = allocatorFreeMemory(obj, mID);
 
 * allocatorFree(obj);
*/
```

### C#

```csharp
public class Allocator {

    public Allocator(int n) {
        
    }
    
    public int Allocate(int size, int mID) {
        
    }
    
    public int FreeMemory(int mID) {
        
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator obj = new Allocator(n);
 * int param_1 = obj.Allocate(size,mID);
 * int param_2 = obj.FreeMemory(mID);
 */
```

### JavaScript

```javascript
/**
 * @param {number} n
 */
var Allocator = function(n) {
    
};

/** 
 * @param {number} size 
 * @param {number} mID
 * @return {number}
 */
Allocator.prototype.allocate = function(size, mID) {
    
};

/** 
 * @param {number} mID
 * @return {number}
 */
Allocator.prototype.freeMemory = function(mID) {
    
};

/** 
 * Your Allocator object will be instantiated and called as such:
 * var obj = new Allocator(n)
 * var param_1 = obj.allocate(size,mID)
 * var param_2 = obj.freeMemory(mID)
 */
```

### TypeScript

```typescript
class Allocator {
    constructor(n: number) {
        
    }

    allocate(size: number, mID: number): number {
        
    }

    freeMemory(mID: number): number {
        
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * var obj = new Allocator(n)
 * var param_1 = obj.allocate(size,mID)
 * var param_2 = obj.freeMemory(mID)
 */
```

### PHP

```php
class Allocator {
    /**
     * @param Integer $n
     */
    function __construct($n) {
        
    }
  
    /**
     * @param Integer $size
     * @param Integer $mID
     * @return Integer
     */
    function allocate($size, $mID) {
        
    }
  
    /**
     * @param Integer $mID
     * @return Integer
     */
    function freeMemory($mID) {
        
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * $obj = Allocator($n);
 * $ret_1 = $obj->allocate($size, $mID);
 * $ret_2 = $obj->freeMemory($mID);
 */
```

### Swift

```swift

class Allocator {

    init(_ n: Int) {
        
    }
    
    func allocate(_ size: Int, _ mID: Int) -> Int {
        
    }
    
    func freeMemory(_ mID: Int) -> Int {
        
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * let obj = Allocator(n)
 * let ret_1: Int = obj.allocate(size, mID)
 * let ret_2: Int = obj.freeMemory(mID)
 */
```

### Kotlin

```kotlin
class Allocator(n: Int) {

    fun allocate(size: Int, mID: Int): Int {
        
    }

    fun freeMemory(mID: Int): Int {
        
    }

}

/**
 * Your Allocator object will be instantiated and called as such:
 * var obj = Allocator(n)
 * var param_1 = obj.allocate(size,mID)
 * var param_2 = obj.freeMemory(mID)
 */
```

### Dart

```dart
class Allocator {

  Allocator(int n) {
    
  }
  
  int allocate(int size, int mID) {
    
  }
  
  int freeMemory(int mID) {
    
  }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator obj = Allocator(n);
 * int param1 = obj.allocate(size,mID);
 * int param2 = obj.freeMemory(mID);
 */
```

### Go

```golang
type Allocator struct {
    
}


func Constructor(n int) Allocator {
    
}


func (this *Allocator) Allocate(size int, mID int) int {
    
}


func (this *Allocator) FreeMemory(mID int) int {
    
}


/**
 * Your Allocator object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Allocate(size,mID);
 * param_2 := obj.FreeMemory(mID);
 */
```

### Ruby

```ruby
class Allocator

=begin
    :type n: Integer
=end
    def initialize(n)
        
    end


=begin
    :type size: Integer
    :type m_id: Integer
    :rtype: Integer
=end
    def allocate(size, m_id)
        
    end


=begin
    :type m_id: Integer
    :rtype: Integer
=end
    def free_memory(m_id)
        
    end


end

# Your Allocator object will be instantiated and called as such:
# obj = Allocator.new(n)
# param_1 = obj.allocate(size, m_id)
# param_2 = obj.free_memory(m_id)
```

### Scala

```scala
class Allocator(_n: Int) {

    def allocate(size: Int, mID: Int): Int = {
        
    }

    def freeMemory(mID: Int): Int = {
        
    }

}

/**
 * Your Allocator object will be instantiated and called as such:
 * val obj = new Allocator(n)
 * val param_1 = obj.allocate(size,mID)
 * val param_2 = obj.freeMemory(mID)
 */
```

### Rust

```rust
struct Allocator {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Allocator {

    fn new(n: i32) -> Self {
        
    }
    
    fn allocate(&self, size: i32, m_id: i32) -> i32 {
        
    }
    
    fn free_memory(&self, m_id: i32) -> i32 {
        
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * let obj = Allocator::new(n);
 * let ret_1: i32 = obj.allocate(size, mID);
 * let ret_2: i32 = obj.free_memory(mID);
 */
```

### Racket

```racket
(define allocator%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    (init-field
      n)
    
    ; allocate : exact-integer? exact-integer? -> exact-integer?
    (define/public (allocate size m-id)
      )
    ; free-memory : exact-integer? -> exact-integer?
    (define/public (free-memory m-id)
      )))

;; Your allocator% object will be instantiated and called as such:
;; (define obj (new allocator% [n n]))
;; (define param_1 (send obj allocate size m-id))
;; (define param_2 (send obj free-memory m-id))
```

### Erlang

```erlang
-spec allocator_init_(N :: integer()) -> any().
allocator_init_(N) ->
  .

-spec allocator_allocate(Size :: integer(), MID :: integer()) -> integer().
allocator_allocate(Size, MID) ->
  .

-spec allocator_free_memory(MID :: integer()) -> integer().
allocator_free_memory(MID) ->
  .


%% Your functions will be called as such:
%% allocator_init_(N),
%% Param_1 = allocator_allocate(Size, MID),
%% Param_2 = allocator_free_memory(MID),

%% allocator_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Allocator do
  @spec init_(n :: integer) :: any
  def init_(n) do
    
  end

  @spec allocate(size :: integer, m_id :: integer) :: integer
  def allocate(size, m_id) do
    
  end

  @spec free_memory(m_id :: integer) :: integer
  def free_memory(m_id) do
    
  end
end

# Your functions will be called as such:
# Allocator.init_(n)
# param_1 = Allocator.allocate(size, m_id)
# param_2 = Allocator.free_memory(m_id)

# Allocator.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Allocator {
    init(n: Int64) {

    }
    
    func allocate(size: Int64, mID: Int64): Int64 {

    }
    
    func freeMemory(mID: Int64): Int64 {

    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * let obj: Allocator = Allocator(n)
 * let param_1 = obj.allocate(size,mID)
 * let param_2 = obj.freeMemory(mID)
 */
```

