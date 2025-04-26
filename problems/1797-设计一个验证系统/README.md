# 1797. 设计一个验证系统

## 题目描述

<p>你需要设计一个包含验证码的验证系统。每一次验证中，用户会收到一个新的验证码，这个验证码在 <code>currentTime</code> 时刻之后 <code>timeToLive</code> 秒过期。如果验证码被更新了，那么它会在 <code>currentTime</code> （可能与之前的 <code>currentTime</code> 不同）时刻延长 <code>timeToLive</code> 秒。</p>

<p>请你实现 <code>AuthenticationManager</code> 类：</p>

<ul>
	<li><code>AuthenticationManager(int timeToLive)</code> 构造 <code>AuthenticationManager</code> 并设置 <code>timeToLive</code> 参数。</li>
	<li><code>generate(string tokenId, int currentTime)</code> 给定 <code>tokenId</code> ，在当前时间 <code>currentTime</code> 生成一个新的验证码。</li>
	<li><code>renew(string tokenId, int currentTime)</code> 将给定 <code>tokenId</code> 且 <strong>未过期</strong> 的验证码在 <code>currentTime</code> 时刻更新。如果给定 <code>tokenId</code> 对应的验证码不存在或已过期，请你忽略该操作，不会有任何更新操作发生。</li>
	<li><code>countUnexpiredTokens(int currentTime)</code> 请返回在给定 <code>currentTime</code> 时刻，<strong>未过期</strong> 的验证码数目。</li>
</ul>

