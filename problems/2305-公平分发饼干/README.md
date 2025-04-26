# 2305. 公平分发饼干

## 题目描述

<p>给你一个整数数组 <code>cookies</code> ，其中 <code>cookies[i]</code> 表示在第 <code>i</code> 个零食包中的饼干数量。另给你一个整数 <code>k</code> 表示等待分发零食包的孩子数量，<strong>所有</strong> 零食包都需要分发。在同一个零食包中的所有饼干都必须分发给同一个孩子，不能分开。</p>

<p>分发的 <strong>不公平程度</strong> 定义为单个孩子在分发过程中能够获得饼干的最大总数。</p>

<p>返回所有分发的最小不公平程度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>cookies = [8,15,10,20,8], k = 2
<strong>输出：</strong>31
<strong>解释：</strong>一种最优方案是 [8,15,8] 和 [10,20] 。
- 第 1 个孩子分到 [8,15,8] ，总计 8 + 15 + 8 = 31 块饼干。
- 第 2 个孩子分到 [10,20] ，总计 10 + 20 = 30 块饼干。
分发的不公平程度为 max(31,30) = 31 。
可以证明不存在不公平程度小于 31 的分发方案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>cookies = [6,1,3,2,2,4,1,2], k = 3
<strong>输出：</strong>7
<strong>解释：</strong>一种最优方案是 [6,1]、[3,2,2] 和 [4,1,2] 。
- 第 1 个孩子分到 [6,1] ，总计 6 + 1 = 7 块饼干。 
- 第 2 个孩子分到 [3,2,2] ，总计 3 + 2 + 2 = 7 块饼干。
- 第 3 个孩子分到 [4,1,2] ，总计 4 + 1 + 2 = 7 块饼干。
分发的不公平程度为 max(7,7,7) = 7 。
可以证明不存在不公平程度小于 7 的分发方案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= cookies.length &lt;= 8</code></li>
	<li><code>1 &lt;= cookies[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= k &lt;= cookies.length</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 动态规划
- 回溯
- 状态压缩

## 提示

1. We have to give each bag to one of the children. How can we enumerate all of the possibilities?
2. Use recursion and keep track of the current number of cookies each child has. Once all the bags have been distributed, find the child with the most cookies.

## 示例

```
[8,15,10,20,8]
2
[6,1,3,2,2,4,1,2]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int distributeCookies(vector<int>& cookies, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int distributeCookies(int[] cookies, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
```

### C

```c
int distributeCookies(int* cookies, int cookiesSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int DistributeCookies(int[] cookies, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} cookies
 * @param {number} k
 * @return {number}
 */
var distributeCookies = function(cookies, k) {
    
};
```

### TypeScript

```typescript
function distributeCookies(cookies: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $cookies
     * @param Integer $k
     * @return Integer
     */
    function distributeCookies($cookies, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func distributeCookies(_ cookies: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun distributeCookies(cookies: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int distributeCookies(List<int> cookies, int k) {
    
  }
}
```

### Go

```golang
func distributeCookies(cookies []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} cookies
# @param {Integer} k
# @return {Integer}
def distribute_cookies(cookies, k)
    
end
```

### Scala

```scala
object Solution {
    def distributeCookies(cookies: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn distribute_cookies(cookies: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (distribute-cookies cookies k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec distribute_cookies(Cookies :: [integer()], K :: integer()) -> integer().
distribute_cookies(Cookies, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec distribute_cookies(cookies :: [integer], k :: integer) :: integer
  def distribute_cookies(cookies, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func distributeCookies(cookies: Array<Int64>, k: Int64): Int64 {

    }
}
```

