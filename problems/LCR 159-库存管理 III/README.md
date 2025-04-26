# LCR 159. 库存管理 III

## 题目描述

<p>仓库管理员以数组 <code>stock</code> 形式记录商品库存表，其中 <code>stock[i]</code> 表示对应商品库存余量。请返回库存余量最少的 <code>cnt</code> 个商品余量，返回&nbsp;<strong>顺序不限</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>stock = [2,5,7,4], cnt = 1
<strong>输出：</strong>[2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>stock = [0,2,3,6], cnt = 2
<strong>输出：</strong>[0,2] 或 [2,0]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= cnt &lt;= stock.length &lt;= 10000<br />
	0 &lt;= stock[i] &lt;= 10000</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 数组
- 分治
- 快速选择
- 排序
- 堆（优先队列）

## 示例

```
[2,5,7,4]
1
[0,2,3,6]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> inventoryManagement(vector<int>& stock, int cnt) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] inventoryManagement(int[] stock, int cnt) {
        
    }
}
```

### Python

```python
class Solution(object):
    def inventoryManagement(self, stock, cnt):
        """
        :type stock: List[int]
        :type cnt: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* inventoryManagement(int* stock, int stockSize, int cnt, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] InventoryManagement(int[] stock, int cnt) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} stock
 * @param {number} cnt
 * @return {number[]}
 */
var inventoryManagement = function(stock, cnt) {
    
};
```

### TypeScript

```typescript
function inventoryManagement(stock: number[], cnt: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $stock
     * @param Integer $cnt
     * @return Integer[]
     */
    function inventoryManagement($stock, $cnt) {
        
    }
}
```

### Swift

```swift
class Solution {
    func inventoryManagement(_ stock: [Int], _ cnt: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun inventoryManagement(stock: IntArray, cnt: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> inventoryManagement(List<int> stock, int cnt) {
    
  }
}
```

### Go

```golang
func inventoryManagement(stock []int, cnt int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} stock
# @param {Integer} cnt
# @return {Integer[]}
def inventory_management(stock, cnt)
    
end
```

### Scala

```scala
object Solution {
    def inventoryManagement(stock: Array[Int], cnt: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn inventory_management(stock: Vec<i32>, cnt: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (inventory-management stock cnt)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec inventory_management(Stock :: [integer()], Cnt :: integer()) -> [integer()].
inventory_management(Stock, Cnt) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec inventory_management(stock :: [integer], cnt :: integer) :: [integer]
  def inventory_management(stock, cnt) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func inventoryManagement(stock: Array<Int64>, cnt: Int64): Array<Int64> {

    }
}
```

