# 911. 在线选举

## 题目描述

<p>给你两个整数数组 <code>persons</code> 和 <code>times</code> 。在选举中，第&nbsp;<code>i</code>&nbsp;张票是在时刻为&nbsp;<code>times[i]</code>&nbsp;时投给候选人 <code>persons[i]</code>&nbsp;的。</p>

<p>对于发生在时刻 <code>t</code> 的每个查询，需要找出在&nbsp;<code>t</code> 时刻在选举中领先的候选人的编号。</p>

<p>在&nbsp;<code>t</code> 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。</p>

<p>实现 <code>TopVotedCandidate</code> 类：</p>

<ul>
	<li><code>TopVotedCandidate(int[] persons, int[] times)</code> 使用&nbsp;<code>persons</code> 和 <code>times</code> 数组初始化对象。</li>
	<li><code>int q(int t)</code> 根据前面描述的规则，返回在时刻 <code>t</code> 在选举中领先的候选人的编号。</li>
</ul>
&nbsp;

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
<strong>输出：</strong>
[null, 0, 1, 1, 0, 0, 1]

<strong>解释：</strong>
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // 返回 0 ，在时刻 3 ，票数分布为 [0] ，编号为 0 的候选人领先。
topVotedCandidate.q(12); // 返回 1 ，在时刻 12 ，票数分布为 [0,1,1] ，编号为 1 的候选人领先。
topVotedCandidate.q(25); // 返回 1 ，在时刻 25 ，票数分布为 [0,1,1,0,0,1] ，编号为 1 的候选人领先。（在平局的情况下，1 是最近获得投票的候选人）。
topVotedCandidate.q(15); // 返回 0
topVotedCandidate.q(24); // 返回 0
topVotedCandidate.q(8); // 返回 1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= persons.length &lt;= 5000</code></li>
	<li><code>times.length == persons.length</code></li>
	<li><code>0 &lt;= persons[i] &lt; persons.length</code></li>
	<li><code>0 &lt;= times[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>times</code> 是一个严格递增的有序数组</li>
	<li><code>times[0] &lt;= t &lt;= 10<sup>9</sup></code></li>
	<li>每个测试用例最多调用 <code>10<sup>4</sup></code> 次 <code>q</code></li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 哈希表
- 二分查找

## 示例

```
["TopVotedCandidate","q","q","q","q","q","q"]
[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
```

## 示例代码

### C++

```cpp
class TopVotedCandidate {
public:
    TopVotedCandidate(vector<int>& persons, vector<int>& times) {
        
    }
    
    int q(int t) {
        
    }
};

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate* obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj->q(t);
 */
```

### Java

```java
class TopVotedCandidate {

    public TopVotedCandidate(int[] persons, int[] times) {
        
    }
    
    public int q(int t) {
        
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.q(t);
 */
```

### Python

```python
class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
```

### Python3

```python3
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        

    def q(self, t: int) -> int:
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
```

### C

```c



typedef struct {
    
} TopVotedCandidate;


TopVotedCandidate* topVotedCandidateCreate(int* persons, int personsSize, int* times, int timesSize) {
    
}

int topVotedCandidateQ(TopVotedCandidate* obj, int t) {
    
}

void topVotedCandidateFree(TopVotedCandidate* obj) {
    
}

/**
 * Your TopVotedCandidate struct will be instantiated and called as such:
 * TopVotedCandidate* obj = topVotedCandidateCreate(persons, personsSize, times, timesSize);
 * int param_1 = topVotedCandidateQ(obj, t);
 
 * topVotedCandidateFree(obj);
*/
```

### C#

```csharp
public class TopVotedCandidate {

    public TopVotedCandidate(int[] persons, int[] times) {
        
    }
    
    public int Q(int t) {
        
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.Q(t);
 */
```

### JavaScript

```javascript
/**
 * @param {number[]} persons
 * @param {number[]} times
 */
var TopVotedCandidate = function(persons, times) {
    
};

/** 
 * @param {number} t
 * @return {number}
 */
TopVotedCandidate.prototype.q = function(t) {
    
};

/** 
 * Your TopVotedCandidate object will be instantiated and called as such:
 * var obj = new TopVotedCandidate(persons, times)
 * var param_1 = obj.q(t)
 */
```

### TypeScript

```typescript
class TopVotedCandidate {
    constructor(persons: number[], times: number[]) {
        
    }

    q(t: number): number {
        
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * var obj = new TopVotedCandidate(persons, times)
 * var param_1 = obj.q(t)
 */
```

### PHP

```php
class TopVotedCandidate {
    /**
     * @param Integer[] $persons
     * @param Integer[] $times
     */
    function __construct($persons, $times) {
        
    }
  
    /**
     * @param Integer $t
     * @return Integer
     */
    function q($t) {
        
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * $obj = TopVotedCandidate($persons, $times);
 * $ret_1 = $obj->q($t);
 */
```

### Swift

```swift

class TopVotedCandidate {

    init(_ persons: [Int], _ times: [Int]) {
        
    }
    
    func q(_ t: Int) -> Int {
        
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * let obj = TopVotedCandidate(persons, times)
 * let ret_1: Int = obj.q(t)
 */
```

### Kotlin

```kotlin
class TopVotedCandidate(persons: IntArray, times: IntArray) {

    fun q(t: Int): Int {
        
    }

}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * var obj = TopVotedCandidate(persons, times)
 * var param_1 = obj.q(t)
 */
```

### Dart

```dart
class TopVotedCandidate {

  TopVotedCandidate(List<int> persons, List<int> times) {
    
  }
  
  int q(int t) {
    
  }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = TopVotedCandidate(persons, times);
 * int param1 = obj.q(t);
 */
```

### Go

```golang
type TopVotedCandidate struct {
    
}


func Constructor(persons []int, times []int) TopVotedCandidate {
    
}


func (this *TopVotedCandidate) Q(t int) int {
    
}


/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * obj := Constructor(persons, times);
 * param_1 := obj.Q(t);
 */
```

### Ruby

```ruby
class TopVotedCandidate

=begin
    :type persons: Integer[]
    :type times: Integer[]
=end
    def initialize(persons, times)
        
    end


=begin
    :type t: Integer
    :rtype: Integer
=end
    def q(t)
        
    end


end

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate.new(persons, times)
# param_1 = obj.q(t)
```

### Scala

```scala
class TopVotedCandidate(_persons: Array[Int], _times: Array[Int]) {

    def q(t: Int): Int = {
        
    }

}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * val obj = new TopVotedCandidate(persons, times)
 * val param_1 = obj.q(t)
 */
```

### Rust

```rust
struct TopVotedCandidate {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TopVotedCandidate {

    fn new(persons: Vec<i32>, times: Vec<i32>) -> Self {
        
    }
    
    fn q(&self, t: i32) -> i32 {
        
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * let obj = TopVotedCandidate::new(persons, times);
 * let ret_1: i32 = obj.q(t);
 */
```

### Racket

```racket
(define top-voted-candidate%
  (class object%
    (super-new)
    
    ; persons : (listof exact-integer?)
    ; times : (listof exact-integer?)
    (init-field
      persons
      times)
    
    ; q : exact-integer? -> exact-integer?
    (define/public (q t)
      )))

;; Your top-voted-candidate% object will be instantiated and called as such:
;; (define obj (new top-voted-candidate% [persons persons] [times times]))
;; (define param_1 (send obj q t))
```

### Erlang

```erlang
-spec top_voted_candidate_init_(Persons :: [integer()], Times :: [integer()]) -> any().
top_voted_candidate_init_(Persons, Times) ->
  .

-spec top_voted_candidate_q(T :: integer()) -> integer().
top_voted_candidate_q(T) ->
  .


%% Your functions will be called as such:
%% top_voted_candidate_init_(Persons, Times),
%% Param_1 = top_voted_candidate_q(T),

%% top_voted_candidate_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule TopVotedCandidate do
  @spec init_(persons :: [integer], times :: [integer]) :: any
  def init_(persons, times) do
    
  end

  @spec q(t :: integer) :: integer
  def q(t) do
    
  end
end

# Your functions will be called as such:
# TopVotedCandidate.init_(persons, times)
# param_1 = TopVotedCandidate.q(t)

# TopVotedCandidate.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class TopVotedCandidate {
    init(persons: Array<Int64>, times: Array<Int64>) {

    }
    
    func q(t: Int64): Int64 {

    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * let obj: TopVotedCandidate = TopVotedCandidate(persons, times)
 * let param_1 = obj.q(t)
 */
```

