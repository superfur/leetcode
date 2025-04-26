# 2424. 最长上传前缀

## 题目描述

<p>给你一个&nbsp;<code>n</code>&nbsp;个视频的上传序列，每个视频编号为&nbsp;<code>1</code>&nbsp;到&nbsp;<code>n</code>&nbsp;之间的 <strong>不同</strong>&nbsp;数字，你需要依次将这些视频上传到服务器。请你实现一个数据结构，在上传的过程中计算 <strong>最长上传前缀</strong>&nbsp;。</p>

<p>如果&nbsp;<strong>闭区间</strong>&nbsp;<code>1</code>&nbsp;到&nbsp;<code>i</code>&nbsp;之间的视频全部都已经被上传到服务器，那么我们称 <code>i</code>&nbsp;是上传前缀。最长上传前缀指的是符合定义的 <code>i</code>&nbsp;中的 <strong>最大值</strong>&nbsp;。<br>
<br>
请你实现&nbsp;<code>LUPrefix</code>&nbsp;类：</p>

<ul>
	<li><code>LUPrefix(int n)</code>&nbsp;初始化一个 <code>n</code>&nbsp;个视频的流对象。</li>
	<li><code>void upload(int video)</code>&nbsp;上传&nbsp;<code>video</code>&nbsp;到服务器。</li>
	<li><code>int longest()</code>&nbsp;返回上述定义的 <strong>最长上传前缀</strong>&nbsp;的长度。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>
