# 1865. 找出和为指定值的下标对

## 题目描述

<p>给你两个整数数组 <code>nums1</code> 和 <code>nums2</code> ，请你实现一个支持下述两类查询的数据结构：</p>

<ol>
	<li><strong>累加</strong> ，将一个正整数加到 <code>nums2</code> 中指定下标对应元素上。</li>
	<li><strong>计数 </strong>，统计满足 <code>nums1[i] + nums2[j]</code> 等于指定值的下标对 <code>(i, j)</code> 数目（<code>0 <= i < nums1.length</code> 且 <code>0 <= j < nums2.length</code>）。</li>
</ol>

<p>实现 <code>FindSumPairs</code> 类：</p>

<ul>
	<li><code>FindSumPairs(int[] nums1, int[] nums2)</code> 使用整数数组 <code>nums1</code> 和 <code>nums2</code> 初始化 <code>FindSumPairs</code> 对象。</li>
	<li><code>void add(int index, int val)</code> 将 <code>val</code> 加到 <code>nums2[index]</code> 上，即，执行 <code>nums2[index] += val</code> 。</li>
	<li><code>int count(int tot)</code> 返回满足 <code>nums1[i] + nums2[j] == tot</code> 的下标对 <code>(i, j)</code> 数目。</li>
</ul>

<p> </p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
<strong>输出：</strong>
[null, 8, null, 2, 1, null, null, 11]

<strong>解释：</strong>
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // 返回 8 ; 下标对 (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) 满足 2 + 5 = 7 ，下标对 (5,1), (5,5) 满足 3 + 4 = 7
findSumPairs.add(3, 2); // 此时 nums2 = [1,4,5,<em><strong>4</strong></em><code>,5,4</code>]
findSumPairs.count(8);  // 返回 2 ；下标对 (5,2), (5,4) 满足 3 + 5 = 8
findSumPairs.count(4);  // 返回 1 ；下标对 (5,0) 满足 3 + 1 = 4
findSumPairs.add(0, 1); // 此时 nums2 = [<em><strong><code>2</code></strong></em>,4,5,4<code>,5,4</code>]
findSumPairs.add(1, 1); // 此时 nums2 = [<code>2</code>,<em><strong>5</strong></em>,5,4<code>,5,4</code>]
findSumPairs.count(7);  // 返回 11 ；下标对 (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) 满足 2 + 5 = 7 ，下标对 (5,3), (5,5) 满足 3 + 4 = 7
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums1.length <= 1000</code></li>
	<li><code>1 <= nums2.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums1[i] <= 10<sup>9</sup></code></li>
	<li><code>1 <= nums2[i] <= 10<sup>5</sup></code></li>
	<li><code>0 <= index < nums2.length</code></li>
	<li><code>1 <= val <= 10<sup>5</sup></code></li>
	<li><code>1 <= tot <= 10<sup>9</sup></code></li>
	<li>最多调用 <code>add</code> 和 <code>count</code> 函数各 <code>1000</code> 次</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 哈希表

## 提示

1. The length of nums1 is small in comparison to that of nums2
2. If we iterate over elements of nums1 we just need to find the count of tot - element for all elements in nums1

## 示例

```
["FindSumPairs","count","add","count","count","add","add","count"]
[[[1,1,2,2,2,3],[1,4,5,2,5,4]],[7],[3,2],[8],[4],[0,1],[1,1],[7]]
```

## 示例代码

### C++

```cpp
class FindSumPairs {
public:
    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        
    }
    
    void add(int index, int val) {
        
    }
    
    int count(int tot) {
        
    }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */
```

### Java

```java
class FindSumPairs {

    public FindSumPairs(int[] nums1, int[] nums2) {
        
    }
    
    public void add(int index, int val) {
        
    }
    
    public int count(int tot) {
        
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs obj = new FindSumPairs(nums1, nums2);
 * obj.add(index,val);
 * int param_2 = obj.count(tot);
 */
```

