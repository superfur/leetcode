# 1348. 推文计数

## 题目描述

<p>一家社交媒体公司正试图通过分析特定时间段内出现的推文数量来监控其网站上的活动。这些时间段可以根据特定的频率（&nbsp;<strong>每分钟&nbsp;</strong>、<strong>每小时&nbsp;</strong>或 <strong>每一天</strong> ）划分为更小的 <strong>时间段</strong> 。</p>

<p>&nbsp;</p>

<p>例如，周期 <code>[10,10000]</code>&nbsp;（以 <strong>秒</strong> 为单位）将被划分为以下频率的 <strong>时间块</strong> :</p>

<ul>
	<li>每 <strong>分钟</strong> (60秒 块)：<meta charset="UTF-8" />&nbsp;<code>[10,69]</code>,&nbsp;<code>[70,129]</code>,&nbsp;<code>[130,189]</code>,&nbsp;<code>...</code>,&nbsp;<code>[9970,10000]</code></li>
	<li>每 <strong>小时</strong> (3600秒 块)：<meta charset="UTF-8" /><code>[10,3609]</code>,&nbsp;<code>[3610,7209]</code>,&nbsp;<code>[7210,10000]</code></li>
	<li>每 <strong>天</strong> (86400秒 块)：<meta charset="UTF-8" />&nbsp;<code>[10,10000]</code></li>
</ul>

<p>注意，最后一个块可能比指定频率的块大小更短，并且总是以时间段的结束时间结束(在上面的示例中为 <code>10000</code> )。</p>

<p>设计和实现一个API来帮助公司进行分析。</p>

<p>实现 <code>TweetCounts</code> 类:</p>

<ul>
	<li><code>TweetCounts()</code> 初始化 <code>TweetCounts</code> 对象。</li>
	<li>存储记录时间的 <code>tweetName</code> (以秒为单位)。</li>
	<li><code>List&lt;integer&gt; getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime)</code>&nbsp;返回一个整数列表，表示给定时间 <code>[startTime, endTime]</code>&nbsp;（单位秒）和频率频率中，每个 <strong>时间块</strong> 中带有 <code>tweetName</code> 的 <code>tweet</code> 的数量。
	<ul>
		<li><code>freq</code> 是 <code>“minute”</code> 、 <code>“hour”</code> 或 <code>“day”</code> 中的一个，分别表示 <strong>每分钟</strong> 、 <strong>每小时</strong> 或 <strong>每一天</strong> 的频率。</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

<strong>输出：</strong>
[null,null,null,null,[2],[2,1],null,[4]]

<strong>解释：</strong>
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);
tweetCounts.recordTweet("tweet3", 60);
tweetCounts.recordTweet("tweet3", 10);                             //&nbsp;"tweet3"&nbsp;发布推文的时间分别是&nbsp;0,&nbsp;10&nbsp;和&nbsp;60 。
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); //&nbsp;返回&nbsp;[2]。统计频率是每分钟（60 秒），因此只有一个有效时间间隔 [0,60&gt;&nbsp;-&nbsp;&gt;&nbsp;2&nbsp;条推文。
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); //&nbsp;返回&nbsp;[2,1]。统计频率是每分钟（60 秒），因此有两个有效时间间隔&nbsp;<strong>1)</strong>&nbsp;[0,60&gt;&nbsp;-&nbsp;&gt;&nbsp;2&nbsp;条推文，和&nbsp;<strong>2)</strong>&nbsp;[60,61&gt;&nbsp;-&nbsp;&gt;&nbsp;1&nbsp;条推文。 
tweetCounts.recordTweet("tweet3", 120);                            // "tweet3"&nbsp;发布推文的时间分别是 0, 10, 60 和 120 。
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  //&nbsp;返回&nbsp;[4]。统计频率是每小时（3600 秒），因此只有一个有效时间间隔 [0,211&gt;&nbsp;-&nbsp;&gt;&nbsp;4&nbsp;条推文。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= time, startTime, endTime &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= endTime - startTime &lt;= 10<sup>4</sup></code></li>
	<li><code>recordTweet</code>&nbsp;和&nbsp;<code>getTweetCountsPerFrequency</code>，最多有<meta charset="UTF-8" />&nbsp;<code>10<sup>4</sup></code>&nbsp;次操作。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 哈希表
- 二分查找
- 有序集合
- 排序

## 示例

```
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]
```

## 示例代码

### C++

```cpp
class TweetCounts {
public:
    TweetCounts() {
        
    }
    
    void recordTweet(string tweetName, int time) {
        
    }
    
    vector<int> getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime) {
        
    }
};

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts* obj = new TweetCounts();
 * obj->recordTweet(tweetName,time);
 * vector<int> param_2 = obj->getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
```

