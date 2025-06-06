# 605. 种花问题

## 题目描述

<p>假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。</p>

<p>给你一个整数数组&nbsp;<code>flowerbed</code> 表示花坛，由若干 <code>0</code> 和 <code>1</code> 组成，其中 <code>0</code> 表示没种植花，<code>1</code> 表示种植了花。另有一个数&nbsp;<code>n</code><strong> </strong>，能否在不打破种植规则的情况下种入&nbsp;<code>n</code><strong>&nbsp;</strong>朵花？能则返回 <code>true</code> ，不能则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>flowerbed = [1,0,0,0,1], n = 1
<strong>输出：</strong>true
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>flowerbed = [1,0,0,0,1], n = 2
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= flowerbed.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>flowerbed[i]</code> 为 <code>0</code> 或 <code>1</code></li>
	<li><code>flowerbed</code> 中不存在相邻的两朵花</li>
	<li><code>0 &lt;= n &lt;= flowerbed.length</code></li>
</ul>

## 难度

Easy

## 标签

- 贪心
- 数组

## 示例

```
[1,0,0,0,1]
1
[1,0,0,0,1]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
```

### C

```c
bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanPlaceFlowers(int[] flowerbed, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    
};
```

### TypeScript

```typescript
function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $flowerbed
     * @param Integer $n
     * @return Boolean
     */
    function canPlaceFlowers($flowerbed, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canPlaceFlowers(_ flowerbed: [Int], _ n: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canPlaceFlowers(List<int> flowerbed, int n) {
    
  }
}
```

### Go

```golang
func canPlaceFlowers(flowerbed []int, n int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} flowerbed
# @param {Integer} n
# @return {Boolean}
def can_place_flowers(flowerbed, n)
    
end
```

### Scala

```scala
object Solution {
    def canPlaceFlowers(flowerbed: Array[Int], n: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-place-flowers flowerbed n)
  (-> (listof exact-integer?) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_place_flowers(Flowerbed :: [integer()], N :: integer()) -> boolean().
can_place_flowers(Flowerbed, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_place_flowers(flowerbed :: [integer], n :: integer) :: boolean
  def can_place_flowers(flowerbed, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canPlaceFlowers(flowerbed: Array<Int64>, n: Int64): Bool {

    }
}
```

