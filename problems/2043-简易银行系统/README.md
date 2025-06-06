# 2043. 简易银行系统

## 题目描述

<p>你的任务是为一个很受欢迎的银行设计一款程序，以自动化执行所有传入的交易（转账，存款和取款）。银行共有 <code>n</code> 个账户，编号从 <code>1</code> 到 <code>n</code> 。每个账号的初始余额存储在一个下标从 <strong>0</strong> 开始的整数数组 <code>balance</code>&nbsp;中，其中第 <code>(i + 1)</code> 个账户的初始余额是 <code>balance[i]</code> 。</p>

<p>请你执行所有 <strong>有效的</strong> 交易。如果满足下面全部条件，则交易 <strong>有效</strong> ：</p>

<ul>
	<li>指定的账户数量在 <code>1</code> 和 <code>n</code> 之间，且</li>
	<li>取款或者转账需要的钱的总数 <strong>小于或者等于</strong> 账户余额。</li>
</ul>

<p>实现 <code>Bank</code> 类：</p>

<ul>
	<li><code>Bank(long[] balance)</code> 使用下标从 <strong>0</strong> 开始的整数数组 <code>balance</code> 初始化该对象。</li>
	<li><code>boolean transfer(int account1, int account2, long money)</code> 从编号为&nbsp;<code>account1</code> 的账户向编号为 <code>account2</code> 的账户转帐 <code>money</code> 美元。如果交易成功，返回 <code>true</code> ，否则，返回 <code>false</code> 。</li>
	<li><code>boolean deposit(int account, long money)</code> 向编号为&nbsp;<code>account</code> 的账户存款 <code>money</code> 美元。如果交易成功，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
	<li><code>boolean withdraw(int account, long money)</code> 从编号为 <code>account</code> 的账户取款 <code>money</code> 美元。如果交易成功，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入</strong>：
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
<strong>输出：</strong>
[null, true, true, true, false, false]

<strong>解释：</strong>
Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    // 返回 true ，账户 3 的余额是 $20 ，所以可以取款 $10 。
                         // 账户 3 余额为 $20 - $10 = $10 。
bank.transfer(5, 1, 20); // 返回 true ，账户 5 的余额是 $30 ，所以可以转账 $20 。
                         // 账户 5 的余额为 $30 - $20 = $10 ，账户 1 的余额为 $10 + $20 = $30 。
bank.deposit(5, 20);     // 返回 true ，可以向账户 5 存款 $20 。
                         // 账户 5 的余额为 $10 + $20 = $30 。
bank.transfer(3, 4, 15); // 返回 false ，账户 3 的当前余额是 $10 。
                         // 所以无法转账 $15 。
bank.withdraw(10, 50);   // 返回 false ，交易无效，因为账户 10 并不存在。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == balance.length</code></li>
	<li><code>1 &lt;= n, account, account1, account2 &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= balance[i], money &lt;= 10<sup>12</sup></code></li>
	<li><code>transfer</code>, <code>deposit</code>, <code>withdraw</code> 三个函数，<strong>每个</strong> 最多调用 <code>10<sup>4</sup></code> 次</li>
</ul>


## 难度

Medium

## 标签

- 设计
- 数组
- 哈希表
- 模拟

## 提示

1. How do you determine if a transaction will fail?
2. Simply apply the operations if the transaction is valid.

## 示例

```
["Bank","withdraw","transfer","deposit","transfer","withdraw"]
[[[10,100,20,50,30]],[3,10],[5,1,20],[5,20],[3,4,15],[10,50]]
```

## 示例代码

### C++

```cpp
class Bank {
public:
    Bank(vector<long long>& balance) {
        
    }
    
    bool transfer(int account1, int account2, long long money) {
        
    }
    
    bool deposit(int account, long long money) {
        
    }
    
    bool withdraw(int account, long long money) {
        
    }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */
```

### Java

```java
class Bank {

    public Bank(long[] balance) {
        
    }
    
    public boolean transfer(int account1, int account2, long money) {
        
    }
    
    public boolean deposit(int account, long money) {
        
    }
    
    public boolean withdraw(int account, long money) {
        
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */
```

### Python

```python
class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
```

### Python3

```python3
class Bank:

    def __init__(self, balance: List[int]):
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        

    def deposit(self, account: int, money: int) -> bool:
        

    def withdraw(self, account: int, money: int) -> bool:
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
```

### C

```c



typedef struct {
    
} Bank;


Bank* bankCreate(long long* balance, int balanceSize) {
    
}

bool bankTransfer(Bank* obj, int account1, int account2, long long money) {
    
}

bool bankDeposit(Bank* obj, int account, long long money) {
    
}

bool bankWithdraw(Bank* obj, int account, long long money) {
    
}

void bankFree(Bank* obj) {
    
}

/**
 * Your Bank struct will be instantiated and called as such:
 * Bank* obj = bankCreate(balance, balanceSize);
 * bool param_1 = bankTransfer(obj, account1, account2, money);
 
 * bool param_2 = bankDeposit(obj, account, money);
 
 * bool param_3 = bankWithdraw(obj, account, money);
 
 * bankFree(obj);
*/
```

