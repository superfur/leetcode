# 1535. 找出数组游戏的赢家

## 题目描述

<p>给你一个由 <strong>不同</strong> 整数组成的整数数组 <code>arr</code> 和一个整数 <code>k</code> 。</p>

<p>每回合游戏都在数组的前两个元素（即 <code>arr[0]</code> 和 <code>arr[1]</code> ）之间进行。比较 <code>arr[0]</code> 与 <code>arr[1]</code> 的大小，较大的整数将会取得这一回合的胜利并保留在位置 <code>0</code> ，较小的整数移至数组的末尾。当一个整数赢得 <code>k</code> 个连续回合时，游戏结束，该整数就是比赛的 <strong>赢家</strong> 。</p>

<p>返回赢得比赛的整数。</p>

<p>题目数据 <strong>保证</strong> 游戏存在赢家。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [2,1,3,5,4,6,7], k = 2
<strong>输出：</strong>5
<strong>解释：</strong>一起看一下本场游戏每回合的情况：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/30/q-example.png" style="height: 90px; width: 400px;">
因此将进行 4 回合比赛，其中 5 是赢家，因为它连胜 2 回合。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [3,2,1], k = 10
<strong>输出：</strong>3
<strong>解释：</strong>3 将会在前 10 个回合中连续获胜。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [1,9,8,2,3,7,6,4,5], k = 7
<strong>输出：</strong>9
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
<strong>输出：</strong>99
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10^6</code></li>
	<li><code>arr</code> 所含的整数 <strong>各不相同</strong> 。</li>
	<li><code>1 &lt;= k &lt;= 10^9</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 模拟

## 提示

1. If k ≥ arr.length return the max element of the array.
2. If k < arr.length simulate the game until a number wins k consecutive games.

## 示例

```
[2,1,3,5,4,6,7]
2
[3,2,1]
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int getWinner(int[] arr, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
```

### C

```c
int getWinner(int* arr, int arrSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetWinner(int[] arr, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var getWinner = function(arr, k) {
    
};
```

### TypeScript

```typescript
function getWinner(arr: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function getWinner($arr, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getWinner(_ arr: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getWinner(arr: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getWinner(List<int> arr, int k) {
    
  }
}
```

### Go

```golang
func getWinner(arr []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def get_winner(arr, k)
    
end
```

### Scala

```scala
object Solution {
    def getWinner(arr: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_winner(arr: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-winner arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec get_winner(Arr :: [integer()], K :: integer()) -> integer().
get_winner(Arr, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_winner(arr :: [integer], k :: integer) :: integer
  def get_winner(arr, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getWinner(arr: Array<Int64>, k: Int64): Int64 {

    }
}
```

