
### practice problem

1. 打印斐波那契数列
  - a, b = 0, 1   a, b = b, a+b是什么意思？
    - 答案：这是Python的语言功能之一元组解包，这种写法等效于：
        new_a = b
        new_b = a + b
        a = new_a
        b = new_b
  - for _ in range(n)是什么意思？为什么不使用for i in range(n)?
    - 答案：for _ in range(n) 与for i in range(n)都可表示循环十次，但是前者表示不需要使用到循环的变量_,而后者一般在循环中使用到了变量i 
