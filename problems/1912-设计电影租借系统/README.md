# 1912. 设计电影租借系统

## 题目描述

<p>你有一个电影租借公司和 <code>n</code> 个电影商店。你想要实现一个电影租借系统，它支持查询、预订和返还电影的操作。同时系统还能生成一份当前被借出电影的报告。</p>

<p>所有电影用二维整数数组 <code>entries</code> 表示，其中 <code>entries[i] = [shop<sub>i</sub>, movie<sub>i</sub>, price<sub>i</sub>]</code> 表示商店 <code>shop<sub>i</sub></code> 有一份电影 <code>movie<sub>i</sub></code> 的拷贝，租借价格为 <code>price<sub>i</sub></code> 。每个商店有 <strong>至多一份</strong> 编号为 <code>movie<sub>i</sub></code> 的电影拷贝。</p>

<p>系统需要支持以下操作：</p>

<ul>
	<li><strong>Search：</strong>找到拥有指定电影且 <strong>未借出</strong> 的商店中 <strong>最便宜的 5 个</strong> 。商店需要按照 <strong>价格</strong> 升序排序，如果价格相同，则 <code>shop<sub>i</sub></code> <strong>较小</strong> 的商店排在前面。如果查询结果少于 5 个商店，则将它们全部返回。如果查询结果没有任何商店，则返回空列表。</li>
	<li><strong>Rent：</strong>从指定商店借出指定电影，题目保证指定电影在指定商店 <strong>未借出</strong> 。</li>
	<li><strong>Drop：</strong>在指定商店返还 <strong>之前已借出</strong> 的指定电影。</li>
	<li><strong>Report：</strong>返回 <strong>最便宜的 5 部已借出电影</strong> （可能有重复的电影 ID），将结果用二维列表 <code>res</code> 返回，其中 <code>res[j] = [shop<sub>j</sub>, movie<sub>j</sub>]</code> 表示第 <code>j</code> 便宜的已借出电影是从商店 <code>shop<sub>j</sub></code> 借出的电影 <code>movie<sub>j</sub></code> 。<code>res</code> 中的电影需要按 <strong>价格</strong> 升序排序；如果价格相同，则<strong> </strong><code>shop<sub>j</sub></code> <strong>较小</strong> 的排在前面；如果仍然相同，则 <code>movie<sub>j</sub></code> <strong>较小 </strong>的排在前面。如果当前借出的电影小于 5 部，则将它们全部返回。如果当前没有借出电影，则返回一个空的列表。</li>
</ul>

<p>请你实现 <code>MovieRentingSystem</code> 类：</p>

<ul>
	<li><code>MovieRentingSystem(int n, int[][] entries)</code> 将 <code>MovieRentingSystem</code> 对象用 <code>n</code> 个商店和 <code>entries</code> 表示的电影列表初始化。</li>
	<li><code>List&lt;Integer&gt; search(int movie)</code> 如上所述，返回 <strong>未借出</strong> 指定 <code>movie</code> 的商店列表。</li>
	<li><code>void rent(int shop, int movie)</code> 从指定商店 <code>shop</code> 借出指定电影 <code>movie</code> 。</li>
	<li><code>void drop(int shop, int movie)</code> 在指定商店 <code>shop</code> 返还之前借出的电影 <code>movie</code> 。</li>
	<li><code>List&lt;List&lt;Integer&gt;&gt; report()</code> 如上所述，返回最便宜的 <strong>已借出</strong> 电影列表。</li>
</ul>

