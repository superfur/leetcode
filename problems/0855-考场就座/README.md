# 855. 考场就座

## 题目描述

<p>在考场里，有&nbsp;<code>n</code>&nbsp;个座位排成一行，编号为 <code>0</code> 到 <code>n - 1</code>。</p>

<p>当学生进入考场后，他必须坐在离最近的人最远的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在 <code>0</code> 号座位上。)</p>

<p>设计一个模拟所述考场的类。</p>

<p>实现&nbsp;<code>ExamRoom</code>&nbsp;类：</p>

<ul>
	<li><code>ExamRoom(int n)</code> 用座位的数量&nbsp;<code>n</code> 初始化考场对象。</li>
	<li><code>int seat()</code> 返回下一个学生将会入座的座位编号。</li>
	<li><code>void leave(int p)</code> 指定坐在座位 <code>p</code> 的学生将离开教室。保证座位 <code>p</code> 上会有一位学生。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
[[10], [], [], [], [], [4], []]
<strong>输出：</strong>
[null, 0, 9, 4, 2, null, 5]
<strong>解释：</strong>
ExamRoom examRoom = new ExamRoom(10);
examRoom.seat(); // 返回 0，房间里没有人，学生坐在 0 号座位。
examRoom.seat(); // 返回 9，学生最后坐在 9 号座位。
examRoom.seat(); // 返回 4，学生最后坐在 4 号座位。
examRoom.seat(); // 返回 2，学生最后坐在 2 号座位。
examRoom.leave(4);
examRoom.seat(); // 返回 5，学生最后坐在 5 号座位。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li>保证有学生正坐在座位 <code>p</code> 上。</li>
	<li><code>seat</code>&nbsp;和&nbsp;<code>leave</code>&nbsp;最多被调用&nbsp;<code>10<sup>4</sup></code>&nbsp;次。</li>
</ol>


## 难度

Medium

## 标签

- 设计
- 有序集合
- 堆（优先队列）

## 示例

```
["ExamRoom","seat","seat","seat","seat","leave","seat"]
[[10],[],[],[],[],[4],[]]
```

## 示例代码

### C++

```cpp
class ExamRoom {
public:
    ExamRoom(int n) {
        
    }
    
    int seat() {
        
    }
    
    void leave(int p) {
        
    }
};

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom* obj = new ExamRoom(n);
 * int param_1 = obj->seat();
 * obj->leave(p);
 */
```

### Java

```java
class ExamRoom {

    public ExamRoom(int n) {
        
    }
    
    public int seat() {
        
    }
    
    public void leave(int p) {
        
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(n);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */
```

### Python

```python
class ExamRoom(object):

    def __init__(self, n):
        """
        :type n: int
        """
        

    def seat(self):
        """
        :rtype: int
        """
        

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
```

### Python3

```python3
class ExamRoom:

    def __init__(self, n: int):
        

    def seat(self) -> int:
        

    def leave(self, p: int) -> None:
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
```

### C

```c



typedef struct {
    
} ExamRoom;


ExamRoom* examRoomCreate(int n) {
    
}

int examRoomSeat(ExamRoom* obj) {
    
}

void examRoomLeave(ExamRoom* obj, int p) {
    
}

void examRoomFree(ExamRoom* obj) {
    
}

/**
 * Your ExamRoom struct will be instantiated and called as such:
 * ExamRoom* obj = examRoomCreate(n);
 * int param_1 = examRoomSeat(obj);
 
 * examRoomLeave(obj, p);
 
 * examRoomFree(obj);
*/
```

### C#

```csharp
public class ExamRoom {

    public ExamRoom(int n) {
        
    }
    
    public int Seat() {
        
    }
    
    public void Leave(int p) {
        
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(n);
 * int param_1 = obj.Seat();
 * obj.Leave(p);
 */
```

### JavaScript

```javascript
/**
 * @param {number} n
 */
var ExamRoom = function(n) {
    
};

/**
 * @return {number}
 */
ExamRoom.prototype.seat = function() {
    
};

/** 
 * @param {number} p
 * @return {void}
 */
ExamRoom.prototype.leave = function(p) {
    
};

/** 
 * Your ExamRoom object will be instantiated and called as such:
 * var obj = new ExamRoom(n)
 * var param_1 = obj.seat()
 * obj.leave(p)
 */
```

### TypeScript

