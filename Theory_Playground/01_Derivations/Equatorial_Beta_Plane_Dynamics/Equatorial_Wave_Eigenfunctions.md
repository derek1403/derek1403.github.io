# Equatorial Wave Eigenfunctions (赤道波本徵函數、歸一化常數與正交歸一)

+++

## 證明目標:

本徵函數的**形式**已在 [project2_1](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/project/project2/project2_1.html) 證過，
本篇補上論文真正需要的三件事：**記法翻譯**、**歸一化常數**、**正交歸一性**，外加簡併特例。

* (a) 本徵函數的顯式形式（$n \ge 0$）：

$$\mathbf{K}_{mnr}(\hat{y}) = A_{mnr}
\begin{pmatrix}
\epsilon^{1/4}\left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\dfrac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\dfrac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right] \cr
-i\left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)\mathcal{H}_{n} \cr
\bar{c}\,\epsilon^{1/4}\left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\dfrac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\dfrac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]
\end{pmatrix}$$

* (b) 使 $\left(\mathbf{K}_{mnr},\ \mathbf{K}_{mnr}\right) = 1$ 的歸一化常數（$n \ge 0$）：

$$A_{mnr} = \left[\epsilon^{1/2}\left(n+1\right)\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)^{2} + \epsilon^{1/2}n\left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)^{2} + \left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)^{2}\right]^{-1/2}$$

* (c) Kelvin 波（$n = -1$、$r = 2$）的歸一化常數：

$$A_{m,-1,2} = 2^{-1/2}\pi^{-1/4}$$

* (d) 正交歸一性：

$$\left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) =
\begin{cases}
1, & \left(n', r'\right) = \left(n, r\right) \\
0, & \left(n', r'\right) \neq \left(n, r\right)
\end{cases}$$

* (e) 簡併特例 —— 緯向對稱的羅斯貝模態（$m = 0$、$n > 0$、$r = 0$）：

