# LCR 058. 我的日程安排表 I

## 题目描述

<p>请实现一个 <code>MyCalendar</code> 类来存放你的日程安排。如果要添加的时间内没有其他安排，则可以存储这个新的日程安排。</p>

<p><code>MyCalendar</code> 有一个 <code>book(int start, int end)</code>方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，即 <code>[start, end)</code>, 实数&nbsp;<code>x</code> 的范围为， &nbsp;<code>start &lt;= x &lt; end</code>。</p>

<p>当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生重复预订。</p>

<p>每次调用 <code>MyCalendar.book</code>方法时，如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 <code>true</code>。否则，返回 <code>false</code>&nbsp;并且不要将该日程安排添加到日历中。</p>

<p>请按照以下步骤调用 <code>MyCalendar</code> 类: <code>MyCalendar cal = new MyCalendar();</code> <code>MyCalendar.book(start, end)</code></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:
</strong>[&quot;MyCalendar&quot;,&quot;book&quot;,&quot;book&quot;,&quot;book&quot;]
[[],[10,20],[15,25],[20,30]]
<strong>输出:</strong> [null,true,false,true]
<strong>解释:</strong> 
MyCalendar myCalendar = new MyCalendar();
MyCalendar.book(10, 20); // returns true 
MyCalendar.book(15, 25); // returns false ，第二个日程安排不能添加到日历中，因为时间 15 已经被第一个日程安排预定了
MyCalendar.book(20, 30); // returns true ，第三个日程安排可以添加到日历中，因为第一个日程安排并不包含时间 20 
</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>每个测试用例，调用&nbsp;<code>MyCalendar.book</code>&nbsp;函数最多不超过&nbsp;<code>1000</code>次。</li>
	<li><code>0 &lt;= start &lt; end &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 729&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/my-calendar-i/">https://leetcode-cn.com/problems/my-calendar-i/</a></p>


## 难度

Medium

## 标签

- 设计
- 线段树
- 二分查找
- 有序集合

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
    
    bool book(int start, int end) {

    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
```

### Java

```java
class MyCalendar {

    public MyCalendar() {

    }
    
    public boolean book(int start, int end) {

    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */
```

### Python

```python
class MyCalendar(object):

    def __init__(self):


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
```

### Python3

```python3
class MyCalendar:

    def __init__(self):


    def book(self, start: int, end: int) -> bool:



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
```

### C

```c



typedef struct {

} MyCalendar;


MyCalendar* myCalendarCreate() {

}

bool myCalendarBook(MyCalendar* obj, int start, int end) {

}

void myCalendarFree(MyCalendar* obj) {

}

/**
 * Your MyCalendar struct will be instantiated and called as such:
 * MyCalendar* obj = myCalendarCreate();
 * bool param_1 = myCalendarBook(obj, start, end);
 
 * myCalendarFree(obj);
*/
```

### C#

```csharp
public class MyCalendar {

    public MyCalendar() {

    }
    
    public bool Book(int start, int end) {

    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * bool param_1 = obj.Book(start,end);
 */
```

### JavaScript

```javascript

var MyCalendar = function() {

};

/** 
 * @param {number} start 
 * @param {number} end
 * @return {boolean}
 */
MyCalendar.prototype.book = function(start, end) {

};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
 */
```

### TypeScript

```typescript
class MyCalendar {
    constructor() {

    }

    book(start: number, end: number): boolean {

    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
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
     * @param Integer $start
     * @param Integer $end
     * @return Boolean
     */
    function book($start, $end) {

    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * $obj = MyCalendar();
 * $ret_1 = $obj->book($start, $end);
 */
```

### Swift

```swift

class MyCalendar {

    init() {

    }
    
    func book(_ start: Int, _ end: Int) -> Bool {

    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * let obj = MyCalendar()
 * let ret_1: Bool = obj.book(start, end)
 */
```

### Kotlin

```kotlin
class MyCalendar() {

    fun book(start: Int, end: Int): Boolean {

    }

}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = MyCalendar()
 * var param_1 = obj.book(start,end)
 */
```

### Go

```golang
type MyCalendar struct {

}


func Constructor() MyCalendar {

}


func (this *MyCalendar) Book(start int, end int) bool {

}


/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
```

### Ruby

```ruby
class MyCalendar
    def initialize()

    end


=begin
    :type start: Integer
    :type end: Integer
    :rtype: Boolean
=end
    def book(start, end)

    end


end

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar.new()
# param_1 = obj.book(start, end)
```

### Scala

```scala
class MyCalendar() {

    def book(start: Int, end: Int): Boolean = {

    }

}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * var obj = new MyCalendar()
 * var param_1 = obj.book(start,end)
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
    
    fn book(&self, start: i32, end: i32) -> bool {

    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * let obj = MyCalendar::new();
 * let ret_1: bool = obj.book(start, end);
 */
```

### Racket

```racket
(define my-calendar%
  (class object%
    (super-new)
    (init-field)
    
    ; book : exact-integer? exact-integer? -> boolean?
    (define/public (book start end)

      )))

;; Your my-calendar% object will be instantiated and called as such:
;; (define obj (new my-calendar%))
;; (define param_1 (send obj book start end))
```

### Erlang

```erlang
-spec my_calendar_init_() -> any().
my_calendar_init_() ->
  .

-spec my_calendar_book(Start :: integer(), End :: integer()) -> boolean().
my_calendar_book(Start, End) ->
  .


%% Your functions will be called as such:
%% my_calendar_init_(),
%% Param_1 = my_calendar_book(Start, End),

%% my_calendar_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MyCalendar do
  @spec init_() :: any
  def init_() do

  end

  @spec book(start :: integer, end :: integer) :: boolean
  def book(start, end) do

  end
end

# Your functions will be called as such:
# MyCalendar.init_()
# param_1 = MyCalendar.book(start, end)

# MyCalendar.init_ will be called before every test case, in which you can do some necessary initializations.
```

