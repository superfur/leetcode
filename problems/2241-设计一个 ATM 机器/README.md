# 2241. 设计一个 ATM 机器

## 题目描述

<p>一个 ATM 机器，存有&nbsp;<code>5</code>&nbsp;种面值的钞票：<code>20</code>&nbsp;，<code>50</code>&nbsp;，<code>100</code>&nbsp;，<code>200</code>&nbsp;和&nbsp;<code>500</code>&nbsp;美元。初始时，ATM 机是空的。用户可以用它存或者取任意数目的钱。</p>

<p>取款时，机器会优先取 <b>较大</b>&nbsp;数额的钱。</p>

<ul>
	<li>比方说，你想取&nbsp;<code>$300</code>&nbsp;，并且机器里有&nbsp;<code>2</code>&nbsp;张 <code>$50</code>&nbsp;的钞票，<code>1</code>&nbsp;张&nbsp;<code>$100</code>&nbsp;的钞票和<code>1</code>&nbsp;张&nbsp;<code>$200</code>&nbsp;的钞票，那么机器会取出&nbsp;<code>$100</code> 和&nbsp;<code>$200</code>&nbsp;的钞票。</li>
	<li>但是，如果你想取&nbsp;<code>$600</code>&nbsp;，机器里有&nbsp;<code>3</code>&nbsp;张&nbsp;<code>$200</code>&nbsp;的钞票和<code>1</code>&nbsp;张&nbsp;<code>$500</code>&nbsp;的钞票，那么取款请求会被拒绝，因为机器会先取出&nbsp;<code>$500</code>&nbsp;的钞票，然后无法取出剩余的&nbsp;<code>$100</code>&nbsp;。注意，因为有&nbsp;<code>$500</code>&nbsp;钞票的存在，机器&nbsp;<strong>不能</strong>&nbsp;取&nbsp;<code>$200</code>&nbsp;的钞票。</li>
</ul>

<p>请你实现 ATM 类：</p>

<ul>
	<li><code>ATM()</code>&nbsp;初始化 ATM 对象。</li>
	<li><code>void deposit(int[] banknotesCount)</code>&nbsp;分别存入&nbsp;<code>$20</code>&nbsp;，<code>$50</code>，<code>$100</code>，<code>$200</code>&nbsp;和&nbsp;<code>$500</code>&nbsp;钞票的数目。</li>
	<li><code>int[] withdraw(int amount)</code>&nbsp;返回一个长度为&nbsp;<code>5</code>&nbsp;的数组，分别表示&nbsp;<code>$20</code>&nbsp;，<code>$50</code>，<code>$100</code>&nbsp;，<code>$200</code>&nbsp;和&nbsp;<code>$500</code>&nbsp;钞票的数目，并且更新 ATM 机里取款后钞票的剩余数量。如果无法取出指定数额的钱，请返回&nbsp;<code>[-1]</code>&nbsp;（这种情况下 <strong>不</strong>&nbsp;取出任何钞票）。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"]
[[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]]
<strong>输出：</strong>
[null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]]

<strong>解释：</strong>
ATM atm = new ATM();
atm.deposit([0,0,1,2,1]); // 存入 1 张 $100 ，2 张 $200 和 1 张 $500 的钞票。
atm.withdraw(600);        // 返回 [0,0,1,0,1] 。机器返回 1 张 $100 和 1 张 $500 的钞票。机器里剩余钞票的数量为 [0,0,0,2,0] 。
atm.deposit([0,1,0,1,1]); // 存入 1 张 $50 ，1 张 $200 和 1 张 $500 的钞票。
                          // 机器中剩余钞票数量为 [0,1,0,3,1] 。
atm.withdraw(600);        // 返回 [-1] 。机器会尝试取出 $500 的钞票，然后无法得到剩余的 $100 ，所以取款请求会被拒绝。
                          // 由于请求被拒绝，机器中钞票的数量不会发生改变。