### Java

```java
class TweetCounts {

    public TweetCounts() {
        
    }
    
    public void recordTweet(String tweetName, int time) {
        
    }
    
    public List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) {
        
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts obj = new TweetCounts();
 * obj.recordTweet(tweetName,time);
 * List<Integer> param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
```

### Python

```python
class TweetCounts(object):

    def __init__(self):
        

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
```

### Python3

```python3
class TweetCounts:

    def __init__(self):
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
```

### C

```c



typedef struct {
    
} TweetCounts;


TweetCounts* tweetCountsCreate() {
    
}

void tweetCountsRecordTweet(TweetCounts* obj, char* tweetName, int time) {
    
}

int* tweetCountsGetTweetCountsPerFrequency(TweetCounts* obj, char* freq, char* tweetName, int startTime, int endTime, int* retSize) {
    
}

void tweetCountsFree(TweetCounts* obj) {
    
}

/**
 * Your TweetCounts struct will be instantiated and called as such:
 * TweetCounts* obj = tweetCountsCreate();
 * tweetCountsRecordTweet(obj, tweetName, time);
 
 * int* param_2 = tweetCountsGetTweetCountsPerFrequency(obj, freq, tweetName, startTime, endTime, retSize);
 
 * tweetCountsFree(obj);
*/
```

### C#

```csharp
public class TweetCounts {

    public TweetCounts() {
        
    }
    
    public void RecordTweet(string tweetName, int time) {
        
    }
    
    public IList<int> GetTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime) {
        
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts obj = new TweetCounts();
 * obj.RecordTweet(tweetName,time);
 * IList<int> param_2 = obj.GetTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
```

### JavaScript

```javascript

var TweetCounts = function() {
    
};

/** 
 * @param {string} tweetName 
 * @param {number} time
 * @return {void}
 */
TweetCounts.prototype.recordTweet = function(tweetName, time) {
    
};

/** 
 * @param {string} freq 
 * @param {string} tweetName 
 * @param {number} startTime 
 * @param {number} endTime
 * @return {number[]}
 */
TweetCounts.prototype.getTweetCountsPerFrequency = function(freq, tweetName, startTime, endTime) {
    
};

/** 
 * Your TweetCounts object will be instantiated and called as such:
 * var obj = new TweetCounts()
 * obj.recordTweet(tweetName,time)
 * var param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
 */
```

### TypeScript

```typescript
class TweetCounts {
    constructor() {
        
    }

    recordTweet(tweetName: string, time: number): void {
        
    }

    getTweetCountsPerFrequency(freq: string, tweetName: string, startTime: number, endTime: number): number[] {
        
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * var obj = new TweetCounts()
 * obj.recordTweet(tweetName,time)
 * var param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
 */
```

### PHP

```php
class TweetCounts {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param String $tweetName
     * @param Integer $time
     * @return NULL
     */
    function recordTweet($tweetName, $time) {
        
    }
  
    /**
     * @param String $freq
     * @param String $tweetName
     * @param Integer $startTime
     * @param Integer $endTime
     * @return Integer[]
     */
    function getTweetCountsPerFrequency($freq, $tweetName, $startTime, $endTime) {
        
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * $obj = TweetCounts();
 * $obj->recordTweet($tweetName, $time);
 * $ret_2 = $obj->getTweetCountsPerFrequency($freq, $tweetName, $startTime, $endTime);
 */
```

### Swift

```swift

class TweetCounts {

    init() {
        
    }
    
    func recordTweet(_ tweetName: String, _ time: Int) {
        
    }
    
    func getTweetCountsPerFrequency(_ freq: String, _ tweetName: String, _ startTime: Int, _ endTime: Int) -> [Int] {
        
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * let obj = TweetCounts()
 * obj.recordTweet(tweetName, time)
 * let ret_2: [Int] = obj.getTweetCountsPerFrequency(freq, tweetName, startTime, endTime)
 */
```

### Kotlin

```kotlin
class TweetCounts() {

    fun recordTweet(tweetName: String, time: Int) {
        
    }

    fun getTweetCountsPerFrequency(freq: String, tweetName: String, startTime: Int, endTime: Int): List<Int> {
        
    }

}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * var obj = TweetCounts()
 * obj.recordTweet(tweetName,time)
 * var param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
 */
```

### Dart

```dart
class TweetCounts {

  TweetCounts() {
    
  }
  
  void recordTweet(String tweetName, int time) {
    
  }
  
  List<int> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) {
    
  }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts obj = TweetCounts();
 * obj.recordTweet(tweetName,time);
 * List<int> param2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
```

### Go

