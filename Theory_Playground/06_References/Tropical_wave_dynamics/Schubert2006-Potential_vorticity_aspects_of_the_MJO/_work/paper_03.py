#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""a_paper.jsonl 第三批：4. Solution of the horizontal structure equations（拆成 3 個 cell）。"""
from _common import append

CELLS = []

# --------------------------------------------------- 4（一）強迫形式與傅立葉轉換
CELLS.append(r"""### 4. Solution of the horizontal structure equations

We assume that the diabatic forcing is due to an eastward propagating region of deep convection. The exact form of the forcing is

$$
\hat{Q}(x, y, t) = \tfrac{1}{2}Q_0 \exp\!\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right]
\begin{cases}
1 + \cos\dfrac{\pi\xi}{a_0}, & |\xi| \le a_0, \\[2mm]
0, & |\xi| \ge a_0,
\end{cases}
\tag{4.1}
$$

where $\xi = x - ct$, $c$ is the propagation speed of the cloud cluster, $y_0$ its center, $a_0$ its half-width in $x$, $b_0$ its $e$-folding width in $y$, and $Q_0$ its peak value. The values chosen for these parameters are listed in Table 1. It is interesting to note that the area integral of $(4.1)$ yields $\iint \hat{Q}(\xi, y)\,dx\,dy = \pi^{1/2}Q_0 a_0 b_0$, so that our variation of the parameter $y_0$ has no effect on the total diabatic heating rate, $\pi^{1/2}Q_0 a_0 b_0$.

Assuming the solutions are steady in a reference frame translating eastward with speed $c$, we can simplify $(3.5)$ through the replacements $\partial/\partial t \to -c(\partial/\partial\xi)$ and $\partial/\partial x \to \partial/\partial\xi$. We then take the Fourier $\xi$-transform of the resulting system, defining, for example,

$$
\hat{u}_m(y) = \frac{1}{2\pi a}\int_{-\pi a}^{\pi a}\hat{u}(\xi, y)\, e^{-im\xi/a}\, d\xi,
\qquad
\hat{u}(\xi, y) = \sum_{m=-\infty}^{\infty}\hat{u}_m(y)\, e^{im\xi/a},
\tag{4.2}
$$

where the integer $m$ denotes the zonal wavenumber. Similar Fourier transform pairs exist for $\hat{v}_m(y)$, $\hat{\phi}_m(y)$, $\hat{T}_m(y)$, $\hat{w}_m(y)$, and $\hat{Q}_m(y)$. In this way, the system $(3.5)$ reduces to

$$
\left(\alpha - \frac{imc}{a}\right)\hat{u}_m - \beta y\hat{v}_m + \frac{im}{a}\hat{\phi}_m = 0,
\qquad
\left(\alpha - \frac{imc}{a}\right)\hat{v}_m + \beta y\hat{u}_m + \frac{d\hat{\phi}_m}{dy} = 0,
$$

$$
\left(\alpha - \frac{imc}{a}\right)\hat{\phi}_m + \bar{c}^{2}\left(\frac{im}{a}\hat{u}_m + \frac{d\hat{v}_m}{dy}\right) = \kappa\hat{Q}_m,
\tag{4.3}
$$

where $\bar{c}^{2} = R\Gamma[(\pi/z_T)^{2} + (1/4)]^{-1} \approx (41.25\text{ m s}^{-1})^{2}$. Once this "shallow water system" has been solved for $\hat{u}_m$, $\hat{v}_m$, $\hat{\phi}_m$, the vertical velocity $\hat{w}_m$ can be recovered from

$$
\hat{w}_m = \left(\frac{\pi^{2}}{z_T^{2}} + \frac{1}{4}\right)^{-1}\left(\frac{im}{a}\hat{u}_m + \frac{d\hat{v}_m}{dy}\right).
\tag{4.4}
$$

The Fourier $\xi$-transform of $\hat{Q}(\xi, y)$, defined by $(4.1)$, is given by $\hat{Q}_m(y) = (2\pi a)^{-1}\int_{-\pi a}^{\pi a}\hat{Q}(\xi, y)\exp(-im\xi/a)\,d\xi$, which is easily evaluated to yield

$$
\hat{Q}_m(y) = \frac{\pi Q_0}{2[\pi^{2} - (ma_0/a)^{2}]}\frac{\sin(ma_0/a)}{m}\exp\!\left[-\left(\frac{y - y_0}{b_0}\right)^{2}\right].
\tag{4.5}
$$

We now write the system $(4.3)$ in the convenient vector form

$$
\left(\alpha - \frac{imc}{a}\right)\hat{\boldsymbol{\eta}}_m + \mathcal{L}\hat{\boldsymbol{\eta}}_m = \kappa\hat{\mathbf{Q}}_m,
\tag{4.6}
$$

> **註 1（原文腳註）**：$(4.6)$ 第一項之所以這麼簡潔，靠的是「瑞利摩擦與牛頓冷卻的阻尼率相等」這個假設。不過 $(4.6)$ 之後的推導很容易推廣到「$10$–$20$ 天輻射阻尼率 ＋ $3$–$5$ 天摩擦阻尼率」的情形 [*Lin et al.*, $2005$]。

---

本節假設**非絕熱強迫來自一塊向東傳播的深對流區**，其精確形式即 $(4.1)$：**緯向是一個半寬 $a_0$ 的升餘弦「帽子」、經向是一個 $e$-folding 寬度為 $b_0$ 的高斯**，中心位在 $y = y_0$，峰值為 $Q_0$，並以速度 $c$ 東移（$\xi = x - ct$ 為隨波座標）。

這裡有一個很漂亮的設計：$(4.1)$ 的面積分是 $\pi^{1/2}Q_0 a_0 b_0$，**完全與 $y_0$ 無關**。這代表後面比較「$y_0 = 0$」與「$y_0 = 450\text{ km}$」兩組實驗時，**兩者的總加熱率一模一樣**——差別純粹來自「加熱擺在哪」，而不是「加熱多少」，這讓對照組乾淨得多。

**求解策略的三段式化簡**：

1. **假設定常**：在以速度 $c$ 東移的參考系中解是定常的 → $\partial/\partial t \to -c\,\partial/\partial\xi$，時間維度消失。
2. **緯向傅立葉轉換**：把 $\xi$ 展開成緯向波數 $m$ 的級數（式 $(4.2)$），$(3.5)$ 就化成每個 $m$ 各自獨立的常微分方程組 $(4.3)$——形式上就是一組**淺水系統**。其中 $\bar{c}^{2} = R\Gamma[(\pi/z_T)^{2} + 1/4]^{-1}$，代入數值得**重力波相速 $\bar{c} \approx 41.25\text{ m s}^{-1}$**（即第一斜壓模態的等效重力波速）。
3. 解出 $\hat{u}_m, \hat{v}_m, \hat{\phi}_m$ 之後，垂直速度 $\hat{w}_m$ 由 $(4.4)$ 的**診斷關係**直接還原。

加熱項本身的緯向傅立葉係數 $(4.5)$ 有一個 $\sin(ma_0/a)/m$ 的因子——這就是「有限寬度帽子」在波數空間的特徵：**$a_0$ 決定了哪些緯向波數被有效激發**。

最後把 $(4.3)$ 寫成向量形式 $(4.6)$，為下一步的**正規模態轉換（normal mode transform）**鋪路。""")

