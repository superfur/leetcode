# 2526. 找到数据流中的连续整数

## 题目描述

<p>给你一个整数数据流，请你实现一个数据结构，检查数据流中最后&nbsp;<code>k</code>&nbsp;个整数是否 <strong>等于</strong> 给定值&nbsp;<code>value</code>&nbsp;。</p>

<p>请你实现&nbsp;<strong>DataStream</strong>&nbsp;类：</p>

<ul>
	<li><code>DataStream(int value, int k)</code>&nbsp;用两个整数 <code>value</code>&nbsp;和 <code>k</code>&nbsp;初始化一个空的整数数据流。</li>
	<li><code>boolean consec(int num)</code>&nbsp;将&nbsp;<code>num</code>&nbsp;添加到整数数据流。如果后 <code>k</code>&nbsp;个整数都等于&nbsp;<code>value</code>&nbsp;，返回&nbsp;<code>true</code>&nbsp;，否则返回&nbsp;<code>false</code>&nbsp;。如果少于&nbsp;<code>k</code>&nbsp;个整数，条件不满足，所以也返回&nbsp;<code>false</code>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["DataStream", "consec", "consec", "consec", "consec"]
[[4, 3], [4], [4], [4], [3]]
<strong>输出：</strong>
[null, false, false, true, false]

<strong>解释：</strong>
DataStream dataStream = new DataStream(4, 3); // value = 4, k = 3 
dataStream.consec(4); // 数据流中只有 1 个整数，所以返回 False 。
dataStream.consec(4); // 数据流中只有 2 个整数
                      // 由于 2 小于 k ，返回 False 。
dataStream.consec(4); // 数据流最后 3 个整数都等于 value， 所以返回 True 。
dataStream.consec(3); // 最后 k 个整数分别是 [4,4,3] 。
                      // 由于 3 不等于 value ，返回 False 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= value, num &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
	<li>至多调用 <code>consec</code>&nbsp;次数为&nbsp;<code>10<sup>5</sup></code>&nbsp;次。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 队列
- 哈希表
- 计数
- 数据流

## 提示

1. Keep track of the last integer which is not equal to <code>value</code>.
2. Use a queue-type data structure to store the last <code>k</code> integers.

## 示例

```
["DataStream","consec","consec","consec","consec"]
[[4,3],[4],[4],[4],[3]]
```

## 示例代码

### C++

```cpp
class DataStream {
public:
    DataStream(int value, int k) {
        
    }
    
    bool consec(int num) {
        
    }
};

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream* obj = new DataStream(value, k);
 * bool param_1 = obj->consec(num);
 */
```

### Java

```java
class DataStream {

    public DataStream(int value, int k) {
        
    }
    
    public boolean consec(int num) {
        
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream obj = new DataStream(value, k);
 * boolean param_1 = obj.consec(num);
 */
```

### Python

```python
class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
```

### Python3

```python3
class DataStream:

    def __init__(self, value: int, k: int):
        

    def consec(self, num: int) -> bool:
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
```

### C

```c



typedef struct {
    
} DataStream;


DataStream* dataStreamCreate(int value, int k) {
    
}

bool dataStreamConsec(DataStream* obj, int num) {
    
}

void dataStreamFree(DataStream* obj) {
    
}

/**
 * Your DataStream struct will be instantiated and called as such:
 * DataStream* obj = dataStreamCreate(value, k);
 * bool param_1 = dataStreamConsec(obj, num);
 
 * dataStreamFree(obj);
*/
```

### C#

```csharp
public class DataStream {

    public DataStream(int value, int k) {
        
    }
    
    public bool Consec(int num) {
        
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream obj = new DataStream(value, k);
 * bool param_1 = obj.Consec(num);
 */
```

### JavaScript

```javascript
/**
 * @param {number} value
 * @param {number} k
 */
var DataStream = function(value, k) {
    
};

/** 
 * @param {number} num
 * @return {boolean}
 */
DataStream.prototype.consec = function(num) {
    
};

/** 
 * Your DataStream object will be instantiated and called as such:
 * var obj = new DataStream(value, k)
 * var param_1 = obj.consec(num)
 */
```

