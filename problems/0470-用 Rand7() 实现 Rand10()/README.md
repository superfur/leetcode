# 470. 用 Rand7() 实现 Rand10()

## 题目描述

<p>给定方法&nbsp;<code>rand7</code>&nbsp;可生成 <code>[1,7]</code> 范围内的均匀随机整数，试写一个方法&nbsp;<code>rand10</code>&nbsp;生成 <code>[1,10]</code> 范围内的均匀随机整数。</p>

<p>你只能调用&nbsp;<code>rand7()</code>&nbsp;且不能调用其他方法。请不要使用系统的&nbsp;<code>Math.random()</code>&nbsp;方法。</p>

<ol>
</ol>

<p>每个测试用例将有一个内部参数 <code>n</code>，即你实现的函数 <code>rand10()</code> 在测试时将被调用的次数。请注意，这不是传递给 <code>rand10()</code> 的参数。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>1
<strong>输出: </strong>[2]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>2
<strong>输出: </strong>[2,8]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>3
<strong>输出: </strong>[3,8,10]
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶:</strong></p>

<ul>
	<li><code>rand7()</code>调用次数的&nbsp;<a href="https://en.wikipedia.org/wiki/Expected_value" target="_blank">期望值</a>&nbsp;是多少&nbsp;?</li>
	<li>你能否尽量少调用 <code>rand7()</code> ?</li>
</ul>


## 难度

Medium

## 标签

- 数学
- 拒绝采样
- 概率与统计
- 随机化

## 示例

```
1
2
3
```

## 示例代码

### C++

```cpp
// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution {
public:
    int rand10() {
        
    }
};
```

### Java

```java
/**
 * The rand7() API is already defined in the parent class SolBase.
 * public int rand7();
 * @return a random integer in the range 1 to 7
 */
class Solution extends SolBase {
    public int rand10() {
        
    }
}
```

### Python

```python
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        
```

### Python3

```python3
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        
```

### C

```c
// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

int rand10() {
    
}
```

### C#

```csharp
/**
 * The Rand7() API is already defined in the parent class SolBase.
 * public int Rand7();
 * @return a random integer in the range 1 to 7
 */
public class Solution : SolBase {
    public int Rand10() {
        
    }
}
```

### JavaScript

```javascript
/**
 * The rand7() API is already defined for you.
 * var rand7 = function() {}
 * @return {number} a random integer in the range 1 to 7
 */
var rand10 = function() {
    
};
```

### TypeScript

```typescript
/**
 * The rand7() API is already defined for you.
 * function rand7(): number {}
 * @return a random integer in the range 1 to 7
 */

function rand10(): number {

};
```

### PHP

```php
/*
 * The rand7() API is already defined for you.
 * @return a random integer in the range 1 to 7
 * function rand7();
*/

class Solution {
    /**
     * @param 
     * @return Integer
     */
    function rand10() {
        
    }
}
```

### Swift

```swift
/**
 * The rand7() API is already defined in the parent class SolBase.
 * func rand7() -> Int = {}
 * @return a random integer in the range 1 to 7
 */
class Solution : SolBase {
    func rand10() -> Int {
        
    }
}
```

### Kotlin

```kotlin
/**
 * The rand7() API is already defined in the parent class SolBase.
 * fun rand7(): Int {}
 * @return a random integer in the range 1 to 7
 */
class Solution : SolBase() {
    fun rand10(): Int {
        
    }
}
```

### Go

```golang
func rand10() int {
    
}
```

### Ruby

```ruby
# The rand7() API is already defined for you.
# def rand7()
# @return {Integer} a random integer in the range 1 to 7

def rand10()
    
end
```

### Scala

```scala
/**
 * The rand7() API is already defined in the parent class SolBase.
 * def rand7(): Int = {}
 * @return a random integer in the range 1 to 7
 */
object Solution extends SolBase {
    def rand10(): Int = {
        
    }
}
```

### Rust

```rust
/** 
 * The rand7() API is already defined for you.
 * @return a random integer in the range 1 to 7
 * fn rand7() -> i32;
 */

impl Solution {
    pub fn rand10() -> i32 {
        
    }
}
```

