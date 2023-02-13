

# CMPS 2200 Assignment 1

**Name:**Kyra Zhu**


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.
.  **Yes. Since $2*2^n$ can get $2^n+1$ inductively and it shows that $2*2^n>= 2^n+1$ for all n>=1 according to base case, which shows $2^n+1$ is in O(2^n)**
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
. 
.  **No. As $2^(2^n)$ can be expressed as $(2^n)*(2^n)$, there is no such constant can make $(2^n)(2^n)>C(2^n)=2^n>C$, which simplifies into $n>log{2} C$ and we cannot choose from it, implying that 2^(2^n) is in ω(2^n) and $2^(2^n)>2^n$**
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  **No, $n^{1.01} \notin O(log{2}(n)^{2})$, because for n>2, $n^{1.01} > O(log{2}(n)^{2})$**
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  **Yes. $n^{1.01} \in \Theta(log{2}(n)^{2})$ evaluated shows $n^{1.01} > O(log{2}(n)^{2})$ for n>2**
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  **No. For $n^{1/2} \in O(log{2}(n)^3)$, If you raise both sides by 2, the right side will dominate asymptotically**
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  **Yes. From the previous answer, the right side will dominate asymptotically and given the right side is Omega, it will match each side.**

  - 1g
. **Assume that f(n) is a member of the intersection o(g(n)) if g(n) is equal to o(f(n)) as indicated. If c>0, then f(n)=o(f(n)) and f(n)<cf (n). Selecting a c<1 results in an intersection that is in conflict with the asymptotic function of f(n). Hence, it can be demonstrated that it contains the empty set at the intersection.**


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  **If x in the fibonacci sequence is greater than 1, this function returns the result of the extra integers**
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  
.  **The work is O(n). Because the list is linearly traversed and only checked once to produce the output, the span is also O(n), giving us an O(n) span and work.**
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  **Work and span is O(n) of this sequential algorithm. $2W(n/2)+c1 =W(n)$ can be considered as the height of tree is lg n and the leaves are 2^(lg n)**
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  **Because it is the same work completed in 3D, the work is unchanged. However, because it is parallelized, the span becomes $S(n)=S(n/2)+c1$ which can be reduced to S(1)=c1. The span changes to O(lg n)**
.  
.  
.  
.  
.  
.  