<p><strong>注意：</strong>测试数据保证 <code>rent</code> 操作中指定商店拥有 <strong>未借出 </strong>的指定电影，且 <code>drop</code> 操作指定的商店 <strong>之前已借出</strong> 指定电影。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
[[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
<strong>输出：</strong>
[null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]

<strong>解释：</strong>
MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]);
movieRentingSystem.search(1);  // 返回 [1, 0, 2] ，商店 1，0 和 2 有未借出的 ID 为 1 的电影。商店 1 最便宜，商店 0 和 2 价格相同，所以按商店编号排序。
movieRentingSystem.rent(0, 1); // 从商店 0 借出电影 1 。现在商店 0 未借出电影编号为 [2,3] 。
movieRentingSystem.rent(1, 2); // 从商店 1 借出电影 2 。现在商店 1 未借出的电影编号为 [1] 。
movieRentingSystem.report();   // 返回 [[0, 1], [1, 2]] 。商店 0 借出的电影 1 最便宜，然后是商店 1 借出的电影 2 。
movieRentingSystem.drop(1, 2); // 在商店 1 返还电影 2 。现在商店 1 未借出的电影编号为 [1,2] 。
movieRentingSystem.search(2);  // 返回 [0, 1] 。商店 0 和 1 有未借出的 ID 为 2 的电影。商店 0 最便宜，然后是商店 1 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 3 * 10<sup>5</sup></code></li>
	<li><code>1 <= entries.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= shop<sub>i</sub> < n</code></li>
	<li><code>1 <= movie<sub>i</sub>, price<sub>i</sub> <= 10<sup>4</sup></code></li>
	<li>每个商店 <strong>至多</strong> 有一份电影 <code>movie<sub>i</sub></code> 的拷贝。</li>
	<li><code>search</code>，<code>rent</code>，<code>drop</code> 和 <code>report</code> 的调用 <strong>总共</strong> 不超过 <code>10<sup>5</sup></code> 次。</li>
</ul>


## 难度

Hard

## 标签

- 设计
- 数组
- 哈希表
- 有序集合
- 堆（优先队列）

## 提示

1. You need to maintain a sorted list for each movie and a sorted list for rented movies
2. When renting a movie remove it from its movies sorted list and added it to the rented list and vice versa in the case of dropping a movie

## 示例

```
["MovieRentingSystem","search","rent","rent","report","drop","search"]
[[3,[[0,1,5],[0,2,6],[0,3,7],[1,1,4],[1,2,7],[2,1,5]]],[1],[0,1],[1,2],[],[1,2],[2]]
```

## 示例代码

### C++

```cpp
class MovieRentingSystem {
public:
    MovieRentingSystem(int n, vector<vector<int>>& entries) {
        
    }
    
    vector<int> search(int movie) {
        
    }
    
    void rent(int shop, int movie) {
        
    }
    
    void drop(int shop, int movie) {
        
    }
    
    vector<vector<int>> report() {
        
    }
};

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem* obj = new MovieRentingSystem(n, entries);
 * vector<int> param_1 = obj->search(movie);
 * obj->rent(shop,movie);
 * obj->drop(shop,movie);
 * vector<vector<int>> param_4 = obj->report();
 */
```

### Java

```java
class MovieRentingSystem {

    public MovieRentingSystem(int n, int[][] entries) {
        
    }
    
    public List<Integer> search(int movie) {
        
    }
    
    public void rent(int shop, int movie) {
        
    }
    
    public void drop(int shop, int movie) {
        
    }
    
    public List<List<Integer>> report() {
        
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem obj = new MovieRentingSystem(n, entries);
 * List<Integer> param_1 = obj.search(movie);
 * obj.rent(shop,movie);
 * obj.drop(shop,movie);
 * List<List<Integer>> param_4 = obj.report();
 */
```

### Python

```python
class MovieRentingSystem(object):

    def __init__(self, n, entries):
        """
        :type n: int
        :type entries: List[List[int]]
        """
        

    def search(self, movie):
        """
        :type movie: int
        :rtype: List[int]
        """
        

    def rent(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        

    def drop(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        

    def report(self):
        """
        :rtype: List[List[int]]
        """
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
```

### Python3

```python3
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        

    def search(self, movie: int) -> List[int]:
        

    def rent(self, shop: int, movie: int) -> None:
        

    def drop(self, shop: int, movie: int) -> None:
        

    def report(self) -> List[List[int]]:
        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
```

### C

