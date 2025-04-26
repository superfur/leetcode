# 面试题 03.06. 动物收容所

## 题目描述

<p>动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出”的原则。在收养该收容所的动物时，收养人只能收养所有动物中“最老”（由其进入收容所的时间长短而定）的动物，或者可以挑选猫或狗（同时必须收养此类动物中“最老”的）。换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如<code>enqueue</code>、<code>dequeueAny</code>、<code>dequeueDog</code>和<code>dequeueCat</code>。允许使用Java内置的LinkedList数据结构。</p>

<p><code>enqueue</code>方法有一个<code>animal</code>参数，<code>animal[0]</code>代表动物编号，<code>animal[1]</code>代表动物种类，其中 0 代表猫，1 代表狗。</p>

<p><code>dequeue*</code>方法返回一个列表<code>[动物编号, 动物种类]</code>，若没有可以收养的动物，则返回<code>[-1,-1]</code>。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：
["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
[[], [[0, 0]], [[1, 0]], [], [], []]
<strong> 输出</strong>：
[null,null,null,[0,0],[-1,-1],[1,0]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：
["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"]
[[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
<strong> 输出</strong>：
[null,null,null,null,[2,1],[0,0],[1,0]]
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>收纳所的最大容量为20000</li>
</ol>


## 难度

Easy

## 标签

- 设计
- 队列

## 提示

1. 让我们假设用不同的列表存储猫和狗。怎样才能找到所有物种中最老的动物呢？要有创意。
2. 可以考虑为狗和猫保留一个链表，然后遍历它找到第一只狗（或猫）。这样做的影响是什么？
3. 想想现实生活中你是怎么做的。你有一个按时间排序的狗列表和一个按时间排序的猫列表。你需要什么数据才能找到最老的动物？你将如何维护这些数据？

## 示例

```
["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
[[], [[0, 0]], [[1, 0]], [], [], []]
["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"]
[[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
```

## 示例代码

### C++

```cpp
class AnimalShelf {
public:
    AnimalShelf() {
        
    }
    
    void enqueue(vector<int> animal) {
        
    }
    
    vector<int> dequeueAny() {
        
    }
    
    vector<int> dequeueDog() {
        
    }
    
    vector<int> dequeueCat() {
        
    }
};

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * AnimalShelf* obj = new AnimalShelf();
 * obj->enqueue(animal);
 * vector<int> param_2 = obj->dequeueAny();
 * vector<int> param_3 = obj->dequeueDog();
 * vector<int> param_4 = obj->dequeueCat();
 */
```

### Java

```java
class AnimalShelf {

    public AnimalShelf() {
        
    }
    
    public void enqueue(int[] animal) {
        
    }
    
    public int[] dequeueAny() {
        
    }
    
    public int[] dequeueDog() {
        
    }
    
    public int[] dequeueCat() {
        
    }
}

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * AnimalShelf obj = new AnimalShelf();
 * obj.enqueue(animal);
 * int[] param_2 = obj.dequeueAny();
 * int[] param_3 = obj.dequeueDog();
 * int[] param_4 = obj.dequeueCat();
 */
```

### Python

```python
class AnimalShelf(object):

    def __init__(self):
        

    def enqueue(self, animal):
        """
        :type animal: List[int]
        :rtype: None
        """
        

    def dequeueAny(self):
        """
        :rtype: List[int]
        """
        

    def dequeueDog(self):
        """
        :rtype: List[int]
        """
        

    def dequeueCat(self):
        """
        :rtype: List[int]
        """
        


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
```

### Python3

```python3
class AnimalShelf:

    def __init__(self):
        

    def enqueue(self, animal: List[int]) -> None:
        

    def dequeueAny(self) -> List[int]:
        

    def dequeueDog(self) -> List[int]:
        

    def dequeueCat(self) -> List[int]:
        


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()
```

### C

```c



typedef struct {
    
} AnimalShelf;


AnimalShelf* animalShelfCreate() {
    
}

void animalShelfEnqueue(AnimalShelf* obj, int* animal, int animalSize) {
    
}

int* animalShelfDequeueAny(AnimalShelf* obj, int* retSize) {
    
}

int* animalShelfDequeueDog(AnimalShelf* obj, int* retSize) {
    
}

int* animalShelfDequeueCat(AnimalShelf* obj, int* retSize) {
    
}

void animalShelfFree(AnimalShelf* obj) {
    
}

/**
 * Your AnimalShelf struct will be instantiated and called as such:
 * AnimalShelf* obj = animalShelfCreate();
 * animalShelfEnqueue(obj, animal, animalSize);
 
 * int* param_2 = animalShelfDequeueAny(obj, retSize);
 
 * int* param_3 = animalShelfDequeueDog(obj, retSize);
 
 * int* param_4 = animalShelfDequeueCat(obj, retSize);
 
 * animalShelfFree(obj);
*/
```

### C#

```csharp
public class AnimalShelf {

    public AnimalShelf() {
        
    }
    
    public void Enqueue(int[] animal) {
        
    }
    
    public int[] DequeueAny() {
        
    }
    
    public int[] DequeueDog() {
        
    }
    
    public int[] DequeueCat() {
        
    }
}

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * AnimalShelf obj = new AnimalShelf();
 * obj.Enqueue(animal);
 * int[] param_2 = obj.DequeueAny();
 * int[] param_3 = obj.DequeueDog();
 * int[] param_4 = obj.DequeueCat();
 */
```

### JavaScript

```javascript

var AnimalShelf = function() {
    
};

/** 
 * @param {number[]} animal
 * @return {void}
 */
AnimalShelf.prototype.enqueue = function(animal) {
    
};

/**
 * @return {number[]}
 */
AnimalShelf.prototype.dequeueAny = function() {
    
};

/**
 * @return {number[]}
 */
AnimalShelf.prototype.dequeueDog = function() {
    
};

/**
 * @return {number[]}
 */
AnimalShelf.prototype.dequeueCat = function() {
    
};

/** 
 * Your AnimalShelf object will be instantiated and called as such:
 * var obj = new AnimalShelf()
 * obj.enqueue(animal)
 * var param_2 = obj.dequeueAny()
 * var param_3 = obj.dequeueDog()
 * var param_4 = obj.dequeueCat()
 */
```

### TypeScript

```typescript
class AnimalShelf {
    constructor() {
        
    }

    enqueue(animal: number[]): void {
        
    }

    dequeueAny(): number[] {
        
    }

    dequeueDog(): number[] {
        
    }

    dequeueCat(): number[] {
        
    }
}

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * var obj = new AnimalShelf()
 * obj.enqueue(animal)
 * var param_2 = obj.dequeueAny()
 * var param_3 = obj.dequeueDog()
 * var param_4 = obj.dequeueCat()
 */
```

### PHP

```php
class AnimalShelf {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer[] $animal
     * @return NULL
     */
    function enqueue($animal) {
        
    }
  
    /**
     * @return Integer[]
     */
    function dequeueAny() {
        
    }
  
    /**
     * @return Integer[]
     */
    function dequeueDog() {
        
    }
  
    /**
     * @return Integer[]
     */
    function dequeueCat() {
        
    }
}

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * $obj = AnimalShelf();
 * $obj->enqueue($animal);
 * $ret_2 = $obj->dequeueAny();
 * $ret_3 = $obj->dequeueDog();
 * $ret_4 = $obj->dequeueCat();
 */
```

### Swift

```swift

class AnimalShelf {

    init() {
        
    }
    
    func enqueue(_ animal: [Int]) {
        
    }
    
    func dequeueAny() -> [Int] {
        
    }
    
    func dequeueDog() -> [Int] {
        
    }
    
    func dequeueCat() -> [Int] {
        
    }
}

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * let obj = AnimalShelf()
 * obj.enqueue(animal)
 * let ret_2: [Int] = obj.dequeueAny()
 * let ret_3: [Int] = obj.dequeueDog()
 * let ret_4: [Int] = obj.dequeueCat()
 */
```

### Kotlin

```kotlin
class AnimalShelf() {

    fun enqueue(animal: IntArray) {
        
    }

    fun dequeueAny(): IntArray {
        
    }

    fun dequeueDog(): IntArray {
        
    }

    fun dequeueCat(): IntArray {
        
    }

}

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * var obj = AnimalShelf()
 * obj.enqueue(animal)
 * var param_2 = obj.dequeueAny()
 * var param_3 = obj.dequeueDog()
 * var param_4 = obj.dequeueCat()
 */
```

### Dart

```dart
class AnimalShelf {

  AnimalShelf() {
    
  }
  
  void enqueue(List<int> animal) {
    
  }
  
  List<int> dequeueAny() {
    
  }
  
  List<int> dequeueDog() {
    
  }
  
  List<int> dequeueCat() {
    
  }
}

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * AnimalShelf obj = AnimalShelf();
 * obj.enqueue(animal);
 * List<int> param2 = obj.dequeueAny();
 * List<int> param3 = obj.dequeueDog();
 * List<int> param4 = obj.dequeueCat();
 */
```

### Go

```golang
type AnimalShelf struct {
    
}


func Constructor() AnimalShelf {
    
}


func (this *AnimalShelf) Enqueue(animal []int)  {
    
}


func (this *AnimalShelf) DequeueAny() []int {
    
}


func (this *AnimalShelf) DequeueDog() []int {
    
}


func (this *AnimalShelf) DequeueCat() []int {
    
}


/**
 * Your AnimalShelf object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Enqueue(animal);
 * param_2 := obj.DequeueAny();
 * param_3 := obj.DequeueDog();
 * param_4 := obj.DequeueCat();
 */
```

### Ruby

```ruby
class AnimalShelf
    def initialize()
        
    end


=begin
    :type animal: Integer[]
    :rtype: Void
=end
    def enqueue(animal)
        
    end


=begin
    :rtype: Integer[]
=end
    def dequeue_any()
        
    end


=begin
    :rtype: Integer[]
=end
    def dequeue_dog()
        
    end


=begin
    :rtype: Integer[]
=end
    def dequeue_cat()
        
    end


end

# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf.new()
# obj.enqueue(animal)
# param_2 = obj.dequeue_any()
# param_3 = obj.dequeue_dog()
# param_4 = obj.dequeue_cat()
```

### Scala

```scala
class AnimalShelf() {

    def enqueue(animal: Array[Int]): Unit = {
        
    }

    def dequeueAny(): Array[Int] = {
        
    }

    def dequeueDog(): Array[Int] = {
        
    }

    def dequeueCat(): Array[Int] = {
        
    }

}

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * val obj = new AnimalShelf()
 * obj.enqueue(animal)
 * val param_2 = obj.dequeueAny()
 * val param_3 = obj.dequeueDog()
 * val param_4 = obj.dequeueCat()
 */
```

### Rust

```rust
struct AnimalShelf {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl AnimalShelf {

    fn new() -> Self {
        
    }
    
    fn enqueue(&self, animal: Vec<i32>) {
        
    }
    
    fn dequeue_any(&self) -> Vec<i32> {
        
    }
    
    fn dequeue_dog(&self) -> Vec<i32> {
        
    }
    
    fn dequeue_cat(&self) -> Vec<i32> {
        
    }
}

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * let obj = AnimalShelf::new();
 * obj.enqueue(animal);
 * let ret_2: Vec<i32> = obj.dequeue_any();
 * let ret_3: Vec<i32> = obj.dequeue_dog();
 * let ret_4: Vec<i32> = obj.dequeue_cat();
 */
```

### Racket

```racket
(define animal-shelf%
  (class object%
    (super-new)
    
    (init-field)
    
    ; enqueue : (listof exact-integer?) -> void?
    (define/public (enqueue animal)
      )
    ; dequeue-any : -> (listof exact-integer?)
    (define/public (dequeue-any)
      )
    ; dequeue-dog : -> (listof exact-integer?)
    (define/public (dequeue-dog)
      )
    ; dequeue-cat : -> (listof exact-integer?)
    (define/public (dequeue-cat)
      )))

;; Your animal-shelf% object will be instantiated and called as such:
;; (define obj (new animal-shelf%))
;; (send obj enqueue animal)
;; (define param_2 (send obj dequeue-any))
;; (define param_3 (send obj dequeue-dog))
;; (define param_4 (send obj dequeue-cat))
```

### Erlang

```erlang
-spec animal_shelf_init_() -> any().
animal_shelf_init_() ->
  .

-spec animal_shelf_enqueue(Animal :: [integer()]) -> any().
animal_shelf_enqueue(Animal) ->
  .

-spec animal_shelf_dequeue_any() -> [integer()].
animal_shelf_dequeue_any() ->
  .

-spec animal_shelf_dequeue_dog() -> [integer()].
animal_shelf_dequeue_dog() ->
  .

-spec animal_shelf_dequeue_cat() -> [integer()].
animal_shelf_dequeue_cat() ->
  .


%% Your functions will be called as such:
%% animal_shelf_init_(),
%% animal_shelf_enqueue(Animal),
%% Param_2 = animal_shelf_dequeue_any(),
%% Param_3 = animal_shelf_dequeue_dog(),
%% Param_4 = animal_shelf_dequeue_cat(),

%% animal_shelf_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule AnimalShelf do
  @spec init_() :: any
  def init_() do
    
  end

  @spec enqueue(animal :: [integer]) :: any
  def enqueue(animal) do
    
  end

  @spec dequeue_any() :: [integer]
  def dequeue_any() do
    
  end

  @spec dequeue_dog() :: [integer]
  def dequeue_dog() do
    
  end

  @spec dequeue_cat() :: [integer]
  def dequeue_cat() do
    
  end
end

# Your functions will be called as such:
# AnimalShelf.init_()
# AnimalShelf.enqueue(animal)
# param_2 = AnimalShelf.dequeue_any()
# param_3 = AnimalShelf.dequeue_dog()
# param_4 = AnimalShelf.dequeue_cat()

# AnimalShelf.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class AnimalShelf {
    init() {

    }
    
    func enqueue(animal: Array<Int64>): Unit {

    }
    
    func dequeueAny(): Array<Int64> {

    }
    
    func dequeueDog(): Array<Int64> {

    }
    
    func dequeueCat(): Array<Int64> {

    }
}

/**
 * Your AnimalShelf object will be instantiated and called as such:
 * let obj: AnimalShelf = AnimalShelf()
 * obj.enqueue(animal)
 * let param_2 = obj.dequeueAny()
 * let param_3 = obj.dequeueDog()
 * let param_4 = obj.dequeueCat()
 */
```

