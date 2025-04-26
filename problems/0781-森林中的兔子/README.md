# 781. 森林中的兔子

## 题目描述

<p>森林中有未知数量的兔子。提问其中若干只兔子<strong> "还有多少只兔子与你（指被提问的兔子）颜色相同?"</strong> ，将答案收集到一个整数数组 <code>answers</code> 中，其中 <code>answers[i]</code> 是第 <code>i</code> 只兔子的回答。</p>

<p>给你数组 <code>answers</code> ，返回森林中兔子的最少数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>answers = [1,1,2]
<strong>输出：</strong>5
<strong>解释：</strong>
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。 
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。 
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。 
因此森林中兔子的最少数量是 5 只：3 只回答的和 2 只没有回答的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>answers = [10,10,10]
<strong>输出：</strong>11
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= answers.length &lt;= 1000</code></li>
	<li><code>0 &lt;= answers[i] &lt; 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 数学

## 示例

```
[1,1,2]
[10,10,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numRabbits(vector<int>& answers) {
        
    }
};
```

### Java

```java
class Solution {
    public int numRabbits(int[] answers) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
```

### C

```c
int numRabbits(int* answers, int answersSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumRabbits(int[] answers) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} answers
 * @return {number}
 */
var numRabbits = function(answers) {
    
};
```

### TypeScript

```typescript
function numRabbits(answers: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $answers
     * @return Integer
     */
    function numRabbits($answers) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numRabbits(_ answers: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numRabbits(answers: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numRabbits(List<int> answers) {
    
  }
}
```

### Go

```golang
func numRabbits(answers []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} answers
# @return {Integer}
def num_rabbits(answers)
    
end
```

### Scala

```scala
object Solution {
    def numRabbits(answers: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_rabbits(answers: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-rabbits answers)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_rabbits(Answers :: [integer()]) -> integer().
num_rabbits(Answers) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_rabbits(answers :: [integer]) :: integer
  def num_rabbits(answers) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numRabbits(answers: Array<Int64>): Int64 {

    }
}
```

