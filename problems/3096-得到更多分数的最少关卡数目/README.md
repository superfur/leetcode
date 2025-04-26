# 3096. 得到更多分数的最少关卡数目

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的二进制数组&nbsp;<code>possible</code>&nbsp;。</p>

<p>Alice 和 Bob 正在玩一个有 <code>n</code> 个关卡的游戏，游戏中有一些关卡是 <strong>困难</strong>&nbsp;模式，其他的关卡是 <strong>简单</strong>&nbsp;模式。如果&nbsp;<code>possible[i] == 0</code>&nbsp;，那么第&nbsp;<code>i</code> 个关卡是 <strong>困难</strong>&nbsp;模式，两个玩家&nbsp;<strong>都不可能</strong> 通过。一个玩家通过一个简单模式的关卡可以获得 <code>1</code>&nbsp;分，遇到困难模式的关卡将失去 <code>1</code>&nbsp;分。</p>

<p>游戏的一开始，Alice 将从第 <code>0</code>&nbsp;级开始 <strong>按顺序</strong> 完成一些关卡，然后 Bob 会完成剩下的所有关卡。</p>

<p>假设两名玩家都采取最优策略，目的是&nbsp;<strong>最大化</strong>&nbsp;自己的得分，Alice 想知道自己&nbsp;<strong>最少</strong> 需要完成多少个关卡，才能获得比 Bob 更多的分数。</p>

<p>请你返回 Alice 获得比 Bob 更多的分数所需要完成的 <strong>最少</strong> 关卡数目，如果 <strong>无法</strong>&nbsp;达成，那么返回 <code>-1</code>&nbsp;。</p>

<p><strong>注意</strong>，每个玩家都至少需要完成&nbsp;<code>1</code> 个关卡。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>possible = [1,0,1,0]</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><strong>解释：</strong></p>

<p>我们来看一下 Alice 可以完成的关卡数目：</p>

<ul>
	<li>如果 Alice 只完成关卡 0 ，Bob 完成剩下的所有关卡，那么 Alice 获得 1 分，Bob 获得 -1 + 1 - 1 = -1 分。</li>
	<li>如果 Alice 完成到关卡 1 ，Bob 完成剩下的所有关卡，那么 Alice 获得&nbsp;1 - 1 = 0 分，Bob 获得 1 - 1 = 0 分。</li>
	<li>如果 Alice 完成到关卡 2 ，Bob 完成剩下的所有关卡，那么 Alice 获得&nbsp;1 - 1 + 1 = 1 分，Bob 获得 -1 分。</li>
</ul>

<p>Alice 需要完成至少一个关卡获得更多的分数。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>possible = [1,1,1,1,1]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p>我们来看一下 Alice 可以完成的关卡数目：</p>

<ul>
	<li>如果 Alice 只完成关卡 0 ，Bob 完成剩下的所有关卡，那么 Alice 获得 1 分，Bob 获得 4 分。</li>
	<li>如果 Alice 完成到关卡 1 ，Bob 完成剩下的所有关卡，那么 Alice 获得&nbsp;2 分，Bob 获得 3 分。</li>
	<li>如果 Alice 完成到关卡 2 ，Bob 完成剩下的所有关卡，那么 Alice 获得&nbsp;3 分，Bob 获得 2&nbsp;分。</li>
	<li>如果 Alice 完成到关卡 3&nbsp;，Bob 完成剩下的所有关卡，那么 Alice 获得 4&nbsp;分，Bob 获得 1&nbsp;分。</li>
</ul>

<p>Alice 需要完成至少三个关卡获得更多的分数。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>possible = [0,0]</span></p>

<p><span class="example-io"><b>输出：</b>-1</span></p>

<p><strong>解释：</strong></p>

<p>两名玩家只能各完成 1 个关卡，Alice 完成关卡 0 得到 -1 分，Bob 完成关卡 1 得到 -1 分。两名玩家得分相同，所以 Alice 无法得到更多分数。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n == possible.length &lt;= 10<sup>5</sup></code></li>
	<li><code>possible[i]</code>&nbsp;要么是&nbsp;<code>0</code>&nbsp;要么是&nbsp;<code>1</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 前缀和

## 提示

1. Change all <code>0</code> in possible array into <code>-1</code>.
2. We need to find the shortest non-empty prefix of the new possible array such that the sum of elements in it is strictly larger than the remaining part.

## 示例

```
[1,0,1,0]
[1,1,1,1,1]
[0,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumLevels(vector<int>& possible) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumLevels(int[] possible) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumLevels(self, possible):
        """
        :type possible: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        
```

### C

```c
int minimumLevels(int* possible, int possibleSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumLevels(int[] possible) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} possible
 * @return {number}
 */
var minimumLevels = function(possible) {
    
};
```

### TypeScript

```typescript
function minimumLevels(possible: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $possible
     * @return Integer
     */
    function minimumLevels($possible) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumLevels(_ possible: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumLevels(possible: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumLevels(List<int> possible) {
    
  }
}
```

### Go

```golang
func minimumLevels(possible []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} possible
# @return {Integer}
def minimum_levels(possible)
    
end
```

### Scala

```scala
object Solution {
    def minimumLevels(possible: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_levels(possible: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-levels possible)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_levels(Possible :: [integer()]) -> integer().
minimum_levels(Possible) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_levels(possible :: [integer]) :: integer
  def minimum_levels(possible) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumLevels(possible: Array<Int64>): Int64 {

    }
}
```

