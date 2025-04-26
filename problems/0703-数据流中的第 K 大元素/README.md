# 703. 数据流中的第 K 大元素

## 题目描述

<p>设计一个找到数据流中第 <code>k</code> 大元素的类（class）。注意是排序后的第 <code>k</code> 大元素，不是第 <code>k</code> 个不同的元素。</p>

<p>请实现 <code>KthLargest</code>&nbsp;类：</p>

<ul>
	<li><code>KthLargest(int k, int[] nums)</code> 使用整数 <code>k</code> 和整数流 <code>nums</code> 初始化对象。</li>
	<li><code>int add(int val)</code> 将 <code>val</code> 插入数据流 <code>nums</code> 后，返回当前数据流中第 <code>k</code> 大的元素。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><br />
<span class="example-io">["KthLargest", "add", "add", "add", "add", "add"]<br />
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]</span></p>

<p><strong>输出：</strong><span class="example-io">[null, 4, 5, 5, 8, 8]</span></p>

<p><strong>解释：</strong></p>

<p>KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);<br />
kthLargest.add(3); // 返回 4<br />
kthLargest.add(5); // 返回 5<br />
kthLargest.add(10); // 返回 5<br />
kthLargest.add(9); // 返回 8<br />
kthLargest.add(4); // 返回 8</p>

<p>&nbsp;</p>
</div>

<p><strong class="example">示例&nbsp;2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><br />
<span class="example-io">["KthLargest", "add", "add", "add", "add"]<br />
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]</span></p>

<p><span class="example-io"><b>输出：</b>[null, 7, 7, 7, 8]</span></p>

<p><strong>解释：</strong></p>
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);<br />
kthLargest.add(2); // 返回 7<br />
kthLargest.add(10); // 返回 7<br />
kthLargest.add(9); // 返回 7<br />
kthLargest.add(9); // 返回 8</div>

<p>&nbsp;</p>
<strong>提示：</strong>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length + 1</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= val &lt;= 10<sup>4</sup></code></li>
	<li>最多调用 <code>add</code> 方法 <code>10<sup>4</sup></code> 次</li>
</ul>


## 难度

Easy

## 标签

- 树
- 设计
- 二叉搜索树
- 二叉树
- 数据流
- 堆（优先队列）

## 示例

```
["KthLargest","add","add","add","add","add"]
[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
["KthLargest","add","add","add","add"]
[[4,[7,7,7,7,8,3]],[2],[10],[9],[9]]
```

## 示例代码

### C++

```cpp
class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) {
        
    }
    
    int add(int val) {
        
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
```

### Java

```java
class KthLargest {

    public KthLargest(int k, int[] nums) {
        
    }
    
    public int add(int val) {
        
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
```

### Python

```python
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```

### Python3

```python3
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        

    def add(self, val: int) -> int:
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```

### C

```c



typedef struct {
    
} KthLargest;


KthLargest* kthLargestCreate(int k, int* nums, int numsSize) {
    
}

int kthLargestAdd(KthLargest* obj, int val) {
    
}

void kthLargestFree(KthLargest* obj) {
    
}

/**
 * Your KthLargest struct will be instantiated and called as such:
 * KthLargest* obj = kthLargestCreate(k, nums, numsSize);
 * int param_1 = kthLargestAdd(obj, val);
 
 * kthLargestFree(obj);
*/
```

### C#

```csharp
public class KthLargest {

    public KthLargest(int k, int[] nums) {
        
    }
    
    public int Add(int val) {
        
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.Add(val);
 */
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest = function(k, nums) {
    
};

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function(val) {
    
};

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */
```

### TypeScript

```typescript
class KthLargest {
    constructor(k: number, nums: number[]) {
        
    }

    add(val: number): number {
        
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */
```

### PHP

```php
class KthLargest {
    /**
     * @param Integer $k
     * @param Integer[] $nums
     */
    function __construct($k, $nums) {
        
    }
  
    /**
     * @param Integer $val
     * @return Integer
     */
    function add($val) {
        
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * $obj = KthLargest($k, $nums);
 * $ret_1 = $obj->add($val);
 */
```

### Swift

```swift

class KthLargest {

    init(_ k: Int, _ nums: [Int]) {
        
    }
    
    func add(_ val: Int) -> Int {
        
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * let obj = KthLargest(k, nums)
 * let ret_1: Int = obj.add(val)
 */
```

### Kotlin

```kotlin
class KthLargest(k: Int, nums: IntArray) {

    fun add(`val`: Int): Int {
        
    }

}

/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = KthLargest(k, nums)
 * var param_1 = obj.add(`val`)
 */
```

### Dart

```dart
class KthLargest {

  KthLargest(int k, List<int> nums) {
    
  }
  
  int add(int val) {
    
  }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = KthLargest(k, nums);
 * int param1 = obj.add(val);
 */
```

### Go

```golang
type KthLargest struct {
    
}


func Constructor(k int, nums []int) KthLargest {
    
}


func (this *KthLargest) Add(val int) int {
    
}


/**
 * Your KthLargest object will be instantiated and called as such:
 * obj := Constructor(k, nums);
 * param_1 := obj.Add(val);
 */
```

### Ruby

```ruby
class KthLargest

=begin
    :type k: Integer
    :type nums: Integer[]
=end
    def initialize(k, nums)
        
    end


=begin
    :type val: Integer
    :rtype: Integer
=end
    def add(val)
        
    end


end

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest.new(k, nums)
# param_1 = obj.add(val)
```

### Scala

```scala
class KthLargest(_k: Int, _nums: Array[Int]) {

    def add(`val`: Int): Int = {
        
    }

}

/**
 * Your KthLargest object will be instantiated and called as such:
 * val obj = new KthLargest(k, nums)
 * val param_1 = obj.add(`val`)
 */
```

### Rust

```rust
struct KthLargest {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl KthLargest {

    fn new(k: i32, nums: Vec<i32>) -> Self {
        
    }
    
    fn add(&self, val: i32) -> i32 {
        
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * let obj = KthLargest::new(k, nums);
 * let ret_1: i32 = obj.add(val);
 */
```

### Racket

```racket
(define kth-largest%
  (class object%
    (super-new)
    
    ; k : exact-integer?
    ; nums : (listof exact-integer?)
    (init-field
      k
      nums)
    
    ; add : exact-integer? -> exact-integer?
    (define/public (add val)
      )))

;; Your kth-largest% object will be instantiated and called as such:
;; (define obj (new kth-largest% [k k] [nums nums]))
;; (define param_1 (send obj add val))
```

### Erlang

```erlang
-spec kth_largest_init_(K :: integer(), Nums :: [integer()]) -> any().
kth_largest_init_(K, Nums) ->
  .

-spec kth_largest_add(Val :: integer()) -> integer().
kth_largest_add(Val) ->
  .


%% Your functions will be called as such:
%% kth_largest_init_(K, Nums),
%% Param_1 = kth_largest_add(Val),

%% kth_largest_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule KthLargest do
  @spec init_(k :: integer, nums :: [integer]) :: any
  def init_(k, nums) do
    
  end

  @spec add(val :: integer) :: integer
  def add(val) do
    
  end
end

# Your functions will be called as such:
# KthLargest.init_(k, nums)
# param_1 = KthLargest.add(val)

# KthLargest.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class KthLargest {
    init(k: Int64, nums: Array<Int64>) {

    }
    
    func add(val: Int64): Int64 {

    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * let obj: KthLargest = KthLargest(k, nums)
 * let param_1 = obj.add(val)
 */
```

