# 2353. 设计食物评分系统

## 题目描述

<p>设计一个支持下述操作的食物评分系统：</p>

<ul>
	<li><strong>修改</strong> 系统中列出的某种食物的评分。</li>
	<li>返回系统中某一类烹饪方式下评分最高的食物。</li>
</ul>

<p>实现 <code>FoodRatings</code> 类：</p>

<ul>
	<li><code>FoodRatings(String[] foods, String[] cuisines, int[] ratings)</code> 初始化系统。食物由 <code>foods</code>、<code>cuisines</code> 和 <code>ratings</code> 描述，长度均为 <code>n</code> 。

	<ul>
		<li><code>foods[i]</code> 是第 <code>i</code> 种食物的名字。</li>
		<li><code>cuisines[i]</code> 是第 <code>i</code> 种食物的烹饪方式。</li>
		<li><code>ratings[i]</code> 是第 <code>i</code> 种食物的最初评分。</li>
	</ul>
	</li>
	<li><code>void changeRating(String food, int newRating)</code> 修改名字为 <code>food</code> 的食物的评分。</li>
	<li><code>String highestRated(String cuisine)</code> 返回指定烹饪方式 <code>cuisine</code> 下评分最高的食物的名字。如果存在并列，返回 <strong>字典序较小</strong> 的名字。</li>
</ul>

<p>注意，字符串 <code>x</code> 的字典序比字符串 <code>y</code> 更小的前提是：<code>x</code> 在字典中出现的位置在 <code>y</code> 之前，也就是说，要么 <code>x</code> 是 <code>y</code> 的前缀，或者在满足&nbsp;<code>x[i] != y[i]</code> 的第一个位置 <code>i</code> 处，<code>x[i]</code> 在字母表中出现的位置在 <code>y[i]</code> 之前。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入</strong>
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
<strong>输出</strong>
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

<strong>解释</strong>
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // 返回 "kimchi"
                                    // "kimchi" 是分数最高的韩式料理，评分为 9 。
foodRatings.highestRated("japanese"); // 返回 "ramen"
                                      // "ramen" 是分数最高的日式料理，评分为 14 。
foodRatings.changeRating("sushi", 16); // "sushi" 现在评分变更为 16 。
foodRatings.highestRated("japanese"); // 返回 "sushi"
                                      // "sushi" 是分数最高的日式料理，评分为 16 。
foodRatings.changeRating("ramen", 16); // "ramen" 现在评分变更为 16 。
foodRatings.highestRated("japanese"); // 返回 "ramen"
                                      // "sushi" 和 "ramen" 的评分都是 16 。
                                      // 但是，"ramen" 的字典序比 "sushi" 更小。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>n == foods.length == cuisines.length == ratings.length</code></li>
	<li><code>1 &lt;= foods[i].length, cuisines[i].length &lt;= 10</code></li>
	<li><code>foods[i]</code>、<code>cuisines[i]</code> 由小写英文字母组成</li>
	<li><code>1 &lt;= ratings[i] &lt;= 10<sup>8</sup></code></li>
	<li><code>foods</code> 中的所有字符串 <strong>互不相同</strong></li>
	<li>在对&nbsp;<code>changeRating</code> 的所有调用中，<code>food</code> 是系统中食物的名字。</li>
	<li>在对&nbsp;<code>highestRated</code> 的所有调用中，<code>cuisine</code> 是系统中 <strong>至少一种</strong> 食物的烹饪方式。</li>
	<li>最多调用 <code>changeRating</code> 和 <code>highestRated</code> <strong>总计</strong> <code>2 * 10<sup>4</sup></code> 次</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 哈希表
- 字符串
- 有序集合
- 堆（优先队列）

## 提示

1. The key to solving this problem is to properly store the data using the right data structures.
2. Firstly, a hash table is needed to efficiently map each food item to its cuisine and current rating.
3. In addition, another hash table is needed to map cuisines to foods within each cuisine stored in an ordered set according to their ratings.

## 示例

```
["FoodRatings","highestRated","highestRated","changeRating","highestRated","changeRating","highestRated"]
[[["kimchi","miso","sushi","moussaka","ramen","bulgogi"],["korean","japanese","japanese","greek","japanese","korean"],[9,12,8,15,14,7]],["korean"],["japanese"],["sushi",16],["japanese"],["ramen",16],["japanese"]]
```

## 示例代码

### C++

```cpp
class FoodRatings {
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        
    }
    
    void changeRating(string food, int newRating) {
        
    }
    
    string highestRated(string cuisine) {
        
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */
```

### Java