### TypeScript

```typescript
class DataStream {
    constructor(value: number, k: number) {
        
    }

    consec(num: number): boolean {
        
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * var obj = new DataStream(value, k)
 * var param_1 = obj.consec(num)
 */
```

### PHP

```php
class DataStream {
    /**
     * @param Integer $value
     * @param Integer $k
     */
    function __construct($value, $k) {
        
    }
  
    /**
     * @param Integer $num
     * @return Boolean
     */
    function consec($num) {
        
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * $obj = DataStream($value, $k);
 * $ret_1 = $obj->consec($num);
 */
```

### Swift

```swift

class DataStream {

    init(_ value: Int, _ k: Int) {
        
    }
    
    func consec(_ num: Int) -> Bool {
        
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * let obj = DataStream(value, k)
 * let ret_1: Bool = obj.consec(num)
 */
```

### Kotlin

```kotlin
class DataStream(value: Int, k: Int) {

    fun consec(num: Int): Boolean {
        
    }

}

/**
 * Your DataStream object will be instantiated and called as such:
 * var obj = DataStream(value, k)
 * var param_1 = obj.consec(num)
 */
```

### Dart

```dart
class DataStream {

  DataStream(int value, int k) {
    
  }
  
  bool consec(int num) {
    
  }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * DataStream obj = DataStream(value, k);
 * bool param1 = obj.consec(num);
 */
```

### Go

```golang
type DataStream struct {
    
}


func Constructor(value int, k int) DataStream {
    
}


func (this *DataStream) Consec(num int) bool {
    
}


/**
 * Your DataStream object will be instantiated and called as such:
 * obj := Constructor(value, k);
 * param_1 := obj.Consec(num);
 */
```

### Ruby

```ruby
class DataStream

=begin
    :type value: Integer
    :type k: Integer
=end
    def initialize(value, k)
        
    end


=begin
    :type num: Integer
    :rtype: Boolean
=end
    def consec(num)
        
    end


end

# Your DataStream object will be instantiated and called as such:
# obj = DataStream.new(value, k)
# param_1 = obj.consec(num)
```

### Scala

```scala
class DataStream(_value: Int, _k: Int) {

    def consec(num: Int): Boolean = {
        
    }

}

/**
 * Your DataStream object will be instantiated and called as such:
 * val obj = new DataStream(value, k)
 * val param_1 = obj.consec(num)
 */
```

### Rust

```rust
struct DataStream {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl DataStream {

    fn new(value: i32, k: i32) -> Self {
        
    }
    
    fn consec(&self, num: i32) -> bool {
        
    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * let obj = DataStream::new(value, k);
 * let ret_1: bool = obj.consec(num);
 */
```

### Racket

```racket
(define data-stream%
  (class object%
    (super-new)
    
    ; value : exact-integer?
    ; k : exact-integer?
    (init-field
      value
      k)
    
    ; consec : exact-integer? -> boolean?
    (define/public (consec num)
      )))

;; Your data-stream% object will be instantiated and called as such:
;; (define obj (new data-stream% [value value] [k k]))
;; (define param_1 (send obj consec num))
```

### Erlang

```erlang
-spec data_stream_init_(Value :: integer(), K :: integer()) -> any().
data_stream_init_(Value, K) ->
  .

-spec data_stream_consec(Num :: integer()) -> boolean().
data_stream_consec(Num) ->
  .


%% Your functions will be called as such:
%% data_stream_init_(Value, K),
%% Param_1 = data_stream_consec(Num),

%% data_stream_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule DataStream do
  @spec init_(value :: integer, k :: integer) :: any
  def init_(value, k) do
    
  end

  @spec consec(num :: integer) :: boolean
  def consec(num) do
    
  end
end

# Your functions will be called as such:
# DataStream.init_(value, k)
# param_1 = DataStream.consec(num)

# DataStream.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class DataStream {
    init(value: Int64, k: Int64) {

    }
    
    func consec(num: Int64): Bool {

    }
}

/**
 * Your DataStream object will be instantiated and called as such:
 * let obj: DataStream = DataStream(value, k)
 * let param_1 = obj.consec(num)
 */
```