$$\mathbf{K}_{0n0}(\hat{y}) = \left(2n + 1\right)^{-1/2}
\begin{pmatrix}
\left(\dfrac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\dfrac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1} \cr
0 \cr
\bar{c}\left[\left(\dfrac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\dfrac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]
\end{pmatrix}$$

* (f) (e) 的本徵函數對應**地轉平衡的緯向流**：

$$\beta y\,U_{0n0} + \frac{d\Phi_{0n0}}{dy} = 0$$

* 註：(a)–(e) 就是 [Schubert & Masarik (2006)](../../06_References/Tropical_wave_dynamics/Schubert2006-Potential_vorticity_aspects_of_the_MJO/Potential_vorticity_aspects_of_the_MJO.ipynb) 的 $(4.11)$、$(4.15)$、$(4.16)$、$(4.17)$、$(A.1)$。
* 註：$\mathcal{H}_n$ 的所有性質（遞迴、微分、正交歸一）都引用本庫 [Hermite Functions and Recurrence](../Differential_Equations/Hermite_Functions_and_Recurrence.md) 與 [Hermite Orthonormality and Oscillator Eigenvalue](../Differential_Equations/Hermite_Orthonormality_and_Oscillator_Eigenvalue.md)，本篇不重證。

+++

## 假設與已知 (Assumptions & Preliminaries)

* **【已知 1】 [赤道波本徵函數（project2_1 記法）(Equatorial wave eigenfunctions in project2_1 notation)](https://derek1403.github.io/PC-NTU/Advanced-Atmospheric-Dynamics/_build/html/project/project2/project2_1.html)：** 以 project2_1 記法寫出的三個場：經向速度只含單一個 Hermite 多項式 $H_n$，而緯向速度與重力位則是 $H_{n+1}$ 與 $H_{n-1}$ 的線性組合 ─ 這個「差一階」的結構正是後面要整批換成歸一化 Hermite 函數的對象。（已於 Advanced Atmospheric Dynamics 的 project2_1【證明 2】完整證明，此處直接引用。）

  * (a) 經向速度：

    $$\hat{v} = i\left(\omega^{2} - k^{2}\right)A\,e^{-\hat{y}^{2}/2}H_n(\hat{y})$$

  * (b) 緯向速度：

    $$\hat{u} = -A\,e^{-\hat{y}^{2}/2}\left[\frac{1}{2}\left(\omega + k\right)H_{n+1} + n\left(\omega - k\right)H_{n-1}\right]$$

  * (c) 重力位：

    $$\hat{\phi} = -A\,e^{-\hat{y}^{2}/2}\left[\frac{1}{2}\left(\omega + k\right)H_{n+1} - n\left(\omega - k\right)H_{n-1}\right]$$

  * $\omega,\ k$ : project2_1 記法的無因次頻率與緯向波數 (Dimensionless frequency and wavenumber) $[\text{無單位}]$
  * $H_n$ : 第 $n$ 階 Hermite 多項式 (Hermite polynomial) $[\text{無單位}]$
  * $A$ : 未定的整體常數 (Undetermined overall constant) $[\text{無單位}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\hat{u},\ \hat{v}$ : 緯向、經向風的水平結構函數 (Horizontal structure functions of the velocities) $[\text{m}\cdot\text{s}^{-1}]$
  * $\hat{\phi}$ : 擾動位勢的水平結構函數 (Horizontal structure function of the perturbation geopotential) $[\text{m}^{2}\cdot\text{s}^{-2}]$
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$

* **【已知 2】 [記法對照與頻散關係 (Notation mapping and dispersion relation)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Matsuno_Dispersion_Relation.html#a-proof-notation-mapping-and-scale-restoration)：** project2_1 與 Schubert 兩套記法的換算，以及換算後的頻散關係；(c) 另外給出 Kelvin 波這個特例 ─ 它的經向速度恆為零，必須單獨當一支處理。（已於本庫 [Matsuno Dispersion Relation](Matsuno_Dispersion_Relation.md) 完整證明，此處直接引用。）

  * (a) 記法換算：

    $$\omega = \epsilon^{1/4}\hat{\nu}_{mnr}, \qquad k = \epsilon^{-1/4}m$$

  * (b) 頻散關係：

    $$\epsilon\hat{\nu}_{mnr}^{2} - m^{2} - \frac{m}{\hat{\nu}_{mnr}} = \epsilon^{1/2}\left(2n + 1\right)$$

  * (c) Kelvin 波的本徵值與其解的結構（$V = 0$、$\Phi = \bar{c}U$、$U \propto e^{-\hat{y}^{2}/2}$）：

    $$\epsilon^{1/2}\hat{\nu}_{m,-1,2} = m$$

  * $\hat{\nu}_{mnr}$ : Schubert 記法的無因次頻率 (Dimensionless frequency) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $\omega,\ k$ : project2_1 記法的無因次頻率與緯向波數 (Dimensionless frequency and wavenumber) $[\text{無單位}]$

* **【已知 3】 [歸一化 Hermite 函數及其常數比 (Normalized Hermite functions and the constant ratios)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Hermite_Functions_and_Recurrence.html#assumptions-preliminaries)：** 歸一化 Hermite 函數的定義與它的四條運算規則：相鄰歸一化常數的比值、乘以 $\hat{y}$ 的遞迴、微分關係，以及最低階的顯式 ─ 有了這些，$H_n$ 的組合才能整批換成 $\mathcal{H}_n$ 而不留下係數尾巴。（已於本庫 [Hermite Functions and Recurrence](../Differential_Equations/Hermite_Functions_and_Recurrence.md) 完整證明，此處直接引用。）

  * (a) 定義：

    $$\mathcal{H}_n(\hat{y}) = c_n\,H_n(\hat{y})\,e^{-\hat{y}^{2}/2}, \qquad c_n = \left(\pi^{1/2}2^{n}n!\right)^{-1/2}$$

  * (b) 相鄰常數比：

    $$\frac{c_n}{c_{n+1}} = \left[2\left(n+1\right)\right]^{1/2}, \qquad \frac{c_n}{c_{n-1}} = \left[\frac{1}{2n}\right]^{1/2}$$

  * (c) 遞迴關係：

    $$\hat{y}\,\mathcal{H}_n = \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}$$

  * (d) 微分關係：

    $$\frac{d\mathcal{H}_n}{d\hat{y}} = -\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}$$

  * (e) 最低階顯式：

    $$\mathcal{H}_0(\hat{y}) = \pi^{-1/4}e^{-\hat{y}^{2}/2}$$

  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $c_n$ : 歸一化常數 (Normalization constant) $[\text{無單位}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $H_n$ : 第 $n$ 階 Hermite 多項式 (Hermite polynomial) $[\text{無單位}]$

* **【已知 4】 [Hermite 函數的正交歸一性 (Orthonormality of the Hermite functions)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Differential_Equations/Hermite_Orthonormality_and_Oscillator_Eigenvalue.html#d-proof-orthonormality)：** 不同階的歸一化 Hermite 函數在全實軸上互相正交、同階積分為一 ─ 這是把本徵函數的模長算成有限值、進而定出歸一化常數 $A_{mnr}$ 的唯一工具。（已於本庫 [Hermite Orthonormality and Oscillator Eigenvalue](../Differential_Equations/Hermite_Orthonormality_and_Oscillator_Eigenvalue.md)【證明 (d)】完整證明，此處直接引用。）

  $$\int_{-\infty}^{\infty}\mathcal{H}_n(\hat{y})\,\mathcal{H}_{n'}(\hat{y})\,d\hat{y} = \begin{cases}1, & n' = n \\ 0, & n' \neq n\end{cases}$$

  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$

* **【已知 5】 [能量內積與本徵函數的正交性 (Energy inner product and orthogonality of the eigenfunctions)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Energy_Inner_Product_and_Skew_Hermitian_Operator.html#e-proof-pure-imaginary-eigenvalues-and-orthogonal-eigenfunctions)：** 能量內積的定義（第三分量帶 $1/\bar{c}^{2}$ 的權重），以及它給出的正交性：本徵值相異的兩個本徵函數在此內積下正交 ─ 這是把任意場展開成模態時各項互不干擾的保證。（已於本庫 [Energy Inner Product and the Skew-Hermitian Operator](Energy_Inner_Product_and_Skew_Hermitian_Operator.md) 完整證明，此處直接引用。）

  * (a) 內積：

    $$\left(\mathbf{f},\ \mathbf{g}\right) = \int_{-\infty}^{\infty}\left(f_1g_1^{*} + f_2g_2^{*} + \frac{1}{\bar{c}^{2}}f_3g_3^{*}\right)d\hat{y}$$

  * (b) 相異本徵值的本徵函數互相正交：

    $$\left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) = 0 \qquad \left(\nu_{mnr} \neq \nu_{mn'r'}\right)$$

  * $\mathbf{f},\ \mathbf{g}$ : 複數三分量向量函數 (Complex three-component vector functions) $[\text{依分量而定}]$
  * $f_j,\ g_j$ : 內積中的兩個三分量向量函數 (Two three-component vector functions) $[\text{依分量而定}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\mathbf{K}_{mnr}$ : 本徵函數 (Eigenfunction) $[\text{依分量而定}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$
  * $\nu_{mnr}$ : 第 $(m, n, r)$ 個本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數

* **【已知 6】 [高斯積分 (Gaussian integral)](https://dlmf.nist.gov/7.4#E1)：** 高斯函數在全實軸上的積分值為 $\pi^{1/2}$，這是所有 Hermite 歸一化常數的來源。（標準結果，此處直接引用。）

  $$\int_{-\infty}^{\infty}e^{-\hat{y}^{2}}\,d\hat{y} = \pi^{1/2}$$

  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$

* **【已知 7】 [本徵值問題與算符 (Eigenvalue problem and the operator)](https://derek1403.github.io/Theory_Playground/_build/html/01_Derivations/Equatorial_Beta_Plane_Dynamics/Fourier_Transform_to_Shallow_Water_System.html#e-proof-vector-form)：** 本徵值問題的第二分量：經向速度由科氏項 $\beta y\,U$ 與位勢的經向梯度兩者的合力決定 ─ 本篇用它把 $V_{mnr}$ 的顯式解出來。（已於本庫 [Fourier Transform to the Shallow Water System](Fourier_Transform_to_Shallow_Water_System.md) 完整證明，此處只用到第二分量那一條。）

  $$\beta y\,U_{mnr} + \frac{d\Phi_{mnr}}{dy} = i\nu_{mnr}V_{mnr}$$

  * $U,\ V$ : 本徵函數的速度分量 (Velocity components of the eigenfunction) $[\text{無單位}]$
  * $\Phi$ : 本徵函數的位勢分量 (Geopotential component) $[\text{m}\cdot\text{s}^{-1}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 有因次經向座標 (Dimensional meridional coordinate) $[\text{m}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$
  * $\nu_{mnr}$ : 第 $(m, n, r)$ 個本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數
  * $i$ : 虛數單位 (Imaginary unit) $[\text{無單位}]$，$i^{2} = -1$

* **【假設 1】 本徵向量的規範自由度 (Gauge freedom of the eigenvector)：** 本徵函數可乘任意非零常數仍是本徵函數；本篇用這個自由度把 project2_1 的整體常數 $A$ 換成 Schubert 的 $A_{mnr}$，並把第三分量還原因次（乘上 $\bar{c}$）

  $$\mathbf{K}_{mnr} \to \sigma\,\mathbf{K}_{mnr} \quad \left(\sigma \neq 0\right)$$

  * $\sigma$ : 任意非零常數 (Arbitrary nonzero constant) $[\text{無單位}]$
  * $\mathbf{K}_{mnr}$ : 本徵函數 (Eigenfunction) $[\text{依分量而定}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$
  * 註：這個自由度**唯一**被【證明 (b)(c)】的歸一化條件用掉；剩下的只有一個整體相位，不影響任何物理量。

* **【假設 2】 非簡併 (Non-degeneracy)：** 【證明 (d)】的正交部分要求兩個模態的本徵值相異

  $$\nu_{mnr} \neq \nu_{mn'r'} \qquad \left(\left(n', r'\right) \neq \left(n, r\right)\right)$$

  * $\nu_{mnr}$ : 第 $(m, n, r)$ 個本徵頻率 (Eigenfrequency) $[\text{s}^{-1}]$，實數
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$
  * 註：唯一的例外是緯向對稱的羅斯貝模態（$m = 0$、$n > 0$、$r = 0$），它們全部有 $\nu_{0n0} = 0$。該情形由【證明 (e)】另外處理，其正交性直接由【已知 4】驗證。

* **【假設 3】 $m$ 暫時視為連續變數 (Treating $m$ as a continuous variable)：** 【證明 (e)】要取 $m \to 0$ 的極限，故暫時放寬 $m$ 的整數限制

  $$m \in \mathbb{R}$$

  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數

* **【定義 1】 上下行振幅 (Upper and lower branch amplitudes)：** 把【證明 (a)】括號裡反覆出現的兩個組合縮寫掉

  * (a) 上行振幅：

    $$\mathcal{P}_{mnr} \overset{\text{def}}{=} \left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\frac{n+1}{2}\right)^{1/2}$$

  * (b) 下行振幅：

    $$\mathcal{M}_{mnr} \overset{\text{def}}{=} \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\frac{n}{2}\right)^{1/2}$$

  * $\mathcal{P}_{mnr},\ \mathcal{M}_{mnr}$ : 上行、下行振幅 (Upper and lower branch amplitudes) $[\text{無單位}]$，皆為實數
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\hat{\nu}_{mnr}$ : Schubert 記法的無因次頻率 (Dimensionless frequency) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$

* **【推導 1】 兩套記法的三個組合 (Three combinations in the two notations)：** 把【已知 2】(a) 代進 project2_1 的三個因子

  * (a) 和：

    $$\begin{gather*}
    \omega + k &\overset{\text{已知 2(a)}}{=}& \epsilon^{1/4}\hat{\nu}_{mnr} + \epsilon^{-1/4}m \\
    &=& \epsilon^{-1/4}\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)
    \end{gather*}$$

  * (b) 差：

    $$\begin{gather*}
    \omega - k &\overset{\text{已知 2(a)}}{=}& \epsilon^{1/4}\hat{\nu}_{mnr} - \epsilon^{-1/4}m \\
    &=& \epsilon^{-1/4}\left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)
    \end{gather*}$$

  * (c) 平方差：

    $$\begin{gather*}
    \omega^{2} - k^{2} &\overset{\text{推導 1(a)(b)}}{=}& \epsilon^{-1/4}\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\cdot\epsilon^{-1/4}\left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right) \\
    &=& \epsilon^{-1/2}\left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)
    \end{gather*}$$

  * $\omega,\ k$ : project2_1 記法的無因次頻率與緯向波數 (Dimensionless frequency and wavenumber) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\hat{\nu}_{mnr}$ : Schubert 記法的無因次頻率 (Dimensionless frequency) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$

* **【推導 2】 Hermite 多項式換成歸一化 Hermite 函數 (Converting to the normalized Hermite functions)：** 這一步把 project2_1 的係數 $\frac{1}{2}$ 與 $n$ 恰好變成 Schubert 的兩個根號

  * (a) 上行項：

    $$\begin{gather*}
    \frac{1}{2}H_{n+1}\,e^{-\hat{y}^{2}/2} &\overset{\text{已知 3(a)}}{=}& \frac{1}{2}\frac{\mathcal{H}_{n+1}}{c_{n+1}} \\
    &=& \frac{1}{c_n}\cdot\frac{1}{2}\frac{c_n}{c_{n+1}}\,\mathcal{H}_{n+1} \\
    &\overset{\text{已知 3(b)}}{=}& \frac{1}{c_n}\cdot\frac{1}{2}\left[2\left(n+1\right)\right]^{1/2}\mathcal{H}_{n+1} \\
    &=& \frac{1}{c_n}\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1}
    \end{gather*}$$

  * (b) 下行項：

    $$\begin{gather*}
    n\,H_{n-1}\,e^{-\hat{y}^{2}/2} &\overset{\text{已知 3(a)}}{=}& n\frac{\mathcal{H}_{n-1}}{c_{n-1}} \\
    &=& \frac{1}{c_n}\cdot n\frac{c_n}{c_{n-1}}\,\mathcal{H}_{n-1} \\
    &\overset{\text{已知 3(b)}}{=}& \frac{1}{c_n}\cdot n\left[\frac{1}{2n}\right]^{1/2}\mathcal{H}_{n-1} \\
    &=& \frac{1}{c_n}\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}
    \end{gather*}$$

  * (c) 中央項：

    $$H_n\,e^{-\hat{y}^{2}/2} \overset{\text{已知 3(a)}}{=} \frac{1}{c_n}\mathcal{H}_n$$

  * $H_n$ : 第 $n$ 階 Hermite 多項式 (Hermite polynomial) $[\text{無單位}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $c_n$ : 歸一化常數 (Normalization constant) $[\text{無單位}]$
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$

* **【推導 3】 本徵函數三分量的範數 (Norms of the three components)：** 用【已知 4】把三個積分算掉；$\mathcal{H}_{n+1}$ 與 $\mathcal{H}_{n-1}$ 的交叉項正交而消失

  * (a) 第一分量：

    $$\begin{gather*}
    \int_{-\infty}^{\infty}\left|U_{mnr}\right|^{2}d\hat{y} &\overset{\text{定義 1(a)(b)}}{=}& A_{mnr}^{2}\,\epsilon^{1/2}\int_{-\infty}^{\infty}\left[\mathcal{P}_{mnr}\mathcal{H}_{n+1} + \mathcal{M}_{mnr}\mathcal{H}_{n-1}\right]^{2}d\hat{y} \\
    &\overset{\text{已知 4}}{=}& A_{mnr}^{2}\,\epsilon^{1/2}\left[\mathcal{P}_{mnr}^{2} + \mathcal{M}_{mnr}^{2}\right]
    \end{gather*}$$

  * (b) 第三分量（帶 $1/\bar{c}^{2}$ 權重，$\bar{c}$ 恰好約掉；括號內的減號在平方後不影響交叉項為零的結論）：

    $$\begin{gather*}
    \frac{1}{\bar{c}^{2}}\int_{-\infty}^{\infty}\left|\Phi_{mnr}\right|^{2}d\hat{y} &\overset{\text{定義 1(a)(b)}}{=}& A_{mnr}^{2}\,\epsilon^{1/2}\int_{-\infty}^{\infty}\left[\mathcal{P}_{mnr}\mathcal{H}_{n+1} - \mathcal{M}_{mnr}\mathcal{H}_{n-1}\right]^{2}d\hat{y} \\
    &\overset{\text{已知 4}}{=}& A_{mnr}^{2}\,\epsilon^{1/2}\left[\mathcal{P}_{mnr}^{2} + \mathcal{M}_{mnr}^{2}\right]
    \end{gather*}$$

  * (c) 第二分量：

    $$\begin{gather*}
    \int_{-\infty}^{\infty}\left|V_{mnr}\right|^{2}d\hat{y} &=& A_{mnr}^{2}\left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)^{2}\int_{-\infty}^{\infty}\mathcal{H}_n^{2}\,d\hat{y} \\
    &\overset{\text{已知 4}}{=}& A_{mnr}^{2}\left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)^{2}
    \end{gather*}$$

  * $U,\ V$ : 本徵函數的速度分量 (Velocity components of the eigenfunction) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $A$ : 未定的整體常數 (Undetermined overall constant) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\mathcal{P}_{mnr},\ \mathcal{M}_{mnr}$ : 上行、下行振幅 (Upper and lower branch amplitudes) $[\text{無單位}]$，皆為實數
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * $\Phi$ : 本徵函數的位勢分量 (Geopotential component) $[\text{m}\cdot\text{s}^{-1}]$
  * $\hat{\nu}_{mnr}$ : Schubert 記法的無因次頻率 (Dimensionless frequency) $[\text{無單位}]$
  * $A_{mnr}$ : 歸一化常數 (Normalization constant) $[\text{無單位}]$

* **【推導 4】 上下行振幅平方和的展開 (Expanding the sum of squared amplitudes)：** 把上下行振幅的平方和用【定義 1】的顯式形式攤開，湊出歸一化常數所需的分母 ─ 這段代數先算掉，主證明才不必在根號裡打轉。

  $$\begin{gather*}
  2\epsilon^{1/2}\left[\mathcal{P}_{mnr}^{2} + \mathcal{M}_{mnr}^{2}\right] &\overset{\text{定義 1(a)(b)}}{=}& 2\epsilon^{1/2}\left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)^{2}\frac{n+1}{2} + \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)^{2}\frac{n}{2}\right] \\
  &=& \epsilon^{1/2}\left(n+1\right)\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)^{2} + \epsilon^{1/2}n\left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)^{2}
  \end{gather*}$$

  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\mathcal{P}_{mnr},\ \mathcal{M}_{mnr}$ : 上行、下行振幅 (Upper and lower branch amplitudes) $[\text{無單位}]$，皆為實數
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $r$ : 波型指標 (Wave-type index) $[\text{無單位}]$
  * $\hat{\nu}_{mnr}$ : Schubert 記法的無因次頻率 (Dimensionless frequency) $[\text{無單位}]$

