# Associated Legendre Equation and Quantization (連帶勒讓德方程式的量子化條件與相鄰階耦合)

+++

## 證明目標:

球狀對稱問題做完變數分離後，天頂角方向恆得到下列本徵方程式（$\lambda$ 為分離常數）：

$$\frac{1}{\sin\theta}\frac{d}{d\theta}\left[ \sin\theta \frac{d\Theta}{d\theta} \right] + \left[ \lambda - \frac{m^2}{\sin^2\theta} \right]\Theta = 0$$

本文從這條式子出發，逐式證明下列六件事：

* (a) 換元 $x = \cos\theta$ 後化為**連帶勒讓德方程式 (Associated Legendre equation)**

  $$\frac{d}{dx}\left[ \left( 1 - x^2 \right)\frac{dy}{dx} \right] + \left[ \lambda - \frac{m^2}{1-x^2} \right]y = 0$$

* (b) 以 $y = \left( 1-x^2 \right)^{|m|/2}v$ 剝離端點奇異因子後，$v$ 的冪級數係數滿足

  $$a_{k+2} = \frac{\left( k + |m| \right)\left( k + |m| + 1 \right) - \lambda}{\left( k+1 \right)\left( k+2 \right)}a_k$$

* (c) 若級數**不**截斷，則 $y$ 在 $x = \pm 1$（即 $\theta = 0, \pi$）發散。
* (d) 因此級數必須截斷，這**強迫**分離常數與階數量子化：

  $$\lambda = l\left( l + 1 \right), \qquad l = |m|, |m|+1, |m|+2, \dots \qquad \Longleftrightarrow \qquad m = 0, \pm 1, \pm 2, \dots, \pm l$$

* (e) 解的結構為 $P_l^m(x) = \left( 1-x^2 \right)^{|m|/2}S_l(x)$，其中 $S_l$ 為次數恰為 $l - |m|$ 的多項式，且

  $$P_l^m\left( -x \right) = \left( -1 \right)^{l+|m|}P_l^m\left( x \right)$$

