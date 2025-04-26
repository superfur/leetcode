# 710. 黑名单中的随机数

## 题目描述

<p>给定一个整数 <code>n</code> 和一个 <strong>无重复</strong> 黑名单整数数组&nbsp;<code>blacklist</code>&nbsp;。设计一种算法，从 <code>[0, n - 1]</code> 范围内的任意整数中选取一个&nbsp;<strong>未加入&nbsp;</strong>黑名单&nbsp;<code>blacklist</code>&nbsp;的整数。任何在上述范围内且不在黑名单&nbsp;<code>blacklist</code>&nbsp;中的整数都应该有 <strong>同等的可能性</strong> 被返回。</p>

<p>优化你的算法，使它最小化调用语言 <strong>内置</strong> 随机函数的次数。</p>

<p>实现&nbsp;<code>Solution</code>&nbsp;类:</p>

<ul>
	<li><code>Solution(int n, int[] blacklist)</code>&nbsp;初始化整数 <code>n</code> 和被加入黑名单&nbsp;<code>blacklist</code>&nbsp;的整数</li>
	<li><code>int pick()</code>&nbsp;返回一个范围为 <code>[0, n - 1]</code> 且不在黑名单&nbsp;<code>blacklist</code> 中的随机整数</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入</strong>
["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
[[7, [2, 3, 5]], [], [], [], [], [], [], []]
<strong>输出</strong>
[null, 0, 4, 1, 6, 1, 0, 4]

<b>解释
</b>Solution solution = new Solution(7, [2, 3, 5]);
solution.pick(); // 返回0，任何[0,1,4,6]的整数都可以。注意，对于每一个pick的调用，
                 // 0、1、4和6的返回概率必须相等(即概率为1/4)。
solution.pick(); // 返回 4
solution.pick(); // 返回 1
solution.pick(); // 返回 6
solution.pick(); // 返回 1
solution.pick(); // 返回 0
solution.pick(); // 返回 4
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= blacklist.length &lt;= min(10<sup>5</sup>, n - 1)</code></li>
	<li><code>0 &lt;= blacklist[i] &lt; n</code></li>
	<li><code>blacklist</code>&nbsp;中所有值都 <strong>不同</strong></li>
	<li>&nbsp;<code>pick</code>&nbsp;最多被调用&nbsp;<code>2 * 10<sup>4</sup></code>&nbsp;次</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 数学
- 二分查找
- 排序
- 随机化

## 示例

```
["Solution","pick","pick","pick","pick","pick","pick","pick"]
[[7,[2,3,5]],[],[],[],[],[],[],[]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    Solution(int n, vector<int>& blacklist) {
        
    }
    
    int pick() {
        
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(n, blacklist);
 * int param_1 = obj->pick();
 */
```

### Java

```java
class Solution {

    public Solution(int n, int[] blacklist) {
        
    }
    
    public int pick() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(n, blacklist);
 * int param_1 = obj.pick();
 */
```

### Python

```python
class Solution(object):

    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        

    def pick(self):
        """
        :rtype: int
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
```

### Python3

```python3
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        

    def pick(self) -> int:
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
```

### C

```c



typedef struct {
    
} Solution;


Solution* solutionCreate(int n, int* blacklist, int blacklistSize) {
    
}

int solutionPick(Solution* obj) {
    
}

void solutionFree(Solution* obj) {
    
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(n, blacklist, blacklistSize);
 * int param_1 = solutionPick(obj);
 
 * solutionFree(obj);
*/
```

### C#

```csharp
public class Solution {

    public Solution(int n, int[] blacklist) {
        
    }
    
    public int Pick() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(n, blacklist);
 * int param_1 = obj.Pick();
 */
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} blacklist
 */
var Solution = function(n, blacklist) {
    
};

/**
 * @return {number}
 */
Solution.prototype.pick = function() {
    
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(n, blacklist)
 * var param_1 = obj.pick()
 */
```

### TypeScript

```typescript
class Solution {
    constructor(n: number, blacklist: number[]) {
        
    }

    pick(): number {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(n, blacklist)
 * var param_1 = obj.pick()
 */
```

### PHP

```php
class Solution {
    /**
     * @param Integer $n
     * @param Integer[] $blacklist
     */
    function __construct($n, $blacklist) {
        
    }
  
    /**
     * @return Integer
     */
    function pick() {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * $obj = Solution($n, $blacklist);
 * $ret_1 = $obj->pick();
 */
```

### Swift

```swift

class Solution {

    init(_ n: Int, _ blacklist: [Int]) {
        
    }
    
    func pick() -> Int {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution(n, blacklist)
 * let ret_1: Int = obj.pick()
 */
```

### Kotlin

```kotlin
class Solution(n: Int, blacklist: IntArray) {

    fun pick(): Int {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = Solution(n, blacklist)
 * var param_1 = obj.pick()
 */
```

### Dart

```dart
class Solution {

  Solution(int n, List<int> blacklist) {
    
  }
  
  int pick() {
    
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = Solution(n, blacklist);
 * int param1 = obj.pick();
 */
```

### Go

```golang
type Solution struct {
    
}


func Constructor(n int, blacklist []int) Solution {
    
}


func (this *Solution) Pick() int {
    
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(n, blacklist);
 * param_1 := obj.Pick();
 */
```

### Ruby

```ruby
class Solution

=begin
    :type n: Integer
    :type blacklist: Integer[]
=end
    def initialize(n, blacklist)
        
    end


=begin
    :rtype: Integer
=end
    def pick()
        
    end


end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(n, blacklist)
# param_1 = obj.pick()
```

### Scala

```scala
class Solution(_n: Int, _blacklist: Array[Int]) {

    def pick(): Int = {
        
    }

}

/**
 * Your Solution object will be instantiated and called as such:
 * val obj = new Solution(n, blacklist)
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

    fn new(n: i32, blacklist: Vec<i32>) -> Self {
        
    }
    
    fn pick(&self) -> i32 {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(n, blacklist);
 * let ret_1: i32 = obj.pick();
 */
```

### Racket

```racket
(define solution%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    ; blacklist : (listof exact-integer?)
    (init-field
      n
      blacklist)
    
    ; pick : -> exact-integer?
    (define/public (pick)
      )))

;; Your solution% object will be instantiated and called as such:
;; (define obj (new solution% [n n] [blacklist blacklist]))
;; (define param_1 (send obj pick))
```

### Erlang

```erlang
-spec solution_init_(N :: integer(), Blacklist :: [integer()]) -> any().
solution_init_(N, Blacklist) ->
  .

-spec solution_pick() -> integer().
solution_pick() ->
  .


%% Your functions will be called as such:
%% solution_init_(N, Blacklist),
%% Param_1 = solution_pick(),

%% solution_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Solution do
  @spec init_(n :: integer, blacklist :: [integer]) :: any
  def init_(n, blacklist) do
    
  end

  @spec pick() :: integer
  def pick() do
    
  end
end

# Your functions will be called as such:
# Solution.init_(n, blacklist)
# param_1 = Solution.pick()

# Solution.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Solution {
    init(n: Int64, blacklist: Array<Int64>) {

    }
    
    func pick(): Int64 {

    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj: Solution = Solution(n, blacklist)
 * let param_1 = obj.pick()
 */
```

