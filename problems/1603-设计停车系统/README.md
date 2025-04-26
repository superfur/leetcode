# 1603. 设计停车系统

## 题目描述

<p>请你给一个停车场设计一个停车系统。停车场总共有三种不同大小的车位：大，中和小，每种尺寸分别有固定数目的车位。</p>

<p>请你实现 <code>ParkingSystem</code> 类：</p>

<ul>
	<li><code>ParkingSystem(int big, int medium, int small)</code> 初始化 <code>ParkingSystem</code> 类，三个参数分别对应每种停车位的数目。</li>
	<li><code>bool addCar(int carType)</code> 检查是否有 <code>carType</code> 对应的停车位。 <code>carType</code> 有三种类型：大，中，小，分别用数字 <code>1</code>， <code>2</code> 和 <code>3</code> 表示。<strong>一辆车只能停在</strong> <strong> </strong><code>carType</code> 对应尺寸的停车位中。如果没有空车位，请返回 <code>false</code> ，否则将该车停入车位并返回 <code>true</code> 。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
<strong>输出：</strong>
[null, true, true, false, false]

<strong>解释：</strong>
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // 返回 true ，因为有 1 个空的大车位
parkingSystem.addCar(2); // 返回 true ，因为有 1 个空的中车位
parkingSystem.addCar(3); // 返回 false ，因为没有空的小车位
parkingSystem.addCar(1); // 返回 false ，因为没有空的大车位，唯一一个大车位已经被占据了
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= big, medium, small <= 1000</code></li>
	<li><code>carType</code> 取值为 <code>1</code>， <code>2</code> 或 <code>3</code></li>
	<li>最多会调用 <code>addCar</code> 函数 <code>1000</code> 次</li>
</ul>


## 难度

Easy

## 标签

- 设计
- 计数
- 模拟

## 提示

1. Record number of parking slots still available for each car type.

## 示例

```
["ParkingSystem","addCar","addCar","addCar","addCar"]
[[1,1,0],[1],[2],[3],[1]]
```

## 示例代码

### C++

```cpp
class ParkingSystem {
public:
    ParkingSystem(int big, int medium, int small) {
        
    }
    
    bool addCar(int carType) {
        
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
```

### Java

```java
class ParkingSystem {

    public ParkingSystem(int big, int medium, int small) {
        
    }
    
    public boolean addCar(int carType) {
        
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */
```

### Python

```python
class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
```

### Python3

```python3
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        

    def addCar(self, carType: int) -> bool:
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
```

### C

```c



typedef struct {
    
} ParkingSystem;


ParkingSystem* parkingSystemCreate(int big, int medium, int small) {
    
}

bool parkingSystemAddCar(ParkingSystem* obj, int carType) {
    
}

void parkingSystemFree(ParkingSystem* obj) {
    
}

/**
 * Your ParkingSystem struct will be instantiated and called as such:
 * ParkingSystem* obj = parkingSystemCreate(big, medium, small);
 * bool param_1 = parkingSystemAddCar(obj, carType);
 
 * parkingSystemFree(obj);
*/
```

### C#

```csharp
public class ParkingSystem {

    public ParkingSystem(int big, int medium, int small) {
        
    }
    
    public bool AddCar(int carType) {
        
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj.AddCar(carType);
 */
```

### JavaScript

```javascript
/**
 * @param {number} big
 * @param {number} medium
 * @param {number} small
 */
var ParkingSystem = function(big, medium, small) {
    
};

/** 
 * @param {number} carType
 * @return {boolean}
 */
ParkingSystem.prototype.addCar = function(carType) {
    
};

/** 
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */
```

### TypeScript

```typescript
class ParkingSystem {
    constructor(big: number, medium: number, small: number) {
        
    }

    addCar(carType: number): boolean {
        
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */
```

### PHP

```php
class ParkingSystem {
    /**
     * @param Integer $big
     * @param Integer $medium
     * @param Integer $small
     */
    function __construct($big, $medium, $small) {
        
    }
  
    /**
     * @param Integer $carType
     * @return Boolean
     */
    function addCar($carType) {
        
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * $obj = ParkingSystem($big, $medium, $small);
 * $ret_1 = $obj->addCar($carType);
 */
```

