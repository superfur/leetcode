# 825. 适龄的朋友

## 题目描述

<p>在社交媒体网站上有 <code>n</code> 个用户。给你一个整数数组 <code>ages</code> ，其中 <code>ages[i]</code> 是第 <code>i</code> 个用户的年龄。</p>

<p>如果下述任意一个条件为真，那么用户 <code>x</code> 将不会向用户 <code>y</code>（<code>x != y</code>）发送好友请求：</p>

<ul>
	<li><code>ages[y] &lt;= 0.5 * ages[x] + 7</code></li>
	<li><code>ages[y] &gt; ages[x]</code></li>
	<li><code>ages[y] &gt; 100 &amp;&amp; ages[x] &lt; 100</code></li>
</ul>

<p>否则，<code>x</code> 将会向 <code>y</code> 发送一条好友请求。</p>

<p>注意，如果 <code>x</code> 向 <code>y</code> 发送一条好友请求，<code>y</code> 不必也向 <code>x</code> 发送一条好友请求。另外，用户不会向自己发送好友请求。</p>

<p>返回在该社交媒体网站上产生的好友请求总数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>ages = [16,16]
<strong>输出：</strong>2
<strong>解释：</strong>2 人互发好友请求。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>ages = [16,17,18]
<strong>输出：</strong>2
<strong>解释：</strong>产生的好友请求为 17 -&gt; 16 ，18 -&gt; 17 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>ages = [20,30,100,110,120]
<strong>输出：</strong>3
<strong>解释：</strong>产生的好友请求为 110 -&gt; 100 ，120 -&gt; 110 ，120 -&gt; 100 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == ages.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= ages[i] &lt;= 120</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 二分查找
- 排序

## 示例

```
[16,16]
[16,17,18]
[20,30,100,110,120]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numFriendRequests(vector<int>& ages) {
        
    }
};
```

### Java

```java
class Solution {
    public int numFriendRequests(int[] ages) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        
```

### C

```c
int numFriendRequests(int* ages, int agesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumFriendRequests(int[] ages) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} ages
 * @return {number}
 */
var numFriendRequests = function(ages) {
    
};
```

### TypeScript

```typescript
function numFriendRequests(ages: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $ages
     * @return Integer
     */
    function numFriendRequests($ages) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numFriendRequests(_ ages: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numFriendRequests(ages: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numFriendRequests(List<int> ages) {
    
  }
}
```

### Go

```golang
func numFriendRequests(ages []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} ages
# @return {Integer}
def num_friend_requests(ages)
    
end
```

### Scala

```scala
object Solution {
    def numFriendRequests(ages: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_friend_requests(ages: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-friend-requests ages)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_friend_requests(Ages :: [integer()]) -> integer().
num_friend_requests(Ages) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_friend_requests(ages :: [integer]) :: integer
  def num_friend_requests(ages) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numFriendRequests(ages: Array<Int64>): Int64 {

    }
}
```

