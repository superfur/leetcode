# 2349. 设计数字容器系统

## 题目描述

<p>设计一个数字容器系统，可以实现以下功能：</p>

<ul>
	<li>在系统中给定下标处&nbsp;<strong>插入</strong>&nbsp;或者 <strong>替换</strong>&nbsp;一个数字。</li>
	<li><strong>返回</strong>&nbsp;系统中给定数字的最小下标。</li>
</ul>

<p>请你实现一个&nbsp;<code>NumberContainers</code>&nbsp;类：</p>

<ul>
	<li><code>NumberContainers()</code>&nbsp;初始化数字容器系统。</li>
	<li><code>void change(int index, int number)</code> 在下标&nbsp;<code>index</code>&nbsp;处填入&nbsp;<code>number</code>&nbsp;。如果该下标&nbsp;<code>index</code>&nbsp;处已经有数字了，那么用 <code>number</code>&nbsp;替换该数字。</li>
	<li><code>int find(int number)</code>&nbsp;返回给定数字&nbsp;<code>number</code>&nbsp;在系统中的最小下标。如果系统中没有&nbsp;<code>number</code>&nbsp;，那么返回&nbsp;<code>-1</code>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
<strong>输出：</strong>
[null, -1, null, null, null, null, 1, null, 2]

<strong>解释：</strong>
NumberContainers nc = new NumberContainers();
nc.find(10); // 没有数字 10 ，所以返回 -1 。
nc.change(2, 10); // 容器中下标为 2 处填入数字 10 。
nc.change(1, 10); // 容器中下标为 1 处填入数字 10 。
nc.change(3, 10); // 容器中下标为 3 处填入数字 10 。
nc.change(5, 10); // 容器中下标为 5 处填入数字 10 。
nc.find(10); // 数字 10 所在的下标为 1 ，2 ，3 和 5 。因为最小下标为 1 ，所以返回 1 。
nc.change(1, 20); // 容器中下标为 1 处填入数字 20 。注意，下标 1 处之前为 10 ，现在被替换为 20 。
nc.find(10); // 数字 10 所在下标为 2 ，3 和 5 。最小下标为 2 ，所以返回 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= index, number &lt;= 10<sup>9</sup></code></li>
	<li>调用&nbsp;<code>change</code> 和&nbsp;<code>find</code>&nbsp;的&nbsp;<strong>总次数</strong>&nbsp;不超过&nbsp;<code>10<sup>5</sup></code> 次。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 哈希表
- 有序集合
- 堆（优先队列）

## 提示

1. Use a hash table to efficiently map each number to all of its indices in the container and to map each index to their current number.
2. In addition, you can use ordered set to store all of the indices for each number to solve the find method. Do not forget to update the ordered set according to the change method.

## 示例

```
["NumberContainers","find","change","change","change","change","find","change","find"]
[[],[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]]
```

## 示例代码

### C++

```cpp
class NumberContainers {
public:
    NumberContainers() {
        
    }
    
    void change(int index, int number) {
        
    }
    
    int find(int number) {
        
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
```

### Java

```java
class NumberContainers {

    public NumberContainers() {
        
    }
    
    public void change(int index, int number) {
        
    }
    
    public int find(int number) {
        
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.change(index,number);
 * int param_2 = obj.find(number);
 */
```

### Python

```python
class NumberContainers(object):

    def __init__(self):
        

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        

    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
```

### Python3

```python3
class NumberContainers:

    def __init__(self):
        

    def change(self, index: int, number: int) -> None:
        

    def find(self, number: int) -> int:
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
```

### C

```c



typedef struct {
    
} NumberContainers;


NumberContainers* numberContainersCreate() {
    
}

void numberContainersChange(NumberContainers* obj, int index, int number) {
    
}

int numberContainersFind(NumberContainers* obj, int number) {
    
}

void numberContainersFree(NumberContainers* obj) {
    
}

/**
 * Your NumberContainers struct will be instantiated and called as such:
 * NumberContainers* obj = numberContainersCreate();
 * numberContainersChange(obj, index, number);
 
 * int param_2 = numberContainersFind(obj, number);
 
 * numberContainersFree(obj);
*/
```

### C#

```csharp
public class NumberContainers {

    public NumberContainers() {
        
    }
    
    public void Change(int index, int number) {
        
    }
    
    public int Find(int number) {
        
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.Change(index,number);
 * int param_2 = obj.Find(number);
 */
```

### JavaScript

```javascript

var NumberContainers = function() {
    
};

/** 
 * @param {number} index 
 * @param {number} number
 * @return {void}
 */
NumberContainers.prototype.change = function(index, number) {
    
};

/** 
 * @param {number} number
 * @return {number}
 */
NumberContainers.prototype.find = function(number) {
    
};

/** 
 * Your NumberContainers object will be instantiated and called as such:
 * var obj = new NumberContainers()
 * obj.change(index,number)
 * var param_2 = obj.find(number)
 */
```

