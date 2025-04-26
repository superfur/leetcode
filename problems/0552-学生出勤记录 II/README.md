# 552. 学生出勤记录 II

## 题目描述

可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
<ul>
	<li><code>'A'</code>：Absent，缺勤</li>
	<li><code>'L'</code>：Late，迟到</li>
	<li><code>'P'</code>：Present，到场</li>
</ul>

<p>如果学生能够 <strong>同时</strong> 满足下面两个条件，则可以获得出勤奖励：</p>

<ul>
	<li>按 <strong>总出勤</strong> 计，学生缺勤（<code>'A'</code>）<strong>严格</strong> 少于两天。</li>
	<li>学生 <strong>不会</strong> 存在 <strong>连续</strong> 3 天或 <strong>连续</strong> 3 天以上的迟到（<code>'L'</code>）记录。</li>
</ul>

<p>给你一个整数 <code>n</code> ，表示出勤记录的长度（次数）。请你返回记录长度为 <code>n</code> 时，可能获得出勤奖励的记录情况 <strong>数量</strong> 。答案可能很大，所以返回对 <code>10<sup>9</sup> + 7</code> <strong>取余</strong> 的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>8
<strong>解释：
</strong>有 8 种长度为 2 的记录将被视为可奖励：
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL" 
只有"AA"不会被视为可奖励，因为缺勤次数为 2 次（需要少于 2 次）。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 10101
<strong>输出：</strong>183236316
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 动态规划

## 示例

```
2
1
10101
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int checkRecord(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int checkRecord(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def checkRecord(self, n: int) -> int:
        
```

### C

```c
int checkRecord(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int CheckRecord(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var checkRecord = function(n) {
    
};
```

### TypeScript

```typescript
function checkRecord(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function checkRecord($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkRecord(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkRecord(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int checkRecord(int n) {
    
  }
}
```

### Go

```golang
func checkRecord(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def check_record(n)
    
end
```

### Scala

```scala
object Solution {
    def checkRecord(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_record(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (check-record n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec check_record(N :: integer()) -> integer().
check_record(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_record(n :: integer) :: integer
  def check_record(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkRecord(n: Int64): Int64 {

    }
}
```

