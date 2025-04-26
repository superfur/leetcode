# 2069. 模拟行走机器人 II

## 题目描述

<p>给你一个在 XY 平面上的&nbsp;<code>width x height</code>&nbsp;的网格图，<strong>左下角</strong>&nbsp;的格子为&nbsp;<code>(0, 0)</code>&nbsp;，<strong>右上角</strong>&nbsp;的格子为&nbsp;<code>(width - 1, height - 1)</code>&nbsp;。网格图中相邻格子为四个基本方向之一（<code>"North"</code>，<code>"East"</code>，<code>"South"</code>&nbsp;和&nbsp;<code>"West"</code>）。一个机器人 <strong>初始</strong>&nbsp;在格子&nbsp;<code>(0, 0)</code>&nbsp;，方向为&nbsp;<code>"East"</code>&nbsp;。</p>

<p>机器人可以根据指令移动指定的 <strong>步数</strong>&nbsp;。每一步，它可以执行以下操作。</p>

<ol>
	<li>沿着当前方向尝试 <strong>往前一步</strong>&nbsp;。</li>
	<li>如果机器人下一步将到达的格子 <strong>超出了边界</strong>&nbsp;，机器人会 <strong>逆时针</strong>&nbsp;转 90 度，然后再尝试往前一步。</li>
</ol>

<p>如果机器人完成了指令要求的移动步数，它将停止移动并等待下一个指令。</p>

<p>请你实现&nbsp;<code>Robot</code>&nbsp;类：</p>

<ul>
	<li><code>Robot(int width, int height)</code>&nbsp;初始化一个&nbsp;<code>width x height</code>&nbsp;的网格图，机器人初始在&nbsp;<code>(0, 0)</code>&nbsp;，方向朝&nbsp;<code>"East"</code>&nbsp;。</li>
	<li><code>void step(int num)</code>&nbsp;给机器人下达前进&nbsp;<code>num</code>&nbsp;步的指令。</li>
	<li><code>int[] getPos()</code>&nbsp;返回机器人当前所处的格子位置，用一个长度为 2 的数组&nbsp;<code>[x, y]</code>&nbsp;表示。</li>
	<li><code>String getDir()</code>&nbsp;返回当前机器人的朝向，为&nbsp;<code>"North"</code>&nbsp;，<code>"East"</code>&nbsp;，<code>"South"</code>&nbsp;或者&nbsp;<code>"West"</code>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="example-1" src="https://assets.leetcode.com/uploads/2021/10/09/example-1.png" style="width: 498px; height: 268px;" /></p>

