# 2286. 以组为单位订音乐会的门票

## 题目描述

<p>一个音乐会总共有&nbsp;<code>n</code>&nbsp;排座位，编号从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;，每一排有&nbsp;<code>m</code>&nbsp;个座椅，编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>m - 1</code>&nbsp;。你需要设计一个买票系统，针对以下情况进行座位安排：</p>

<ul>
	<li>同一组的 <code>k</code>&nbsp;位观众坐在<strong> 同一排座位，且座位连续 </strong>。</li>
	<li><code>k</code>&nbsp;位观众中 <strong>每一位</strong>&nbsp;都有座位坐，但他们 <strong>不一定</strong>&nbsp;坐在一起。</li>
</ul>

<p>由于观众非常挑剔，所以：</p>

<ul>
	<li>只有当一个组里所有成员座位的排数都 <strong>小于等于</strong>&nbsp;<code>maxRow</code>&nbsp;，这个组才能订座位。每一组的&nbsp;<code>maxRow</code>&nbsp;可能 <strong>不同</strong>&nbsp;。</li>
	<li>如果有多排座位可以选择，优先选择 <strong>最小</strong>&nbsp;的排数。如果同一排中有多个座位可以坐，优先选择号码 <strong>最小</strong>&nbsp;的。</li>
</ul>

<p>请你实现&nbsp;<code>BookMyShow</code>&nbsp;类：</p>

<ul>
	<li><code>BookMyShow(int n, int m)</code>&nbsp;，初始化对象，<code>n</code>&nbsp;是排数，<code>m</code>&nbsp;是每一排的座位数。</li>
	<li><code>int[] gather(int k, int maxRow)</code>&nbsp;返回长度为 <code>2</code>&nbsp;的数组，表示 <code>k</code>&nbsp;个成员中 <strong>第一个座位</strong>&nbsp;的排数和座位编号，这 <code>k</code>&nbsp;位成员必须坐在 <strong>同一排座位，且座位连续 </strong>。换言之，返回最小可能的&nbsp;<code>r</code> 和&nbsp;<code>c</code>&nbsp;满足第&nbsp;<code>r</code>&nbsp;排中&nbsp;<code>[c, c + k - 1]</code>&nbsp;的座位都是空的，且&nbsp;<code>r &lt;= maxRow</code>&nbsp;。如果&nbsp;<strong>无法</strong>&nbsp;安排座位，返回&nbsp;<code>[]</code>&nbsp;。</li>
	<li><code>boolean scatter(int k, int maxRow)</code>&nbsp;如果组里所有&nbsp;<code>k</code>&nbsp;个成员&nbsp;<strong>不一定</strong>&nbsp;要坐在一起的前提下，都能在第&nbsp;<code>0</code> 排到第&nbsp;<code>maxRow</code>&nbsp;排之间找到座位，那么请返回&nbsp;<code>true</code>&nbsp;。这种情况下，每个成员都优先找排数&nbsp;<strong>最小</strong>&nbsp;，然后是座位编号最小的座位。如果不能安排所有&nbsp;<code>k</code>&nbsp;个成员的座位，请返回&nbsp;<code>false</code>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["BookMyShow", "gather", "gather", "scatter", "scatter"]