<p>如果一个验证码在时刻 <code>t</code> 过期，且另一个操作恰好在时刻 <code>t</code> 发生（<code>renew</code> 或者 <code>countUnexpiredTokens</code> 操作），过期事件 <strong>优先于</strong> 其他操作。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/copy-of-pc68_q2.png" style="width: 500px; height: 287px;" />
<pre>
<strong>输入：</strong>
["AuthenticationManager", "<code>renew</code>", "generate", "<code>countUnexpiredTokens</code>", "generate", "<code>renew</code>", "<code>renew</code>", "<code>countUnexpiredTokens</code>"]
[[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
<strong>输出：</strong>
[null, null, null, 1, null, null, null, 0]

<strong>解释：</strong>
AuthenticationManager authenticationManager = new AuthenticationManager(5); // 构造 AuthenticationManager ，设置 <code>timeToLive</code> = 5 秒。
authenticationManager.<code>renew</code>("aaa", 1); // 时刻 1 时，没有验证码的 tokenId 为 "aaa" ，没有验证码被更新。
authenticationManager.generate("aaa", 2); // 时刻 2 时，生成一个 tokenId 为 "aaa" 的新验证码。
authenticationManager.<code>countUnexpiredTokens</code>(6); // 时刻 6 时，只有 tokenId 为 "aaa" 的验证码未过期，所以返回 1 。
authenticationManager.generate("bbb", 7); // 时刻 7 时，生成一个 tokenId 为 "bbb" 的新验证码。
authenticationManager.<code>renew</code>("aaa", 8); // tokenId 为 "aaa" 的验证码在时刻 7 过期，且 8 >= 7 ，所以时刻 8 的renew 操作被忽略，没有验证码被更新。
authenticationManager.<code>renew</code>("bbb", 10); // tokenId 为 "bbb" 的验证码在时刻 10 没有过期，所以 renew 操作会执行，该 token 将在时刻 15 过期。
authenticationManager.<code>countUnexpiredTokens</code>(15); // tokenId 为 "bbb" 的验证码在时刻 15 过期，tokenId 为 "aaa" 的验证码在时刻 7 过期，所有验证码均已过期，所以返回 0 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= timeToLive <= 10<sup>8</sup></code></li>
	<li><code>1 <= currentTime <= 10<sup>8</sup></code></li>
	<li><code>1 <= tokenId.length <= 5</code></li>
	<li><code>tokenId</code> 只包含小写英文字母。</li>
	<li>所有 <code>generate</code> 函数的调用都会包含独一无二的 <code>tokenId</code> 值。</li>
	<li>所有函数调用中，<code>currentTime</code> 的值 <strong>严格递增</strong> 。</li>
	<li>所有函数的调用次数总共不超过 <code>2000</code> 次。</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 哈希表
- 链表
- 双向链表

## 提示

1. Using a map, track the expiry times of the tokens.
2. When generating a new token, add it to the map with its expiry time.
3. When renewing a token, check if it's on the map and has not expired yet. If so, update its expiry time.
4. To count unexpired tokens, iterate on the map and check for each token if it's not expired yet.

## 示例

```
["AuthenticationManager","renew","generate","countUnexpiredTokens","generate","renew","renew","countUnexpiredTokens"]
[[5],["aaa",1],["aaa",2],[6],["bbb",7],["aaa",8],["bbb",10],[15]]
```

## 示例代码

### C++

```cpp
class AuthenticationManager {
public:
    AuthenticationManager(int timeToLive) {
        
    }
    
    void generate(string tokenId, int currentTime) {
        
    }
    
    void renew(string tokenId, int currentTime) {
        
    }
    
    int countUnexpiredTokens(int currentTime) {
        
    }
};

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager* obj = new AuthenticationManager(timeToLive);
 * obj->generate(tokenId,currentTime);
 * obj->renew(tokenId,currentTime);
 * int param_3 = obj->countUnexpiredTokens(currentTime);
 */
```

### Java

```java
class AuthenticationManager {

    public AuthenticationManager(int timeToLive) {
        
    }
    
    public void generate(String tokenId, int currentTime) {
        
    }
    
    public void renew(String tokenId, int currentTime) {
        
    }
    
    public int countUnexpiredTokens(int currentTime) {
        
    }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager obj = new AuthenticationManager(timeToLive);
 * obj.generate(tokenId,currentTime);
 * obj.renew(tokenId,currentTime);
 * int param_3 = obj.countUnexpiredTokens(currentTime);
 */
```

### Python

```python
class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
```

### Python3

```python3
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
```

### C

```c



typedef struct {
    
} AuthenticationManager;


AuthenticationManager* authenticationManagerCreate(int timeToLive) {
    
}

void authenticationManagerGenerate(AuthenticationManager* obj, char* tokenId, int currentTime) {
    
}

void authenticationManagerRenew(AuthenticationManager* obj, char* tokenId, int currentTime) {
    
}

int authenticationManagerCountUnexpiredTokens(AuthenticationManager* obj, int currentTime) {
    
}

void authenticationManagerFree(AuthenticationManager* obj) {
    
}

/**
 * Your AuthenticationManager struct will be instantiated and called as such:
 * AuthenticationManager* obj = authenticationManagerCreate(timeToLive);
 * authenticationManagerGenerate(obj, tokenId, currentTime);
 
 * authenticationManagerRenew(obj, tokenId, currentTime);
 
 * int param_3 = authenticationManagerCountUnexpiredTokens(obj, currentTime);
 
 * authenticationManagerFree(obj);
*/
```

### C#

```csharp
public class AuthenticationManager {

    public AuthenticationManager(int timeToLive) {
        
    }
    
    public void Generate(string tokenId, int currentTime) {
        
    }
    
    public void Renew(string tokenId, int currentTime) {
        
    }
    
    public int CountUnexpiredTokens(int currentTime) {
        
    }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager obj = new AuthenticationManager(timeToLive);
 * obj.Generate(tokenId,currentTime);
 * obj.Renew(tokenId,currentTime);
 * int param_3 = obj.CountUnexpiredTokens(currentTime);
 */
```

### JavaScript

```javascript
/**
 * @param {number} timeToLive
 */
var AuthenticationManager = function(timeToLive) {
    
};

/** 
 * @param {string} tokenId 
 * @param {number} currentTime
 * @return {void}
 */
AuthenticationManager.prototype.generate = function(tokenId, currentTime) {
    
};

/** 
 * @param {string} tokenId 
 * @param {number} currentTime
 * @return {void}
 */
AuthenticationManager.prototype.renew = function(tokenId, currentTime) {
    
};

/** 
 * @param {number} currentTime
 * @return {number}
 */
AuthenticationManager.prototype.countUnexpiredTokens = function(currentTime) {
    
};

/** 
 * Your AuthenticationManager object will be instantiated and called as such:
 * var obj = new AuthenticationManager(timeToLive)
 * obj.generate(tokenId,currentTime)
 * obj.renew(tokenId,currentTime)
 * var param_3 = obj.countUnexpiredTokens(currentTime)
 */
```

### TypeScript

```typescript
class AuthenticationManager {
    constructor(timeToLive: number) {
        
    }

    generate(tokenId: string, currentTime: number): void {
        
    }

    renew(tokenId: string, currentTime: number): void {
        
    }

    countUnexpiredTokens(currentTime: number): number {
        
    }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * var obj = new AuthenticationManager(timeToLive)
 * obj.generate(tokenId,currentTime)
 * obj.renew(tokenId,currentTime)
 * var param_3 = obj.countUnexpiredTokens(currentTime)
 */
```

### PHP

```php
class AuthenticationManager {
    /**
     * @param Integer $timeToLive
     */
    function __construct($timeToLive) {
        
    }
  
    /**
     * @param String $tokenId
     * @param Integer $currentTime
     * @return NULL
     */
    function generate($tokenId, $currentTime) {
        
    }
  
    /**
     * @param String $tokenId
     * @param Integer $currentTime
     * @return NULL
     */
    function renew($tokenId, $currentTime) {
        
    }
  
    /**
     * @param Integer $currentTime
     * @return Integer
     */
    function countUnexpiredTokens($currentTime) {
        
    }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * $obj = AuthenticationManager($timeToLive);
 * $obj->generate($tokenId, $currentTime);
 * $obj->renew($tokenId, $currentTime);
 * $ret_3 = $obj->countUnexpiredTokens($currentTime);
 */
```

### Swift

```swift

class AuthenticationManager {

    init(_ timeToLive: Int) {
        
    }
    
    func generate(_ tokenId: String, _ currentTime: Int) {
        
    }
    
    func renew(_ tokenId: String, _ currentTime: Int) {
        
    }
    
    func countUnexpiredTokens(_ currentTime: Int) -> Int {
        
    }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * let obj = AuthenticationManager(timeToLive)
 * obj.generate(tokenId, currentTime)
 * obj.renew(tokenId, currentTime)
 * let ret_3: Int = obj.countUnexpiredTokens(currentTime)
 */
```

### Kotlin

```kotlin
class AuthenticationManager(timeToLive: Int) {

    fun generate(tokenId: String, currentTime: Int) {
        
    }

    fun renew(tokenId: String, currentTime: Int) {
        
    }

    fun countUnexpiredTokens(currentTime: Int): Int {
        
    }

}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * var obj = AuthenticationManager(timeToLive)
 * obj.generate(tokenId,currentTime)
 * obj.renew(tokenId,currentTime)
 * var param_3 = obj.countUnexpiredTokens(currentTime)
 */
```

### Dart

```dart
class AuthenticationManager {

  AuthenticationManager(int timeToLive) {
    
  }
  
  void generate(String tokenId, int currentTime) {
    
  }
  
  void renew(String tokenId, int currentTime) {
    
  }
  
  int countUnexpiredTokens(int currentTime) {
    
  }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager obj = AuthenticationManager(timeToLive);
 * obj.generate(tokenId,currentTime);
 * obj.renew(tokenId,currentTime);
 * int param3 = obj.countUnexpiredTokens(currentTime);
 */
```

### Go

```golang
type AuthenticationManager struct {
    
}


func Constructor(timeToLive int) AuthenticationManager {
    
}


func (this *AuthenticationManager) Generate(tokenId string, currentTime int)  {
    
}


func (this *AuthenticationManager) Renew(tokenId string, currentTime int)  {
    
}


func (this *AuthenticationManager) CountUnexpiredTokens(currentTime int) int {
    
}


/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * obj := Constructor(timeToLive);
 * obj.Generate(tokenId,currentTime);
 * obj.Renew(tokenId,currentTime);
 * param_3 := obj.CountUnexpiredTokens(currentTime);
 */
```

### Ruby

```ruby
class AuthenticationManager

=begin
    :type time_to_live: Integer
=end
    def initialize(time_to_live)
        
    end


=begin
    :type token_id: String
    :type current_time: Integer
    :rtype: Void
=end
    def generate(token_id, current_time)
        
    end


=begin
    :type token_id: String
    :type current_time: Integer
    :rtype: Void
=end
    def renew(token_id, current_time)
        
    end


=begin
    :type current_time: Integer
    :rtype: Integer
=end
    def count_unexpired_tokens(current_time)
        
    end


end

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager.new(time_to_live)
# obj.generate(token_id, current_time)
# obj.renew(token_id, current_time)
# param_3 = obj.count_unexpired_tokens(current_time)
```

### Scala

```scala
class AuthenticationManager(_timeToLive: Int) {

    def generate(tokenId: String, currentTime: Int): Unit = {
        
    }

    def renew(tokenId: String, currentTime: Int): Unit = {
        
    }

    def countUnexpiredTokens(currentTime: Int): Int = {
        
    }

}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * val obj = new AuthenticationManager(timeToLive)
 * obj.generate(tokenId,currentTime)
 * obj.renew(tokenId,currentTime)
 * val param_3 = obj.countUnexpiredTokens(currentTime)
 */
```

### Rust

```rust
struct AuthenticationManager {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl AuthenticationManager {

    fn new(timeToLive: i32) -> Self {
        
    }
    
    fn generate(&self, token_id: String, current_time: i32) {
        
    }
    
    fn renew(&self, token_id: String, current_time: i32) {
        
    }
    
    fn count_unexpired_tokens(&self, current_time: i32) -> i32 {
        
    }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * let obj = AuthenticationManager::new(timeToLive);
 * obj.generate(tokenId, currentTime);
 * obj.renew(tokenId, currentTime);
 * let ret_3: i32 = obj.count_unexpired_tokens(currentTime);
 */
```

### Racket

```racket
(define authentication-manager%
  (class object%
    (super-new)
    
    ; time-to-live : exact-integer?
    (init-field
      time-to-live)
    
    ; generate : string? exact-integer? -> void?
    (define/public (generate token-id current-time)
      )
    ; renew : string? exact-integer? -> void?
    (define/public (renew token-id current-time)
      )
    ; count-unexpired-tokens : exact-integer? -> exact-integer?
    (define/public (count-unexpired-tokens current-time)
      )))

;; Your authentication-manager% object will be instantiated and called as such:
;; (define obj (new authentication-manager% [time-to-live time-to-live]))
;; (send obj generate token-id current-time)
;; (send obj renew token-id current-time)
;; (define param_3 (send obj count-unexpired-tokens current-time))
```

### Erlang

```erlang
-spec authentication_manager_init_(TimeToLive :: integer()) -> any().
authentication_manager_init_(TimeToLive) ->
  .

-spec authentication_manager_generate(TokenId :: unicode:unicode_binary(), CurrentTime :: integer()) -> any().
authentication_manager_generate(TokenId, CurrentTime) ->
  .

-spec authentication_manager_renew(TokenId :: unicode:unicode_binary(), CurrentTime :: integer()) -> any().
authentication_manager_renew(TokenId, CurrentTime) ->
  .

-spec authentication_manager_count_unexpired_tokens(CurrentTime :: integer()) -> integer().
authentication_manager_count_unexpired_tokens(CurrentTime) ->
  .


%% Your functions will be called as such:
%% authentication_manager_init_(TimeToLive),
%% authentication_manager_generate(TokenId, CurrentTime),
%% authentication_manager_renew(TokenId, CurrentTime),
%% Param_3 = authentication_manager_count_unexpired_tokens(CurrentTime),

%% authentication_manager_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule AuthenticationManager do
  @spec init_(time_to_live :: integer) :: any
  def init_(time_to_live) do
    
  end

  @spec generate(token_id :: String.t, current_time :: integer) :: any
  def generate(token_id, current_time) do
    
  end

  @spec renew(token_id :: String.t, current_time :: integer) :: any
  def renew(token_id, current_time) do
    
  end

  @spec count_unexpired_tokens(current_time :: integer) :: integer
  def count_unexpired_tokens(current_time) do
    
  end
end

# Your functions will be called as such:
# AuthenticationManager.init_(time_to_live)
# AuthenticationManager.generate(token_id, current_time)
# AuthenticationManager.renew(token_id, current_time)
# param_3 = AuthenticationManager.count_unexpired_tokens(current_time)

# AuthenticationManager.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class AuthenticationManager {
    init(timeToLive: Int64) {

    }
    
    func generate(tokenId: String, currentTime: Int64): Unit {

    }
    
    func renew(tokenId: String, currentTime: Int64): Unit {

    }
    
    func countUnexpiredTokens(currentTime: Int64): Int64 {

    }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * let obj: AuthenticationManager = AuthenticationManager(timeToLive)
 * obj.generate(tokenId,currentTime)
 * obj.renew(tokenId,currentTime)
 * let param_3 = obj.countUnexpiredTokens(currentTime)
 */
```

