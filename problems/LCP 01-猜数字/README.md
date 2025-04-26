# LCP 01. 猜数字

## 题目描述

<p>小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小A 猜对了几次？</p>

<p>&nbsp;</p>

<p>输入的<code>guess</code>数组为 小A 每次的猜测，<code>answer</code>数组为 小B 每次的选择。<code>guess</code>和<code>answer</code>的长度都等于3。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>guess = [1,2,3], answer = [1,2,3]
<strong>输出：</strong>3
<strong>解释：</strong>小A 每次都猜对了。</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>guess = [2,2,3], answer = [3,2,1]
<strong>输出：</strong>1
<strong>解释：</strong>小A 只猜对了第二次。</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ol>
	<li><code>guess</code>的长度 = 3</li>
	<li><code>answer</code>的长度 = 3</li>
	<li><code>guess</code>的元素取值为 <code>{1, 2, 3}</code> 之一。</li>
	<li><code>answer</code>的元素取值为 <code>{1, 2, 3}</code> 之一。</li>
</ol>


## 难度

Easy

## 标签

- 数组

## 示例

```
[1,2,3]
[1,2,3]
[2,2,3]
[3,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int game(vector<int>& guess, vector<int>& answer) {

    }
};
```

### Java

```java
class Solution {
    public int game(int[] guess, int[] answer) {

    }
}
```

### Python

```python
class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
```

### C

```c


int game(int* guess, int guessSize, int* answer, int answerSize){

}

```

### JavaScript

```javascript
/**
 * @param {number[]} guess
 * @param {number[]} answer
 * @return {number}
 */
var game = function(guess, answer) {

};
```

### TypeScript

```typescript
function game(guess: number[], answer: number[]): number {

};
```

### Go

```golang
func game(guess []int, answer []int) int {

}
```

