# 3508. 设计路由器

## 题目描述

<p>请你设计一个数据结构来高效管理网络路由器中的数据包。每个数据包包含以下属性：</p>

<ul>
	<li><code>source</code>：生成该数据包的机器的唯一标识符。</li>
	<li><code>destination</code>：目标机器的唯一标识符。</li>
	<li><code>timestamp</code>：该数据包到达路由器的时间戳。</li>
</ul>

<p>实现 <code>Router</code> 类：</p>

<p><code>Router(int memoryLimit)</code>：初始化路由器对象，并设置固定的内存限制。</p>

<ul>
	<li><code>memoryLimit</code> 是路由器在任意时间点可以存储的 <strong>最大</strong> 数据包数量。</li>
	<li>如果添加一个新数据包会超过这个限制，则必须移除 <strong>最旧的</strong> 数据包以腾出空间。</li>
</ul>

<p><code>bool addPacket(int source, int destination, int timestamp)</code>：将具有给定属性的数据包添加到路由器。</p>

<ul>
	<li>如果路由器中已经存在一个具有相同 <code>source</code>、<code>destination</code> 和 <code>timestamp</code> 的数据包，则视为重复数据包。</li>
	<li>如果数据包成功添加（即不是重复数据包），返回 <code>true</code>；否则返回 <code>false</code>。</li>
</ul>

<p><code>int[] forwardPacket()</code>：以 FIFO（先进先出）顺序转发下一个数据包。</p>

<ul>
	<li>从存储中移除该数据包。</li>
	<li>以数组 <code>[source, destination, timestamp]</code> 的形式返回该数据包。</li>
	<li>如果没有数据包可以转发，则返回空数组。</li>
</ul>

<p><code>int getCount(int destination, int startTime, int endTime)</code>：</p>

<ul>
	<li>返回当前存储在路由器中（即尚未转发）的，且目标地址为指定 <code>destination</code> 且时间戳在范围 <code>[startTime, endTime]</code>（包括两端）内的数据包数量。</li>
</ul>