```typescript
class ExamRoom {
    constructor(n: number) {
        
    }

    seat(): number {
        
    }

    leave(p: number): void {
        
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * var obj = new ExamRoom(n)
 * var param_1 = obj.seat()
 * obj.leave(p)
 */
```

### PHP

```php
class ExamRoom {
    /**
     * @param Integer $n
     */
    function __construct($n) {
        
    }
  
    /**
     * @return Integer
     */
    function seat() {
        
    }
  
    /**
     * @param Integer $p
     * @return NULL
     */
    function leave($p) {
        
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * $obj = ExamRoom($n);
 * $ret_1 = $obj->seat();
 * $obj->leave($p);
 */
```

### Swift

```swift

class ExamRoom {

    init(_ n: Int) {
        
    }
    
    func seat() -> Int {
        
    }
    
    func leave(_ p: Int) {
        
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * let obj = ExamRoom(n)
 * let ret_1: Int = obj.seat()
 * obj.leave(p)
 */
```

### Kotlin

```kotlin
class ExamRoom(n: Int) {

    fun seat(): Int {
        
    }

    fun leave(p: Int) {
        
    }

}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * var obj = ExamRoom(n)
 * var param_1 = obj.seat()
 * obj.leave(p)
 */
```

### Dart

```dart
class ExamRoom {

  ExamRoom(int n) {
    
  }
  
  int seat() {
    
  }
  
  void leave(int p) {
    
  }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = ExamRoom(n);
 * int param1 = obj.seat();
 * obj.leave(p);
 */
```

### Go

```golang
type ExamRoom struct {
    
}


func Constructor(n int) ExamRoom {
    
}


func (this *ExamRoom) Seat() int {
    
}


func (this *ExamRoom) Leave(p int)  {
    
}


/**
 * Your ExamRoom object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Seat();
 * obj.Leave(p);
 */
```

### Ruby

```ruby
class ExamRoom

=begin
    :type n: Integer
=end
    def initialize(n)
        
    end


=begin
    :rtype: Integer
=end
    def seat()
        
    end


=begin
    :type p: Integer
    :rtype: Void
=end
    def leave(p)
        
    end


end

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom.new(n)
# param_1 = obj.seat()
# obj.leave(p)
```

### Scala

```scala
class ExamRoom(_n: Int) {

    def seat(): Int = {
        
    }

    def leave(p: Int): Unit = {
        
    }

}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * val obj = new ExamRoom(n)
 * val param_1 = obj.seat()
 * obj.leave(p)
 */
```

### Rust

```rust
struct ExamRoom {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ExamRoom {

    fn new(n: i32) -> Self {
        
    }
    
    fn seat(&self) -> i32 {
        
    }
    
    fn leave(&self, p: i32) {
        
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * let obj = ExamRoom::new(n);
 * let ret_1: i32 = obj.seat();
 * obj.leave(p);
 */
```

### Racket

```racket
(define exam-room%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    (init-field
      n)
    
    ; seat : -> exact-integer?
    (define/public (seat)
      )
    ; leave : exact-integer? -> void?
    (define/public (leave p)
      )))

;; Your exam-room% object will be instantiated and called as such:
;; (define obj (new exam-room% [n n]))
;; (define param_1 (send obj seat))
;; (send obj leave p)
```

### Erlang

```erlang
-spec exam_room_init_(N :: integer()) -> any().
exam_room_init_(N) ->
  .

-spec exam_room_seat() -> integer().
exam_room_seat() ->
  .

-spec exam_room_leave(P :: integer()) -> any().
exam_room_leave(P) ->
  .


%% Your functions will be called as such:
%% exam_room_init_(N),
%% Param_1 = exam_room_seat(),
%% exam_room_leave(P),

%% exam_room_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule ExamRoom do
  @spec init_(n :: integer) :: any
  def init_(n) do
    
  end

  @spec seat() :: integer
  def seat() do
    
  end

  @spec leave(p :: integer) :: any
  def leave(p) do
    
  end
end

# Your functions will be called as such:
# ExamRoom.init_(n)
# param_1 = ExamRoom.seat()
# ExamRoom.leave(p)

# ExamRoom.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class ExamRoom {
    init(n: Int64) {

    }
    
    func seat(): Int64 {

    }
    
    func leave(p: Int64): Unit {

    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * let obj: ExamRoom = ExamRoom(n)
 * let param_1 = obj.seat()
 * obj.leave(p)
 */
```

