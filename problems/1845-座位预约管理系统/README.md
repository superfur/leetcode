# 1845. 座位预约管理系统

## 题目描述

<p>请你设计一个管理 <code>n</code> 个座位预约的系统，座位编号从 <code>1</code> 到 <code>n</code> 。</p>

<p>请你实现 <code>SeatManager</code> 类：</p>

<ul>
	<li><code>SeatManager(int n)</code> 初始化一个 <code>SeatManager</code> 对象，它管理从 <code>1</code> 到 <code>n</code> 编号的 <code>n</code> 个座位。所有座位初始都是可预约的。</li>
	<li><code>int reserve()</code> 返回可以预约座位的 <strong>最小编号</strong> ，此座位变为不可预约。</li>
	<li><code>void unreserve(int seatNumber)</code> 将给定编号 <code>seatNumber</code> 对应的座位变成可以预约。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
<strong>输出：</strong>
[null, 1, 2, null, 2, 3, 4, 5, null]

<strong>解释：</strong>
SeatManager seatManager = new SeatManager(5); // 初始化 SeatManager ，有 5 个座位。
seatManager.reserve();    // 所有座位都可以预约，所以返回最小编号的座位，也就是 1 。
seatManager.reserve();    // 可以预约的座位为 [2,3,4,5] ，返回最小编号的座位，也就是 2 。
seatManager.unreserve(2); // 将座位 2 变为可以预约，现在可预约的座位为 [2,3,4,5] 。
seatManager.reserve();    // 可以预约的座位为 [2,3,4,5] ，返回最小编号的座位，也就是 2 。
seatManager.reserve();    // 可以预约的座位为 [3,4,5] ，返回最小编号的座位，也就是 3 。
seatManager.reserve();    // 可以预约的座位为 [4,5] ，返回最小编号的座位，也就是 4 。
seatManager.reserve();    // 唯一可以预约的是座位 5 ，所以返回 5 。
seatManager.unreserve(5); // 将座位 5 变为可以预约，现在可预约的座位为 [5] 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= seatNumber &lt;= n</code></li>
	<li>每一次对 <code>reserve</code> 的调用，题目保证至少存在一个可以预约的座位。</li>
	<li>每一次对 <code>unreserve</code> 的调用，题目保证 <code>seatNumber</code> 在调用函数前都是被预约状态。</li>
	<li>对 <code>reserve</code> 和 <code>unreserve</code> 的调用 <strong>总共</strong> 不超过 <code>10<sup>5</sup></code> 次。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 堆（优先队列）

## 提示

1. You need a data structure that maintains the states of the seats. This data structure should also allow you to get the first available seat and flip the state of a seat in a reasonable time.
2. You can let the data structure contain the available seats. Then you want to be able to get the lowest element and erase an element, in a reasonable time.
3. Ordered sets support these operations.

## 示例

```
["SeatManager","reserve","reserve","unreserve","reserve","reserve","reserve","reserve","unreserve"]
[[5],[],[],[2],[],[],[],[],[5]]
```

## 示例代码

### C++

```cpp
class SeatManager {
public:
    SeatManager(int n) {
        
    }
    
    int reserve() {
        
    }
    
    void unreserve(int seatNumber) {
        
    }
};

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager* obj = new SeatManager(n);
 * int param_1 = obj->reserve();
 * obj->unreserve(seatNumber);
 */
```

### Java

```java
class SeatManager {

    public SeatManager(int n) {
        
    }
    
    public int reserve() {
        
    }
    
    public void unreserve(int seatNumber) {
        
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */
```

### Python

```python
class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        

    def reserve(self):
        """
        :rtype: int
        """
        

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
```

### Python3

```python3
class SeatManager:

    def __init__(self, n: int):
        

    def reserve(self) -> int:
        

    def unreserve(self, seatNumber: int) -> None:
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
```

### C

```c



typedef struct {
    
} SeatManager;


SeatManager* seatManagerCreate(int n) {
    
}

int seatManagerReserve(SeatManager* obj) {
    
}

void seatManagerUnreserve(SeatManager* obj, int seatNumber) {
    
}

void seatManagerFree(SeatManager* obj) {
    
}

/**
 * Your SeatManager struct will be instantiated and called as such:
 * SeatManager* obj = seatManagerCreate(n);
 * int param_1 = seatManagerReserve(obj);
 
 * seatManagerUnreserve(obj, seatNumber);
 
 * seatManagerFree(obj);
*/
```

### C#

```csharp
public class SeatManager {

    public SeatManager(int n) {
        
    }
    
    public int Reserve() {
        
    }
    
    public void Unreserve(int seatNumber) {
        
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.Reserve();
 * obj.Unreserve(seatNumber);
 */
```

### JavaScript

```javascript
/**
 * @param {number} n
 */
var SeatManager = function(n) {
    
};

/**
 * @return {number}
 */
SeatManager.prototype.reserve = function() {
    
};

/** 
 * @param {number} seatNumber
 * @return {void}
 */
SeatManager.prototype.unreserve = function(seatNumber) {
    
};

/** 
 * Your SeatManager object will be instantiated and called as such:
 * var obj = new SeatManager(n)
 * var param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */
```