# --------------------------------------------------- 4（二）正規模態轉換
CELLS.append(r"""#### （承 §4）正規模態轉換與赤道波本徵函數

where

$$
\mathcal{L} = \begin{pmatrix}
0 & -\beta y & im/a \\
\beta y & 0 & d/dy \\
\bar{c}^{2}im/a & \bar{c}^{2}d/dy & 0
\end{pmatrix},
\qquad
\hat{\boldsymbol{\eta}}_m(y) = \begin{pmatrix}\hat{u}_m(y) \\ \hat{v}_m(y) \\ \hat{\phi}_m(y)\end{pmatrix},
\qquad
\hat{\mathbf{Q}}_m(y) = \begin{pmatrix}0 \\ 0 \\ \hat{Q}_m(y)\end{pmatrix}.
\tag{4.7}
$$

The Fourier transformed Eq. $(4.6)$ can be solved using a normal mode transform in the meridional direction. To accomplish this, first define the inner product

$$
(\mathbf{f}, \mathbf{g}) = \int_{-\infty}^{\infty}\left(f_1 g_1^{*} + f_2 g_2^{*} + \frac{1}{\bar{c}^{2}}f_3 g_3^{*}\right)d\hat{y},
\tag{4.8}
$$

where $\mathbf{f}(\hat{y})$ and $\mathbf{g}(\hat{y})$ are complex, three component vector functions of the dimensionless meridional coordinate $\hat{y} = (\beta/\bar{c})^{1/2}y = \epsilon^{1/4}(y/a)$, and where the '$*$' symbol denotes the complex conjugate and $\epsilon = 4\Omega^{2}a^{2}/\bar{c}^{2}$ is Lamb's parameter. With $\bar{c} = 41.25\text{ m s}^{-1}$ we obtain $\epsilon = 507.3$. The inner product $(4.8)$ is suggested by the total energy principle associated with $(4.6)$. The adjoint of $\mathcal{L}$, denoted by $\mathcal{L}^{\dagger}$ and defined by $(\mathcal{L}\mathbf{f}, \mathbf{g}) = (\mathbf{f}, \mathcal{L}^{\dagger}\mathbf{g})$, is related to $\mathcal{L}$ by $\mathcal{L}^{\dagger} = -\mathcal{L}$. In other words, the linear operator $\mathcal{L}$ is skew-Hermitian with respect to the inner product $(4.8)$. The skew-Hermitian property dictates that the eigenvalues of $\mathcal{L}$ are pure imaginary and that the eigenfunctions form a complete [*Wu and Moore*, $2004$], orthogonal set (as long as degeneracy does not occur). Denoting an eigenvalue by $i\nu_{mnr}$ and a corresponding eigenfunction by $\mathbf{K}_{mnr}(\hat{y})$, we have

$$
\mathcal{L}\mathbf{K}_{mnr} = i\nu_{mnr}\mathbf{K}_{mnr},
\qquad\text{with}\qquad
\mathbf{K}_{mnr}(\hat{y}) = \begin{pmatrix}U_{mnr}(\hat{y}) \\ V_{mnr}(\hat{y}) \\ \Phi_{mnr}(\hat{y})\end{pmatrix}.
\tag{4.9}
$$

The eigenvalues of $\mathcal{L}$, which yield the dispersion relation for equatorially trapped waves, satisfy the cubic equation [*Matsuno*, $1966$]

$$
\epsilon\hat{\nu}^{2} - m^{2} - \frac{m}{\hat{\nu}} = \epsilon^{1/2}(2n + 1),
\tag{4.10}
$$

where $n = 0, 1, 2, \ldots$ is the index for the meridional mode and $\hat{\nu} = \nu/(2\Omega)$ is the dimensionless frequency. We let $r = 0, 1, 2$ be the index corresponding to the three roots of the dispersion relation, so that the eigenfunctions and eigenvalues can be characterized by the triple index $m, n, r$. Special care is required for the case $n = 0$, for which $(4.10)$ can be factored into $(\epsilon^{1/2}\hat{\nu} + m)(\epsilon^{1/2}\hat{\nu}^{2} - m\hat{\nu} - 1) = 0$. The root $\epsilon^{1/2}\hat{\nu} = -m$ must be discarded because the corresponding eigenfunction is unbounded in $\hat{y}$. Thus, when $n = 0$, only the two solutions of $\epsilon^{1/2}\hat{\nu}^{2} - m\hat{\nu} - 1 = 0$ are retained and are indexed by $r = 0$ (mixed Rossby-gravity wave) and $r = 2$ (eastward inertia-gravity wave). The eigenfunctions for Kelvin waves can be found separately by setting $V_{mnr}$ to zero in $(4.9)$. The Kelvin wave eigenvalues $\epsilon^{1/2}\hat{\nu} = m$ can be formally considered as a solution to $(4.10)$ when $n = -1$. We index this solution as $r = 2$. Then, for given $n = -1, 0, 1, \ldots$, $\mathbf{K}_{mnr}(\hat{y})$ is the eigenfunction corresponding to the eigenvalue $\nu_{mnr}$. The eigenfunctions $\mathbf{K}_{mnr}(\hat{y})$ are given by

$$
\mathbf{K}_{mnr}(\hat{y}) = A_{mnr}
\begin{pmatrix}
\epsilon^{1/4}\left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\dfrac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) + \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\dfrac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})\right] \\[3mm]
-i\left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)\mathcal{H}_{n}(\hat{y}) \\[3mm]
\bar{c}\epsilon^{1/4}\left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\dfrac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) - \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\dfrac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y})\right]
\end{pmatrix},
\tag{4.11}
$$

where the meridional structure functions $\mathcal{H}_n(\hat{y})$ ($n = 0, 1, 2, \ldots$) are related to the Hermite polynomials $H_n(\hat{y})$ ($n = 0, 1, 2, \ldots$) by

$$
\mathcal{H}_n(\hat{y}) = \left(\pi^{1/2}2^{n}n!\right)^{-(1/2)}H_n(\hat{y})\, e^{-(1/2)\hat{y}^{2}}.
\tag{4.12}
$$

> **註 2（原文腳註）**：對本文的用途而言，經向結構函數 $\mathcal{H}_n$ 比拋物柱函數（parabolic cylinder functions）$D_n$ 更方便。兩者的關係是 $\mathcal{H}_n(\hat{y}) = (\pi^{1/2}n!)^{-(1/2)}D_n(2^{1/2}\hat{y})$。

Since the Hermite polynomials satisfy the recurrence relation $\hat{y}H_n(\hat{y}) = \frac{1}{2}H_{n+1}(\hat{y}) + nH_{n-1}(\hat{y})$ and the derivative relation $dH_n(\hat{y})/d\hat{y} = 2nH_{n-1}(\hat{y})$, it is easily shown that the meridional structure functions $\mathcal{H}_n(\hat{y})$ satisfy the recurrence relation

$$
\hat{y}\mathcal{H}_n(\hat{y}) = \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y}),
\tag{4.13}
$$

and the derivative relation

$$
\frac{d\mathcal{H}_n(\hat{y})}{d\hat{y}} = -\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}(\hat{y}) + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}(\hat{y}).
\tag{4.14}
$$

The first two meridional structure functions are $\mathcal{H}_0(\hat{y}) = \pi^{-(1/4)}e^{-(1/2)\hat{y}^{2}}$ and $\mathcal{H}_1(\hat{y}) = 2^{1/2}\pi^{-(1/4)}\hat{y}\, e^{-(1/2)\hat{y}^{2}}$, from which all succeeding structure functions can be computed using the recurrence relation $(4.13)$. Computing $\mathcal{H}_n(\hat{y})$ via its recurrence relation is much preferable to computing $H_n(\hat{y})$ via its recurrence relation and then computing $\mathcal{H}_n(\hat{y})$ by evaluation of the right hand side of $(4.12)$, because the former method avoids explicit calculation of the factor $2^{n}n!$ for large $n$. Plots of $\mathcal{H}_n(\hat{y})$ for $n = 0, 1, 2, 3, 4$ are shown in Fig. 2. The normalization factor in $(4.11)$ is given by

$$
A_{mnr} = \left[\epsilon^{1/2}(n+1)\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)^{2} + \epsilon^{1/2}n\left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)^{2} + \left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)^{2}\right]^{-(1/2)}
\tag{4.15}
$$

for $n \ge 0$ and by

$$
A_{m,-1,2} = 2^{-(1/2)}\pi^{-(1/4)}
\tag{4.16}
$$

for $n = -1$. These normalization factors result in the orthonormality property

$$
\left(\mathbf{K}_{mnr}(\hat{y}), \mathbf{K}_{mn'r'}(\hat{y})\right) =
\begin{cases}
1, & (n', r') = (n, r) \\
0, & (n', r') \ne (n, r).
\end{cases}
\tag{4.17}
$$

The normality part of $(4.17)$ is easily confirmed by substituting $(4.11)$ into the left hand side and then using

$$
\int_{-\infty}^{\infty}\mathcal{H}_n(\hat{y})\mathcal{H}_{n'}(\hat{y})\,d\hat{y} =
\begin{cases}
1, & n' = n, \\
0, & n' \ne n
\end{cases}
\tag{4.18}
$$

to evaluate the three resulting integrals.

![](./pic/Schubert2006_fig2.png)

**Fig. 2.** $\mathcal{H}_n(\hat{y})$ for $n = 0, 1, 2, 3, 4$.

---

這一段是全文數學機器的核心：**把 $(4.6)$ 這個「對 $y$ 的常微分方程組」轉成「一組純代數方程」**。

**第一步：定義一個「對的」內積。** $(4.7)$ 把 $(4.3)$ 的係數收進算符 $\mathcal{L}$。接著在無因次經向座標 $\hat{y} = (\beta/\bar{c})^{1/2}y = \epsilon^{1/4}(y/a)$ 上定義內積 $(4.8)$，其中 $\epsilon = 4\Omega^{2}a^{2}/\bar{c}^{2}$ 是 **Lamb 參數（Lamb's parameter）**；取 $\bar{c} = 41.25\text{ m s}^{-1}$ 得 $\epsilon = 507.3$。

**這個內積不是隨便挑的——它是由 $(4.6)$ 對應的總能量原理「暗示」出來的**（注意第三項帶著 $1/\bar{c}^{2}$，正是位能項的權重）。挑對內積之後，關鍵性質就出現了：

$$
\mathcal{L}^{\dagger} = -\mathcal{L}
$$

也就是 **$\mathcal{L}$ 相對於這個內積是「反厄米（skew-Hermitian）」的**。這一步帶來兩個立即的紅利：

* **本徵值必為純虛數** → 寫成 $i\nu_{mnr}$，$\nu$ 是實頻率（無成長、無衰減，符合線性無耗散波動的物理）；
* **本徵函數構成完備、正交的集合**（只要沒有簡併），於是可以用它們當展開基底。

**第二步：解本徵問題，得到赤道波的頻散關係。** $(4.9)$ 的本徵值滿足 Matsuno (1966) 的**三次方程 $(4.10)$**。因為是三次方程，每組 $(m, n)$ 對應**三個根**，用 $r = 0, 1, 2$ 標記——這正對應到**西傳羅斯貝波、西傳慣性重力波、東傳慣性重力波**三類。

**幾個必須小心處理的特例：**

* **$n = 0$**：$(4.10)$ 可因式分解成 $(\epsilon^{1/2}\hat{\nu} + m)(\epsilon^{1/2}\hat{\nu}^{2} - m\hat{\nu} - 1) = 0$。根 $\epsilon^{1/2}\hat{\nu} = -m$ **必須捨棄**，因為它對應的本徵函數在 $\hat{y} \to \pm\infty$ 時發散（不是赤道捕捉波）。剩下兩根即 $r = 0$（**混合羅斯貝–重力波**）與 $r = 2$（**東傳慣性重力波**）。
* **Kelvin 波**：在 $(4.9)$ 中令 $V_{mnr} = 0$ 單獨求得，其本徵值 $\epsilon^{1/2}\hat{\nu} = m$ 可形式上視為 $(4.10)$ 在 $n = -1$ 的解，索引為 $r = 2$。**這就是為什麼後面所有級數的 $n$ 都從 $-1$ 開始數。**

**第三步：經向結構函數。** 本徵函數 $(4.11)$ 全部由 $\mathcal{H}_n(\hat{y})$ 組成，而 $\mathcal{H}_n$ 就是 $(4.12)$ 定義的**歸一化 Hermite 函數**（Hermite 多項式乘上高斯包絡）。$(4.13)$、$(4.14)$ 分別是它的遞迴關係與微分關係——注意 $\mathcal{H}_n$ 的微分**仍然只用到 $\mathcal{H}_{n\pm1}$**，這正是後面所有推導能保持封閉的原因。

作者還給了一個**很實用的數值建議**：要算 $\mathcal{H}_n$，應該直接用 $(4.13)$ 對 $\mathcal{H}_n$ 遞迴，而**不要**先算 $H_n$ 再套 $(4.12)$——因為後者會顯式碰到 $2^{n}n!$，$n$ 一大就溢位。（本文實作要遞迴到 $n = 200$，這個細節是必要的。）

$(4.15)$、$(4.16)$ 是歸一化常數 $A_{mnr}$，$(4.17)$ 則是由此得到的**正交歸一性**——這是把 $(4.6)$ 化成代數方程的最後一塊拼圖。""")

