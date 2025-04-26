# LCR 177. 撞色搭配

## 题目描述

<p>整数数组 <code>sockets</code> 记录了一个袜子礼盒的颜色分布情况，其中 <code>sockets[i]</code> 表示该袜子的颜色编号。礼盒中除了一款撞色搭配的袜子，每种颜色的袜子均有两只。请设计一个程序，在时间复杂度 O(n)，空间复杂度O(1) 内找到这双撞色搭配袜子的两个颜色编号。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>sockets = [4, 5, 2, 4, 6, 6]
<strong>输出：</strong>[2,5] 或 [5,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>sockets = [1, 2, 4, 1, 4, 3, 12, 3]
<strong>输出：</strong>[2,12] 或 [12,2]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= sockets.length &lt;= 10000</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组

## 示例

```
[4,5,2,4,6,6]
[1,2,4,1,4,3,12,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> sockCollocation(vector<int>& sockets) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] sockCollocation(int[] sockets) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sockCollocation(self, sockets):
        """
        :type sockets: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def sockCollocation(self, sockets: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sockCollocation(int* sockets, int socketsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SockCollocation(int[] sockets) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} sockets
 * @return {number[]}
 */
var sockCollocation = function(sockets) {
    
};
```

### TypeScript

```typescript
function sockCollocation(sockets: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $sockets
     * @return Integer[]
     */
    function sockCollocation($sockets) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sockCollocation(_ sockets: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sockCollocation(sockets: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> sockCollocation(List<int> sockets) {
    
  }
}
```

### Go

```golang
func sockCollocation(sockets []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} sockets
# @return {Integer[]}
def sock_collocation(sockets)
    
end
```

### Scala

```scala
object Solution {
    def sockCollocation(sockets: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sock_collocation(sockets: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (sock-collocation sockets)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec sock_collocation(Sockets :: [integer()]) -> [integer()].
sock_collocation(Sockets) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sock_collocation(sockets :: [integer]) :: [integer]
  def sock_collocation(sockets) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sockCollocation(sockets: Array<Int64>): Array<Int64> {

    }
}
```

