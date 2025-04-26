# 2671. 频率跟踪器

## 题目描述

<p>请你设计并实现一个能够对其中的值进行跟踪的数据结构，并支持对频率相关查询进行应答。</p>

<p>实现 <code>FrequencyTracker</code> 类：</p>

<ul>
	<li><code>FrequencyTracker()</code>：使用一个空数组初始化 <code>FrequencyTracker</code> 对象。</li>
	<li><code>void add(int number)</code>：添加一个 <code>number</code> 到数据结构中。</li>
	<li><code>void deleteOne(int number)</code>：从数据结构中删除一个 <code>number</code> 。数据结构 <strong>可能不包含</strong> <code>number</code> ，在这种情况下不删除任何内容。</li>
	<li><code>bool hasFrequency(int frequency)</code>: 如果数据结构中存在出现 <code>frequency</code> 次的数字，则返回 <code>true</code>，否则返回 <code>false</code>。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入</strong>
["FrequencyTracker", "add", "add", "hasFrequency"]
[[], [3], [3], [2]]
<strong>输出</strong>
[null, null, null, true]

<strong>解释</strong>
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(3); // 数据结构现在包含 [3]
frequencyTracker.add(3); // 数据结构现在包含 [3, 3]
frequencyTracker.hasFrequency(2); // 返回 true ，因为 3 出现 2 次
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入</strong>
["FrequencyTracker", "add", "deleteOne", "hasFrequency"]
[[], [1], [1], [1]]
<strong>输出</strong>
[null, null, null, false]

<strong>解释</strong>
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.add(1); // 数据结构现在包含 [1]
frequencyTracker.deleteOne(1); // 数据结构现在为空 []
frequencyTracker.hasFrequency(1); // 返回 false ，因为数据结构为空
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入</strong>
["FrequencyTracker", "hasFrequency", "add", "hasFrequency"]
[[], [2], [3], [1]]
<strong>输出</strong>
[null, false, null, true]

<strong>解释</strong>
FrequencyTracker frequencyTracker = new FrequencyTracker();
frequencyTracker.hasFrequency(2); // 返回 false ，因为数据结构为空
frequencyTracker.add(3); // 数据结构现在包含 [3]
frequencyTracker.hasFrequency(1); // 返回 true ，因为 3 出现 1 次
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= number &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= frequency &lt;= 10<sup>5</sup></code></li>
	<li>最多调用 <code>add</code>、<code>deleteOne</code> 和 <code>hasFrequency</code> <strong>共计</strong> <code>2 *&nbsp;10<sup>5</sup></code> 次</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 哈希表

## 提示

1. Put all the numbers in a hash map (or just an integer array given the number range is small) to maintain each number’s frequency dynamically.
2. Put each frequency in another hash map (or just an integer array given the range is small, note there are only 200000 calls in total) to maintain each kind of frequency dynamically.
3. Keep the 2 hash maps in sync.

## 示例

```
["FrequencyTracker","add","add","hasFrequency"]
[[],[3],[3],[2]]
["FrequencyTracker","add","deleteOne","hasFrequency"]
[[],[1],[1],[1]]
["FrequencyTracker","hasFrequency","add","hasFrequency"]
[[],[2],[3],[1]]
```

## 示例代码

### C++

```cpp
class FrequencyTracker {
public:
    FrequencyTracker() {
        
    }
    
    void add(int number) {
        
    }
    
    void deleteOne(int number) {
        
    }
    
    bool hasFrequency(int frequency) {
        
    }
};

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * FrequencyTracker* obj = new FrequencyTracker();
 * obj->add(number);
 * obj->deleteOne(number);
 * bool param_3 = obj->hasFrequency(frequency);
 */
```

### Java

```java
class FrequencyTracker {

    public FrequencyTracker() {
        
    }
    
    public void add(int number) {
        
    }
    
    public void deleteOne(int number) {
        
    }
    
    public boolean hasFrequency(int frequency) {
        
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * FrequencyTracker obj = new FrequencyTracker();
 * obj.add(number);
 * obj.deleteOne(number);
 * boolean param_3 = obj.hasFrequency(frequency);
 */
```

### Python

```python
class FrequencyTracker(object):

    def __init__(self):
        

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
```

### Python3

```python3
class FrequencyTracker:

    def __init__(self):
        

    def add(self, number: int) -> None:
        

    def deleteOne(self, number: int) -> None:
        

    def hasFrequency(self, frequency: int) -> bool:
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
```