atm.withdraw(550);        // 返回 [0,1,0,0,1] ，机器会返回 1 张 $50 的钞票和 1 张 $500 的钞票。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>banknotesCount.length == 5</code></li>
	<li><code>0 &lt;= banknotesCount[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= amount &lt;= 10<sup>9</sup></code></li>
	<li><strong>总共</strong>&nbsp;最多有&nbsp;<code>5000</code>&nbsp;次&nbsp;<code>withdraw</code> 和&nbsp;<code>deposit</code>&nbsp;的调用。</li>
	<li><span style="">函数 </span><code>withdraw</code> 和&nbsp;<code>deposit</code>&nbsp;至少各有 <strong>一次&nbsp;</strong>调用。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 设计
- 数组

## 提示

1. Store the number of banknotes of each denomination.
2. Can you use math to quickly evaluate a withdrawal request?

## 示例

```
["ATM","deposit","withdraw","deposit","withdraw","withdraw"]
[[],[[0,0,1,2,1]],[600],[[0,1,0,1,1]],[600],[550]]
```

## 示例代码

### C++

```cpp
class ATM {
public:
    ATM() {
        
    }
    
    void deposit(vector<int> banknotesCount) {
        
    }
    
    vector<int> withdraw(int amount) {
        
    }
};

/**
 * Your ATM object will be instantiated and called as such:
 * ATM* obj = new ATM();
 * obj->deposit(banknotesCount);
 * vector<int> param_2 = obj->withdraw(amount);
 */
```

### Java

```java
class ATM {

    public ATM() {
        
    }
    
    public void deposit(int[] banknotesCount) {
        
    }
    
    public int[] withdraw(int amount) {
        
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * ATM obj = new ATM();
 * obj.deposit(banknotesCount);
 * int[] param_2 = obj.withdraw(amount);
 */
```

### Python

```python
class ATM(object):

    def __init__(self):
        

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
```

### Python3

```python3
class ATM:

    def __init__(self):
        

    def deposit(self, banknotesCount: List[int]) -> None:
        

    def withdraw(self, amount: int) -> List[int]:
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
```

### C

```c



typedef struct {
    
} ATM;


ATM* aTMCreate() {
    
}

void aTMDeposit(ATM* obj, int* banknotesCount, int banknotesCountSize) {
    
}

int* aTMWithdraw(ATM* obj, int amount, int* retSize) {
    
}

void aTMFree(ATM* obj) {
    
}

/**
 * Your ATM struct will be instantiated and called as such:
 * ATM* obj = aTMCreate();
 * aTMDeposit(obj, banknotesCount, banknotesCountSize);
 
 * int* param_2 = aTMWithdraw(obj, amount, retSize);
 
 * aTMFree(obj);
*/
```

### C#

```csharp
public class ATM {

    public ATM() {
        
    }
    
    public void Deposit(int[] banknotesCount) {
        
    }
    
    public int[] Withdraw(int amount) {
        
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * ATM obj = new ATM();
 * obj.Deposit(banknotesCount);
 * int[] param_2 = obj.Withdraw(amount);
 */
```

### JavaScript

```javascript

var ATM = function() {
    
};

/** 
 * @param {number[]} banknotesCount
 * @return {void}
 */
ATM.prototype.deposit = function(banknotesCount) {
    
};

/** 
 * @param {number} amount
 * @return {number[]}
 */
ATM.prototype.withdraw = function(amount) {
    
};

/** 
 * Your ATM object will be instantiated and called as such:
 * var obj = new ATM()
 * obj.deposit(banknotesCount)
 * var param_2 = obj.withdraw(amount)
 */
```

### TypeScript

```typescript
class ATM {
    constructor() {
        
    }

    deposit(banknotesCount: number[]): void {
        
    }

    withdraw(amount: number): number[] {
        
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * var obj = new ATM()
 * obj.deposit(banknotesCount)
 * var param_2 = obj.withdraw(amount)
 */
```

### PHP

```php
class ATM {
    /**
     */
    function __construct() {
        
    }
  
    /**
     * @param Integer[] $banknotesCount
     * @return NULL
     */
    function deposit($banknotesCount) {
        
    }
  
    /**
     * @param Integer $amount
     * @return Integer[]
     */
    function withdraw($amount) {
        
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * $obj = ATM();
 * $obj->deposit($banknotesCount);
 * $ret_2 = $obj->withdraw($amount);
 */
```

### Swift

```swift

class ATM {

    init() {
        
    }
    
    func deposit(_ banknotesCount: [Int]) {
        
    }
    
    func withdraw(_ amount: Int) -> [Int] {
        
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * let obj = ATM()
 * obj.deposit(banknotesCount)
 * let ret_2: [Int] = obj.withdraw(amount)
 */
```

### Kotlin

```kotlin
class ATM() {

    fun deposit(banknotesCount: IntArray) {
        
    }

    fun withdraw(amount: Int): IntArray {
        
    }

}

/**
 * Your ATM object will be instantiated and called as such:
 * var obj = ATM()
 * obj.deposit(banknotesCount)
 * var param_2 = obj.withdraw(amount)
 */
```

### Dart

```dart
class ATM {

  ATM() {
    
  }
  
  void deposit(List<int> banknotesCount) {
    
  }
  
  List<int> withdraw(int amount) {
    
  }
}

/**
 * Your ATM object will be instantiated and called as such:
 * ATM obj = ATM();
 * obj.deposit(banknotesCount);
 * List<int> param2 = obj.withdraw(amount);
 */
```

### Go

```golang
type ATM struct {
    
}


func Constructor() ATM {
    
}


func (this *ATM) Deposit(banknotesCount []int)  {
    
}


func (this *ATM) Withdraw(amount int) []int {
    
}


/**
 * Your ATM object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Deposit(banknotesCount);
 * param_2 := obj.Withdraw(amount);
 */
```

### Ruby

```ruby
class ATM
    def initialize()
        
    end


=begin
    :type banknotes_count: Integer[]
    :rtype: Void
=end
    def deposit(banknotes_count)
        
    end


=begin
    :type amount: Integer
    :rtype: Integer[]
=end
    def withdraw(amount)
        
    end


end

# Your ATM object will be instantiated and called as such:
# obj = ATM.new()
# obj.deposit(banknotes_count)
# param_2 = obj.withdraw(amount)
```

### Scala

```scala
class ATM() {

    def deposit(banknotesCount: Array[Int]): Unit = {
        
    }

    def withdraw(amount: Int): Array[Int] = {
        
    }

}

/**
 * Your ATM object will be instantiated and called as such:
 * val obj = new ATM()
 * obj.deposit(banknotesCount)
 * val param_2 = obj.withdraw(amount)
 */
```

### Rust

```rust
struct ATM {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ATM {

    fn new() -> Self {
        
    }
    
    fn deposit(&self, banknotes_count: Vec<i32>) {
        
    }
    
    fn withdraw(&self, amount: i32) -> Vec<i32> {
        
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * let obj = ATM::new();
 * obj.deposit(banknotesCount);
 * let ret_2: Vec<i32> = obj.withdraw(amount);
 */
```

### Racket

```racket
(define atm%
  (class object%
    (super-new)
    
    (init-field)
    
    ; deposit : (listof exact-integer?) -> void?
    (define/public (deposit banknotes-count)
      )
    ; withdraw : exact-integer? -> (listof exact-integer?)
    (define/public (withdraw amount)
      )))

;; Your atm% object will be instantiated and called as such:
;; (define obj (new atm%))
;; (send obj deposit banknotes-count)
;; (define param_2 (send obj withdraw amount))
```

### Erlang

```erlang
-spec atm_init_() -> any().
atm_init_() ->
  .

-spec atm_deposit(BanknotesCount :: [integer()]) -> any().
atm_deposit(BanknotesCount) ->
  .

-spec atm_withdraw(Amount :: integer()) -> [integer()].
atm_withdraw(Amount) ->
  .


%% Your functions will be called as such:
%% atm_init_(),
%% atm_deposit(BanknotesCount),
%% Param_2 = atm_withdraw(Amount),

%% atm_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule ATM do
  @spec init_() :: any
  def init_() do
    
  end

  @spec deposit(banknotes_count :: [integer]) :: any
  def deposit(banknotes_count) do
    
  end

  @spec withdraw(amount :: integer) :: [integer]
  def withdraw(amount) do
    
  end
end

# Your functions will be called as such:
# ATM.init_()
# ATM.deposit(banknotes_count)
# param_2 = ATM.withdraw(amount)

# ATM.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class ATM {
    init() {

    }
    
    func deposit(banknotesCount: Array<Int64>): Unit {

    }
    
    func withdraw(amount: Int64): Array<Int64> {

    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * let obj: ATM = ATM()
 * obj.deposit(banknotesCount)
 * let param_2 = obj.withdraw(amount)
 */
```

