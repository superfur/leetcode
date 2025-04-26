# 3270. 求出数字答案

## 题目描述

<p>给你三个 <strong>正</strong>&nbsp;整数&nbsp;<code>num1</code>&nbsp;，<code>num2</code>&nbsp;和&nbsp;<code>num3</code>&nbsp;。</p>

<p>数字 <code>num1</code>&nbsp;，<code>num2</code>&nbsp;和 <code>num3</code>&nbsp;的数字答案 <code>key</code>&nbsp;是一个四位数，定义如下：</p>

<ul>
	<li>一开始，如果有数字 <strong>少于</strong>&nbsp;四位数，给它补 <strong>前导 0 </strong>。</li>
	<li>答案 <code>key</code>&nbsp;的第&nbsp;<code>i</code>&nbsp;个数位（<code>1 &lt;= i &lt;= 4</code>）为&nbsp;<code>num1</code>&nbsp;，<code>num2</code>&nbsp;和&nbsp;<code>num3</code>&nbsp;第&nbsp;<code>i</code>&nbsp;个数位中的&nbsp;<strong>最小</strong>&nbsp;值。</li>
</ul>

<p>请你返回三个数字 <strong>没有</strong>&nbsp;前导 0 的数字答案。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>num1 = 1, num2 = 10, num3 = 1000</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><b>解释：</b></p>

<p>补前导 0 后，<code>num1</code>&nbsp;变为&nbsp;<code>"0001"</code>&nbsp;，<code>num2</code> 变为&nbsp;<code>"0010"</code>&nbsp;，<code>num3</code>&nbsp;保持不变，为&nbsp;<code>"1000"</code>&nbsp;。</p>

<ul>
	<li>数字答案 <code>key</code>&nbsp;的第&nbsp;<code>1</code>&nbsp;个数位为&nbsp;<code>min(0, 0, 1)</code>&nbsp;。</li>
	<li>数字答案 <code>key</code>&nbsp;的第&nbsp;<code>2</code>&nbsp;个数位为&nbsp;<code>min(0, 0, 0)</code>&nbsp;。</li>
	<li>数字答案 <code>key</code>&nbsp;的第 <code>3</code> 个数位为&nbsp;<code>min(0, 1, 0)</code>&nbsp;。</li>
	<li>数字答案 <code>key</code>&nbsp;的第 <code>4</code> 个数位为&nbsp;<code>min(1, 0, 0)</code>&nbsp;。</li>
</ul>

<p>所以数字答案为&nbsp;<code>"0000"</code>&nbsp;，也就是 0 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">num1 = 987, num2 = 879, num3 = 798</span></p>

<p><span class="example-io"><b>输出：</b>777</span></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>num1 = 1, num2 = 2, num3 = 3</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num1, num2, num3 &lt;= 9999</code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 示例

```
1
10
1000
987
879
798
1
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int generateKey(int num1, int num2, int num3) {
        
    }
};
```

### Java

```java
class Solution {
    public int generateKey(int num1, int num2, int num3) {
        
    }
}
```

### Python

```python
class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        
```

### C

```c
int generateKey(int num1, int num2, int num3) {
    
}
```

### C#

```csharp
public class Solution {
    public int GenerateKey(int num1, int num2, int num3) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num1
 * @param {number} num2
 * @param {number} num3
 * @return {number}
 */
var generateKey = function(num1, num2, num3) {
    
};
```

### TypeScript

```typescript
function generateKey(num1: number, num2: number, num3: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num1
     * @param Integer $num2
     * @param Integer $num3
     * @return Integer
     */
    function generateKey($num1, $num2, $num3) {
        
    }
}
```

### Swift

```swift
class Solution {
    func generateKey(_ num1: Int, _ num2: Int, _ num3: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun generateKey(num1: Int, num2: Int, num3: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int generateKey(int num1, int num2, int num3) {
    
  }
}
```

### Go

```golang
func generateKey(num1 int, num2 int, num3 int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num1
# @param {Integer} num2
# @param {Integer} num3
# @return {Integer}
def generate_key(num1, num2, num3)
    
end
```

### Scala

```scala
object Solution {
    def generateKey(num1: Int, num2: Int, num3: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn generate_key(num1: i32, num2: i32, num3: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (generate-key num1 num2 num3)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec generate_key(Num1 :: integer(), Num2 :: integer(), Num3 :: integer()) -> integer().
generate_key(Num1, Num2, Num3) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec generate_key(num1 :: integer, num2 :: integer, num3 :: integer) :: integer
  def generate_key(num1, num2, num3) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func generateKey(num1: Int64, num2: Int64, num3: Int64): Int64 {

    }
}
```

