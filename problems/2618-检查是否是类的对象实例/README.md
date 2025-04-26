# 2618. 检查是否是类的对象实例

## 题目描述

<p>请你编写一个函数，检查给定的值是否是给定类或超类的实例。</p>

<p>可以传递给函数的数据类型没有限制。例如，值或类可能是&nbsp; <code>undefined</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>func = () =&gt; checkIfInstance(new Date(), Date)
<b>输出：</b>true
<strong>解释：</strong>根据定义，Date 构造函数返回的对象是 Date 的一个实例。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>func = () =&gt; { class Animal {}; class Dog extends Animal {}; return checkIfInstance(new Dog(), Animal); }
<b>输出：</b>true
<strong>解释：</strong>
class Animal {};
class Dog extends Animal {};
checkIfInstanceOf(new Dog(), Animal); // true

Dog 是 Animal 的子类。因此，Dog 对象同时是 Dog 和 Animal 的实例。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>func = () =&gt; checkIfInstance(Date, Date)
<b>输出：</b>false
<strong>解释：</strong>日期的构造函数在逻辑上不能是其自身的实例。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>func = () =&gt; checkIfInstance(5, Number)
<b>输出：</b>true
<strong>解释：</strong>5 是一个 Number。注意，"instanceof" 关键字将返回 false。</pre>


## 难度

Medium

## 提示

1. In Javascript, inheritance is achieved with the prototype chain.
2. You can get the prototype of an object with the Object.getPrototypeOf(obj) function. Alternatively, you can code obj['__proto__'].
3. You can compare an object's __proto__ with classFunction.prototype.
4. Traverse the entire prototype chain until you find a match.

## 示例

```
() => checkIfInstanceOf(new Date(), Date)
() => { class Animal {}; class Dog extends Animal {}; return checkIfInstanceOf(new Dog(), Animal); }
() => checkIfInstanceOf(Date, Date)
() => checkIfInstanceOf(5, Number)
```

## 示例代码

### JavaScript

```javascript
/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
```

### TypeScript

```typescript
function checkIfInstanceOf(obj: any, classFunction: any): boolean {
    
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
```

