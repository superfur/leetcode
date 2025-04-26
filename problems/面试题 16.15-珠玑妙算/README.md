# 面试题 16.15. 珠玑妙算

## 题目描述

<p>珠玑妙算游戏（the game of master mind）的玩法如下。</p>
<p>计算机有4个槽，每个槽放一个球，颜色可能是红色（R）、黄色（Y）、绿色（G）或蓝色（B）。例如，计算机可能有RGGB 4种（槽1为红色，槽2、3为绿色，槽4为蓝色）。作为用户，你试图猜出颜色组合。打个比方，你可能会猜YRGB。要是猜对某个槽的颜色，则算一次“猜中”；要是只猜对颜色但槽位猜错了，则算一次“伪猜中”。注意，“猜中”不能算入“伪猜中”。</p>
<p>给定一种颜色组合<code>solution</code>和一个猜测<code>guess</code>，编写一个方法，返回猜中和伪猜中的次数<code>answer</code>，其中<code>answer[0]</code>为猜中的次数，<code>answer[1]</code>为伪猜中的次数。</p>
<p><strong>示例：</strong></p>
<pre><strong>输入：</strong> solution="RGBY",guess="GGRR"
<strong>输出：</strong> [1,1]
<strong>解释：</strong> 猜中1次，伪猜中1次。
</pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>len(solution) = len(guess) = 4</code></li>
<li><code>solution</code>和<code>guess</code>仅包含<code>"R"</code>,<code>"G"</code>,<code>"B"</code>,<code>"Y"</code>这4种字符</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. 首先尝试创建一个具有每个元素发生频率的数组。
2. 为了在实现中简单明了，你可能需要使用其他方法和类。

## 示例

```
"RGRB"
"BBBY"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> masterMind(string solution, string guess) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] masterMind(String solution, String guess) {
        
    }
}
```

### Python

```python
class Solution(object):
    def masterMind(self, solution, guess):
        """
        :type solution: str
        :type guess: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* masterMind(char* solution, char* guess, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MasterMind(string solution, string guess) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} solution
 * @param {string} guess
 * @return {number[]}
 */
var masterMind = function(solution, guess) {
    
};
```

### TypeScript

```typescript
function masterMind(solution: string, guess: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $solution
     * @param String $guess
     * @return Integer[]
     */
    function masterMind($solution, $guess) {
        
    }
}
```

### Swift

```swift
class Solution {
    func masterMind(_ solution: String, _ guess: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun masterMind(solution: String, guess: String): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> masterMind(String solution, String guess) {
    
  }
}
```

### Go

```golang
func masterMind(solution string, guess string) []int {
    
}
```

### Ruby

```ruby
# @param {String} solution
# @param {String} guess
# @return {Integer[]}
def master_mind(solution, guess)
    
end
```

### Scala

```scala
object Solution {
    def masterMind(solution: String, guess: String): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn master_mind(solution: String, guess: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (master-mind solution guess)
  (-> string? string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec master_mind(Solution :: unicode:unicode_binary(), Guess :: unicode:unicode_binary()) -> [integer()].
master_mind(Solution, Guess) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec master_mind(solution :: String.t, guess :: String.t) :: [integer]
  def master_mind(solution, guess) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func masterMind(solution: String, guess: String): Array<Int64> {

    }
}
```

