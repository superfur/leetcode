# 956. 最高的广告牌

## 题目描述

<p>你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，两边各一个。每个钢支架的高度必须相等。</p>

<p>你有一堆可以焊接在一起的钢筋 <code>rods</code>。举个例子，如果钢筋的长度为 <code>1</code>、<code>2</code> 和 <code>3</code>，则可以将它们焊接在一起形成长度为 <code>6</code>&nbsp;的支架。</p>

<p>返回 <em>广告牌的最大可能安装高度</em> 。如果没法安装广告牌，请返回 <code>0</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>[1,2,3,6]
<strong>输出：</strong>6
<strong>解释：</strong>我们有两个不相交的子集 {1,2,3} 和 {6}，它们具有相同的和 sum = 6。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>[1,2,3,4,5,6]
<strong>输出：</strong>10
<strong>解释：</strong>我们有两个不相交的子集 {2,3,5} 和 {4,6}，它们具有相同的和 sum = 10。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>[1,2]
<strong>输出：</strong>0
<strong>解释：</strong>没法安装广告牌，所以返回 0。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= rods.length &lt;= 20</code></li>
	<li><code>1 &lt;= rods[i] &lt;= 1000</code></li>
	<li><code>sum(rods[i]) &lt;= 5000</code></li>
</ol>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 示例

```
[1,2,3,6]
[1,2,3,4,5,6]
[1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int tallestBillboard(vector<int>& rods) {
        
    }
};
```

### Java

```java
class Solution {
    public int tallestBillboard(int[] rods) {
        
    }
}
```

### Python

```python
class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
```

### C

```c
int tallestBillboard(int* rods, int rodsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int TallestBillboard(int[] rods) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} rods
 * @return {number}
 */
var tallestBillboard = function(rods) {
    
};
```

### TypeScript

```typescript
function tallestBillboard(rods: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $rods
     * @return Integer
     */
    function tallestBillboard($rods) {
        
    }
}
```

### Swift

```swift
class Solution {
    func tallestBillboard(_ rods: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun tallestBillboard(rods: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int tallestBillboard(List<int> rods) {
    
  }
}
```

### Go

```golang
func tallestBillboard(rods []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} rods
# @return {Integer}
def tallest_billboard(rods)
    
end
```

### Scala

```scala
object Solution {
    def tallestBillboard(rods: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn tallest_billboard(rods: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (tallest-billboard rods)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec tallest_billboard(Rods :: [integer()]) -> integer().
tallest_billboard(Rods) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec tallest_billboard(rods :: [integer]) :: integer
  def tallest_billboard(rods) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func tallestBillboard(rods: Array<Int64>): Int64 {

    }
}
```

