# 519. 随机翻转矩阵

## 题目描述

<p>给你一个 <code>m x n</code> 的二元矩阵 <code>matrix</code> ，且所有值被初始化为 <code>0</code> 。请你设计一个算法，随机选取一个满足&nbsp;<code>matrix[i][j] == 0</code> 的下标&nbsp;<code>(i, j)</code> ，并将它的值变为 <code>1</code> 。所有满足 <code>matrix[i][j] == 0</code> 的下标 <code>(i, j)</code> 被选取的概率应当均等。</p>

<p>尽量最少调用内置的随机函数，并且优化时间和空间复杂度。</p>

<p>实现 <code>Solution</code> 类：</p>

<ul>
	<li><code>Solution(int m, int n)</code> 使用二元矩阵的大小 <code>m</code> 和 <code>n</code> 初始化该对象</li>
	<li><code>int[] flip()</code> 返回一个满足&nbsp;<code>matrix[i][j] == 0</code> 的随机下标 <code>[i, j]</code> ，并将其对应格子中的值变为 <code>1</code></li>
	<li><code>void reset()</code> 将矩阵中所有的值重置为 <code>0</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>
["Solution", "flip", "flip", "flip", "reset", "flip"]
[[3, 1], [], [], [], [], []]
<strong>输出</strong>
[null, [1, 0], [2, 0], [0, 0], null, [2, 0]]

<strong>解释</strong>
Solution solution = new Solution(3, 1);
solution.flip();  // 返回 [1, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同
solution.flip();  // 返回 [2, 0]，因为 [1,0] 已经返回过了，此时返回 [2,0] 和 [0,0] 的概率应当相同
solution.flip();  // 返回 [0, 0]，根据前面已经返回过的下标，此时只能返回 [0,0]
solution.reset(); // 所有值都重置为 0 ，并可以再次选择下标返回
solution.flip();  // 返回 [2, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 10<sup>4</sup></code></li>
	<li>每次调用<code>flip</code> 时，矩阵中至少存在一个值为 0 的格子。</li>
	<li>最多调用 <code>1000</code> 次 <code>flip</code> 和 <code>reset</code> 方法。</li>
</ul>


## 难度

Medium

## 标签

- 水塘抽样
- 哈希表
- 数学
- 随机化

## 示例

```
["Solution","flip","flip","flip","reset","flip"]
[[3,1],[],[],[],[],[]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    Solution(int m, int n) {
        
    }
    
    vector<int> flip() {
        
    }
    
    void reset() {
        
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(m, n);
 * vector<int> param_1 = obj->flip();
 * obj->reset();
 */
```

### Java

```java
class Solution {

    public Solution(int m, int n) {
        
    }
    
    public int[] flip() {
        
    }
    
    public void reset() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(m, n);
 * int[] param_1 = obj.flip();
 * obj.reset();
 */
```

### Python

```python
class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        

    def flip(self):
        """
        :rtype: List[int]
        """
        

    def reset(self):
        """
        :rtype: None
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
```

### Python3

```python3
class Solution:

    def __init__(self, m: int, n: int):
        

    def flip(self) -> List[int]:
        

    def reset(self) -> None:
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
```

### C

```c



typedef struct {
    
} Solution;


Solution* solutionCreate(int m, int n) {
    
}

int* solutionFlip(Solution* obj, int* retSize) {
    
}

void solutionReset(Solution* obj) {
    
}

void solutionFree(Solution* obj) {
    
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(m, n);
 * int* param_1 = solutionFlip(obj, retSize);
 
 * solutionReset(obj);
 
 * solutionFree(obj);
*/
```

### C#

```csharp
public class Solution {

    public Solution(int m, int n) {
        
    }
    
    public int[] Flip() {
        
    }
    
    public void Reset() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(m, n);
 * int[] param_1 = obj.Flip();
 * obj.Reset();
 */
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 */
var Solution = function(m, n) {
    
};

/**
 * @return {number[]}
 */
Solution.prototype.flip = function() {
    
};

/**
 * @return {void}
 */
Solution.prototype.reset = function() {
    
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(m, n)
 * var param_1 = obj.flip()
 * obj.reset()
 */
```