```c



typedef struct {
    
} MovieRentingSystem;


MovieRentingSystem* movieRentingSystemCreate(int n, int** entries, int entriesSize, int* entriesColSize) {
    
}

int* movieRentingSystemSearch(MovieRentingSystem* obj, int movie, int* retSize) {
    
}

void movieRentingSystemRent(MovieRentingSystem* obj, int shop, int movie) {
    
}

void movieRentingSystemDrop(MovieRentingSystem* obj, int shop, int movie) {
    
}

int** movieRentingSystemReport(MovieRentingSystem* obj, int* retSize, int** retColSize) {
    
}

void movieRentingSystemFree(MovieRentingSystem* obj) {
    
}

/**
 * Your MovieRentingSystem struct will be instantiated and called as such:
 * MovieRentingSystem* obj = movieRentingSystemCreate(n, entries, entriesSize, entriesColSize);
 * int* param_1 = movieRentingSystemSearch(obj, movie, retSize);
 
 * movieRentingSystemRent(obj, shop, movie);
 
 * movieRentingSystemDrop(obj, shop, movie);
 
 * int** param_4 = movieRentingSystemReport(obj, retSize, retColSize);
 
 * movieRentingSystemFree(obj);
*/
```

### C#

```csharp
public class MovieRentingSystem {

    public MovieRentingSystem(int n, int[][] entries) {
        
    }
    
    public IList<int> Search(int movie) {
        
    }
    
    public void Rent(int shop, int movie) {
        
    }
    
    public void Drop(int shop, int movie) {
        
    }
    
    public IList<IList<int>> Report() {
        
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem obj = new MovieRentingSystem(n, entries);
 * IList<int> param_1 = obj.Search(movie);
 * obj.Rent(shop,movie);
 * obj.Drop(shop,movie);
 * IList<IList<int>> param_4 = obj.Report();
 */
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} entries
 */
var MovieRentingSystem = function(n, entries) {
    
};

/** 
 * @param {number} movie
 * @return {number[]}
 */
MovieRentingSystem.prototype.search = function(movie) {
    
};

/** 
 * @param {number} shop 
 * @param {number} movie
 * @return {void}
 */
MovieRentingSystem.prototype.rent = function(shop, movie) {
    
};

/** 
 * @param {number} shop 
 * @param {number} movie
 * @return {void}
 */
MovieRentingSystem.prototype.drop = function(shop, movie) {
    
};

/**
 * @return {number[][]}
 */
MovieRentingSystem.prototype.report = function() {
    
};

/** 
 * Your MovieRentingSystem object will be instantiated and called as such:
 * var obj = new MovieRentingSystem(n, entries)
 * var param_1 = obj.search(movie)
 * obj.rent(shop,movie)
 * obj.drop(shop,movie)
 * var param_4 = obj.report()
 */
```

### TypeScript

```typescript
class MovieRentingSystem {
    constructor(n: number, entries: number[][]) {
        
    }

    search(movie: number): number[] {
        
    }

    rent(shop: number, movie: number): void {
        
    }

    drop(shop: number, movie: number): void {
        
    }

    report(): number[][] {
        
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * var obj = new MovieRentingSystem(n, entries)
 * var param_1 = obj.search(movie)
 * obj.rent(shop,movie)
 * obj.drop(shop,movie)
 * var param_4 = obj.report()
 */
```

### PHP

```php
class MovieRentingSystem {
    /**
     * @param Integer $n
     * @param Integer[][] $entries
     */
    function __construct($n, $entries) {
        
    }
  
    /**
     * @param Integer $movie
     * @return Integer[]
     */
    function search($movie) {
        
    }
  
    /**
     * @param Integer $shop
     * @param Integer $movie
     * @return NULL
     */
    function rent($shop, $movie) {
        
    }
  
    /**
     * @param Integer $shop
     * @param Integer $movie
     * @return NULL
     */
    function drop($shop, $movie) {
        
    }
  
    /**
     * @return Integer[][]
     */
    function report() {
        
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * $obj = MovieRentingSystem($n, $entries);
 * $ret_1 = $obj->search($movie);
 * $obj->rent($shop, $movie);
 * $obj->drop($shop, $movie);
 * $ret_4 = $obj->report();
 */
```

