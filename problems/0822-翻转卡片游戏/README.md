# 822. 翻转卡片游戏

## 题目描述

<p>在桌子上有 <code>n</code> 张卡片，每张卡片的正面和背面都写着一个正数（正面与背面上的数有可能不一样）。</p>

<p>我们可以先翻转任意张卡片，然后选择其中一张卡片。</p>

<p>如果选中的那张卡片背面的数字 <code>x</code> 与任意一张卡片的正面的数字都不同，那么这个数字是我们想要的数字。</p>

<p>哪个数是这些想要的数字中最小的数（找到这些数中的最小值）呢？如果没有一个数字符合要求的，输出 <code>0</code> 。</p>

<p>其中, <code>fronts[i]</code>&nbsp;和&nbsp;<code>backs[i]</code>&nbsp;分别代表第&nbsp;<code>i</code>&nbsp;张卡片的正面和背面的数字。</p>

<p>如果我们通过翻转卡片来交换正面与背面上的数，那么当初在正面的数就变成背面的数，背面的数就变成正面的数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
<strong>输出：</strong><code>2</code>
<strong>解释：</strong>假设我们翻转第二张卡片，那么在正面的数变成了 <code>[1,3,4,4,7]</code> ， 背面的数变成了 <code>[1,2,4,1,3]。</code>
接着我们选择第二张卡片，因为现在该卡片的背面的数是 2，2 与任意卡片上正面的数都不同，所以 2 就是我们想要的数字。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>fronts = [1], backs = [1]
<strong>输出：</strong>0
<strong>解释：</strong>
无论如何翻转都无法得到想要的数字，所以返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == fronts.length == backs.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= fronts[i], backs[i] &lt;= 2000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表

## 示例

```
[1,2,4,4,7]
[1,3,4,1,3]
[1]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int flipgame(vector<int>& fronts, vector<int>& backs) {
        
    }
};
```

### Java

```java
class Solution {
    public int flipgame(int[] fronts, int[] backs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
```

### C

```c
int flipgame(int* fronts, int frontsSize, int* backs, int backsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int Flipgame(int[] fronts, int[] backs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} fronts
 * @param {number[]} backs
 * @return {number}
 */
var flipgame = function(fronts, backs) {
    
};
```

### TypeScript

```typescript
function flipgame(fronts: number[], backs: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $fronts
     * @param Integer[] $backs
     * @return Integer
     */
    function flipgame($fronts, $backs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func flipgame(_ fronts: [Int], _ backs: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun flipgame(fronts: IntArray, backs: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int flipgame(List<int> fronts, List<int> backs) {
    
  }
}
```

### Go

```golang
func flipgame(fronts []int, backs []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} fronts
# @param {Integer[]} backs
# @return {Integer}
def flipgame(fronts, backs)
    
end
```

### Scala

```scala
object Solution {
    def flipgame(fronts: Array[Int], backs: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn flipgame(fronts: Vec<i32>, backs: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (flipgame fronts backs)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec flipgame(Fronts :: [integer()], Backs :: [integer()]) -> integer().
flipgame(Fronts, Backs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec flipgame(fronts :: [integer], backs :: [integer]) :: integer
  def flipgame(fronts, backs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func flipgame(fronts: Array<Int64>, backs: Array<Int64>): Int64 {

    }
}
```