### TypeScript

```typescript
class Solution {
    constructor(m: number, n: number) {
        
    }

    flip(): number[] {
        
    }

    reset(): void {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(m, n)
 * var param_1 = obj.flip()
 * obj.reset()
 */
```

### PHP

```php
class Solution {
    /**
     * @param Integer $m
     * @param Integer $n
     */
    function __construct($m, $n) {
        
    }
  
    /**
     * @return Integer[]
     */
    function flip() {
        
    }
  
    /**
     * @return NULL
     */
    function reset() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = Solution($m, $n);
 * $ret_1 = $obj->flip();
 * $obj->reset();
 */
```

### Swift

```swift

class Solution {

    init(_ m: Int, _ n: Int) {
        
    }
    
    func flip() -> [Int] {
        
    }
    
    func reset() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution(m, n)
 * let ret_1: [Int] = obj.flip()
 * obj.reset()
 */
```

### Kotlin

```kotlin
class Solution(m: Int, n: Int) {

    fun flip(): IntArray {
        
    }

    fun reset() {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(m, n)
 * var param_1 = obj.flip()
 * obj.reset()
 */
```

### Dart

```dart
class Solution {

  Solution(int m, int n) {
    
  }
  
  List<int> flip() {
    
  }
  
  void reset() {
    
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(m, n);
 * List<int> param1 = obj.flip();
 * obj.reset();
 */
```

### Go

```golang
type Solution struct {
    
}


func Constructor(m int, n int) Solution {
    
}


func (this *Solution) Flip() []int {
    
}


func (this *Solution) Reset()  {
    
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(m, n);
 * param_1 := obj.Flip();
 * obj.Reset();
 */
```

### Ruby

```ruby
class Solution

=begin
    :type m: Integer
    :type n: Integer
=end
    def initialize(m, n)
        
    end


=begin
    :rtype: Integer[]
=end
    def flip()
        
    end


=begin
    :rtype: Void
=end
    def reset()
        
    end


end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(m, n)
# param_1 = obj.flip()
# obj.reset()
```

### Scala

```scala
class Solution(_m: Int, _n: Int) {

    def flip(): Array[Int] = {
        
    }

    def reset(): Unit = {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(m, n)
 * val param_1 = obj.flip()
 * obj.reset()
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

    fn new(m: i32, n: i32) -> Self {
        
    }
    
    fn flip(&self) -> Vec<i32> {
        
    }
    
    fn reset(&self) {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(m, n);
 * let ret_1: Vec<i32> = obj.flip();
 * obj.reset();
 */
```

### Racket

```racket
(define solution%
  (class object%
    (super-new)
    
    ; m : exact-integer?
    ; n : exact-integer?
    (init-field
      m
      n)
    
    ; flip : -> (listof exact-integer?)
    (define/public (flip)
      )
    ; reset : -> void?
    (define/public (reset)
      )))

;; Your solution% object will be instantiated and called as such:
;; (define obj (new solution% [m m] [n n]))
;; (define param_1 (send obj flip))
;; (send obj reset)
```

### Erlang

```erlang
-spec solution_init_(M :: integer(), N :: integer()) -> any().
solution_init_(M, N) ->
  .

-spec solution_flip() -> [integer()].
solution_flip() ->
  .

-spec solution_reset() -> any().
solution_reset() ->
  .


%% Your functions will be called as such:
%% solution_init_(M, N),
%% Param_1 = solution_flip(),
%% solution_reset(),

%% solution_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Solution do
  @spec init_(m :: integer, n :: integer) :: any
  def init_(m, n) do
    
  end

  @spec flip() :: [integer]
  def flip() do
    
  end

  @spec reset() :: any
  def reset() do
    
  end
end

# Your functions will be called as such:
# Solution.init_(m, n)
# param_1 = Solution.flip()
# Solution.reset()

# Solution.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Solution {
    init(m: Int64, n: Int64) {

    }
    
    func flip(): Array<Int64> {

    }
    
    func reset(): Unit {

    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj: Solution = Solution(m, n)
 * let param_1 = obj.flip()
 * obj.reset()
 */
```

