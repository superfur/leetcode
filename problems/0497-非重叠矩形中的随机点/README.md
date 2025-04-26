# 497. 非重叠矩形中的随机点

## 题目描述

<p>给定一个由非重叠的轴对齐矩形的数组 <code>rects</code> ，其中 <code>rects[i] = [ai, bi, xi, yi]</code> 表示 <code>(ai, bi)</code> 是第 <code>i</code> 个矩形的左下角点，<code>(xi, yi)</code> 是第 <code>i</code> 个矩形的右上角点。设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。所有满足要求的点必须等概率被返回。</p>

<p>在给定的矩形覆盖的空间内的任何整数点都有可能被返回。</p>

<p><strong>请注意&nbsp;</strong>，整数点是具有整数坐标的点。</p>

<p>实现&nbsp;<code>Solution</code>&nbsp;类:</p>

<ul>
	<li><code>Solution(int[][] rects)</code>&nbsp;用给定的矩形数组&nbsp;<code>rects</code> 初始化对象。</li>
	<li><code>int[] pick()</code>&nbsp;返回一个随机的整数点 <code>[u, v]</code> 在给定的矩形所覆盖的空间内。</li>
</ul>

<ol>
</ol>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/07/24/lc-pickrandomrec.jpg" style="height: 539px; width: 419px;" /></p>

<pre>
<strong>输入: 
</strong>["Solution", "pick", "pick", "pick", "pick", "pick"]
[[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
<strong>输出: 
</strong>[null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]

<strong>解释：</strong>
Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
solution.pick(); // 返回 [1, -2]
solution.pick(); // 返回 [1, -1]
solution.pick(); // 返回 [-1, -2]
solution.pick(); // 返回 [-2, -2]
solution.pick(); // 返回 [0, 0]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rects.length &lt;= 100</code></li>
	<li><code>rects[i].length == 4</code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= a<sub>i</sub>&nbsp;&lt; x<sub>i</sub>&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= b<sub>i</sub>&nbsp;&lt; y<sub>i</sub>&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>x<sub>i</sub>&nbsp;- a<sub>i</sub>&nbsp;&lt;= 2000</code></li>
	<li><code>y<sub>i</sub>&nbsp;- b<sub>i</sub>&nbsp;&lt;= 2000</code></li>
	<li>所有的矩形不重叠。</li>
	<li><code>pick</code> 最多被调用&nbsp;<code>10<sup>4</sup></code>&nbsp;次。</li>
</ul>


## 难度

Medium

## 标签

- 水塘抽样
- 数组
- 数学
- 二分查找
- 有序集合
- 前缀和
- 随机化

## 示例

```
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,1,1],[2,2,4,6]]],[],[],[],[],[]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    Solution(vector<vector<int>>& rects) {
        
    }
    
    vector<int> pick() {
        
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(rects);
 * vector<int> param_1 = obj->pick();
 */
```

### Java

```java
class Solution {

    public Solution(int[][] rects) {
        
    }
    
    public int[] pick() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(rects);
 * int[] param_1 = obj.pick();
 */
```

### Python

```python
class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        

    def pick(self):
        """
        :rtype: List[int]
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
```

### Python3

```python3
class Solution:

    def __init__(self, rects: List[List[int]]):
        

    def pick(self) -> List[int]:
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
```

### C

```c



typedef struct {
    
} Solution;


Solution* solutionCreate(int** rects, int rectsSize, int* rectsColSize) {
    
}

int* solutionPick(Solution* obj, int* retSize) {
    
}

void solutionFree(Solution* obj) {
    
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(rects, rectsSize, rectsColSize);
 * int* param_1 = solutionPick(obj, retSize);
 
 * solutionFree(obj);
*/
```

### C#

```csharp
public class Solution {

    public Solution(int[][] rects) {
        
    }
    
    public int[] Pick() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(rects);
 * int[] param_1 = obj.Pick();
 */
```

### JavaScript

```javascript
/**
 * @param {number[][]} rects
 */
var Solution = function(rects) {
    
};

/**
 * @return {number[]}
 */
Solution.prototype.pick = function() {
    
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(rects)
 * var param_1 = obj.pick()
 */
```

### TypeScript

```typescript
class Solution {
    constructor(rects: number[][]) {
        
    }

    pick(): number[] {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(rects)
 * var param_1 = obj.pick()
 */
```

### PHP

```php
class Solution {
    /**
     * @param Integer[][] $rects
     */
    function __construct($rects) {
        
    }
  
    /**
     * @return Integer[]
     */
    function pick() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = Solution($rects);
 * $ret_1 = $obj->pick();
 */
```

### Swift

```swift

class Solution {

    init(_ rects: [[Int]]) {
        
    }
    
    func pick() -> [Int] {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution(rects)
 * let ret_1: [Int] = obj.pick()
 */
```

### Kotlin

```kotlin
class Solution(rects: Array<IntArray>) {

    fun pick(): IntArray {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(rects)
 * var param_1 = obj.pick()
 */
```

### Dart

```dart
class Solution {

  Solution(List<List<int>> rects) {
    
  }
  
  List<int> pick() {
    
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(rects);
 * List<int> param1 = obj.pick();
 */
```

### Go

```golang
type Solution struct {
    
}


func Constructor(rects [][]int) Solution {
    
}


func (this *Solution) Pick() []int {
    
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(rects);
 * param_1 := obj.Pick();
 */
```

### Ruby

```ruby
class Solution

=begin
    :type rects: Integer[][]
=end
    def initialize(rects)
        
    end


=begin
    :rtype: Integer[]
=end
    def pick()
        
    end


end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(rects)
# param_1 = obj.pick()
```

### Scala

```scala
class Solution(_rects: Array[Array[Int]]) {

    def pick(): Array[Int] = {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(rects)
 * val param_1 = obj.pick()
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

    fn new(rects: Vec<Vec<i32>>) -> Self {
        
    }
    
    fn pick(&self) -> Vec<i32> {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(rects);
 * let ret_1: Vec<i32> = obj.pick();
 */
```

### Racket

```racket
(define solution%
  (class object%
    (super-new)
    
    ; rects : (listof (listof exact-integer?))
    (init-field
      rects)
    
    ; pick : -> (listof exact-integer?)
    (define/public (pick)
      )))

;; Your solution% object will be instantiated and called as such:
;; (define obj (new solution% [rects rects]))
;; (define param_1 (send obj pick))
```

### Erlang

```erlang
-spec solution_init_(Rects :: [[integer()]]) -> any().
solution_init_(Rects) ->
  .

-spec solution_pick() -> [integer()].
solution_pick() ->
  .


%% Your functions will be called as such:
%% solution_init_(Rects),
%% Param_1 = solution_pick(),

%% solution_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Solution do
  @spec init_(rects :: [[integer]]) :: any
  def init_(rects) do
    
  end

  @spec pick() :: [integer]
  def pick() do
    
  end
end

# Your functions will be called as such:
# Solution.init_(rects)
# param_1 = Solution.pick()

# Solution.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Solution {
    init(rects: Array<Array<Int64>>) {

    }
    
    func pick(): Array<Int64> {

    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj: Solution = Solution(rects)
 * let param_1 = obj.pick()
 */
```

