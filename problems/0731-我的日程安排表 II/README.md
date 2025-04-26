# 731. 我的日程安排表 II

## 题目描述

<p>实现一个程序来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。</p>

<p>当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生 <strong>三重预订</strong>。</p>

<p>事件能够用一对整数&nbsp;<code>startTime</code>&nbsp;和&nbsp;<code>endTime</code>&nbsp;表示，在一个半开区间的时间&nbsp;<code>[startTime, endTime)</code>&nbsp;上预定。实数&nbsp;<code>x</code> 的范围为&nbsp;&nbsp;<code>startTime &lt;= x &lt; endTime</code>。</p>

<p>实现&nbsp;<code>MyCalendarTwo</code> 类：</p>

<ul>
	<li><code>MyCalendarTwo()</code>&nbsp;初始化日历对象。</li>
	<li><code>boolean book(int startTime, int endTime)</code>&nbsp;如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 <code>true</code>。否则，返回 <code>false</code> 并且不要将该日程安排添加到日历中。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
<strong>输出：</strong>
[null, true, true, true, false, true, true]

<strong>解释：</strong>
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // 返回 True，能够预定该日程。
myCalendarTwo.book(50, 60); // 返回 True，能够预定该日程。
myCalendarTwo.book(10, 40); // 返回 True，该日程能够被重复预定。
myCalendarTwo.book(5, 15);  // 返回 False，该日程导致了三重预定，所以不能预定。
myCalendarTwo.book(5, 10); // 返回 True，能够预定该日程，因为它不使用已经双重预订的时间 10。
myCalendarTwo.book(25, 55); // 返回 True，能够预定该日程，因为时间段 [25, 40) 将被第三个日程重复预定，时间段 [40, 50) 将被单独预定，而时间段 [50, 55) 将被第二个日程重复预定。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= start &lt; end &lt;= 10<sup>9</sup></code></li>
	<li>最多调用&nbsp;<code>book</code>&nbsp;1000 次。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 线段树
- 数组
- 二分查找
- 有序集合
- 前缀和

## 提示

1. Store two sorted lists of intervals: one list will be all times that are at least single booked, and another list will be all times that are definitely double booked.  If none of the double bookings conflict, then the booking will succeed, and you should update your single and double bookings accordingly.

## 示例

```
["MyCalendarTwo","book","book","book","book","book","book"]
[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
```

## 示例代码

### C++

```cpp
class MyCalendarTwo {
public:
    MyCalendarTwo() {
        
    }
    
    bool book(int startTime, int endTime) {
        
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(startTime,endTime);
 */
```

### Java

```java
class MyCalendarTwo {

    public MyCalendarTwo() {
        
    }
    
    public boolean book(int startTime, int endTime) {
        
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(startTime,endTime);
 */
```

### Python

```python
class MyCalendarTwo(object):

    def __init__(self):
        

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
```

### Python3

```python3
class MyCalendarTwo:

    def __init__(self):
        

    def book(self, startTime: int, endTime: int) -> bool:
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
```

### C

```c



typedef struct {
    
} MyCalendarTwo;


MyCalendarTwo* myCalendarTwoCreate() {
    
}

bool myCalendarTwoBook(MyCalendarTwo* obj, int startTime, int endTime) {
    
}

void myCalendarTwoFree(MyCalendarTwo* obj) {
    
}

/**
 * Your MyCalendarTwo struct will be instantiated and called as such:
 * MyCalendarTwo* obj = myCalendarTwoCreate();
 * bool param_1 = myCalendarTwoBook(obj, startTime, endTime);
 
 * myCalendarTwoFree(obj);
*/
```

### C#

```csharp
public class MyCalendarTwo {

    public MyCalendarTwo() {
        
    }
    
    public bool Book(int startTime, int endTime) {
        
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * bool param_1 = obj.Book(startTime,endTime);
 */
```

### JavaScript