```java
class FoodRatings {

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        
    }
    
    public void changeRating(String food, int newRating) {
        
    }
    
    public String highestRated(String cuisine) {
        
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.changeRating(food,newRating);
 * String param_2 = obj.highestRated(cuisine);
 */
```

### Python

```python
class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
```

### Python3

```python3
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        

    def changeRating(self, food: str, newRating: int) -> None:
        

    def highestRated(self, cuisine: str) -> str:
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
```

### C

```c



typedef struct {
    
} FoodRatings;


FoodRatings* foodRatingsCreate(char** foods, int foodsSize, char** cuisines, int cuisinesSize, int* ratings, int ratingsSize) {
    
}

void foodRatingsChangeRating(FoodRatings* obj, char* food, int newRating) {
    
}

char* foodRatingsHighestRated(FoodRatings* obj, char* cuisine) {
    
}

void foodRatingsFree(FoodRatings* obj) {
    
}

/**
 * Your FoodRatings struct will be instantiated and called as such:
 * FoodRatings* obj = foodRatingsCreate(foods, foodsSize, cuisines, cuisinesSize, ratings, ratingsSize);
 * foodRatingsChangeRating(obj, food, newRating);
 
 * char* param_2 = foodRatingsHighestRated(obj, cuisine);
 
 * foodRatingsFree(obj);
*/
```

### C#

```csharp
public class FoodRatings {

    public FoodRatings(string[] foods, string[] cuisines, int[] ratings) {
        
    }
    
    public void ChangeRating(string food, int newRating) {
        
    }
    
    public string HighestRated(string cuisine) {
        
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.ChangeRating(food,newRating);
 * string param_2 = obj.HighestRated(cuisine);
 */
```

### JavaScript

```javascript
/**
 * @param {string[]} foods
 * @param {string[]} cuisines
 * @param {number[]} ratings
 */
var FoodRatings = function(foods, cuisines, ratings) {
    
};

/** 
 * @param {string} food 
 * @param {number} newRating
 * @return {void}
 */
FoodRatings.prototype.changeRating = function(food, newRating) {
    
};

/** 
 * @param {string} cuisine
 * @return {string}
 */
FoodRatings.prototype.highestRated = function(cuisine) {
    
};

/** 
 * Your FoodRatings object will be instantiated and called as such:
 * var obj = new FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food,newRating)
 * var param_2 = obj.highestRated(cuisine)
 */
```

### TypeScript

```typescript
class FoodRatings {
    constructor(foods: string[], cuisines: string[], ratings: number[]) {
        
    }

    changeRating(food: string, newRating: number): void {
        
    }

    highestRated(cuisine: string): string {
        
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * var obj = new FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food,newRating)
 * var param_2 = obj.highestRated(cuisine)
 */
```

### PHP

```php
class FoodRatings {
    /**
     * @param String[] $foods
     * @param String[] $cuisines
     * @param Integer[] $ratings
     */
    function __construct($foods, $cuisines, $ratings) {
        
    }
  
    /**
     * @param String $food
     * @param Integer $newRating
     * @return NULL
     */
    function changeRating($food, $newRating) {
        
    }
  
    /**
     * @param String $cuisine
     * @return String
     */
    function highestRated($cuisine) {
        
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * $obj = FoodRatings($foods, $cuisines, $ratings);
 * $obj->changeRating($food, $newRating);
 * $ret_2 = $obj->highestRated($cuisine);
 */
```

### Swift

```swift

class FoodRatings {

    init(_ foods: [String], _ cuisines: [String], _ ratings: [Int]) {
        
    }
    
    func changeRating(_ food: String, _ newRating: Int) {
        
    }
    
    func highestRated(_ cuisine: String) -> String {
        
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * let obj = FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food, newRating)
 * let ret_2: String = obj.highestRated(cuisine)
 */
```

### Kotlin

```kotlin
class FoodRatings(foods: Array<String>, cuisines: Array<String>, ratings: IntArray) {

    fun changeRating(food: String, newRating: Int) {
        
    }

    fun highestRated(cuisine: String): String {
        
    }

}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * var obj = FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food,newRating)
 * var param_2 = obj.highestRated(cuisine)
 */
```

### Dart

```dart
class FoodRatings {

  FoodRatings(List<String> foods, List<String> cuisines, List<int> ratings) {
    
  }
  
  void changeRating(String food, int newRating) {
    
  }
  
  String highestRated(String cuisine) {
    
  }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = FoodRatings(foods, cuisines, ratings);
 * obj.changeRating(food,newRating);
 * String param2 = obj.highestRated(cuisine);
 */
```

### Go

