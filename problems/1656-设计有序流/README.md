# 1656. 设计有序流

## 题目描述

<p>有 <code>n</code> 个 <code>(id, value)</code> 对，其中 <code>id</code> 是 <code>1</code> 到 <code>n</code> 之间的一个整数，<code>value</code> 是一个字符串。不存在 <code>id</code> 相同的两个 <code>(id, value)</code> 对。</p>

<p>设计一个流，以 <strong>任意</strong> 顺序获取 <code>n</code> 个 <code>(id, value)</code> 对，并在多次调用时 <strong>按 <code>id</code> 递增的顺序</strong> 返回一些值。</p>

<p>实现 <code>OrderedStream</code> 类：</p>

<ul>
	<li><code>OrderedStream(int n)</code> 构造一个能接收 <code>n</code> 个值的流，并将当前指针 <code>ptr</code> 设为 <code>1</code> 。</li>
	<li><code>String[] insert(int id, String value)</code> 向流中存储新的 <code>(id, value)</code> 对。存储后：
	<ul>
		<li>如果流存储有 <code>id = ptr</code> 的 <code>(id, value)</code> 对，则找出从 <code>id = ptr</code> 开始的 <strong>最长 id 连续递增序列</strong> ，并 <strong>按顺序</strong> 返回与这些 id 关联的值的列表。然后，将 <code>ptr</code> 更新为最后那个  <code>id + 1</code> 。</li>
		<li>
		<p>否则，返回一个空列表。</p>
		</li>
	</ul>
	</li>
</ul>

<p> </p>

<p><strong>示例：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/15/q1.gif" style="width: 682px; height: 240px;" /></strong></p>

<pre>
<strong>输入</strong>
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
<strong>输出</strong>
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

<strong>解释</strong>
OrderedStream os= new OrderedStream(5);
os.insert(3, "ccccc"); // 插入 (3, "ccccc")，返回 []
os.insert(1, "aaaaa"); // 插入 (1, "aaaaa")，返回 ["aaaaa"]
os.insert(2, "bbbbb"); // 插入 (2, "bbbbb")，返回 ["bbbbb", "ccccc"]
os.insert(5, "eeeee"); // 插入 (5, "eeeee")，返回 []
os.insert(4, "ddddd"); // 插入 (4, "ddddd")，返回 ["ddddd", "eeeee"]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 1000</code></li>
	<li><code>1 <= id <= n</code></li>
	<li><code>value.length == 5</code></li>
	<li><code>value</code> 仅由小写字母组成</li>
	<li>每次调用 <code>insert</code> 都会使用一个唯一的 <code>id</code></li>
	<li>恰好调用 <code>n</code> 次 <code>insert</code></li>
</ul>


## 难度

Easy

## 标签

- 设计
- 数组
- 哈希表
- 数据流

## 提示

1. Maintain the next id that should be outputted.
2. Maintain the ids that were inserted in the stream.
3. Per each insert, make a loop where you check if the id that has the turn has been inserted, and if so increment the id that has the turn and continue the loop, else break.

## 示例

```
["OrderedStream","insert","insert","insert","insert","insert"]
[[5],[3,"ccccc"],[1,"aaaaa"],[2,"bbbbb"],[5,"eeeee"],[4,"ddddd"]]
```

## 示例代码

### C++

```cpp
class OrderedStream {
public:
    OrderedStream(int n) {
        
    }
    
    vector<string> insert(int idKey, string value) {
        
    }
};

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream* obj = new OrderedStream(n);
 * vector<string> param_1 = obj->insert(idKey,value);
 */
```

### Java

```java
class OrderedStream {

    public OrderedStream(int n) {
        
    }
    
    public List<String> insert(int idKey, String value) {
        
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = new OrderedStream(n);
 * List<String> param_1 = obj.insert(idKey,value);
 */
```

### Python

```python
class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
```

### Python3

```python3
class OrderedStream:

    def __init__(self, n: int):
        

    def insert(self, idKey: int, value: str) -> List[str]:
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
```

### C

```c



typedef struct {
    
} OrderedStream;


OrderedStream* orderedStreamCreate(int n) {
    
}

char** orderedStreamInsert(OrderedStream* obj, int idKey, char* value, int* retSize) {
    
}

void orderedStreamFree(OrderedStream* obj) {
    
}

/**
 * Your OrderedStream struct will be instantiated and called as such:
 * OrderedStream* obj = orderedStreamCreate(n);
 * char** param_1 = orderedStreamInsert(obj, idKey, value, retSize);
 
 * orderedStreamFree(obj);
*/
```