```javascript

var MyCalendarTwo = function() {
    
};

/** 
 * @param {number} startTime 
 * @param {number} endTime
 * @return {boolean}
 */
MyCalendarTwo.prototype.book = function(startTime, endTime) {
    
};

/** 
 * Your MyCalendarTwo object will be instantiated and called as such:
 * var obj = new MyCalendarTwo()
 * var param_1 = obj.book(startTime,endTime)
 */
```

### TypeScript

```typescript
class MyCalendarTwo {
    constructor() {
        
    }

    book(startTime: number, endTime: number): boolean {
        
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * var obj = new MyCalendarTwo()
 * var param_1 = obj.book(startTime,endTime)
 */
```

### PHP

```php
class MyCalendarTwo {
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
 * Your MyCalendarTwo object will be instantiated and called as such:
 * $obj = MyCalendarTwo();
 * $ret_1 = $obj->book($startTime, $endTime);
 */
```

### Swift

```swift

class MyCalendarTwo {

    init() {
        
    }
    
    func book(_ startTime: Int, _ endTime: Int) -> Bool {
        
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * let obj = MyCalendarTwo()
 * let ret_1: Bool = obj.book(startTime, endTime)
 */
```

### Kotlin

```kotlin
class MyCalendarTwo() {

    fun book(startTime: Int, endTime: Int): Boolean {
        
    }

}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * var obj = MyCalendarTwo()
 * var param_1 = obj.book(startTime,endTime)
 */
```

### Dart

```dart
class MyCalendarTwo {

  MyCalendarTwo() {
    
  }
  
  bool book(int startTime, int endTime) {
    
  }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = MyCalendarTwo();
 * bool param1 = obj.book(startTime,endTime);
 */
```

### Go

```golang
type MyCalendarTwo struct {
    
}


func Constructor() MyCalendarTwo {
    
}


func (this *MyCalendarTwo) Book(startTime int, endTime int) bool {
    
}


/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(startTime,endTime);
 */
```

### Ruby

```ruby
class MyCalendarTwo
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

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo.new()
# param_1 = obj.book(start_time, end_time)
```

### Scala

```scala
class MyCalendarTwo() {

    def book(startTime: Int, endTime: Int): Boolean = {
        
    }

}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * val obj = new MyCalendarTwo()
 * val param_1 = obj.book(startTime,endTime)
 */
```

### Rust

```rust
struct MyCalendarTwo {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCalendarTwo {

    fn new() -> Self {
        
    }
    
    fn book(&self, start_time: i32, end_time: i32) -> bool {
        
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * let obj = MyCalendarTwo::new();
 * let ret_1: bool = obj.book(startTime, endTime);
 */
```

### Racket

```racket
(define my-calendar-two%
  (class object%
    (super-new)
    
    (init-field)
    
    ; book : exact-integer? exact-integer? -> boolean?
    (define/public (book start-time end-time)
      )))

;; Your my-calendar-two% object will be instantiated and called as such:
;; (define obj (new my-calendar-two%))
;; (define param_1 (send obj book start-time end-time))
```

### Erlang

```erlang
-spec my_calendar_two_init_() -> any().
my_calendar_two_init_() ->
  .

-spec my_calendar_two_book(StartTime :: integer(), EndTime :: integer()) -> boolean().
my_calendar_two_book(StartTime, EndTime) ->
  .


%% Your functions will be called as such:
%% my_calendar_two_init_(),
%% Param_1 = my_calendar_two_book(StartTime, EndTime),

%% my_calendar_two_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MyCalendarTwo do
  @spec init_() :: any
  def init_() do
    
  end

  @spec book(start_time :: integer, end_time :: integer) :: boolean
  def book(start_time, end_time) do
    
  end
end

# Your functions will be called as such:
# MyCalendarTwo.init_()
# param_1 = MyCalendarTwo.book(start_time, end_time)

# MyCalendarTwo.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MyCalendarTwo {
    init() {

    }
    
    func book(start: Int64, end: Int64): Bool {

    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * let obj: MyCalendarTwo = MyCalendarTwo()
 * let param_1 = obj.book(start,end)
 */
```

