# 981. 基于时间的键值存储

## 题目描述

<p>设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。</p>

<p>实现 <code>TimeMap</code> 类：</p>

<ul>
	<li><code>TimeMap()</code> 初始化数据结构对象</li>
	<li><code>void set(String key, String value, int timestamp)</code> 存储给定时间戳&nbsp;<code>timestamp</code>&nbsp;时的键&nbsp;<code>key</code>&nbsp;和值&nbsp;<code>value</code>。</li>
	<li><code>String get(String key, int timestamp)</code>&nbsp;返回一个值，该值在之前调用了 <code>set</code>，其中&nbsp;<code>timestamp_prev &lt;= timestamp</code>&nbsp;。如果有多个这样的值，它将返回与最大 &nbsp;<code>timestamp_prev</code>&nbsp;关联的值。如果没有值，则返回空字符串（<code>""</code>）。</li>
</ul>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
<strong>输出：</strong>
[null, null, "bar", "bar", null, "bar2", "bar2"]

<strong>解释：</strong>
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1 &nbsp; 
timeMap.get("foo", 1);         // 返回 "bar"
timeMap.get("foo", 3);         // 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 。
timeMap.set("foo", "bar2", 4); // 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4&nbsp; 
timeMap.get("foo", 4);         // 返回 "bar2"
timeMap.get("foo", 5);         // 返回 "bar2"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= key.length, value.length &lt;= 100</code></li>
	<li><code>key</code> 和 <code>value</code> 由小写英文字母和数字组成</li>
	<li><code>1 &lt;= timestamp &lt;= 10<sup>7</sup></code></li>
	<li><code>set</code> 操作中的时间戳 <code>timestamp</code> 都是严格递增的</li>
	<li>最多调用&nbsp;<code>set</code> 和 <code>get</code> 操作 <code>2 * 10<sup>5</sup></code> 次</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 哈希表
- 字符串
- 二分查找

## 示例

```
["TimeMap","set","get","get","set","get","get"]
[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
```

## 示例代码

### C++

```cpp
class TimeMap {
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        
    }
    
    string get(string key, int timestamp) {
        
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
```

### Java

```java
class TimeMap {

    public TimeMap() {
        
    }
    
    public void set(String key, String value, int timestamp) {
        
    }
    
    public String get(String key, int timestamp) {
        
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
```

### Python

```python
class TimeMap(object):

    def __init__(self):
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

### Python3

```python3
class TimeMap:

    def __init__(self):
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        

    def get(self, key: str, timestamp: int) -> str:
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

### C

```c



typedef struct {
    
} TimeMap;


TimeMap* timeMapCreate() {
    
}

void timeMapSet(TimeMap* obj, char* key, char* value, int timestamp) {
    
}

char* timeMapGet(TimeMap* obj, char* key, int timestamp) {
    
}

void timeMapFree(TimeMap* obj) {
    
}

/**
 * Your TimeMap struct will be instantiated and called as such:
 * TimeMap* obj = timeMapCreate();
 * timeMapSet(obj, key, value, timestamp);
 
 * char* param_2 = timeMapGet(obj, key, timestamp);
 
 * timeMapFree(obj);
*/
```

### C#

```csharp
public class TimeMap {

    public TimeMap() {
        
    }
    
    public void Set(string key, string value, int timestamp) {
        
    }
    
    public string Get(string key, int timestamp) {
        
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.Set(key,value,timestamp);
 * string param_2 = obj.Get(key,timestamp);
 */
```

### JavaScript

```javascript

var TimeMap = function() {
    
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
    
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {
    
};

/** 
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
```

### TypeScript

```typescript
class TimeMap {
    constructor() {
        
    }

    set(key: string, value: string, timestamp: number): void {
        
    }

    get(key: string, timestamp: number): string {
        
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
```

### PHP

```php
class TimeMap {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param String $key
     * @param String $value
     * @param Integer $timestamp
     * @return NULL
     */
    function set($key, $value, $timestamp) {
        
    }
  
    /**
     * @param String $key
     * @param Integer $timestamp
     * @return String
     */
    function get($key, $timestamp) {
        
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * $obj = TimeMap();
 * $obj->set($key, $value, $timestamp);
 * $ret_2 = $obj->get($key, $timestamp);
 */
```

### Swift