* **【推導 5】 羅斯貝分支在 $m \to 0$ 的漸近行為 (Asymptotics of the Rossby branch as $m \to 0$)：** 在 $m \to 0$ 的極限下，色散關係的主平衡落到 $-m/\hat{\nu}$ 這一項，於是頻率與上下行振幅都退化成只含 $n$ 的簡單比例；這是【證明 (e)】能取極限的前提

  * (a) 由【已知 2】(b)，$\hat{\nu} \to 0$ 時 $\epsilon\hat{\nu}^{2}$ 與 $m^{2}$ 皆為高階小量，主平衡落在 $-m/\hat{\nu}$ 這一項：

    $$\begin{gather*}
    \epsilon^{1/2}\left(2n + 1\right) &\overset{\text{已知 2(b)}}{=}& \epsilon\hat{\nu}_{0n0}^{2} - m^{2} - \frac{m}{\hat{\nu}_{0n0}} \\
    \epsilon^{1/2}\left(2n + 1\right) &\approx& -\frac{m}{\hat{\nu}_{0n0}} \\
    \epsilon^{1/2}\hat{\nu}_{0n0} &\approx& -\frac{m}{2n + 1}
    \end{gather*}$$

  * (b) 由 (a) 得上行組合的極限：

    $$\begin{gather*}
    \epsilon^{1/2}\hat{\nu}_{0n0} + m &\overset{\text{推導 5(a)}}{\approx}& m\left[1 - \frac{1}{2n+1}\right] \\
    &=& \frac{2nm}{2n + 1}
    \end{gather*}$$

  * (c) 同樣得下行組合的極限：

    $$\begin{gather*}
    \epsilon^{1/2}\hat{\nu}_{0n0} - m &\overset{\text{推導 5(a)}}{\approx}& -m\left[1 + \frac{1}{2n+1}\right] \\
    &=& -\frac{\left(2n + 2\right)m}{2n + 1}
    \end{gather*}$$

  * (d) 第二分量的係數是 $m$ 的二次小量，故相對於 (b)(c) 可捨棄：

    $$\begin{gather*}
    \epsilon\hat{\nu}_{0n0}^{2} - m^{2} &\overset{\text{推導 5(a)}}{\approx}& m^{2}\left[\frac{1}{\left(2n+1\right)^{2}} - 1\right] \\
    &\ll& \frac{2nm}{2n+1} \qquad \left(m \to 0\right)
    \end{gather*}$$

  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $\hat{\nu}_{mnr}$ : Schubert 記法的無因次頻率 (Dimensionless frequency) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數

