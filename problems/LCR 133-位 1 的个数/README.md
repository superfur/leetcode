# LCR 133. 位 1 的个数

## 题目描述

<p>编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为&nbsp;<a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">汉明重量</a>).）。</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。</li>
	<li>在 Java 中，编译器使用 <a href="https://baike.baidu.com/item/二进制补码/5295284">二进制补码</a> 记法来表示有符号整数。因此，在上面的&nbsp;<strong>示例 3&nbsp;</strong>中，输入表示有符号整数 <code>-3</code>。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 11 (控制台输入 00000000000000000000000000001011)
<strong>输出：</strong>3
<strong>解释：</strong>输入的二进制串 <code><strong>00000000000000000000000000001011</strong>&nbsp;中，共有三位为 '1'。</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 128 (控制台输入 00000000000000000000000010000000)
<strong>输出：</strong>1
<strong>解释：</strong>输入的二进制串 <strong>00000000000000000000000010000000</strong>&nbsp;中，共有一位为 '1'。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4294967293 (控制台输入 11111111111111111111111111111101，部分语言中 n = -3）
<strong>输出：</strong>31
<strong>解释：</strong>输入的二进制串 <strong>11111111111111111111111111111101</strong> 中，共有 31 位为 '1'。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>输入必须是长度为 <code>32</code> 的 <strong>二进制串</strong> 。</li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 191 题相同：<a href="https://leetcode-cn.com/problems/number-of-1-bits/">https://leetcode-cn.com/problems/number-of-1-bits/</a></p>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 位运算

## 示例

```
00000000000000000000000000001011
00000000000000000000000010000000
11111111111111111111111111111101
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        
    }
};
```

### Java

```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def hammingWeight(self, n: int) -> int:
        
```

### C

```c
int hammingWeight(uint32_t n) {
    
}
```

### C#

```csharp
public class Solution {
    public int HammingWeight(uint n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    
};
```

### Swift

```swift
class Solution {
    func hammingWeight(_ n: Int) -> Int {
        
    }
}
```

### Go

```golang
func hammingWeight(num uint32) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n, a positive integer
# @return {Integer}
def hamming_weight(n)
    
end
```

