# 2335. 装满杯子需要的最短总时长

## 题目描述

<p>现有一台饮水机，可以制备冷水、温水和热水。每秒钟，可以装满 <code>2</code> 杯 <strong>不同</strong> 类型的水或者 <code>1</code> 杯任意类型的水。</p>

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>3</code> 的整数数组 <code>amount</code> ，其中 <code>amount[0]</code>、<code>amount[1]</code> 和 <code>amount[2]</code> 分别表示需要装满冷水、温水和热水的杯子数量。返回装满所有杯子所需的 <strong>最少</strong> 秒数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>amount = [1,4,2]
<strong>输出：</strong>4
<strong>解释：</strong>下面给出一种方案：
第 1 秒：装满一杯冷水和一杯温水。
第 2 秒：装满一杯温水和一杯热水。
第 3 秒：装满一杯温水和一杯热水。
第 4 秒：装满一杯温水。
可以证明最少需要 4 秒才能装满所有杯子。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>amount = [5,4,4]
<strong>输出：</strong>7
<strong>解释：</strong>下面给出一种方案：
第 1 秒：装满一杯冷水和一杯热水。
第 2 秒：装满一杯冷水和一杯温水。
第 3 秒：装满一杯冷水和一杯温水。
第 4 秒：装满一杯温水和一杯热水。
第 5 秒：装满一杯冷水和一杯热水。
第 6 秒：装满一杯冷水和一杯温水。
第 7 秒：装满一杯热水。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>amount = [5,0,0]
<strong>输出：</strong>5
<strong>解释：</strong>每秒装满一杯冷水。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>amount.length == 3</code></li>
	<li><code>0 &lt;= amount[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 排序
- 堆（优先队列）

## 提示

1. To minimize the amount of time needed, you want to fill up as many cups as possible in each second. This means that you want to maximize the number of seconds where you are filling up two cups.
2. You always want to fill up the two types of water with the most unfilled cups.

## 示例

```
[1,4,2]
[5,4,4]
[5,0,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int fillCups(vector<int>& amount) {
        
    }
};
```

### Java

```java
class Solution {
    public int fillCups(int[] amount) {
        
    }
}
```

### Python

```python
class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
```

### C

```c
int fillCups(int* amount, int amountSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FillCups(int[] amount) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} amount
 * @return {number}
 */
var fillCups = function(amount) {
    
};
```

### TypeScript

```typescript
function fillCups(amount: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $amount
     * @return Integer
     */
    function fillCups($amount) {
        
    }
}
```

### Swift

```swift
class Solution {
    func fillCups(_ amount: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun fillCups(amount: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int fillCups(List<int> amount) {
    
  }
}
```

### Go

```golang
func fillCups(amount []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} amount
# @return {Integer}
def fill_cups(amount)
    
end
```

### Scala

```scala
object Solution {
    def fillCups(amount: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn fill_cups(amount: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (fill-cups amount)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec fill_cups(Amount :: [integer()]) -> integer().
fill_cups(Amount) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec fill_cups(amount :: [integer]) :: integer
  def fill_cups(amount) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func fillCups(amount: Array<Int64>): Int64 {

    }
}
```

