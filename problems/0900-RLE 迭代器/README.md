# 900. RLE 迭代器

## 题目描述

<p>我们可以使用游程编码(即&nbsp;<strong>RLE&nbsp;</strong>)来编码一个整数序列。在偶数长度&nbsp;<code>encoding</code>&nbsp;( <strong>从 0 开始</strong> )的游程编码数组中，对于所有偶数 <code>i</code> ，<code>encoding[i]</code>&nbsp;告诉我们非负整数&nbsp;<code>encoding[i + 1]</code>&nbsp;在序列中重复的次数。</p>

<ul>
	<li>例如，序列&nbsp;<code>arr = [8,8,8,5,5]</code>&nbsp;可以被编码为 <code>encoding =[3,8,2,5]</code> 。<code>encoding =[3,8,0,9,2,5]</code>&nbsp;和 <code>encoding =[2,8,1,8,2,5]</code> 也是&nbsp;<code>arr</code> 有效的 <strong>RLE</strong> 。</li>
</ul>

<p>给定一个游程长度的编码数组，设计一个迭代器来遍历它。</p>

<p>实现 <code>RLEIterator</code> 类:</p>

<ul>
	<li><code>RLEIterator(int[] encoded)</code>&nbsp;用编码后的数组初始化对象。</li>
	<li><code>int next(int n)</code> 以这种方式耗尽后 <code>n</code> 个元素并返回最后一个耗尽的元素。如果没有剩余的元素要耗尽，则返回 <code>-1</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：
