# 1396. 设计地铁系统

## 题目描述

<p>地铁系统跟踪不同车站之间的乘客出行时间，并使用这一数据来计算从一站到另一站的平均时间。</p>

<p>实现 <code>UndergroundSystem</code> 类：</p>

<ul>
	<li><code>void checkIn(int id, string stationName, int t)</code>

	<ul>
		<li>通行卡 ID 等于 <code>id</code> 的乘客，在时间 <code>t</code> ，从 <code>stationName</code> 站进入</li>
		<li>乘客一次只能从一个站进入</li>
	</ul>
	</li>
	<li><code>void checkOut(int id, string stationName, int t)</code>
	<ul>
		<li>通行卡 ID 等于 <code>id</code> 的乘客，在时间 <code>t</code> ，从 <code>stationName</code> 站离开</li>
	</ul>
	</li>
	<li><code>double getAverageTime(string startStation, string endStation)</code>
	<ul>
		<li>返回从 <code>startStation</code> 站到 <code>endStation</code> 站的平均时间</li>
		<li>平均时间会根据截至目前所有从 <code>startStation</code> 站 <strong>直接</strong> 到达 <code>endStation</code> 站的行程进行计算，也就是从 <code>startStation</code> 站进入并从 <code>endStation</code> 离开的行程</li>
		<li>从 <code>startStation</code> 到 <code>endStation</code> 的行程时间与从 <code>endStation</code> 到 <code>startStation</code> 的行程时间可能不同</li>
		<li>在调用 <code>getAverageTime</code> 之前，至少有一名乘客从 <code>startStation</code> 站到达 <code>endStation</code> 站</li>
	</ul>
	</li>
</ul>

<p>你可以假设对 <code>checkIn</code> 和 <code>checkOut</code> 方法的所有调用都是符合逻辑的。如果一名乘客在时间 <code>t<sub>1</sub></code> 进站、时间 <code>t<sub>2</sub></code> 出站，那么 <code>t<sub>1</sub> &lt; t<sub>2</sub></code> 。所有时间都按时间顺序发生。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入</strong>
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

<strong>输出</strong>
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

