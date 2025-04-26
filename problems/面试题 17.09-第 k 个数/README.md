# 面试题 17.09. 第 k 个数

## 题目描述

<p>有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>k = 5
<strong>输出：</strong>9
</pre>


## 难度

Medium

## 标签

- 哈希表
- 数学
- 动态规划
- 堆（优先队列）

## 提示

1. 明确这个问题的要求。要求满足 3a× 5b× 7c 这一形式的第 k 小的值。
2. 蛮力解法得到的形如 3a× 5b × 7c 的第 k 小的值是什么样的?
3. 在寻找 3a × 5b × 7c 的第 k 个最小值时，我们知道 a、b、c 将小于等于 k。你能生成所有可能的数字吗?
4. 查看 3a×5b×7c 对应的所有值的列表，可以观察到列表中的每个值都是 3×(列表中前面的某值)、5×(列表中前面的某值)或 7×(列表中前面的某值)。
5. 由于每个数字都是列表中先前值的 3 倍、5 倍或 7 倍，因此我们可以检查所有可能的值，然后选择下一个还没有看到的值。这将导致许多重复的工作。如何才能避免这种情况呢?
6. 不要检查列表中的所有值来寻找下一个值(通过将每个值乘以 3、5、7)，而是这样考虑:当你将一个值 x 插入列表时，可以“构造”3x、5x 和 7x 以供以后使用。
7. 当你将 x 添加到前 k 个值的列表中时，可以将 3x、5x 和 7x 添加到新的列表中。如何使其尽可能地优化?保留多个队列如何?总是需要插入 3x、5x 和 7x 吗? 或者，有时你只需要插入 7x?你需要避免相同的数字出现两次。

## 示例

```
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getKthMagicNumber(int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int getKthMagicNumber(int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getKthMagicNumber(self, k):
        """
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        
```

### C

```c
int getKthMagicNumber(int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetKthMagicNumber(int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @return {number}
 */
var getKthMagicNumber = function(k) {
    
};
```

### TypeScript

```typescript
function getKthMagicNumber(k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @return Integer
     */
    function getKthMagicNumber($k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getKthMagicNumber(_ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getKthMagicNumber(k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getKthMagicNumber(int k) {
    
  }
}
```

### Go

```golang
func getKthMagicNumber(k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @return {Integer}
def get_kth_magic_number(k)
    
end
```

### Scala

```scala
object Solution {
    def getKthMagicNumber(k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_kth_magic_number(k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-kth-magic-number k)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec get_kth_magic_number(K :: integer()) -> integer().
get_kth_magic_number(K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_kth_magic_number(k :: integer) :: integer
  def get_kth_magic_number(k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getKthMagicNumber(k: Int64): Int64 {

    }
}
```

