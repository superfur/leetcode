# LCR 186. 文物朝代判断

## 题目描述

<p>展览馆展出来自 13 个朝代的文物，每排展柜展出 5 个文物。某排文物的摆放情况记录于数组 <code>places</code>，其中 <code>places[i]</code> 表示处于第 <code>i</code> 位文物的所属朝代编号。其中，编号为 0 的朝代表示未知朝代。请判断并返回这排文物的所属朝代编号是否能够视为连续的五个朝代（如遇未知朝代可算作连续情况）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>places = [0, 6, 9, 0, 7]
<strong>输出：</strong>True
</pre>

<p>&nbsp;</p>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>places = [7, 8, 9, 10, 11]
<strong>输出：</strong>True
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>places.length = 5</code></li>
	<li><code>0 &lt;= places[i] &lt;= 13</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 数组
- 排序

## 示例

```
[0,6,9,0,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkDynasty(vector<int>& places) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkDynasty(int[] places) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkDynasty(self, places):
        """
        :type places: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        
```

### C

```c
bool checkDynasty(int* places, int placesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckDynasty(int[] places) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} places
 * @return {boolean}
 */
var checkDynasty = function(places) {
    
};
```

### TypeScript

```typescript
function checkDynasty(places: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $places
     * @return Boolean
     */
    function checkDynasty($places) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkDynasty(_ places: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkDynasty(places: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkDynasty(List<int> places) {
    
  }
}
```

### Go

```golang
func checkDynasty(places []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} places
# @return {Boolean}
def check_dynasty(places)
    
end
```

### Scala

```scala
object Solution {
    def checkDynasty(places: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_dynasty(places: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-dynasty places)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec check_dynasty(Places :: [integer()]) -> boolean().
check_dynasty(Places) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_dynasty(places :: [integer]) :: boolean
  def check_dynasty(places) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkDynasty(places: Array<Int64>): Bool {

    }
}
```

