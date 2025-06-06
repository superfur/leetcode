# LCP 27. 黑盒光线反射

## 题目描述

秋日市集上有个奇怪的黑盒，黑盒的主视图为 n\*m 的矩形。从黑盒的主视图来看，黑盒的上面和下面各均匀分布有 m 个小孔，黑盒的左面和右面各均匀分布有 n 个小孔。黑盒左上角小孔序号为 0，按顺时针编号，总共有 2*(m+n) 个小孔。每个小孔均可以打开或者关闭，初始时，所有小孔均处于关闭状态。每个小孔上的盖子均为镜面材质。例如一个 2\*3 的黑盒主视图与其小孔分布如图所示:

![image.png](https://pic.leetcode-cn.com/1598951281-ZCBrif-image.png){:height="200px"}

店长告诉小扣，这里是「几何学的快问快答」，店长可能有两种操作：

- `open(int index, int direction)` - 若小孔处于关闭状态，则打开小孔，照入光线；否则直接照入光线；
- `close(int index)` - 关闭处于打开状态小孔，店长保证不会关闭已处于关闭状态的小孔；

其中：
- `index`： 表示小孔序号
- `direction`：`1` 表示光线沿 $y=x$ 方向，`-1` 表示光线沿 $y=-x$ 方向。

![image.png](https://pic.leetcode-cn.com/1599620810-HdOlMi-image.png){:height="200px"}


当光线照至边界时：若边界上的小孔为开启状态，则光线会射出；否则，光线会在小孔之间进行反射。特别地：
1. 若光线射向未打开的拐角（黑盒顶点），则光线会原路反射回去；
2. 光线自拐角处的小孔照入时，只有一种入射方向（如自序号为 0 的小孔照入方向只能为 `-1`）

![image.png](https://pic.leetcode-cn.com/1598953840-DLiAsf-image.png){:height="200px"}

请帮助小扣判断并返回店长每次照入的光线从几号小孔射出。


**示例 1：**
>输入：
>`["BlackBox","open","open","open","close","open"]`
>`[[2,3],[6,-1],[4,-1],[0,-1],[6],[0,-1]]`
>
>输出：`[null,6,4,6,null,4]`
>
>解释：
>BlackBox b = BlackBox(2,3); // 新建一个 2x3 的黑盒
>b.open(6,-1) // 打开 6 号小孔，并沿 y=-x 方向照入光线，光线至 0 号小孔反射，从 6 号小孔射出
>b.open(4,-1) // 打开 4 号小孔，并沿 y=-x 方向照入光线，光线轨迹为 4-2-8-2-4，从 4 号小孔射出
>b.open(0,-1) // 打开 0 号小孔，并沿 y=-x 方向照入光线，由于 6 号小孔为开启状态，光线从 6 号小孔射出
>b.close(6) // 关闭 6 号小孔
>b.shoot(0,-1) // 从 0 号小孔沿 y=-x 方向照入光线，由于 6 号小孔为关闭状态，4 号小孔为开启状态，光线轨迹为 0-6-4，从 4 号小孔射出

**示例 2：**
>输入：
>`["BlackBox","open","open","open","open","close","open","close","open"]`
>`[[3,3],[1,-1],[5,1],[11,-1],[11,1],[1],[11,1],[5],[11,-1]]`
>
>输出：`[null,1,1,5,1,null,5,null,11]`
>
>解释：
>
>![image.png](https://pic.leetcode-cn.com/1599204202-yGDMVk-image.png){:height="300px"}
>
>BlackBox b = BlackBox(3,3); // 新建一个 3x3 的黑盒
>b.open(1,-1) // 打开 1 号小孔，并沿 y=-x 方向照入光线，光线轨迹为 1-5-7-11-1，从 1 号小孔射出
>b.open(5,1) // 打开 5 号小孔，并沿 y=x 方向照入光线，光线轨迹为 5-7-11-1，从 1 号小孔射出
>b.open(11,-1) // 打开 11 号小孔，并沿逆 y=-x 方向照入光线，光线轨迹为 11-7-5，从 5 号小孔射出
>b.open(11,1) // 从 11 号小孔沿 y=x 方向照入光线，光线轨迹为 11-1，从 1 号小孔射出
>b.close(1) // 关闭 1 号小孔
>b.open(11,1) // 从 11 号小孔沿 y=x 方向照入光线，光线轨迹为 11-1-5，从 5 号小孔射出
>b.close(5) // 关闭 5 号小孔
>b.open(11,-1) // 从 11 号小孔沿 y=-x 方向照入光线，光线轨迹为 11-1-5-7-11，从 11 号小孔射出



**提示：**
- `1 <= n, m <= 10000`
- `1 <= 操作次数 <= 10000`
- `direction` 仅为 `1` 或 `-1`
- `0 <= index < 2*(m+n)`


## 难度

Hard

## 标签

- 设计
- 线段树
- 数学
- 有序集合

## 示例

```
["BlackBox","open","open","open","close","open"]
[[2,3],[6,-1],[4,-1],[0,-1],[6],[0,-1]]
["BlackBox","open","open","open","open","close","open","close","open"]
[[3,3],[1,-1],[5,1],[11,-1],[11,1],[1],[11,1],[5],[11,-1]]
```

## 示例代码

### C++

```cpp
class BlackBox {
public:
    BlackBox(int n, int m) {

    }
    
    int open(int index, int direction) {

    }
    
    void close(int index) {

    }
};

/**
 * Your BlackBox object will be instantiated and called as such:
 * BlackBox* obj = new BlackBox(n, m);
 * int param_1 = obj->open(index,direction);
 * obj->close(index);
 */
```

### Java

```java
class BlackBox {

    public BlackBox(int n, int m) {

    }
    
    public int open(int index, int direction) {

    }
    
    public void close(int index) {

    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * BlackBox obj = new BlackBox(n, m);
 * int param_1 = obj.open(index,direction);
 * obj.close(index);
 */
```

### Python

```python
class BlackBox(object):

    def __init__(self, n, m):
        """
        :type n: int
        :type m: int
        """


    def open(self, index, direction):
        """
        :type index: int
        :type direction: int
        :rtype: int
        """


    def close(self, index):
        """
        :type index: int
        :rtype: None
        """



# Your BlackBox object will be instantiated and called as such:
# obj = BlackBox(n, m)
# param_1 = obj.open(index,direction)
# obj.close(index)
```

### Python3

```python3
class BlackBox:

    def __init__(self, n: int, m: int):


    def open(self, index: int, direction: int) -> int:


    def close(self, index: int) -> None:



# Your BlackBox object will be instantiated and called as such:
# obj = BlackBox(n, m)
# param_1 = obj.open(index,direction)
# obj.close(index)
```

### C

```c



typedef struct {

} BlackBox;


BlackBox* blackBoxCreate(int n, int m) {

}

int blackBoxOpen(BlackBox* obj, int index, int direction) {

}

void blackBoxClose(BlackBox* obj, int index) {

}

void blackBoxFree(BlackBox* obj) {

}

/**
 * Your BlackBox struct will be instantiated and called as such:
 * BlackBox* obj = blackBoxCreate(n, m);
 * int param_1 = blackBoxOpen(obj, index, direction);
 
 * blackBoxClose(obj, index);
 
 * blackBoxFree(obj);
*/
```

### C#

```csharp
public class BlackBox {

    public BlackBox(int n, int m) {

    }
    
    public int Open(int index, int direction) {

    }
    
    public void Close(int index) {

    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * BlackBox obj = new BlackBox(n, m);
 * int param_1 = obj.Open(index,direction);
 * obj.Close(index);
 */
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} m
 */
var BlackBox = function(n, m) {

};

/** 
 * @param {number} index 
 * @param {number} direction
 * @return {number}
 */
BlackBox.prototype.open = function(index, direction) {

};

/** 
 * @param {number} index
 * @return {void}
 */
BlackBox.prototype.close = function(index) {

};

/**
 * Your BlackBox object will be instantiated and called as such:
 * var obj = new BlackBox(n, m)
 * var param_1 = obj.open(index,direction)
 * obj.close(index)
 */
```

### TypeScript

```typescript
class BlackBox {
    constructor(n: number, m: number) {

    }

    open(index: number, direction: number): number {

    }

    close(index: number): void {

    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * var obj = new BlackBox(n, m)
 * var param_1 = obj.open(index,direction)
 * obj.close(index)
 */
```

### PHP

```php
class BlackBox {
    /**
     * @param Integer $n
     * @param Integer $m
     */
    function __construct($n, $m) {

    }

    /**
     * @param Integer $index
     * @param Integer $direction
     * @return Integer
     */
    function open($index, $direction) {

    }

    /**
     * @param Integer $index
     * @return NULL
     */
    function close($index) {

    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * $obj = BlackBox($n, $m);
 * $ret_1 = $obj->open($index, $direction);
 * $obj->close($index);
 */
```

### Swift

```swift

class BlackBox {

    init(_ n: Int, _ m: Int) {

    }
    
    func open(_ index: Int, _ direction: Int) -> Int {

    }
    
    func close(_ index: Int) {

    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * let obj = BlackBox(n, m)
 * let ret_1: Int = obj.open(index, direction)
 * obj.close(index)
 */
```

### Kotlin

```kotlin
class BlackBox(n: Int, m: Int) {

    fun open(index: Int, direction: Int): Int {

    }

    fun close(index: Int) {

    }

}

/**
 * Your BlackBox object will be instantiated and called as such:
 * var obj = BlackBox(n, m)
 * var param_1 = obj.open(index,direction)
 * obj.close(index)
 */
```

### Go

```golang
type BlackBox struct {

}


func Constructor(n int, m int) BlackBox {

}


func (this *BlackBox) Open(index int, direction int) int {

}


func (this *BlackBox) Close(index int)  {

}


/**
 * Your BlackBox object will be instantiated and called as such:
 * obj := Constructor(n, m);
 * param_1 := obj.Open(index,direction);
 * obj.Close(index);
 */
```

### Ruby

```ruby
class BlackBox

=begin
    :type n: Integer
    :type m: Integer
=end
    def initialize(n, m)

    end


=begin
    :type index: Integer
    :type direction: Integer
    :rtype: Integer
=end
    def open(index, direction)

    end


=begin
    :type index: Integer
    :rtype: Void
=end
    def close(index)

    end


end

# Your BlackBox object will be instantiated and called as such:
# obj = BlackBox.new(n, m)
# param_1 = obj.open(index, direction)
# obj.close(index)
```

### Scala

```scala
class BlackBox(_n: Int, _m: Int) {

    def open(index: Int, direction: Int): Int = {

    }

    def close(index: Int) {

    }

}

/**
 * Your BlackBox object will be instantiated and called as such:
 * var obj = new BlackBox(n, m)
 * var param_1 = obj.open(index,direction)
 * obj.close(index)
 */
```

### Rust

```rust
struct BlackBox {

}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl BlackBox {

    fn new(n: i32, m: i32) -> Self {

    }
    
    fn open(&self, index: i32, direction: i32) -> i32 {

    }
    
    fn close(&self, index: i32) {

    }
}

/**
 * Your BlackBox object will be instantiated and called as such:
 * let obj = BlackBox::new(n, m);
 * let ret_1: i32 = obj.open(index, direction);
 * obj.close(index);
 */
```

