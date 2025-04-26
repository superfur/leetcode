# 732. 我的日程安排表 III

## 题目描述

<p>当 <code>k</code> 个日程存在一些非空交集时（即, <code>k</code> 个日程包含了一些相同时间），就会产生 <code>k</code> 次预订。</p>

<p>给你一些日程安排 <code>[startTime, endTime)</code> ，请你在每个日程安排添加后，返回一个整数 <code>k</code> ，表示所有先前日程安排会产生的最大 <code>k</code> 次预订。</p>

<p>实现一个 <code>MyCalendarThree</code> 类来存放你的日程安排，你可以一直添加新的日程安排。</p>

<ul>
	<li><code>MyCalendarThree()</code> 初始化对象。</li>
	<li><code>int book(int startTime, int endTime)</code> 返回一个整数 <code>k</code> ，表示日历中存在的 <code>k</code> 次预订的最大值。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
<strong>输出：</strong>
[null, 1, 1, 2, 3, 3, 3]

<strong>解释：</strong>
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(50, 60); // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(10, 40); // 返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
myCalendarThree.book(5, 15); // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
myCalendarThree.book(5, 10); // 返回 3
myCalendarThree.book(25, 55); // 返回 3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= startTime &lt; endTime &lt;= 10<sup>9</sup></code></li>
	<li>每个测试用例，调用 <code>book</code>&nbsp;函数最多不超过&nbsp;<code>400</code>次</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 线段树
- 二分查找
- 有序集合
- 前缀和

## 提示

1. Treat each interval [start, end) as two events "start" and "end", and process them in sorted order.

## 示例

```
["MyCalendarThree","book","book","book","book","book","book"]
[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
```

## 示例代码

### C++

```cpp
class MyCalendarThree {
public:
    MyCalendarThree() {
        
    }
    
    int book(int startTime, int endTime) {
        
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(startTime,endTime);
 */
```

### Java

```java
class MyCalendarThree {

    public MyCalendarThree() {
        
    }
    
    public int book(int startTime, int endTime) {
        
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(startTime,endTime);
 */
```

### Python

```python
class MyCalendarThree(object):

    def __init__(self):
        

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
```

### Python3

```python3
class MyCalendarThree:

    def __init__(self):
        

    def book(self, startTime: int, endTime: int) -> int:
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
```

### C

```c



typedef struct {
    
} MyCalendarThree;


MyCalendarThree* myCalendarThreeCreate() {
    
}

int myCalendarThreeBook(MyCalendarThree* obj, int startTime, int endTime) {
    
}

void myCalendarThreeFree(MyCalendarThree* obj) {
    
}

/**
 * Your MyCalendarThree struct will be instantiated and called as such:
 * MyCalendarThree* obj = myCalendarThreeCreate();
 * int param_1 = myCalendarThreeBook(obj, startTime, endTime);
 
 * myCalendarThreeFree(obj);
*/
```

### C#

```csharp
public class MyCalendarThree {

    public MyCalendarThree() {
        
    }
    
    public int Book(int startTime, int endTime) {
        
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.Book(startTime,endTime);
 */
```

### JavaScript

```javascript

var MyCalendarThree = function() {
    
};

/** 
 * @param {number} startTime 
 * @param {number} endTime
 * @return {number}
 */
MyCalendarThree.prototype.book = function(startTime, endTime) {
    
};

/** 
 * Your MyCalendarThree object will be instantiated and called as such:
 * var obj = new MyCalendarThree()
 * var param_1 = obj.book(startTime,endTime)
 */
```

### TypeScript

```typescript
class MyCalendarThree {
    constructor() {
        
    }

    book(startTime: number, endTime: number): number {
        
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * var obj = new MyCalendarThree()
 * var param_1 = obj.book(startTime,endTime)
 */
```

### PHP

```php
class MyCalendarThree {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $startTime
     * @param Integer $endTime
     * @return Integer
     */
    function book($startTime, $endTime) {
        
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * $obj = MyCalendarThree();
 * $ret_1 = $obj->book($startTime, $endTime);
 */
```

### Swift

```swift

class MyCalendarThree {

    init() {
        
    }
    
    func book(_ startTime: Int, _ endTime: Int) -> Int {
        
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * let obj = MyCalendarThree()
 * let ret_1: Int = obj.book(startTime, endTime)
 */
```

### Kotlin

```kotlin
class MyCalendarThree() {

    fun book(startTime: Int, endTime: Int): Int {
        
    }

}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * var obj = MyCalendarThree()
 * var param_1 = obj.book(startTime,endTime)
 */
```

### Dart

```dart
class MyCalendarThree {

  MyCalendarThree() {
    
  }
  
  int book(int startTime, int endTime) {
    
  }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = MyCalendarThree();
 * int param1 = obj.book(startTime,endTime);
 */
```

### Go

```golang
type MyCalendarThree struct {
    
}


func Constructor() MyCalendarThree {
    
}


func (this *MyCalendarThree) Book(startTime int, endTime int) int {
    
}


/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(startTime,endTime);
 */
```

### Ruby

```ruby
class MyCalendarThree
    def initialize()
        
    end


=begin
    :type start_time: Integer
    :type end_time: Integer
    :rtype: Integer
=end
    def book(start_time, end_time)
        
    end


end

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree.new()
# param_1 = obj.book(start_time, end_time)
```

### Scala

```scala
class MyCalendarThree() {

    def book(startTime: Int, endTime: Int): Int = {
        
    }

}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * val obj = new MyCalendarThree()
 * val param_1 = obj.book(startTime,endTime)
 */
```

### Rust

```rust
struct MyCalendarThree {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCalendarThree {

    fn new() -> Self {
        
    }
    
    fn book(&self, start_time: i32, end_time: i32) -> i32 {
        
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * let obj = MyCalendarThree::new();
 * let ret_1: i32 = obj.book(startTime, endTime);
 */
```

### Racket

```racket
(define my-calendar-three%
  (class object%
    (super-new)
    
    (init-field)
    
    ; book : exact-integer? exact-integer? -> exact-integer?
    (define/public (book start-time end-time)
      )))

;; Your my-calendar-three% object will be instantiated and called as such:
;; (define obj (new my-calendar-three%))
;; (define param_1 (send obj book start-time end-time))
```

### Erlang

```erlang
-spec my_calendar_three_init_() -> any().
my_calendar_three_init_() ->
  .

-spec my_calendar_three_book(StartTime :: integer(), EndTime :: integer()) -> integer().
my_calendar_three_book(StartTime, EndTime) ->
  .


%% Your functions will be called as such:
%% my_calendar_three_init_(),
%% Param_1 = my_calendar_three_book(StartTime, EndTime),

%% my_calendar_three_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MyCalendarThree do
  @spec init_() :: any
  def init_() do
    
  end

  @spec book(start_time :: integer, end_time :: integer) :: integer
  def book(start_time, end_time) do
    
  end
end

# Your functions will be called as such:
# MyCalendarThree.init_()
# param_1 = MyCalendarThree.book(start_time, end_time)

# MyCalendarThree.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MyCalendarThree {
    init() {

    }
    
    func book(startTime: Int64, endTime: Int64): Int64 {

    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * let obj: MyCalendarThree = MyCalendarThree()
 * let param_1 = obj.book(startTime,endTime)
 */
```

