# LCR 128. 库存管理 I

## 题目描述

<p>仓库管理员以数组 <code>stock</code> 形式记录商品库存表。<code>stock[i]</code> 表示商品 <code>id</code>，可能存在重复。原库存表按商品 <code>id</code> 升序排列。现因突发情况需要进行商品紧急调拨，管理员将这批商品 <code>id</code> 提前依次整理至库存表最后。请你找到并返回库存表中编号的 <strong>最小的元素</strong> 以便及时记录本次调拨。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>stock =<strong> </strong>[4,5,8,3,4]
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>stock = [5,7,9,1,2]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p>提示：</p>

<ul>
	<li>1 &lt;= stock.length &lt;= 5000</li>
	<li>-5000 &lt;= stock[i] &lt;= 5000</li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 154 题相同：<a href="https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/">https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/</a></p>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 数组
- 二分查找

## 示例

```
[4,5,8,3,4]
[5,7,9,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int inventoryManagement(vector<int>& stock) {
        
    }
};
```

### Java

```java
class Solution {
    public int inventoryManagement(int[] stock) {
        
    }
}
```

### Python

```python
class Solution(object):
    def inventoryManagement(self, stock):
        """
        :type stock: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        
```

### C

```c
int inventoryManagement(int* stock, int stockSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int InventoryManagement(int[] stock) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} stock
 * @return {number}
 */
var inventoryManagement = function(stock) {
    
};
```

### TypeScript

```typescript
function inventoryManagement(stock: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $stock
     * @return Integer
     */
    function inventoryManagement($stock) {
        
    }
}
```

### Swift

```swift
class Solution {
    func inventoryManagement(_ stock: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun inventoryManagement(stock: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int inventoryManagement(List<int> stock) {
    
  }
}
```

### Go

```golang
func inventoryManagement(stock []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} stock
# @return {Integer}
def inventory_management(stock)
    
end
```

### Scala

```scala
object Solution {
    def inventoryManagement(stock: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn inventory_management(stock: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (inventory-management stock)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec inventory_management(Stock :: [integer()]) -> integer().
inventory_management(Stock) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec inventory_management(stock :: [integer]) :: integer
  def inventory_management(stock) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func inventoryManagement(stock: Array<Int64>): Int64 {

    }
}
```