* (f) 在同一個 $m$ 之下，$\left\{ P_l^m \right\}$ 帶權正交，且**乘以 $x$ 只會耦合到相鄰階**：

  $$\int_{-1}^{1}P_{l'}^m\left( x \right)\,x\,P_{l}^m\left( x \right)\,dx \ne 0 \quad \Longrightarrow \quad l' = l \pm 1$$

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【定義 1】 天頂角本徵方程式 (Polar-angle eigenvalue equation)：** 變數分離後的 $\theta$ 方程式，$\lambda$ 為第二個分離常數。

  $$\frac{1}{\sin\theta}\frac{d}{d\theta}\left[ \sin\theta \frac{d\Theta}{d\theta} \right] + \left[ \lambda - \frac{m^2}{\sin^2\theta} \right]\Theta = 0$$

  * $\Theta(\theta)$ : 天頂角方向的解 (Polar-angle solution) $[\text{無單位}]$
  * $\theta$ : 天頂角 (Polar angle) $[\text{rad}]$，$0 \le \theta \le \pi$
  * $\lambda$ : 第二個分離常數 (Second separation constant) $[\text{無單位}]$，待定
  * $m$ : 第一個分離常數所給定的階數 (Order) $[\text{無單位}]$

* **【定義 2】 換元 (Change of variable)：**

  $$\begin{gather*}
  x &\overset{\text{def}}{=}& \cos\theta \\
  y\left( x \right) &\overset{\text{def}}{=}& \Theta\left( \theta \right)
  \end{gather*}$$

  * $x$ : 天頂角的餘弦 (Cosine of the polar angle) $[\text{無單位}]$，$-1 \le x \le 1$
  * $y(x)$ : 換元後的解 (Solution in the new variable) $[\text{無單位}]$

* **【定義 3】 剝離端點奇異因子 (Peeling off the endpoint singular factor)：** 端點 $x = \pm1$ 是方程式的正規奇點，先把奇異行為以顯式因子提出來，剩下的部分才用冪級數展開。

  $$y\left( x \right) \overset{\text{def}}{=} \left( 1 - x^2 \right)^{s/2}v\left( x \right)$$

  * $s$ : 階數的絕對值 (Absolute order) $[\text{無單位}]$，$s \overset{\text{def}}{=} |m|$
  * $v(x)$ : 剝離奇異因子後的餘因子 (Residual factor) $[\text{無單位}]$

* **【假設 1】 端點有界性 (Boundedness at the endpoints)：** $\theta = 0$ 與 $\theta = \pi$（南北極）是物理空間中的**平凡點**，解在該處必須有限。

  $$\left| y\left( \pm 1 \right) \right| < \infty$$

* **【假設 2】 階數為整數 (Integer order)：** 在球狀對稱問題中，$m$ 來自方位角方程式的單值條件，故為整數。

  $$m \in \mathbb{Z}, \qquad s = |m| \in \left\{ 0, 1, 2, \dots \right\}$$

* **【已知 1】 [Sturm–Liouville 本徵函數的正交性 (Orthogonality of Sturm–Liouville eigenfunctions)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Sturm_Liouville_Orthogonality.html)：** 適用前提為方程式可寫成自伴形式 $\dfrac{d}{dz}\left[ p_{\text{SL}}\dfrac{d\psi}{dz} \right] + \left( q_{\text{SL}} + \lambda w \right)\psi = 0$，且邊界項 $\left[ p_{\text{SL}}\left( \psi_i\psi_j' - \psi_j\psi_i' \right) \right]_a^b = 0$；此時對應到相異本徵值的本徵函數，在權函數 $w$ 之下彼此正交。

  $$\int_{a}^{b} w\left( z \right)\psi_{i}\left( z \right)\psi_{j}\left( z \right) dz = 0, \qquad \lambda_i \ne \lambda_j$$

  * $\psi_i$ : 第 $i$ 個本徵函數 (Eigenfunction) $[\text{無單位}]$
  * $w(z)$ : 權函數 (Weight function) $[\text{無單位}]$
  * $\lambda_i$ : 第 $i$ 個本徵值 (Eigenvalue) $[\text{無單位}]$
  * $p_{\text{SL}}, q_{\text{SL}}$ : 自伴形式的兩個係數函數 (Coefficients of the self-adjoint form) $[\text{無單位}]$
  * $a, b$ : 積分區間的兩個端點 (Endpoints of the interval)

* **【已知 2】 冪級數展開 (Power series expansion)：** 在正規點鄰域，二階線性 ODE 的解可寫成冪級數。

  $$v\left( x \right) = \sum_{k=0}^{\infty}a_k x^{k}$$

  * $a_k$ : 第 $k$ 階展開係數 (Expansion coefficient) $[\text{無單位}]$

* **【已知 3】 二項級數 (Binomial series)：** 用來辨認級數在端點的漸近行為。

  $$\begin{gather*}
  \left( 1 - u \right)^{-p} &=& \sum_{j=0}^{\infty}\binom{p+j-1}{j}u^{j} \\
  -\ln\left( 1 - u \right) &=& \sum_{j=1}^{\infty}\frac{u^{j}}{j}
  \end{gather*}$$

  * $p$ : 冪次 (Exponent) $[\text{無單位}]$，$p > 0$
  * $u$ : 展開變數 (Expansion variable) $[\text{無單位}]$，$|u| < 1$

* **【推導 1】 微分算子的換元 (Change of variable for the differential operator)：** 由【定義 2】直接微分。

  * (a) 一階算子：

  $$\begin{gather*}
  \frac{dx}{d\theta} &\overset{\text{定義 2}}{=}& \frac{d}{d\theta}\left[ \cos\theta \right] \\
  \frac{dx}{d\theta} &=& -\sin\theta
  \end{gather*}$$

  $$\begin{gather*}
  \frac{d}{d\theta} &=& \frac{dx}{d\theta}\frac{d}{dx} \\
  \frac{d}{d\theta} &\overset{\text{推導 1(a) 上式}}{=}& -\sin\theta\frac{d}{dx}
  \end{gather*}$$

  * (b) 正弦平方：

  $$\begin{gather*}
  \sin^2\theta &=& 1 - \cos^2\theta \\
  \sin^2\theta &\overset{\text{定義 2}}{=}& 1 - x^2
  \end{gather*}$$

* **【推導 2】 剝離奇異因子後的各項 (Terms after peeling off the singular factor)：** 由【定義 3】逐項微分，供 (b) 組裝。

  * (a) 一階導數：

  $$\begin{gather*}
  \frac{dy}{dx} &\overset{\text{定義 3}}{=}& \frac{d}{dx}\left[ \left( 1-x^2 \right)^{s/2}v \right] \\
  &=& \left( 1-x^2 \right)^{s/2}\frac{dv}{dx} - s x \left( 1-x^2 \right)^{s/2-1}v
  \end{gather*}$$

  * (b) 乘上 $\left( 1-x^2 \right)$：

  $$\begin{gather*}
  \left( 1-x^2 \right)\frac{dy}{dx} &\overset{\text{推導 2(a)}}{=}& \left( 1-x^2 \right)^{s/2+1}\frac{dv}{dx} - s x \left( 1-x^2 \right)^{s/2}v
  \end{gather*}$$

  * (c) 再微分一次（逐項套乘法律）：

  $$\begin{gather*}
  \frac{d}{dx}\left[ \left( 1-x^2 \right)^{s/2+1}\frac{dv}{dx} \right] &=& \left( 1-x^2 \right)^{s/2+1}\frac{d^2v}{dx^2} - \left( s+2 \right)x\left( 1-x^2 \right)^{s/2}\frac{dv}{dx}
  \end{gather*}$$

  $$\begin{gather*}
  \frac{d}{dx}\left[ -s x \left( 1-x^2 \right)^{s/2}v \right] &=& -s\left( 1-x^2 \right)^{s/2}v + s^2 x^2 \left( 1-x^2 \right)^{s/2-1}v - s x \left( 1-x^2 \right)^{s/2}\frac{dv}{dx}
  \end{gather*}$$

* **【推導 3】 級數各項的指標平移 (Index shift of the series terms)：** 把【已知 2】的冪級數代入下列三個算符項，逐項整理成 $x^{k}$ 的係數，供 (b) 比對。此處**只做代數展開**，不預設任何方程式成立。

  * (a) 二階項（先代入級數、再微分兩次，第一個和的最低冪次為 $x^{-2}$，故令 $k \to k+2$ 平移）：

  $$\begin{gather*}
  \left( 1-x^2 \right)\frac{d^2v}{dx^2} &\overset{\text{已知 2}}{=}& \left( 1-x^2 \right)\frac{d^2}{dx^2}\left[ \sum_{k=0}^{\infty}a_k x^{k} \right] \\
  &=& \left( 1-x^2 \right)\sum_{k=0}^{\infty}k\left( k-1 \right)a_k x^{k-2} \\
  &=& \sum_{k=0}^{\infty}k\left( k-1 \right)a_k x^{k-2} - \sum_{k=0}^{\infty}k\left( k-1 \right)a_k x^{k} \\
  &=& \sum_{k=0}^{\infty}\left( k+2 \right)\left( k+1 \right)a_{k+2}x^{k} - \sum_{k=0}^{\infty}k\left( k-1 \right)a_k x^{k}
  \end{gather*}$$

  * (b) 一階項（先代入級數、再微分一次，乘上 $x$ 之後冪次已是 $x^{k}$，不需平移）：

  $$\begin{gather*}
  -2\left( s+1 \right)x\frac{dv}{dx} &\overset{\text{已知 2}}{=}& -2\left( s+1 \right)x\frac{d}{dx}\left[ \sum_{k=0}^{\infty}a_k x^{k} \right] \\
  &=& -2\left( s+1 \right)x\sum_{k=0}^{\infty}k\,a_k x^{k-1} \\
  &=& -\sum_{k=0}^{\infty}2\left( s+1 \right)k\,a_k x^{k}
  \end{gather*}$$

  * (c) 零階項（不含微分，直接代入級數即可）：

  $$\left[ \lambda - s\left( s+1 \right) \right]v \overset{\text{已知 2}}{=} \sum_{k=0}^{\infty}\left[ \lambda - s\left( s+1 \right) \right]a_k x^{k}$$

+++

## 證明:

### (a) proof 連帶勒讓德方程式 (Associated Legendre equation)

先把【定義 1】的內層括號換元：

$$\begin{gather*}
\sin\theta\frac{d\Theta}{d\theta} &\overset{\text{推導 1(a)}}{=}& \sin\theta\left( -\sin\theta \right)\frac{dy}{dx} \\
&=& -\sin^2\theta\frac{dy}{dx} \\
&\overset{\text{推導 1(b)}}{=}& -\left( 1 - x^2 \right)\frac{dy}{dx}
\end{gather*}$$

再套一次外層算子：

$$\begin{gather*}
\frac{1}{\sin\theta}\frac{d}{d\theta}\left[ \sin\theta\frac{d\Theta}{d\theta} \right] &\overset{\text{(a) 上式}}{=}& \frac{1}{\sin\theta}\frac{d}{d\theta}\left[ -\left( 1-x^2 \right)\frac{dy}{dx} \right] \\
&\overset{\text{推導 1(a)}}{=}& \frac{1}{\sin\theta}\left( -\sin\theta \right)\frac{d}{dx}\left[ -\left( 1-x^2 \right)\frac{dy}{dx} \right] \\
&=& \frac{d}{dx}\left[ \left( 1-x^2 \right)\frac{dy}{dx} \right]
\end{gather*}$$

代回【定義 1】，並用【推導 1(b)】把 $\sin^2\theta$ 換成 $1-x^2$：

$$\frac{d}{dx}\left[ \left( 1 - x^2 \right)\frac{dy}{dx} \right] + \left[ \lambda - \frac{m^2}{1-x^2} \right]y = 0$$

此即**連帶勒讓德方程式**，且已經是自伴形式，可與【已知 1】對照：$p\left( x \right) = 1-x^2$、$q\left( x \right) = -\dfrac{m^2}{1-x^2}$、權函數 $w\left( x \right) = 1$、本徵值為 $\lambda$、區間為 $\left[ -1, 1 \right]$。

### (b) proof 級數遞迴關係 (Series recurrence relation)

把【推導 2(b)(c)】代入 (a) 的結果，並注意 $m^2 = s^2$：

$$\begin{gather*}
0 &\overset{\text{(a)}}{=}& \frac{d}{dx}\left[ \left( 1-x^2 \right)\frac{dy}{dx} \right] + \left[ \lambda - \frac{s^2}{1-x^2} \right]y \\
0 &\overset{\text{推導 2(c),定義 3}}{=}& \left( 1-x^2 \right)^{s/2+1}\frac{d^2v}{dx^2} - \left( 2s+2 \right)x\left( 1-x^2 \right)^{s/2}\frac{dv}{dx} - s\left( 1-x^2 \right)^{s/2}v + s^2x^2\left( 1-x^2 \right)^{s/2-1}v + \lambda\left( 1-x^2 \right)^{s/2}v - s^2\left( 1-x^2 \right)^{s/2-1}v
\end{gather*}$$

其中兩個 $\left( 1-x^2 \right)^{s/2-1}$ 項可先合併：

$$\begin{gather*}
s^2x^2\left( 1-x^2 \right)^{s/2-1} - s^2\left( 1-x^2 \right)^{s/2-1} &=& -s^2\left( 1 - x^2 \right)\left( 1-x^2 \right)^{s/2-1} \\
&=& -s^2\left( 1-x^2 \right)^{s/2}
\end{gather*}$$

代回並整體除以 $\left( 1-x^2 \right)^{s/2}$：

$$\begin{gather*}
0 &=& \left( 1-x^2 \right)\frac{d^2v}{dx^2} - \left( 2s+2 \right)x\frac{dv}{dx} + \left[ \lambda - s - s^2 \right]v \\
0 &=& \left( 1-x^2 \right)\frac{d^2v}{dx^2} - 2\left( s+1 \right)x\frac{dv}{dx} + \left[ \lambda - s\left( s+1 \right) \right]v
\end{gather*}$$

把【推導 3】的三項相加，並要求每一個 $x^{k}$ 的係數為零：

$$\begin{gather*}
0 &\overset{\text{推導 3(a)(b)(c)}}{=}& \left( k+2 \right)\left( k+1 \right)a_{k+2} - k\left( k-1 \right)a_k - 2\left( s+1 \right)k\,a_k + \left[ \lambda - s\left( s+1 \right) \right]a_k \\
\left( k+2 \right)\left( k+1 \right)a_{k+2} &=& \left[ k\left( k-1 \right) + 2\left( s+1 \right)k + s\left( s+1 \right) - \lambda \right]a_k \\
\left( k+2 \right)\left( k+1 \right)a_{k+2} &=& \left[ k^2 + \left( 2s+1 \right)k + s^2 + s - \lambda \right]a_k \\
\left( k+2 \right)\left( k+1 \right)a_{k+2} &=& \left[ \left( k+s \right)\left( k+s+1 \right) - \lambda \right]a_k \\
a_{k+2} &=& \frac{\left( k+s \right)\left( k+s+1 \right) - \lambda}{\left( k+1 \right)\left( k+2 \right)}a_k
\end{gather*}$$

遞迴每次跨兩階，故偶次項與奇次項各自成一條獨立的級數。

### (c) proof 不截斷則於端點發散 (Divergence at the endpoints without truncation)

若級數不截斷，取 $k \to \infty$ 的漸近比值：

$$\begin{gather*}
\frac{a_{k+2}}{a_k} &\overset{\text{(b)}}{=}& \frac{k^2 + \left( 2s+1 \right)k + s^2 + s - \lambda}{k^2 + 3k + 2} \\
&=& 1 + \frac{\left( 2s + 1 - 3 \right)k + s^2 + s - \lambda - 2}{k^2 + 3k + 2} \\
&=& 1 + \frac{2s-2}{k} + O\left( k^{-2} \right)
\end{gather*}$$

拿【已知 3】的兩個標準級數當比較對象（令 $u = x^2$，故 $j = k/2$）：

* (c-1) 當 $s \ge 1$，取 $p = s$：

$$\begin{gather*}
\frac{c_{k+2}}{c_k} &\overset{\text{已知 3}}{=}& \frac{\binom{s+j}{j+1}}{\binom{s+j-1}{j}} \\
&=& \frac{s+j}{j+1} \\
&=& 1 + \frac{s-1}{j+1} \\
&=& 1 + \frac{2\left( s-1 \right)}{k} + O\left( k^{-2} \right)
\end{gather*}$$

與 (c) 的漸近比值相同，故 $v\left( x \right)$ 在 $x \to \pm 1$ 的行為與 $\left( 1-x^2 \right)^{-s}$ 同階：

$$\begin{gather*}
y &\overset{\text{定義 3}}{=}& \left( 1-x^2 \right)^{s/2}v \\
&\sim& \left( 1-x^2 \right)^{s/2}\left( 1-x^2 \right)^{-s} \\
&\sim& \left( 1-x^2 \right)^{-s/2}
\end{gather*}$$

* (c-2) 當 $s = 0$，取對數級數：

$$\begin{gather*}
\frac{c_{k+2}}{c_k} &\overset{\text{已知 3}}{=}& \frac{j}{j+1} \\
&=& 1 - \frac{1}{j+1} \\
&=& 1 - \frac{2}{k} + O\left( k^{-2} \right)
\end{gather*}$$

同樣與 (c) 的漸近比值一致（$s = 0$ 時 $1 + \frac{2s-2}{k} = 1 - \frac{2}{k}$），故

$$\begin{gather*}
y &\overset{\text{定義 3}}{=}& v \\
&\sim& -\ln\left( 1 - x^2 \right)
\end{gather*}$$

兩種情形皆有 $\left| y\left( \pm 1 \right) \right| \to \infty$，與【假設 1】矛盾。

### (d) proof 分離常數與階數的量子化 (Quantization of the separation constant and the order)

由 (c)，級數**必須**截斷。取偶次或奇次其中一條級數在 $k = k_{\max}$ 截斷（另一條以 $a_0 = 0$ 或 $a_1 = 0$ 抹除），截斷即要求 (b) 的分子為零：

$$\begin{gather*}
a_{k_{\max}+2} &\overset{\text{def}}{=}& 0 \\
\left( k_{\max}+s \right)\left( k_{\max}+s+1 \right) - \lambda &\overset{\text{(b)}}{=}& 0 \\
\lambda &=& \left( k_{\max}+s \right)\left( k_{\max}+s+1 \right)
\end{gather*}$$

令

$$l \overset{\text{def}}{=} k_{\max} + s$$

代回上式即得

$$\lambda = l\left( l+1 \right)$$

而 $k_{\max} \in \left\{ 0, 1, 2, \dots \right\}$、由【假設 2】$s = |m|$ 為非負整數，故

$$\begin{gather*}
l &=& k_{\max} + |m| \\
l &\in& \left\{ |m|, |m|+1, |m|+2, \dots \right\}
\end{gather*}$$

$l$ 必為非負整數且 $l \ge |m|$。把這個不等式反過來讀，就是對固定的 $l$，階數只能取

$$m = 0, \pm 1, \pm 2, \dots, \pm l$$

### (e) proof 多項式結構與宇稱 (Polynomial structure and parity)

由 (d)，$v$ 是次數恰為 $k_{\max} = l - |m|$ 的多項式；又由 (b) 遞迴每次跨兩階、且另一條奇偶級數已被抹除，$v$ 只含與 $k_{\max}$ 同奇偶的冪次。把這個多項式記為 $S_l$，並把對應的解記為 $P_l^m$：

$$\begin{gather*}
P_l^m\left( x \right) &\overset{\text{定義 3}}{=}& \left( 1-x^2 \right)^{|m|/2}S_l\left( x \right) \\
\deg S_l &\overset{\text{(d)}}{=}& l - |m| \\
S_l\left( -x \right) &=& \left( -1 \right)^{l-|m|}S_l\left( x \right)
\end{gather*}$$

因子 $\left( 1-x^2 \right)^{|m|/2}$ 為偶函數，故

$$\begin{gather*}
P_l^m\left( -x \right) &=& \left( 1-x^2 \right)^{|m|/2}S_l\left( -x \right) \\
&=& \left( -1 \right)^{l-|m|}P_l^m\left( x \right) \\
&=& \left( -1 \right)^{l+|m|}P_l^m\left( x \right)
\end{gather*}$$

（最後一步用到 $\left( -1 \right)^{-2|m|} = 1$。）

### (f) proof 帶權正交性與相鄰階耦合 (Weighted orthogonality and adjacent-order coupling)

* (f-1) 帶權正交性：由 (a)，方程式已是自伴形式且 $p\left( \pm 1 \right) = 1 - \left( \pm 1 \right)^2 = 0$，邊界項自動為零；權函數 $w = 1$、本徵值 $\lambda = l\left( l+1 \right)$ 對相異 $l$ 相異。套【已知 1】：

$$\int_{-1}^{1}P_{l'}^m\left( x \right)P_{l}^m\left( x \right)dx = 0, \qquad l' \ne l$$

代入 (e) 的結構，即知 $\left\{ S_l \right\}_{l \ge |m|}$ 是權函數為 $\left( 1-x^2 \right)^{|m|}$ 的一族正交多項式：

$$\int_{-1}^{1}\left( 1-x^2 \right)^{|m|}S_{l'}\left( x \right)S_{l}\left( x \right)dx = 0, \qquad l' \ne l$$

* (f-2) 正交多項式對低次多項式的正交性：$\left\{ S_{|m|}, S_{|m|+1}, \dots, S_{l'-1} \right\}$ 的次數依序為 $0, 1, \dots, l'-|m|-1$，故其線性組合可張出**所有**次數小於 $l'-|m|$ 的多項式。任取次數小於 $l'-|m|$ 的多項式 $g$，把它展開成這組基底再逐項套 (f-1)：

$$\int_{-1}^{1}\left( 1-x^2 \right)^{|m|}S_{l'}\left( x \right)g\left( x \right)dx = 0, \qquad \deg g < l' - |m|$$

* (f-3) 上界：把待求積分用 (e) 改寫，並注意 $\deg\left( xS_l \right) = l - |m| + 1$：

$$\begin{gather*}
\int_{-1}^{1}P_{l'}^m\,x\,P_{l}^m\,dx &\overset{\text{(e)}}{=}& \int_{-1}^{1}\left( 1-x^2 \right)^{|m|}S_{l'}\left( x \right)\left[ xS_l\left( x \right) \right]dx
\end{gather*}$$

由 (f-2)，只要 $\deg\left( xS_l \right) < l'-|m|$ 此積分即為零：

$$\begin{gather*}
l - |m| + 1 &<& l' - |m| \\
l' &>& l + 1
\end{gather*}$$

故 $l' > l+1$ 時積分為零。

* (f-4) 下界：把 $x$ 改配給另一側，同理由 (f-2)：

$$\begin{gather*}
\int_{-1}^{1}P_{l'}^m\,x\,P_{l}^m\,dx &\overset{\text{(e)}}{=}& \int_{-1}^{1}\left( 1-x^2 \right)^{|m|}S_{l}\left( x \right)\left[ xS_{l'}\left( x \right) \right]dx
\end{gather*}$$

$$\begin{gather*}
l' - |m| + 1 &<& l - |m| \\
l' &<& l - 1
\end{gather*}$$

故 $l' < l-1$ 時積分亦為零。

* (f-5) 剔除 $l' = l$：由 (e) 的宇稱，被積函數的宇稱為

$$\begin{gather*}
P_{l'}^m\left( -x \right)\left( -x \right)P_{l}^m\left( -x \right) &\overset{\text{(e)}}{=}& \left( -1 \right)^{l'+|m|}\left( -1 \right)\left( -1 \right)^{l+|m|}P_{l'}^m\left( x \right)\,x\,P_{l}^m\left( x \right) \\
&=& \left( -1 \right)^{l+l'+1}P_{l'}^m\left( x \right)\,x\,P_{l}^m\left( x \right)
\end{gather*}$$

在對稱區間 $\left[ -1, 1 \right]$ 上，奇函數的積分為零，故積分不為零要求 $l+l'+1$ 為偶數，即 $l+l'$ 為奇數，於是 $l' \ne l$。

* (f-6) 合併 (f-3)(f-4)(f-5)：唯一可能不為零的情形是

$$l' = l \pm 1$$

+++

## 結構解釋

### 「量子化」不是物理額外加上去的，是微分方程自己逼出來的

整條鏈的關鍵只有一句話：**級數若不截斷就在端點爆掉**。$\theta = 0, \pi$ 是南北極，在真實空間中和其他點沒有兩樣，解在那裡必須是有限值——這不是額外假設，而是「$y$ 是一個定義在球面上的函數」這件事本身。一旦要求有限，遞迴分子就必須在某一階歸零，而分子 $\left( k+s \right)\left( k+s+1 \right)-\lambda$ 歸零的條件恰好把 $\lambda$ 鎖成 $l(l+1)$ 的形式。**先寫成 $l(l+1)$ 不是先知道答案，而是因為兩個相鄰整數的乘積正是這個分子的形狀。**

### $l \ge |m|$ 為什麼是「附贈」的

$l$ 的定義是 $l = k_{\max} + |m|$：$|m|$ 來自被剝離出去的奇異因子 $\left( 1-x^2 \right)^{|m|/2}$，$k_{\max}$ 來自剩下多項式的次數。多項式次數不可能為負，所以 $l$ 至少是 $|m|$。也就是說，$|m| \le l$ 這條在量子力學裡看起來像是額外規則的東西，其實只是「多項式次數 $\ge 0$」的改寫。

### (f) 為什麼是「選擇律」的數學骨架

(f) 說的是：把 $P_l^m$ 乘上一個 $x$（在球座標裡就是 $\cos\theta$，也就是 $z/r$），結果只會落在 $l\pm1$ 這兩個階上。三個限制各司其職——(f-3)(f-4) 是**次數守恆**（乘一個 $x$ 只能把次數推高一階，所以跨不到 $l\pm2$ 以上），(f-5) 是**宇稱**（$x$ 是奇函數，把同階配對打掉）。原子物理中電偶極躍遷的 $\Delta l = \pm 1$ 就是這三行的直接後果，跟「電子」「光子」都沒有關係，純粹是正交多項式的代數性質。

### 這族解在哪裡還會再出現

同一條方程式（換不同的 $m$ 與 $\lambda$）會在任何具球狀對稱的線性問題中出現：地球重力場與磁場的球諧展開、電磁學的多極展開、行星大氣的 Hough 函數、以及本文的直接目標——氫原子的角向波函數。因此把量子化條件在這裡一次證清楚，之後各領域都只需引用而不必重證。
