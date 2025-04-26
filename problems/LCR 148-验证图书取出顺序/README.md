# LCR 148. 验证图书取出顺序

## 题目描述

<p>现在图书馆有一堆图书需要放入书架，并且图书馆的书架是一种特殊的数据结构，只能按照 <strong>一定</strong> 的顺序 <strong>放入</strong> 和 <strong>拿取</strong> 书籍。</p>

<p>给定一个表示图书放入顺序的整数序列 <code>putIn</code>，请判断序列 <code>takeOut</code> 是否为按照正确的顺序拿取书籍的操作序列。你可以假设放入书架的所有书籍编号都不相同。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>putIn = [6,7,8,9,10,11], takeOut = [9,11,10,8,7,6]
<strong>输出：</strong>true
<strong>解释：</strong>我们可以按以下操作放入并拿取书籍：
push(6), push(7), push(8), push(9), pop() -&gt; 9,
push(10), push(11),pop() -&gt; 11,pop() -&gt; 10, pop() -&gt; 8, pop() -&gt; 7, pop() -&gt; 6
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>putIn = [6,7,8,9,10,11], takeOut = [11,9,8,10,6,7]
<strong>输出：</strong>false
<strong>解释：</strong>6 不能在 7 之前取出。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= putIn.length == takeOut.length &lt;= 1000</code></li>
	<li><code>0 &lt;= putIn[i], takeOut &lt; 1000</code></li>
	<li><code>putIn</code> 是 <code>takeOut</code> 的排列。</li>
</ul>

<p>注意：本题与主站 946 题相同：<a href="https://leetcode-cn.com/problems/validate-stack-sequences/">https://leetcode-cn.com/problems/validate-stack-sequences/</a></p>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 栈
- 数组
- 模拟

## 示例

```
[6,7,8,9,10,11]
[9,11,10,8,7,6]
[6,7,8,9,10,11]
[11,9,8,10,6,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool validateBookSequences(vector<int>& putIn, vector<int>& takeOut) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean validateBookSequences(int[] putIn, int[] takeOut) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validateBookSequences(self, putIn, takeOut):
        """
        :type putIn: List[int]
        :type takeOut: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def validateBookSequences(self, putIn: List[int], takeOut: List[int]) -> bool:
        
```

### C

```c
bool validateBookSequences(int* putIn, int putInSize, int* takeOut, int takeOutSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ValidateBookSequences(int[] putIn, int[] takeOut) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} putIn
 * @param {number[]} takeOut
 * @return {boolean}
 */
var validateBookSequences = function(putIn, takeOut) {
    
};
```

### TypeScript

```typescript
function validateBookSequences(putIn: number[], takeOut: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $putIn
     * @param Integer[] $takeOut
     * @return Boolean
     */
    function validateBookSequences($putIn, $takeOut) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validateBookSequences(_ putIn: [Int], _ takeOut: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validateBookSequences(putIn: IntArray, takeOut: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool validateBookSequences(List<int> putIn, List<int> takeOut) {
    
  }
}
```

### Go

```golang
func validateBookSequences(putIn []int, takeOut []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} put_in
# @param {Integer[]} take_out
# @return {Boolean}
def validate_book_sequences(put_in, take_out)
    
end
```

### Scala

```scala
object Solution {
    def validateBookSequences(putIn: Array[Int], takeOut: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn validate_book_sequences(put_in: Vec<i32>, take_out: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (validate-book-sequences putIn takeOut)
  (-> (listof exact-integer?) (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec validate_book_sequences(PutIn :: [integer()], TakeOut :: [integer()]) -> boolean().
validate_book_sequences(PutIn, TakeOut) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec validate_book_sequences(put_in :: [integer], take_out :: [integer]) :: boolean
  def validate_book_sequences(put_in, take_out) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validateBookSequences(putIn: Array<Int64>, takeOut: Array<Int64>): Bool {

    }
}
```

