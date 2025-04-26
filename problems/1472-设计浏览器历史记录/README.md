# 1472. 设计浏览器历史记录

## 题目描述

<p>你有一个只支持单个标签页的 <strong>浏览器</strong>&nbsp;，最开始你浏览的网页是&nbsp;<code>homepage</code>&nbsp;，你可以访问其他的网站&nbsp;<code>url</code>&nbsp;，也可以在浏览历史中后退&nbsp;<code>steps</code>&nbsp;步或前进&nbsp;<code>steps</code>&nbsp;步。</p>

<p>请你实现&nbsp;<code>BrowserHistory</code> 类：</p>

<ul>
	<li><code>BrowserHistory(string homepage)</code>&nbsp;，用&nbsp;<code>homepage</code>&nbsp;初始化浏览器类。</li>
	<li><code>void visit(string url)</code>&nbsp;从当前页跳转访问 <code>url</code> 对应的页面&nbsp;&nbsp;。执行此操作会把浏览历史前进的记录全部删除。</li>
	<li><code>string back(int steps)</code>&nbsp;在浏览历史中后退&nbsp;<code>steps</code>&nbsp;步。如果你只能在浏览历史中后退至多&nbsp;<code>x</code> 步且&nbsp;<code>steps &gt; x</code>&nbsp;，那么你只后退&nbsp;<code>x</code>&nbsp;步。请返回后退 <strong>至多</strong> <code>steps</code>&nbsp;步以后的&nbsp;<code>url</code>&nbsp;。</li>
	<li><code>string forward(int steps)</code>&nbsp;在浏览历史中前进&nbsp;<code>steps</code>&nbsp;步。如果你只能在浏览历史中前进至多&nbsp;<code>x</code>&nbsp;步且&nbsp;<code>steps &gt; x</code>&nbsp;，那么你只前进 <code>x</code>&nbsp;步。请返回前进&nbsp;<strong>至多</strong>&nbsp;<code>steps</code>步以后的 <code>url</code>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>
[&quot;BrowserHistory&quot;,&quot;visit&quot;,&quot;visit&quot;,&quot;visit&quot;,&quot;back&quot;,&quot;back&quot;,&quot;forward&quot;,&quot;visit&quot;,&quot;forward&quot;,&quot;back&quot;,&quot;back&quot;]
[[&quot;leetcode.com&quot;],[&quot;google.com&quot;],[&quot;facebook.com&quot;],[&quot;youtube.com&quot;],[1],[1],[1],[&quot;linkedin.com&quot;],[2],[2],[7]]
<strong>输出：</strong>
[null,null,null,null,&quot;facebook.com&quot;,&quot;google.com&quot;,&quot;facebook.com&quot;,null,&quot;linkedin.com&quot;,&quot;google.com&quot;,&quot;leetcode.com&quot;]

<strong>解释：</strong>
BrowserHistory browserHistory = new BrowserHistory(&quot;leetcode.com&quot;);
browserHistory.visit(&quot;google.com&quot;);       // 你原本在浏览 &quot;leetcode.com&quot; 。访问 &quot;google.com&quot;
browserHistory.visit(&quot;facebook.com&quot;);     // 你原本在浏览 &quot;google.com&quot; 。访问 &quot;facebook.com&quot;
browserHistory.visit(&quot;youtube.com&quot;);      // 你原本在浏览 &quot;facebook.com&quot; 。访问 &quot;youtube.com&quot;
browserHistory.back(1);                   // 你原本在浏览 &quot;youtube.com&quot; ，后退到 &quot;facebook.com&quot; 并返回 &quot;facebook.com&quot;
browserHistory.back(1);                   // 你原本在浏览 &quot;facebook.com&quot; ，后退到 &quot;google.com&quot; 并返回 &quot;google.com&quot;
browserHistory.forward(1);                // 你原本在浏览 &quot;google.com&quot; ，前进到 &quot;facebook.com&quot; 并返回 &quot;facebook.com&quot;
browserHistory.visit(&quot;linkedin.com&quot;);     // 你原本在浏览 &quot;facebook.com&quot; 。 访问 &quot;linkedin.com&quot;
browserHistory.forward(2);                // 你原本在浏览 &quot;linkedin.com&quot; ，你无法前进任何步数。
browserHistory.back(2);                   // 你原本在浏览 &quot;linkedin.com&quot; ，后退两步依次先到 &quot;facebook.com&quot; ，然后到 &quot;google.com&quot; ，并返回 &quot;google.com&quot;
browserHistory.back(7);                   // 你原本在浏览 &quot;google.com&quot;， 你只能后退一步到 &quot;leetcode.com&quot; ，并返回 &quot;leetcode.com&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= homepage.length &lt;= 20</code></li>
	<li><code>1 &lt;= url.length &lt;= 20</code></li>
	<li><code>1 &lt;= steps &lt;= 100</code></li>
	<li><code>homepage</code> 和&nbsp;<code>url</code>&nbsp;都只包含&nbsp;&#39;.&#39; 或者小写英文字母。</li>
	<li>最多调用&nbsp;<code>5000</code>&nbsp;次&nbsp;<code>visit</code>，&nbsp;<code>back</code>&nbsp;和&nbsp;<code>forward</code>&nbsp;函数。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 设计