<pre>
<strong>输入：</strong>
["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
<strong>输出：</strong>
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

<strong>解释：</strong>
Robot robot = new Robot(6, 3); // 初始化网格图，机器人在 (0, 0) ，朝东。
robot.step(2);  // 机器人朝东移动 2 步，到达 (2, 0) ，并朝东。
robot.step(2);  // 机器人朝东移动 2 步，到达 (4, 0) ，并朝东。
robot.getPos(); // 返回 [4, 0]
robot.getDir(); // 返回 "East"
robot.step(2);  // 朝东移动 1 步到达 (5, 0) ，并朝东。
                // 下一步继续往东移动将出界，所以逆时针转变方向朝北。
                // 然后，往北移动 1 步到达 (5, 1) ，并朝北。
robot.step(1);  // 朝北移动 1 步到达 (5, 2) ，并朝 <strong>北</strong> （不是朝西）。
robot.step(4);  // 下一步继续往北移动将出界，所以逆时针转变方向朝西。
                // 然后，移动 4 步到 (1, 2) ，并朝西。
robot.getPos(); // 返回 [1, 2]
robot.getDir(); // 返回 "West"

</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= width, height &lt;= 100</code></li>
	<li><code>1 &lt;= num &lt;= 10<sup>5</sup></code></li>
	<li><code>step</code> ，<code>getPos</code>&nbsp;和&nbsp;<code>getDir</code>&nbsp;<strong>总共&nbsp;</strong>调用次数不超过&nbsp;<code>10<sup>4</sup></code>&nbsp;次。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 模拟

## 提示

1. The robot only moves along the perimeter of the grid. Can you think if modulus can help you quickly compute which cell it stops at?
2. After the robot moves one time, whenever the robot stops at some cell, it will always face a specific direction. i.e., The direction it faces is determined by the cell it stops at.
3. Can you precompute what direction it faces when it stops at each cell along the perimeter, and reuse the results?

## 示例

```
["Robot","step","step","getPos","getDir","step","step","step","getPos","getDir"]
[[6,3],[2],[2],[],[],[2],[1],[4],[],[]]
```

## 示例代码

### C++

```cpp
class Robot {
public:
    Robot(int width, int height) {
        
    }
    
    void step(int num) {
        
    }
    
    vector<int> getPos() {
        
    }
    
    string getDir() {
        
    }
};

/**
 * Your Robot object will be instantiated and called as such:
 * Robot* obj = new Robot(width, height);
 * obj->step(num);
 * vector<int> param_2 = obj->getPos();
 * string param_3 = obj->getDir();
 */
```

### Java

```java
class Robot {

    public Robot(int width, int height) {
        
    }
    
    public void step(int num) {
        
    }
    
    public int[] getPos() {
        
    }
    
    public String getDir() {
        
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * Robot obj = new Robot(width, height);
 * obj.step(num);
 * int[] param_2 = obj.getPos();
 * String param_3 = obj.getDir();
 */
```

### Python

```python
class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        

    def getPos(self):
        """
        :rtype: List[int]
        """
        

    def getDir(self):
        """
        :rtype: str
        """
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
```

### Python3

```python3
class Robot:

    def __init__(self, width: int, height: int):
        

    def step(self, num: int) -> None:
        

    def getPos(self) -> List[int]:
        

    def getDir(self) -> str:
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
```

### C

```c



typedef struct {
    
} Robot;


Robot* robotCreate(int width, int height) {
    
}

void robotStep(Robot* obj, int num) {
    
}

int* robotGetPos(Robot* obj, int* retSize) {
    
}

char* robotGetDir(Robot* obj) {
    
}

void robotFree(Robot* obj) {
    
}

/**
 * Your Robot struct will be instantiated and called as such:
 * Robot* obj = robotCreate(width, height);
 * robotStep(obj, num);
 
 * int* param_2 = robotGetPos(obj, retSize);
 
 * char* param_3 = robotGetDir(obj);
 
 * robotFree(obj);
*/
```

### C#

```csharp
public class Robot {

    public Robot(int width, int height) {
        
    }
    
    public void Step(int num) {
        
    }
    
    public int[] GetPos() {
        
    }
    
    public string GetDir() {
        
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * Robot obj = new Robot(width, height);
 * obj.Step(num);
 * int[] param_2 = obj.GetPos();
 * string param_3 = obj.GetDir();
 */
```

### JavaScript

```javascript
/**
 * @param {number} width
 * @param {number} height
 */
var Robot = function(width, height) {
    
};

/** 
 * @param {number} num
 * @return {void}
 */
Robot.prototype.step = function(num) {
    
};

/**
 * @return {number[]}
 */
Robot.prototype.getPos = function() {
    
};

/**
 * @return {string}
 */
Robot.prototype.getDir = function() {
    
};

/** 
 * Your Robot object will be instantiated and called as such:
 * var obj = new Robot(width, height)
 * obj.step(num)
 * var param_2 = obj.getPos()
 * var param_3 = obj.getDir()
 */
```

### TypeScript

```typescript
class Robot {
    constructor(width: number, height: number) {
        
    }

    step(num: number): void {
        
    }

    getPos(): number[] {
        
    }

    getDir(): string {
        
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * var obj = new Robot(width, height)
 * obj.step(num)
 * var param_2 = obj.getPos()
 * var param_3 = obj.getDir()
 */
```

### PHP

```php
class Robot {
    /**
     * @param Integer $width
     * @param Integer $height
     */
    function __construct($width, $height) {
        
    }
  
    /**
     * @param Integer $num
     * @return NULL
     */
    function step($num) {
        
    }
  
    /**
     * @return Integer[]
     */
    function getPos() {
        
    }
  
    /**
     * @return String
     */
    function getDir() {
        
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * $obj = Robot($width, $height);
 * $obj->step($num);
 * $ret_2 = $obj->getPos();
 * $ret_3 = $obj->getDir();
 */
```

### Swift

```swift

class Robot {

    init(_ width: Int, _ height: Int) {
        
    }
    
    func step(_ num: Int) {
        
    }
    
    func getPos() -> [Int] {
        
    }
    
    func getDir() -> String {
        
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * let obj = Robot(width, height)
 * obj.step(num)
 * let ret_2: [Int] = obj.getPos()
 * let ret_3: String = obj.getDir()
 */
```

### Kotlin

```kotlin
class Robot(width: Int, height: Int) {

    fun step(num: Int) {
        
    }

    fun getPos(): IntArray {
        
    }

    fun getDir(): String {
        
    }

}

/**
 * Your Robot object will be instantiated and called as such:
 * var obj = Robot(width, height)
 * obj.step(num)
 * var param_2 = obj.getPos()
 * var param_3 = obj.getDir()
 */
```

### Dart

```dart
class Robot {

  Robot(int width, int height) {
    
  }
  
  void step(int num) {
    
  }
  
  List<int> getPos() {
    
  }
  
  String getDir() {
    
  }
}

/**
 * Your Robot object will be instantiated and called as such:
 * Robot obj = Robot(width, height);
 * obj.step(num);
 * List<int> param2 = obj.getPos();
 * String param3 = obj.getDir();
 */
```

### Go

```golang
type Robot struct {
    
}


func Constructor(width int, height int) Robot {
    
}


func (this *Robot) Step(num int)  {
    
}


func (this *Robot) GetPos() []int {
    
}


func (this *Robot) GetDir() string {
    
}


/**
 * Your Robot object will be instantiated and called as such:
 * obj := Constructor(width, height);
 * obj.Step(num);
 * param_2 := obj.GetPos();
 * param_3 := obj.GetDir();
 */
```

### Ruby

```ruby
class Robot

=begin
    :type width: Integer
    :type height: Integer
=end
    def initialize(width, height)
        
    end


=begin
    :type num: Integer
    :rtype: Void
=end
    def step(num)
        
    end


=begin
    :rtype: Integer[]
=end
    def get_pos()
        
    end


=begin
    :rtype: String
=end
    def get_dir()
        
    end


end

# Your Robot object will be instantiated and called as such:
# obj = Robot.new(width, height)
# obj.step(num)
# param_2 = obj.get_pos()
# param_3 = obj.get_dir()
```

### Scala

```scala
class Robot(_width: Int, _height: Int) {

    def step(num: Int): Unit = {
        
    }

    def getPos(): Array[Int] = {
        
    }

    def getDir(): String = {
        
    }

}

/**
 * Your Robot object will be instantiated and called as such:
 * val obj = new Robot(width, height)
 * obj.step(num)
 * val param_2 = obj.getPos()
 * val param_3 = obj.getDir()
 */
```

### Rust

```rust
struct Robot {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Robot {

    fn new(width: i32, height: i32) -> Self {
        
    }
    
    fn step(&self, num: i32) {
        
    }
    
    fn get_pos(&self) -> Vec<i32> {
        
    }
    
    fn get_dir(&self) -> String {
        
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * let obj = Robot::new(width, height);
 * obj.step(num);
 * let ret_2: Vec<i32> = obj.get_pos();
 * let ret_3: String = obj.get_dir();
 */
```

### Racket

```racket
(define robot%
  (class object%
    (super-new)
    
    ; width : exact-integer?
    ; height : exact-integer?
    (init-field
      width
      height)
    
    ; step : exact-integer? -> void?
    (define/public (step num)
      )
    ; get-pos : -> (listof exact-integer?)
    (define/public (get-pos)
      )
    ; get-dir : -> string?
    (define/public (get-dir)
      )))

;; Your robot% object will be instantiated and called as such:
;; (define obj (new robot% [width width] [height height]))
;; (send obj step num)
;; (define param_2 (send obj get-pos))
;; (define param_3 (send obj get-dir))
```

### Erlang

```erlang
-spec robot_init_(Width :: integer(), Height :: integer()) -> any().
robot_init_(Width, Height) ->
  .

-spec robot_step(Num :: integer()) -> any().
robot_step(Num) ->
  .

-spec robot_get_pos() -> [integer()].
robot_get_pos() ->
  .

-spec robot_get_dir() -> unicode:unicode_binary().
robot_get_dir() ->
  .


%% Your functions will be called as such:
%% robot_init_(Width, Height),
%% robot_step(Num),
%% Param_2 = robot_get_pos(),
%% Param_3 = robot_get_dir(),

%% robot_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Robot do
  @spec init_(width :: integer, height :: integer) :: any
  def init_(width, height) do
    
  end

  @spec step(num :: integer) :: any
  def step(num) do
    
  end

  @spec get_pos() :: [integer]
  def get_pos() do
    
  end

  @spec get_dir() :: String.t
  def get_dir() do
    
  end
end

# Your functions will be called as such:
# Robot.init_(width, height)
# Robot.step(num)
# param_2 = Robot.get_pos()
# param_3 = Robot.get_dir()

# Robot.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Robot {
    init(width: Int64, height: Int64) {

    }
    
    func step(num: Int64): Unit {

    }
    
    func getPos(): Array<Int64> {

    }
    
    func getDir(): String {

    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * let obj: Robot = Robot(width, height)
 * obj.step(num)
 * let param_2 = obj.getPos()
 * let param_3 = obj.getDir()
 */
```

