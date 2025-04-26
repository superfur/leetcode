# 904. 水果成篮

## 题目描述

<p>你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 <code>fruits</code> 表示，其中 <code>fruits[i]</code> 是第 <code>i</code> 棵树上的水果 <strong>种类</strong> 。</p>

<p>你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：</p>

<ul>
	<li>你只有 <strong>两个</strong> 篮子，并且每个篮子只能装 <strong>单一类型</strong> 的水果。每个篮子能够装的水果总量没有限制。</li>
	<li>你可以选择任意一棵树开始采摘，你必须从 <strong>每棵</strong> 树（包括开始采摘的树）上 <strong>恰好摘一个水果</strong> 。采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。</li>
	<li>一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。</li>
</ul>

<p>给你一个整数数组 <code>fruits</code> ，返回你可以收集的水果的 <strong>最大</strong> 数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>fruits = [<em><strong>1,2,1</strong></em>]
<strong>输出：</strong>3
<strong>解释：</strong>可以采摘全部 3 棵树。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>fruits = [0,<em><strong>1,2,2</strong></em>]
<strong>输出：</strong>3
<strong>解释：</strong>可以采摘 [1,2,2] 这三棵树。
如果从第一棵树开始采摘，则只能采摘 [0,1] 这两棵树。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>fruits = [1,<em><strong>2,3,2,2</strong></em>]
<strong>输出：</strong>4
<strong>解释：</strong>可以采摘 [2,3,2,2] 这四棵树。
如果从第一棵树开始采摘，则只能采摘 [1,2] 这两棵树。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>fruits = [3,3,3,<em><strong>1,2,1,1,2</strong></em>,3,3,4]
<strong>输出：</strong>5
<strong>解释：</strong>可以采摘 [1,2,1,1,2] 这五棵树。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= fruits.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= fruits[i] &lt; fruits.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 滑动窗口

## 示例

```
[1,2,1]
[0,1,2,2]
[1,2,3,2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        
    }
};
```

### Java

```java
class Solution {
    public int totalFruit(int[] fruits) {
        
    }
}
```

### Python

```python
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
```

### C

```c
int totalFruit(int* fruits, int fruitsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int TotalFruit(int[] fruits) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function(fruits) {
    
};
```

### TypeScript

```typescript
function totalFruit(fruits: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $fruits
     * @return Integer
     */
    function totalFruit($fruits) {
        
    }
}
```

### Swift

```swift
class Solution {
    func totalFruit(_ fruits: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun totalFruit(fruits: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int totalFruit(List<int> fruits) {
    
  }
}
```

### Go

```golang
func totalFruit(fruits []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} fruits
# @return {Integer}
def total_fruit(fruits)
    
end
```

### Scala

```scala
object Solution {
    def totalFruit(fruits: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn total_fruit(fruits: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (total-fruit fruits)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec total_fruit(Fruits :: [integer()]) -> integer().
total_fruit(Fruits) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec total_fruit(fruits :: [integer]) :: integer
  def total_fruit(fruits) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func totalFruit(fruits: Array<Int64>): Int64 {

    }
}
```