* **【推導 6】 極限下的根號係數重組 (Regrouping the radical coefficients in the limit)：** 【推導 5】(b)(c) 的極限值配上【定義 1】的根號後，可以把共同因子 $\left[n\left(n+1\right)\right]^{1/2}$ 提出來，兩個根號恰好**互換**

  * (a) 上行項：

    $$\begin{gather*}
    \frac{2nm}{2n+1}\left(\frac{n+1}{2}\right)^{1/2} &=& \frac{2m}{2n+1}\cdot n\left(\frac{n+1}{2}\right)^{1/2} \\
    &=& \frac{2m}{2n+1}\left[n\left(n+1\right)\right]^{1/2}\left(\frac{n}{2}\right)^{1/2}
    \end{gather*}$$

  * (b) 下行項：

    $$\begin{gather*}
    \frac{\left(2n+2\right)m}{2n+1}\left(\frac{n}{2}\right)^{1/2} &=& \frac{2m}{2n+1}\cdot\left(n+1\right)\left(\frac{n}{2}\right)^{1/2} \\
    &=& \frac{2m}{2n+1}\left[n\left(n+1\right)\right]^{1/2}\left(\frac{n+1}{2}\right)^{1/2}
    \end{gather*}$$

  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $m$ : 緯向波數 (Zonal wavenumber) $[\text{無單位}]$，整數

