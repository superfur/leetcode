# 2102. 序列顺序查询

## 题目描述

<p>一个观光景点由它的名字&nbsp;<code>name</code> 和景点评分&nbsp;<code>score</code>&nbsp;组成，其中&nbsp;<code>name</code>&nbsp;是所有观光景点中&nbsp;<strong>唯一</strong>&nbsp;的字符串，<code>score</code>&nbsp;是一个整数。景点按照最好到最坏排序。景点评分 <strong>越高</strong>&nbsp;，这个景点越好。如果有两个景点的评分一样，那么 <strong>字典序较小</strong>&nbsp;的景点更好。</p>

<p>你需要搭建一个系统，查询景点的排名。初始时系统里没有任何景点。这个系统支持：</p>

<ul>
	<li><strong>添加</strong> 景点，每次添加 <strong>一个</strong> 景点。</li>
	<li><strong>查询 </strong>已经添加景点中第&nbsp;<code>i</code>&nbsp;<strong>好</strong>&nbsp;的景点，其中&nbsp;<code>i</code>&nbsp;是系统目前位置查询的次数（包括当前这一次）。
	<ul>
		<li>比方说，如果系统正在进行第 <code>4</code>&nbsp;次查询，那么需要返回所有已经添加景点中第 <code>4</code>&nbsp;好的。</li>
	</ul>
	</li>
</ul>

<p>注意，测试数据保证&nbsp;<strong>任意查询时刻</strong>&nbsp;，查询次数都 <strong>不超过</strong>&nbsp;系统中景点的数目。</p>

<p>请你实现&nbsp;<code>SORTracker</code>&nbsp;类：</p>

<ul>
	<li><code>SORTracker()</code>&nbsp;初始化系统。</li>
	<li><code>void add(string name, int score)</code>&nbsp;向系统中添加一个名为&nbsp;<code>name</code> 评分为&nbsp;<code>score</code>&nbsp;的景点。</li>
	<li><code>string get()</code>&nbsp;查询第 <code>i</code>&nbsp;好的景点，其中 <code>i</code>&nbsp;是目前系统查询的次数（包括当前这次查询）。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]