### TypeScript

```typescript
class NumberContainers {
    constructor() {
        
    }

    change(index: number, number: number): void {
        
    }

    find(number: number): number {
        
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * var obj = new NumberContainers()
 * obj.change(index,number)
 * var param_2 = obj.find(number)
 */
```

### PHP

```php
class NumberContainers {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $index
     * @param Integer $number
     * @return NULL
     */
    function change($index, $number) {
        
    }
  
    /**
     * @param Integer $number
     * @return Integer
     */
    function find($number) {
        
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * $obj = NumberContainers();
 * $obj->change($index, $number);
 * $ret_2 = $obj->find($number);
 */
```

### Swift

```swift

class NumberContainers {

    init() {
        
    }
    
    func change(_ index: Int, _ number: Int) {
        
    }
    
    func find(_ number: Int) -> Int {
        
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * let obj = NumberContainers()
 * obj.change(index, number)
 * let ret_2: Int = obj.find(number)
 */
```

### Kotlin

```kotlin
class NumberContainers() {

    fun change(index: Int, number: Int) {
        
    }

    fun find(number: Int): Int {
        
    }

}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * var obj = NumberContainers()
 * obj.change(index,number)
 * var param_2 = obj.find(number)
 */
```

### Dart

```dart
class NumberContainers {

  NumberContainers() {
    
  }
  
  void change(int index, int number) {
    
  }
  
  int find(int number) {
    
  }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = NumberContainers();
 * obj.change(index,number);
 * int param2 = obj.find(number);
 */
```

### Go

```golang
type NumberContainers struct {
    
}


func Constructor() NumberContainers {
    
}


func (this *NumberContainers) Change(index int, number int)  {
    
}


func (this *NumberContainers) Find(number int) int {
    
}


/**
 * Your NumberContainers object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Change(index,number);
 * param_2 := obj.Find(number);
 */
```

### Ruby

```ruby
class NumberContainers
    def initialize()
        
    end


=begin
    :type index: Integer
    :type number: Integer
    :rtype: Void
=end
    def change(index, number)
        
    end


=begin
    :type number: Integer
    :rtype: Integer
=end
    def find(number)
        
    end


end

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers.new()
# obj.change(index, number)
# param_2 = obj.find(number)
```

### Scala

```scala
class NumberContainers() {

    def change(index: Int, number: Int): Unit = {
        
    }

    def find(number: Int): Int = {
        
    }

}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * val obj = new NumberContainers()
 * obj.change(index,number)
 * val param_2 = obj.find(number)
 */
```

### Rust

```rust
struct NumberContainers {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumberContainers {

    fn new() -> Self {
        
    }
    
    fn change(&self, index: i32, number: i32) {
        
    }
    
    fn find(&self, number: i32) -> i32 {
        
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * let obj = NumberContainers::new();
 * obj.change(index, number);
 * let ret_2: i32 = obj.find(number);
 */
```

### Racket

```racket
(define number-containers%
  (class object%
    (super-new)
    
    (init-field)
    
    ; change : exact-integer? exact-integer? -> void?
    (define/public (change index number)
      )
    ; find : exact-integer? -> exact-integer?
    (define/public (find number)
      )))

;; Your number-containers% object will be instantiated and called as such:
;; (define obj (new number-containers%))
;; (send obj change index number)
;; (define param_2 (send obj find number))
```

### Erlang

```erlang
-spec number_containers_init_() -> any().
number_containers_init_() ->
  .

-spec number_containers_change(Index :: integer(), Number :: integer()) -> any().
number_containers_change(Index, Number) ->
  .

-spec number_containers_find(Number :: integer()) -> integer().
number_containers_find(Number) ->
  .


%% Your functions will be called as such:
%% number_containers_init_(),
%% number_containers_change(Index, Number),
%% Param_2 = number_containers_find(Number),

%% number_containers_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule NumberContainers do
  @spec init_() :: any
  def init_() do
    
  end

  @spec change(index :: integer, number :: integer) :: any
  def change(index, number) do
    
  end

  @spec find(number :: integer) :: integer
  def find(number) do
    
  end
end

# Your functions will be called as such:
# NumberContainers.init_()
# NumberContainers.change(index, number)
# param_2 = NumberContainers.find(number)

# NumberContainers.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class NumberContainers {
    init() {

    }
    
    func change(index: Int64, number: Int64): Unit {

    }
    
    func find(number: Int64): Int64 {

    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * let obj: NumberContainers = NumberContainers()
 * obj.change(index,number)
 * let param_2 = obj.find(number)
 */
```