* **【推導 7】 緯向對稱模態的 $\hat{y}$ 乘法 (Multiplication by $\hat{y}$ for the zonally symmetric mode)：** 把【已知 3】(c) 用在【證明 (e)】第一分量的括號上，$\mathcal{H}_n$ 項對消

  $$\begin{gather*}
  \hat{y}\left[\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]
  &\overset{\text{已知 3(c)}}{=}& \left(\frac{n}{2}\right)^{1/2}\left[\left(\frac{n+2}{2}\right)^{1/2}\mathcal{H}_{n+2} + \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n}\right] \\
  && - \left(\frac{n+1}{2}\right)^{1/2}\left[\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n} + \left(\frac{n-1}{2}\right)^{1/2}\mathcal{H}_{n-2}\right] \\
  &=& \left(\frac{n\left(n+2\right)}{4}\right)^{1/2}\mathcal{H}_{n+2} - \left(\frac{\left(n+1\right)\left(n-1\right)}{4}\right)^{1/2}\mathcal{H}_{n-2}
  \end{gather*}$$

  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$

* **【推導 8】 緯向對稱模態的微分 (Differentiation for the zonally symmetric mode)：** 把【已知 3】(d) 用在【證明 (e)】第三分量的括號上，同樣是 $\mathcal{H}_n$ 項對消

  $$\begin{gather*}
  \frac{d}{d\hat{y}}\left[\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]
  &\overset{\text{已知 3(d)}}{=}& \left(\frac{n}{2}\right)^{1/2}\left[-\left(\frac{n+2}{2}\right)^{1/2}\mathcal{H}_{n+2} + \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n}\right] \\
  && + \left(\frac{n+1}{2}\right)^{1/2}\left[-\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n} + \left(\frac{n-1}{2}\right)^{1/2}\mathcal{H}_{n-2}\right] \\
  &=& -\left(\frac{n\left(n+2\right)}{4}\right)^{1/2}\mathcal{H}_{n+2} + \left(\frac{\left(n+1\right)\left(n-1\right)}{4}\right)^{1/2}\mathcal{H}_{n-2}
  \end{gather*}$$

  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $n$ : 經向模態指標 (Meridional mode index) $[\text{無單位}]$
  * $\mathcal{H}_n$ : 歸一化 Hermite 函數 (Normalized Hermite function) $[\text{無單位}]$

