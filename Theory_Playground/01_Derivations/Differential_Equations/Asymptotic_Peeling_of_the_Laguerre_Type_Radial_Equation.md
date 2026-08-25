---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Asymptotic Peeling of the Laguerre-Type Radial Equation (拉蓋爾型徑向方程式的漸近行為剝離)

+++

## 證明目標:

任何最終能以連帶拉蓋爾多項式解出的物理系統，其徑向方程式在無因次化之後都可以寫成 $\frac{d^{2}u}{dx^{2}} + \frac{b}{x}\frac{du}{dx} + \left[ -\frac{1}{4} + \frac{\lambda}{x} - \frac{c}{x^{2}} \right]u = 0$ 而處理這條方程式的第一步，永遠是**先把兩端** $(x \to \infty , x \to 0)$ **的漸近行為以顯式因子提出來**，再對剩下的部分做冪級數 $v(x)$ 展開

$$\begin{gather*}
&\frac{d^{2}u}{dx^{2}} + \frac{b}{x}\frac{du}{dx} + \left[ -\frac{1}{4} + \frac{\lambda}{x} - \frac{c}{x^{2}} \right]u &=& 0 \\
\Rightarrow& x\frac{d^{2}v}{dx^{2}} + \left( p + 1 - x \right)\frac{dv}{dx} + q\,v &=& 0 \\
& \left\{\begin{matrix}
u\left( x \right) &=& e^{-x/2}x^{\alpha}v\left( x \right) \\
p &=& 2\alpha + b - 1 \\
q &=& \lambda - \alpha - \frac{b}{2}
\end{matrix}\right.
\end{gather*}$$

其中

* $x$ : 無因次徑向座標 (Dimensionless radial coordinate) $[\text{無單位}]$，$0 < x < \infty$
* $u(x)$ : 尚未剝離漸近行為的完整徑向解 (Full radial solution) $[\text{無單位}]$
* $v(x)$ : 剝離之後剩下的餘因子 (Residual factor) $[\text{無單位}]$，其冪級數可截斷成多項式
* $b$ : 一階項係數 (First-order coefficient) $[\text{無單位}]$，三維球座標的徑向問題為 $b = 2$
* $c$ : 離心項係數 (Centrifugal coefficient) $[\text{無單位}]$，$c \ge 0$；三維球座標為 $c = \ell\left( \ell+1 \right)$
* $\lambda$ : 無因次能量參數 (Dimensionless energy parameter) $[\text{無單位}]$，兩端都不主導，其影響全部落在 $v$ 上
* $\alpha$ : 原點處的冪次 (Exponent at the origin) $[\text{無單位}]$，為指標方程式 $\alpha^{2} + \left( b-1 \right)\alpha - c = 0$ 的較大根
* $e^{-x/2}$ : 無窮遠處的指數衰減因子 (Exponential decay factor) $[\text{無單位}]$
* $p$ : 連帶拉蓋爾方程式的階參數 (Order parameter of the associated Laguerre equation) $[\text{無單位}]$
* $q$ : 連帶拉蓋爾方程式的本徵值 (Eigenvalue of the associated Laguerre equation) $[\text{無單位}]$

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【定義 1】 拉蓋爾型徑向方程式 (Laguerre-type radial equation)：** 中心力場的徑向方程式在做完無因次化（把長度尺度吸收進 $x$、使無窮遠處的衰減率恰為 $\tfrac12$）之後的標準形式。

  $$\frac{d^{2}u}{dx^{2}} + p\left( x \right)\frac{du}{dx} + q\left( x \right)u = 0$$

  * (a) 一階項的係數函數：

  $$p\left( x \right) \overset{\text{def}}{=} \frac{b}{x}$$

  * (b) 零階項的係數函數：

  $$q\left( x \right) \overset{\text{def}}{=} -\frac{1}{4} + \frac{\lambda}{x} - \frac{c}{x^{2}}$$

  * (c) 離心項係數非負：

  $$c \ge 0$$

  * (d) 為使原點處的第二解確實發散（而非有界），另要求：

  $$c > 0 \quad \text{或} \quad b > 1$$

  * $x$ : 無因次徑向座標 (Dimensionless radial coordinate) $[\text{無單位}]$，$0 < x < \infty$
  * $u(x)$ : 尚未剝離漸近行為的完整徑向解 (Full radial solution) $[\text{無單位}]$
  * $p(x)$ : 一階項的係數函數 (First-order coefficient function) $[\text{無單位}]$
  * $q(x)$ : 零階項的係數函數 (Zeroth-order coefficient function) $[\text{無單位}]$
  * $b$ : 一階項係數 (First-order coefficient) $[\text{無單位}]$，三維球座標的徑向問題為 $b = 2$
  * $c$ : 離心項係數 (Centrifugal coefficient) $[\text{無單位}]$，三維球座標為 $c = \ell\left( \ell+1 \right)$
  * $\lambda$ : 無因次能量參數 (Dimensionless energy parameter) $[\text{無單位}]$


* **【定義 2】 連帶拉蓋爾方程式的標準形式 (Standard form of the associated Laguerre equation)：** 本文最終要比對的目標形式。此方程式本身的截斷條件與帶權正交性，見本庫 [⟨Associated Laguerre Equation and Polynomials⟩](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Associated_Laguerre_Equation_and_Polynomials.html)。

  $$x\frac{d^{2}v}{dx^{2}} + \left( p + 1 - x \right)\frac{dv}{dx} + q\,v = 0$$

  * $x$ : 無因次自變數 (Dimensionless independent variable) $[\text{無單位}]$，與【定義 1】同一個
  * $v(x)$ : 剝離漸近行為之後剩下的餘因子 (Residual factor) $[\text{無單位}]$
  * $p$ : 階參數 (Order parameter) $[\text{無單位}]$
  * $q$ : 本徵值 (Eigenvalue) $[\text{無單位}]$

* **【假設 1】 無窮遠處的可歸一化條件 (Normalizability at infinity)：** 束縛態的解在無窮遠處必須趨於零，否則機率積分發散。

  $$\lim_{x \to \infty}u\left( x \right) = 0$$

  * $u(x)$ : 完整徑向解 (Full radial solution) $[\text{無單位}]$
  * $x$ : 無因次徑向座標 (Dimensionless radial coordinate) $[\text{無單位}]$

* **【假設 2】 原點處的有界性 (Boundedness at the origin)：** 原點是物理空間中的**平凡點**（力心所在，但不是物理奇點），解在該處必須有限。

  $$\left| u\left( 0 \right) \right| < \infty$$

  * $u(0)$ : 完整徑向解在原點的值 (Value of the solution at the origin) $[\text{無單位}]$

* **【已知 1】 Poincaré–Perron 定理 (Poincaré–Perron theorem)：** 適用前提有二：$p(x)$ 與 $q(x)$ 在 $x \to \infty$ 皆收斂到**有限**極限（見 (a)(b)），且 (d) 特徵方程式的兩根**實部相異**。滿足時，【定義 1】的**任一**非零解的指數成長率必等於其中一根。注意此定理只鎖定**指數**行為，解仍可帶次指數的冪次因子。



  $$\lim_{x \to \infty}\frac{1}{x}\ln\left| u\left( x \right) \right| = s_{i}, \qquad i \in \left\{ +, - \right\}$$


  * (a) 一階項係數函數的極限（適用前提之一：須為有限值）：

  $$p_{\infty} \overset{\text{def}}{=} \lim_{x \to \infty}p\left( x \right)$$

  * (b) 零階項係數函數的極限（適用前提之一：須為有限值）：

  $$q_{\infty} \overset{\text{def}}{=} \lim_{x \to \infty}q\left( x \right)$$

  * (c) 無窮遠處的**極限方程式**：把【定義 1】的兩個係數函數各自換成 (a)(b) 的極限值，得到一條常係數方程式：

  $$\frac{d^{2}u}{dx^{2}} + p_{\infty}\frac{du}{dx} + q_{\infty}u = 0$$

  * (d) **特徵方程式**：把指數試解 $u = e^{sx}$ 代入 (c)（$e^{sx} \ne 0$ 故可整條除掉）：

  $$\begin{gather*}
  0 &\overset{\text{已知 1(c)}}{=}& \frac{d^{2}}{dx^{2}}\left[ e^{sx} \right] + p_{\infty}\frac{d}{dx}\left[ e^{sx} \right] + q_{\infty}e^{sx} \\
  0 &=& s^{2}e^{sx} + p_{\infty}s\,e^{sx} + q_{\infty}e^{sx} \\
  0 &=& \left( s^{2} + p_{\infty}s + q_{\infty} \right)e^{sx} \\
  0 &=& s^{2} + p_{\infty}s + q_{\infty}
  \end{gather*}$$

  * $u(x)$ : 【定義 1】的任一非零解 (Any nontrivial solution) $[\text{無單位}]$
  * $x$ : 無因次徑向座標 (Dimensionless radial coordinate) $[\text{無單位}]$
  * $s_{\pm}$ : 特徵方程式的兩根 (Roots of the characteristic equation) $[\text{無單位}]$
  * $p_{\infty}$ : 一階項係數函數在無窮遠處的極限 (Limit of the first-order coefficient function) $[\text{無單位}]$
  * $q_{\infty}$ : 零階項係數函數在無窮遠處的極限 (Limit of the zeroth-order coefficient function) $[\text{無單位}]$
  * $s$ : 指數試解 $e^{sx}$ 的成長率 (Growth rate of the exponential trial solution) $[\text{無單位}]$


* **【已知 2】 Frobenius 定理 (Frobenius theorem at a regular singular point)：** 適用前提為 $x = 0$ 是**正規奇點**，即 $x\,p(x)$ 與 $x^{2}q(x)$ 在 $x \to 0$ 皆收斂到**有限**極限（見 (a)(b)）。滿足時，兩個線性獨立解在 $x \to 0$ 的**領頭行為**由 (d) 指標方程式的兩根 $\alpha_{\pm}$ 給出。兩根相差整數時，較小根那一支可能另乘一個 $\ln x$；由於 $\ln x$ 在原點本身就發散，這不影響下文「該支是否發散」的判定。

  $$u\left( x \right) \sim C_{+}x^{\alpha_{+}} + C_{-}x^{\alpha_{-}}$$


  * (a) 一階項的極限（適用前提之一：須為有限值）：

  $$p_{0} \overset{\text{def}}{=} \lim_{x \to 0}x\,p\left( x \right)$$

  * (b) 零階項的極限（適用前提之一：須為有限值）：

  $$q_{0} \overset{\text{def}}{=} \lim_{x \to 0}x^{2}q\left( x \right)$$

  * (c) 原點處的**極限方程式（尤拉方程式）**：把【定義 1】兩側同乘 $x^{2}$ 之後，一階項與零階項的係數分別是 $x\,p(x)$ 與 $x^{2}q(x)$；在 $x \to 0$ 各自換成 (a)(b) 的極限值：

  $$x^{2}\frac{d^{2}u}{dx^{2}} + p_{0}\,x\frac{du}{dx} + q_{0}\,u = 0$$

  * (d) **指標方程式**：把冪次試解 $u = x^{\alpha}$ 代入 (c)（$x^{\alpha} \ne 0$ 於 $x > 0$ 故可整條除掉）：

  $$\begin{gather*}
  0 &\overset{\text{已知 2(c)}}{=}& x^{2}\frac{d^{2}}{dx^{2}}\left[ x^{\alpha} \right] + p_{0}\,x\frac{d}{dx}\left[ x^{\alpha} \right] + q_{0}\,x^{\alpha} \\
  0 &=& x^{2}\,\alpha\left( \alpha-1 \right)x^{\alpha-2} + p_{0}\,x\,\alpha x^{\alpha-1} + q_{0}\,x^{\alpha} \\
  0 &=& \left[ \alpha\left( \alpha-1 \right) + p_{0}\,\alpha + q_{0} \right]x^{\alpha} \\
  0 &=& \alpha\left( \alpha-1 \right) + p_{0}\,\alpha + q_{0}
  \end{gather*}$$

  * $u(x)$ : 【定義 1】的通解 (General solution) $[\text{無單位}]$
  * $x$ : 無因次徑向座標 (Dimensionless radial coordinate) $[\text{無單位}]$
  * $\alpha_{\pm}$ : 指標方程式的兩根 (Roots of the indicial equation) $[\text{無單位}]$，$\alpha_{-} \le \alpha_{+}$
  * $C_{\pm}$ : 兩個線性獨立解的組合係數 (Combination coefficients) $[\text{無單位}]$
  * $p_{0}$ : 一階項在正規奇點處的極限 (Limit of the first-order coefficient at the regular singular point) $[\text{無單位}]$
  * $q_{0}$ : 零階項在正規奇點處的極限 (Limit of the zeroth-order coefficient at the regular singular point) $[\text{無單位}]$
  * $\alpha$ : 冪次試解 $x^{\alpha}$ 的冪次 (Exponent of the power trial solution) $[\text{無單位}]$


* **【已知 3】 一元二次方程式的公式解 (Quadratic formula)：** 適用前提為二次項係數 $A_2 \ne 0$。

  $$\begin{gather*}
  A_2 z^{2} + A_1 z + A_0 &=& 0 \\
  z_{\pm} &=& \frac{-A_1 \pm \left( A_1^{2} - 4A_2 A_0 \right)^{1/2}}{2A_2}
  \end{gather*}$$

  * $z_{\pm}$ : 兩個根 (The two roots) $[\text{無單位}]$
  * $A_2, A_1, A_0$ : 二次、一次、常數項係數 (Quadratic, linear and constant coefficients) $[\text{無單位}]$，$A_2 \ne 0$

* **【推導 1】 $x \to \infty$ 時拉蓋爾型徑向方程式的特徵根 (Characteristic roots of the Laguerre-type radial equation as $x \to \infty$)：** 先算出【已知 1】所需的兩個係數極限 (a)(b)（順帶確認兩者皆有限，適用前提之一成立），再餵進【已知 1(d)】的特徵方程式解根 (c)，最後 (d) 驗證兩根實部相異。

  * (a) 一階項係數函數的極限：

  $$\begin{gather*}
  \lim_{x \to \infty}p\left( x \right) &\overset{\text{定義 1(a)}}{=}& \lim_{x \to \infty}\frac{b}{x} \\
  \lim_{x \to \infty}p\left( x \right) &=& 0 \\
  p_{\infty} &\overset{\text{已知 1(a)}}{=}& 0
  \end{gather*}$$

  * (b) 零階項係數函數的極限：

  $$\begin{gather*}
  \lim_{x \to \infty}q\left( x \right) &\overset{\text{定義 1(b)}}{=}& \lim_{x \to \infty}\left( -\frac{1}{4} + \frac{\lambda}{x} - \frac{c}{x^{2}} \right) \\
  \lim_{x \to \infty}q\left( x \right) &=& -\frac{1}{4} + 0 - 0 \\
  \lim_{x \to \infty}q\left( x \right) &=& -\frac{1}{4} \\
  q_{\infty} &\overset{\text{已知 1(b)}}{=}& -\frac{1}{4}
  \end{gather*}$$

  * (c) 代入特徵方程式解根：

  $$\begin{gather*}
  0 &\overset{\text{已知 1(d)}}{=}& s^{2} + p_{\infty}s + q_{\infty} \\
  0 &\overset{\text{推導 1(a)(b)}}{=}& s^{2} + 0 \cdot s - \frac{1}{4} \\
  0 &=& s^{2} - \frac{1}{4} \\
  s^{2} &=& \frac{1}{4} \\
  s_{\pm} &=& \pm\frac{1}{2}
  \end{gather*}$$

  * (d) 兩根實部相異，【已知 1】的第二個適用前提成立：

  $$\begin{gather*}
  \mathrm{Re}\left( s_{+} \right) - \mathrm{Re}\left( s_{-} \right) &\overset{\text{推導 1(c)}}{=}& \frac{1}{2} - \left( -\frac{1}{2} \right) \\
  &=& 1 \\
  &\ne& 0
  \end{gather*}$$

  * $s_{\pm}$ : 特徵方程式的兩根 (Roots of the characteristic equation) $[\text{無單位}]$
  * $p_{\infty}, q_{\infty}$ : 兩個係數函數在無窮遠處的極限 (Limits of the coefficient functions) $[\text{無單位}]$

* **【推導 2】 無窮遠處的指數衰減率 (Exponential decay rate at infinity)：** 兩個適用前提已由【推導 1(a)(b)(d)】驗畢，故可用【已知 1】把成長率鎖在 $\pm\tfrac12$；再由【假設 1】推出成長率不可能為正，於是只剩負根。


  $$\begin{gather*}
  0 &\overset{\text{假設 1}}{=}& \lim_{x \to \infty}u\left( x \right) \\
  -\infty &=& \lim_{x \to \infty}\ln\left| u\left( x \right) \right| \\
  \frac{1}{x}\ln\left| u\left( x \right) \right| &<& 0 &\qquad \left( x \text{ 足夠大時} \right) \\
  \lim_{x \to \infty}\frac{1}{x}\ln\left| u\left( x \right) \right| &\le& 0 \\
  \lim_{x \to \infty}\frac{1}{x}\ln\left| u\left( x \right) \right| &\overset{\text{已知 1,推導 1(d)}}{=}& s_{i}&, i \in \left\{ +, - \right\} , \qquad s_{i} &\le& 0 \\
  \lim_{x \to \infty}\frac{1}{x}\ln\left| u\left( x \right) \right| &\overset{\text{推導 1(c)}}{=}& -\frac{1}{2}   \end{gather*}$$

  * $u(x)$ : 完整徑向解 (Full radial solution) $[\text{無單位}]$
  * $x$ : 無因次徑向座標 (Dimensionless radial coordinate) $[\text{無單位}]$
  * $s_{\pm}$ : 特徵方程式的兩根 (Roots of the characteristic equation) $[\text{無單位}]$，其值由【推導 1(c)】給出
  * $s_{i}$ : 兩根之中實際被解取到的那一個 (The root actually realized by the solution) $[\text{無單位}]$，$i \in \left\{ +, - \right\}$

* **【推導 3】 $x \to 0$ 時拉蓋爾型徑向方程式的指標根 (Indicial roots of the Laguerre-type radial equation as $x \to 0$)：** 先算出【已知 2】所需的兩個極限 (a)(b)（兩者皆為有限值，故 $x = 0$ 確為正規奇點，適用前提成立），再餵進【已知 2(d)】的指標方程式解根 (c)。


  * (a) 一階項在原點的極限：

  $$\begin{gather*}
  \lim_{x \to 0}x\,p\left( x \right) &\overset{\text{定義 1(a)}}{=}& \lim_{x \to 0}x \cdot \frac{b}{x} \\
  \lim_{x \to 0}x\,p\left( x \right) &=& b \\
  p_{0} &\overset{\text{已知 2(a)}}{=}& b
  \end{gather*}$$

  * (b) 零階項在原點的極限：

  $$\begin{gather*}
  \lim_{x \to 0}x^{2}q\left( x \right) &\overset{\text{定義 1(b)}}{=}& \lim_{x \to 0}x^{2}\left( -\frac{1}{4} + \frac{\lambda}{x} - \frac{c}{x^{2}} \right) \\
  \lim_{x \to 0}x^{2}q\left( x \right) &=& \lim_{x \to 0}\left( -\frac{x^{2}}{4} + \lambda x - c \right) \\
  \lim_{x \to 0}x^{2}q\left( x \right) &=& -c \\
  q_{0} &\overset{\text{已知 2(b)}}{=}& -c
  \end{gather*}$$

  * (c) 代入指標方程式解根（二次項係數 $A_2 = 1 \ne 0$，【已知 3】可用）：

  $$\begin{gather*}
  0 &\overset{\text{已知 2(d)}}{=}& \alpha\left( \alpha-1 \right) + p_{0}\,\alpha + q_{0} \\
  0 &\overset{\text{推導 3(a)(b)}}{=}& \alpha\left( \alpha-1 \right) + b\,\alpha - c \\
  0 &=& \alpha^{2} + \left( b-1 \right)\alpha - c \\
  \alpha_{\pm} &\overset{\text{已知 3}}{=}& \frac{-\left( b-1 \right) \pm \left[ \left( b-1 \right)^{2} - 4 \cdot 1 \cdot \left( -c \right) \right]^{1/2}}{2 \cdot 1} \\
  \alpha_{\pm} &=& \frac{\left( 1-b \right) \pm \left[ \left( 1-b \right)^{2} + 4c \right]^{1/2}}{2}
  \end{gather*}$$

  * $\alpha_{\pm}$ : 指標方程式的兩根 (Roots of the indicial equation) $[\text{無單位}]$
  * $p_{0}, q_{0}$ : 正規奇點處的兩個極限 (Limits at the regular singular point) $[\text{無單位}]$


* **【推導 4】 較小指標根為負 (The smaller indicial root is negative)：** 由【定義 1(d)】的兩種情形分別推出 $\alpha_{-} < 0$，供【推導 5】用【假設 2】剔除該支。

  * (a) 當 $c > 0$ ：只要這個條件成立，就自動滿足了【定義 1(d)】裡的 **或** 條件，此時不需要再去管 $b$ 是多少。

  $$\begin{gather*}
  1-b &\le& \left| 1-b \right| \\
  1-b &\overset{\text{定義 1(d)}}{<}& \left[ \left( 1-b \right)^{2} + 4c \right]^{1/2} \\
  \left( 1-b \right) - \left[ \left( 1-b \right)^{2} + 4c \right]^{1/2} &<& 0 \\
  \frac{\left( 1-b \right) - \left[ \left( 1-b \right)^{2} + 4c \right]^{1/2}}{2} &<& 0 \\
  \alpha_{-} &\overset{\text{推導 3(c)}}{<}& 0
  \end{gather*}$$

  * (b) 當 $c = 0$ 且 $b > 1$： 在 $c=0$ 的前提下，為了繼續滿足【定義 1(d)】，就必須強迫另一個條件成立，也就是必須要求 $b > 1$

  $$\begin{gather*}
  \left( 1-b \right)^{2} + 4c  &=&  \left( 1-b \right)^{2} \\
  \left[ \left( 1-b \right)^{2} + 4c \right]^{1/2} &=& \left[ \left( 1-b \right)^{2} \right]^{1/2} \\
  \left[ \left( 1-b \right)^{2} + 4c \right]^{1/2} &=& \left| 1-b \right| \\
  \left[ \left( 1-b \right)^{2} + 4c \right]^{1/2} &\overset{\text{定義 1(d)}}{=}& b-1 \\
  \frac{\left( 1-b \right) - \left[ \left( 1-b \right)^{2} + 4c \right]^{1/2}}{2} &=& \frac{\left( 1-b \right) - \left( b-1 \right)}{2} \\
  \frac{\left( 1-b \right) - \left[ \left( 1-b \right)^{2} + 4c \right]^{1/2}}{2} &=& 1-b \\
  \alpha_{-} &\overset{\text{推導 3(c)}}{=}& 1-b \\
  \alpha_{-} &\overset{\text{定義 1(d)}}{<}& 0
  \end{gather*}$$

  * $\alpha_{-}$ : 較小的指標根 (The smaller indicial root) $[\text{無單位}]$
  * $b, c$ : 【定義 1】的兩個係數 (Coefficients of the Laguerre-type radial equation) $[\text{無單位}]$

* **【推導 5】 原點處的領頭冪次 (Leading power at the origin)：** 適用前提已由【推導 3(a)(b)】驗畢，故可用【已知 2】把通解的領頭行為攤成兩支；再由【推導 4】知較小根那支發散，與【假設 2】矛盾，其係數必為零。


  $$\begin{gather*}
  &u\left( x \right) &\overset{\text{已知 2,推導 3(c)}}{\sim}& C_{+}x^{\alpha_{+}} + C_{-}x^{\alpha_{-}} \\
  &\lim_{x \to 0}\left| u\left( x \right) \right| &=& \lim_{x \to 0}\left| C_{+}x^{\alpha_{+}} + C_{-}x^{\alpha_{-}} \right| \\
  &\lim_{x \to 0}\left| u\left( x \right) \right| &=& \lim_{x\to 0} \left| x^{\alpha_-} \left( C_+ x^{\alpha_+ - \alpha_-} + C_- \right) \right| \\
  &\lim_{x \to 0}\left| u\left( x \right) \right| &=& \lim_{x\to 0} |x^{\alpha_-}| \cdot \lim_{x\to 0} \left| C_+ x^{\alpha_+ - \alpha_-} + C_- \right|   \\
  &\lim_{x \to 0}\left| u\left( x \right) \right| &\overset{\text{推導 3(c)}}{=}& \lim_{x\to 0} |x^{\alpha_-}| \cdot  \left| C_+ \cdot 0 + C_- \right|   \\
  &\lim_{x \to 0}\left| u\left( x \right) \right| &\overset{\text{推導 4(a)(b)}}{=}& \infty \cdot |C_-|\\
  \overset{\text{假設 2}}{\Rightarrow}&C_{-} &=& 0 \\
  \Rightarrow&u\left( x \right) &\sim& C_{+}x^{\alpha_{+}} + 0 \cdot x^{\alpha_{-}} \\
  &u\left( x \right) &\sim& C_{+}x^{\alpha_{+}}
  \end{gather*}$$

  * $u(x)$ : 完整徑向解 (Full radial solution) $[\text{無單位}]$
  * $\alpha_{\pm}$ : 指標方程式的兩根 (Roots of the indicial equation) $[\text{無單位}]$
  * $C_{\pm}$ : 兩支的組合係數 (Combination coefficients) $[\text{無單位}]$



* **【推導 6】 漸近因子的剝離設定 (The peeling ansatz)：** 把【推導 2】（無窮遠處的指數行為）與【推導 5】（原點的冪次行為）兩端的領頭行為，以顯式因子 $f$ 提出來，剩下的部分定義為餘因子 $v$。此步驟本身只是**改寫**（$f > 0$ 於 $x > 0$，故 $v$ 恆為良定義）；前面兩個推導的作用，是保證這樣提出來之後 $v$ 在兩端都不再帶指數行為或奇異冪次。


  * (a) 取較大指標根為剝離冪次（較小根那支已由【推導 5】剔除）：

  $$\alpha \overset{\text{let}}{=} \alpha_{+}$$

  * (b) 剝離因子（指數部分的 $-\tfrac12$ 來自【推導 2】、冪次部分的 $\alpha$ 來自【推導 5】）：

  $$f\left( x \right) \overset{\text{let}}{=} e^{-x/2}x^{\alpha}$$

  * (c) 餘因子：

  $$v\left( x \right) \overset{\text{let}}{=} \frac{u\left( x \right)}{f\left( x \right)}$$

  * (d) 於是完整解可改寫成：

  $$\begin{gather*}
  u\left( x \right) &\overset{\text{推導 6(c)}}{=}& f\left( x \right)v\left( x \right) \\
  u\left( x \right) &\overset{\text{推導 6(b)}}{=}& e^{-x/2}x^{\alpha}v\left( x \right)
  \end{gather*}$$

  * $\alpha$ : 剝離所取的原點冪次 (Peeling exponent at the origin) $[\text{無單位}]$
  * $\alpha_{+}$ : 較大的指標根 (The larger indicial root) $[\text{無單位}]$
  * $f(x)$ : 剝離因子 (Peeling factor) $[\text{無單位}]$，於 $x > 0$ 恆有 $f > 0$
  * $u(x)$ : 完整徑向解 (Full radial solution) $[\text{無單位}]$
  * $v(x)$ : 剝離之後剩下的餘因子 (Residual factor) $[\text{無單位}]$


* **【推導 7】 剝離因子的導數與代入後的兩個係數 (Derivatives of the peeling factor and the resulting coefficients)：** 把【推導 6】設好的 $f$ 微分兩次，並先把「代入【定義 1】並除以 $f$」之後會出現的一階項係數 (e) 與零階項係數 (f) 算完，讓證明段只剩一條乾淨的代入鏈。


  * (a) 一階對數導數：

  $$\begin{gather*}
  \frac{1}{f}\frac{df}{dx} &=& \frac{d}{dx}\left[ \ln f \right] \\
  \frac{1}{f}\frac{df}{dx} &\overset{\text{推導 6(b)}}{=}& \frac{d}{dx}\left[ \ln\left( e^{-x/2}x^{\alpha} \right) \right] \\
  \frac{1}{f}\frac{df}{dx} &=& \frac{d}{dx}\left[ \alpha\ln x - \frac{x}{2} \right] \\
  \frac{1}{f}\frac{df}{dx} &=& \frac{\alpha}{x} - \frac{1}{2}
  \end{gather*}$$

  * (b) 二階導數：

  $$\begin{gather*}
  \frac{1}{f}\frac{df}{dx} &\overset{\text{推導 7(a)}}{=}& \frac{\alpha}{x} - \frac{1}{2}  \\
  \frac{df}{dx} &=& f\left( \frac{\alpha}{x} - \frac{1}{2} \right) \\
  \frac{d^{2}f}{dx^{2}} &=& \frac{df}{dx}\left( \frac{\alpha}{x} - \frac{1}{2} \right) + f\frac{d}{dx}\left[ \frac{\alpha}{x} - \frac{1}{2} \right] \\
  \frac{d^{2}f}{dx^{2}} &=& f\left( \frac{\alpha}{x} - \frac{1}{2} \right)^{2} + f\left( -\frac{\alpha}{x^{2}} \right) \\
  \frac{1}{f}\frac{d^{2}f}{dx^{2}} &=& \frac{\alpha^{2}}{x^{2}} - \frac{\alpha}{x} + \frac{1}{4} - \frac{\alpha}{x^{2}}
  \end{gather*}$$

  * (c) $u = fv$ 的一階導數：

  $$\begin{gather*}
  \frac{du}{dx} &\overset{\text{推導 6(d)}}{=}& \frac{d}{dx}\left[ f v \right] \\
  \frac{du}{dx} &=& \frac{df}{dx}v + f\frac{dv}{dx}
  \end{gather*}$$

  * (d) $u = fv$ 的二階導數：

  $$\begin{gather*}
  \frac{du}{dx} &\overset{\text{推導 7(c)}}{=}& \frac{df}{dx}v + f\frac{dv}{dx} \\
  \frac{d^{2}u}{dx^{2}} &=& \frac{d}{dx}\left[ \frac{df}{dx}v + f\frac{dv}{dx} \right] \\
  \frac{d^{2}u}{dx^{2}} &=& \frac{d^{2}f}{dx^{2}}v + 2\frac{df}{dx}\frac{dv}{dx} + f\frac{d^{2}v}{dx^{2}}
  \end{gather*}$$

  * (e) 代入並除以 $f$ 之後，一階項的係數：

  $$\begin{gather*}
  \frac{2}{f}\frac{df}{dx} &\overset{\text{推導 7(a)}}{=}& 2\left( \frac{\alpha}{x} - \frac{1}{2} \right)  \\
  \frac{2}{f}\frac{df}{dx} + p\left( x \right) &=& 2\left( \frac{\alpha}{x} - \frac{1}{2} \right) + p\left( x \right) \\
  \frac{2}{f}\frac{df}{dx} + p\left( x \right)&\overset{\text{定義 1(a)}}{=}& \frac{2\alpha}{x} - 1 + \frac{b}{x} \\
  \frac{2}{f}\frac{df}{dx} + p\left( x \right)&=& \frac{2\alpha + b}{x} - 1
  \end{gather*}$$

  * (f) 代入並除以 $f$ 之後，零階項的係數（$x^{-2}$ 項的分子恰為【推導 3(c)】的指標方程式左式，而 $\alpha$ 依【推導 6(a)】正是它的根，故整批消失）：

  $$\begin{gather*}
  \frac{1}{f}\frac{d^{2}f}{dx^{2}} + p\left( x \right)\frac{1}{f}\frac{df}{dx} + q\left( x \right) &\overset{\text{推導 7(a)(b)}}{=}& \left( \frac{\alpha^{2}}{x^{2}} - \frac{\alpha}{x} + \frac{1}{4} - \frac{\alpha}{x^{2}} \right) + p\left( x \right)\left( \frac{\alpha}{x} - \frac{1}{2} \right) + q\left( x \right) \\
  &\overset{\text{定義 1(a)(b)}}{=}& \left( \frac{\alpha^{2}}{x^{2}} - \frac{\alpha}{x} + \frac{1}{4} - \frac{\alpha}{x^{2}} \right) + \frac{b}{x}\left( \frac{\alpha}{x} - \frac{1}{2} \right) + \left( -\frac{1}{4} + \frac{\lambda}{x} - \frac{c}{x^{2}} \right) \\
  &=& \frac{\alpha^{2} - \alpha + b\alpha - c}{x^{2}} + \frac{\lambda - \alpha - \frac{b}{2}}{x} + \frac{1}{4} - \frac{1}{4} \\
  &\overset{\text{推導 3(c),推導 6(a)}}{=}& \frac{0}{x^{2}} + \frac{\lambda - \alpha - \frac{b}{2}}{x} \\
  &=& \frac{\lambda - \alpha - \frac{b}{2}}{x}
  \end{gather*}$$

  * $f(x)$ : 剝離因子 (Peeling factor) $[\text{無單位}]$
  * $u(x)$ : 完整徑向解 (Full radial solution) $[\text{無單位}]$
  * $v(x)$ : 餘因子 (Residual factor) $[\text{無單位}]$
  * $\alpha$ : 剝離所取的原點冪次 (Peeling exponent at the origin) $[\text{無單位}]$


+++

## 證明:

### (a) proof 化為連帶拉蓋爾方程式 (Reduction to the associated Laguerre equation)

把【推導 6】的剝離設定代入【定義 1】、整條除以 $f$，再套【推導 7(e)(f)】算好的兩個係數，最後兩側同乘 $x$：

$$\begin{gather*}
0 &\overset{\text{定義 1}}{=}& \frac{d^{2}u}{dx^{2}} + p\left( x \right)\frac{du}{dx} + q\left( x \right)u \\
0 &\overset{\text{推導 7(c)(d)}}{=}& \left( \frac{d^{2}f}{dx^{2}}v + 2\frac{df}{dx}\frac{dv}{dx} + f\frac{d^{2}v}{dx^{2}} \right) + p\left( x \right)\left( \frac{df}{dx}v + f\frac{dv}{dx} \right) + q\left( x \right)f v \\
0 &=& \frac{d^{2}v}{dx^{2}} + \left[ \frac{2}{f}\frac{df}{dx} + p\left( x \right) \right]\frac{dv}{dx} + \left[ \frac{1}{f}\frac{d^{2}f}{dx^{2}} + p\left( x \right)\frac{1}{f}\frac{df}{dx} + q\left( x \right) \right]v \\
0 &\overset{\text{推導 7(e)(f)}}{=}& \frac{d^{2}v}{dx^{2}} + \left( \frac{2\alpha + b}{x} - 1 \right)\frac{dv}{dx} + \frac{\lambda - \alpha - \frac{b}{2}}{x}v \\
0 &=& x\frac{d^{2}v}{dx^{2}} + \left( 2\alpha + b - x \right)\frac{dv}{dx} + \left( \lambda - \alpha - \frac{b}{2} \right)v
\end{gather*}$$

與【定義 2】比對一階項係數：

$$\begin{gather*}
p + 1 &\overset{\text{定義 2,(a)}}{=}& 2\alpha + b \\
p &=& 2\alpha + b - 1
\end{gather*}$$

與【定義 2】比對零階項係數：

$$q \overset{\text{定義 2,(a)}}{=} \lambda - \alpha - \frac{b}{2}$$

### (b) verify 三維球座標的庫倫問題 (Verification: the 3-D Coulomb case)

取 $b = 2$、$c = \ell\left( \ell+1 \right)$，先由【推導 3(c)】求 $\alpha$：

$$\begin{gather*}
\alpha &\overset{\text{推導 3(c),推導 6(a)}}{=}& \frac{\left( 1-2 \right) + \left[ \left( 1-2 \right)^{2} + 4\ell\left( \ell+1 \right) \right]^{1/2}}{2} \\
\alpha &=& \frac{-1 + \left( 4\ell^{2} + 4\ell + 1 \right)^{1/2}}{2} \\
\alpha &=& \frac{-1 + \left( 2\ell+1 \right)}{2} \\
\alpha &=& \ell
\end{gather*}$$

再代入 (a) 的兩條係數式：

$$\begin{gather*}
p &\overset{\text{(a)}}{=}& 2\ell + 2 - 1 \\
p &=& 2\ell + 1 \\
q &\overset{\text{(a)}}{=}& \lambda - \ell - \frac{2}{2} \\
q &=& \lambda - \ell - 1
\end{gather*}$$

與氫原子問題中直接硬做所得的結果完全相同。

+++

## 結構解釋

### 「剝離」不是技巧，是被冪級數法逼出來的

冪級數 $\sum_k a_k x^k$ 有兩件事做不到：它在 $x = 0$ 必定解析（表現不了 $x^{-3/2}$ 這種奇異冪次），而且它要用無窮多項才能湊出 $e^{-x/2}$（因此永遠不會截斷）。方程式在兩端的行為恰好就是這兩種——原點是正規奇點、無窮遠是指數型——所以**先把這兩種行為以顯式因子提出來，剩下的部分才有可能是多項式**。整套「剝離 → 級數 → 截斷 → 量子化」的流程，第一步之所以長這樣，原因僅此而已。

### 為什麼不能「把方程式取極限」

一個常見但**不嚴謹**的寫法，是把整條方程式加上 $\left. \cdot \right|_{x \to \infty}$，說 $\frac{b}{x}\frac{du}{dx}$ 與 $\frac{\lambda}{x}u$ 都趨於零因此可丟。問題在於：若 $u$ 本身像 $e^{x/2}$ 那樣發散，則 $\frac{d^{2}u}{dx^{2}}$ 與 $\frac{b}{x}\frac{du}{dx}$ **兩者都發散**，「趨於零所以可丟」根本不成立。

嚴謹的做法是把極限取在**係數函數**上，而不是取在方程式或解上。這正是【已知 1(c)】與【已知 2(c)】兩條**極限方程式**的意義：換掉的是常數 $p_{\infty}, q_{\infty}$（或 $p_{0}, q_{0}$），不是解。而【已知 1】與【已知 2】兩條定理保證了「極限方程式的根」確實鎖死了「原方程式的解」的漸近行為。特徵方程式與指標方程式也不是憑空出現的——它們就是把試解 $e^{sx}$、$x^{\alpha}$ 代進各自的極限方程式、再除掉那個非零因子的結果，見【已知 1(d)】與【已知 2(d)】。這樣一來，【推導 1】與【推導 3】各自都只是「算兩個極限、代一次、解一元二次」，中間不需要任何「某項可丟」的宣告。

### 剝離的目的不是把 $v$ 變成常數

【推導 2】只證出**指數成長率**是 $-\tfrac12$，並沒有證出 $u$ 就等於 $e^{-x/2}$——次指數的冪次修正並沒有被鎖定，它會被吸收進 $v$。同理 $x^{\alpha}$ 拿掉的只是**原點的奇異冪次**。因此 $v$ 在證明 (a) 之後是一個**多項式**而不是常數；它的次數就是 $q$，也就是量子數。兩個因子拿掉的，恰好就是冪級數展開處理不了的那兩種行為，不多不少。

### 兩個因子分別來自方程式的哪一項

看【定義 1(b)】的 $q(x)$：$-\dfrac{1}{4}$ 是**唯一不隨 $x$ 衰減**的那一項，因此它獨自決定了 $q_{\infty}$、給出 $s_{\pm} = \pm\tfrac12$；而 $-\dfrac{c}{x^{2}}$ 是**發散最快**的那一項，因此它獨自決定了 $q_{0} = -c$、給出指標方程式。夾在中間的 $\dfrac{\lambda}{x}$ 在兩個極限中都被壓成零，它的影響全部落在 $v$ 身上——而 $v$ 的截斷條件 $q = \lambda - \alpha - \dfrac{b}{2}$ 為非負整數，正是**能量量子化**的來源。**量子化條件之所以只跟 $\lambda$ 有關，就是因為 $\lambda$ 是那個「兩端都不主導」的參數。**

### 為什麼指標方程式的根一定要選那一個

【推導 7(f)】的關鍵在於 $x^{-2}$ 項的分子 $\alpha^{2} - \alpha + b\alpha - c$ 恰好就是指標方程式本身。換句話說，$\alpha$ 之所以要取指標方程式的根，**不是為了讓解在原點有界（那只是篩掉哪一個根的理由），而是為了讓剝離之後的方程式不再有 $x^{-2}$ 奇異項**——沒有這一步，$v$ 的方程式就不會落在連帶拉蓋爾的標準形式上。兩個目的剛好被同一條方程式一次滿足，這不是巧合：正規奇點的指標方程式本來就是「把奇異行為抽乾淨」的充要條件。

### 【定義 1(d)】為什麼需要

若沒有這條，可能出現 $\alpha_{-} = 0$ 的情形（例如 $c = 0$ 且 $b < 1$）。那時較小根那一支在原點是**有界**的，【假設 2】就篩不掉它，【推導 5】的邏輯會斷。加上「$c > 0$ 或 $b > 1$」之後，【推導 4】的兩種情形涵蓋所有可能，$\alpha_{-} < 0$ 恆成立；順帶地，這條也自動保證兩根相異（判別式 $(1-b)^{2} + 4c > 0$），因此不必再額外要求非重根。下表三個系統都滿足此條件。

### 為什麼指數上是 $-\dfrac{x}{2}$ 而不是 $-x$

$\tfrac12$ 不是物理，是**無因次化時的人為選擇**：把長度尺度定成讓 $q_{\infty}$ 恰為 $-\tfrac14$，特徵根就會是 $\pm\sqrt{1/4} = \pm\tfrac12$。之所以要這樣選，是為了讓證明 (a) 的結果剛好落在連帶拉蓋爾方程式的**標準形式** $xv'' + (p+1-x)v' + qv = 0$ 上——標準形式裡的 $-x\dfrac{dv}{dx}$ 係數是 $-1$，回推回去就要求衰減率為 $\tfrac12$。若當初把尺度定成別的值，方程式仍然可解，只是要多做一次伸縮才對得上文獻裡的 $L_q^p$。

### 這份推導覆蓋哪些系統

只要徑向方程式能化成【定義 1】的形式就適用，$b$ 與 $c$ 隨系統改變：

| 系統 | $b$ | $c$ | $\alpha$ | $p$ | $\lambda$ |
|---|---|---|---|---|---|
| 三維庫倫場（氫原子、類氫離子、里德堡態） | $2$ | $\ell\left( \ell+1 \right)$ | $\ell$ | $2\ell+1$ | $\dfrac{me^{2}}{4\pi\varepsilon_0\hbar^{2}\alpha_{\text{decay}}}$ |
| 二維庫倫場 | $1$ | $m^{2}$ | $\left\| m \right\|$ | $2\left\| m \right\|$ | 同型 |
| 三維等向諧振子（先做 $x \propto r^{2}$ 換元） | $\tfrac{3}{2}$ | $\tfrac{\ell\left( \ell+1 \right)}{4}$ | $\tfrac{\ell}{2}$ | $\ell + \tfrac{1}{2}$ | $\dfrac{E}{2\hbar\omega}$ |

三者的 $e^{-x/2}$ 完全一樣，差別只在原點的冪次 $\alpha$——**這就是為什麼「剝離指數因子」這一步值得單獨寫成一份可引用的推導，而不必在每個系統裡重做一次。**