- 数组
- 链表
- 数据流
- 双向链表

## 提示

1. Use two stacks: one for back history, and one for forward history. You can simulate the functions by popping an element from one stack and pushing it into the other.
2. Can you improve program runtime by using a different data structure?

## 示例

```
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
```

## 示例代码

### C++

```cpp
class BrowserHistory {
public:
    BrowserHistory(string homepage) {
        
    }
    
    void visit(string url) {
        
    }
    
    string back(int steps) {
        
    }
    
    string forward(int steps) {
        
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */
```

### Java

```java
class BrowserHistory {

    public BrowserHistory(String homepage) {
        
    }
    
    public void visit(String url) {
        
    }
    
    public String back(int steps) {
        
    }
    
    public String forward(int steps) {
        
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */
```

### Python

```python
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
```

### Python3

```python3
class BrowserHistory:

    def __init__(self, homepage: str):
        

    def visit(self, url: str) -> None:
        

    def back(self, steps: int) -> str:
        

    def forward(self, steps: int) -> str:
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
```

### C

```c



typedef struct {
    
} BrowserHistory;


BrowserHistory* browserHistoryCreate(char* homepage) {
    
}

void browserHistoryVisit(BrowserHistory* obj, char* url) {
    
}

char* browserHistoryBack(BrowserHistory* obj, int steps) {
    
}

char* browserHistoryForward(BrowserHistory* obj, int steps) {
    
}

void browserHistoryFree(BrowserHistory* obj) {
    
}

/**
 * Your BrowserHistory struct will be instantiated and called as such:
 * BrowserHistory* obj = browserHistoryCreate(homepage);
 * browserHistoryVisit(obj, url);
 
 * char* param_2 = browserHistoryBack(obj, steps);
 
 * char* param_3 = browserHistoryForward(obj, steps);
 
 * browserHistoryFree(obj);
*/
```

### C#

```csharp
public class BrowserHistory {

    public BrowserHistory(string homepage) {
        
    }
    
    public void Visit(string url) {
        
    }
    
    public string Back(int steps) {
        
    }
    
    public string Forward(int steps) {
        
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.Visit(url);
 * string param_2 = obj.Back(steps);
 * string param_3 = obj.Forward(steps);
 */
```

### JavaScript

```javascript
/**
 * @param {string} homepage
 */
var BrowserHistory = function(homepage) {
    
};

/** 
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function(url) {
    
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function(steps) {
    
};

/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function(steps) {
    
};

/** 
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */
```

### TypeScript

```typescript
class BrowserHistory {
    constructor(homepage: string) {
        
    }

    visit(url: string): void {
        
    }

    back(steps: number): string {
        
    }

    forward(steps: number): string {
        
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */
```

### PHP

```php
class BrowserHistory {
    /**
     * @param String $homepage
     */
    function __construct($homepage) {
        
    }
  
    /**
     * @param String $url
     * @return NULL
     */
    function visit($url) {
        
    }
  
    /**
     * @param Integer $steps
     * @return String
     */
    function back($steps) {
        
    }
  
    /**
     * @param Integer $steps
     * @return String
     */
    function forward($steps) {
        
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * $obj = BrowserHistory($homepage);
 * $obj->visit($url);
 * $ret_2 = $obj->back($steps);
 * $ret_3 = $obj->forward($steps);
 */
```

### Swift

```swift

class BrowserHistory {

    init(_ homepage: String) {
        
    }
    
    func visit(_ url: String) {
        
    }
    
    func back(_ steps: Int) -> String {
        
    }
    
    func forward(_ steps: Int) -> String {
        
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * let obj = BrowserHistory(homepage)
 * obj.visit(url)
 * let ret_2: String = obj.back(steps)
 * let ret_3: String = obj.forward(steps)
 */
```

### Kotlin

```kotlin
class BrowserHistory(homepage: String) {

    fun visit(url: String) {
        
    }

    fun back(steps: Int): String {
        
    }

    fun forward(steps: Int): String {
        
    }

}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */
```