### Swift

```swift

class MovieRentingSystem {

    init(_ n: Int, _ entries: [[Int]]) {
        
    }
    
    func search(_ movie: Int) -> [Int] {
        
    }
    
    func rent(_ shop: Int, _ movie: Int) {
        
    }
    
    func drop(_ shop: Int, _ movie: Int) {
        
    }
    
    func report() -> [[Int]] {
        
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * let obj = MovieRentingSystem(n, entries)
 * let ret_1: [Int] = obj.search(movie)
 * obj.rent(shop, movie)
 * obj.drop(shop, movie)
 * let ret_4: [[Int]] = obj.report()
 */
```

### Kotlin

```kotlin
class MovieRentingSystem(n: Int, entries: Array<IntArray>) {

    fun search(movie: Int): List<Int> {
        
    }

    fun rent(shop: Int, movie: Int) {
        
    }

    fun drop(shop: Int, movie: Int) {
        
    }

    fun report(): List<List<Int>> {
        
    }

}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * var obj = MovieRentingSystem(n, entries)
 * var param_1 = obj.search(movie)
 * obj.rent(shop,movie)
 * obj.drop(shop,movie)
 * var param_4 = obj.report()
 */
```

### Dart

```dart
class MovieRentingSystem {

  MovieRentingSystem(int n, List<List<int>> entries) {
    
  }
  
  List<int> search(int movie) {
    
  }
  
  void rent(int shop, int movie) {
    
  }
  
  void drop(int shop, int movie) {
    
  }
  
  List<List<int>> report() {
    
  }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * MovieRentingSystem obj = MovieRentingSystem(n, entries);
 * List<int> param1 = obj.search(movie);
 * obj.rent(shop,movie);
 * obj.drop(shop,movie);
 * List<List<int>> param4 = obj.report();
 */
```

### Go

```golang
type MovieRentingSystem struct {
    
}


func Constructor(n int, entries [][]int) MovieRentingSystem {
    
}


func (this *MovieRentingSystem) Search(movie int) []int {
    
}


func (this *MovieRentingSystem) Rent(shop int, movie int)  {
    
}


func (this *MovieRentingSystem) Drop(shop int, movie int)  {
    
}


func (this *MovieRentingSystem) Report() [][]int {
    
}


/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * obj := Constructor(n, entries);
 * param_1 := obj.Search(movie);
 * obj.Rent(shop,movie);
 * obj.Drop(shop,movie);
 * param_4 := obj.Report();
 */
```

### Ruby

```ruby
class MovieRentingSystem

=begin
    :type n: Integer
    :type entries: Integer[][]
=end
    def initialize(n, entries)
        
    end


=begin
    :type movie: Integer
    :rtype: Integer[]
=end
    def search(movie)
        
    end


=begin
    :type shop: Integer
    :type movie: Integer
    :rtype: Void
=end
    def rent(shop, movie)
        
    end


=begin
    :type shop: Integer
    :type movie: Integer
    :rtype: Void
=end
    def drop(shop, movie)
        
    end


=begin
    :rtype: Integer[][]
=end
    def report()
        
    end


end

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem.new(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop, movie)
# obj.drop(shop, movie)
# param_4 = obj.report()
```

### Scala

```scala
class MovieRentingSystem(_n: Int, _entries: Array[Array[Int]]) {

    def search(movie: Int): List[Int] = {
        
    }

    def rent(shop: Int, movie: Int): Unit = {
        
    }

    def drop(shop: Int, movie: Int): Unit = {
        
    }

    def report(): List[List[Int]] = {
        
    }

}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * val obj = new MovieRentingSystem(n, entries)
 * val param_1 = obj.search(movie)
 * obj.rent(shop,movie)
 * obj.drop(shop,movie)
 * val param_4 = obj.report()
 */
```

### Rust

