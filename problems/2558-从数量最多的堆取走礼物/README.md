# 2558. 从数量最多的堆取走礼物

## 题目描述

<p>给你一个整数数组 <code>gifts</code> ，表示各堆礼物的数量。每一秒，你需要执行以下操作：</p>

<ul>
	<li>选择礼物数量最多的那一堆。</li>
	<li>如果不止一堆都符合礼物数量最多，从中选择任一堆即可。</li>
	<li>将堆中的礼物数量减少到堆中原来礼物数量的平方根，向下取整。</li>
</ul>

<p>返回在 <code>k</code> 秒后剩下的礼物数量<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>gifts = [25,64,9,4,100], k = 4
<strong>输出：</strong>29
<strong>解释：</strong> 
按下述方式取走礼物：
- 在第一秒，选中最后一堆，剩下 10 个礼物。
- 接着第二秒选中第二堆礼物，剩下 8 个礼物。
- 然后选中第一堆礼物，剩下 5 个礼物。
- 最后，再次选中最后一堆礼物，剩下 3 个礼物。
最后剩下的礼物数量分别是 [5,8,9,4,3] ，所以，剩下礼物的总数量是 29 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>gifts = [1,1,1,1], k = 4
<strong>输出：</strong>4
<strong>解释：</strong>
在本例中，不管选中哪一堆礼物，都必须剩下 1 个礼物。 
也就是说，你无法获取任一堆中的礼物。 
所以，剩下礼物的总数量是 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= gifts.length &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= gifts[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>3</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 模拟
- 堆（优先队列）

## 提示

1. How can you keep track of the largest gifts in the array
2. What is an efficient way to find the square root of a number?
3. Can you keep adding up the values of the gifts while ensuring they are in a certain order?
4. Can we use a priority queue or heap here?

## 示例

```
[25,64,9,4,100]
4
[1,1,1,1]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long pickGifts(int[] gifts, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
```

### C

```c
long long pickGifts(int* gifts, int giftsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long PickGifts(int[] gifts, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} gifts
 * @param {number} k
 * @return {number}
 */
var pickGifts = function(gifts, k) {
    
};
```

### TypeScript

```typescript
function pickGifts(gifts: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $gifts
     * @param Integer $k
     * @return Integer
     */
    function pickGifts($gifts, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func pickGifts(_ gifts: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun pickGifts(gifts: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int pickGifts(List<int> gifts, int k) {
    
  }
}
```

### Go

```golang
func pickGifts(gifts []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} gifts
# @param {Integer} k
# @return {Integer}
def pick_gifts(gifts, k)
    
end
```

### Scala

```scala
object Solution {
    def pickGifts(gifts: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn pick_gifts(gifts: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (pick-gifts gifts k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec pick_gifts(Gifts :: [integer()], K :: integer()) -> integer().
pick_gifts(Gifts, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec pick_gifts(gifts :: [integer], k :: integer) :: integer
  def pick_gifts(gifts, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func pickGifts(gifts: Array<Int64>, k: Int64): Int64 {

    }
}
```