<strong>解释</strong>
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);  // 乘客 45 "Leyton" -&gt; "Waterloo" ，用时 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20);  // 乘客 27 "Leyton" -&gt; "Waterloo" ，用时 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22); // 乘客 32 "Paradise" -&gt; "Cambridge" ，用时 22-8 = 14
undergroundSystem.getAverageTime("Paradise", "Cambridge"); // 返回 14.00000 。只有一个 "Paradise" -&gt; "Cambridge" 的行程，(14) / 1 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // 返回 11.00000 。有两个 "Leyton" -&gt; "Waterloo" 的行程，(10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // 返回 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);  // 乘客 10 "Leyton" -&gt; "Waterloo" ，用时 38-24 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // 返回 12.00000 。有三个 "Leyton" -&gt; "Waterloo" 的行程，(10 + 12 + 14) / 3 = 12
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入</strong>
["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
[[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]

<strong>输出</strong>
[null,null,null,5.00000,null,null,5.50000,null,null,6.66667]

<strong>解释</strong>
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(10, "Leyton", 3);
undergroundSystem.checkOut(10, "Paradise", 8); // 乘客 10 "Leyton" -&gt; "Paradise" ，用时 8-3 = 5
undergroundSystem.getAverageTime("Leyton", "Paradise"); // 返回 5.00000 ，(5) / 1 = 5
undergroundSystem.checkIn(5, "Leyton", 10);
undergroundSystem.checkOut(5, "Paradise", 16); // 乘客 5 "Leyton" -&gt; "Paradise" ，用时 16-10 = 6
undergroundSystem.getAverageTime("Leyton", "Paradise"); // 返回 5.50000 ，(5 + 6) / 2 = 5.5
undergroundSystem.checkIn(2, "Leyton", 21);
undergroundSystem.checkOut(2, "Paradise", 30); // 乘客 2 "Leyton" -&gt; "Paradise" ，用时 30-21 = 9
undergroundSystem.getAverageTime("Leyton", "Paradise"); // 返回 6.66667 ，(5 + 6 + 9) / 3 = 6.66667
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= id, t &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= stationName.length, startStation.length, endStation.length &lt;= 10</code> 次</li>
	<li>所有字符串由大小写英文字母与数字组成</li>
	<li>总共最多调用 <code>checkIn</code>、<code>checkOut</code> 和 <code>getAverageTime</code> 方法 <code>2 * 10<sup>4 </sup></code></li>
	<li>与标准答案误差在 <code>10<sup>-5</sup></code> 以内的结果都被视为正确结果</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 哈希表
- 字符串

## 提示

1. Use two hash tables. The first to save the check-in time for a customer and the second to update the total time between two stations.

## 示例

```
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
[[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]
```

## 示例代码

### C++

```cpp
class UndergroundSystem {
public:
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, string stationName, int t) {
        
    }
    
    void checkOut(int id, string stationName, int t) {
        
    }
    
    double getAverageTime(string startStation, string endStation) {
        
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */
```

### Java

```java
class UndergroundSystem {

    public UndergroundSystem() {
        
    }
    
    public void checkIn(int id, String stationName, int t) {
        
    }
    
    public void checkOut(int id, String stationName, int t) {
        
    }
    
    public double getAverageTime(String startStation, String endStation) {
        
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */
```

### Python

```python
class UndergroundSystem(object):

    def __init__(self):
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
```

### Python3

```python3
class UndergroundSystem:

    def __init__(self):
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
```

### C

```c



typedef struct {
    
} UndergroundSystem;


UndergroundSystem* undergroundSystemCreate() {
    
}

void undergroundSystemCheckIn(UndergroundSystem* obj, int id, char* stationName, int t) {
    
}

void undergroundSystemCheckOut(UndergroundSystem* obj, int id, char* stationName, int t) {
    
}

double undergroundSystemGetAverageTime(UndergroundSystem* obj, char* startStation, char* endStation) {
    
}

void undergroundSystemFree(UndergroundSystem* obj) {
    
}

/**
 * Your UndergroundSystem struct will be instantiated and called as such:
 * UndergroundSystem* obj = undergroundSystemCreate();
 * undergroundSystemCheckIn(obj, id, stationName, t);
 
 * undergroundSystemCheckOut(obj, id, stationName, t);
 
 * double param_3 = undergroundSystemGetAverageTime(obj, startStation, endStation);
 
 * undergroundSystemFree(obj);
*/
```

### C#

```csharp
public class UndergroundSystem {

    public UndergroundSystem() {
        
    }
    
    public void CheckIn(int id, string stationName, int t) {
        
    }
    
    public void CheckOut(int id, string stationName, int t) {
        
    }
    
    public double GetAverageTime(string startStation, string endStation) {
        
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * double param_3 = obj.GetAverageTime(startStation,endStation);
 */
```

### JavaScript

```javascript

var UndergroundSystem = function() {
    
};

/** 
 * @param {number} id 
 * @param {string} stationName 
 * @param {number} t
 * @return {void}
 */
UndergroundSystem.prototype.checkIn = function(id, stationName, t) {
    
};

/** 
 * @param {number} id 
 * @param {string} stationName 
 * @param {number} t
 * @return {void}
 */
UndergroundSystem.prototype.checkOut = function(id, stationName, t) {
    
};

/** 
 * @param {string} startStation 
 * @param {string} endStation
 * @return {number}
 */
UndergroundSystem.prototype.getAverageTime = function(startStation, endStation) {
    
};

/** 
 * Your UndergroundSystem object will be instantiated and called as such:
 * var obj = new UndergroundSystem()
 * obj.checkIn(id,stationName,t)
 * obj.checkOut(id,stationName,t)
 * var param_3 = obj.getAverageTime(startStation,endStation)
 */
```

### TypeScript

```typescript
class UndergroundSystem {
    constructor() {
        
    }

    checkIn(id: number, stationName: string, t: number): void {
        
    }

    checkOut(id: number, stationName: string, t: number): void {
        
    }

    getAverageTime(startStation: string, endStation: string): number {
        
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * var obj = new UndergroundSystem()
 * obj.checkIn(id,stationName,t)
 * obj.checkOut(id,stationName,t)
 * var param_3 = obj.getAverageTime(startStation,endStation)
 */
```

### PHP

```php
class UndergroundSystem {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer $id
     * @param String $stationName
     * @param Integer $t
     * @return NULL
     */
    function checkIn($id, $stationName, $t) {
        
    }
  
    /**
     * @param Integer $id
     * @param String $stationName
     * @param Integer $t
     * @return NULL
     */
    function checkOut($id, $stationName, $t) {
        
    }
  
    /**
     * @param String $startStation
     * @param String $endStation
     * @return Float
     */
    function getAverageTime($startStation, $endStation) {
        
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * $obj = UndergroundSystem();
 * $obj->checkIn($id, $stationName, $t);
 * $obj->checkOut($id, $stationName, $t);
 * $ret_3 = $obj->getAverageTime($startStation, $endStation);
 */
```

### Swift

```swift

class UndergroundSystem {

    init() {
        
    }
    
    func checkIn(_ id: Int, _ stationName: String, _ t: Int) {
        
    }
    
    func checkOut(_ id: Int, _ stationName: String, _ t: Int) {
        
    }
    
    func getAverageTime(_ startStation: String, _ endStation: String) -> Double {
        
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * let obj = UndergroundSystem()
 * obj.checkIn(id, stationName, t)
 * obj.checkOut(id, stationName, t)
 * let ret_3: Double = obj.getAverageTime(startStation, endStation)
 */
```

### Kotlin

```kotlin
class UndergroundSystem() {

    fun checkIn(id: Int, stationName: String, t: Int) {
        
    }

    fun checkOut(id: Int, stationName: String, t: Int) {
        
    }

    fun getAverageTime(startStation: String, endStation: String): Double {
        
    }

}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * var obj = UndergroundSystem()
 * obj.checkIn(id,stationName,t)
 * obj.checkOut(id,stationName,t)
 * var param_3 = obj.getAverageTime(startStation,endStation)
 */
```

### Dart

```dart
class UndergroundSystem {

  UndergroundSystem() {
    
  }
  
  void checkIn(int id, String stationName, int t) {
    
  }
  
  void checkOut(int id, String stationName, int t) {
    
  }
  
  double getAverageTime(String startStation, String endStation) {
    
  }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param3 = obj.getAverageTime(startStation,endStation);
 */
```

### Go

```golang
type UndergroundSystem struct {
    
}


func Constructor() UndergroundSystem {
    
}


func (this *UndergroundSystem) CheckIn(id int, stationName string, t int)  {
    
}


func (this *UndergroundSystem) CheckOut(id int, stationName string, t int)  {
    
}


func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
    
}


/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * param_3 := obj.GetAverageTime(startStation,endStation);
 */
```

### Ruby

```ruby
class UndergroundSystem
    def initialize()
        
    end


=begin
    :type id: Integer
    :type station_name: String
    :type t: Integer
    :rtype: Void
=end
    def check_in(id, station_name, t)
        
    end


=begin
    :type id: Integer
    :type station_name: String
    :type t: Integer
    :rtype: Void
=end
    def check_out(id, station_name, t)
        
    end


=begin
    :type start_station: String
    :type end_station: String
    :rtype: Float
=end
    def get_average_time(start_station, end_station)
        
    end


end

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem.new()
# obj.check_in(id, station_name, t)
# obj.check_out(id, station_name, t)
# param_3 = obj.get_average_time(start_station, end_station)
```

### Scala

```scala
class UndergroundSystem() {

    def checkIn(id: Int, stationName: String, t: Int): Unit = {
        
    }

    def checkOut(id: Int, stationName: String, t: Int): Unit = {
        
    }

    def getAverageTime(startStation: String, endStation: String): Double = {
        
    }

}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * val obj = new UndergroundSystem()
 * obj.checkIn(id,stationName,t)
 * obj.checkOut(id,stationName,t)
 * val param_3 = obj.getAverageTime(startStation,endStation)
 */
```

### Rust

```rust
struct UndergroundSystem {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl UndergroundSystem {

    fn new() -> Self {
        
    }
    
    fn check_in(&self, id: i32, station_name: String, t: i32) {
        
    }
    
    fn check_out(&self, id: i32, station_name: String, t: i32) {
        
    }
    
    fn get_average_time(&self, start_station: String, end_station: String) -> f64 {
        
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * let obj = UndergroundSystem::new();
 * obj.check_in(id, stationName, t);
 * obj.check_out(id, stationName, t);
 * let ret_3: f64 = obj.get_average_time(startStation, endStation);
 */
```

### Racket

```racket
(define underground-system%
  (class object%
    (super-new)
    
    (init-field)
    
    ; check-in : exact-integer? string? exact-integer? -> void?
    (define/public (check-in id station-name t)
      )
    ; check-out : exact-integer? string? exact-integer? -> void?
    (define/public (check-out id station-name t)
      )
    ; get-average-time : string? string? -> flonum?
    (define/public (get-average-time start-station end-station)
      )))

;; Your underground-system% object will be instantiated and called as such:
;; (define obj (new underground-system%))
;; (send obj check-in id station-name t)
;; (send obj check-out id station-name t)
;; (define param_3 (send obj get-average-time start-station end-station))
```

### Erlang

```erlang
-spec underground_system_init_() -> any().
underground_system_init_() ->
  .

-spec underground_system_check_in(Id :: integer(), StationName :: unicode:unicode_binary(), T :: integer()) -> any().
underground_system_check_in(Id, StationName, T) ->
  .

-spec underground_system_check_out(Id :: integer(), StationName :: unicode:unicode_binary(), T :: integer()) -> any().
underground_system_check_out(Id, StationName, T) ->
  .

-spec underground_system_get_average_time(StartStation :: unicode:unicode_binary(), EndStation :: unicode:unicode_binary()) -> float().
underground_system_get_average_time(StartStation, EndStation) ->
  .


%% Your functions will be called as such:
%% underground_system_init_(),
%% underground_system_check_in(Id, StationName, T),
%% underground_system_check_out(Id, StationName, T),
%% Param_3 = underground_system_get_average_time(StartStation, EndStation),

%% underground_system_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule UndergroundSystem do
  @spec init_() :: any
  def init_() do
    
  end

  @spec check_in(id :: integer, station_name :: String.t, t :: integer) :: any
  def check_in(id, station_name, t) do
    
  end

  @spec check_out(id :: integer, station_name :: String.t, t :: integer) :: any
  def check_out(id, station_name, t) do
    
  end

  @spec get_average_time(start_station :: String.t, end_station :: String.t) :: float
  def get_average_time(start_station, end_station) do
    
  end
end

# Your functions will be called as such:
# UndergroundSystem.init_()
# UndergroundSystem.check_in(id, station_name, t)
# UndergroundSystem.check_out(id, station_name, t)
# param_3 = UndergroundSystem.get_average_time(start_station, end_station)

# UndergroundSystem.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class UndergroundSystem {
    init() {

    }
    
    func checkIn(id: Int64, stationName: String, t: Int64): Unit {

    }
    
    func checkOut(id: Int64, stationName: String, t: Int64): Unit {

    }
    
    func getAverageTime(startStation: String, endStation: String): Float64 {

    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * let obj: UndergroundSystem = UndergroundSystem()
 * obj.checkIn(id,stationName,t)
 * obj.checkOut(id,stationName,t)
 * let param_3 = obj.getAverageTime(startStation,endStation)
 */
```