```rust
struct MovieRentingSystem {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MovieRentingSystem {

    fn new(n: i32, entries: Vec<Vec<i32>>) -> Self {
        
    }
    
    fn search(&self, movie: i32) -> Vec<i32> {
        
    }
    
    fn rent(&self, shop: i32, movie: i32) {
        
    }
    
    fn drop(&self, shop: i32, movie: i32) {
        
    }
    
    fn report(&self) -> Vec<Vec<i32>> {
        
    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * let obj = MovieRentingSystem::new(n, entries);
 * let ret_1: Vec<i32> = obj.search(movie);
 * obj.rent(shop, movie);
 * obj.drop(shop, movie);
 * let ret_4: Vec<Vec<i32>> = obj.report();
 */
```

### Racket

```racket
(define movie-renting-system%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    ; entries : (listof (listof exact-integer?))
    (init-field
      n
      entries)
    
    ; search : exact-integer? -> (listof exact-integer?)
    (define/public (search movie)
      )
    ; rent : exact-integer? exact-integer? -> void?
    (define/public (rent shop movie)
      )
    ; drop : exact-integer? exact-integer? -> void?
    (define/public (drop shop movie)
      )
    ; report : -> (listof (listof exact-integer?))
    (define/public (report)
      )))

;; Your movie-renting-system% object will be instantiated and called as such:
;; (define obj (new movie-renting-system% [n n] [entries entries]))
;; (define param_1 (send obj search movie))
;; (send obj rent shop movie)
;; (send obj drop shop movie)
;; (define param_4 (send obj report))
```

### Erlang

```erlang
-spec movie_renting_system_init_(N :: integer(), Entries :: [[integer()]]) -> any().
movie_renting_system_init_(N, Entries) ->
  .

-spec movie_renting_system_search(Movie :: integer()) -> [integer()].
movie_renting_system_search(Movie) ->
  .

-spec movie_renting_system_rent(Shop :: integer(), Movie :: integer()) -> any().
movie_renting_system_rent(Shop, Movie) ->
  .

-spec movie_renting_system_drop(Shop :: integer(), Movie :: integer()) -> any().
movie_renting_system_drop(Shop, Movie) ->
  .

-spec movie_renting_system_report() -> [[integer()]].
movie_renting_system_report() ->
  .


%% Your functions will be called as such:
%% movie_renting_system_init_(N, Entries),
%% Param_1 = movie_renting_system_search(Movie),
%% movie_renting_system_rent(Shop, Movie),
%% movie_renting_system_drop(Shop, Movie),
%% Param_4 = movie_renting_system_report(),

%% movie_renting_system_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule MovieRentingSystem do
  @spec init_(n :: integer, entries :: [[integer]]) :: any
  def init_(n, entries) do
    
  end

  @spec search(movie :: integer) :: [integer]
  def search(movie) do
    
  end

  @spec rent(shop :: integer, movie :: integer) :: any
  def rent(shop, movie) do
    
  end

  @spec drop(shop :: integer, movie :: integer) :: any
  def drop(shop, movie) do
    
  end

  @spec report() :: [[integer]]
  def report() do
    
  end
end

# Your functions will be called as such:
# MovieRentingSystem.init_(n, entries)
# param_1 = MovieRentingSystem.search(movie)
# MovieRentingSystem.rent(shop, movie)
# MovieRentingSystem.drop(shop, movie)
# param_4 = MovieRentingSystem.report()

# MovieRentingSystem.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class MovieRentingSystem {
    init(n: Int64, entries: Array<Array<Int64>>) {

    }
    
    func search(movie: Int64): ArrayList<Int64> {

    }
    
    func rent(shop: Int64, movie: Int64): Unit {

    }
    
    func drop(shop: Int64, movie: Int64): Unit {

    }
    
    func report(): ArrayList<ArrayList<Int64>> {

    }
}

/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * let obj: MovieRentingSystem = MovieRentingSystem(n, entries)
 * let param_1 = obj.search(movie)
 * obj.rent(shop,movie)
 * obj.drop(shop,movie)
 * let param_4 = obj.report()
 */
```