[[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]
<strong>输出：</strong>
[null, [0, 0], [], true, false]

<strong>解释：</strong>
BookMyShow bms = new BookMyShow(2, 5); // 总共有 2 排，每排 5 个座位。
bms.gather(4, 0); // 返回 [0, 0]
                  // 这一组安排第 0 排 [0, 3] 的座位。
bms.gather(2, 0); // 返回 []
                  // 第 0 排只剩下 1 个座位。
                  // 所以无法安排 2 个连续座位。
bms.scatter(5, 1); // 返回 True
                   // 这一组安排第 0 排第 4 个座位和第 1 排 [0, 3] 的座位。
bms.scatter(5, 1); // 返回 False
                   // 总共只剩下 1 个座位。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m, k &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= maxRow &lt;= n - 1</code></li>
	<li><code>gather</code> 和&nbsp;<code>scatter</code>&nbsp;<strong>总</strong> 调用次数不超过&nbsp;<code>5 * 10<sup>4</sup></code> 次。</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 树状数组
- 线段树
- 二分查找

## 提示

1. Since seats are allocated by smallest row and then by smallest seat numbers, how can we keep a record of the smallest seat number vacant in each row?
2. How can range max query help us to check if contiguous seats can be allocated in a range?
3. Similarly, can range sum query help us to check if enough seats are available in a range?
4. Which data structure can be used to implement the above?

## 示例

```
["BookMyShow","gather","gather","scatter","scatter"]
[[2,5],[4,0],[2,0],[5,1],[5,1]]
```

## 示例代码

### C++

```cpp
class BookMyShow {
public:
    BookMyShow(int n, int m) {
        
    }
    
    vector<int> gather(int k, int maxRow) {
        
    }
    
    bool scatter(int k, int maxRow) {
        
    }
};

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow* obj = new BookMyShow(n, m);
 * vector<int> param_1 = obj->gather(k,maxRow);
 * bool param_2 = obj->scatter(k,maxRow);
 */
```

### Java

```java
class BookMyShow {

    public BookMyShow(int n, int m) {
        
    }
    
    public int[] gather(int k, int maxRow) {
        
    }
    
    public boolean scatter(int k, int maxRow) {
        
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow obj = new BookMyShow(n, m);
 * int[] param_1 = obj.gather(k,maxRow);
 * boolean param_2 = obj.scatter(k,maxRow);
 */
```

### Python

```python
class BookMyShow(object):

    def __init__(self, n, m):
        """
        :type n: int
        :type m: int
        """
        

    def gather(self, k, maxRow):
        """
        :type k: int
        :type maxRow: int
        :rtype: List[int]
        """
        

    def scatter(self, k, maxRow):
        """
        :type k: int
        :type maxRow: int
        :rtype: bool
        """
        


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
```

### Python3

```python3
class BookMyShow:

    def __init__(self, n: int, m: int):
        

    def gather(self, k: int, maxRow: int) -> List[int]:
        

    def scatter(self, k: int, maxRow: int) -> bool:
        


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
```

### C

```c



typedef struct {
    
} BookMyShow;


BookMyShow* bookMyShowCreate(int n, int m) {
    
}

int* bookMyShowGather(BookMyShow* obj, int k, int maxRow, int* retSize) {
    
}

bool bookMyShowScatter(BookMyShow* obj, int k, int maxRow) {
    
}

void bookMyShowFree(BookMyShow* obj) {
    
}

/**
 * Your BookMyShow struct will be instantiated and called as such:
 * BookMyShow* obj = bookMyShowCreate(n, m);
 * int* param_1 = bookMyShowGather(obj, k, maxRow, retSize);
 
 * bool param_2 = bookMyShowScatter(obj, k, maxRow);
 
 * bookMyShowFree(obj);
*/
```

### C#

```csharp
public class BookMyShow {

    public BookMyShow(int n, int m) {
        
    }
    
    public int[] Gather(int k, int maxRow) {
        
    }
    
    public bool Scatter(int k, int maxRow) {
        
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow obj = new BookMyShow(n, m);
 * int[] param_1 = obj.Gather(k,maxRow);
 * bool param_2 = obj.Scatter(k,maxRow);
 */
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} m
 */
var BookMyShow = function(n, m) {
    
};

/** 
 * @param {number} k 
 * @param {number} maxRow
 * @return {number[]}
 */
BookMyShow.prototype.gather = function(k, maxRow) {
    
};

/** 
 * @param {number} k 
 * @param {number} maxRow
 * @return {boolean}
 */
BookMyShow.prototype.scatter = function(k, maxRow) {
    
};

/** 
 * Your BookMyShow object will be instantiated and called as such:
 * var obj = new BookMyShow(n, m)
 * var param_1 = obj.gather(k,maxRow)
 * var param_2 = obj.scatter(k,maxRow)
 */
```

### TypeScript

```typescript
class BookMyShow {
    constructor(n: number, m: number) {
        
    }

    gather(k: number, maxRow: number): number[] {
        
    }

    scatter(k: number, maxRow: number): boolean {
        
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * var obj = new BookMyShow(n, m)
 * var param_1 = obj.gather(k,maxRow)
 * var param_2 = obj.scatter(k,maxRow)
 */
```

### PHP

```php
class BookMyShow {
    /**
     * @param Integer $n
     * @param Integer $m
     */
    function __construct($n, $m) {
        
    }
  
    /**
     * @param Integer $k
     * @param Integer $maxRow
     * @return Integer[]
     */
    function gather($k, $maxRow) {
        
    }
  
    /**
     * @param Integer $k
     * @param Integer $maxRow
     * @return Boolean
     */
    function scatter($k, $maxRow) {
        
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * $obj = BookMyShow($n, $m);
 * $ret_1 = $obj->gather($k, $maxRow);
 * $ret_2 = $obj->scatter($k, $maxRow);
 */
```

### Swift

```swift

class BookMyShow {

    init(_ n: Int, _ m: Int) {
        
    }
    
    func gather(_ k: Int, _ maxRow: Int) -> [Int] {
        
    }
    
    func scatter(_ k: Int, _ maxRow: Int) -> Bool {
        
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * let obj = BookMyShow(n, m)
 * let ret_1: [Int] = obj.gather(k, maxRow)
 * let ret_2: Bool = obj.scatter(k, maxRow)
 */
```

### Kotlin

```kotlin
class BookMyShow(n: Int, m: Int) {

    fun gather(k: Int, maxRow: Int): IntArray {
        
    }

    fun scatter(k: Int, maxRow: Int): Boolean {
        
    }

}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * var obj = BookMyShow(n, m)
 * var param_1 = obj.gather(k,maxRow)
 * var param_2 = obj.scatter(k,maxRow)
 */
```

### Dart

```dart
class BookMyShow {

  BookMyShow(int n, int m) {
    
  }
  
  List<int> gather(int k, int maxRow) {
    
  }
  
  bool scatter(int k, int maxRow) {
    
  }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow obj = BookMyShow(n, m);
 * List<int> param1 = obj.gather(k,maxRow);
 * bool param2 = obj.scatter(k,maxRow);
 */
```

### Go

```golang
type BookMyShow struct {
    
}


func Constructor(n int, m int) BookMyShow {
    
}


func (this *BookMyShow) Gather(k int, maxRow int) []int {
    
}


func (this *BookMyShow) Scatter(k int, maxRow int) bool {
    
}


/**
 * Your BookMyShow object will be instantiated and called as such:
 * obj := Constructor(n, m);
 * param_1 := obj.Gather(k,maxRow);
 * param_2 := obj.Scatter(k,maxRow);
 */
```

### Ruby

```ruby
class BookMyShow

=begin
    :type n: Integer
    :type m: Integer
=end
    def initialize(n, m)
        
    end


=begin
    :type k: Integer
    :type max_row: Integer
    :rtype: Integer[]
=end
    def gather(k, max_row)
        
    end


=begin
    :type k: Integer
    :type max_row: Integer
    :rtype: Boolean
=end
    def scatter(k, max_row)
        
    end


end

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow.new(n, m)
# param_1 = obj.gather(k, max_row)
# param_2 = obj.scatter(k, max_row)
```

### Scala

```scala
class BookMyShow(_n: Int, _m: Int) {

    def gather(k: Int, maxRow: Int): Array[Int] = {
        
    }

    def scatter(k: Int, maxRow: Int): Boolean = {
        
    }

}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * val obj = new BookMyShow(n, m)
 * val param_1 = obj.gather(k,maxRow)
 * val param_2 = obj.scatter(k,maxRow)
 */
```

### Rust

```rust
struct BookMyShow {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl BookMyShow {

    fn new(n: i32, m: i32) -> Self {
        
    }
    
    fn gather(&self, k: i32, max_row: i32) -> Vec<i32> {
        
    }
    
    fn scatter(&self, k: i32, max_row: i32) -> bool {
        
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * let obj = BookMyShow::new(n, m);
 * let ret_1: Vec<i32> = obj.gather(k, maxRow);
 * let ret_2: bool = obj.scatter(k, maxRow);
 */
```

### Racket

```racket
(define book-my-show%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    ; m : exact-integer?
    (init-field
      n
      m)
    
    ; gather : exact-integer? exact-integer? -> (listof exact-integer?)
    (define/public (gather k max-row)
      )
    ; scatter : exact-integer? exact-integer? -> boolean?
    (define/public (scatter k max-row)
      )))

;; Your book-my-show% object will be instantiated and called as such:
;; (define obj (new book-my-show% [n n] [m m]))
;; (define param_1 (send obj gather k max-row))
;; (define param_2 (send obj scatter k max-row))
```

### Erlang

```erlang
-spec book_my_show_init_(N :: integer(), M :: integer()) -> any().
book_my_show_init_(N, M) ->
  .

-spec book_my_show_gather(K :: integer(), MaxRow :: integer()) -> [integer()].
book_my_show_gather(K, MaxRow) ->
  .

-spec book_my_show_scatter(K :: integer(), MaxRow :: integer()) -> boolean().
book_my_show_scatter(K, MaxRow) ->
  .


%% Your functions will be called as such:
%% book_my_show_init_(N, M),
%% Param_1 = book_my_show_gather(K, MaxRow),
%% Param_2 = book_my_show_scatter(K, MaxRow),

%% book_my_show_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule BookMyShow do
  @spec init_(n :: integer, m :: integer) :: any
  def init_(n, m) do
    
  end

  @spec gather(k :: integer, max_row :: integer) :: [integer]
  def gather(k, max_row) do
    
  end

  @spec scatter(k :: integer, max_row :: integer) :: boolean
  def scatter(k, max_row) do
    
  end
end

# Your functions will be called as such:
# BookMyShow.init_(n, m)
# param_1 = BookMyShow.gather(k, max_row)
# param_2 = BookMyShow.scatter(k, max_row)

# BookMyShow.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class BookMyShow {
    init(n: Int64, m: Int64) {

    }
    
    func gather(k: Int64, maxRow: Int64): Array<Int64> {

    }
    
    func scatter(k: Int64, maxRow: Int64): Bool {

    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * let obj: BookMyShow = BookMyShow(n, m)
 * let param_1 = obj.gather(k,maxRow)
 * let param_2 = obj.scatter(k,maxRow)
 */
```