### TypeScript

```typescript
class SeatManager {
    constructor(n: number) {
        
    }

    reserve(): number {
        
    }

    unreserve(seatNumber: number): void {
        
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * var obj = new SeatManager(n)
 * var param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */
```

### PHP

```php
class SeatManager {
    /**
     * @param Integer $n
     */
    function __construct($n) {
        
    }
  
    /**
     * @return Integer
     */
    function reserve() {
        
    }
  
    /**
     * @param Integer $seatNumber
     * @return NULL
     */
    function unreserve($seatNumber) {
        
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * $obj = SeatManager($n);
 * $ret_1 = $obj->reserve();
 * $obj->unreserve($seatNumber);
 */
```

### Swift

```swift

class SeatManager {

    init(_ n: Int) {
        
    }
    
    func reserve() -> Int {
        
    }
    
    func unreserve(_ seatNumber: Int) {
        
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * let obj = SeatManager(n)
 * let ret_1: Int = obj.reserve()
 * obj.unreserve(seatNumber)
 */
```

### Kotlin

```kotlin
class SeatManager(n: Int) {

    fun reserve(): Int {
        
    }

    fun unreserve(seatNumber: Int) {
        
    }

}

/**
 * Your SeatManager object will be instantiated and called as such:
 * var obj = SeatManager(n)
 * var param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */
```

### Dart

```dart
class SeatManager {

  SeatManager(int n) {
    
  }
  
  int reserve() {
    
  }
  
  void unreserve(int seatNumber) {
    
  }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = SeatManager(n);
 * int param1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */
```

### Go

```golang
type SeatManager struct {
    
}


func Constructor(n int) SeatManager {
    
}


func (this *SeatManager) Reserve() int {
    
}


func (this *SeatManager) Unreserve(seatNumber int)  {
    
}


/**
 * Your SeatManager object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Reserve();
 * obj.Unreserve(seatNumber);
 */
```

### Ruby

```ruby
class SeatManager

=begin
    :type n: Integer
=end
    def initialize(n)
        
    end


=begin
    :rtype: Integer
=end
    def reserve()
        
    end


=begin
    :type seat_number: Integer
    :rtype: Void
=end
    def unreserve(seat_number)
        
    end


end

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager.new(n)
# param_1 = obj.reserve()
# obj.unreserve(seat_number)
```

### Scala

```scala
class SeatManager(_n: Int) {

    def reserve(): Int = {
        
    }

    def unreserve(seatNumber: Int): Unit = {
        
    }

}

/**
 * Your SeatManager object will be instantiated and called as such:
 * val obj = new SeatManager(n)
 * val param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */
```

### Rust

```rust
struct SeatManager {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SeatManager {

    fn new(n: i32) -> Self {
        
    }
    
    fn reserve(&self) -> i32 {
        
    }
    
    fn unreserve(&self, seat_number: i32) {
        
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * let obj = SeatManager::new(n);
 * let ret_1: i32 = obj.reserve();
 * obj.unreserve(seatNumber);
 */
```

### Racket

```racket
(define seat-manager%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    (init-field
      n)
    
    ; reserve : -> exact-integer?
    (define/public (reserve)
      )
    ; unreserve : exact-integer? -> void?
    (define/public (unreserve seat-number)
      )))

;; Your seat-manager% object will be instantiated and called as such:
;; (define obj (new seat-manager% [n n]))
;; (define param_1 (send obj reserve))
;; (send obj unreserve seat-number)
```

### Erlang

```erlang
-spec seat_manager_init_(N :: integer()) -> any().
seat_manager_init_(N) ->
  .

-spec seat_manager_reserve() -> integer().
seat_manager_reserve() ->
  .

-spec seat_manager_unreserve(SeatNumber :: integer()) -> any().
seat_manager_unreserve(SeatNumber) ->
  .


%% Your functions will be called as such:
%% seat_manager_init_(N),
%% Param_1 = seat_manager_reserve(),
%% seat_manager_unreserve(SeatNumber),

%% seat_manager_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule SeatManager do
  @spec init_(n :: integer) :: any
  def init_(n) do
    
  end

  @spec reserve() :: integer
  def reserve() do
    
  end

  @spec unreserve(seat_number :: integer) :: any
  def unreserve(seat_number) do
    
  end
end

# Your functions will be called as such:
# SeatManager.init_(n)
# param_1 = SeatManager.reserve()
# SeatManager.unreserve(seat_number)

# SeatManager.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class SeatManager {
    init(n: Int64) {

    }
    
    func reserve(): Int64 {

    }
    
    func unreserve(seatNumber: Int64): Unit {

    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * let obj: SeatManager = SeatManager(n)
 * let param_1 = obj.reserve()
 * obj.unreserve(seatNumber)
 */
```

