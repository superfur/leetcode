# 335. 路径交叉

## 题目描述

<p>给你一个整数数组 <code>distance</code><em> </em>。</p>

<p>从 <strong>X-Y</strong> 平面上的点&nbsp;<code>(0,0)</code>&nbsp;开始，先向北移动 <code>distance[0]</code> 米，然后向西移动 <code>distance[1]</code> 米，向南移动 <code>distance[2]</code> 米，向东移动 <code>distance[3]</code> 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。</p>

<p>判断你所经过的路径是否相交。如果相交，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/selfcross1-plane.jpg" style="width: 400px; height: 435px;" />
<pre>
<strong>输入：</strong>distance = [2,1,1,2]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/selfcross2-plane.jpg" style="width: 400px; height: 435px;" />
<pre>
<strong>输入：</strong>distance = [1,2,3,4]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/selfcross3-plane.jpg" style="width: 400px; height: 435px;" />
<pre>
<strong>输入：</strong>distance = [1,1,1,1]
<strong>输出：</strong>true</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;distance.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;=&nbsp;distance[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 几何
- 数组
- 数学

## 示例

```
[2,1,1,2]
[1,2,3,4]
[1,1,1,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isSelfCrossing(vector<int>& distance) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isSelfCrossing(int[] distance) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        
```

### C

```c
bool isSelfCrossing(int* distance, int distanceSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsSelfCrossing(int[] distance) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} distance
 * @return {boolean}
 */
var isSelfCrossing = function(distance) {
    
};
```

### TypeScript

```typescript
function isSelfCrossing(distance: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $distance
     * @return Boolean
     */
    function isSelfCrossing($distance) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isSelfCrossing(_ distance: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isSelfCrossing(distance: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isSelfCrossing(List<int> distance) {
    
  }
}
```

### Go

```golang
func isSelfCrossing(distance []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} distance
# @return {Boolean}
def is_self_crossing(distance)
    
end
```

### Scala

```scala
object Solution {
    def isSelfCrossing(distance: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_self_crossing(distance: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-self-crossing distance)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec is_self_crossing(Distance :: [integer()]) -> boolean().
is_self_crossing(Distance) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_self_crossing(distance :: [integer]) :: boolean
  def is_self_crossing(distance) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isSelfCrossing(distance: Array<Int64>): Bool {

    }
}
```