### C#

```csharp
public class Bank {

    public Bank(long[] balance) {
        
    }
    
    public bool Transfer(int account1, int account2, long money) {
        
    }
    
    public bool Deposit(int account, long money) {
        
    }
    
    public bool Withdraw(int account, long money) {
        
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * bool param_1 = obj.Transfer(account1,account2,money);
 * bool param_2 = obj.Deposit(account,money);
 * bool param_3 = obj.Withdraw(account,money);
 */
```

### JavaScript

```javascript
/**
 * @param {number[]} balance
 */
var Bank = function(balance) {
    
};

/** 
 * @param {number} account1 
 * @param {number} account2 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.transfer = function(account1, account2, money) {
    
};

/** 
 * @param {number} account 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.deposit = function(account, money) {
    
};

/** 
 * @param {number} account 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.withdraw = function(account, money) {
    
};

/** 
 * Your Bank object will be instantiated and called as such:
 * var obj = new Bank(balance)
 * var param_1 = obj.transfer(account1,account2,money)
 * var param_2 = obj.deposit(account,money)
 * var param_3 = obj.withdraw(account,money)
 */
```

### TypeScript

```typescript
class Bank {
    constructor(balance: number[]) {
        
    }

    transfer(account1: number, account2: number, money: number): boolean {
        
    }

    deposit(account: number, money: number): boolean {
        
    }

    withdraw(account: number, money: number): boolean {
        
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * var obj = new Bank(balance)
 * var param_1 = obj.transfer(account1,account2,money)
 * var param_2 = obj.deposit(account,money)
 * var param_3 = obj.withdraw(account,money)
 */
```

### PHP

```php
class Bank {
    /**
     * @param Integer[] $balance
     */
    function __construct($balance) {
        
    }
  
    /**
     * @param Integer $account1
     * @param Integer $account2
     * @param Integer $money
     * @return Boolean
     */
    function transfer($account1, $account2, $money) {
        
    }
  
    /**
     * @param Integer $account
     * @param Integer $money
     * @return Boolean
     */
    function deposit($account, $money) {
        
    }
  
    /**
     * @param Integer $account
     * @param Integer $money
     * @return Boolean
     */
    function withdraw($account, $money) {
        
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * $obj = Bank($balance);
 * $ret_1 = $obj->transfer($account1, $account2, $money);
 * $ret_2 = $obj->deposit($account, $money);
 * $ret_3 = $obj->withdraw($account, $money);
 */
```

### Swift

```swift

class Bank {

    init(_ balance: [Int]) {
        
    }
    
    func transfer(_ account1: Int, _ account2: Int, _ money: Int) -> Bool {
        
    }
    
    func deposit(_ account: Int, _ money: Int) -> Bool {
        
    }
    
    func withdraw(_ account: Int, _ money: Int) -> Bool {
        
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * let obj = Bank(balance)
 * let ret_1: Bool = obj.transfer(account1, account2, money)
 * let ret_2: Bool = obj.deposit(account, money)
 * let ret_3: Bool = obj.withdraw(account, money)
 */
```

### Kotlin

```kotlin
class Bank(balance: LongArray) {

    fun transfer(account1: Int, account2: Int, money: Long): Boolean {
        
    }

    fun deposit(account: Int, money: Long): Boolean {
        
    }

    fun withdraw(account: Int, money: Long): Boolean {
        
    }

}

/**
 * Your Bank object will be instantiated and called as such:
 * var obj = Bank(balance)
 * var param_1 = obj.transfer(account1,account2,money)
 * var param_2 = obj.deposit(account,money)
 * var param_3 = obj.withdraw(account,money)
 */
```

### Dart

```dart
class Bank {

  Bank(List<int> balance) {
    
  }
  
  bool transfer(int account1, int account2, int money) {
    
  }
  
  bool deposit(int account, int money) {
    
  }
  
  bool withdraw(int account, int money) {
    
  }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = Bank(balance);
 * bool param1 = obj.transfer(account1,account2,money);
 * bool param2 = obj.deposit(account,money);
 * bool param3 = obj.withdraw(account,money);
 */
```

### Go

```golang
type Bank struct {
    
}


func Constructor(balance []int64) Bank {
    
}


func (this *Bank) Transfer(account1 int, account2 int, money int64) bool {
    
}


func (this *Bank) Deposit(account int, money int64) bool {
    
}


func (this *Bank) Withdraw(account int, money int64) bool {
    
}


/**
 * Your Bank object will be instantiated and called as such:
 * obj := Constructor(balance);
 * param_1 := obj.Transfer(account1,account2,money);
 * param_2 := obj.Deposit(account,money);
 * param_3 := obj.Withdraw(account,money);
 */
```

### Ruby