### Python

```python
class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
```

### Python3

```python3
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        

    def add(self, index: int, val: int) -> None:
        

    def count(self, tot: int) -> int:
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
```

### C

```c



typedef struct {
    
} FindSumPairs;


FindSumPairs* findSumPairsCreate(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}

void findSumPairsAdd(FindSumPairs* obj, int index, int val) {
    
}

int findSumPairsCount(FindSumPairs* obj, int tot) {
    
}

void findSumPairsFree(FindSumPairs* obj) {
    
}

/**
 * Your FindSumPairs struct will be instantiated and called as such:
 * FindSumPairs* obj = findSumPairsCreate(nums1, nums1Size, nums2, nums2Size);
 * findSumPairsAdd(obj, index, val);
 
 * int param_2 = findSumPairsCount(obj, tot);
 
 * findSumPairsFree(obj);
*/
```

### C#

```csharp
public class FindSumPairs {

    public FindSumPairs(int[] nums1, int[] nums2) {
        
    }
    
    public void Add(int index, int val) {
        
    }
    
    public int Count(int tot) {
        
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs obj = new FindSumPairs(nums1, nums2);
 * obj.Add(index,val);
 * int param_2 = obj.Count(tot);
 */
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 */
var FindSumPairs = function(nums1, nums2) {
    
};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
FindSumPairs.prototype.add = function(index, val) {
    
};

/** 
 * @param {number} tot
 * @return {number}
 */
FindSumPairs.prototype.count = function(tot) {
    
};

/** 
 * Your FindSumPairs object will be instantiated and called as such:
 * var obj = new FindSumPairs(nums1, nums2)
 * obj.add(index,val)
 * var param_2 = obj.count(tot)
 */
```

### TypeScript

```typescript
class FindSumPairs {
    constructor(nums1: number[], nums2: number[]) {
        
    }

    add(index: number, val: number): void {
        
    }

    count(tot: number): number {
        
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * var obj = new FindSumPairs(nums1, nums2)
 * obj.add(index,val)
 * var param_2 = obj.count(tot)
 */
```

### PHP

```php
class FindSumPairs {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     */
    function __construct($nums1, $nums2) {
        
    }
  
    /**
     * @param Integer $index
     * @param Integer $val
     * @return NULL
     */
    function add($index, $val) {
        
    }
  
    /**
     * @param Integer $tot
     * @return Integer
     */
    function count($tot) {
        
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * $obj = FindSumPairs($nums1, $nums2);
 * $obj->add($index, $val);
 * $ret_2 = $obj->count($tot);
 */
```

### Swift

```swift

class FindSumPairs {

    init(_ nums1: [Int], _ nums2: [Int]) {
        
    }
    
    func add(_ index: Int, _ val: Int) {
        
    }
    
    func count(_ tot: Int) -> Int {
        
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * let obj = FindSumPairs(nums1, nums2)
 * obj.add(index, val)
 * let ret_2: Int = obj.count(tot)
 */
```

### Kotlin

```kotlin
class FindSumPairs(nums1: IntArray, nums2: IntArray) {

    fun add(index: Int, `val`: Int) {
        
    }

    fun count(tot: Int): Int {
        
    }

}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * var obj = FindSumPairs(nums1, nums2)
 * obj.add(index,`val`)
 * var param_2 = obj.count(tot)
 */
```

### Dart

```dart
class FindSumPairs {

  FindSumPairs(List<int> nums1, List<int> nums2) {
    
  }
  
  void add(int index, int val) {
    
  }
  
  int count(int tot) {
    
  }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs obj = FindSumPairs(nums1, nums2);
 * obj.add(index,val);
 * int param2 = obj.count(tot);
 */
```

### Go