```swift

class TimeMap {

    init() {
        
    }
    
    func set(_ key: String, _ value: String, _ timestamp: Int) {
        
    }
    
    func get(_ key: String, _ timestamp: Int) -> String {
        
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * let obj = TimeMap()
 * obj.set(key, value, timestamp)
 * let ret_2: String = obj.get(key, timestamp)
 */
```

### Kotlin

```kotlin
class TimeMap() {

    fun set(key: String, value: String, timestamp: Int) {
        
    }

    fun get(key: String, timestamp: Int): String {
        
    }

}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */
```

### Dart

```dart
class TimeMap {

  TimeMap() {
    
  }
  
  void set(String key, String value, int timestamp) {
    
  }
  
  String get(String key, int timestamp) {
    
  }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = TimeMap();
 * obj.set(key,value,timestamp);
 * String param2 = obj.get(key,timestamp);
 */
```

### Go

```golang
type TimeMap struct {
    
}


func Constructor() TimeMap {
    
}


func (this *TimeMap) Set(key string, value string, timestamp int)  {
    
}


func (this *TimeMap) Get(key string, timestamp int) string {
    
}


/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */
```

### Ruby

```ruby
class TimeMap
    def initialize()
        
    end


=begin
    :type key: String
    :type value: String
    :type timestamp: Integer
    :rtype: Void
=end
    def set(key, value, timestamp)
        
    end


=begin
    :type key: String
    :type timestamp: Integer
    :rtype: String
=end
    def get(key, timestamp)
        
    end


end

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap.new()
# obj.set(key, value, timestamp)
# param_2 = obj.get(key, timestamp)
```

### Scala

```scala
class TimeMap() {

    def set(key: String, value: String, timestamp: Int): Unit = {
        
    }

    def get(key: String, timestamp: Int): String = {
        
    }

}

/**
 * Your TimeMap object will be instantiated and called as such:
 * val obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * val param_2 = obj.get(key,timestamp)
 */
```

### Rust

```rust
struct TimeMap {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TimeMap {

    fn new() -> Self {
        
    }
    
    fn set(&self, key: String, value: String, timestamp: i32) {
        
    }
    
    fn get(&self, key: String, timestamp: i32) -> String {
        
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * let obj = TimeMap::new();
 * obj.set(key, value, timestamp);
 * let ret_2: String = obj.get(key, timestamp);
 */
```

### Racket

```racket
(define time-map%
  (class object%
    (super-new)
    
    (init-field)
    
    ; set : string? string? exact-integer? -> void?
    (define/public (set key value timestamp)
      )
    ; get : string? exact-integer? -> string?
    (define/public (get key timestamp)
      )))

;; Your time-map% object will be instantiated and called as such:
;; (define obj (new time-map%))
;; (send obj set key value timestamp)
;; (define param_2 (send obj get key timestamp))
```

### Erlang

```erlang
-spec time_map_init_() -> any().
time_map_init_() ->
  .

-spec time_map_set(Key :: unicode:unicode_binary(), Value :: unicode:unicode_binary(), Timestamp :: integer()) -> any().
time_map_set(Key, Value, Timestamp) ->
  .

-spec time_map_get(Key :: unicode:unicode_binary(), Timestamp :: integer()) -> unicode:unicode_binary().
time_map_get(Key, Timestamp) ->
  .


%% Your functions will be called as such:
%% time_map_init_(),
%% time_map_set(Key, Value, Timestamp),
%% Param_2 = time_map_get(Key, Timestamp),

%% time_map_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule TimeMap do
  @spec init_() :: any
  def init_() do
    
  end

  @spec set(key :: String.t, value :: String.t, timestamp :: integer) :: any
  def set(key, value, timestamp) do
    
  end

  @spec get(key :: String.t, timestamp :: integer) :: String.t
  def get(key, timestamp) do
    
  end
end

# Your functions will be called as such:
# TimeMap.init_()
# TimeMap.set(key, value, timestamp)
# param_2 = TimeMap.get(key, timestamp)

# TimeMap.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class TimeMap {
    init() {

    }
    
    func set(key: String, value: String, timestamp: Int64): Unit {

    }
    
    func get(key: String, timestamp: Int64): String {

    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * let obj: TimeMap = TimeMap()
 * obj.set(key,value,timestamp)
 * let param_2 = obj.get(key,timestamp)
 */
```

