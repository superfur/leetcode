# 949. 给定数字能组成的最大时间

## 题目描述

<p>给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。</p>

<p>24 小时格式为 <code>"HH:MM"</code> ，其中 <code>HH</code> 在 <code>00</code> 到 <code>23</code> 之间，<code>MM</code> 在 <code>00</code> 到 <code>59</code> 之间。最小的 24 小时制时间是 <code>00:00</code> ，而最大的是 <code>23:59</code> 。从 00:00 （午夜）开始算起，过得越久，时间越大。</p>

<p>以长度为 5 的字符串，按 <code>"HH:MM"</code> 格式返回答案。如果不能确定有效时间，则返回空字符串。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3,4]
<strong>输出：</strong>"23:41"
<strong>解释：</strong>有效的 24 小时制时间是 "12:34"，"12:43"，"13:24"，"13:42"，"14:23"，"14:32"，"21:34"，"21:43"，"23:14" 和 "23:41" 。这些时间中，"23:41" 是最大时间。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [5,5,5,5]
<strong>输出：</strong>""
<strong>解释：</strong>不存在有效的 24 小时制时间，因为 "55:55" 无效。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [0,0,0,0]
<strong>输出：</strong>"00:00"
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>arr = [0,0,1,0]
<strong>输出：</strong>"10:00"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>arr.length == 4</code></li>
	<li><code>0 <= arr[i] <= 9</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 字符串
- 回溯
- 枚举

## 示例

```
[1,2,3,4]
[5,5,5,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string largestTimeFromDigits(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public String largestTimeFromDigits(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
```

### C

```c
char* largestTimeFromDigits(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string LargestTimeFromDigits(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {string}
 */
var largestTimeFromDigits = function(arr) {
    
};
```

### TypeScript

```typescript
function largestTimeFromDigits(arr: number[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return String
     */
    function largestTimeFromDigits($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestTimeFromDigits(_ arr: [Int]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestTimeFromDigits(arr: IntArray): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String largestTimeFromDigits(List<int> arr) {
    
  }
}
```

### Go

```golang
func largestTimeFromDigits(arr []int) string {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {String}
def largest_time_from_digits(arr)
    
end
```

### Scala

```scala
object Solution {
    def largestTimeFromDigits(arr: Array[Int]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_time_from_digits(arr: Vec<i32>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (largest-time-from-digits arr)
  (-> (listof exact-integer?) string?)
  )
```

### Erlang

```erlang
-spec largest_time_from_digits(Arr :: [integer()]) -> unicode:unicode_binary().
largest_time_from_digits(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_time_from_digits(arr :: [integer]) :: String.t
  def largest_time_from_digits(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestTimeFromDigits(arr: Array<Int64>): String {

    }
}
```

