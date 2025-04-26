# 2678. 老人的数目

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>details</code>&nbsp;。<code>details</code>&nbsp;中每个元素都是一位乘客的信息，信息用长度为 <code>15</code>&nbsp;的字符串表示，表示方式如下：</p>

<ul>
	<li>前十个字符是乘客的手机号码。</li>
	<li>接下来的一个字符是乘客的性别。</li>
	<li>接下来两个字符是乘客的年龄。</li>
	<li>最后两个字符是乘客的座位号。</li>
</ul>

<p>请你返回乘客中年龄 <strong>严格大于 60 岁</strong>&nbsp;的人数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
<b>输出：</b>2
<b>解释：</b>下标为 0 ，1 和 2 的乘客年龄分别为 75 ，92 和 40 。所以有 2 人年龄大于 60 岁。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>details = ["1313579440F2036","2921522980M5644"]
<b>输出：</b>0
<b>解释：</b>没有乘客的年龄大于 60 岁。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= details.length &lt;= 100</code></li>
	<li><code>details[i].length == 15</code></li>
	<li><code>details[i]</code>&nbsp;中的数字只包含&nbsp;<code>'0'</code>&nbsp;到&nbsp;<code>'9'</code>&nbsp;。</li>
	<li><code>details[i][10]</code>&nbsp;是 <code>'M'</code>&nbsp;，<code>'F'</code>&nbsp;或者&nbsp;<code>'O'</code>&nbsp;之一。</li>
	<li>所有乘客的手机号码和座位号互不相同。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. Convert the value at index 11 and 12 to a numerical value.
2. The age of the person at index i is equal to details[i][11]*10+details[i][12].

## 示例

```
["7868190130M7522","5303914400F9211","9273338290F4010"]
["1313579440F2036","2921522980M5644"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSeniors(vector<string>& details) {
        
    }
};
```

### Java

```java
class Solution {
    public int countSeniors(String[] details) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
```

### C

```c
int countSeniors(char** details, int detailsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountSeniors(string[] details) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} details
 * @return {number}
 */
var countSeniors = function(details) {
    
};
```

### TypeScript

```typescript
function countSeniors(details: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $details
     * @return Integer
     */
    function countSeniors($details) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSeniors(_ details: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSeniors(details: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSeniors(List<String> details) {
    
  }
}
```

### Go

```golang
func countSeniors(details []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} details
# @return {Integer}
def count_seniors(details)
    
end
```

### Scala

```scala
object Solution {
    def countSeniors(details: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_seniors(details: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-seniors details)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_seniors(Details :: [unicode:unicode_binary()]) -> integer().
count_seniors(Details) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_seniors(details :: [String.t]) :: integer
  def count_seniors(details) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSeniors(details: Array<String>): Int64 {

    }
}
```