</strong>["RLEIterator","next","next","next","next"]
[[[3,8,0,9,2,5]],[2],[1],[1],[2]]
<strong>输出：
</strong>[null,8,8,5,-1]
<strong>解释：</strong>
RLEIterator rLEIterator = new RLEIterator([3, 8, 0, 9, 2, 5]); // 这映射到序列 [8,8,8,5,5]。
rLEIterator.next(2); // 耗去序列的 2 个项，返回 8。现在剩下的序列是 [8, 5, 5]。
rLEIterator.next(1); // 耗去序列的 1 个项，返回 8。现在剩下的序列是 [5, 5]。
rLEIterator.next(1); // 耗去序列的 1 个项，返回 5。现在剩下的序列是 [5]。
rLEIterator.next(2); // 耗去序列的 2 个项，返回 -1。 这是由于第一个被耗去的项是 5，
但第二个项并不存在。由于最后一个要耗去的项不存在，我们返回 -1。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= encoding.length &lt;= 1000</code></li>
	<li><code>encoding.length</code>&nbsp;为偶</li>
	<li><code>0 &lt;= encoding[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li>每个测试用例调用<code>next </code>不高于&nbsp;<code>1000</code>&nbsp;次&nbsp;</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 计数
- 迭代器

## 示例

```
["RLEIterator","next","next","next","next"]
[[[3,8,0,9,2,5]],[2],[1],[1],[2]]
```

## 示例代码

### C++

```cpp
class RLEIterator {
public:
    RLEIterator(vector<int>& encoding) {
        
    }
    
    int next(int n) {
        
    }
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator* obj = new RLEIterator(encoding);
 * int param_1 = obj->next(n);
 */
```

### Java

```java
class RLEIterator {

    public RLEIterator(int[] encoding) {
        
    }
    
    public int next(int n) {
        
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = new RLEIterator(encoding);
 * int param_1 = obj.next(n);
 */
```

### Python

```python
class RLEIterator(object):

    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
```

### Python3

```python3
class RLEIterator:

    def __init__(self, encoding: List[int]):
        

    def next(self, n: int) -> int:
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
```

### C

```c



typedef struct {
    
} RLEIterator;


RLEIterator* rLEIteratorCreate(int* encoding, int encodingSize) {
    
}

int rLEIteratorNext(RLEIterator* obj, int n) {
    
}

void rLEIteratorFree(RLEIterator* obj) {
    
}

/**
 * Your RLEIterator struct will be instantiated and called as such:
 * RLEIterator* obj = rLEIteratorCreate(encoding, encodingSize);
 * int param_1 = rLEIteratorNext(obj, n);
 
 * rLEIteratorFree(obj);
*/
```

### C#

```csharp
public class RLEIterator {

    public RLEIterator(int[] encoding) {
        
    }
    
    public int Next(int n) {
        
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = new RLEIterator(encoding);
 * int param_1 = obj.Next(n);
 */
```

### JavaScript

```javascript
/**
 * @param {number[]} encoding
 */
var RLEIterator = function(encoding) {
    
};

/** 
 * @param {number} n
 * @return {number}
 */
RLEIterator.prototype.next = function(n) {
    
};

/** 
 * Your RLEIterator object will be instantiated and called as such:
 * var obj = new RLEIterator(encoding)
 * var param_1 = obj.next(n)
 */
```

### TypeScript

```typescript
class RLEIterator {
    constructor(encoding: number[]) {
        
    }

    next(n: number): number {
        
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * var obj = new RLEIterator(encoding)
 * var param_1 = obj.next(n)
 */
```

### PHP

```php
class RLEIterator {
    /**
     * @param Integer[] $encoding
     */
    function __construct($encoding) {
        
    }
  
    /**
     * @param Integer $n
     * @return Integer
     */
    function next($n) {
        
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * $obj = RLEIterator($encoding);
 * $ret_1 = $obj->next($n);
 */
```

### Swift

```swift

class RLEIterator {

    init(_ encoding: [Int]) {
        
    }
    
    func next(_ n: Int) -> Int {
        
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * let obj = RLEIterator(encoding)
 * let ret_1: Int = obj.next(n)
 */
```

### Kotlin

```kotlin
class RLEIterator(encoding: IntArray) {

    fun next(n: Int): Int {
        
    }

}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * var obj = RLEIterator(encoding)
 * var param_1 = obj.next(n)
 */
```

### Dart

```dart
class RLEIterator {

  RLEIterator(List<int> encoding) {
    
  }
  
  int next(int n) {
    
  }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = RLEIterator(encoding);
 * int param1 = obj.next(n);
 */
```

### Go

```golang
type RLEIterator struct {
    
}


func Constructor(encoding []int) RLEIterator {
    
}


func (this *RLEIterator) Next(n int) int {
    
}


/**
 * Your RLEIterator object will be instantiated and called as such:
 * obj := Constructor(encoding);
 * param_1 := obj.Next(n);
 */
```

### Ruby

```ruby
class RLEIterator

=begin
    :type encoding: Integer[]
=end
    def initialize(encoding)
        
    end


=begin
    :type n: Integer
    :rtype: Integer
=end
    def next(n)
        
    end


end

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator.new(encoding)
# param_1 = obj.next(n)
```

### Scala

```scala
class RLEIterator(_encoding: Array[Int]) {

    def next(n: Int): Int = {
        
    }

}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * val obj = new RLEIterator(encoding)
 * val param_1 = obj.next(n)
 */
```

### Rust

```rust
struct RLEIterator {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RLEIterator {

    fn new(encoding: Vec<i32>) -> Self {
        
    }
    
    fn next(&self, n: i32) -> i32 {
        
    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * let obj = RLEIterator::new(encoding);
 * let ret_1: i32 = obj.next(n);
 */
```

### Racket

```racket
(define rle-iterator%
  (class object%
    (super-new)
    
    ; encoding : (listof exact-integer?)
    (init-field
      encoding)
    
    ; next : exact-integer? -> exact-integer?
    (define/public (next n)
      )))

;; Your rle-iterator% object will be instantiated and called as such:
;; (define obj (new rle-iterator% [encoding encoding]))
;; (define param_1 (send obj next n))
```

### Erlang

```erlang
-spec rle_iterator_init_(Encoding :: [integer()]) -> any().
rle_iterator_init_(Encoding) ->
  .

-spec rle_iterator_next(N :: integer()) -> integer().
rle_iterator_next(N) ->
  .


%% Your functions will be called as such:
%% rle_iterator_init_(Encoding),
%% Param_1 = rle_iterator_next(N),

%% rle_iterator_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule RLEIterator do
  @spec init_(encoding :: [integer]) :: any
  def init_(encoding) do
    
  end

  @spec next(n :: integer) :: integer
  def next(n) do
    
  end
end

# Your functions will be called as such:
# RLEIterator.init_(encoding)
# param_1 = RLEIterator.next(n)

# RLEIterator.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class RLEIterator {
    init(encoding: Array<Int64>) {

    }
    
    func next(n: Int64): Int64 {

    }
}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * let obj: RLEIterator = RLEIterator(encoding)
 * let param_1 = obj.next(n)
 */
```