### C#

```csharp
public class OrderedStream {

    public OrderedStream(int n) {
        
    }
    
    public IList<string> Insert(int idKey, string value) {
        
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = new OrderedStream(n);
 * IList<string> param_1 = obj.Insert(idKey,value);
 */
```

### JavaScript

```javascript
/**
 * @param {number} n
 */
var OrderedStream = function(n) {
    
};

/** 
 * @param {number} idKey 
 * @param {string} value
 * @return {string[]}
 */
OrderedStream.prototype.insert = function(idKey, value) {
    
};

/** 
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(idKey,value)
 */
```

### TypeScript

```typescript
class OrderedStream {
    constructor(n: number) {
        
    }

    insert(idKey: number, value: string): string[] {
        
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(idKey,value)
 */
```

### PHP

```php
class OrderedStream {
    /**
     * @param Integer $n
     */
    function __construct($n) {
        
    }
  
    /**
     * @param Integer $idKey
     * @param String $value
     * @return String[]
     */
    function insert($idKey, $value) {
        
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * $obj = OrderedStream($n);
 * $ret_1 = $obj->insert($idKey, $value);
 */
```

### Swift

```swift

class OrderedStream {

    init(_ n: Int) {
        
    }
    
    func insert(_ idKey: Int, _ value: String) -> [String] {
        
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * let obj = OrderedStream(n)
 * let ret_1: [String] = obj.insert(idKey, value)
 */
```

### Kotlin

```kotlin
class OrderedStream(n: Int) {

    fun insert(idKey: Int, value: String): List<String> {
        
    }

}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = OrderedStream(n)
 * var param_1 = obj.insert(idKey,value)
 */
```

### Dart

```dart
class OrderedStream {

  OrderedStream(int n) {
    
  }
  
  List<String> insert(int idKey, String value) {
    
  }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = OrderedStream(n);
 * List<String> param1 = obj.insert(idKey,value);
 */
```

### Go

```golang
type OrderedStream struct {
    
}


func Constructor(n int) OrderedStream {
    
}


func (this *OrderedStream) Insert(idKey int, value string) []string {
    
}


/**
 * Your OrderedStream object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Insert(idKey,value);
 */
```

### Ruby

```ruby
class OrderedStream

=begin
    :type n: Integer
=end
    def initialize(n)
        
    end


=begin
    :type id_key: Integer
    :type value: String
    :rtype: String[]
=end
    def insert(id_key, value)
        
    end


end

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream.new(n)
# param_1 = obj.insert(id_key, value)
```

### Scala

```scala
class OrderedStream(_n: Int) {

    def insert(idKey: Int, value: String): List[String] = {
        
    }

}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * val obj = new OrderedStream(n)
 * val param_1 = obj.insert(idKey,value)
 */
```

### Rust

```rust
struct OrderedStream {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl OrderedStream {

    fn new(n: i32) -> Self {
        
    }
    
    fn insert(&self, id_key: i32, value: String) -> Vec<String> {
        
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * let obj = OrderedStream::new(n);
 * let ret_1: Vec<String> = obj.insert(idKey, value);
 */
```

### Racket

```racket
(define ordered-stream%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    (init-field
      n)
    
    ; insert : exact-integer? string? -> (listof string?)
    (define/public (insert id-key value)
      )))

;; Your ordered-stream% object will be instantiated and called as such:
;; (define obj (new ordered-stream% [n n]))
;; (define param_1 (send obj insert id-key value))
```

### Erlang

```erlang
-spec ordered_stream_init_(N :: integer()) -> any().
ordered_stream_init_(N) ->
  .

-spec ordered_stream_insert(IdKey :: integer(), Value :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
ordered_stream_insert(IdKey, Value) ->
  .


%% Your functions will be called as such:
%% ordered_stream_init_(N),
%% Param_1 = ordered_stream_insert(IdKey, Value),

%% ordered_stream_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule OrderedStream do
  @spec init_(n :: integer) :: any
  def init_(n) do
    
  end

  @spec insert(id_key :: integer, value :: String.t) :: [String.t]
  def insert(id_key, value) do
    
  end
end

# Your functions will be called as such:
# OrderedStream.init_(n)
# param_1 = OrderedStream.insert(id_key, value)

# OrderedStream.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class OrderedStream {
    init(n: Int64) {

    }
    
    func insert(idKey: Int64, value: String): ArrayList<String> {

    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * let obj: OrderedStream = OrderedStream(n)
 * let param_1 = obj.insert(idKey,value)
 */
```