* **【推導 9】 有因次地轉關係的無因次形式 (Dimensionless form of the geostrophic relation)：** 把【已知 7】的 $\beta y$ 與 $d/dy$ 換成 $\hat{y}$ 與 $d/d\hat{y}$，兩個係數恰好相同

  $$\begin{gather*}
  \beta y &\overset{\text{已知 2}}{=}& \frac{2\Omega}{a}\cdot\frac{a\,\hat{y}}{\epsilon^{1/4}} \\
  \beta y &=& \frac{2\Omega}{\epsilon^{1/4}}\hat{y} \\
  \frac{d}{dy} &\overset{\text{已知 2}}{=}& \frac{\epsilon^{1/4}}{a}\frac{d}{d\hat{y}} \\
  \bar{c}\frac{d}{dy} &\overset{\text{已知 2}}{=}& \frac{2\Omega a}{\epsilon^{1/2}}\cdot\frac{\epsilon^{1/4}}{a}\frac{d}{d\hat{y}} \\
  \bar{c}\frac{d}{dy} &=& \frac{2\Omega}{\epsilon^{1/4}}\frac{d}{d\hat{y}}
  \end{gather*}$$

  * $\Omega$ : 地球自轉角速度 (Earth's angular velocity) $[\text{s}^{-1}]$
  * $a$ : 地球半徑 (Earth's radius) $[\text{m}]$
  * $\beta$ : 赤道 $\beta$ 參數 (Equatorial beta parameter) $[\text{m}^{-1}\cdot\text{s}^{-1}]$
  * $y$ : 有因次經向座標 (Dimensional meridional coordinate) $[\text{m}]$
  * $\hat{y}$ : 無因次經向座標 (Dimensionless meridional coordinate) $[\text{無單位}]$
  * $\epsilon$ : Lamb 參數 (Lamb's parameter) $[\text{無單位}]$，$\epsilon \approx 507.3$
  * $\bar{c}$ : 等效重力波速 (Equivalent gravity wave speed) $[\text{m}\cdot\text{s}^{-1}]$
  * 註：本卡片用到 $\bar{c} = \dfrac{2\Omega a}{\epsilon^{1/2}}$，這是【已知 2】Lamb 參數定義 $\epsilon = \dfrac{4\Omega^{2}a^{2}}{\bar{c}^{2}}$ 的直接改寫。

+++

## 證明:

### (a) proof 本徵函數的顯式形式 (Explicit form of the eigenfunctions)

三個分量各自把【推導 1】的記法換算與【推導 2】的函數換算代進【已知 1】，整體常數依【假設 1】重新命名為 $A_{mnr}$。

* **第一分量：**

$$\begin{gather*}
\hat{u} &\overset{\text{已知 1(b)}}{=}& -A\left[\frac{1}{2}\left(\omega + k\right)H_{n+1}\,e^{-\hat{y}^{2}/2} + n\left(\omega - k\right)H_{n-1}\,e^{-\hat{y}^{2}/2}\right] \\
\hat{u} &\overset{\text{推導 1(a)(b)}}{=}& -A\,\epsilon^{-1/4}\left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\frac{1}{2}H_{n+1}\,e^{-\hat{y}^{2}/2} + \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)n\,H_{n-1}\,e^{-\hat{y}^{2}/2}\right] \\
\hat{u} &\overset{\text{推導 2(a)(b)}}{=}& -\frac{A\,\epsilon^{-1/4}}{c_n}\left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right] \\
U_{mnr} &\overset{\text{假設 1}}{=}& A_{mnr}\,\epsilon^{1/4}\left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]
\end{gather*}$$

* **第二分量：**

$$\begin{gather*}
\hat{v} &\overset{\text{已知 1(a)}}{=}& i\left(\omega^{2} - k^{2}\right)A\,H_n\,e^{-\hat{y}^{2}/2} \\
\hat{v} &\overset{\text{推導 1(c),推導 2(c)}}{=}& \frac{i\,A\,\epsilon^{-1/2}}{c_n}\left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)\mathcal{H}_n \\
V_{mnr} &\overset{\text{假設 1}}{=}& -i\,A_{mnr}\left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)\mathcal{H}_n
\end{gather*}$$

* **第三分量：**

$$\begin{gather*}
\hat{\phi} &\overset{\text{已知 1(c)}}{=}& -A\left[\frac{1}{2}\left(\omega + k\right)H_{n+1}\,e^{-\hat{y}^{2}/2} - n\left(\omega - k\right)H_{n-1}\,e^{-\hat{y}^{2}/2}\right] \\
\hat{\phi} &\overset{\text{推導 1(a)(b),推導 2(a)(b)}}{=}& -\frac{A\,\epsilon^{-1/4}}{c_n}\left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right] \\
\Phi_{mnr} &\overset{\text{假設 1}}{=}& \bar{c}\,A_{mnr}\,\epsilon^{1/4}\left[\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]
\end{gather*}$$

### (b) proof 歸一化常數（$n \ge 0$）(Normalization constant for $n \ge 0$)

