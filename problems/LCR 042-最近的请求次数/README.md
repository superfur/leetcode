# LCR 042. 最近的请求次数

## 题目描述

<p>写一个&nbsp;<code>RecentCounter</code>&nbsp;类来计算特定时间范围内最近的请求。</p>

<p>请实现 <code>RecentCounter</code> 类：</p>

<ul>
	<li><code>RecentCounter()</code> 初始化计数器，请求数为 0 。</li>
	<li><code>int ping(int t)</code> 在时间 <code>t</code> 添加一个新请求，其中 <code>t</code> 表示以毫秒为单位的某个时间，并返回过去 <code>3000</code> 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 <code>[t-3000, t]</code> 内发生的请求数。</li>
</ul>

<p><strong>保证</strong> 每次对 <code>ping</code> 的调用都使用比之前更大的 <code>t</code> 值。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
inputs = [&quot;RecentCounter&quot;, &quot;ping&quot;, &quot;ping&quot;, &quot;ping&quot;, &quot;ping&quot;]
inputs = [[], [1], [100], [3001], [3002]]
<strong>输出：</strong>
[null, 1, 2, 3, 3]

<strong>解释：</strong>
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [<strong>1</strong>]，范围是 [-2999,1]，返回 1
recentCounter.ping(100);   // requests = [<strong>1</strong>, <strong>100</strong>]，范围是 [-2900,100]，返回 2
recentCounter.ping(3001);  // requests = [<strong>1</strong>, <strong>100</strong>, <strong>3001</strong>]，范围是 [1,3001]，返回 3
recentCounter.ping(3002);  // requests = [1, <strong>100</strong>, <strong>3001</strong>, <strong>3002</strong>]，范围是 [2,3002]，返回 3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= t &lt;= 10<sup>9</sup></code></li>
	<li>保证每次对 <code>ping</code> 调用所使用的 <code>t</code> 值都 <strong>严格递增</strong></li>
	<li>至多调用 <code>ping</code> 方法 <code>10<sup>4</sup></code> 次</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 933&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/number-of-recent-calls/">https://leetcode-cn.com/problems/number-of-recent-calls/</a></p>


## 难度

Easy

## 标签

- 设计
- 队列
- 数据流

## 示例

```
["RecentCounter","ping","ping","ping","ping"]
[[],[1],[100],[3001],[3002]]
```

## 示例代码

### C++

```cpp
class RecentCounter {
public:
    RecentCounter() {

    }
    
    int ping(int t) {

    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
```

### Java

```java
class RecentCounter {

    public RecentCounter() {

    }
    
    public int ping(int t) {

    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */
```

### Python

```python
class RecentCounter(object):

    def __init__(self):


    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```

### Python3

```python3
class RecentCounter:

    def __init__(self):


    def ping(self, t: int) -> int:



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```

### C

```c



typedef struct {

} RecentCounter;


RecentCounter* recentCounterCreate() {

}

int recentCounterPing(RecentCounter* obj, int t) {

}

void recentCounterFree(RecentCounter* obj) {

}

/**
 * Your RecentCounter struct will be instantiated and called as such:
 * RecentCounter* obj = recentCounterCreate();
 * int param_1 = recentCounterPing(obj, t);
 
 * recentCounterFree(obj);
*/
```

### C#

```csharp
public class RecentCounter {

    public RecentCounter() {

    }
    
    public int Ping(int t) {

    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.Ping(t);
 */
```

### JavaScript

```javascript

var RecentCounter = function() {

};

/** 
 * @param {number} t
 * @return {number}
 */
RecentCounter.prototype.ping = function(t) {

};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */
```

### TypeScript

```typescript
class RecentCounter {
    constructor() {

    }

    ping(t: number): number {

    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */
```

### PHP

```php
class RecentCounter {
    /**
     */
    function __construct() {

    }

    /**
     * @param Integer $t
     * @return Integer
     */
    function ping($t) {

    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * $obj = RecentCounter();
 * $ret_1 = $obj->ping($t);
 */
```

### Swift

```swift

class RecentCounter {

    init() {

    }
    
    func ping(_ t: Int) -> Int {

    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * let obj = RecentCounter()
 * let ret_1: Int = obj.ping(t)
 */
```

### Kotlin

```kotlin
class RecentCounter() {

    fun ping(t: Int): Int {

    }

}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = RecentCounter()
 * var param_1 = obj.ping(t)
 */
```

### Go

```golang
type RecentCounter struct {

}


func Constructor() RecentCounter {

}


func (this *RecentCounter) Ping(t int) int {

}


/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
```

### Ruby

```ruby
class RecentCounter
    def initialize()

    end


=begin
    :type t: Integer
    :rtype: Integer
=end
    def ping(t)

    end


end

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter.new()
# param_1 = obj.ping(t)
```

### Scala

```scala
class RecentCounter() {

    def ping(t: Int): Int = {

    }

}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */
```

### Rust

```rust
struct RecentCounter {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RecentCounter {

    fn new() -> Self {

    }
    
    fn ping(&self, t: i32) -> i32 {

    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * let obj = RecentCounter::new();
 * let ret_1: i32 = obj.ping(t);
 */
```

### Racket

```racket
(define recent-counter%
  (class object%
    (super-new)
    (init-field)
    
    ; ping : exact-integer? -> exact-integer?
    (define/public (ping t)

      )))

;; Your recent-counter% object will be instantiated and called as such:
;; (define obj (new recent-counter%))
;; (define param_1 (send obj ping t))
```

### Erlang

```erlang
-spec recent_counter_init_() -> any().
recent_counter_init_() ->
  .

-spec recent_counter_ping(T :: integer()) -> integer().
recent_counter_ping(T) ->
  .


%% Your functions will be called as such:
%% recent_counter_init_(),
%% Param_1 = recent_counter_ping(T),

%% recent_counter_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule RecentCounter do
  @spec init_() :: any
  def init_() do

  end

  @spec ping(t :: integer) :: integer
  def ping(t) do

  end
end

# Your functions will be called as such:
# RecentCounter.init_()
# param_1 = RecentCounter.ping(t)

# RecentCounter.init_ will be called before every test case, in which you can do some necessary initializations.
```

