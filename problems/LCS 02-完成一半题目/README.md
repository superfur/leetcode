# LCS 02. 完成一半题目

## 题目描述

有 `N` 位扣友参加了微软与力扣举办了「以扣会友」线下活动。主办方提供了 `2*N` 道题目，整型数组 `questions` 中每个数字对应了每道题目所涉及的知识点类型。
若每位扣友选择不同的一题，请返回被选的 `N` 道题目至少包含多少种知识点类型。


**示例 1：**
>输入：`questions = [2,1,6,2]`
>
>输出：`1`
>
>解释：有 2 位扣友在 4 道题目中选择 2 题。
> 可选择完成知识点类型为 2 的题目时，此时仅一种知识点类型
> 因此至少包含 1 种知识点类型。

**示例 2：**
>输入：`questions = [1,5,1,3,4,5,2,5,3,3,8,6]`
>
>输出：`2`
>
>解释：有 6 位扣友在 12 道题目中选择题目，需要选择 6 题。
> 选择完成知识点类型为 3、5 的题目，因此至少包含 2 种知识点类型。



**提示：**
- `questions.length == 2*n`
- `2 <= questions.length <= 10^5`
- `1 <= questions[i] <= 1000`

## 难度

Easy

## 标签

- 贪心
- 数组
- 哈希表
- 排序

## 示例

```
[2,1,6,2]
[1,5,1,3,4,5,2,5,3,3,8,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int halfQuestions(vector<int>& questions) {

    }
};
```

### Java

```java
class Solution {
    public int halfQuestions(int[] questions) {

    }
}
```

### Python

```python
class Solution(object):
    def halfQuestions(self, questions):
        """
        :type questions: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
```

### C

```c


int halfQuestions(int* questions, int questionsSize){

}
```

### C#

```csharp
public class Solution {
    public int HalfQuestions(int[] questions) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} questions
 * @return {number}
 */
var halfQuestions = function(questions) {

};
```

### TypeScript

```typescript
function halfQuestions(questions: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $questions
     * @return Integer
     */
    function halfQuestions($questions) {

    }
}
```

### Swift

```swift
class Solution {
    func halfQuestions(_ questions: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun halfQuestions(questions: IntArray): Int {

    }
}
```

### Go

```golang
func halfQuestions(questions []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} questions
# @return {Integer}
def half_questions(questions)

end
```

### Scala

```scala
object Solution {
    def halfQuestions(questions: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn half_questions(questions: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (half-questions questions)
  (-> (listof exact-integer?) exact-integer?)

  )
```

