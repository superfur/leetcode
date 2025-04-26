# 1276. 不浪费原料的汉堡制作方案

## 题目描述

<p>圣诞活动预热开始啦，汉堡店推出了全新的汉堡套餐。为了避免浪费原料，请你帮他们制定合适的制作计划。</p>

<p>给你两个整数&nbsp;<code>tomatoSlices</code>&nbsp;和&nbsp;<code>cheeseSlices</code>，分别表示番茄片和奶酪片的数目。不同汉堡的原料搭配如下：</p>

<ul>
	<li><strong>巨无霸汉堡：</strong>4 片番茄和 1 片奶酪</li>
	<li><strong>小皇堡：</strong>2 片番茄和&nbsp;1 片奶酪</li>
</ul>

<p>请你以&nbsp;<code>[total_jumbo, total_small]</code>（[巨无霸汉堡总数，小皇堡总数]）的格式返回恰当的制作方案，使得剩下的番茄片&nbsp;<code>tomatoSlices</code>&nbsp;和奶酪片&nbsp;<code>cheeseSlices</code>&nbsp;的数量都是&nbsp;<code>0</code>。</p>

<p>如果无法使剩下的番茄片&nbsp;<code>tomatoSlices</code>&nbsp;和奶酪片&nbsp;<code>cheeseSlices</code>&nbsp;的数量为&nbsp;<code>0</code>，就请返回&nbsp;<code>[]</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>tomatoSlices = 16, cheeseSlices = 7
<strong>输出：</strong>[1,6]
<strong>解释：</strong>制作 1 个巨无霸汉堡和 6 个小皇堡需要 4*1 + 2*6 = 16 片番茄和 1 + 6 = 7 片奶酪。不会剩下原料。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>tomatoSlices = 17, cheeseSlices = 4
<strong>输出：</strong>[]
<strong>解释：</strong>只制作小皇堡和巨无霸汉堡无法用光全部原料。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>tomatoSlices = 4, cheeseSlices = 17
<strong>输出：</strong>[]
<strong>解释：</strong>制作 1 个巨无霸汉堡会剩下 16 片奶酪，制作 2 个小皇堡会剩下 15 片奶酪。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>tomatoSlices = 0, cheeseSlices = 0
<strong>输出：</strong>[0,0]
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>tomatoSlices = 2, cheeseSlices = 1
<strong>输出：</strong>[0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= tomatoSlices &lt;= 10^7</code></li>
	<li><code>0 &lt;= cheeseSlices &lt;= 10^7</code></li>
</ul>


## 难度

Medium

## 标签

- 数学

## 提示

1. Can we have an answer if the number of tomatoes is odd ?
2. If we have answer will be there multiple answers or just one answer ?
3. Let us define number of jumbo burgers as X and number of small burgers as Y
We have to find an x and y in this equation
4. 1. 4X + 2Y = tomato
5. 2. X + Y = cheese

## 示例

```
16
7
17
4
4
17
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numOfBurgers(int tomatoSlices, int cheeseSlices, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> NumOfBurgers(int tomatoSlices, int cheeseSlices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} tomatoSlices
 * @param {number} cheeseSlices
 * @return {number[]}
 */
var numOfBurgers = function(tomatoSlices, cheeseSlices) {
    
};
```

### TypeScript

```typescript
function numOfBurgers(tomatoSlices: number, cheeseSlices: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $tomatoSlices
     * @param Integer $cheeseSlices
     * @return Integer[]
     */
    function numOfBurgers($tomatoSlices, $cheeseSlices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numOfBurgers(_ tomatoSlices: Int, _ cheeseSlices: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numOfBurgers(tomatoSlices: Int, cheeseSlices: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
    
  }
}
```

### Go

```golang
func numOfBurgers(tomatoSlices int, cheeseSlices int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} tomato_slices
# @param {Integer} cheese_slices
# @return {Integer[]}
def num_of_burgers(tomato_slices, cheese_slices)
    
end
```

### Scala

```scala
object Solution {
    def numOfBurgers(tomatoSlices: Int, cheeseSlices: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_of_burgers(tomato_slices: i32, cheese_slices: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (num-of-burgers tomatoSlices cheeseSlices)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec num_of_burgers(TomatoSlices :: integer(), CheeseSlices :: integer()) -> [integer()].
num_of_burgers(TomatoSlices, CheeseSlices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_of_burgers(tomato_slices :: integer, cheese_slices :: integer) :: [integer]
  def num_of_burgers(tomato_slices, cheese_slices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numOfBurgers(tomatoSlices: Int64, cheeseSlices: Int64): ArrayList<Int64> {

    }
}
```