<strong>输出：</strong>
[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

<strong>解释：</strong>
SORTracker tracker = new SORTracker(); // 初始化系统
tracker.add("bradford", 2); // 添加 name="bradford" 且 score=2 的景点。
tracker.add("branford", 3); // 添加 name="branford" 且 score=3 的景点。
tracker.get();              // 从好到坏的景点为：branford ，bradford 。
                            // 注意到 branford 比 bradford 好，因为它的 <strong>评分更高</strong> (3 &gt; 2) 。
                            // 这是第 1 次调用 get() ，所以返回最好的景点："branford" 。
tracker.add("alps", 2);     // 添加 name="alps" 且 score=2 的景点。
tracker.get();              // 从好到坏的景点为：branford, alps, bradford 。
                            // 注意 alps 比 bradford 好，虽然它们评分相同，都为 2 。
                            // 这是因为 "alps" <strong>字典序</strong>&nbsp;比 "bradford" 小。
                            // 返回第 2 好的地点 "alps" ，因为当前为第 2 次调用 get() 。
tracker.add("orland", 2);   // 添加 name="orland" 且 score=2 的景点。
tracker.get();              // 从好到坏的景点为：branford, alps, bradford, orland 。
                            // 返回 "bradford" ，因为当前为第 3 次调用 get() 。
tracker.add("orlando", 3);  // 添加 name="orlando" 且 score=3 的景点。
tracker.get();              // 从好到坏的景点为：branford, orlando, alps, bradford, orland 。
                            // 返回 "bradford".
tracker.add("alpine", 2);   // 添加 name="alpine" 且 score=2 的景点。
tracker.get();              // 从好到坏的景点为：branford, orlando, alpine, alps, bradford, orland 。
                            // 返回 "bradford" 。
tracker.get();              // 从好到坏的景点为：branford, orlando, alpine, alps, bradford, orland 。
                            // 返回 "orland" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>name</code>&nbsp;只包含小写英文字母，且每个景点名字互不相同。</li>
	<li><code>1 &lt;= name.length &lt;= 10</code></li>
	<li><code>1 &lt;= score &lt;= 10<sup>5</sup></code></li>
	<li>任意时刻，调用&nbsp;<code>get</code>&nbsp;的次数都不超过调用&nbsp;<code>add</code>&nbsp;的次数。</li>
	<li><strong>总共</strong>&nbsp;调用&nbsp;<code>add</code> 和&nbsp;<code>get</code>&nbsp;不超过&nbsp;<code>4 * 10<sup>4</sup></code>&nbsp;</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 数据流
- 有序集合
- 堆（优先队列）

## 提示

1. If the problem were to find the median of a stream of scenery locations while they are being added, can you solve it?
2. We can use a similar approach as an optimization to avoid repeated sorting.
3. Employ two heaps: left heap and right heap. The left heap is a max-heap, and the right heap is a min-heap. The size of the left heap is k + 1 (best locations), where k is the number of times the get method was invoked. The other locations are maintained in the right heap.
4. Every time when add is being called, we add it to the left heap. If the size of the left heap exceeds k + 1, we move the head element to the right heap.
5. When the get method is invoked again (the k + 1 time it is invoked), we can return the head element of the left heap. But before returning it, if the right heap is not empty, we maintain the left heap to have the best k + 2 items by moving the best location from the right heap to the left heap.

## 示例

```
["SORTracker","add","add","get","add","get","add","get","add","get","add","get","get"]
[[],["bradford",2],["branford",3],[],["alps",2],[],["orland",2],[],["orlando",3],[],["alpine",2],[],[]]
```

## 示例代码

### C++

```cpp
class SORTracker {
public:
    SORTracker() {
        
    }
    
    void add(string name, int score) {
        
    }
    
    string get() {
        
    }
};

/**
 * Your SORTracker object will be instantiated and called as such:
 * SORTracker* obj = new SORTracker();
 * obj->add(name,score);
 * string param_2 = obj->get();
 */
```

### Java

```java
class SORTracker {

    public SORTracker() {
        
    }
    
    public void add(String name, int score) {
        
    }
    
    public String get() {
        
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * SORTracker obj = new SORTracker();
 * obj.add(name,score);
 * String param_2 = obj.get();
 */
```

### Python

```python
class SORTracker(object):

    def __init__(self):
        

    def add(self, name, score):
        """
        :type name: str
        :type score: int
        :rtype: None
        """
        

    def get(self):
        """
        :rtype: str
        """
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
```

### Python3

```python3
class SORTracker:

    def __init__(self):
        

    def add(self, name: str, score: int) -> None:
        

    def get(self) -> str:
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
```

### C

```c



typedef struct {
    
} SORTracker;


SORTracker* sORTrackerCreate() {
    
}

void sORTrackerAdd(SORTracker* obj, char* name, int score) {
    
}

char* sORTrackerGet(SORTracker* obj) {
    
}

void sORTrackerFree(SORTracker* obj) {
    
}

/**
 * Your SORTracker struct will be instantiated and called as such:
 * SORTracker* obj = sORTrackerCreate();
 * sORTrackerAdd(obj, name, score);
 
 * char* param_2 = sORTrackerGet(obj);
 
 * sORTrackerFree(obj);
*/
```

### C#

```csharp
public class SORTracker {

    public SORTracker() {
        
    }
    
    public void Add(string name, int score) {
        
    }
    
    public string Get() {
        
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * SORTracker obj = new SORTracker();
 * obj.Add(name,score);
 * string param_2 = obj.Get();
 */
```

### JavaScript

```javascript

var SORTracker = function() {
    
};

/** 
 * @param {string} name 
 * @param {number} score
 * @return {void}
 */
SORTracker.prototype.add = function(name, score) {
    
};

/**
 * @return {string}
 */
SORTracker.prototype.get = function() {
    
};

/** 
 * Your SORTracker object will be instantiated and called as such:
 * var obj = new SORTracker()
 * obj.add(name,score)
 * var param_2 = obj.get()
 */
```

### TypeScript

```typescript
class SORTracker {
    constructor() {
        
    }

    add(name: string, score: number): void {
        
    }

    get(): string {
        
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * var obj = new SORTracker()
 * obj.add(name,score)
 * var param_2 = obj.get()
 */
```

### PHP

```php
class SORTracker {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param String $name
     * @param Integer $score
     * @return NULL
     */
    function add($name, $score) {
        
    }
  
    /**
     * @return String
     */
    function get() {
        
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * $obj = SORTracker();
 * $obj->add($name, $score);
 * $ret_2 = $obj->get();
 */
```

### Swift

```swift

class SORTracker {

    init() {
        
    }
    
    func add(_ name: String, _ score: Int) {
        
    }
    
    func get() -> String {
        
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * let obj = SORTracker()
 * obj.add(name, score)
 * let ret_2: String = obj.get()
 */
```

### Kotlin

```kotlin
class SORTracker() {

    fun add(name: String, score: Int) {
        
    }

    fun get(): String {
        
    }

}

/**
 * Your SORTracker object will be instantiated and called as such:
 * var obj = SORTracker()
 * obj.add(name,score)
 * var param_2 = obj.get()
 */
```

### Dart

```dart
class SORTracker {

  SORTracker() {
    
  }
  
  void add(String name, int score) {
    
  }
  
  String get() {
    
  }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * SORTracker obj = SORTracker();
 * obj.add(name,score);
 * String param2 = obj.get();
 */
```

### Go

```golang
type SORTracker struct {
    
}


func Constructor() SORTracker {
    
}


func (this *SORTracker) Add(name string, score int)  {
    
}


func (this *SORTracker) Get() string {
    
}


/**
 * Your SORTracker object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(name,score);
 * param_2 := obj.Get();
 */
```

### Ruby

```ruby
class SORTracker
    def initialize()
        
    end


=begin
    :type name: String
    :type score: Integer
    :rtype: Void
=end
    def add(name, score)
        
    end


=begin
    :rtype: String
=end
    def get()
        
    end


end

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker.new()
# obj.add(name, score)
# param_2 = obj.get()
```

### Scala

```scala
class SORTracker() {

    def add(name: String, score: Int): Unit = {
        
    }

    def get(): String = {
        
    }

}

/**
 * Your SORTracker object will be instantiated and called as such:
 * val obj = new SORTracker()
 * obj.add(name,score)
 * val param_2 = obj.get()
 */
```

### Rust

```rust
struct SORTracker {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SORTracker {

    fn new() -> Self {
        
    }
    
    fn add(&self, name: String, score: i32) {
        
    }
    
    fn get(&self) -> String {
        
    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * let obj = SORTracker::new();
 * obj.add(name, score);
 * let ret_2: String = obj.get();
 */
```

### Racket

```racket
(define sor-tracker%
  (class object%
    (super-new)
    
    (init-field)
    
    ; add : string? exact-integer? -> void?
    (define/public (add name score)
      )
    ; get : -> string?
    (define/public (get)
      )))

;; Your sor-tracker% object will be instantiated and called as such:
;; (define obj (new sor-tracker%))
;; (send obj add name score)
;; (define param_2 (send obj get))
```

### Erlang

```erlang
-spec sor_tracker_init_() -> any().
sor_tracker_init_() ->
  .

-spec sor_tracker_add(Name :: unicode:unicode_binary(), Score :: integer()) -> any().
sor_tracker_add(Name, Score) ->
  .

-spec sor_tracker_get() -> unicode:unicode_binary().
sor_tracker_get() ->
  .


%% Your functions will be called as such:
%% sor_tracker_init_(),
%% sor_tracker_add(Name, Score),
%% Param_2 = sor_tracker_get(),

%% sor_tracker_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule SORTracker do
  @spec init_() :: any
  def init_() do
    
  end

  @spec add(name :: String.t, score :: integer) :: any
  def add(name, score) do
    
  end

  @spec get() :: String.t
  def get() do
    
  end
end

# Your functions will be called as such:
# SORTracker.init_()
# SORTracker.add(name, score)
# param_2 = SORTracker.get()

# SORTracker.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class SORTracker {
    init() {

    }
    
    func add(name: String, score: Int64): Unit {

    }
    
    func get(): String {

    }
}

/**
 * Your SORTracker object will be instantiated and called as such:
 * let obj: SORTracker = SORTracker()
 * obj.add(name,score)
 * let param_2 = obj.get()
 */
```

