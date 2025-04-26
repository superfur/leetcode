# 528. 按权重随机选择

## 题目描述

<p>给你一个 <strong>下标从 0 开始</strong> 的正整数数组&nbsp;<code>w</code> ，其中&nbsp;<code>w[i]</code> 代表第 <code>i</code> 个下标的权重。</p>

<p>请你实现一个函数&nbsp;<code>pickIndex</code>&nbsp;，它可以 <strong>随机地</strong> 从范围 <code>[0, w.length - 1]</code> 内（含 <code>0</code> 和 <code>w.length - 1</code>）选出并返回一个下标。选取下标 <code>i</code>&nbsp;的 <strong>概率</strong> 为 <code>w[i] / sum(w)</code> 。</p>

<ol>
</ol>

<ul>
	<li>例如，对于 <code>w = [1, 3]</code>，挑选下标 <code>0</code> 的概率为 <code>1 / (1 + 3)&nbsp;= 0.25</code> （即，25%），而选取下标 <code>1</code> 的概率为 <code>3 / (1 + 3)&nbsp;= 0.75</code>（即，<code>75%</code>）。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["Solution","pickIndex"]
[[[1]],[]]
<strong>输出：</strong>
[null,0]
<strong>解释：</strong>
Solution solution = new Solution([1]);
solution.pickIndex(); // 返回 0，因为数组中只有一个元素，所以唯一的选择是返回下标 0。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
<strong>输出：</strong>
[null,1,1,1,1,0]
<strong>解释：</strong>
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // 返回 1，返回下标 1，返回该下标概率为 3/4 。
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 0，返回下标 0，返回该下标概率为 1/4 。

由于这是一个随机问题，允许多个答案，因此下列输出都可以被认为是正确的:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
诸若此类。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= w.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= w[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>pickIndex</code>&nbsp;将被调用不超过 <code>10<sup>4</sup></code>&nbsp;次</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 二分查找
- 前缀和
- 随机化

## 示例

```
["Solution","pickIndex"]
[[[1]],[]]
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    Solution(vector<int>& w) {
        
    }
    
    int pickIndex() {
        
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
```

### Java

```java
class Solution {

    public Solution(int[] w) {
        
    }
    
    public int pickIndex() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */
```

### Python

```python
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        

    def pickIndex(self):
        """
        :rtype: int
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```

### Python3

```python3
class Solution:

    def __init__(self, w: List[int]):
        

    def pickIndex(self) -> int:
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```

### C

```c



typedef struct {
    
} Solution;


Solution* solutionCreate(int* w, int wSize) {
    
}

int solutionPickIndex(Solution* obj) {
    
}

void solutionFree(Solution* obj) {
    
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(w, wSize);
 * int param_1 = solutionPickIndex(obj);
 
 * solutionFree(obj);
*/
```

### C#

```csharp
public class Solution {

    public Solution(int[] w) {
        
    }
    
    public int PickIndex() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.PickIndex();
 */
```

### JavaScript

```javascript
/**
 * @param {number[]} w
 */
var Solution = function(w) {
    
};

/**
 * @return {number}
 */
Solution.prototype.pickIndex = function() {
    
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(w)
 * var param_1 = obj.pickIndex()
 */
```

### TypeScript

```typescript
class Solution {
    constructor(w: number[]) {
        
    }

    pickIndex(): number {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(w)
 * var param_1 = obj.pickIndex()
 */
```

### PHP

```php
class Solution {
    /**
     * @param Integer[] $w
     */
    function __construct($w) {
        
    }
  
    /**
     * @return Integer
     */
    function pickIndex() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = Solution($w);
 * $ret_1 = $obj->pickIndex();
 */
```

### Swift

```swift

class Solution {

    init(_ w: [Int]) {
        
    }
    
    func pickIndex() -> Int {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution(w)
 * let ret_1: Int = obj.pickIndex()
 */
```

### Kotlin

```kotlin
class Solution(w: IntArray) {

    fun pickIndex(): Int {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(w)
 * var param_1 = obj.pickIndex()
 */
```

### Dart

```dart
class Solution {

  Solution(List<int> w) {
    
  }
  
  int pickIndex() {
    
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(w);
 * int param1 = obj.pickIndex();
 */
```

### Go

```golang
type Solution struct {
    
}


func Constructor(w []int) Solution {
    
}


func (this *Solution) PickIndex() int {
    
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(w);
 * param_1 := obj.PickIndex();
 */
```

### Ruby

```ruby
class Solution

=begin
    :type w: Integer[]
=end
    def initialize(w)
        
    end


=begin
    :rtype: Integer
=end
    def pick_index()
        
    end


end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(w)
# param_1 = obj.pick_index()
```

### Scala

```scala
class Solution(_w: Array[Int]) {

    def pickIndex(): Int = {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(w)
 * val param_1 = obj.pickIndex()
 */
```

### Rust

```rust
struct Solution {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(w: Vec<i32>) -> Self {
        
    }
    
    fn pick_index(&self) -> i32 {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(w);
 * let ret_1: i32 = obj.pick_index();
 */
```

### Racket

```racket
(define solution%
  (class object%
    (super-new)
    
    ; w : (listof exact-integer?)
    (init-field
      w)
    
    ; pick-index : -> exact-integer?
    (define/public (pick-index)
      )))

;; Your solution% object will be instantiated and called as such:
;; (define obj (new solution% [w w]))
;; (define param_1 (send obj pick-index))
```

### Erlang

```erlang
-spec solution_init_(W :: [integer()]) -> any().
solution_init_(W) ->
  .

-spec solution_pick_index() -> integer().
solution_pick_index() ->
  .


%% Your functions will be called as such:
%% solution_init_(W),
%% Param_1 = solution_pick_index(),

%% solution_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Solution do
  @spec init_(w :: [integer]) :: any
  def init_(w) do
    
  end

  @spec pick_index() :: integer
  def pick_index() do
    
  end
end

# Your functions will be called as such:
# Solution.init_(w)
# param_1 = Solution.pick_index()

# Solution.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Solution {
    init(w: Array<Int64>) {

    }
    
    func pickIndex(): Int64 {

    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj: Solution = Solution(w)
 * let param_1 = obj.pickIndex()
 */
```