# --------------------------------------------------- 4（三）解的組裝與物理場還原
CELLS.append(r"""#### （承 §4）解的組裝、物理空間場的還原，與 Figs. 3–6

It should be noted that there is a degeneracy for the zonally symmetric Rossby modes (i.e., for $m = 0$, $n > 0$, $r = 0$), in which case $(4.11)$ is indeterminant because both $m$ and $\hat{\nu}_{0n0}$ vanish. However, orthonormal eigenfunctions are easily constructed in this case, as discussed in Appendix A. Because of the orthonormality and completeness of the eigenfunctions $\mathbf{K}_{mnr}(\hat{y})$, we can set up the transform pair [*Silva Dias et al.*, $1983$; *DeMaria*, $1985$]

$$
\hat{\eta}_{mnr} = \left(\hat{\boldsymbol{\eta}}_m(\hat{y}), \mathbf{K}_{mnr}(\hat{y})\right),
\tag{4.19}
$$

$$
\hat{\boldsymbol{\eta}}_m(\hat{y}) = \sum_{n=-1}^{\infty}\sum_{r}\hat{\eta}_{mnr}\mathbf{K}_{mnr}(\hat{y}),
\tag{4.20}
$$

where $\hat{\eta}_{mnr}$ are the scalar coefficients in the normal mode expansion of the vector $\hat{\boldsymbol{\eta}}_m(\hat{y})$. Note that $(4.19)$ can be obtained by taking the inner product of $(4.20)$ with $\mathbf{K}_{mn'r'}(\hat{y})$ and using the orthonormality property $(4.17)$.

We now have the tools necessary to solve $(4.6)$. Taking the inner product of $(4.6)$ with the eigenfunction $\mathbf{K}_{mnr}(\hat{y})$, and then using $(\mathcal{L}\hat{\boldsymbol{\eta}}_m, \mathbf{K}_{mnr}) = -(\hat{\boldsymbol{\eta}}_m, \mathcal{L}\mathbf{K}_{mnr}) = -(\hat{\boldsymbol{\eta}}_m, i\nu_{mnr}\mathbf{K}_{mnr}) = i\nu_{mnr}\hat{\eta}_{mnr}$, we can reduce our ordinary differential Eq. $(4.6)$ to the system of algebraic equations

$$
\hat{\eta}_{mnr} = \frac{\kappa\hat{Q}_{mnr}}{\alpha + i\left(\nu_{mnr} - (cm/a)\right)},
\tag{4.21}
$$

where $\hat{Q}_{mnr} = (\hat{\mathbf{Q}}_m, \mathbf{K}_{mnr})$. The inner product $(\hat{\mathbf{Q}}_m, \mathbf{K}_{mnr})$ is derived using the integral given in Appendix B. Using the result $(B.1)$ twice, once with $n$ replaced by $n + 1$ and once with $n$ replaced by $n - 1$, we can write $\hat{Q}_{mnr}$ as

$$
\begin{aligned}
\hat{Q}_{mnr} = &\ \frac{A_{mnr}\epsilon^{1/2}\pi Q_0 a_0 b_0}{2\bar{c}a^{2}[\pi^{2} - (ma_0/a)^{2}]}\frac{\sin(ma_0/a)}{(ma_0/a)}\left(\frac{2\pi}{2 + \hat{b}_0^{2}}\right)^{1/2}\exp\!\left(\frac{\hat{b}_0^{2}\hat{y}_0^{2}}{4 - \hat{b}_0^{4}}\right) \\[2mm]
&\times \left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\frac{2 - \hat{b}_0^{2}}{2 + \hat{b}_0^{2}}\right)^{(n+1)/2}\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}\!\left(\frac{2\hat{y}_0}{(4 - \hat{b}_0^{4})^{1/2}}\right)\right. \\[2mm]
&\qquad \left. -\left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\frac{2 - \hat{b}_0^{2}}{2 + \hat{b}_0^{2}}\right)^{(n-1)/2}\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\!\left(\frac{2\hat{y}_0}{(4 - \hat{b}_0^{4})^{1/2}}\right)\right]
\end{aligned}
\tag{4.22}
$$

for $n \ge 0$, and as

$$
\hat{Q}_{mnr} = \frac{A_{mnr}\epsilon^{1/4}\pi Q_0 a_0 b_0}{2\bar{c}a^{2}[\pi^{2} - (ma_0/a)^{2}]}\frac{\sin(ma_0/a)}{(ma_0/a)}\left(\frac{2\pi}{2 + \hat{b}_0^{2}}\right)^{1/2}\exp\!\left(-\frac{\hat{y}_0^{2}}{2 + \hat{b}_0^{2}}\right).
\tag{4.23}
$$

for the Kelvin wave ($n = -1$, $r = 2$). After $\hat{\eta}_{mnr}$ is computed from $(4.21)$–$(4.23)$, the physical space fields $u, v, \phi$ can be recovered by making use of $(4.20)$, followed by the inverse Fourier transform in $\xi$, i.e.,

$$
\begin{pmatrix}u(\xi, y, z) \\ v(\xi, y, z) \\ \phi(\xi, y, z)\end{pmatrix}
= Z(z)\sum_{m=-\infty}^{\infty}\sum_{n=-1}^{\infty}\sum_{r}\hat{\eta}_{mnr}
\begin{pmatrix}U_{mnr}(\hat{y}) \\ V_{mnr}(\hat{y}) \\ \Phi_{mnr}(\hat{y})\end{pmatrix}e^{im\xi/a}.
\tag{4.24}
$$

In addition, the potential vorticity field can be recovered from

$$
q(\xi, y, z) = Z(z)\sum_{m=-\infty}^{\infty}\sum_{n=-1}^{\infty}\sum_{r}\hat{q}_{mnr}\mathcal{H}_n(\hat{y})\, e^{im\xi/a},
\tag{4.25}
$$

where

$$
\hat{q}_{mnr} = A_{mnr}\left(\frac{m^{2} - \epsilon\hat{\nu}_{mnr}^{2}}{a\hat{\nu}_{mnr}}\right)\hat{\eta}_{mnr}.
\tag{4.26}
$$

A simple confirmation of $(4.25)$ and $(4.26)$ is obtained by noting that $(4.9)$ implies that $i\nu_{mnr}[i(m/a)V_{mnr} - dU_{mnr}/dy - (\beta/\bar{c}^{2})y\Phi_{mnr}] = \beta V_{mnr}$ and then using the second entry in $(4.11)$ for $V_{mnr}$ on the right hand side. According to $(4.25)$ and $(4.26)$, the physical space potential vorticity field is a superposition of the potential vorticity associated with all wave types except for the Kelvin wave, which has zero potential vorticity since the $m^{2} - \epsilon\hat{\nu}_{mnr}^{2}$ term in $(4.26)$ vanishes. Although equatorial $\beta$-plane dynamics differs from midlatitude $f$-plane dynamics in the sense that inertia-gravity waves have zero potential vorticity on the midlatitude $f$-plane but not on the equatorial $\beta$-plane, the contribution of the equatorial $\beta$-plane inertia-gravity waves to the potential vorticity tends to be quite small, especially for the higher zonal wavenumbers, because for inertia-gravity waves $m^{2} - \epsilon\hat{\nu}_{mnr}^{2}$ decreases and $|\hat{\nu}_{mnr}|$ increases as $m$ increases.

Using $(4.4)$, $(4.11)$ and $(4.14)$ the physical space vertical log-pressure velocity can be recovered from

$$
w(\xi, y, z) = \frac{Z'(z)}{R\Gamma}\sum_{m=-\infty}^{\infty}\sum_{n=-1}^{\infty}\sum_{r}i\nu_{mnr}\hat{\eta}_{mnr}\Phi_{mnr}(\hat{y})\, e^{im\xi/a}.
\tag{4.27}
$$

For later use we note that the vertical log-pressure velocity $w = Dz/Dt$ is related to the vertical $p$-velocity $\omega = Dp/Dt$ by $\omega = -p_0 e^{-z}w$.

All the model results shown in this section have been constructed by numerical evaluation of $(4.24)$, $(4.25)$ and $(4.27)$, which involves a superposition of zonal wavenumbers (sum over $m$), meridional wavenumbers (sum over $n$), and wave types (sum over $r$). In our examples the spectral coefficients $\hat{\eta}_{mnr}$ decay exponentially with $n$ for all choices of $m$, which enables us to truncate the spectral solution at $n = N$ with a specified degree of accuracy. In general, $N = 200$ gives accurate results.

Using the parameters listed in Table 1, the 850 hPa wind and geopotential fields computed from $(4.24)$ are shown in the top panel of Fig. 3 for $y_0 = 0$ and in the top panel of Fig. 5 for $y_0 = 450\text{ km}$. The choice of parameters describing the speed, size, and magnitude of the forcing was guided by the observational analyses of [*Hendon and Salby*, $1994$], [*Lin and Johnson*, $1996$b] and [*Kiladis et al.*, $2005$]. The choice of 850 hPa as the display level is arbitrary. According to the profile of $Z(z)$ shown in Fig. 1, upper tropospheric fields have the opposite sign and approximately twice the magnitude of the lower tropospheric fields. An interesting property of these simple linear solutions is that the lower tropospheric maximum westerly winds in the wake of the convective envelope are stronger than the lower tropospheric maximum easterly winds ahead of the convection. For example, in Fig. 3 the maximum 850 hPa westerly flow is $3.7\text{ m s}^{-1}$ while the maximum easterly flow is $1.6\text{ m s}^{-1}$. In Fig. 5 the corresponding values are $4.2\text{ m s}^{-1}$ and $1.4\text{ m s}^{-1}$. These wind speeds, the degree of asymmetry between westerlies and easterlies, and the larger zonal extent of the easterlies compared to the westerlies all agree well with the observed MJO composite presented by [*Kiladis et al.*, $2005$, their Fig. 3]. The remaining panels of Figs. 3 and 5 show the decomposition of the total fields into Rossby modes ($r = 0$ with $n \ge 1$), inertia-gravity modes ($r = 1, 2$ with $n \ge 1$ and $r = 2$ with $n = 0$), and Kelvin modes ($r = 2$ with $n = -1$). We have not plotted the contribution from mixed Rossby-gravity modes ($r = 0$ with $n = 0$) since it vanishes when $y_0 = 0$ and is very small when $y_0 = 450\text{ km}$.

![](./pic/Schubert2006_fig3.png)

**Fig. 3.** The upper panel shows the geopotential height anomaly and winds at 850 mb for $y_0 = 0$ and for the remaining parameters listed in Table 1. The remaining three panels show respectively the contributions made by Rossby waves, inertia-gravity waves, and Kelvin waves.

The 850 hPa potential vorticity field computed from $(4.25)$ and the 395 hPa vertical motion field computed from $(4.27)$ are shown in the top two panels of Fig. 4 for $y_0 = 0$ and in the top two panels of Fig. 6 for $y_0 = 450\text{ km}$. The bottom two panels of Figs. 4 and 6 show the decomposition of the vertical motion field into inertia-gravity waves and Kelvin waves (contributions from other modes are small). We have not shown the decomposition of the PV field because it is essentially entirely due to Rossby waves.

![](./pic/Schubert2006_fig4.png)

**Fig. 4.** The upper panel shows the 850 hPa potential vorticity anomaly $q$, with a contour interval of $1\times10^{-6}\text{ s}^{-1}$. The second panel shows the vertical $p$-velocity, $\omega$, at 395 hPa, with a contour interval of $30\text{ hPa day}^{-1}$ in the region of rising motion (dashed contours), and a contour interval of $0.5\text{ hPa day}^{-1}$ in the region of sinking motion (solid contours). The third and fourth panels show the respective contributions of inertia-gravity waves and Kelvin waves to the vertical motion field. Results in this figure are for $y_0 = 0$.

Several notable features are apparent from Figs. 3–6. The total $u, v, \phi$ fields are composed of Rossby waves on the west side of the source, Kelvin waves on the east side, with "slaved" inertia-gravity waves providing low-level convergence near the source. The PV anomaly patterns and the associated equatorial trough shear zones are zonally elongated because of the eastward movement of the convective envelope and the equatorward advection of the basic state PV in the wake of the convective envelope. As the center of the convective envelope is shifted off the equator there is very little change in the response east of the forcing. In contrast, the response west of the forcing becomes biased to the northern hemisphere. In particular, the PV anomaly is nearly twice as strong in the northern hemisphere when $y_0 = 450\text{ km}$.

![](./pic/Schubert2006_fig5.png)

**Fig. 5.** Same as Fig. 3, but with the center of the convective forcing shifted north of the equator ($y_0 = 450\text{ km}$).

![](./pic/Schubert2006_fig6.png)

**Fig. 6.** Same as Fig. 4, but with the center of the convective forcing shifted north of the equator ($y_0 = 450\text{ km}$).

It is interesting to interpret Figs. 3–6 in terms of the ITCZ, a concept that can be associated with a variety of observing methods and hence a variety of meteorological fields, e.g., geopotential anomalies, vorticity, divergence, cloudiness, and rainfall. Since the lower tropospheric geopotential anomalies are negative and the balanced flow is cyclonic, the terms "equatorial trough zone" and "equatorial trough shear zone" are sometimes used. Our model does not explicitly describe cloud processes and boundary layer dynamics. However, it does produce equatorial trough zones and zonally elongated vorticity strips. We shall take the liberty of calling these "ITCZs", under the assumption that, in a more complete model, low-level cyclonic vorticity would produce boundary layer convergence, Ekman pumping, cloudiness, and rain. According to this interpretation, a convective envelope centered on the equator produces a symmetric double ITCZ in its wake, while a convective envelope centered several hundred kilometers off the equator still produces a double ITCZ but with a bias toward the hemisphere to which the convection is shifted. In this way convection can be enhanced away from the equator in the MJO wake, even when the maximum sea surface temperature is at the equator. This is consistent with the observational study of [*Liebmann et al.*, $1994$], who found that tropical depressions, tropical storms, and typhoons preferentially develop in the large-scale low level cyclonic vorticity anomalies that form westward and poleward of the MJO convective envelope. The general tendency for double ITCZs to form even when the maximum sea surface temperature lies on the equator probably plays an important role in the Indian and western Pacific Oceans. In contrast, the formation of the ITCZ north of the equator in the Atlantic and eastern Pacific Oceans is associated with upwelling patterns, shallow thermocline depths, and cold sea surface temperatures at the equator [*Waliser and Somerville*, $1994$; *Philander et al.*, $1996$; *Lietzke et al.*, $2001$].

---

**簡併的處理**：緯向對稱的羅斯貝模態（$m = 0$、$n > 0$、$r = 0$）會讓 $(4.11)$ 變成 $0/0$ 的不定式（因為 $m$ 與 $\hat{\nu}_{0n0}$ 同時為零）。作者把這個特例的處理放進 Appendix A（用 l'Hôpital 法則取 $m \to 0$ 的極限）。

**把微分方程壓成代數方程**：靠著本徵函數的正交完備性，建立轉換對 $(4.19)$–$(4.20)$，再把 $(4.6)$ 與 $\mathbf{K}_{mnr}$ 做內積。這裡用到反厄米性質 $(\mathcal{L}\hat{\boldsymbol{\eta}}_m, \mathbf{K}_{mnr}) = -(\hat{\boldsymbol{\eta}}_m, \mathcal{L}\mathbf{K}_{mnr}) = i\nu_{mnr}\hat{\eta}_{mnr}$，於是常微分方程 $(4.6)$ 就**塌縮成一行代數式 $(4.21)$**：

$$
\hat{\eta}_{mnr} = \frac{\kappa\hat{Q}_{mnr}}{\alpha + i\left(\nu_{mnr} - cm/a\right)}
$$

這條式子的物理讀法非常直觀——**它就是一個受迫阻尼振子的響應函數**：

* 分子是**強迫投影到該模態上的分量** $\hat{Q}_{mnr}$；
* 分母的實部 $\alpha$ 是**阻尼**；
* 分母的虛部 $\nu_{mnr} - cm/a$ 是**該模態的自然頻率與強迫移動頻率之差**。當某個波模的相速接近對流的移速 $c$ 時（$\nu_{mnr} \approx cm/a$），分母僅剩 $\alpha$，**該模態就被「共振」放大**。這正是「為什麼移動熱源會選擇性地激發出特定的赤道波」的數學根源。

$(4.22)$、$(4.23)$ 則把 $\hat{Q}_{mnr}$ 明確寫出來（其中 $\hat{b}_0 = \epsilon^{1/4}(b_0/a)$、$\hat{y}_0 = \epsilon^{1/4}(y_0/a)$ 是無因次化的對流寬度與偏移量），推導所用的積分見 Appendix B。

**還原物理空間**：$(4.24)$ 還原 $u, v, \phi$，$(4.25)$–$(4.26)$ 還原 PV，$(4.27)$ 還原垂直速度 $w$（並註明 $\omega = -p_0 e^{-z}w$ 才是常見的 $p$ 座標垂直速度）。

$(4.26)$ 裡藏著本文後半段的關鍵事實：

$$
\hat{q}_{mnr} \propto \left(m^{2} - \epsilon\hat{\nu}_{mnr}^{2}\right)
$$

* **Kelvin 波的 PV 恰好為零**——因為 Kelvin 波的頻散關係就是 $\epsilon^{1/2}\hat{\nu} = m$，代入括號直接歸零。**這件事會在第 6 節變成「可逆性原理救不回對流東側流場」的根本原因。**
* 赤道 $\beta$ 平面與中緯度 $f$ 平面有一個差別：$f$ 平面上慣性重力波的 PV 為零，**赤道 $\beta$ 平面上則不為零**。不過作者指出其貢獻**很小**，尤其在高緯向波數：因為 $m$ 增大時 $m^{2} - \epsilon\hat{\nu}_{mnr}^{2}$ 變小、$|\hat{\nu}_{mnr}|$ 變大，分子小分母大，兩頭夾殺。

**數值實作**：$\hat{\eta}_{mnr}$ 隨 $n$ **指數衰減**，因此可以在 $n = N$ 截斷；作者指出 **$N = 200$ 已能給出準確結果**。

**結果解讀（Figs. 3–6）：**

* **東西風不對稱**：對流尾流（西側）的低層最大西風，**強於**對流前方（東側）的低層最大東風。$y_0 = 0$ 時為 $3.7\text{ m s}^{-1}$ vs. $1.6\text{ m s}^{-1}$；$y_0 = 450\text{ km}$ 時為 $4.2\text{ m s}^{-1}$ vs. $1.4\text{ m s}^{-1}$。這個風速大小、不對稱程度、以及「東風的緯向範圍比西風寬」的特徵，**都與 Kiladis et al. (2005) 的 MJO 觀測合成場吻合**。
* **波模分工**：$u, v, \phi$ 總場 = 熱源**西側的羅斯貝波** ＋ **東側的 Kelvin 波** ＋ 熱源附近提供低層輻合的「**受役（slaved）慣性重力波**」。混合羅斯貝–重力波（$r=0$, $n=0$）在 $y_0 = 0$ 時**恰好為零**、在 $y_0 = 450\text{ km}$ 時也極小，因此沒有畫出。
* **上下反號**：依圖 1 的 $Z(z)$ 剖面，**對流層高層的場與低層反號、且量值約為兩倍**。
* **偏移的效果**：把對流中心從赤道移到 $y_0 = 450\text{ km}$，**東側響應幾乎不變**，但**西側響應明顯偏向北半球**——北半球的 PV 距平**強了將近一倍**。
* **PV 幾乎全由羅斯貝波貢獻**（所以作者連 PV 的波模分解都省了）。PV 距平帶之所以被拉得那麼長，是**東移的對流包絡** ＋ **尾流中把基本態 PV 往赤道方向平流**兩件事合力造成的。

**與 ITCZ 的連結（本節的物理收尾）：**

模式並沒有顯式描述雲物理與邊界層動力，但它**確實造出了赤道槽區與被拉長的渦度帶**。作者於是「借用」ITCZ 這個名字——假設在更完整的模式裡，低層氣旋式渦度會導致**邊界層輻合 → Ekman pumping → 雲量 → 降雨**。在這個詮釋下：

* 對流中心**在赤道上** → 尾流中生成**對稱的雙 ITCZ**；
* 對流中心**偏離赤道數百公里** → **仍是雙 ITCZ，但偏向對流所在的那個半球**。

**這帶來一個重要推論：即使最高海表溫度就在赤道上，MJO 尾流仍可以把對流增強在遠離赤道的地方。** 這與 Liebmann et al. (1994) 的觀測一致——熱帶低壓、熱帶風暴與颱風**偏好生成於 MJO 對流包絡「西側且偏極側」的大尺度低層氣旋式渦度距平中**。

作者也小心地區分了兩種 ITCZ 成因：印度洋與西太平洋的雙 ITCZ 傾向，很可能就是上述動力機制；**而大西洋與東太平洋「ITCZ 偏在赤道以北」則另有其因**——與湧升流型態、淺溫躍層、赤道冷海溫有關 [*Waliser and Somerville*, $1994$; *Philander et al.*, $1996$; *Lietzke et al.*, $2001$]。""")

if __name__ == "__main__":
    n = append("a_paper.jsonl", CELLS)
    print("paper_03 -> a_paper.jsonl  cells=%d" % n)