### Dart

```dart
class BrowserHistory {

  BrowserHistory(String homepage) {
    
  }
  
  void visit(String url) {
    
  }
  
  String back(int steps) {
    
  }
  
  String forward(int steps) {
    
  }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = BrowserHistory(homepage);
 * obj.visit(url);
 * String param2 = obj.back(steps);
 * String param3 = obj.forward(steps);
 */
```

### Go

```golang
type BrowserHistory struct {
    
}


func Constructor(homepage string) BrowserHistory {
    
}


func (this *BrowserHistory) Visit(url string)  {
    
}


func (this *BrowserHistory) Back(steps int) string {
    
}


func (this *BrowserHistory) Forward(steps int) string {
    
}


/**
 * Your BrowserHistory object will be instantiated and called as such:
 * obj := Constructor(homepage);
 * obj.Visit(url);
 * param_2 := obj.Back(steps);
 * param_3 := obj.Forward(steps);
 */
```

### Ruby

```ruby
class BrowserHistory

=begin
    :type homepage: String
=end
    def initialize(homepage)
        
    end


=begin
    :type url: String
    :rtype: Void
=end
    def visit(url)
        
    end


=begin
    :type steps: Integer
    :rtype: String
=end
    def back(steps)
        
    end


=begin
    :type steps: Integer
    :rtype: String
=end
    def forward(steps)
        
    end


end

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory.new(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
```

### Scala

```scala
class BrowserHistory(_homepage: String) {

    def visit(url: String): Unit = {
        
    }

    def back(steps: Int): String = {
        
    }

    def forward(steps: Int): String = {
        
    }

}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * val obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * val param_2 = obj.back(steps)
 * val param_3 = obj.forward(steps)
 */
```

### Rust

```rust
struct BrowserHistory {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl BrowserHistory {

    fn new(homepage: String) -> Self {
        
    }
    
    fn visit(&self, url: String) {
        
    }
    
    fn back(&self, steps: i32) -> String {
        
    }
    
    fn forward(&self, steps: i32) -> String {
        
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * let obj = BrowserHistory::new(homepage);
 * obj.visit(url);
 * let ret_2: String = obj.back(steps);
 * let ret_3: String = obj.forward(steps);
 */
```

### Racket

```racket
(define browser-history%
  (class object%
    (super-new)
    
    ; homepage : string?
    (init-field
      homepage)
    
    ; visit : string? -> void?
    (define/public (visit url)
      )
    ; back : exact-integer? -> string?
    (define/public (back steps)
      )
    ; forward : exact-integer? -> string?
    (define/public (forward steps)
      )))

;; Your browser-history% object will be instantiated and called as such:
;; (define obj (new browser-history% [homepage homepage]))
;; (send obj visit url)
;; (define param_2 (send obj back steps))
;; (define param_3 (send obj forward steps))
```

### Erlang

```erlang
-spec browser_history_init_(Homepage :: unicode:unicode_binary()) -> any().
browser_history_init_(Homepage) ->
  .

-spec browser_history_visit(Url :: unicode:unicode_binary()) -> any().
browser_history_visit(Url) ->
  .

-spec browser_history_back(Steps :: integer()) -> unicode:unicode_binary().
browser_history_back(Steps) ->
  .

-spec browser_history_forward(Steps :: integer()) -> unicode:unicode_binary().
browser_history_forward(Steps) ->
  .


%% Your functions will be called as such:
%% browser_history_init_(Homepage),
%% browser_history_visit(Url),
%% Param_2 = browser_history_back(Steps),
%% Param_3 = browser_history_forward(Steps),

%% browser_history_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule BrowserHistory do
  @spec init_(homepage :: String.t) :: any
  def init_(homepage) do
    
  end

  @spec visit(url :: String.t) :: any
  def visit(url) do
    
  end

  @spec back(steps :: integer) :: String.t
  def back(steps) do
    
  end

  @spec forward(steps :: integer) :: String.t
  def forward(steps) do
    
  end
end

# Your functions will be called as such:
# BrowserHistory.init_(homepage)
# BrowserHistory.visit(url)
# param_2 = BrowserHistory.back(steps)
# param_3 = BrowserHistory.forward(steps)

# BrowserHistory.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class BrowserHistory {
    init(homepage: String) {

    }
    
    func visit(url: String): Unit {

    }
    
    func back(steps: Int64): String {

    }
    
    func forward(steps: Int64): String {

    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * let obj: BrowserHistory = BrowserHistory(homepage)
 * obj.visit(url)
 * let param_2 = obj.back(steps)
 * let param_3 = obj.forward(steps)
 */
```

