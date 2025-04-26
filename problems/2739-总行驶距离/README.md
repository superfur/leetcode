# 2739. 总行驶距离

## 题目描述

<p>卡车有两个油箱。给你两个整数，<code>mainTank</code> 表示主油箱中的燃料（以升为单位），<code>additionalTank</code> 表示副油箱中的燃料（以升为单位）。</p>

<p>该卡车每耗费 <code>1</code> 升燃料都可以行驶 <code>10</code> km。每当主油箱使用了 <code>5</code> 升燃料时，如果副油箱至少有 <code>1</code> 升燃料，则会将 <code>1</code> 升燃料从副油箱转移到主油箱。</p>

<p>返回卡车可以行驶的最大距离。</p>

<p>注意：从副油箱向主油箱注入燃料不是连续行为。这一事件会在每消耗 <code>5</code> 升燃料时突然且立即发生。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>mainTank = 5, additionalTank = 10
<strong>输出：</strong>60
<strong>解释：</strong>
在用掉 5 升燃料后，主油箱中燃料还剩下 (5 - 5 + 1) = 1 升，行驶距离为 50km 。
在用掉剩下的 1 升燃料后，没有新的燃料注入到主油箱中，主油箱变为空。
总行驶距离为 60km 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>mainTank = 1, additionalTank = 2
<strong>输出：</strong>10
<strong>解释：</strong>
在用掉 1 升燃料后，主油箱变为空。
总行驶距离为 10km 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= mainTank, additionalTank &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 模拟

## 提示

1. Avoid calculations in decimal to prevent precision errors.

## 示例

```
5
10
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int distanceTraveled(int mainTank, int additionalTank) {
        
    }
};
```

### Java

```java
class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        
    }
}
```

### Python

```python
class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        
```

### C

```c
int distanceTraveled(int mainTank, int additionalTank) {
    
}
```

### C#

```csharp
public class Solution {
    public int DistanceTraveled(int mainTank, int additionalTank) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} mainTank
 * @param {number} additionalTank
 * @return {number}
 */
var distanceTraveled = function(mainTank, additionalTank) {
    
};
```

### TypeScript

```typescript
function distanceTraveled(mainTank: number, additionalTank: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $mainTank
     * @param Integer $additionalTank
     * @return Integer
     */
    function distanceTraveled($mainTank, $additionalTank) {
        
    }
}
```

### Swift

```swift
class Solution {
    func distanceTraveled(_ mainTank: Int, _ additionalTank: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun distanceTraveled(mainTank: Int, additionalTank: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int distanceTraveled(int mainTank, int additionalTank) {
    
  }
}
```

### Go

```golang
func distanceTraveled(mainTank int, additionalTank int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} main_tank
# @param {Integer} additional_tank
# @return {Integer}
def distance_traveled(main_tank, additional_tank)
    
end
```

### Scala

```scala
object Solution {
    def distanceTraveled(mainTank: Int, additionalTank: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn distance_traveled(main_tank: i32, additional_tank: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (distance-traveled mainTank additionalTank)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec distance_traveled(MainTank :: integer(), AdditionalTank :: integer()) -> integer().
distance_traveled(MainTank, AdditionalTank) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec distance_traveled(main_tank :: integer, additional_tank :: integer) :: integer
  def distance_traveled(main_tank, additional_tank) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func distanceTraveled(mainTank: Int64, additionalTank: Int64): Int64 {

    }
}
```