```ruby
class Bank

=begin
    :type balance: Integer[]
=end
    def initialize(balance)
        
    end


=begin
    :type account1: Integer
    :type account2: Integer
    :type money: Integer
    :rtype: Boolean
=end
    def transfer(account1, account2, money)
        
    end


=begin
    :type account: Integer
    :type money: Integer
    :rtype: Boolean
=end
    def deposit(account, money)
        
    end


=begin
    :type account: Integer
    :type money: Integer
    :rtype: Boolean
=end
    def withdraw(account, money)
        
    end


end

# Your Bank object will be instantiated and called as such:
# obj = Bank.new(balance)
# param_1 = obj.transfer(account1, account2, money)
# param_2 = obj.deposit(account, money)
# param_3 = obj.withdraw(account, money)
```

### Scala

```scala
class Bank(_balance: Array[Long]) {

    def transfer(account1: Int, account2: Int, money: Long): Boolean = {
        
    }

    def deposit(account: Int, money: Long): Boolean = {
        
    }

    def withdraw(account: Int, money: Long): Boolean = {
        
    }

}

/**
 * Your Bank object will be instantiated and called as such:
 * val obj = new Bank(balance)
 * val param_1 = obj.transfer(account1,account2,money)
 * val param_2 = obj.deposit(account,money)
 * val param_3 = obj.withdraw(account,money)
 */
```

### Rust

```rust
struct Bank {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Bank {

    fn new(balance: Vec<i64>) -> Self {
        
    }
    
    fn transfer(&self, account1: i32, account2: i32, money: i64) -> bool {
        
    }
    
    fn deposit(&self, account: i32, money: i64) -> bool {
        
    }
    
    fn withdraw(&self, account: i32, money: i64) -> bool {
        
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * let obj = Bank::new(balance);
 * let ret_1: bool = obj.transfer(account1, account2, money);
 * let ret_2: bool = obj.deposit(account, money);
 * let ret_3: bool = obj.withdraw(account, money);
 */
```

### Racket

```racket
(define bank%
  (class object%
    (super-new)
    
    ; balance : (listof exact-integer?)
    (init-field
      balance)
    
    ; transfer : exact-integer? exact-integer? exact-integer? -> boolean?
    (define/public (transfer account1 account2 money)
      )
    ; deposit : exact-integer? exact-integer? -> boolean?
    (define/public (deposit account money)
      )
    ; withdraw : exact-integer? exact-integer? -> boolean?
    (define/public (withdraw account money)
      )))

;; Your bank% object will be instantiated and called as such:
;; (define obj (new bank% [balance balance]))
;; (define param_1 (send obj transfer account1 account2 money))
;; (define param_2 (send obj deposit account money))
;; (define param_3 (send obj withdraw account money))
```

### Erlang

```erlang
-spec bank_init_(Balance :: [integer()]) -> any().
bank_init_(Balance) ->
  .

-spec bank_transfer(Account1 :: integer(), Account2 :: integer(), Money :: integer()) -> boolean().
bank_transfer(Account1, Account2, Money) ->
  .

-spec bank_deposit(Account :: integer(), Money :: integer()) -> boolean().
bank_deposit(Account, Money) ->
  .

-spec bank_withdraw(Account :: integer(), Money :: integer()) -> boolean().
bank_withdraw(Account, Money) ->
  .


%% Your functions will be called as such:
%% bank_init_(Balance),
%% Param_1 = bank_transfer(Account1, Account2, Money),
%% Param_2 = bank_deposit(Account, Money),
%% Param_3 = bank_withdraw(Account, Money),

%% bank_init_ will be called before every test case, in which you can do some necessary initializations.
```

### Elixir

```elixir
defmodule Bank do
  @spec init_(balance :: [integer]) :: any
  def init_(balance) do
    
  end

  @spec transfer(account1 :: integer, account2 :: integer, money :: integer) :: boolean
  def transfer(account1, account2, money) do
    
  end

  @spec deposit(account :: integer, money :: integer) :: boolean
  def deposit(account, money) do
    
  end

  @spec withdraw(account :: integer, money :: integer) :: boolean
  def withdraw(account, money) do
    
  end
end

# Your functions will be called as such:
# Bank.init_(balance)
# param_1 = Bank.transfer(account1, account2, money)
# param_2 = Bank.deposit(account, money)
# param_3 = Bank.withdraw(account, money)

# Bank.init_ will be called before every test case, in which you can do some necessary initializations.
```

### Cangjie

```cangjie
class Bank {
    init(balance: Array<Int64>) {

    }
    
    func transfer(account1: Int64, account2: Int64, money: Int64): Bool {

    }
    
    func deposit(account: Int64, money: Int64): Bool {

    }
    
    func withdraw(account: Int64, money: Int64): Bool {

    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * let obj: Bank = Bank(balance)
 * let param_1 = obj.transfer(account1,account2,money)
 * let param_2 = obj.deposit(account,money)
 * let param_3 = obj.withdraw(account,money)
 */
```