["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
[[4], [3], [], [1], [], [2], []]
<strong>输出：</strong>
[null, null, 0, null, 1, null, 3]

<strong>解释：</strong>
LUPrefix server = new LUPrefix(4);   // 初始化 4个视频的上传流
server.upload(3);                    // 上传视频 3 。
server.longest();                    // 由于视频 1 还没有被上传，最长上传前缀是 0 。
server.upload(1);                    // 上传视频 1 。
server.longest();                    // 前缀 [1] 是最长上传前缀，所以我们返回 1 。
server.upload(2);                    // 上传视频 2 。
server.longest();                    // 前缀 [1,2,3] 是最长上传前缀，所以我们返回 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= video &lt;= 10<sup>5</sup></code></li>
	<li><code>video</code>&nbsp;中所有值 <strong>互不相同</strong>&nbsp;。</li>
	<li><code>upload</code> 和&nbsp;<code>longest</code>&nbsp;<strong>总调用</strong> 次数至多不超过&nbsp;<code>2 * 10<sup>5</sup></code>&nbsp;次。</li>
	<li>至少会调用&nbsp;<code>longest</code>&nbsp;一次。</li>
</ul>


## 难度

Medium

## 标签

- 并查集
- 设计
- 树状数组
- 线段树
- 二分查找
- 有序集合
- 堆（优先队列）

## 提示

1. Maintain an array keeping track of whether video “i” has been uploaded yet.

## 示例

```
["LUPrefix","upload","longest","upload","longest","upload","longest"]
[[4],[3],[],[1],[],[2],[]]
```

## 示例代码

### C++

```cpp
class LUPrefix {
public:
    LUPrefix(int n) {
        
    }
    
    void upload(int video) {
        
    }
    
    int longest() {
        
    }
};

/**
 * Your LUPrefix object will be instantiated and called as such:
 * LUPrefix* obj = new LUPrefix(n);
 * obj->upload(video);
 * int param_2 = obj->longest();
 */
```

### Java

```java
class LUPrefix {

    public LUPrefix(int n) {
        
    }
    
    public void upload(int video) {
        
    }
    
    public int longest() {
        
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * LUPrefix obj = new LUPrefix(n);
 * obj.upload(video);
 * int param_2 = obj.longest();
 */
```

### Python

```python
class LUPrefix(object):

    def __init__(self, n):
        """
        :type n: int
        """
        

    def upload(self, video):
        """
        :type video: int
        :rtype: None
        """
        

    def longest(self):
        """
        :rtype: int
        """
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
```

### Python3

```python3
class LUPrefix:

    def __init__(self, n: int):
        

    def upload(self, video: int) -> None:
        

    def longest(self) -> int:
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
```

### C

```c



typedef struct {
    
} LUPrefix;


LUPrefix* lUPrefixCreate(int n) {
    
}

void lUPrefixUpload(LUPrefix* obj, int video) {
    
}

int lUPrefixLongest(LUPrefix* obj) {
    
}

void lUPrefixFree(LUPrefix* obj) {
    
}

/**
 * Your LUPrefix struct will be instantiated and called as such:
 * LUPrefix* obj = lUPrefixCreate(n);
 * lUPrefixUpload(obj, video);
 
 * int param_2 = lUPrefixLongest(obj);
 
 * lUPrefixFree(obj);
*/
```

### C#

```csharp
public class LUPrefix {

    public LUPrefix(int n) {
        
    }
    
    public void Upload(int video) {
        
    }
    
    public int Longest() {
        
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * LUPrefix obj = new LUPrefix(n);
 * obj.Upload(video);
 * int param_2 = obj.Longest();
 */
```

### JavaScript

```javascript
/**
 * @param {number} n
 */
var LUPrefix = function(n) {
    
};

/** 
 * @param {number} video
 * @return {void}
 */
LUPrefix.prototype.upload = function(video) {
    
};

/**
 * @return {number}
 */
LUPrefix.prototype.longest = function() {
    
};

/** 
 * Your LUPrefix object will be instantiated and called as such:
 * var obj = new LUPrefix(n)
 * obj.upload(video)
 * var param_2 = obj.longest()
 */
```

### TypeScript

```typescript
class LUPrefix {
    constructor(n: number) {
        
    }

    upload(video: number): void {
        
    }

    longest(): number {
        
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * var obj = new LUPrefix(n)
 * obj.upload(video)
 * var param_2 = obj.longest()
 */
```

### PHP

```php
class LUPrefix {
    /**
     * @param Integer $n
     */
    function __construct($n) {
        
    }
  
    /**
     * @param Integer $video
     * @return NULL
     */
    function upload($video) {
        
    }
  
    /**
     * @return Integer
     */
    function longest() {
        
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * $obj = LUPrefix($n);
 * $obj->upload($video);
 * $ret_2 = $obj->longest();
 */
```

### Swift

```swift

class LUPrefix {

    init(_ n: Int) {
        
    }
    
    func upload(_ video: Int) {
        
    }
    
    func longest() -> Int {
        
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * let obj = LUPrefix(n)
 * obj.upload(video)
 * let ret_2: Int = obj.longest()
 */
```

### Kotlin

```kotlin
class LUPrefix(n: Int) {

    fun upload(video: Int) {
        
    }

    fun longest(): Int {
        
    }

}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * var obj = LUPrefix(n)
 * obj.upload(video)
 * var param_2 = obj.longest()
 */
```

### Dart

```dart
class LUPrefix {

  LUPrefix(int n) {
    
  }
  
  void upload(int video) {
    
  }
  
  int longest() {
    
  }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * LUPrefix obj = LUPrefix(n);
 * obj.upload(video);
 * int param2 = obj.longest();
 */
```

### Go

```golang
type LUPrefix struct {
    
}


func Constructor(n int) LUPrefix {
    
}


func (this *LUPrefix) Upload(video int)  {
    
}


func (this *LUPrefix) Longest() int {
    
}


/**
 * Your LUPrefix object will be instantiated and called as such:
 * obj := Constructor(n);
 * obj.Upload(video);
 * param_2 := obj.Longest();
 */
```

### Ruby

```ruby
class LUPrefix

=begin
    :type n: Integer
=end
    def initialize(n)
        
    end


=begin
    :type video: Integer
    :rtype: Void
=end
    def upload(video)
        
    end


=begin
    :rtype: Integer
=end
    def longest()
        
    end


end

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix.new(n)
# obj.upload(video)
# param_2 = obj.longest()
```

### Scala

```scala
class LUPrefix(_n: Int) {

    def upload(video: Int): Unit = {
        
    }

    def longest(): Int = {
        
    }

}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * val obj = new LUPrefix(n)
 * obj.upload(video)
 * val param_2 = obj.longest()
 */
```

### Rust

```rust
struct LUPrefix {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LUPrefix {

    fn new(n: i32) -> Self {
        
    }
    
    fn upload(&self, video: i32) {
        
    }
    
    fn longest(&self) -> i32 {
        
    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * let obj = LUPrefix::new(n);
 * obj.upload(video);
 * let ret_2: i32 = obj.longest();
 */
```

### Racket

```racket
(define lu-prefix%
  (class object%
    (super-new)
    
    ; n : exact-integer?
    (init-field
      n)
    
    ; upload : exact-integer? -> void?
    (define/public (upload video)
      )
    ; longest : -> exact-integer?
    (define/public (longest)
      )))

;; Your lu-prefix% object will be instantiated and called as such:
;; (define obj (new lu-prefix% [n n]))
;; (send obj upload video)
;; (define param_2 (send obj longest))
```

### Erlang

```erlang
-spec lu_prefix_init_(N :: integer()) -> any().
lu_prefix_init_(N) ->
  .

-spec lu_prefix_upload(Video :: integer()) -> any().
lu_prefix_upload(Video) ->
  .

-spec lu_prefix_longest() -> integer().
lu_prefix_longest() ->
  .


%% Your functions will be called as such:
%% lu_prefix_init_(N),
%% lu_prefix_upload(Video),
%% Param_2 = lu_prefix_longest(),

%% lu_prefix_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule LUPrefix do
  @spec init_(n :: integer) :: any
  def init_(n) do
    
  end

  @spec upload(video :: integer) :: any
  def upload(video) do
    
  end

  @spec longest() :: integer
  def longest() do
    
  end
end

# Your functions will be called as such:
# LUPrefix.init_(n)
# LUPrefix.upload(video)
# param_2 = LUPrefix.longest()

# LUPrefix.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class LUPrefix {
    init(n: Int64) {

    }
    
    func upload(video: Int64): Unit {

    }
    
    func longest(): Int64 {

    }
}

/**
 * Your LUPrefix object will be instantiated and called as such:
 * let obj: LUPrefix = LUPrefix(n)
 * obj.upload(video)
 * let param_2 = obj.longest()
 */
```