```golang
type FoodRatings struct {
    
}


func Constructor(foods []string, cuisines []string, ratings []int) FoodRatings {
    
}


func (this *FoodRatings) ChangeRating(food string, newRating int)  {
    
}


func (this *FoodRatings) HighestRated(cuisine string) string {
    
}


/**
 * Your FoodRatings object will be instantiated and called as such:
 * obj := Constructor(foods, cuisines, ratings);
 * obj.ChangeRating(food,newRating);
 * param_2 := obj.HighestRated(cuisine);
 */
```

### Ruby

```ruby
class FoodRatings

=begin
    :type foods: String[]
    :type cuisines: String[]
    :type ratings: Integer[]
=end
    def initialize(foods, cuisines, ratings)
        
    end


=begin
    :type food: String
    :type new_rating: Integer
    :rtype: Void
=end
    def change_rating(food, new_rating)
        
    end


=begin
    :type cuisine: String
    :rtype: String
=end
    def highest_rated(cuisine)
        
    end


end

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings.new(foods, cuisines, ratings)
# obj.change_rating(food, new_rating)
# param_2 = obj.highest_rated(cuisine)
```

### Scala

```scala
class FoodRatings(_foods: Array[String], _cuisines: Array[String], _ratings: Array[Int]) {

    def changeRating(food: String, newRating: Int): Unit = {
        
    }

    def highestRated(cuisine: String): String = {
        
    }

}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * val obj = new FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food,newRating)
 * val param_2 = obj.highestRated(cuisine)
 */
```

### Rust

```rust
struct FoodRatings {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FoodRatings {

    fn new(foods: Vec<String>, cuisines: Vec<String>, ratings: Vec<i32>) -> Self {
        
    }
    
    fn change_rating(&self, food: String, new_rating: i32) {
        
    }
    
    fn highest_rated(&self, cuisine: String) -> String {
        
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * let obj = FoodRatings::new(foods, cuisines, ratings);
 * obj.change_rating(food, newRating);
 * let ret_2: String = obj.highest_rated(cuisine);
 */
```

### Racket

```racket
(define food-ratings%
  (class object%
    (super-new)
    
    ; foods : (listof string?)
    ; cuisines : (listof string?)
    ; ratings : (listof exact-integer?)
    (init-field
      foods
      cuisines
      ratings)
    
    ; change-rating : string? exact-integer? -> void?
    (define/public (change-rating food new-rating)
      )
    ; highest-rated : string? -> string?
    (define/public (highest-rated cuisine)
      )))

;; Your food-ratings% object will be instantiated and called as such:
;; (define obj (new food-ratings% [foods foods] [cuisines cuisines] [ratings ratings]))
;; (send obj change-rating food new-rating)
;; (define param_2 (send obj highest-rated cuisine))
```

### Erlang

```erlang
-spec food_ratings_init_(Foods :: [unicode:unicode_binary()], Cuisines :: [unicode:unicode_binary()], Ratings :: [integer()]) -> any().
food_ratings_init_(Foods, Cuisines, Ratings) ->
  .

-spec food_ratings_change_rating(Food :: unicode:unicode_binary(), NewRating :: integer()) -> any().
food_ratings_change_rating(Food, NewRating) ->
  .

-spec food_ratings_highest_rated(Cuisine :: unicode:unicode_binary()) -> unicode:unicode_binary().
food_ratings_highest_rated(Cuisine) ->
  .


%% Your functions will be called as such:
%% food_ratings_init_(Foods, Cuisines, Ratings),
%% food_ratings_change_rating(Food, NewRating),
%% Param_2 = food_ratings_highest_rated(Cuisine),

%% food_ratings_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule FoodRatings do
  @spec init_(foods :: [String.t], cuisines :: [String.t], ratings :: [integer]) :: any
  def init_(foods, cuisines, ratings) do
    
  end

  @spec change_rating(food :: String.t, new_rating :: integer) :: any
  def change_rating(food, new_rating) do
    
  end

  @spec highest_rated(cuisine :: String.t) :: String.t
  def highest_rated(cuisine) do
    
  end
end

# Your functions will be called as such:
# FoodRatings.init_(foods, cuisines, ratings)
# FoodRatings.change_rating(food, new_rating)
# param_2 = FoodRatings.highest_rated(cuisine)

# FoodRatings.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class FoodRatings {
    init(foods: Array<String>, cuisines: Array<String>, ratings: Array<Int64>) {

    }
    
    func changeRating(food: String, newRating: Int64): Unit {

    }
    
    func highestRated(cuisine: String): String {

    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * let obj: FoodRatings = FoodRatings(foods, cuisines, ratings)
 * obj.changeRating(food,newRating)
 * let param_2 = obj.highestRated(cuisine)
 */
```

