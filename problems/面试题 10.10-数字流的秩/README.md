# 面试题 10.10. 数字流的秩

## 题目描述

<p>假设你正在读取一串整数。每隔一段时间，你希望能找出数字 x 的秩(小于或等于 x 的值的个数)。请实现数据结构和算法来支持这些操作，也就是说：</p>

<p>实现 <code>track(int x)</code>&nbsp;方法，每读入一个数字都会调用该方法；</p>

<p>实现 <code>getRankOfNumber(int x)</code> 方法，返回小于或等于 x 的值的个数。</p>

<p><strong>注意：</strong>本题相对原题稍作改动</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
[[], [1], [0], [0]]
<strong>输出：
</strong>[null,0,null,1]
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>x &lt;= 50000</code></li>
	<li><code>track</code>&nbsp;和&nbsp;<code>getRankOfNumber</code> 方法的调用次数均不超过 2000 次</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 树状数组
- 二分查找
- 数据流

## 提示

1. 使用数组存在的问题是插入一个数字会比较慢。我们还能使用其他的数据结构吗？
2. 二叉搜索树效果好吗？
3. 考虑一个二叉搜索树，其中每个节点存储一些额外的数据。

## 示例

```
["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
[[], [1], [0], [0]]
```

## 示例代码

### C++

```cpp
class StreamRank {
public:
    StreamRank() {
        
    }
    
    void track(int x) {
        
    }
    
    int getRankOfNumber(int x) {
        
    }
};

/**
 * Your StreamRank object will be instantiated and called as such:
 * StreamRank* obj = new StreamRank();
 * obj->track(x);
 * int param_2 = obj->getRankOfNumber(x);
 */
```

### Java

```java
class StreamRank {

    public StreamRank() {
        
    }
    
    public void track(int x) {
        
    }
    
    public int getRankOfNumber(int x) {
        
    }
}

/**
 * Your StreamRank object will be instantiated and called as such:
 * StreamRank obj = new StreamRank();
 * obj.track(x);
 * int param_2 = obj.getRankOfNumber(x);
 */
```

### Python

```python
class StreamRank(object):

    def __init__(self):
        

    def track(self, x):
        """
        :type x: int
        :rtype: None
        """
        

    def getRankOfNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)
```

### Python3

```python3
class StreamRank:

    def __init__(self):
        

    def track(self, x: int) -> None:
        

    def getRankOfNumber(self, x: int) -> int:
        


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)
```

### C

```c



typedef struct {
    
} StreamRank;


StreamRank* streamRankCreate() {
    
}

void streamRankTrack(StreamRank* obj, int x) {
    
}

int streamRankGetRankOfNumber(StreamRank* obj, int x) {
    
}

void streamRankFree(StreamRank* obj) {
    
}

/**
 * Your StreamRank struct will be instantiated and called as such:
 * StreamRank* obj = streamRankCreate();
 * streamRankTrack(obj, x);
 
 * int param_2 = streamRankGetRankOfNumber(obj, x);
 
 * streamRankFree(obj);
*/
```

### C#

```csharp
public class StreamRank {

    public StreamRank() {
        
    }
    
    public void Track(int x) {
        
    }
    
    public int GetRankOfNumber(int x) {
        
    }
}

/**
 * Your StreamRank object will be instantiated and called as such:
 * StreamRank obj = new StreamRank();
 * obj.Track(x);
 * int param_2 = obj.GetRankOfNumber(x);
 */
```

### JavaScript

```javascript

var StreamRank = function() {
    
};

/** 
 * @param {number} x
 * @return {void}
 */
StreamRank.prototype.track = function(x) {
    
};

/** 
 * @param {number} x
 * @return {number}
 */
StreamRank.prototype.getRankOfNumber = function(x) {
    
};

/** 
 * Your StreamRank object will be instantiated and called as such:
 * var obj = new StreamRank()
 * obj.track(x)
 * var param_2 = obj.getRankOfNumber(x)
 */
```

### TypeScript

```typescript
class StreamRank {
    constructor() {
        
    }

    track(x: number): void {
        
    }

    getRankOfNumber(x: number): number {
        
    }
}

/**
 * Your StreamRank object will be instantiated and called as such:
 * var obj = new StreamRank()
 * obj.track(x)
 * var param_2 = obj.getRankOfNumber(x)
 */
```

### PHP

```php
class StreamRank {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $x
     * @return NULL
     */
    function track($x) {
        
    }
  
    /**
     * @param Integer $x
     * @return Integer
     */
    function getRankOfNumber($x) {
        
    }
}

/**
 * Your StreamRank object will be instantiated and called as such:
 * $obj = StreamRank();
 * $obj->track($x);
 * $ret_2 = $obj->getRankOfNumber($x);
 */
```

