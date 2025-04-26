# 1780. 判断一个数字是否可以表示成三的幂的和

## 题目描述

<p>给你一个整数 <code>n</code> ，如果你可以将 <code>n</code> 表示成若干个不同的三的幂之和，请你返回 <code>true</code> ，否则请返回 <code>false</code> 。</p>

<p>对于一个整数 <code>y</code> ，如果存在整数 <code>x</code> 满足 <code>y == 3<sup>x</sup></code> ，我们称这个整数 <code>y</code> 是三的幂。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>n = 12
<b>输出：</b>true
<b>解释：</b>12 = 3<sup>1</sup> + 3<sup>2</sup>
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>n = 91
<b>输出：</b>true
<b>解释：</b>91 = 3<sup>0</sup> + 3<sup>2</sup> + 3<sup>4</sup>
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>n = 21
<b>输出：</b>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学

## 提示

1. Let's note that the maximum power of 3 you'll use in your soln is 3^16
2. The number can not be represented as a sum of powers of 3 if it's ternary presentation has a 2 in it

## 示例

```
12
91
21
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkPowersOfThree(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkPowersOfThree(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
```

### C

```c
bool checkPowersOfThree(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckPowersOfThree(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var checkPowersOfThree = function(n) {
    
};
```

### TypeScript

```typescript
function checkPowersOfThree(n: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function checkPowersOfThree($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkPowersOfThree(_ n: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkPowersOfThree(n: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkPowersOfThree(int n) {
    
  }
}
```

### Go

```golang
func checkPowersOfThree(n int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def check_powers_of_three(n)
    
end
```

### Scala

```scala
object Solution {
    def checkPowersOfThree(n: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_powers_of_three(n: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-powers-of-three n)
  (-> exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec check_powers_of_three(N :: integer()) -> boolean().
check_powers_of_three(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_powers_of_three(n :: integer) :: boolean
  def check_powers_of_three(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkPowersOfThree(n: Int64): Bool {

    }
}
```