把【推導 3】的三個範數加起來令其為 $1$，再用【推導 4】展開。

$$\begin{gather*}
1 &\overset{\text{let}}{=}& \left(\mathbf{K}_{mnr},\ \mathbf{K}_{mnr}\right) \\
1 &\overset{\text{已知 5(a)}}{=}& \int_{-\infty}^{\infty}\left[\left|U_{mnr}\right|^{2} + \left|V_{mnr}\right|^{2} + \frac{1}{\bar{c}^{2}}\left|\Phi_{mnr}\right|^{2}\right]d\hat{y} \\
1 &\overset{\text{推導 3(a)(b)(c)}}{=}& A_{mnr}^{2}\left[2\epsilon^{1/2}\left(\mathcal{P}_{mnr}^{2} + \mathcal{M}_{mnr}^{2}\right) + \left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)^{2}\right] \\
1 &\overset{\text{推導 4}}{=}& A_{mnr}^{2}\left[\epsilon^{1/2}\left(n+1\right)\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)^{2} + \epsilon^{1/2}n\left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)^{2} + \left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)^{2}\right] \\
A_{mnr} &=& \left[\epsilon^{1/2}\left(n+1\right)\left(\epsilon^{1/2}\hat{\nu}_{mnr} + m\right)^{2} + \epsilon^{1/2}n\left(\epsilon^{1/2}\hat{\nu}_{mnr} - m\right)^{2} + \left(\epsilon\hat{\nu}_{mnr}^{2} - m^{2}\right)^{2}\right]^{-1/2}
\end{gather*}$$

### (c) proof Kelvin 波的歸一化常數 (Normalization constant for the Kelvin wave)

Kelvin 波只有兩個非零分量，且兩者的貢獻**恰好相等**，故總範數是單一高斯積分的兩倍。

$$\begin{gather*}
1 &\overset{\text{let}}{=}& \left(\mathbf{K}_{m,-1,2},\ \mathbf{K}_{m,-1,2}\right) \\
1 &\overset{\text{已知 2(c),已知 5(a)}}{=}& A_{m,-1,2}^{2}\int_{-\infty}^{\infty}\left[e^{-\hat{y}^{2}} + 0 + \frac{1}{\bar{c}^{2}}\bar{c}^{2}e^{-\hat{y}^{2}}\right]d\hat{y} \\
1 &=& 2A_{m,-1,2}^{2}\int_{-\infty}^{\infty}e^{-\hat{y}^{2}}\,d\hat{y} \\
1 &\overset{\text{已知 6}}{=}& 2A_{m,-1,2}^{2}\,\pi^{1/2} \\
A_{m,-1,2} &=& \left(2\pi^{1/2}\right)^{-1/2} \\
A_{m,-1,2} &=& 2^{-1/2}\pi^{-1/4}
\end{gather*}$$

### (d) proof 正交歸一性 (Orthonormality)

歸一部分由【證明 (b)(c)】給出，正交部分由反厄米性給出。

$$\left(\mathbf{K}_{mnr},\ \mathbf{K}_{mn'r'}\right) \overset{\text{證明 (b)(c),已知 5(b),假設 2}}{=}
\begin{cases}
1, & \left(n', r'\right) = \left(n, r\right) \\
0, & \left(n', r'\right) \neq \left(n, r\right)
\end{cases}$$

### (e) proof 緯向對稱羅斯貝模態的本徵函數 (Eigenfunctions of the zonally symmetric Rossby modes)

$m = 0$、$\hat{\nu}_{0n0} = 0$ 時【證明 (a)】變成 $0/0$ 的不定式。把 $m$ 當連續變數取極限，共同因子 $\dfrac{2m\left[n\left(n+1\right)\right]^{1/2}}{2n+1}$ 被【假設 1】的規範自由度吸收掉。

* **第一分量：**

$$\begin{gather*}
U_{0n0} &\overset{\text{證明 (a),假設 3}}{=}& \lim_{m \to 0}A_{0n0}\,\epsilon^{1/4}\left[\left(\epsilon^{1/2}\hat{\nu}_{0n0} + m\right)\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\epsilon^{1/2}\hat{\nu}_{0n0} - m\right)\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right] \\
&\overset{\text{推導 5(b)(c)}}{=}& \lim_{m \to 0}A_{0n0}\,\epsilon^{1/4}\left[\frac{2nm}{2n+1}\left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n+1} - \frac{\left(2n+2\right)m}{2n+1}\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n-1}\right] \\
&\overset{\text{推導 6(a)(b)}}{=}& \lim_{m \to 0}A_{0n0}\,\epsilon^{1/4}\frac{2m\left[n\left(n+1\right)\right]^{1/2}}{2n+1}\left[\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}\right] \\
&\overset{\text{假設 1}}{=}& C_n\left[\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]
\end{gather*}$$

* **第二分量：**

$$\begin{gather*}
V_{0n0} &\overset{\text{證明 (a),假設 3}}{=}& \lim_{m \to 0}\left(-i\right)A_{0n0}\left(\epsilon\hat{\nu}_{0n0}^{2} - m^{2}\right)\mathcal{H}_n \\
&\overset{\text{推導 5(d)}}{=}& 0
\end{gather*}$$

* **第三分量：**

$$\begin{gather*}
\Phi_{0n0} &\overset{\text{證明 (a),推導 5(b)(c),推導 6(a)(b)}}{=}& \lim_{m \to 0}\bar{c}\,A_{0n0}\,\epsilon^{1/4}\frac{2m\left[n\left(n+1\right)\right]^{1/2}}{2n+1}\left[\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}\right] \\
&\overset{\text{假設 1}}{=}& \bar{c}\,C_n\left[\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]
\end{gather*}$$

* **歸一化常數：**