```golang
type FindSumPairs struct {
    
}


func Constructor(nums1 []int, nums2 []int) FindSumPairs {
    
}


func (this *FindSumPairs) Add(index int, val int)  {
    
}


func (this *FindSumPairs) Count(tot int) int {
    
}


/**
 * Your FindSumPairs object will be instantiated and called as such:
 * obj := Constructor(nums1, nums2);
 * obj.Add(index,val);
 * param_2 := obj.Count(tot);
 */
```

### Ruby

```ruby
class FindSumPairs

=begin
    :type nums1: Integer[]
    :type nums2: Integer[]
=end
    def initialize(nums1, nums2)
        
    end


=begin
    :type index: Integer
    :type val: Integer
    :rtype: Void
=end
    def add(index, val)
        
    end


=begin
    :type tot: Integer
    :rtype: Integer
=end
    def count(tot)
        
    end


end

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs.new(nums1, nums2)
# obj.add(index, val)
# param_2 = obj.count(tot)
```

### Scala

```scala
class FindSumPairs(_nums1: Array[Int], _nums2: Array[Int]) {

    def add(index: Int, `val`: Int): Unit = {
        
    }

    def count(tot: Int): Int = {
        
    }

}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * val obj = new FindSumPairs(nums1, nums2)
 * obj.add(index,`val`)
 * val param_2 = obj.count(tot)
 */
```

### Rust

```rust
struct FindSumPairs {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FindSumPairs {

    fn new(nums1: Vec<i32>, nums2: Vec<i32>) -> Self {
        
    }
    
    fn add(&self, index: i32, val: i32) {
        
    }
    
    fn count(&self, tot: i32) -> i32 {
        
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * let obj = FindSumPairs::new(nums1, nums2);
 * obj.add(index, val);
 * let ret_2: i32 = obj.count(tot);
 */
```

### Racket

```racket
(define find-sum-pairs%
  (class object%
    (super-new)
    
    ; nums1 : (listof exact-integer?)
    ; nums2 : (listof exact-integer?)
    (init-field
      nums1
      nums2)
    
    ; add : exact-integer? exact-integer? -> void?
    (define/public (add index val)
      )
    ; count : exact-integer? -> exact-integer?
    (define/public (count tot)
      )))

;; Your find-sum-pairs% object will be instantiated and called as such:
;; (define obj (new find-sum-pairs% [nums1 nums1] [nums2 nums2]))
;; (send obj add index val)
;; (define param_2 (send obj count tot))
```

### Erlang

```erlang
-spec find_sum_pairs_init_(Nums1 :: [integer()], Nums2 :: [integer()]) -> any().
find_sum_pairs_init_(Nums1, Nums2) ->
  .

-spec find_sum_pairs_add(Index :: integer(), Val :: integer()) -> any().
find_sum_pairs_add(Index, Val) ->
  .

-spec find_sum_pairs_count(Tot :: integer()) -> integer().
find_sum_pairs_count(Tot) ->
  .


%% Your functions will be called as such:
%% find_sum_pairs_init_(Nums1, Nums2),
%% find_sum_pairs_add(Index, Val),
%% Param_2 = find_sum_pairs_count(Tot),

%% find_sum_pairs_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule FindSumPairs do
  @spec init_(nums1 :: [integer], nums2 :: [integer]) :: any
  def init_(nums1, nums2) do
    
  end

  @spec add(index :: integer, val :: integer) :: any
  def add(index, val) do
    
  end

  @spec count(tot :: integer) :: integer
  def count(tot) do
    
  end
end

# Your functions will be called as such:
# FindSumPairs.init_(nums1, nums2)
# FindSumPairs.add(index, val)
# param_2 = FindSumPairs.count(tot)

# FindSumPairs.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class FindSumPairs {
    init(nums1: Array<Int64>, nums2: Array<Int64>) {

    }
    
    func add(index: Int64, val: Int64): Unit {

    }
    
    func count(tot: Int64): Int64 {

    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * let obj: FindSumPairs = FindSumPairs(nums1, nums2)
 * obj.add(index,val)
 * let param_2 = obj.count(tot)
 */
```