<p><strong>注意</strong>：对于 <code>addPacket</code> 的查询会按照 <code>timestamp</code> 的递增顺序进行。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><br />
<span class="example-io">["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]<br />
[[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]</span></p>

<p><strong>输出：</strong><br />
<span class="example-io">[null, true, true, false, true, true, [2, 5, 90], true, 1] </span></p>

<p><strong>解释：</strong></p>
<code>Router router = new Router(3);</code> // 初始化路由器，内存限制为 3。<br />
<code>router.addPacket(1, 4, 90);</code> // 数据包被添加，返回 True。<br />
<code>router.addPacket(2, 5, 90);</code> // 数据包被添加，返回 True。<br />
<code>router.addPacket(1, 4, 90);</code> // 这是一个重复数据包，返回 False。<br />
<code>router.addPacket(3, 5, 95);</code> // 数据包被添加，返回 True。<br />
<code>router.addPacket(4, 5, 105);</code> // 数据包被添加，<code>[1, 4, 90]</code> 被移除，因为数据包数量超过限制，返回 True。<br />
<code>router.forwardPacket();</code> // 转发数据包 <code>[2, 5, 90]</code> 并将其从路由器中移除。<br />
<code>router.addPacket(5, 2, 110);</code> // 数据包被添加，返回 True。<br />
<code>router.getCount(5, 100, 110);</code> // 唯一目标地址为 5 且时间在 <code>[100, 110]</code>&nbsp;范围内的数据包是 <code>[4, 5, 105]</code>，返回 1。</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><br />
<span class="example-io">["Router", "addPacket", "forwardPacket", "forwardPacket"]<br />
[[2], [7, 4, 90], [], []]</span></p>

<p><strong>输出：</strong><br />
<span class="example-io">[null, true, [7, 4, 90], []] </span></p>

<p><strong>解释：</strong></p>
<code>Router router = new Router(2);</code> // 初始化路由器，内存限制为 2。<br />
<code>router.addPacket(7, 4, 90);</code> // 返回 True。<br />
<code>router.forwardPacket();</code> // 返回 <code>[7, 4, 90]</code>。<br />
<code>router.forwardPacket();</code> // 没有数据包可以转发，返回 <code>[]</code>。</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= memoryLimit &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= source, destination &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= timestamp &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= startTime &lt;= endTime &lt;= 10<sup>9</sup></code></li>
	<li><code>addPacket</code>、<code>forwardPacket</code> 和 <code>getCount</code> 方法的总调用次数最多为 <code>10<sup>5</sup></code>。</li>
	<li>对于 <code>addPacket</code> 的查询，<code>timestamp</code> 按递增顺序给出。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 队列
- 数组
- 哈希表
- 二分查找
- 有序集合

## 提示

1. A deque can simulate the adding and forwarding of packets efficiently.
2. Use binary search for counting packets within a timestamp range.

## 示例

```
["Router","addPacket","addPacket","addPacket","addPacket","addPacket","forwardPacket","addPacket","getCount"]
[[3],[1,4,90],[2,5,90],[1,4,90],[3,5,95],[4,5,105],[],[5,2,110],[5,100,110]]
["Router","addPacket","forwardPacket","forwardPacket"]
[[2],[7,4,90],[],[]]
```

## 示例代码

### C++

```cpp
class Router {
public:
    Router(int memoryLimit) {
        
    }
    
    bool addPacket(int source, int destination, int timestamp) {
        
    }
    
    vector<int> forwardPacket() {
        
    }
    
    int getCount(int destination, int startTime, int endTime) {
        
    }
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */
```

### Java

```java
class Router {

    public Router(int memoryLimit) {
        
    }
    
    public boolean addPacket(int source, int destination, int timestamp) {
        
    }
    
    public int[] forwardPacket() {
        
    }
    
    public int getCount(int destination, int startTime, int endTime) {
        
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * Router obj = new Router(memoryLimit);
 * boolean param_1 = obj.addPacket(source,destination,timestamp);
 * int[] param_2 = obj.forwardPacket();
 * int param_3 = obj.getCount(destination,startTime,endTime);
 */
```

### Python

```python
class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
```

### Python3

```python3
class Router:

    def __init__(self, memoryLimit: int):
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        

    def forwardPacket(self) -> List[int]:
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
```

### C

```c



typedef struct {
    
} Router;


Router* routerCreate(int memoryLimit) {
    
}

bool routerAddPacket(Router* obj, int source, int destination, int timestamp) {
    
}

int* routerForwardPacket(Router* obj, int* retSize) {
    
}

int routerGetCount(Router* obj, int destination, int startTime, int endTime) {
    
}

void routerFree(Router* obj) {
    
}

/**
 * Your Router struct will be instantiated and called as such:
 * Router* obj = routerCreate(memoryLimit);
 * bool param_1 = routerAddPacket(obj, source, destination, timestamp);
 
 * int* param_2 = routerForwardPacket(obj, retSize);
 
 * int param_3 = routerGetCount(obj, destination, startTime, endTime);
 
 * routerFree(obj);
*/
```

### C#

```csharp
public class Router {

    public Router(int memoryLimit) {
        
    }
    
    public bool AddPacket(int source, int destination, int timestamp) {
        
    }
    
    public int[] ForwardPacket() {
        
    }
    
    public int GetCount(int destination, int startTime, int endTime) {
        
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * Router obj = new Router(memoryLimit);
 * bool param_1 = obj.AddPacket(source,destination,timestamp);
 * int[] param_2 = obj.ForwardPacket();
 * int param_3 = obj.GetCount(destination,startTime,endTime);
 */
```

### JavaScript

```javascript
/**
 * @param {number} memoryLimit
 */
var Router = function(memoryLimit) {
    
};

/** 
 * @param {number} source 
 * @param {number} destination 
 * @param {number} timestamp
 * @return {boolean}
 */
Router.prototype.addPacket = function(source, destination, timestamp) {
    
};

/**
 * @return {number[]}
 */
Router.prototype.forwardPacket = function() {
    
};

/** 
 * @param {number} destination 
 * @param {number} startTime 
 * @param {number} endTime
 * @return {number}
 */
Router.prototype.getCount = function(destination, startTime, endTime) {
    
};

/** 
 * Your Router object will be instantiated and called as such:
 * var obj = new Router(memoryLimit)
 * var param_1 = obj.addPacket(source,destination,timestamp)
 * var param_2 = obj.forwardPacket()
 * var param_3 = obj.getCount(destination,startTime,endTime)
 */
```

### TypeScript

```typescript
class Router {
    constructor(memoryLimit: number) {
        
    }

    addPacket(source: number, destination: number, timestamp: number): boolean {
        
    }

    forwardPacket(): number[] {
        
    }

    getCount(destination: number, startTime: number, endTime: number): number {
        
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * var obj = new Router(memoryLimit)
 * var param_1 = obj.addPacket(source,destination,timestamp)
 * var param_2 = obj.forwardPacket()
 * var param_3 = obj.getCount(destination,startTime,endTime)
 */
```

### PHP

```php
class Router {
    /**
     * @param Integer $memoryLimit
     */
    function __construct($memoryLimit) {
        
    }
  
    /**
     * @param Integer $source
     * @param Integer $destination
     * @param Integer $timestamp
     * @return Boolean
     */
    function addPacket($source, $destination, $timestamp) {
        
    }
  
    /**
     * @return Integer[]
     */
    function forwardPacket() {
        
    }
  
    /**
     * @param Integer $destination
     * @param Integer $startTime
     * @param Integer $endTime
     * @return Integer
     */
    function getCount($destination, $startTime, $endTime) {
        
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * $obj = Router($memoryLimit);
 * $ret_1 = $obj->addPacket($source, $destination, $timestamp);
 * $ret_2 = $obj->forwardPacket();
 * $ret_3 = $obj->getCount($destination, $startTime, $endTime);
 */
```

### Swift

```swift

class Router {

    init(_ memoryLimit: Int) {
        
    }
    
    func addPacket(_ source: Int, _ destination: Int, _ timestamp: Int) -> Bool {
        
    }
    
    func forwardPacket() -> [Int] {
        
    }
    
    func getCount(_ destination: Int, _ startTime: Int, _ endTime: Int) -> Int {
        
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * let obj = Router(memoryLimit)
 * let ret_1: Bool = obj.addPacket(source, destination, timestamp)
 * let ret_2: [Int] = obj.forwardPacket()
 * let ret_3: Int = obj.getCount(destination, startTime, endTime)
 */
```

### Kotlin

```kotlin
class Router(memoryLimit: Int) {

    fun addPacket(source: Int, destination: Int, timestamp: Int): Boolean {
        
    }

    fun forwardPacket(): IntArray {
        
    }

    fun getCount(destination: Int, startTime: Int, endTime: Int): Int {
        
    }

}

/**
 * Your Router object will be instantiated and called as such:
 * var obj = Router(memoryLimit)
 * var param_1 = obj.addPacket(source,destination,timestamp)
 * var param_2 = obj.forwardPacket()
 * var param_3 = obj.getCount(destination,startTime,endTime)
 */
```

### Dart

```dart
class Router {

  Router(int memoryLimit) {
    
  }
  
  bool addPacket(int source, int destination, int timestamp) {
    
  }
  
  List<int> forwardPacket() {
    
  }
  
  int getCount(int destination, int startTime, int endTime) {
    
  }
}

/**
 * Your Router object will be instantiated and called as such:
 * Router obj = Router(memoryLimit);
 * bool param1 = obj.addPacket(source,destination,timestamp);
 * List<int> param2 = obj.forwardPacket();
 * int param3 = obj.getCount(destination,startTime,endTime);
 */
```

### Go

```golang
type Router struct {
    
}


func Constructor(memoryLimit int) Router {
    
}


func (this *Router) AddPacket(source int, destination int, timestamp int) bool {
    
}


func (this *Router) ForwardPacket() []int {
    
}


func (this *Router) GetCount(destination int, startTime int, endTime int) int {
    
}


/**
 * Your Router object will be instantiated and called as such:
 * obj := Constructor(memoryLimit);
 * param_1 := obj.AddPacket(source,destination,timestamp);
 * param_2 := obj.ForwardPacket();
 * param_3 := obj.GetCount(destination,startTime,endTime);
 */
```

### Ruby

```ruby
class Router

=begin
    :type memory_limit: Integer
=end
    def initialize(memory_limit)
        
    end


=begin
    :type source: Integer
    :type destination: Integer
    :type timestamp: Integer
    :rtype: Boolean
=end
    def add_packet(source, destination, timestamp)
        
    end


=begin
    :rtype: Integer[]
=end
    def forward_packet()
        
    end


=begin
    :type destination: Integer
    :type start_time: Integer
    :type end_time: Integer
    :rtype: Integer
=end
    def get_count(destination, start_time, end_time)
        
    end


end

# Your Router object will be instantiated and called as such:
# obj = Router.new(memory_limit)
# param_1 = obj.add_packet(source, destination, timestamp)
# param_2 = obj.forward_packet()
# param_3 = obj.get_count(destination, start_time, end_time)
```

### Scala

```scala
class Router(_memoryLimit: Int) {

    def addPacket(source: Int, destination: Int, timestamp: Int): Boolean = {
        
    }

    def forwardPacket(): Array[Int] = {
        
    }

    def getCount(destination: Int, startTime: Int, endTime: Int): Int = {
        
    }

}

/**
 * Your Router object will be instantiated and called as such:
 * val obj = new Router(memoryLimit)
 * val param_1 = obj.addPacket(source,destination,timestamp)
 * val param_2 = obj.forwardPacket()
 * val param_3 = obj.getCount(destination,startTime,endTime)
 */
```

### Rust

```rust
struct Router {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Router {

    fn new(memoryLimit: i32) -> Self {
        
    }
    
    fn add_packet(&self, source: i32, destination: i32, timestamp: i32) -> bool {
        
    }
    
    fn forward_packet(&self) -> Vec<i32> {
        
    }
    
    fn get_count(&self, destination: i32, start_time: i32, end_time: i32) -> i32 {
        
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * let obj = Router::new(memoryLimit);
 * let ret_1: bool = obj.add_packet(source, destination, timestamp);
 * let ret_2: Vec<i32> = obj.forward_packet();
 * let ret_3: i32 = obj.get_count(destination, startTime, endTime);
 */
```

### Racket

```racket
(define router%
  (class object%
    (super-new)
    
    ; memory-limit : exact-integer?
    (init-field
      memory-limit)
    
    ; add-packet : exact-integer? exact-integer? exact-integer? -> boolean?
    (define/public (add-packet source destination timestamp)
      )
    ; forward-packet : -> (listof exact-integer?)
    (define/public (forward-packet)
      )
    ; get-count : exact-integer? exact-integer? exact-integer? -> exact-integer?
    (define/public (get-count destination start-time end-time)
      )))

;; Your router% object will be instantiated and called as such:
;; (define obj (new router% [memory-limit memory-limit]))
;; (define param_1 (send obj add-packet source destination timestamp))
;; (define param_2 (send obj forward-packet))
;; (define param_3 (send obj get-count destination start-time end-time))
```

### Erlang

```erlang
-spec router_init_(MemoryLimit :: integer()) -> any().
router_init_(MemoryLimit) ->
  .

-spec router_add_packet(Source :: integer(), Destination :: integer(), Timestamp :: integer()) -> boolean().
router_add_packet(Source, Destination, Timestamp) ->
  .

-spec router_forward_packet() -> [integer()].
router_forward_packet() ->
  .

-spec router_get_count(Destination :: integer(), StartTime :: integer(), EndTime :: integer()) -> integer().
router_get_count(Destination, StartTime, EndTime) ->
  .


%% Your functions will be called as such:
%% router_init_(MemoryLimit),
%% Param_1 = router_add_packet(Source, Destination, Timestamp),
%% Param_2 = router_forward_packet(),
%% Param_3 = router_get_count(Destination, StartTime, EndTime),

%% router_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Router do
  @spec init_(memory_limit :: integer) :: any
  def init_(memory_limit) do
    
  end

  @spec add_packet(source :: integer, destination :: integer, timestamp :: integer) :: boolean
  def add_packet(source, destination, timestamp) do
    
  end

  @spec forward_packet() :: [integer]
  def forward_packet() do
    
  end

  @spec get_count(destination :: integer, start_time :: integer, end_time :: integer) :: integer
  def get_count(destination, start_time, end_time) do
    
  end
end

# Your functions will be called as such:
# Router.init_(memory_limit)
# param_1 = Router.add_packet(source, destination, timestamp)
# param_2 = Router.forward_packet()
# param_3 = Router.get_count(destination, start_time, end_time)

# Router.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Router {
    init(memoryLimit: Int64) {

    }
    
    func addPacket(source: Int64, destination: Int64, timestamp: Int64): Bool {

    }
    
    func forwardPacket(): Array<Int64> {

    }
    
    func getCount(destination: Int64, startTime: Int64, endTime: Int64): Int64 {

    }
}

/**
 * Your Router object will be instantiated and called as such:
 * let obj: Router = Router(memoryLimit)
 * let param_1 = obj.addPacket(source,destination,timestamp)
 * let param_2 = obj.forwardPacket()
 * let param_3 = obj.getCount(destination,startTime,endTime)
 */
```