### Swift

```swift

class ParkingSystem {

    init(_ big: Int, _ medium: Int, _ small: Int) {
        
    }
    
    func addCar(_ carType: Int) -> Bool {
        
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * let obj = ParkingSystem(big, medium, small)
 * let ret_1: Bool = obj.addCar(carType)
 */
```

### Kotlin

```kotlin
class ParkingSystem(big: Int, medium: Int, small: Int) {

    fun addCar(carType: Int): Boolean {
        
    }

}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */
```

### Dart

```dart
class ParkingSystem {

  ParkingSystem(int big, int medium, int small) {
    
  }
  
  bool addCar(int carType) {
    
  }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = ParkingSystem(big, medium, small);
 * bool param1 = obj.addCar(carType);
 */
```

### Go

```golang
type ParkingSystem struct {
    
}


func Constructor(big int, medium int, small int) ParkingSystem {
    
}


func (this *ParkingSystem) AddCar(carType int) bool {
    
}


/**
 * Your ParkingSystem object will be instantiated and called as such:
 * obj := Constructor(big, medium, small);
 * param_1 := obj.AddCar(carType);
 */
```

### Ruby

```ruby
class ParkingSystem

=begin
    :type big: Integer
    :type medium: Integer
    :type small: Integer
=end
    def initialize(big, medium, small)
        
    end


=begin
    :type car_type: Integer
    :rtype: Boolean
=end
    def add_car(car_type)
        
    end


end

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem.new(big, medium, small)
# param_1 = obj.add_car(car_type)
```

### Scala

```scala
class ParkingSystem(_big: Int, _medium: Int, _small: Int) {

    def addCar(carType: Int): Boolean = {
        
    }

}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * val obj = new ParkingSystem(big, medium, small)
 * val param_1 = obj.addCar(carType)
 */
```

### Rust

```rust
struct ParkingSystem {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ParkingSystem {

    fn new(big: i32, medium: i32, small: i32) -> Self {
        
    }
    
    fn add_car(&self, car_type: i32) -> bool {
        
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * let obj = ParkingSystem::new(big, medium, small);
 * let ret_1: bool = obj.add_car(carType);
 */
```

### Racket

```racket
(define parking-system%
  (class object%
    (super-new)
    
    ; big : exact-integer?
    ; medium : exact-integer?
    ; small : exact-integer?
    (init-field
      big
      medium
      small)
    
    ; add-car : exact-integer? -> boolean?
    (define/public (add-car car-type)
      )))

;; Your parking-system% object will be instantiated and called as such:
;; (define obj (new parking-system% [big big] [medium medium] [small small]))
;; (define param_1 (send obj add-car car-type))
```

### Erlang

```erlang
-spec parking_system_init_(Big :: integer(), Medium :: integer(), Small :: integer()) -> any().
parking_system_init_(Big, Medium, Small) ->
  .

-spec parking_system_add_car(CarType :: integer()) -> boolean().
parking_system_add_car(CarType) ->
  .


%% Your functions will be called as such:
%% parking_system_init_(Big, Medium, Small),
%% Param_1 = parking_system_add_car(CarType),

%% parking_system_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule ParkingSystem do
  @spec init_(big :: integer, medium :: integer, small :: integer) :: any
  def init_(big, medium, small) do
    
  end

  @spec add_car(car_type :: integer) :: boolean
  def add_car(car_type) do
    
  end
end

# Your functions will be called as such:
# ParkingSystem.init_(big, medium, small)
# param_1 = ParkingSystem.add_car(car_type)

# ParkingSystem.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class ParkingSystem {
    init(big: Int64, medium: Int64, small: Int64) {

    }
    
    func addCar(carType: Int64): Bool {

    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * let obj: ParkingSystem = ParkingSystem(big, medium, small)
 * let param_1 = obj.addCar(carType)
 */
```

