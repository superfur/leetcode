# 729. 我的日程安排表 I

## 题目描述

<p>实现一个 <code>MyCalendar</code> 类来存放你的日程安排。如果要添加的日程安排不会造成 <strong>重复预订</strong> ，则可以存储这个新的日程安排。</p>

<p>当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 <strong>重复预订</strong> 。</p>

<p>日程可以用一对整数 <code>startTime</code> 和 <code>endTime</code> 表示，这里的时间是半开区间，即 <code>[startTime, endTime)</code>, 实数&nbsp;<code>x</code> 的范围为， &nbsp;<code>startTime &lt;= x &lt; endTime</code> 。</p>

<p>实现 <code>MyCalendar</code> 类：</p>

<ul>
	<li><code>MyCalendar()</code> 初始化日历对象。</li>
	<li><code>boolean book(int startTime, int endTime)</code> 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 <code>true</code> 。否则，返回 <code>false</code>&nbsp;并且不要将该日程安排添加到日历中。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例：</strong></p>

<pre>
<strong>输入：</strong>
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
<strong>输出：</strong>
[null, true, false, true]

<strong>解释：</strong>
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False ，这个日程安排不能添加到日历中，因为时间 15 已经被另一个日程安排预订了。
myCalendar.book(20, 30); // return True ，这个日程安排可以添加到日历中，因为第一个日程安排预订的每个时间都小于 20 ，且不包含时间 20 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= start &lt; end &lt;= 10<sup>9</sup></code></li>
	<li>每个测试用例，调用 <code>book</code> 方法的次数最多不超过 <code>1000</code> 次。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 线段树
- 数组
- 二分查找
- 有序集合

## 提示

1. Store the events as a sorted list of intervals.  If none of the events conflict, then the new event can be added.

## 示例

```
["MyCalendar","book","book","book"]
[[],[10,20],[15,25],[20,30]]
```

## 示例代码

### C++

```cpp
class MyCalendar {
public:
    MyCalendar() {
        
    }
    
    bool book(int startTime, int endTime) {
        
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(startTime,endTime);
 */
```

### Java

```java
class MyCalendar {

    public MyCalendar() {
        
    }
    
    public boolean book(int startTime, int endTime) {
        
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(startTime,endTime);
 */
```

### Python

```python
class MyCalendar(object):

    def __init__(self):
        

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
```

### Python3

```python3
class MyCalendar:

    def __init__(self):
        

    def book(self, startTime: int, endTime: int) -> bool:
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
```

### C

```c



typedef struct {
    
} MyCalendar;


MyCalendar* myCalendarCreate() {
    
}

bool myCalendarBook(MyCalendar* obj, int startTime, int endTime) {
    
}

void myCalendarFree(MyCalendar* obj) {
    
}

/**
 * Your MyCalendar struct will be instantiated and called as such:
 * MyCalendar* obj = myCalendarCreate();
 * bool param_1 = myCalendarBook(obj, startTime, endTime);
 
 * myCalendarFree(obj);
*/
```

### C#

```csharp
public class MyCalendar {

    public MyCalendar() {
        
    }
    
    public bool Book(int startTime, int endTime) {
        
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * bool param_1 = obj.Book(startTime,endTime);
 */
```

### JavaScript

```javascript

var MyCalendar = function() {
    
};

/** 
 * @param {number} startTime 
 * @param {number} endTime
 * @return {boolean}
 */
MyCalendar.prototype.book = function(startTime, endTime) {
    
};

/** 
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(startTime,endTime)
 */
```

### TypeScript

```typescript
class MyCalendar {
    constructor() {
        
    }

    book(startTime: number, endTime: number): boolean {
        
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(startTime,endTime)
 */
```

### PHP

```php
class MyCalendar {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $startTime
     * @param Integer $endTime
     * @return Boolean
     */
    function book($startTime, $endTime) {
        
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * $obj = MyCalendar();
 * $ret_1 = $obj->book($startTime, $endTime);
 */
```

### Swift

```swift

class MyCalendar {

    init() {
        
    }
    
    func book(_ startTime: Int, _ endTime: Int) -> Bool {
        
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * let obj = MyCalendar()
 * let ret_1: Bool = obj.book(startTime, endTime)
 */
```

### Kotlin

```kotlin
class MyCalendar() {

    fun book(startTime: Int, endTime: Int): Boolean {
        
    }

}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = MyCalendar()
 * var param_1 = obj.book(startTime,endTime)
 */
```

### Dart

```dart
class MyCalendar {

  MyCalendar() {
    
  }
  
  bool book(int startTime, int endTime) {
    
  }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = MyCalendar();
 * bool param1 = obj.book(startTime,endTime);
 */
```

### Go

```golang
type MyCalendar struct {
    
}


func Constructor() MyCalendar {
    
}


func (this *MyCalendar) Book(startTime int, endTime int) bool {
    
}


/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(startTime,endTime);
 */
```

### Ruby

```ruby
class MyCalendar
    def initialize()
        
    end


=begin
    :type start_time: Integer
    :type end_time: Integer
    :rtype: Boolean
=end
    def book(start_time, end_time)
        
    end


end

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar.new()
# param_1 = obj.book(start_time, end_time)
```

### Scala

```scala
class MyCalendar() {

    def book(startTime: Int, endTime: Int): Boolean = {
        
    }

}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * val obj = new MyCalendar()
 * val param_1 = obj.book(startTime,endTime)
 */
```

### Rust

```rust
struct MyCalendar {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCalendar {

    fn new() -> Self {
        
    }
    
    fn book(&self, start_time: i32, end_time: i32) -> bool {
        
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * let obj = MyCalendar::new();
 * let ret_1: bool = obj.book(startTime, endTime);
 */
```

### Racket

```racket
(define my-calendar%
  (class object%
    (super-new)
    
    (init-field)
    
    ; book : exact-integer? exact-integer? -> boolean?
    (define/public (book start-time end-time)
      )))

;; Your my-calendar% object will be instantiated and called as such:
;; (define obj (new my-calendar%))
;; (define param_1 (send obj book start-time end-time))
```

### Erlang

```erlang
-spec my_calendar_init_() -> any().
my_calendar_init_() ->
  .

-spec my_calendar_book(StartTime :: integer(), EndTime :: integer()) -> boolean().
my_calendar_book(StartTime, EndTime) ->
  .


%% Your functions will be called as such:
%% my_calendar_init_(),
%% Param_1 = my_calendar_book(StartTime, EndTime),

%% my_calendar_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MyCalendar do
  @spec init_() :: any
  def init_() do
    
  end

  @spec book(start_time :: integer, end_time :: integer) :: boolean
  def book(start_time, end_time) do
    
  end
end

# Your functions will be called as such:
# MyCalendar.init_()
# param_1 = MyCalendar.book(start_time, end_time)

# MyCalendar.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MyCalendar {
    init() {

    }
    
    func book(start: Int64, end: Int64): Bool {

    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * let obj: MyCalendar = MyCalendar()
 * let param_1 = obj.book(start,end)
 */
```