$$\begin{gather*}
1 &\overset{\text{let}}{=}& \left(\mathbf{K}_{0n0},\ \mathbf{K}_{0n0}\right) \\
1 &\overset{\text{已知 5(a)}}{=}& C_n^{2}\int_{-\infty}^{\infty}\left[\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]^{2}d\hat{y} + C_n^{2}\int_{-\infty}^{\infty}\left[\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]^{2}d\hat{y} \\
1 &\overset{\text{已知 4}}{=}& C_n^{2}\left[\frac{n}{2} + \frac{n+1}{2}\right] + C_n^{2}\left[\frac{n}{2} + \frac{n+1}{2}\right] \\
1 &=& C_n^{2}\left(2n + 1\right) \\
C_n &=& \left(2n + 1\right)^{-1/2}
\end{gather*}$$

### (f) verify 緯向對稱模態即地轉平衡緯向流 (Zonally symmetric modes are geostrophically balanced zonal flows)

【已知 7】在 $\nu_{0n0} = 0$、$V_{0n0} = 0$ 時退化成地轉平衡。【推導 7】與【推導 8】的結果**恰好互為相反數**，故兩者相加為零。

$$\begin{gather*}
\beta y\,U_{0n0} + \frac{d\Phi_{0n0}}{dy}
&\overset{\text{已知 7,證明 (e),推導 9}}{=}& \frac{2\Omega\,C_n}{\epsilon^{1/4}}\left\{\hat{y}\left[\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} - \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}\right] + \frac{d}{d\hat{y}}\left[\left(\frac{n}{2}\right)^{1/2}\mathcal{H}_{n+1} + \left(\frac{n+1}{2}\right)^{1/2}\mathcal{H}_{n-1}\right]\right\} \\
&\overset{\text{推導 7,推導 8}}{=}& \frac{2\Omega\,C_n}{\epsilon^{1/4}}\cdot 0 \\
&=& 0
\end{gather*}$$

+++

## 結構解釋

### 為什麼 project2_1 的 $\frac{1}{2}$ 與 $n$ 會變成兩個對稱的根號

【推導 2】是本篇最精巧的一步。在 $H_n$ 的世界裡，遞迴係數是**不對稱**的 $\frac{1}{2}$ 與 $n$；換成 $\mathcal{H}_n$ 之後，兩者變成**對稱**的 $\left(\frac{n+1}{2}\right)^{1/2}$ 與 $\left(\frac{n}{2}\right)^{1/2}$。

這不是巧合。歸一化常數 $c_n = \left(\pi^{1/2}2^{n}n!\right)^{-1/2}$ 就是**專門為了製造這個對稱性**而挑的（見 [Hermite Functions and Recurrence](../Differential_Equations/Hermite_Functions_and_Recurrence.md) 的結構解釋）。而這個對稱性正是【推導 3】(a)(b) 兩個分量的範數**恰好相等**、進而【證明 (b)】的 $A_{mnr}$ 能寫得這麼緊湊的原因。

### 動能與位能為什麼各佔一半

【推導 3】(a)(b) 算出來的兩個結果**完全相同**：

$$\int\left|U_{mnr}\right|^{2}d\hat{y} = \frac{1}{\bar{c}^{2}}\int\left|\Phi_{mnr}\right|^{2}d\hat{y} = A_{mnr}^{2}\epsilon^{1/2}\left[\mathcal{P}_{mnr}^{2} + \mathcal{M}_{mnr}^{2}\right]$$

這是**能量均分**：對每一個赤道波模態，「緯向動能」與「位能」的貢獻嚴格相等。第二分量（經向動能）則另計。

Kelvin 波是這件事最乾淨的例子 —— 【證明 (c)】裡 $U$ 與 $\Phi/\bar{c}$ **逐點相等**，所以總範數就是單一高斯積分的兩倍，$A_{m,-1,2} = 2^{-1/2}\pi^{-1/4}$ 中的 $2^{-1/2}$ 正是這「兩倍」的平方根。

### 簡併特例的物理

【證明 (e)】的 $\mathbf{K}_{0n0}$ 有兩個特徵：

1. **$V_{0n0} = 0$** —— 緯向對稱的模態沒有經向風。這符合直覺：$m = 0$ 表示場不隨經度變化，沒有緯向壓力梯度，也就沒有驅動經向運動的力。
2. **$\nu_{0n0} = 0$** —— 頻率為零，**不傳播**。

【證明 (f)】把兩者合起來解釋清楚：這些模態就是**定常的地轉平衡緯向噴流**。$\beta y\,U + \dfrac{d\Phi}{dy} = 0$ 是赤道 $\beta$ 平面版的地轉關係（$f \to \beta y$）。既然是地轉平衡的定常態，當然不振盪，頻率自然為零。

**這也解釋了為什麼會簡併**：所有 $n$ 的緯向對稱羅斯貝模態頻率都是零，因此【已知 5】(b) 的「相異本徵值 ⟹ 正交」用不上。所幸它們的正交性可以由【已知 4】的 $\mathcal{H}_n$ 正交性**直接驗證**（見【證明 (e)】的歸一化計算，交叉項全部落在不同階的 $\mathcal{H}$ 上）。

### 這一組基底之後怎麼用

【證明 (d)】的正交歸一性讓下面這件事成為可能：任何一個場 $\hat{\boldsymbol{\eta}}_m(\hat{y})$ 都可以展開成

$$\hat{\boldsymbol{\eta}}_m = \sum_{n = -1}^{\infty}\sum_{r}\hat{\eta}_{mnr}\mathbf{K}_{mnr}, \qquad \hat{\eta}_{mnr} = \left(\hat{\boldsymbol{\eta}}_m,\ \mathbf{K}_{mnr}\right)$$

**取係數只要做一次內積，不必解聯立方程**。這正是 [受迫解](Forced_Response_of_Equatorial_Modes.md) 能把常微分方程壓成一行除法的全部本錢。