### C

```c



typedef struct {
    
} FrequencyTracker;


FrequencyTracker* frequencyTrackerCreate() {
    
}

void frequencyTrackerAdd(FrequencyTracker* obj, int number) {
    
}

void frequencyTrackerDeleteOne(FrequencyTracker* obj, int number) {
    
}

bool frequencyTrackerHasFrequency(FrequencyTracker* obj, int frequency) {
    
}

void frequencyTrackerFree(FrequencyTracker* obj) {
    
}

/**
 * Your FrequencyTracker struct will be instantiated and called as such:
 * FrequencyTracker* obj = frequencyTrackerCreate();
 * frequencyTrackerAdd(obj, number);
 
 * frequencyTrackerDeleteOne(obj, number);
 
 * bool param_3 = frequencyTrackerHasFrequency(obj, frequency);
 
 * frequencyTrackerFree(obj);
*/
```

### C#

```csharp
public class FrequencyTracker {

    public FrequencyTracker() {
        
    }
    
    public void Add(int number) {
        
    }
    
    public void DeleteOne(int number) {
        
    }
    
    public bool HasFrequency(int frequency) {
        
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * FrequencyTracker obj = new FrequencyTracker();
 * obj.Add(number);
 * obj.DeleteOne(number);
 * bool param_3 = obj.HasFrequency(frequency);
 */
```

### JavaScript

```javascript

var FrequencyTracker = function() {
    
};

/** 
 * @param {number} number
 * @return {void}
 */
FrequencyTracker.prototype.add = function(number) {
    
};

/** 
 * @param {number} number
 * @return {void}
 */
FrequencyTracker.prototype.deleteOne = function(number) {
    
};

/** 
 * @param {number} frequency
 * @return {boolean}
 */
FrequencyTracker.prototype.hasFrequency = function(frequency) {
    
};

/** 
 * Your FrequencyTracker object will be instantiated and called as such:
 * var obj = new FrequencyTracker()
 * obj.add(number)
 * obj.deleteOne(number)
 * var param_3 = obj.hasFrequency(frequency)
 */
```

### TypeScript

```typescript
class FrequencyTracker {
    constructor() {
        
    }

    add(number: number): void {
        
    }

    deleteOne(number: number): void {
        
    }

    hasFrequency(frequency: number): boolean {
        
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * var obj = new FrequencyTracker()
 * obj.add(number)
 * obj.deleteOne(number)
 * var param_3 = obj.hasFrequency(frequency)
 */
```

### PHP

```php
class FrequencyTracker {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $number
     * @return NULL
     */
    function add($number) {
        
    }
  
    /**
     * @param Integer $number
     * @return NULL
     */
    function deleteOne($number) {
        
    }
  
    /**
     * @param Integer $frequency
     * @return Boolean
     */
    function hasFrequency($frequency) {
        
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * $obj = FrequencyTracker();
 * $obj->add($number);
 * $obj->deleteOne($number);
 * $ret_3 = $obj->hasFrequency($frequency);
 */
```

### Swift

```swift

class FrequencyTracker {

    init() {
        
    }
    
    func add(_ number: Int) {
        
    }
    
    func deleteOne(_ number: Int) {
        
    }
    
    func hasFrequency(_ frequency: Int) -> Bool {
        
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * let obj = FrequencyTracker()
 * obj.add(number)
 * obj.deleteOne(number)
 * let ret_3: Bool = obj.hasFrequency(frequency)
 */
```

### Kotlin

```kotlin
class FrequencyTracker() {

    fun add(number: Int) {
        
    }

    fun deleteOne(number: Int) {
        
    }

    fun hasFrequency(frequency: Int): Boolean {
        
    }

}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * var obj = FrequencyTracker()
 * obj.add(number)
 * obj.deleteOne(number)
 * var param_3 = obj.hasFrequency(frequency)
 */
```

### Dart

```dart
class FrequencyTracker {

  FrequencyTracker() {
    
  }
  
  void add(int number) {
    
  }
  
  void deleteOne(int number) {
    
  }
  
  bool hasFrequency(int frequency) {
    
  }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * FrequencyTracker obj = FrequencyTracker();
 * obj.add(number);
 * obj.deleteOne(number);
 * bool param3 = obj.hasFrequency(frequency);
 */
```

