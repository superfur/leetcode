# 2682. 找出转圈游戏输家

## 题目描述

<p><code>n</code> 个朋友在玩游戏。这些朋友坐成一个圈，按 <strong>顺时针方向</strong> 从 <code>1</code> 到 <code>n</code> 编号。准确的说，从第 <code>i</code> 个朋友的位置开始顺时针移动 <code>1</code> 步会到达第 <code>(i + 1)</code> 个朋友的位置（<code>1 &lt;= i &lt; n</code>），而从第 <code>n</code> 个朋友的位置开始顺时针移动 <code>1</code> 步会回到第 <code>1</code> 个朋友的位置。</p>

<p>游戏规则如下：</p>

<p>第 <code>1</code> 个朋友接球。</p>

<ul>
	<li>接着，第 <code>1</code> 个朋友将球传给距离他顺时针方向 <code>k</code> 步的朋友。</li>
	<li>然后，接球的朋友应该把球传给距离他顺时针方向 <code>2 * k</code> 步的朋友。</li>
	<li>接着，接球的朋友应该把球传给距离他顺时针方向 <code>3 * k</code> 步的朋友，以此类推。</li>
</ul>

<p>换句话说，在第 <code>i</code> 轮中持有球的那位朋友需要将球传递给距离他顺时针方向 <code>i * k</code> 步的朋友。</p>

<p>当某个朋友第 2 次接到球时，游戏结束。</p>

<p>在整场游戏中没有接到过球的朋友是 <strong>输家</strong> 。</p>

<p>给你参与游戏的朋友数量 <code>n</code> 和一个整数 <code>k</code> ，请按升序排列返回包含所有输家编号的数组 <code>answer</code> 作为答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 5, k = 2
<strong>输出：</strong>[4,5]
<strong>解释：</strong>以下为游戏进行情况：
1）第 1 个朋友接球，第 1 个朋友将球传给距离他顺时针方向 2 步的玩家 —— 第 3 个朋友。
2）第 3 个朋友将球传给距离他顺时针方向 4 步的玩家 —— 第 2 个朋友。
3）第 2 个朋友将球传给距离他顺时针方向 6 步的玩家 —— 第 3 个朋友。
4）第 3 个朋友接到两次球，游戏结束。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 4, k = 4
<strong>输出：</strong>[2,3,4]
<strong>解释：</strong>以下为游戏进行情况：
1）第 1 个朋友接球，第 1 个朋友将球传给距离他顺时针方向 4 步的玩家 —— 第 1 个朋友。
2）第 1 个朋友接到两次球，游戏结束。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= n &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 模拟

## 提示

1. Simulate the whole game until a player receives the ball for the second time.

## 示例

```
5
2
4
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> circularGameLosers(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] circularGameLosers(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def circularGameLosers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* circularGameLosers(int n, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] CircularGameLosers(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var circularGameLosers = function(n, k) {
    
};
```

### TypeScript

```typescript
function circularGameLosers(n: number, k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer[]
     */
    function circularGameLosers($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func circularGameLosers(_ n: Int, _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun circularGameLosers(n: Int, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> circularGameLosers(int n, int k) {
    
  }
}
```

### Go

```golang
func circularGameLosers(n int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def circular_game_losers(n, k)
    
end
```

### Scala

```scala
object Solution {
    def circularGameLosers(n: Int, k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn circular_game_losers(n: i32, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (circular-game-losers n k)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec circular_game_losers(N :: integer(), K :: integer()) -> [integer()].
circular_game_losers(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec circular_game_losers(n :: integer, k :: integer) :: [integer]
  def circular_game_losers(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func circularGameLosers(n: Int64, k: Int64): Array<Int64> {

    }
}
```