```golang
type TweetCounts struct {
    
}


func Constructor() TweetCounts {
    
}


func (this *TweetCounts) RecordTweet(tweetName string, time int)  {
    
}


func (this *TweetCounts) GetTweetCountsPerFrequency(freq string, tweetName string, startTime int, endTime int) []int {
    
}


/**
 * Your TweetCounts object will be instantiated and called as such:
 * obj := Constructor();
 * obj.RecordTweet(tweetName,time);
 * param_2 := obj.GetTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
```

### Ruby

```ruby
class TweetCounts
    def initialize()
        
    end


=begin
    :type tweet_name: String
    :type time: Integer
    :rtype: Void
=end
    def record_tweet(tweet_name, time)
        
    end


=begin
    :type freq: String
    :type tweet_name: String
    :type start_time: Integer
    :type end_time: Integer
    :rtype: Integer[]
=end
    def get_tweet_counts_per_frequency(freq, tweet_name, start_time, end_time)
        
    end


end

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts.new()
# obj.record_tweet(tweet_name, time)
# param_2 = obj.get_tweet_counts_per_frequency(freq, tweet_name, start_time, end_time)
```

### Scala

```scala
class TweetCounts() {

    def recordTweet(tweetName: String, time: Int): Unit = {
        
    }

    def getTweetCountsPerFrequency(freq: String, tweetName: String, startTime: Int, endTime: Int): List[Int] = {
        
    }

}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * val obj = new TweetCounts()
 * obj.recordTweet(tweetName,time)
 * val param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
 */
```

### Rust

```rust
struct TweetCounts {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TweetCounts {

    fn new() -> Self {
        
    }
    
    fn record_tweet(&self, tweet_name: String, time: i32) {
        
    }
    
    fn get_tweet_counts_per_frequency(&self, freq: String, tweet_name: String, start_time: i32, end_time: i32) -> Vec<i32> {
        
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * let obj = TweetCounts::new();
 * obj.record_tweet(tweetName, time);
 * let ret_2: Vec<i32> = obj.get_tweet_counts_per_frequency(freq, tweetName, startTime, endTime);
 */
```

### Racket

```racket
(define tweet-counts%
  (class object%
    (super-new)
    
    (init-field)
    
    ; record-tweet : string? exact-integer? -> void?
    (define/public (record-tweet tweet-name time)
      )
    ; get-tweet-counts-per-frequency : string? string? exact-integer? exact-integer? -> (listof exact-integer?)
    (define/public (get-tweet-counts-per-frequency freq tweet-name start-time end-time)
      )))

;; Your tweet-counts% object will be instantiated and called as such:
;; (define obj (new tweet-counts%))
;; (send obj record-tweet tweet-name time)
;; (define param_2 (send obj get-tweet-counts-per-frequency freq tweet-name start-time end-time))
```

### Erlang

```erlang
-spec tweet_counts_init_() -> any().
tweet_counts_init_() ->
  .

-spec tweet_counts_record_tweet(TweetName :: unicode:unicode_binary(), Time :: integer()) -> any().
tweet_counts_record_tweet(TweetName, Time) ->
  .

-spec tweet_counts_get_tweet_counts_per_frequency(Freq :: unicode:unicode_binary(), TweetName :: unicode:unicode_binary(), StartTime :: integer(), EndTime :: integer()) -> [integer()].
tweet_counts_get_tweet_counts_per_frequency(Freq, TweetName, StartTime, EndTime) ->
  .


%% Your functions will be called as such:
%% tweet_counts_init_(),
%% tweet_counts_record_tweet(TweetName, Time),
%% Param_2 = tweet_counts_get_tweet_counts_per_frequency(Freq, TweetName, StartTime, EndTime),

%% tweet_counts_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule TweetCounts do
  @spec init_() :: any
  def init_() do
    
  end

  @spec record_tweet(tweet_name :: String.t, time :: integer) :: any
  def record_tweet(tweet_name, time) do
    
  end

  @spec get_tweet_counts_per_frequency(freq :: String.t, tweet_name :: String.t, start_time :: integer, end_time :: integer) :: [integer]
  def get_tweet_counts_per_frequency(freq, tweet_name, start_time, end_time) do
    
  end
end

# Your functions will be called as such:
# TweetCounts.init_()
# TweetCounts.record_tweet(tweet_name, time)
# param_2 = TweetCounts.get_tweet_counts_per_frequency(freq, tweet_name, start_time, end_time)

# TweetCounts.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class TweetCounts {
    init() {

    }
    
    func recordTweet(tweetName: String, time: Int64): Unit {

    }
    
    func getTweetCountsPerFrequency(freq: String, tweetName: String, startTime: Int64, endTime: Int64): ArrayList<Int64> {

    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * let obj: TweetCounts = TweetCounts()
 * obj.recordTweet(tweetName,time)
 * let param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
 */
```