### Swift

```swift

class StreamRank {

    init() {
        
    }
    
    func track(_ x: Int) {
        
    }
    
    func getRankOfNumber(_ x: Int) -> Int {
        
    }
}

/**
 * Your StreamRank object will be instantiated and called as such:
 * let obj = StreamRank()
 * obj.track(x)
 * let ret_2: Int = obj.getRankOfNumber(x)
 */
```

### Kotlin

```kotlin
class StreamRank() {

    fun track(x: Int) {
        
    }

    fun getRankOfNumber(x: Int): Int {
        
    }

}

/**
 * Your StreamRank object will be instantiated and called as such:
 * var obj = StreamRank()
 * obj.track(x)
 * var param_2 = obj.getRankOfNumber(x)
 */
```

### Dart

```dart
class StreamRank {

  StreamRank() {
    
  }
  
  void track(int x) {
    
  }
  
  int getRankOfNumber(int x) {
    
  }
}

/**
 * Your StreamRank object will be instantiated and called as such:
 * StreamRank obj = StreamRank();
 * obj.track(x);
 * int param2 = obj.getRankOfNumber(x);
 */
```

### Go

```golang
type StreamRank struct {
    
}


func Constructor() StreamRank {
    
}


func (this *StreamRank) Track(x int)  {
    
}


func (this *StreamRank) GetRankOfNumber(x int) int {
    
}


/**
 * Your StreamRank object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Track(x);
 * param_2 := obj.GetRankOfNumber(x);
 */
```

### Ruby

```ruby
class StreamRank
    def initialize()
        
    end


=begin
    :type x: Integer
    :rtype: Void
=end
    def track(x)
        
    end


=begin
    :type x: Integer
    :rtype: Integer
=end
    def get_rank_of_number(x)
        
    end


end

# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank.new()
# obj.track(x)
# param_2 = obj.get_rank_of_number(x)
```

### Scala

```scala
class StreamRank() {

    def track(x: Int): Unit = {
        
    }

    def getRankOfNumber(x: Int): Int = {
        
    }

}

/**
 * Your StreamRank object will be instantiated and called as such:
 * val obj = new StreamRank()
 * obj.track(x)
 * val param_2 = obj.getRankOfNumber(x)
 */
```

### Rust

```rust
struct StreamRank {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StreamRank {

    fn new() -> Self {
        
    }
    
    fn track(&self, x: i32) {
        
    }
    
    fn get_rank_of_number(&self, x: i32) -> i32 {
        
    }
}

/**
 * Your StreamRank object will be instantiated and called as such:
 * let obj = StreamRank::new();
 * obj.track(x);
 * let ret_2: i32 = obj.get_rank_of_number(x);
 */
```

### Racket

```racket
(define stream-rank%
  (class object%
    (super-new)
    
    (init-field)
    
    ; track : exact-integer? -> void?
    (define/public (track x)
      )
    ; get-rank-of-number : exact-integer? -> exact-integer?
    (define/public (get-rank-of-number x)
      )))

;; Your stream-rank% object will be instantiated and called as such:
;; (define obj (new stream-rank%))
;; (send obj track x)
;; (define param_2 (send obj get-rank-of-number x))
```

### Erlang

```erlang
-spec stream_rank_init_() -> any().
stream_rank_init_() ->
  .

-spec stream_rank_track(X :: integer()) -> any().
stream_rank_track(X) ->
  .

-spec stream_rank_get_rank_of_number(X :: integer()) -> integer().
stream_rank_get_rank_of_number(X) ->
  .


%% Your functions will be called as such:
%% stream_rank_init_(),
%% stream_rank_track(X),
%% Param_2 = stream_rank_get_rank_of_number(X),

%% stream_rank_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule StreamRank do
  @spec init_() :: any
  def init_() do
    
  end

  @spec track(x :: integer) :: any
  def track(x) do
    
  end

  @spec get_rank_of_number(x :: integer) :: integer
  def get_rank_of_number(x) do
    
  end
end

# Your functions will be called as such:
# StreamRank.init_()
# StreamRank.track(x)
# param_2 = StreamRank.get_rank_of_number(x)

# StreamRank.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class StreamRank {
    init() {

    }
    
    func track(x: Int64): Unit {

    }
    
    func getRankOfNumber(x: Int64): Int64 {

    }
}

/**
 * Your StreamRank object will be instantiated and called as such:
 * let obj: StreamRank = StreamRank()
 * obj.track(x)
 * let param_2 = obj.getRankOfNumber(x)
 */
```