### Go

```golang
type FrequencyTracker struct {
    
}


func Constructor() FrequencyTracker {
    
}


func (this *FrequencyTracker) Add(number int)  {
    
}


func (this *FrequencyTracker) DeleteOne(number int)  {
    
}


func (this *FrequencyTracker) HasFrequency(frequency int) bool {
    
}


/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(number);
 * obj.DeleteOne(number);
 * param_3 := obj.HasFrequency(frequency);
 */
```

### Ruby

```ruby
class FrequencyTracker
    def initialize()
        
    end


=begin
    :type number: Integer
    :rtype: Void
=end
    def add(number)
        
    end


=begin
    :type number: Integer
    :rtype: Void
=end
    def delete_one(number)
        
    end


=begin
    :type frequency: Integer
    :rtype: Boolean
=end
    def has_frequency(frequency)
        
    end


end

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker.new()
# obj.add(number)
# obj.delete_one(number)
# param_3 = obj.has_frequency(frequency)
```

### Scala

```scala
class FrequencyTracker() {

    def add(number: Int): Unit = {
        
    }

    def deleteOne(number: Int): Unit = {
        
    }

    def hasFrequency(frequency: Int): Boolean = {
        
    }

}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * val obj = new FrequencyTracker()
 * obj.add(number)
 * obj.deleteOne(number)
 * val param_3 = obj.hasFrequency(frequency)
 */
```

### Rust

```rust
struct FrequencyTracker {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FrequencyTracker {

    fn new() -> Self {
        
    }
    
    fn add(&self, number: i32) {
        
    }
    
    fn delete_one(&self, number: i32) {
        
    }
    
    fn has_frequency(&self, frequency: i32) -> bool {
        
    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * let obj = FrequencyTracker::new();
 * obj.add(number);
 * obj.delete_one(number);
 * let ret_3: bool = obj.has_frequency(frequency);
 */
```

### Racket

```racket
(define frequency-tracker%
  (class object%
    (super-new)
    
    (init-field)
    
    ; add : exact-integer? -> void?
    (define/public (add number)
      )
    ; delete-one : exact-integer? -> void?
    (define/public (delete-one number)
      )
    ; has-frequency : exact-integer? -> boolean?
    (define/public (has-frequency frequency)
      )))

;; Your frequency-tracker% object will be instantiated and called as such:
;; (define obj (new frequency-tracker%))
;; (send obj add number)
;; (send obj delete-one number)
;; (define param_3 (send obj has-frequency frequency))
```

### Erlang

```erlang
-spec frequency_tracker_init_() -> any().
frequency_tracker_init_() ->
  .

-spec frequency_tracker_add(Number :: integer()) -> any().
frequency_tracker_add(Number) ->
  .

-spec frequency_tracker_delete_one(Number :: integer()) -> any().
frequency_tracker_delete_one(Number) ->
  .

-spec frequency_tracker_has_frequency(Frequency :: integer()) -> boolean().
frequency_tracker_has_frequency(Frequency) ->
  .


%% Your functions will be called as such:
%% frequency_tracker_init_(),
%% frequency_tracker_add(Number),
%% frequency_tracker_delete_one(Number),
%% Param_3 = frequency_tracker_has_frequency(Frequency),

%% frequency_tracker_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule FrequencyTracker do
  @spec init_() :: any
  def init_() do
    
  end

  @spec add(number :: integer) :: any
  def add(number) do
    
  end

  @spec delete_one(number :: integer) :: any
  def delete_one(number) do
    
  end

  @spec has_frequency(frequency :: integer) :: boolean
  def has_frequency(frequency) do
    
  end
end

# Your functions will be called as such:
# FrequencyTracker.init_()
# FrequencyTracker.add(number)
# FrequencyTracker.delete_one(number)
# param_3 = FrequencyTracker.has_frequency(frequency)

# FrequencyTracker.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class FrequencyTracker {
    init() {

    }
    
    func add(number: Int64): Unit {

    }
    
    func deleteOne(number: Int64): Unit {

    }
    
    func hasFrequency(frequency: Int64): Bool {

    }
}

/**
 * Your FrequencyTracker object will be instantiated and called as such:
 * let obj: FrequencyTracker = FrequencyTracker()
 * obj.add(number)
 * obj.deleteOne(number)
 * let param_3 = obj.hasFrequency(frequency)
 */
```

